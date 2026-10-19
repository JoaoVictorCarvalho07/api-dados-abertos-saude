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

### Armazenamento dos dados preparados

O conjunto preparado no RA1 é salvo em **Parquet** (`dados/preparados/leitos_2025.parquet`), não em banco SQL.

- **Volume pequeno:** cerca de 86 mil linhas numa única tabela; o pandas lê em cerca de 1 s. Um banco não traz ganho de desempenho nem de organização.
- **O RA2 lê arquivos:** o Spark Structured Streaming recebe registros novos por uma pasta de arquivos. Banco SQL não é fonte de streaming no Spark sem ferramentas extras, e o enunciado dispensa integrações adicionais.
- **Tipos preservados:** `CNES` continua texto (com os zeros à esquerda) e `COMP` continua data, sem precisar definir esquema à mão como num banco ou perder tipos como num CSV.
- **Reprodutibilidade:** quem clonar o repositório roda o notebook sem instalar ou configurar banco.

Um banco passaria a fazer sentido se o projeto juntasse vários anos ou várias tabelas (por exemplo, hospitais separados dos leitos mês a mês, ou cruzamento com população do IBGE), ou se uma etapa futura exigisse uma fonte consultada por várias pessoas ao mesmo tempo.

Para usar SQL sem banco, o [DuckDB](https://duckdb.org/) consulta o Parquet direto, útil nas verificações de qualidade:

```python
duckdb.sql("SELECT UF, COUNT(*) FROM 'dados/preparados/leitos_2025.parquet' GROUP BY UF")
```

---

**Curso:** Sistemas de Informação

**Alunos:** 
- Bruna da Silva Carnelossi
- João Pedro de Souza Quintiliano da Silva
- João Victor Carvalho de Freitas
- Matheus Henrique Heinzen
