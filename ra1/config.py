from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent

URL_BRUTO = "https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SINAN/Dengue/csv/DENGBR26.csv.zip"
ARQUIVO_BRUTO = RAIZ / "DENGBR26.csv.zip"
SEPARADOR = ","
CODIFICACAO = "utf-8"

ARQUIVO_PREPARADO = RAIZ / "dados" / "preparados" / "dengue_brasil_2026.parquet"
PASTA_SAIDAS = RAIZ / "ra1" / "saidas"

INICIO_PERIODO_VALIDO = pd.Timestamp("2025-12-01")
FIM_PERIODO_VALIDO = pd.Timestamp("2026-10-10")
ANO_REFERENCIA = 2026
IDADE_MAXIMA = 120
ATRASO_EXTREMO_DIAS = 60

CHAVE_POSSIVEL_DUPLICATA = [
    "ID_MUNICIP",
    "ID_UNIDADE",
    "DT_NOTIFIC",
    "DT_SIN_PRI",
    "ANO_NASC",
    "NU_IDADE_N",
    "CS_SEXO",
    "ID_MN_RESI",
]
