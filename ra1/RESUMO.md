# RA1 — Resumo da entrega

Commit `01e96a5` na branch `master` de
[api-dados-abertos-saude](https://github.com/JoaoVictorCarvalho07/api-dados-abertos-saude).

## Recorte

- Fonte: `DENGBR26.csv.zip`, conjunto [Sinan/Dengue](https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue) do Portal de Dados Abertos do SUS.
- Notificações de dengue de todo o Brasil em 2026: 470.451 linhas, 121 colunas, de 04/01 a 04/10/2026.
- O zip na raiz do repositório é idêntico, byte a byte, ao arquivo do portal.

## O que está no repositório

| Arquivo | Etapa do documento | O que faz |
|---|---|---|
| `ra1/config.py` | — | Caminhos, URL oficial e limites das regras |
| `ra1/dominios.py` | — | Tradução dos códigos do SINAN |
| `ra1/relatorio.py` | — | Grava os relatórios em Markdown |
| `ra1/ingestao.py` | 02 — Fontes e ingestão | Carrega o CSV como texto e confere se todas as linhas foram lidas |
| `ra1/qualidade.py` | 03 — Compreensão e qualidade | Roda 22 verificações (Q1–Q22) sobre o dado bruto |
| `ra1/limpeza.py` | 04 e 05 — Limpeza e resultado | Aplica as decisões D1–D11, valida com 12 regras e grava o Parquet |
| `ra1/saidas/` | Evidências | Relatórios gerados pelos três scripts |
| `requirements.txt` | 06 — Reprodutibilidade | Versões fixas de pandas, pyarrow e tabulate |

Também saíram do repositório `coletar_amostras.py` e `gerar_amostra.py`.

## Resultado

| Medida | Após ingestão | Após preparação |
|---|---|---|
| Registros | 470.451 | 470.221 |
| Atributos | 121 | 24 |
| Duplicatas exatas | 230 | 0 |
| `CLASSI_FIN` fora do domínio | 4.318 | 0 |

Arquivo preparado: `dados/preparados/dengue_brasil_2026.parquet`. Ele não vai para o GitHub; é gerado ao rodar os scripts.

## Principais achados de qualidade

- **`CLASSI_FIN = 0`:** 4.318 casos, todos do Espírito Santo (21% das notificações do estado). O ES grava o vazio como `0`.
- **Sem classificação final:** 30.577 casos (6,5%), ainda em investigação porque o ano não terminou.
- **Possíveis duplicatas:** 2.925. Sem identificador de paciente, não dá para confirmar.
- **Atraso acima de 60 dias** entre sintomas e notificação: 2.442 casos (mediana de 3 dias).
- **Comorbidades sem informação:** cerca de 3,2% em diabetes e hipertensão.

Quase nenhuma decisão apaga linhas: só as 230 cópias exatas saem. Os demais problemas viram vazio ou uma coluna de sinalização, e cada pergunta decide como tratá-los.

## Como reproduzir

Na raiz do repositório (Windows, Python 3.11):

```bash
py -3.11 -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe ra1/ingestao.py
.venv/Scripts/python.exe ra1/qualidade.py
.venv/Scripts/python.exe ra1/limpeza.py
```

## Pendências

1. Conferir os códigos de `ra1/dominios.py` no `dic_dados_dengue.pdf`: `CLASSI_FIN`, `CRITERIO`, `EVOLUCAO` e a unidade de `NU_IDADE_N`.
2. Decidir se a P1 usa a UF de residência (`uf_residencia`) ou a de notificação (`uf_notificacao`).
3. Completar no documento as variáveis da P2 (`sexo`, `caso_grave`) e corrigir as da P3 (`faixa_etaria`, `caso_grave`, `diabetes`, `hipertensao`).
4. Decidir o que fazer com `ANALISE_QUALIDADE.md` (amostra do PR 2024), `FORMATOS.md` e `swagger.json`.
