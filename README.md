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

### RA1: Ingestão e preparação (`ra1/`)

Usamos o arquivo `DENGBR26.csv.zip`, do conjunto [Sinan/Dengue](https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue) do Portal de Dados Abertos do SUS. O recorte são as notificações de dengue de todo o Brasil em 2026 (470.451 linhas e 121 colunas, de 04/01 a 04/10/2026).

A implementação principal é o notebook único `ra1/ra1_dengue_2026.ipynb`. Ele faz a ingestão, o diagnóstico de qualidade e a limpeza, e grava `dados/preparados/dengue_brasil_2026.parquet`.

Para reproduzir (Windows, Python 3.11), a partir da raiz do repositório:

```bash
py -3.11 -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m jupyter nbconvert --to notebook --execute --inplace ra1/ra1_dengue_2026.ipynb
```

Se o `DENGBR26.csv.zip` não estiver na raiz, o notebook baixa o arquivo da URL oficial.

Salvamos o conjunto preparado em Parquet e não num banco SQL. O volume cabe no pandas, o Spark Structured Streaming do RA2 lê arquivos, o Parquet mantém os tipos (datas, categorias e códigos como texto) e ninguém precisa instalar um banco para reproduzir.

### RA2: Streaming com janelas temporais (`ra2/`)

Notebook: `ra2/ra2_dengue_2026.ipynb` (Cenário A, dados estáticos com chegada simulada).

- Simulamos notificações dos dias 05 a 07/10/2026 com o perfil (UF, região e classificação) de casos reais do conjunto preparado no RA1, usando semente fixa.
- Publicamos quatro lotes de JSON numa pasta que o Spark Structured Streaming monitora (`readStream`). O último lote chega atrasado.
- Usamos uma janela **tumbling de 1 dia** sobre `dt_notificacao`, por região, que conta as notificações e soma os casos graves. A saída fica em memória no modo `complete`.
- No final, comparamos o resultado do streaming com o mesmo cálculo feito em lote.

Além do `requirements.txt`, é preciso ter o **Java 17** e, no Windows, a variável `HADOOP_HOME` apontando para uma pasta com `bin/winutils.exe` e `bin/hadoop.dll`. O Spark usa esses arquivos para gravar o checkpoint do streaming. Antes, rode o notebook do RA1, que gera `dados/preparados/dengue_brasil_2026.parquet`.

```bash
.venv/Scripts/python.exe -m jupyter nbconvert --to notebook --execute --inplace ra2/ra2_dengue_2026.ipynb
```

### RA3: Análise, visualização e Machine Learning (`ra3/`)

Notebook: `ra3/ra3_dengue_2026.ipynb`, com as seções 3.1 a 3.5 do template da disciplina. O resumo para estudar para a apresentação está em `ra3/RESUMO.md`.

| Seção | O que fizemos | Principal resultado |
|---|---|---|
| 3.1 Estatística descritiva | Média, mediana, moda, desvio-padrão, IQR, amplitude e assimetria da idade e do atraso até a notificação, e frequências de gravidade | Mediana de 29 anos e de 3 dias de atraso, as duas com cauda à direita |
| 3.2 Visualizações | Notificações por semana, por UF (total e por 100 mil habitantes), idade por hospitalização e hospitalização por faixa etária | Pico na SE 14, Goiás com 1.632 notificações por 100 mil e hospitalização em "U" por idade |
| 3.3 Representatividade | Origem, abrangência, completude e vieses do Sinan | Vigilância passiva e campos de desfecho com 26 a 29% de vazios |
| 3.4 Machine Learning | Classificação de hospitalização com regressão logística e árvore de decisão (`class_weight="balanced"`), treino e teste 80/20 estratificado, sem as colunas que entregam o desfecho | Regressão logística com recall de 0,67 e ROC-AUC de 0,75 (baseline 0,50) |
| 3.5 Conclusões | Relação dos resultados com as perguntas P1 a P3 | Ver o notebook |

Antes é preciso rodar o notebook do RA1, que gera `dados/preparados/dengue_brasil_2026.parquet`. O RA3 também lê o `DENGBR26.csv.zip` (sintomas e comorbidades) e o `ra3/populacao_uf_censo2022.csv` (Censo 2022, IBGE/SIDRA tabela 4709). Não precisa de Java nem de Spark.

```bash
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m jupyter nbconvert --to notebook --execute --inplace ra3/ra3_dengue_2026.ipynb
```

O notebook sai com os resultados e as figuras ficam em `ra3/figuras/` (`fig1` a `fig5`). A execução leva menos de 1 minuto e usa semente fixa (`random_state=42`), então os números se repetem.

---

**Curso:** Sistemas de Informação

**Alunos:** 
- Bruna da Silva Carnelossi
- João Pedro de Souza Quintiliano da Silva
- João Victor Carvalho de Freitas
- Matheus Henrique Heinzen
