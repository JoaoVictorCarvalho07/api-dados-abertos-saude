import numpy as np
import pandas as pd

from config import (
    ANO_REFERENCIA,
    ARQUIVO_PREPARADO,
    ATRASO_EXTREMO_DIAS,
    CHAVE_POSSIVEL_DUPLICATA,
    FIM_PERIODO_VALIDO,
    IDADE_MAXIMA,
    INICIO_PERIODO_VALIDO,
)
from dominios import (
    CLASSIFICACAO_FINAL,
    CLASSIFICACOES_COM_GRAVIDADE,
    CLASSIFICACOES_GRAVES,
    CRITERIO_CONFIRMACAO,
    EVOLUCAO,
    FAIXAS_ETARIAS,
    REGIAO_POR_PRIMEIRO_DIGITO,
    ROTULOS_FAIXAS_ETARIAS,
    SIM_NAO_IGNORADO,
    UF_POR_CODIGO,
)
from ingestao import carregar_bruto
from qualidade import idade_declarada_em_anos
from relatorio import salvar, tabela

COLUNAS_ORIGEM = [
    "DT_NOTIFIC", "DT_SIN_PRI", "SEM_PRI",
    "SG_UF_NOT", "ID_MUNICIP", "SG_UF", "ID_MN_RESI",
    "CS_SEXO", "NU_IDADE_N", "ANO_NASC",
    "CLASSI_FIN", "CRITERIO", "HOSPITALIZ", "EVOLUCAO",
    "DIABETES", "HIPERTENSA",
]

SEM_CLASSIFICACAO = "Sem classificação"
SEXO_INFORMADO = {"M": "Masculino", "F": "Feminino"}
EVOLUCAO_INFORMADA = {codigo: rotulo for codigo, rotulo in EVOLUCAO.items() if codigo != "9"}

DICIONARIO_PREPARADO = [
    ("id_registro", "posição da linha no arquivo bruto", "rastreabilidade até o DENGBR26"),
    ("dt_notificacao", "DT_NOTIFIC", "data da notificação"),
    ("dt_sintomas", "DT_SIN_PRI", "data de início dos sintomas; vazia quando inválida"),
    ("semana_epi_sintomas", "SEM_PRI", "semana epidemiológica dos sintomas (AAAASS)"),
    ("mes_sintomas", "derivada de dt_sintomas", "AAAA-MM"),
    ("uf_notificacao", "SG_UF_NOT", "sigla da UF onde o caso foi notificado"),
    ("regiao_notificacao", "SG_UF_NOT", "região da UF de notificação"),
    ("municipio_notificacao", "ID_MUNICIP", "código IBGE (6 dígitos)"),
    ("uf_residencia", "SG_UF", "sigla da UF de residência"),
    ("regiao_residencia", "SG_UF", "região da UF de residência"),
    ("municipio_residencia", "ID_MN_RESI", "código IBGE (6 dígitos)"),
    ("sexo", "CS_SEXO", "Masculino / Feminino; vazio quando ignorado"),
    ("idade_anos", "NU_IDADE_N, ANO_NASC", f"anos completos, 0 a {IDADE_MAXIMA}"),
    ("faixa_etaria", "derivada de idade_anos", ", ".join(ROTULOS_FAIXAS_ETARIAS)),
    ("classificacao_final", "CLASSI_FIN", ", ".join(list(CLASSIFICACAO_FINAL.values()) + [SEM_CLASSIFICACAO])),
    ("caso_grave", "derivada de CLASSI_FIN", "verdadeiro para 11 e 12, falso para 10, vazio nas demais"),
    ("criterio_confirmacao", "CRITERIO", ", ".join(CRITERIO_CONFIRMACAO.values())),
    ("hospitalizado", "HOSPITALIZ", "verdadeiro / falso; vazio quando ignorado"),
    ("evolucao", "EVOLUCAO", ", ".join(EVOLUCAO_INFORMADA.values())),
    ("diabetes", "DIABETES", "verdadeiro / falso; vazio quando ignorado"),
    ("hipertensao", "HIPERTENSA", "verdadeiro / falso; vazio quando ignorado"),
    ("atraso_notificacao_dias", "DT_NOTIFIC - DT_SIN_PRI", "dias, mantidos inclusive os extremos"),
    ("dt_sintomas_invalida", "derivada", "verdadeiro quando DT_SIN_PRI foi descartada"),
    ("possivel_duplicata", "derivada", "verdadeiro quando outra linha tem a mesma chave"),
]


def data_no_periodo(coluna):
    data = pd.to_datetime(coluna, errors="coerce", format="%Y-%m-%d")
    return data.where(data.between(INICIO_PERIODO_VALIDO, FIM_PERIODO_VALIDO))


def uf_e_regiao(codigo):
    uf = codigo.map(UF_POR_CODIGO)
    regiao = codigo.str[0].map(REGIAO_POR_PRIMEIRO_DIGITO).where(uf.notna())
    return uf, regiao


def sim_nao(coluna):
    return coluna.map(SIM_NAO_IGNORADO).astype("boolean")


def idade_em_anos(origem):
    _, declarada = idade_declarada_em_anos(origem)
    declarada = declarada.where(declarada.between(0, IDADE_MAXIMA))
    pelo_nascimento = ANO_REFERENCIA - pd.to_numeric(origem["ANO_NASC"], errors="coerce")
    pelo_nascimento = pelo_nascimento.where(pelo_nascimento.between(0, IDADE_MAXIMA))
    return np.floor(declarada.fillna(pelo_nascimento)).astype("Int64")


def preparar(bruto):
    sem_duplicatas = bruto.drop_duplicates()
    origem = sem_duplicatas[COLUNAS_ORIGEM]

    notificacao = data_no_periodo(origem["DT_NOTIFIC"])
    sintomas = data_no_periodo(origem["DT_SIN_PRI"])
    sintomas_invalidos = origem["DT_SIN_PRI"].notna() & (sintomas.isna() | (sintomas > notificacao))
    sintomas = sintomas.where(~sintomas_invalidos)

    classificacao = origem["CLASSI_FIN"].where(origem["CLASSI_FIN"].isin(list(CLASSIFICACAO_FINAL)))
    uf_residencia, regiao_residencia = uf_e_regiao(origem["SG_UF"])
    uf_notificacao, regiao_notificacao = uf_e_regiao(origem["SG_UF_NOT"])
    idade = idade_em_anos(origem)

    preparado = pd.DataFrame(
        {
            "id_registro": pd.Series(origem.index, index=origem.index),
            "dt_notificacao": notificacao,
            "dt_sintomas": sintomas,
            "semana_epi_sintomas": origem["SEM_PRI"],
            "mes_sintomas": sintomas.dt.strftime("%Y-%m"),
            "uf_notificacao": uf_notificacao,
            "regiao_notificacao": regiao_notificacao,
            "municipio_notificacao": origem["ID_MUNICIP"],
            "uf_residencia": uf_residencia,
            "regiao_residencia": regiao_residencia,
            "municipio_residencia": origem["ID_MN_RESI"],
            "sexo": origem["CS_SEXO"].map(SEXO_INFORMADO),
            "idade_anos": idade,
            "faixa_etaria": pd.cut(idade.astype("float"), bins=FAIXAS_ETARIAS, right=False, labels=ROTULOS_FAIXAS_ETARIAS),
            "classificacao_final": classificacao.map(CLASSIFICACAO_FINAL).fillna(SEM_CLASSIFICACAO),
            "caso_grave": classificacao.isin(list(CLASSIFICACOES_GRAVES)).where(classificacao.isin(list(CLASSIFICACOES_COM_GRAVIDADE))).astype("boolean"),
            "criterio_confirmacao": origem["CRITERIO"].map(CRITERIO_CONFIRMACAO),
            "hospitalizado": sim_nao(origem["HOSPITALIZ"]),
            "evolucao": origem["EVOLUCAO"].map(EVOLUCAO_INFORMADA),
            "diabetes": sim_nao(origem["DIABETES"]),
            "hipertensao": sim_nao(origem["HIPERTENSA"]),
            "atraso_notificacao_dias": (notificacao - sintomas).dt.days.astype("Int64"),
            "dt_sintomas_invalida": sintomas_invalidos.astype("boolean"),
            "possivel_duplicata": sem_duplicatas.duplicated(CHAVE_POSSIVEL_DUPLICATA, keep=False).astype("boolean"),
        }
    ).reset_index(drop=True)

    textos = ["semana_epi_sintomas", "mes_sintomas", "municipio_notificacao", "municipio_residencia"]
    categorias = [
        "uf_notificacao", "regiao_notificacao", "uf_residencia", "regiao_residencia",
        "sexo", "classificacao_final", "criterio_confirmacao", "evolucao",
    ]
    preparado[textos] = preparado[textos].astype("string")
    preparado[categorias] = preparado[categorias].astype("category")
    return preparado


def validar(bruto, preparado):
    esperado = len(bruto) - bruto.duplicated().sum()
    sintomas = preparado["dt_sintomas"]
    idade = preparado["idade_anos"]
    classificacoes = set(CLASSIFICACAO_FINAL.values()) | {SEM_CLASSIFICACAO}
    com_gravidade = preparado["classificacao_final"].isin([CLASSIFICACAO_FINAL[c] for c in CLASSIFICACOES_COM_GRAVIDADE])
    regras = [
        ("Registros = bruto menos duplicatas exatas", len(preparado) == esperado),
        ("id_registro único", preparado["id_registro"].is_unique),
        ("dt_notificacao preenchida e dentro do período", preparado["dt_notificacao"].between(INICIO_PERIODO_VALIDO, FIM_PERIODO_VALIDO).all()),
        ("dt_sintomas vazia ou dentro do período", (sintomas.isna() | sintomas.between(INICIO_PERIODO_VALIDO, FIM_PERIODO_VALIDO)).all()),
        ("dt_sintomas nunca depois da notificação", ~(sintomas > preparado["dt_notificacao"]).any()),
        ("Atraso de notificação nunca negativo", ~(preparado["atraso_notificacao_dias"] < 0).any()),
        (f"idade_anos vazia ou entre 0 e {IDADE_MAXIMA}", (idade.isna() | idade.between(0, IDADE_MAXIMA)).all()),
        ("faixa_etaria vazia só quando idade_anos vazia", (preparado["faixa_etaria"].isna() == idade.isna()).all()),
        ("classificacao_final dentro do domínio", preparado["classificacao_final"].isin(classificacoes).all()),
        ("caso_grave preenchido só nas classificações 10, 11 e 12", (preparado["caso_grave"].notna() == com_gravidade).all()),
        ("uf_residencia vazia ou uma das 27 UFs", (preparado["uf_residencia"].isna() | preparado["uf_residencia"].isin(UF_POR_CODIGO.values())).all()),
        ("sexo vazio ou Masculino / Feminino", (preparado["sexo"].isna() | preparado["sexo"].isin(SEXO_INFORMADO.values())).all()),
    ]
    return pd.DataFrame(regras, columns=["Regra", "Passou"])


def antes_e_depois(bruto, preparado):
    datas_sintomas = pd.to_datetime(bruto["DT_SIN_PRI"], errors="coerce", format="%Y-%m-%d")
    datas_notificacao = pd.to_datetime(bruto["DT_NOTIFIC"], errors="coerce", format="%Y-%m-%d")
    sintomas_invalidos = bruto["DT_SIN_PRI"].notna() & (
        ~datas_sintomas.between(INICIO_PERIODO_VALIDO, FIM_PERIODO_VALIDO) | (datas_sintomas > datas_notificacao)
    )
    _, idade_declarada = idade_declarada_em_anos(bruto)
    classi = bruto["CLASSI_FIN"]

    def pct(serie):
        return f"{serie.mean():.2%}"

    linhas = [
        ("Registros", len(bruto), len(preparado), "Remoção das duplicatas exatas (D1)"),
        ("Atributos", bruto.shape[1], preparado.shape[1], "Seleção das colunas usadas por P1–P3 e derivadas (D2, D11)"),
        ("Duplicatas exatas", int(bruto.duplicated().sum()), int(preparado["id_registro"].duplicated().sum()), "D1; no preparado, medido por id_registro repetido"),
        ("Data de sintomas inválida", int(sintomas_invalidos.sum()), 0, f"Esvaziadas e sinalizadas em dt_sintomas_invalida: {int(preparado['dt_sintomas_invalida'].sum())} (D4)"),
        ("CLASSI_FIN fora do domínio", int((classi.notna() & ~classi.isin(list(CLASSIFICACAO_FINAL))).sum()), 0, "Agrupadas em 'Sem classificação' (D6)"),
        ("Idade inutilizável", int((idade_declarada.isna() | ~idade_declarada.between(0, IDADE_MAXIMA)).sum()), int(preparado["idade_anos"].isna().sum()), "Recuperada pelo ano de nascimento quando possível (D7)"),
        ("Sexo sem M/F", pct(~bruto["CS_SEXO"].isin(["M", "F"])), pct(preparado["sexo"].isna()), "Ignorado vira vazio (D8)"),
        ("Diabetes sem sim/não", pct(~bruto["DIABETES"].isin(["1", "2"])), pct(preparado["diabetes"].isna()), "9 e fora do domínio viram vazio (D9)"),
        ("Hipertensão sem sim/não", pct(~bruto["HIPERTENSA"].isin(["1", "2"])), pct(preparado["hipertensao"].isna()), "9 e fora do domínio viram vazio (D9)"),
        (f"Atraso > {ATRASO_EXTREMO_DIAS} dias", int(((datas_notificacao - datas_sintomas).dt.days > ATRASO_EXTREMO_DIAS).sum()), int((preparado["atraso_notificacao_dias"] > ATRASO_EXTREMO_DIAS).sum()), "Mantidos: valor extremo não justifica exclusão (D5)"),
        ("Linhas envolvidas em possível duplicata", "-", int(preparado["possivel_duplicata"].sum()), "Mantidas e sinalizadas; conta todas as linhas de cada grupo, inclusive a primeira (D10)"),
    ]
    return pd.DataFrame(linhas, columns=["Medida", "Após ingestão", "Após preparação", "Explicação"])


def decisoes(bruto, preparado):
    classi = bruto["CLASSI_FIN"]
    _, idade_declarada = idade_declarada_em_anos(bruto)
    idade_recuperada = int(((idade_declarada.isna() | ~idade_declarada.between(0, IDADE_MAXIMA)).sum()) - preparado["idade_anos"].isna().sum())
    linhas = [
        ("D1", "Q3", "Remover linhas duplicadas por completo", int(bruto.duplicated().sum()),
         "Linha idêntica nas 121 colunas é o mesmo registro repetido; mantê-la inflaria a contagem de casos (P1)."),
        ("D2", "Q1, Q2, Q8, Q9, Q18, Q21", f"Manter só as {len(COLUNAS_ORIGEM)} colunas usadas por P1–P3", bruto.shape[1] - len(COLUNAS_ORIGEM),
         "As perguntas não usam as demais; TP_NOT, ID_AGRAVO e NU_ANO são constantes. Problemas em colunas descartadas (DT_DIGITA, DT_ENCERRA, DT_INTERNA, CS_GESTANT) ficam registrados, sem tratamento."),
        ("D3", "Q5", "Converter tipos: datas, idade inteira, sim/não booleano, categorias", len(preparado),
         "Tudo foi lido como texto para não perder zeros nem inferir tipos errados; a conversão acontece aqui, com regra explícita."),
        ("D4", "Q6, Q7", "Esvaziar e sinalizar data de sintomas fora do período ou depois da notificação", int(preparado["dt_sintomas_invalida"].sum()),
         "Nenhum caso em 2026; a regra fica como proteção para reexecuções com o arquivo atualizado."),
        ("D5", "Q10", f"Manter atrasos acima de {ATRASO_EXTREMO_DIAS} dias", int((preparado["atraso_notificacao_dias"] > ATRASO_EXTREMO_DIAS).sum()),
         "Notificação tardia é plausível; valor extremo, por si só, não justifica exclusão."),
        ("D6", "Q11, Q12, Q13", "CLASSI_FIN '0' e vazio viram 'Sem classificação'", int((classi.isna() | ~classi.isin(list(CLASSIFICACAO_FINAL))).sum()),
         "'0' não existe no dicionário e só o ES o usa, como vazio. Esses casos ficam fora do denominador de gravidade (caso_grave vazio)."),
        ("D7", "Q14, Q15, Q16", "Idade em anos pela unidade do código; acima de 120 vira vazio; ano de nascimento como alternativa", idade_recuperada,
         "O código mistura unidade e valor (4026 = 26 anos). A coluna Afetados mostra as idades recuperadas pelo ano de nascimento."),
        ("D8", "Q17", "Sexo 'I' (ignorado) vira vazio", int((bruto["CS_SEXO"] == "I").sum()),
         "P2 compara homens e mulheres; 'ignorado' não informa e sai só dessa comparação."),
        ("D9", "Q19, Q20", "Comorbidades 9 (ignorado) e vazio viram vazio", int(preparado["diabetes"].isna().sum()),
         "A linha é mantida; a falta de informação só a exclui da análise de comorbidades (P3)."),
        ("D10", "Q4", "Manter e sinalizar possíveis duplicatas", int(bruto.drop_duplicates().duplicated(CHAVE_POSSIVEL_DUPLICATA).sum()),
         "Sem identificador de paciente, linhas parecidas podem ser pessoas diferentes; remover apagaria casos reais."),
        ("D11", "-", "Criar mes_sintomas, região, faixa_etaria, caso_grave e atraso_notificacao_dias", len(preparado),
         "Colunas derivadas que as perguntas exigem (mês e UF para P1, sexo e gravidade para P2, faixa etária e comorbidade para P3, atraso para o RA2)."),
    ]
    return pd.DataFrame(linhas, columns=["Decisão", "Relacionada a", "Ação", "Afetados", "Justificativa"])


def dicionario(preparado):
    tipos = preparado.dtypes.astype(str)
    return pd.DataFrame(
        [(nome, origem, tipos[nome], descricao) for nome, origem, descricao in DICIONARIO_PREPARADO],
        columns=["Atributo", "Origem", "Tipo", "Domínio / descrição"],
    )


def main():
    bruto = carregar_bruto()
    preparado = preparar(bruto)
    validacoes = validar(bruto, preparado)
    print(validacoes.to_string(index=False))
    if not validacoes["Passou"].all():
        raise SystemExit("Validação falhou; o arquivo preparado não foi gravado.")

    ARQUIVO_PREPARADO.parent.mkdir(parents=True, exist_ok=True)
    preparado.to_parquet(ARQUIVO_PREPARADO, index=False)
    relido = pd.read_parquet(ARQUIVO_PREPARADO)
    releitura_ok = relido.shape == preparado.shape and (relido.dtypes.astype(str) == preparado.dtypes.astype(str)).all()

    comparacao = antes_e_depois(bruto, preparado)
    print(comparacao.to_string(index=False))
    destino = salvar(
        "03_limpeza_e_resultado.md",
        "RA1 — Limpeza, preparação e conjunto resultante",
        [
            ("Arquivo gerado", f"`{ARQUIVO_PREPARADO.relative_to(ARQUIVO_PREPARADO.parents[2]).as_posix()}` — {len(preparado):,} linhas x {preparado.shape[1]} colunas, Parquet. Releitura idêntica: **{releitura_ok}**".replace(",", ".")),
            ("Registro das decisões", tabela(decisoes(bruto, preparado))),
            ("Comparação antes e depois", tabela(comparacao)),
            ("Validações após o tratamento", tabela(validacoes)),
            ("Dicionário do conjunto preparado", tabela(dicionario(preparado))),
        ],
    )
    print("Relatório:", destino)


if __name__ == "__main__":
    main()
