# RA2: Resumo da entrega

## Objetivo

Acompanhar, dia a dia e por região, quantas novas notificações de dengue chegam e quantas delas são casos graves (dengue com sinais de alarme ou dengue grave). É a versão contínua das perguntas do RA1: os números se formam enquanto as notificações chegam.

## Cenário

**Cenário A, dados estáticos com chegada simulada.** O arquivo do RA1 vai até 04/10/2026; o RA2 simula as notificações dos dias seguintes (05 a 07/10).

- Cada notificação simulada tem identificador e horário artificiais, mas o perfil (UF e região de residência, classificação final, caso grave) é sorteado entre os 365.519 casos de dengue do conjunto preparado no RA1.
- O sorteio usa semente fixa: toda execução gera os mesmos registros.

## O que está no repositório

| Arquivo | O que faz |
|---|---|
| `ra2/ra2_dengue_2026.ipynb` | Notebook do RA2, seções 8 a 12 do template, executado (é a entrega) |
| `ra2/config.py` | Pastas, lotes e semente compartilhados pelo produtor e pelo consumidor |
| `ra2/produtor.py` | Gera as notificações simuladas e publica um lote a cada N segundos |
| `ra2/consumidor.py` | Spark Structured Streaming com a janela, imprimindo a tabela a cada micro-batch |
| `requirements.txt` | Inclui `pyspark==4.0.3` |

O notebook é a entrega; produtor e consumidor servem à demonstração ao vivo. Os dois geram exatamente os mesmos lotes e chegam aos mesmos resultados.

## Como os registros chegam

Quatro lotes de JSON, publicados um de cada vez numa pasta monitorada pelo Spark Structured Streaming (`readStream`). Cada arquivo é escrito em outra pasta e só depois movido para a pasta monitorada, para o Spark nunca ler um arquivo pela metade.

| Lote | Notificações | Dias | O que mudou na tabela |
|---|---|---|---|
| 1 | 30 | 05/10 | Surgiram 5 janelas de 05/10, uma por região |
| 2 | 45 | 05/10 e 06/10 | As janelas de 05/10 cresceram e surgiram as de 06/10 |
| 3 | 50 | 06/10 e 07/10 | 05/10 ficou igual; 06/10 cresceu e surgiram as de 07/10 |
| 4 (atrasado) | 10 | 05/10 | As janelas de 05/10 voltaram a crescer |

## Janela temporal

| Item | Escolha |
|---|---|
| Tipo | Tumbling (sem sobreposição) |
| Duração | 1 dia |
| Deslocamento | Não se aplica |
| Coluna de tempo | `dt_notificacao` (tempo do evento) |
| Agrupamento | Janela × `regiao_residencia` |
| Agregações | `count(*)` = notificações; `sum(caso_grave)` = casos graves |
| Saída | Tabela em memória, modo `complete` |

A sessão do Spark usa o fuso **UTC** para que a janela de um dia vá de 00:00 a 24:00 da data registrada. Com o fuso de São Paulo, o Spark alinharia as janelas às 21:00.

## Resultado

- 135 notificações publicadas e 135 processadas, em 13 janelas (dia × região).
- Por dia: 60 notificações em 05/10, 40 em 06/10 e 35 em 07/10, com 1 caso grave em cada dia.
- O resultado final do streaming é idêntico ao do mesmo cálculo feito em lote (`spark.read`), conferido com `assert` no notebook.

Três comportamentos ficaram visíveis:

- **Estado:** a contagem de cada janela é mantida entre os lotes e somada aos registros novos.
- **Tempo do evento:** as notificações atrasadas do lote 4 entraram na janela de 05/10, e não na do dia em que chegaram.
- **Correção:** o streaming chega ao mesmo resultado do processamento em lote, só que atualizado aos poucos.

## Como reproduzir

Pré-requisitos: Java 17 e, no Windows, `HADOOP_HOME` apontando para uma pasta com `bin/winutils.exe` e `bin/hadoop.dll`. O notebook do RA1 precisa ter sido executado antes, porque gera `dados/preparados/dengue_brasil_2026.parquet`.

Na raiz do repositório:

```bash
.venv/Scripts/python.exe -m jupyter nbconvert --to notebook --execute --inplace ra2/ra2_dengue_2026.ipynb
```

### Demonstração ao vivo (dois terminais)

No notebook, produtor e consumidor rodam no mesmo processo, em sequência. Na demonstração eles rodam ao mesmo tempo, como num fluxo real: o consumidor não sabe quando o próximo lote vai chegar.

Terminal 1, iniciado primeiro (limpa `dados/streaming` e fica aguardando):

```bash
.venv/Scripts/python.exe ra2/consumidor.py
```

Terminal 2 (espera o consumidor ficar pronto e publica um lote a cada 10 s):

```bash
.venv/Scripts/python.exe ra2/produtor.py --intervalo 10
```

Cada lote aparece no terminal 1 como um micro-batch (`Batch: 0` a `Batch: 3`), com a tabela de janelas atualizada. `Ctrl+C` encerra o consumidor. Os nomes de coluna no terminal não têm acento (`inicio`, `regiao`), porque a saída do Spark no console do Windows não sai em UTF-8.

## Limitações

- O streaming é um exercício didático: a fonte pública é um arquivo anual atualizado periodicamente, não um fluxo de eventos, e os registros dos lotes são simulados.
- As proporções entre regiões e de casos graves nos lotes refletem o perfil real usado no sorteio, não uma tendência dos dias simulados.
- Não foi usado *watermark*: no modo `complete` o Spark guarda o estado de todas as janelas, o que serve para a demonstração, mas não para uma aplicação que rode por meses.

## Pendências

1. Gerar o PDF com os notebooks do RA1 e do RA2 para a entrega.
2. Ensaiar a demonstração de 5 minutos com os dois terminais, destacando a janela de 05/10 mudando no lote atrasado (Batch 3).
