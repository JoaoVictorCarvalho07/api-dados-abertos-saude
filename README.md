## Data Analytics - API de Dados Abertos 

API para disponibilização de dados abertos para repartições pertencentes ao DEMAS.

https://apidadosabertos.saude.gov.br/v1/#/Assist%C3%AAncia%20%C3%A0%20Sa%C3%BAde/get_assistencia_a_saude_hospitais_e_leitos

---

### Part 1 - Inspect

Identify at least 5 data quality problems in the dataset.

- Column/Line
- Problem identified
- Why it is a problem
- Proposed solution

---

### Part 2 - Prepare

Using Pandas or any other data processing library of your choice:

- inspect the dataset;
- handle duplicated records;
- identify missing values;
- correct inconsistent formats;
- convert incorrect data types;
- validate the resulting dataset.

---

### RA1 — Ingestão e preparação (`ra1/`)

Fonte: `DENGBR26.csv.zip`, conjunto [Sinan/Dengue](https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue) do Portal de Dados Abertos do SUS. Recorte: notificações de dengue de todo o Brasil em 2026 (470.451 linhas, 121 colunas, de 04/01 a 04/10/2026).

| Script | Etapa do documento | Evidência gerada |
|---|---|---|
| `ra1/ingestao.py` | 02 — Fontes e ingestão | `ra1/saidas/01_ingestao.md` |
| `ra1/qualidade.py` | 03 — Compreensão e qualidade | `ra1/saidas/02_diagnostico_qualidade.md` e `.csv` |
| `ra1/limpeza.py` | 04 e 05 — Limpeza e conjunto resultante | `ra1/saidas/03_limpeza_e_resultado.md` e `dados/preparados/dengue_brasil_2026.parquet` |

Como reproduzir (Windows, Python 3.11), a partir da raiz do repositório:

```bash
py -3.11 -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe ra1/ingestao.py
.venv/Scripts/python.exe ra1/qualidade.py
.venv/Scripts/python.exe ra1/limpeza.py
```

Se `DENGBR26.csv.zip` não estiver na raiz, `ingestao.py` baixa da URL oficial. O `limpeza.py` só grava o Parquet se todas as validações passarem.

O conjunto preparado é salvo em **Parquet**, não em banco SQL: o volume cabe no pandas, o Spark Structured Streaming do RA2 lê arquivos, o Parquet preserva os tipos (datas, categorias, códigos como texto) e ninguém precisa instalar banco para reproduzir.

### RA2: Streaming com janelas temporais (`ra2/`)

Notebook: `ra2/ra2_dengue_2026.ipynb` (Cenário A, dados estáticos com chegada simulada).

- Notificações dos dias 05 a 07/10/2026 são simuladas com o perfil (UF, região, classificação) de casos reais do conjunto preparado no RA1, com semente fixa.
- Quatro lotes de JSON são publicados numa pasta monitorada pelo Spark Structured Streaming (`readStream`); o último lote é atrasado.
- Janela **tumbling de 1 dia** sobre `dt_notificacao`, por região: contagem de notificações e soma de casos graves, com saída em memória no modo `complete`.
- Ao final, o resultado do streaming é conferido contra o mesmo cálculo em lote.

Pré-requisitos além do `requirements.txt`: **Java 17** e, no Windows, a variável `HADOOP_HOME` apontando para uma pasta com `bin/winutils.exe` e `bin/hadoop.dll` (o Spark precisa deles para gravar o checkpoint do streaming). Execute antes o notebook do RA1, que gera `dados/preparados/dengue_brasil_2026.parquet`.

```bash
.venv/Scripts/python.exe -m jupyter nbconvert --to notebook --execute --inplace ra2/ra2_dengue_2026.ipynb
```

**Demonstração ao vivo (dois terminais).** Os mesmos lotes do notebook podem ser publicados por um processo e consumidos por outro, como num fluxo real:

| Arquivo | Papel |
|---|---|
| `ra2/config.py` | Pastas, lotes e semente compartilhados pelos dois processos |
| `ra2/consumidor.py` | Spark Structured Streaming: monitora `dados/streaming/entrada`, aplica a janela e imprime a tabela a cada micro-batch |
| `ra2/produtor.py` | Gera as notificações simuladas e publica um lote a cada N segundos |

Terminal 1 (inicie primeiro; limpa `dados/streaming` e fica aguardando):

```bash
.venv/Scripts/python.exe ra2/consumidor.py
```

Terminal 2 (espera o consumidor ficar pronto e publica um lote a cada 10 s):

```bash
.venv/Scripts/python.exe ra2/produtor.py --intervalo 10
```

Cada lote vira um micro-batch no terminal 1. `Ctrl+C` encerra o consumidor.

---

**Curso:** Sistemas de Informação

**Alunos:** 
- Bruna da Silva Carnelossi
- João Pedro de Souza Quintiliano da Silva
- João Victor Carvalho de Freitas
- Matheus Henrique Heinzen
