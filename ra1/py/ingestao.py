import urllib.request
import zipfile

import pandas as pd

from config import ARQUIVO_BRUTO, CODIFICACAO, SEPARADOR, URL_BRUTO
from relatorio import salvar, tabela


def garantir_arquivo_bruto():
    if not ARQUIVO_BRUTO.exists():
        urllib.request.urlretrieve(URL_BRUTO, ARQUIVO_BRUTO)
    return ARQUIVO_BRUTO


def carregar_bruto():
    return pd.read_csv(
        garantir_arquivo_bruto(),
        sep=SEPARADOR,
        encoding=CODIFICACAO,
        dtype="string[pyarrow]",
    )


def contar_linhas_de_dados():
    with zipfile.ZipFile(ARQUIVO_BRUTO) as pacote:
        interno = pacote.infolist()[0]
        with pacote.open(interno) as arquivo:
            linhas = sum(1 for _ in arquivo)
    return interno, linhas - 1


def resumo_da_ingestao(bruto):
    interno, linhas_no_arquivo = contar_linhas_de_dados()
    datas_notificacao = pd.to_datetime(bruto["DT_NOTIFIC"], errors="coerce")
    resumo = pd.DataFrame(
        [
            ("Arquivo", ARQUIVO_BRUTO.name),
            ("Conteúdo do zip", interno.filename),
            ("Tamanho compactado (MB)", round(ARQUIVO_BRUTO.stat().st_size / 1e6, 1)),
            ("Tamanho descompactado (MB)", round(interno.file_size / 1e6, 1)),
            ("Separador / codificação", f"'{SEPARADOR}' / {CODIFICACAO}"),
            ("Tipo usado na leitura", "texto (string[pyarrow]) em todas as colunas"),
            ("Linhas de dados no arquivo", linhas_no_arquivo),
            ("Linhas carregadas pelo pandas", len(bruto)),
            ("Colunas carregadas", bruto.shape[1]),
            ("Memória em uso (MB)", round(bruto.memory_usage(deep=True).sum() / 1e6, 1)),
            ("Primeira notificação", datas_notificacao.min().date()),
            ("Última notificação", datas_notificacao.max().date()),
        ],
        columns=["Item", "Valor"],
    )
    return resumo, linhas_no_arquivo == len(bruto)


def main():
    bruto = carregar_bruto()
    resumo, carregamento_completo = resumo_da_ingestao(bruto)
    print(resumo.to_string(index=False))
    print("Carregamento completo:", carregamento_completo)
    destino = salvar(
        "01_ingestao.md",
        "RA1 — Ingestão",
        [
            ("Resumo do carregamento", tabela(resumo)),
            (
                "Verificação do carregamento",
                f"Linhas no arquivo = linhas carregadas: **{carregamento_completo}**",
            ),
            ("Colunas do arquivo", ", ".join(f"`{c}`" for c in bruto.columns)),
        ],
    )
    print("Relatório:", destino)


if __name__ == "__main__":
    main()
