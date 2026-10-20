from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_PREPARADO = RAIZ / "dados" / "preparados" / "dengue_brasil_2026.parquet"

PASTA_STREAMING = RAIZ / "dados" / "streaming"
PASTA_ENTRADA = PASTA_STREAMING / "entrada"
PASTA_PUBLICACAO = PASTA_STREAMING / "publicacao"
PASTA_CHECKPOINT = PASTA_STREAMING / "checkpoint"
SINAL_CONSUMIDOR_PRONTO = PASTA_STREAMING / "consumidor_pronto"

FORMATO_DATA_HORA = "yyyy-MM-dd HH:mm:ss"
SEMENTE = 2026
INTERVALO_PADRAO_SEGUNDOS = 10

LOTES = [
    {"lote": 1, "chegada": "1ª", "dias": {"2026-10-05": 30}},
    {"lote": 2, "chegada": "2ª", "dias": {"2026-10-05": 20, "2026-10-06": 25}},
    {"lote": 3, "chegada": "3ª", "dias": {"2026-10-06": 15, "2026-10-07": 35}},
    {"lote": 4, "chegada": "4ª (atrasada)", "dias": {"2026-10-05": 10}},
]
