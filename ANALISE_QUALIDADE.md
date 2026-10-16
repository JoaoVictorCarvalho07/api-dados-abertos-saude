# Análise de qualidade — amostra do PR 2024

Planejamento dos pontos 4 (compreensão e avaliação da qualidade) e 5 (limpeza e preparação) do RA1,
feito sobre uma amostra de 100 linhas do arquivo oficial.

## Fonte

- Conjunto de dados: [Sinan/Dengue — Portal de Dados Abertos do SUS](https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue)
- Arquivo: [DENGBR24.csv.zip](https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SINAN/Dengue/csv/DENGBR24.csv.zip) (187 MB compactado, 1,8 GB descompactado, atualizado em 10/10/2026)
- Dicionário de dados: [dic_dados_dengue.pdf](https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SINAN/Dengue/dic_dados_dengue.pdf)

| | |
|---|---|
| Formato | CSV, separador vírgula, UTF-8, 121 colunas |
| Brasil 2024 | 6.564.924 notificações |
| Notificadas no PR | 647.663 |
| Residentes do PR | 647.802 (1.492 notificados em outro estado) |

## A amostra

Gerada com `python gerar_amostra.py 100` → `dados/amostras/amostra_pr_100.csv`. O script espera o zip em `dados/brutos/DENGBR24.csv.zip`.

São as **primeiras** 100 linhas do PR no arquivo, não um sorteio. Por isso a amostra mostra **que tipo**
de problema existe, não **quanto**. Exemplo do viés: 42% de casos inconclusivos (`CLASSI_FIN=8`) na
amostra contra 3,6% na base completa do PR.

## Ponto 4 — problemas a avaliar

| Problema | O que apareceu na amostra | Como medir na base completa |
|---|---|---|
| Colunas sem informação | 26 de 121 colunas 100% vazias; 6 constantes (`TP_NOT`, `ID_AGRAVO`, `NU_ANO`, `SG_UF_NOT`, `ID_PAIS`, `CS_FLXRET`) | % de vazios e nº de valores distintos por coluna |
| Vazio "por desenho" | `GRAV_*` 99% vazios, `ALRM_*` 96% — só preenchidos em caso grave ou com sinais de alarme | Cruzar o vazio com `CLASSI_FIN` |
| "Ignorado" disfarçado | Código `9` em 13% de `CS_RACA` e 28% de `CS_ESCOL_N` (mais 24% em branco) | Somar `9` + vazio por coluna |
| Códigos especiais | `ID_OCUPA_N` com `999991`, `998999`, `000000` | Confirmar no dicionário e contar |
| Idade codificada | `NU_IDADE_N=4026` = 26 anos; `3xxx` = meses; 1 caso diverge de `ANO_NASC` | Decodificar e comparar com `ANO_NASC` |
| Inconsistência entre campos | 1 caso com `HOSPITALIZ=1` sem `DT_INTERNA` | Regras cruzadas: homem gestante, internação sem data, óbito em caso leve |
| Datas fora de ordem | Nenhum na amostra; a 1ª linha do arquivo (ES) tem investigação 1 ano antes da notificação | Sintoma depois da notificação; investigação/encerramento antes dela |
| Prazo de encerramento | Encerramentos em junho de 2025 (prazo oficial: 60 dias) | Dias entre notificação e encerramento; contar acima de 60 |
| Duplicatas | Nenhuma em 100 linhas (amostra pequena demais) | Chave: município + data de sintoma + ano de nascimento + sexo |
| Outliers | Atraso sintoma → notificação de 0 a 13 dias (mediana 2) | Extremos: atraso negativo ou de centenas de dias |

## Ponto 5 — tratamentos propostos

1. **Remover colunas 100% vazias e constantes** — não carregam informação.
2. **Manter os vazios "por desenho"** — preencher `GRAV_*` de quem não teve dengue grave inventaria dado; o vazio significa "não se aplica" e fica documentado.
3. **Unificar `9` e vazio em "Ignorado"** — apagar as linhas descartaria ~30% da base por causa da escolaridade.
4. **Converter a idade para anos** (`idade_anos`), usando `ANO_NASC` quando `NU_IDADE_N` estiver vazio ou incoerente.
5. **Corrigir tipos** — datas de texto para data; sintomas `1/2` para booleano.
6. **Marcar datas impossíveis** com `data_inconsistente` em vez de apagar; decidir a remoção pelo volume medido.
7. **Traduzir códigos** (`CLASSI_FIN 10` → "Dengue", `11` → "Com sinais de alarme"…) a partir do dicionário oficial.
8. **Duplicatas** — remover só as exatas; analisar as "parecidas" antes, porque reinfecção no mesmo ano é possível.

## A confirmar no dicionário

- Significado de `CLASSI_FIN 8`.
- Códigos `9999xx` e `000000` de `ID_OCUPA_N`.
- Códigos de `CS_GESTANT`.
- Se a base pública exclui os casos descartados (`CLASSI_FIN 5` não aparece no PR).
