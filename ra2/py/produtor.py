import argparse
import json
import time

import numpy as np
import pandas as pd

from config import (
    ARQUIVO_PREPARADO,
    INTERVALO_PADRAO_SEGUNDOS,
    LOTES,
    PASTA_ENTRADA,
    PASTA_PUBLICACAO,
    SEMENTE,
    SINAL_CONSUMIDOR_PRONTO,
)

ESPERA_MAXIMA_CONSUMIDOR_SEGUNDOS = 180


def carregar_casos_classificados():
    if not ARQUIVO_PREPARADO.exists():
        raise SystemExit("Execute antes o notebook do RA1, que gera o conjunto preparado.")
    referencia = pd.read_parquet(
        ARQUIVO_PREPARADO,
        columns=["uf_residencia", "regiao_residencia", "classificacao_final", "caso_grave"],
    )
    return referencia[referencia["caso_grave"].notna()].reset_index(drop=True)


def gerar_lotes(casos):
    gerador = np.random.default_rng(SEMENTE)
    lotes = {}
    proximo_id = 1
    for lote in LOTES:
        notificacoes = []
        for dia, quantidade in lote["dias"].items():
            perfis = casos.iloc[gerador.choice(len(casos), size=quantidade, replace=False)]
            minutos = np.sort(gerador.integers(0, 24 * 60, size=quantidade))
            horarios = pd.Timestamp(dia) + pd.to_timedelta(minutos, unit="min")
            notificacoes += [
                {
                    "id_notificacao": f"SIM-{proximo_id + posicao:04d}",
                    "dt_notificacao": horario.strftime("%Y-%m-%d %H:%M:%S"),
                    "uf_residencia": perfil.uf_residencia,
                    "regiao_residencia": perfil.regiao_residencia,
                    "classificacao_final": perfil.classificacao_final,
                    "caso_grave": bool(perfil.caso_grave),
                }
                for posicao, (horario, perfil) in enumerate(zip(horarios, perfis.itertuples()))
            ]
            proximo_id += quantidade
        lotes[lote["lote"]] = notificacoes
    return lotes


def publicar(numero, notificacoes):
    nome_arquivo = f"lote_{numero:02d}.json"
    arquivo = PASTA_PUBLICACAO / nome_arquivo
    with arquivo.open("w", encoding="utf-8") as saida:
        for notificacao in notificacoes:
            saida.write(json.dumps(notificacao, ensure_ascii=False) + "\n")
    arquivo.replace(PASTA_ENTRADA / nome_arquivo)


def esperar_consumidor():
    inicio = time.monotonic()
    while not SINAL_CONSUMIDOR_PRONTO.exists():
        if time.monotonic() - inicio > ESPERA_MAXIMA_CONSUMIDOR_SEGUNDOS:
            raise SystemExit("O consumidor não respondeu. Inicie ra2/consumidor.py em outro terminal.")
        time.sleep(1)


def main():
    argumentos = argparse.ArgumentParser(description="Publica lotes de notificações simuladas de dengue.")
    argumentos.add_argument("--intervalo", type=float, default=INTERVALO_PADRAO_SEGUNDOS, help="segundos entre um lote e o próximo")
    intervalo = argumentos.parse_args().intervalo

    lotes = gerar_lotes(carregar_casos_classificados())
    print("Aguardando o consumidor ficar pronto...", flush=True)
    esperar_consumidor()
    if any(PASTA_ENTRADA.iterdir()):
        raise SystemExit("A pasta de entrada já tem lotes. Reinicie o consumidor para começar uma simulação nova.")

    for posicao, lote in enumerate(LOTES):
        notificacoes = lotes[lote["lote"]]
        publicar(lote["lote"], notificacoes)
        dias = ", ".join(pd.Timestamp(dia).strftime("%d/%m") for dia in lote["dias"])
        graves = sum(n["caso_grave"] for n in notificacoes)
        atraso = " (atrasado)" if "atrasada" in lote["chegada"] else ""
        print(f"[{time.strftime('%H:%M:%S')}] Lote {lote['lote']}{atraso} publicado: {len(notificacoes)} notificações de {dias}, {graves} grave(s)", flush=True)
        if posicao < len(LOTES) - 1:
            time.sleep(intervalo)
    print("Todos os lotes foram publicados.", flush=True)


if __name__ == "__main__":
    main()
