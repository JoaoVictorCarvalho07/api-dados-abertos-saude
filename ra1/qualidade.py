import pandas as pd

from config import (
    ANO_REFERENCIA,
    ATRASO_EXTREMO_DIAS,
    CHAVE_POSSIVEL_DUPLICATA,
    FIM_PERIODO_VALIDO,
    IDADE_MAXIMA,
    INICIO_PERIODO_VALIDO,
    PASTA_SAIDAS,
)
from dominios import (
    CLASSIFICACAO_FINAL,
    CODIGOS_SIM_NAO_IGNORADO,
    GESTANTE_EM_GESTACAO,
    SEXO,
    UF_POR_CODIGO,
    UNIDADE_IDADE_EM_ANOS,
)
from ingestao import carregar_bruto
from relatorio import salvar, tabela


def colunas_de_data(df):
    return [c for c in df.columns if c.startswith("DT_")]


def converter_datas(bruto):
    return bruto[colunas_de_data(bruto)].apply(pd.to_datetime, errors="coerce", format="%Y-%m-%d")


def idade_declarada_em_anos(bruto):
    codigo = bruto["NU_IDADE_N"].astype("string")
    unidade = codigo.str[0]
    valor = pd.to_numeric(codigo.str[1:], errors="coerce")
    return unidade, valor * unidade.map(UNIDADE_IDADE_EM_ANOS).astype("float")


class Diagnostico:
    def __init__(self, total_registros):
        self.total = total_registros
        self.itens = []

    def registrar(self, campo, regra, afetados, observacao="", unidade="registros"):
        denominador = self.total if unidade == "registros" else None
        self.itens.append(
            {
                "ID": f"Q{len(self.itens) + 1}",
                "Campo": campo,
                "Verificação e regra": regra,
                "Afetados": int(afetados),
                "Unidade": unidade,
                "% do total": f"{afetados / denominador:.2%}" if denominador else "-",
                "Observação": observacao,
            }
        )

    def tabela(self):
        return pd.DataFrame(self.itens)


def diagnosticar(bruto):
    d = Diagnostico(len(bruto))
    datas = converter_datas(bruto)

    vazias = [c for c in bruto.columns if bruto[c].isna().all()]
    d.registrar("todas", "Colunas 100% vazias", len(vazias), ", ".join(vazias), unidade="colunas")

    constantes = [c for c in bruto.columns if bruto[c].notna().all() and bruto[c].nunique() == 1]
    d.registrar("todas", "Colunas com um único valor", len(constantes), ", ".join(constantes), unidade="colunas")

    exatas = bruto.duplicated().sum()
    d.registrar("todas", "Linhas duplicadas por completo", exatas)

    por_chave = bruto.duplicated(CHAVE_POSSIVEL_DUPLICATA).sum() - exatas
    d.registrar(
        "+".join(CHAVE_POSSIVEL_DUPLICATA),
        "Possíveis duplicatas: mesma pessoa, local e datas, mas linha não idêntica",
        por_chave,
        "Sem identificador de paciente, não é possível confirmar",
    )

    nao_convertidas = sum(int((bruto[c].notna() & datas[c].isna()).sum()) for c in datas.columns)
    d.registrar("DT_*", "Datas que não seguem o formato AAAA-MM-DD", nao_convertidas, unidade="valores")

    fora = (datas < INICIO_PERIODO_VALIDO) | (datas > FIM_PERIODO_VALIDO)
    por_coluna = fora.sum()
    d.registrar(
        "DT_*",
        f"Registros com alguma data fora de {INICIO_PERIODO_VALIDO.date()} a {FIM_PERIODO_VALIDO.date()}",
        fora.any(axis=1).sum(),
        ", ".join(f"{c}: {n}" for c, n in por_coluna[por_coluna > 0].sort_values(ascending=False).items()),
    )

    d.registrar("DT_SIN_PRI, DT_NOTIFIC", "Início dos sintomas depois da notificação", (datas.DT_SIN_PRI > datas.DT_NOTIFIC).sum())
    d.registrar("DT_DIGITA, DT_NOTIFIC", "Digitação antes da notificação", (datas.DT_DIGITA < datas.DT_NOTIFIC).sum())
    d.registrar("DT_ENCERRA, DT_NOTIFIC", "Encerramento antes da notificação", (datas.DT_ENCERRA < datas.DT_NOTIFIC).sum())

    atraso = (datas.DT_NOTIFIC - datas.DT_SIN_PRI).dt.days
    d.registrar(
        "DT_SIN_PRI, DT_NOTIFIC",
        f"Atraso entre sintomas e notificação acima de {ATRASO_EXTREMO_DIAS} dias (outlier)",
        (atraso > ATRASO_EXTREMO_DIAS).sum(),
        f"mediana {atraso.median():.0f} dias, p99 {atraso.quantile(0.99):.0f}, máximo {atraso.max():.0f}",
    )

    classi = bruto["CLASSI_FIN"]
    invalidos = classi.notna() & ~classi.isin(list(CLASSIFICACAO_FINAL))
    d.registrar(
        "CLASSI_FIN",
        "Código fora do domínio do dicionário",
        invalidos.sum(),
        ", ".join(f"'{v}': {n}" for v, n in classi[invalidos].value_counts().items()),
    )
    d.registrar("CLASSI_FIN", "Sem classificação final (caso em investigação)", classi.isna().sum())

    zero_por_uf = (
        pd.DataFrame({"uf": bruto["SG_UF_NOT"].map(UF_POR_CODIGO), "zero": classi == "0"})
        .groupby("uf")["zero"].mean()
    )
    zero_por_uf = zero_por_uf[zero_por_uf > 0].sort_values(ascending=False)
    d.registrar(
        "CLASSI_FIN, SG_UF_NOT",
        "Uso de '0' no lugar de vazio concentrado por UF",
        (classi == "0").sum(),
        f"{len(zero_por_uf)} UF(s) usam '0': " + ", ".join(f"{uf} ({p:.1%} das notificações da UF)" for uf, p in zero_por_uf.items()),
    )

    unidade, idade = idade_declarada_em_anos(bruto)
    d.registrar("NU_IDADE_N", "Idade vazia ou com unidade fora de 1 a 4", (~unidade.isin(list(UNIDADE_IDADE_EM_ANOS)) | idade.isna()).sum())
    d.registrar("NU_IDADE_N", f"Idade acima de {IDADE_MAXIMA} anos", (idade > IDADE_MAXIMA).sum())

    pela_data = ANO_REFERENCIA - pd.to_numeric(bruto["ANO_NASC"], errors="coerce")
    divergente = (unidade == "4") & ((idade - pela_data).abs() > 1)
    d.registrar("NU_IDADE_N, ANO_NASC", "Idade diverge do ano de nascimento em mais de 1 ano", divergente.sum())

    sexo = bruto["CS_SEXO"]
    d.registrar(
        "CS_SEXO",
        "Sexo ignorado, vazio ou fora do domínio M/F",
        (~sexo.isin(["M", "F"])).sum(),
        ", ".join(f"'{v}': {n}" for v, n in sexo[~sexo.isin(["M", "F"])].fillna("<vazio>").value_counts().items()),
    )
    d.registrar("CS_SEXO, CS_GESTANT", "Sexo masculino marcado como gestante", ((sexo == "M") & bruto["CS_GESTANT"].isin(list(GESTANTE_EM_GESTACAO))).sum())

    for campo in ["DIABETES", "HIPERTENSA"]:
        valor = bruto[campo]
        sem_informacao = valor.isna() | (valor == "9") | ~valor.isin(list(CODIGOS_SIM_NAO_IGNORADO))
        d.registrar(
            campo,
            "Comorbidade sem informação útil (vazio, 9 = ignorado ou fora do domínio)",
            sem_informacao.sum(),
            ", ".join(f"'{v}': {n}" for v, n in valor[sem_informacao].fillna("<vazio>").value_counts().items()),
        )

    d.registrar("HOSPITALIZ, DT_INTERNA", "Hospitalizado sem data de internação", ((bruto["HOSPITALIZ"] == "1") & datas.DT_INTERNA.isna()).sum())

    uf_residencia = bruto["SG_UF"]
    d.registrar("SG_UF", "UF de residência vazia ou com código inexistente", (~uf_residencia.isin(list(UF_POR_CODIGO))).sum())

    return d.tabela()


def main():
    bruto = carregar_bruto()
    diagnostico = diagnosticar(bruto)
    print(diagnostico.drop(columns="Observação").to_string(index=False))
    destino = salvar(
        "02_diagnostico_qualidade.md",
        "RA1 — Diagnóstico de qualidade",
        [
            ("Base avaliada", f"{len(bruto):,} notificações x {bruto.shape[1]} colunas, como vieram do arquivo bruto.".replace(",", ".")),
            ("Verificações", tabela(diagnostico)),
            (
                "Pendência",
                "Os domínios de código usados nas regras seguem o dicionário de dados do SINAN "
                "(`dic_dados_dengue.pdf`) e devem ser conferidos pelo grupo no documento oficial.",
            ),
        ],
    )
    diagnostico.to_csv(PASTA_SAIDAS / "02_diagnostico_qualidade.csv", index=False)
    print("Relatório:", destino)


if __name__ == "__main__":
    main()
