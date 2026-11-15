# RA3: resumo para estudar a apresentação

Este texto é para o grupo se preparar para a apresentação de 18/11. Todos os números saem do notebook `ra3/ra3_dengue_2026.ipynb` já executado.

## O que entregamos

| Arquivo | O que é |
|---|---|
| `ra3/ra3_dengue_2026.ipynb` | Notebook do RA3, com as seções 3.1 a 3.5 do template da disciplina |
| `ra3/figuras/` | As 5 figuras do notebook em PNG |
| `ra3/populacao_uf_censo2022.csv` | População por UF do Censo 2022 (IBGE, tabela SIDRA 4709), usada na taxa por 100 mil habitantes |
| `ra3/RESUMO.md` | Este texto |

O notebook lê o Parquet gerado no RA1 (`dados/preparados/dengue_brasil_2026.parquet`, com 470.221 notificações). Para o modelo ele também lê do arquivo bruto as colunas de sintomas e comorbidades e junta tudo pela posição original da linha (`id_registro`).

## 3.1 Estatística descritiva

Resumimos duas variáveis numéricas, a idade e o atraso entre os sintomas e a notificação, e contamos as categorias de gravidade.

| Medida | Idade (anos) | Atraso (dias) |
|---|---|---|
| Média | 31,6 | 4,5 |
| Mediana | 29 | 3 |
| Desvio-padrão | 19,2 | 8,6 |
| Q1 a Q3 (IQR) | 17 a 44 (27) | 1 a 5 (4) |
| Mínimo a máximo (amplitude) | 0 a 120 (120) | 0 a 238 (238) |
| Assimetria | 0,55 | 9,16 |

- Média e mediana mostram o valor típico (tendência central). Desvio-padrão, amplitude e IQR mostram o quanto os valores variam (dispersão). Quartis, assimetria e histograma mostram o formato da distribuição.
- Usamos mediana e IQR porque as duas variáveis têm cauda à direita. Alguns idosos e alguns atrasos enormes puxam a média para cima. A mediana é o valor do meio e o IQR é a faixa dos 50% do centro, e nenhum dos dois muda por causa de poucos valores extremos.
- Assimetria maior que 0 quer dizer cauda à direita. Na idade é leve (0,55) e no atraso é muito forte (9,16).
- 89,3% das notificações saem em até 7 dias. Só 2.442 (0,5%) passam de 60 dias.
- Na classificação final, 75,0% são dengue, 14,9% inconclusivos, 7,4% sem classificação, 2,6% com sinais de alarme e 0,2% dengue grave. Dos 365.519 confirmados, 3,5% são graves ou com sinais de alarme.
- 8,6% das 346.623 notificações com o campo preenchido foram hospitalizadas. Em 26,3% das notificações esse campo está vazio.
- A faixa etária com mais notificações é a de 15 a 29 anos (32,0%).

## 3.2 Como ler cada gráfico

1. **Figura 1, linha por semana epidemiológica.** O eixo X é a semana do início dos sintomas e o eixo Y é o número de notificações. O pico é a SE 14, no começo de abril, com 20.520 notificações. Metade do ano está em 13 das 39 semanas. A queda na última semana (SE 39, com 3.440) vem do atraso de digitação, e por isso pintamos essa parte de cinza.
2. **Figura 2, barras por UF.** À esquerda está o total e à direita a taxa por 100 mil habitantes. Goiás lidera nas duas (115.161 notificações e 1.632 por 100 mil, sete vezes a taxa do Brasil, que é 231,5). São Paulo é o 2º em total, mas na taxa fica abaixo da média (153,9). Por isso só faz sentido comparar estados de tamanhos diferentes pela taxa por habitante.
3. **Figura 3, histograma da idade e boxplot por hospitalização.** O histograma mostra muitos pacientes entre 15 e 30 anos e uma cauda de idosos. No boxplot, a linha do meio é a mediana, a caixa vai do Q1 ao Q3 e as hastes mostram até onde vão os dados sem os outliers. As medianas são quase iguais (30 e 29 anos), mas a caixa dos hospitalizados é bem mais larga (de 15 a 50 anos, contra 18 a 44).
4. **Figura 4, percentual de hospitalização por faixa etária.** Tem forma de "U". São 13,1% de 0 a 4 anos, cerca de 7% entre 15 e 44 anos e 22,2% acima de 75 anos. Quem mais pega dengue são os jovens, mas quem mais interna são as crianças pequenas e os idosos.
5. **Figura 5, matriz de confusão do modelo.** Explicamos na parte da seção 3.4.

## 3.3 Representatividade

Não fizemos amostragem.

- Os dados vêm do Sinan, que é vigilância passiva. Só entra quem procurou atendimento e teve a ficha preenchida. Cada linha é uma notificação, e não uma pessoa nem um caso confirmado.
- O arquivo cobre as 27 UFs, de 04/01 a 04/10/2026. Usamos todas as notificações, e o único sorteio é a divisão entre treino e teste do modelo.
- Limitações:
  1. Há subnotificação, porque casos leves e assintomáticos não aparecem.
  2. Cada UF notifica com intensidade e qualidade diferentes.
  3. Há atraso no encerramento. As notificações sem classificação são 1,1% em junho, 35,5% em agosto, 65,9% em setembro e 86,2% em outubro.
  4. Muitos campos estão vazios. Faltam 26,3% na hospitalização e 28,6% na evolução, com variação de 19,0% (Centro-Oeste) a 46,2% (Sul).
  5. O arquivo público não traz nenhum caso descartado, e 14,9% estão como inconclusivos.
  6. 5.797 linhas estão marcadas como possível duplicata.

## 3.4 O modelo explicado de forma simples

- A pergunta é se dá para prever, só com a ficha de notificação, se o paciente vai ser hospitalizado. É uma classificação (sim ou não).
- O target (alvo) é a coluna que queremos prever, `hospitalizado`. Só usamos as 346.623 notificações em que ela está preenchida.
- As features são as 31 colunas que o modelo usa para prever: idade, atraso, sexo, gestante, 14 sintomas, 7 comorbidades, um indicador de ficha clínica vazia e a região de residência.
- Vazamento de dados (*leakage*) é usar como feature uma informação que só existe depois daquilo que queremos prever. Seria como "prever" a internação usando a data da internação. Por isso tiramos `DT_INTERNA`, `EVOLUCAO`, `DT_OBITO`, `CLASSI_FIN`, `CRITERIO`, `DT_ENCERRA`, os sinais de alarme (`ALRM_*`), os sinais de gravidade (`GRAV_*`) e os resultados de exames.
- Separamos 80% para o modelo aprender (277.298) e 20% para avaliar (69.325). A divisão é estratificada, então as duas partes têm 8,6% de hospitalizados. A semente é fixa (42) e o resultado sai sempre igual.
- Comparamos quatro modelos:
  - um *baseline* que sempre diz "não interna", só como referência mínima;
  - a regressão logística, que é o modelo principal porque é simples e mostra o peso de cada variável;
  - uma árvore de decisão rasa, para comparar;
  - a mesma logística sem a leucopenia, como teste.
- Nos modelos de verdade usamos `class_weight="balanced"` para o modelo não ignorar a classe rara.
- A acurácia sozinha não serve aqui. Como 91,4% não internam, o *baseline* tem 91,4% de acurácia sem acertar nenhum hospitalizado. Por isso usamos outras métricas:
  - recall, que diz quantos dos que realmente internaram o modelo encontrou;
  - precisão, que diz quantos dos pacientes sinalizados realmente internaram;
  - F1, que é a média harmônica entre recall e precisão;
  - ROC-AUC, que é a chance de o modelo dar um risco maior para um paciente que interna do que para um que não interna. 0,5 é igual a sortear e 1,0 é perfeito.

| Modelo | Acurácia | Precisão | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Baseline | 0,914 | 0,000 | 0,000 | 0,000 | 0,500 |
| **Regressão logística** | 0,699 | 0,174 | **0,669** | 0,276 | **0,747** |
| Árvore de decisão | 0,678 | 0,168 | 0,698 | 0,271 | 0,744 |
| Logística sem leucopenia | 0,680 | 0,163 | 0,663 | 0,262 | 0,730 |

- Na matriz de confusão da logística, dos 5.938 hospitalizados do teste o modelo achou 3.971 e deixou passar 1.967. Ele também deu 18.870 alarmes falsos entre os 63.387 que não internaram. De cada 100 pacientes sinalizados, cerca de 17 internam, o dobro da taxa geral de 8,6%.
- A razão de chances diz por quanto a chance de internar é multiplicada quando a variável é "sim".
  - Aumentam a chance: leucopenia 4,08, gestante 2,62, Nordeste 1,91, doença autoimune 1,90, renal 1,84, hematológica 1,75, vômito 1,72 e diabetes 1,65.
  - Diminuem a chance: Sudeste 0,56, cefaleia 0,59 e Centro-Oeste 0,63.
  - A idade dá só 1,07 por década, porque o efeito é em "U" e a logística só desenha uma reta.
- O desempenho é moderado (AUC de 0,75). O modelo serve para triagem, para escolher quem acompanhar primeiro, e não para diagnóstico. A decisão de internar depende de exames e de leitos, que não estão na ficha.

## 3.5 Conclusões

- O pico foi em abril (SE 14).
- Goiás foi o estado mais atingido, em número e por habitante. Na taxa vêm depois Tocantins, Piauí e Espírito Santo.
- Quem mais pega dengue são os adultos jovens. Quem mais interna são as crianças pequenas, os idosos, as gestantes e as pessoas com comorbidades.
- Usando só a ficha de notificação, o modelo encontra 2 de cada 3 internações, mas com muitos alarmes falsos.
- As limitações principais são a subnotificação, os campos vazios que mudam muito entre regiões e os meses recentes ainda incompletos.

## Perguntas que a professora pode fazer

1. **Por que mediana e não média?** Idade e atraso têm assimetria à direita e a média é puxada pelos extremos. O atraso médio é de 4,5 dias e a mediana é 3. A mediana e o IQR não mudam muito com outliers.
2. **Por que dividir pela população?** O total mistura o tamanho do estado com a intensidade da epidemia. São Paulo é o 2º em total, mas por habitante fica abaixo da média.
3. **Os dados representam a dengue no Brasil?** Representam os casos que chegaram a um serviço de saúde e foram notificados. Há subnotificação, diferença entre estados e atraso nas semanas mais recentes.
4. **Por que a curva cai no final?** Por causa do atraso de digitação nas últimas semanas. A epidemia não acabou ali.
5. **Por que regressão logística?** O problema é de sim ou não, e a logística é simples, rápida e dá para explicar pela razão de chances. A árvore deu praticamente o mesmo resultado.
6. **Se o baseline tem 91% de acurácia, por que ele é pior?** Porque nunca encontra um hospitalizado (recall 0). Com classes desbalanceadas olhamos recall, F1 e ROC-AUC.
7. **O que é vazamento de dados e o que vocês fizeram?** É usar uma informação que só existe depois do evento que queremos prever. Tiramos a data de internação, a evolução, o óbito, a classificação final, os sinais de alarme e de gravidade e os exames.
8. **Uma precisão de 0,17 não é ruim?** É baixa, mas é o dobro da taxa base (8,6%). A ideia é fazer triagem, e preferimos ter alarmes falsos a deixar passar quem vai internar (recall de 0,67). Mudando o limiar dá para trocar recall por precisão.
9. **Por que tiraram os registros sem hospitalização?** Sem a resposta certa não dá para treinar nem avaliar. A consequência é que o modelo só vale para fichas preenchidas.
10. **Como reproduzir?** Rodamos o notebook do RA1, que gera o Parquet, e depois `jupyter nbconvert --to notebook --execute --inplace ra3/ra3_dengue_2026.ipynb`. Com a semente fixa os números saem iguais.
