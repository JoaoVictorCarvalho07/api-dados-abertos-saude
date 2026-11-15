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

Implementa??o principal: notebook ?nico `ra1/ra1_dengue_2026.ipynb`, que faz ingest?o, diagn?stico de qualidade e limpeza e grava `dados/preparados/dengue_brasil_2026.parquet`.

Como reproduzir (Windows, Python 3.11), a partir da raiz do reposit?rio:

```bash
py -3.11 -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m jupyter nbconvert --to notebook --execute --inplace ra1/ra1_dengue_2026.ipynb
```

Alternativa: as mesmas etapas separadas em scripts, em `ra1/py/`. Eles importam `ra1/config.py`, ent?o rode com `PYTHONPATH=ra1`:

| Script | Etapa do documento | Evid?ncia gerada |
|---|---|---|
| `ra1/py/ingestao.py` | 02 ? Fontes e ingest?o | `ra1/saidas/01_ingestao.md` |
| `ra1/py/qualidade.py` | 03 ? Compreens?o e qualidade | `ra1/saidas/02_diagnostico_qualidade.md` e `.csv` |
| `ra1/py/limpeza.py` | 04 e 05 ? Limpeza e conjunto resultante | `ra1/saidas/03_limpeza_e_resultado.md` e `dados/preparados/dengue_brasil_2026.parquet` |

```powershell
$env:PYTHONPATH = "ra1"
.venv/Scripts/python.exe ra1/py/ingestao.py
.venv/Scripts/python.exe ra1/py/qualidade.py
.venv/Scripts/python.exe ra1/py/limpeza.py
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

### RA3: Análise, visualização e Machine Learning (`ra3/`)

Notebook: `ra3/ra3_dengue_2026.ipynb`, seguindo as seções 3.1 a 3.5 do template da disciplina. Resumo para estudo e apresentação: `ra3/RESUMO.md`.

| Seção | O que faz | Principal resultado |
|---|---|---|
| 3.1 Estatística descritiva | Média, mediana, moda, desvio-padrão, IQR, amplitude e assimetria da idade e do atraso até a notificação; frequências de gravidade | Mediana de 29 anos e de 3 dias de atraso, ambas com cauda à direita |
| 3.2 Visualizações | Notificações por semana, por UF (total e por 100 mil habitantes), idade x hospitalização e hospitalização por faixa etária | Pico na SE 14; Goiás com 1.632 notificações por 100 mil; hospitalização em "U" por idade |
| 3.3 Representatividade | Origem, abrangência, completude e vieses do Sinan | Vigilância passiva, campos de desfecho com 26–29% de vazios |
| 3.4 Machine Learning | Classificação de hospitalização com regressão logística e árvore de decisão (`class_weight="balanced"`), treino/teste 80/20 estratificado, sem colunas que vazam o desfecho | Regressão logística: recall 0,67 e ROC-AUC 0,75 (baseline 0,50) |
| 3.5 Conclusões | Liga os resultados às perguntas P1–P3 | — |

Execute antes o notebook do RA1, que gera `dados/preparados/dengue_brasil_2026.parquet`. O RA3 também lê `DENGBR26.csv.zip` (sintomas e comorbidades) e `ra3/populacao_uf_censo2022.csv` (Censo 2022, IBGE/SIDRA tabela 4709). Não precisa de Java nem de Spark.

```bash
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m jupyter nbconvert --to notebook --execute --inplace ra3/ra3_dengue_2026.ipynb
```

Saídas: o notebook com os resultados e as figuras em `ra3/figuras/` (`fig1` a `fig5`). A execução leva menos de 1 minuto e usa semente fixa (`random_state=42`), então os números se repetem.

---

**Curso:** Sistemas de Informação

**Alunos:** 
- Bruna da Silva Carnelossi
- João Pedro de Souza Quintiliano da Silva
- João Victor Carvalho de Freitas
- Matheus Henrique Heinzen
