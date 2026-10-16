import sys
from pathlib import Path

import pandas as pd

ARQUIVO_BRUTO = Path("dados/brutos/DENGBR24.csv.zip")
PASTA_AMOSTRAS = Path("dados/amostras")
UF_PARANA = "41"


def primeiras_linhas_do_parana(quantidade):
    encontradas = []
    total = 0
    for parte in pd.read_csv(ARQUIVO_BRUTO, dtype="string", chunksize=50_000):
        parana = parte[parte["SG_UF_NOT"] == UF_PARANA]
        encontradas.append(parana)
        total += len(parana)
        if total >= quantidade:
            break
    return pd.concat(encontradas).head(quantidade)


if __name__ == "__main__":
    quantidade = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    PASTA_AMOSTRAS.mkdir(parents=True, exist_ok=True)
    destino = PASTA_AMOSTRAS / f"amostra_pr_{quantidade}.csv"
    primeiras_linhas_do_parana(quantidade).to_csv(destino, index=False, encoding="utf-8-sig")
    print(f"{quantidade} linhas salvas em {destino}")
