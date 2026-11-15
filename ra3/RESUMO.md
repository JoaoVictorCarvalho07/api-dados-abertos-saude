# RA3 — Resumo para estudar a apresentação

Texto de apoio para o grupo explicar o RA3 em 18/11. Todos os números abaixo saem do notebook `ra3/ra3_dengue_2026.ipynb` executado.

## O que entregamos

| Arquivo | O que é |
|---|---|
| `ra3/ra3_dengue_2026.ipynb` | Notebook do RA3, seguindo as seções 3.1 a 3.5 do template da disciplina |
| `ra3/figuras/` | As 5 figuras do notebook em PNG |
| `ra3/populacao_uf_censo2022.csv` | População por UF do Censo 2022 (IBGE, tabela SIDRA 4709), usada para calcular a taxa por 100 mil habitantes |
| `ra3/RESUMO.md` | Este texto |

O notebook lê o Parquet gerado no RA1 (`dados/preparados/dengue_brasil_2026.parquet`, 470.221 notificações). Para o modelo, ele também lê do arquivo bruto as colunas de sintomas e comorbidades, ligadas pela posição original da linha (`id_registro`).

## 3.1 Estatística descritiva

**O que faz:** resume duas variáveis numéricas (idade e atraso entre sintomas e notificação) e conta as categorias de gravidade.

| Medida | Idade (anos) | Atraso (dias) |
|---|---|---|
| Média | 31,6 | 4,5 |
| Mediana | 29 | 3 |
| Desvio-padrão | 19,2 | 8,6 |
| Q1 – Q3 (IQR) | 17 – 44 (27) | 1 – 5 (4) |
| Mínimo – máximo (amplitude) | 0 – 120 (120) | 0 – 238 (238) |
| Assimetria | 0,55 | 9,16 |

- **Tendência central** (média, mediana) diz qual é o valor típico. **Dispersão** (desvio-padrão, amplitude, IQR) diz o quanto os valores variam. **Distribuição** (quartis, assimetria, histograma) diz o formato.
- **Por que mediana e IQR?** As duas variáveis têm cauda à direita: alguns idosos e alguns atrasos enormes puxam a média para cima. A mediana é o valor do meio e o IQR é a faixa onde ficam os 50% centrais. Nenhum dos dois muda por causa de poucos valores extremos.
- Assimetria maior que 0 significa cauda à direita. 0,55 é leve (idade); 9,16 é muito forte (atraso).
- 89,3% das notificações saem em até 7 dias; 2.442 (0,5%) passam de 60 dias.
- Classificação final: dengue 75,0%, inconclusivo 14,9%, sem classificação 7,4%, com sinais de alarme 2,6%, grave 0,2%. Entre os 365.519 confirmados, 3,5% são graves ou com sinais de alarme.
- Hospitalização: 8,6% das 346.623 notificações com o campo preenchido. O campo está vazio em 26,3% das notificações.
- Faixa etária mais notificada: 15–29 anos (32,0%).

## 3.2 Visualizações e como ler cada uma

1. **Figura 1, linha por semana epidemiológica.** Eixo X é a semana do início dos sintomas, eixo Y o número de notificações. O pico é a SE 14 (início de abril), com 20.520 notificações. Metade do ano está em 13 das 39 semanas. A queda na última semana (SE 39, com 3.440) é atraso de digitação, não fim da epidemia; por isso a faixa cinza.
2. **Figura 2, barras por UF.** À esquerda está o total; à direita, a taxa por 100 mil habitantes. Goiás lidera nas duas medidas (115.161 notificações; 1.632 por 100 mil, sete vezes a taxa do Brasil, de 231,5). São Paulo é o 2º em total, mas fica abaixo da média na taxa (153,9). **Lição:** comparar estados de tamanhos diferentes só faz sentido por habitante.
3. **Figura 3, histograma da idade e boxplot por hospitalização.** O histograma mostra a concentração entre 15 e 30 anos e a cauda de idosos. No boxplot, a linha do meio é a mediana, a caixa vai do Q1 ao Q3 e as hastes mostram a extensão sem os outliers. As medianas são quase iguais (30 x 29 anos), mas a caixa dos hospitalizados é bem mais larga (15 a 50 anos contra 18 a 44).
4. **Figura 4, percentual de hospitalização por faixa etária.** Tem forma de "U": 13,1% em 0–4 anos, cerca de 7% entre 15 e 44 anos e 22,2% acima de 75 anos. Quem mais adoece são os jovens, mas quem mais interna são os extremos de idade.
5. **Figura 5, matriz de confusão do modelo** (explicada na seção 3.4).

## 3.3 Representatividade (sem amostragem)

- **Origem:** Sinan, vigilância **passiva**. Só entra quem procurou atendimento e teve a ficha preenchida. Cada linha é uma **notificação**, não uma pessoa nem um caso confirmado.
- **Abrangência:** 27 UFs, de 04/01 a 04/10/2026. Usamos todas as notificações, sem amostragem; o único sorteio é a divisão treino/teste do modelo.
- **Limitações e vieses:**
  1. Subnotificação, porque casos leves e assintomáticos não aparecem.
  2. Cada UF notifica com intensidade e qualidade diferentes.
  3. Atraso: as notificações sem classificação são 1,1% em junho, 35,5% em agosto, 65,9% em setembro e 86,2% em outubro.
  4. Campos vazios: hospitalização 26,3% e evolução 28,6%, indo de 19,0% (Centro-Oeste) a 46,2% (Sul).
  5. O arquivo público não traz nenhum caso descartado, e 14,9% estão como inconclusivos.
  6. 5.797 linhas estão marcadas como possível duplicata.

## 3.4 Modelo de Machine Learning em palavras simples

- **Pergunta:** olhando só a ficha de notificação, dá para prever se o paciente **vai ser hospitalizado**? É uma **classificação** (sim/não).
- **Target (alvo):** a coluna que queremos prever, `hospitalizado`. Só usamos as 346.623 notificações em que ela está preenchida.
- **Features (características):** as 31 colunas usadas para prever: idade, atraso, sexo, gestante, 14 sintomas, 7 comorbidades, indicador de ficha clínica vazia e região de residência.
- **Vazamento de dados (*leakage*):** é usar como feature uma informação que só existe depois do que queremos prever. Seria como "prever" a internação usando a data da internação. Por isso tiramos `DT_INTERNA`, `EVOLUCAO`, `DT_OBITO`, `CLASSI_FIN`, `CRITERIO`, `DT_ENCERRA`, sinais de alarme (`ALRM_*`), sinais de gravidade (`GRAV_*`) e resultados de exames.
- **Treino e teste:** 80% para o modelo aprender (277.298) e 20% guardados para avaliar (69.325). A divisão é **estratificada**, então as duas partes têm 8,6% de hospitalizados, e a semente é fixa (42), então dá sempre o mesmo resultado.
- **Modelos:**
  - *Baseline*, que sempre diz "não interna". Serve de régua mínima.
  - **Regressão logística**, o modelo principal. É simples e mostra o peso de cada variável.
  - Árvore de decisão rasa, para comparar.
  - Nos dois modelos de verdade usamos `class_weight="balanced"`, para o modelo não ignorar a classe rara.
- **Por que não só acurácia?** Como 91,4% não internam, o *baseline* tem 91,4% de acurácia sem acertar nenhum hospitalizado. A acurácia engana quando as classes são desbalanceadas.
  - **Recall:** dos que realmente internaram, quantos o modelo encontrou.
  - **Precisão:** dos que o modelo sinalizou, quantos realmente internaram.
  - **F1:** a média harmônica entre recall e precisão.
  - **ROC-AUC:** a chance de o modelo dar risco maior a um paciente que interna do que a um que não interna. 0,5 é sorteio e 1,0 é perfeito.

| Modelo | Acurácia | Precisão | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Baseline | 0,914 | 0,000 | 0,000 | 0,000 | 0,500 |
| **Regressão logística** | 0,699 | 0,174 | **0,669** | 0,276 | **0,747** |
| Árvore de decisão | 0,678 | 0,168 | 0,698 | 0,271 | 0,744 |
| Logística sem leucopenia | 0,680 | 0,163 | 0,663 | 0,262 | 0,730 |

- **Matriz de confusão (logística):**
  - Dos 5.938 hospitalizados do teste, o modelo achou 3.971 e deixou passar 1.967.
  - Gerou 18.870 alarmes falsos entre os 63.387 que não internaram.
  - De cada 100 pacientes sinalizados, cerca de 17 internam, o dobro da taxa geral de 8,6%.
- **Razão de chances:** quanto a chance de internar é multiplicada quando a variável é "sim".
  - Aumentam a chance: leucopenia 4,08, gestante 2,62, Nordeste 1,91, doença autoimune 1,90, renal 1,84, hematológica 1,75, vômito 1,72 e diabetes 1,65.
  - Reduzem a chance: Sudeste 0,56, cefaleia 0,59 e Centro-Oeste 0,63.
  - Idade: só 1,07 por década, porque o efeito é em "U" e a logística desenha uma reta.
- **Leitura honesta:** o desempenho é **moderado** (AUC 0,75). O modelo serve para **triagem**, para priorizar quem acompanhar, e não para diagnóstico. A decisão de internar depende de exames e de leitos, que não estão na ficha.

## 3.5 Conclusões em uma frase cada

- **Quando:** pico em abril (SE 14).
- **Onde:** Goiás, em número e por habitante, seguido de Tocantins, Piauí e Espírito Santo na taxa.
- **Quem:** quem mais adoece são os adultos jovens; quem mais interna são as crianças pequenas, os idosos, as gestantes e as pessoas com comorbidades.
- **Modelo:** encontra 2 em cada 3 internações usando só a ficha de notificação, com muitos alarmes falsos.
- **Limitações:** subnotificação, campos vazios desiguais entre regiões e meses recentes incompletos.

## Perguntas prováveis da professora

1. **Por que mediana e não média?** Idade e atraso são assimétricos à direita, e a média é puxada pelos extremos (atraso médio de 4,5 dias contra mediana de 3). A mediana e o IQR são robustos a outliers.
2. **Por que dividir pela população?** O total mistura tamanho do estado com intensidade da epidemia. São Paulo é o 2º em total, mas fica abaixo da média por habitante.
3. **Os dados representam a dengue no Brasil?** Representam os casos que chegaram ao serviço de saúde e foram notificados. Há subnotificação, diferença entre estados e atraso nas semanas recentes.
4. **Por que a curva cai no final?** É atraso de digitação nas últimas semanas, não fim da epidemia.
5. **Por que regressão logística?** É um problema sim/não, o modelo é simples, rápido e interpretável pela razão de chances. A árvore deu praticamente o mesmo resultado.
6. **Por que o baseline tem 91% de acurácia e mesmo assim é pior?** Porque ele nunca encontra um hospitalizado (recall 0). Com classes desbalanceadas, olhamos recall, F1 e ROC-AUC.
7. **O que é vazamento de dados e o que vocês fizeram?** É usar informação posterior ao evento previsto. Excluímos data de internação, evolução, óbito, classificação final, sinais de alarme e de gravidade e exames.
8. **A precisão de 0,17 não é ruim?** É baixa, mas é o dobro da taxa base (8,6%). O objetivo é triagem: preferimos alarmes falsos a deixar passar quem vai internar (recall 0,67). Ajustar o limiar troca recall por precisão.
9. **Por que tiraram os vazios de hospitalização?** Sem a resposta certa não dá para treinar nem avaliar. A limitação é que o modelo vale para as fichas preenchidas.
10. **Como reproduzir?** Rode o notebook do RA1 (que gera o Parquet) e depois `jupyter nbconvert --to notebook --execute --inplace ra3/ra3_dengue_2026.ipynb`. A semente fixa garante os mesmos números.
