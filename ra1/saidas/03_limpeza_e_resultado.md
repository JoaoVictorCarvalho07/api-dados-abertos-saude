# RA1 — Limpeza, preparação e conjunto resultante

## Arquivo gerado

`dados/preparados/dengue_brasil_2026.parquet` — 470.221 linhas x 24 colunas. Parquet. Releitura idêntica: **True**

## Registro das decisões

| Decisão   | Relacionada a            | Ação                                                                                              |   Afetados | Justificativa                                                                                                                                                                                   |
|:----------|:-------------------------|:--------------------------------------------------------------------------------------------------|-----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D1        | Q3                       | Remover linhas duplicadas por completo                                                            |        230 | Linha idêntica nas 121 colunas é o mesmo registro repetido; mantê-la inflaria a contagem de casos (P1).                                                                                         |
| D2        | Q1, Q2, Q8, Q9, Q18, Q21 | Manter só as 16 colunas usadas por P1–P3                                                          |        105 | As perguntas não usam as demais; TP_NOT, ID_AGRAVO e NU_ANO são constantes. Problemas em colunas descartadas (DT_DIGITA, DT_ENCERRA, DT_INTERNA, CS_GESTANT) ficam registrados, sem tratamento. |
| D3        | Q5                       | Converter tipos: datas, idade inteira, sim/não booleano, categorias                               |     470221 | Tudo foi lido como texto para não perder zeros nem inferir tipos errados; a conversão acontece aqui, com regra explícita.                                                                       |
| D4        | Q6, Q7                   | Esvaziar e sinalizar data de sintomas fora do período ou depois da notificação                    |          0 | Nenhum caso em 2026; a regra fica como proteção para reexecuções com o arquivo atualizado.                                                                                                      |
| D5        | Q10                      | Manter atrasos acima de 60 dias                                                                   |       2442 | Notificação tardia é plausível; valor extremo, por si só, não justifica exclusão.                                                                                                               |
| D6        | Q11, Q12, Q13            | CLASSI_FIN '0' e vazio viram 'Sem classificação'                                                  |      34895 | '0' não existe no dicionário e só o ES o usa, como vazio. Esses casos ficam fora do denominador de gravidade (caso_grave vazio).                                                                |
| D7        | Q14, Q15, Q16            | Idade em anos pela unidade do código; acima de 120 vira vazio; ano de nascimento como alternativa |          3 | O código mistura unidade e valor (4026 = 26 anos). A coluna Afetados mostra as idades recuperadas pelo ano de nascimento.                                                                       |
| D8        | Q17                      | Sexo 'I' (ignorado) vira vazio                                                                    |        279 | P2 compara homens e mulheres; 'ignorado' não informa e sai só dessa comparação.                                                                                                                 |
| D9        | Q19, Q20                 | Comorbidades 9 (ignorado) e vazio viram vazio                                                     |      14899 | A linha é mantida; a falta de informação só a exclui da análise de comorbidades (P3).                                                                                                           |
| D10       | Q4                       | Manter e sinalizar possíveis duplicatas                                                           |       2925 | Sem identificador de paciente, linhas parecidas podem ser pessoas diferentes; remover apagaria casos reais.                                                                                     |
| D11       | -                        | Criar mes_sintomas, região, faixa_etaria, caso_grave e atraso_notificacao_dias                    |     470221 | Colunas derivadas que as perguntas exigem (mês e UF para P1, sexo e gravidade para P2, faixa etária e comorbidade para P3, atraso para o RA2).                                                  |

## Comparação antes e depois

| Medida                                  | Após ingestão   | Após preparação   | Explicação                                                                              |
|:----------------------------------------|:----------------|:------------------|:----------------------------------------------------------------------------------------|
| Registros                               | 470451          | 470221            | Remoção das duplicatas exatas (D1)                                                      |
| Atributos                               | 121             | 24                | Seleção das colunas usadas por P1–P3 e derivadas (D2, D11)                              |
| Duplicatas exatas                       | 230             | 0                 | D1; no preparado, medido por id_registro repetido                                       |
| Data de sintomas inválida               | 0               | 0                 | Esvaziadas e sinalizadas em dt_sintomas_invalida: 0 (D4)                                |
| CLASSI_FIN fora do domínio              | 4318            | 0                 | Agrupadas em 'Sem classificação' (D6)                                                   |
| Idade inutilizável                      | 18              | 15                | Recuperada pelo ano de nascimento quando possível (D7)                                  |
| Sexo sem M/F                            | 0.06%           | 0.06%             | Ignorado vira vazio (D8)                                                                |
| Diabetes sem sim/não                    | 3.18%           | 3.17%             | 9 e fora do domínio viram vazio (D9)                                                    |
| Hipertensão sem sim/não                 | 3.18%           | 3.17%             | 9 e fora do domínio viram vazio (D9)                                                    |
| Atraso > 60 dias                        | 2442            | 2442              | Mantidos: valor extremo não justifica exclusão (D5)                                     |
| Linhas envolvidas em possível duplicata | -               | 5797              | Mantidas e sinalizadas; conta todas as linhas de cada grupo, inclusive a primeira (D10) |

## Validações após o tratamento

| Regra                                                   | Passou   |
|:--------------------------------------------------------|:---------|
| Registros = bruto menos duplicatas exatas               | True     |
| id_registro único                                       | True     |
| dt_notificacao preenchida e dentro do período           | True     |
| dt_sintomas vazia ou dentro do período                  | True     |
| dt_sintomas nunca depois da notificação                 | True     |
| Atraso de notificação nunca negativo                    | True     |
| idade_anos vazia ou entre 0 e 120                       | True     |
| faixa_etaria vazia só quando idade_anos vazia           | True     |
| classificacao_final dentro do domínio                   | True     |
| caso_grave preenchido só nas classificações 10, 11 e 12 | True     |
| uf_residencia vazia ou uma das 27 UFs                   | True     |
| sexo vazio ou Masculino / Feminino                      | True     |

## Dicionário do conjunto preparado

| Atributo                | Origem                            | Tipo           | Domínio / descrição                                                                                         |
|:------------------------|:----------------------------------|:---------------|:------------------------------------------------------------------------------------------------------------|
| id_registro             | posição da linha no arquivo bruto | int64          | rastreabilidade até o DENGBR26                                                                              |
| dt_notificacao          | DT_NOTIFIC                        | datetime64[ns] | data da notificação                                                                                         |
| dt_sintomas             | DT_SIN_PRI                        | datetime64[ns] | data de início dos sintomas; vazia quando inválida                                                          |
| semana_epi_sintomas     | SEM_PRI                           | string         | semana epidemiológica dos sintomas (AAAASS)                                                                 |
| mes_sintomas            | derivada de dt_sintomas           | string         | AAAA-MM                                                                                                     |
| uf_notificacao          | SG_UF_NOT                         | category       | sigla da UF onde o caso foi notificado                                                                      |
| regiao_notificacao      | SG_UF_NOT                         | category       | região da UF de notificação                                                                                 |
| municipio_notificacao   | ID_MUNICIP                        | string         | código IBGE (6 dígitos)                                                                                     |
| uf_residencia           | SG_UF                             | category       | sigla da UF de residência                                                                                   |
| regiao_residencia       | SG_UF                             | category       | região da UF de residência                                                                                  |
| municipio_residencia    | ID_MN_RESI                        | string         | código IBGE (6 dígitos)                                                                                     |
| sexo                    | CS_SEXO                           | category       | Masculino / Feminino; vazio quando ignorado                                                                 |
| idade_anos              | NU_IDADE_N, ANO_NASC              | Int64          | anos completos, 0 a 120                                                                                     |
| faixa_etaria            | derivada de idade_anos            | category       | 0-4, 5-14, 15-29, 30-44, 45-59, 60-74, 75+                                                                  |
| classificacao_final     | CLASSI_FIN                        | category       | Descartado, Inconclusivo, Dengue, Dengue com sinais de alarme, Dengue grave, Chikungunya, Sem classificação |
| caso_grave              | derivada de CLASSI_FIN            | boolean        | verdadeiro para 11 e 12, falso para 10, vazio nas demais                                                    |
| criterio_confirmacao    | CRITERIO                          | category       | Laboratorial, Clínico-epidemiológico, Em investigação                                                       |
| hospitalizado           | HOSPITALIZ                        | boolean        | verdadeiro / falso; vazio quando ignorado                                                                   |
| evolucao                | EVOLUCAO                          | category       | Cura, Óbito pelo agravo, Óbito por outras causas, Óbito em investigação                                     |
| diabetes                | DIABETES                          | boolean        | verdadeiro / falso; vazio quando ignorado                                                                   |
| hipertensao             | HIPERTENSA                        | boolean        | verdadeiro / falso; vazio quando ignorado                                                                   |
| atraso_notificacao_dias | DT_NOTIFIC - DT_SIN_PRI           | Int64          | dias, mantidos inclusive os extremos                                                                        |
| dt_sintomas_invalida    | derivada                          | boolean        | verdadeiro quando DT_SIN_PRI foi descartada                                                                 |
| possivel_duplicata      | derivada                          | boolean        | verdadeiro quando outra linha tem a mesma chave                                                             |
