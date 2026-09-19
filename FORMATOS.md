# Formato das respostas — API de Dados Abertos do Ministério da Saúde

Fonte: https://apidadosabertos.saude.gov.br/v1/ · spec: https://apidadosabertos.saude.gov.br/static/swagger.json · coletado em 2026-09-18 21:57

Rotas que respondem 200 com lista vazia (sem dado publicado, formato do registro desconhecido):

- `/saude-indigena/acompanhamento-obra-infraestrutura-saude`
- `/atencao-primaria/pmmb-relatorio-historico-cadastro-cnes`
- `/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-nascidos-vivos`
- `/saude-indigena/sesai-hepatites-virais`
- `/saude-indigena/sesai-obitos`
- `/ciencia-tecnologia/plataformabr-pesquisa-saude`
- `/ciencia-tecnologia/plataformabr-projeto-aprovado`

Rotas que exigem filtro, chamadas com um valor fixo:

- `/economia-da-saude/bps`: `{'codigoCatmat': '267512'}`

| Rota | HTTP | Registros | Segundos |
|---|---|---|---|
| `/cnes/tipounidades` | 200 | 39 | 0.3 |
| `/cnes/tipounidades/{codigo_tipo_unidade}` | 200 | 0 | 0.2 |
| `/cnes/estabelecimentos` | 200 | 20 | 0.4 |
| `/cnes/estabelecimentos/{codigo_cnes}` | 200 | 0 | 0.4 |
| `/sisagua/vigilancia-parametros-basicos` | 200 | 100 | 0.7 |
| `/sisagua/controle-semestral` | 200 | 100 | 0.6 |
| `/sisagua/controle-mensal-parametros-basicos` | 200 | 100 | 0.6 |
| `/sisagua/pontos-de-captacao` | 200 | 100 | 0.5 |
| `/sisagua/cadastro-carro-pipa-populacao` | 200 | 100 | 0.5 |
| `/sisagua/cadastro-carro-pipa-procedencia` | 200 | 100 | 0.4 |
| `/sisagua/controle-mensal-amostras-fora-do-padrao` | 200 | 100 | 0.5 |
| `/sisagua/controle-mensal-demais-parametros` | 200 | 100 | 0.7 |
| `/sisagua/controle-mensal-infraestrutura-operacional` | 200 | 100 | 0.6 |
| `/sisagua/controle-mensal-plano-amostragem` | 200 | 100 | 0.7 |
| `/sisagua/populacao-abastecida` | 200 | 100 | 0.9 |
| `/sisagua/tratamento-de-agua` | 200 | 100 | 0.9 |
| `/sisagua/vigilancia-cianobacterias-e-cianotoxinas` | 200 | 100 | 0.5 |
| `/sisagua/vigilancia-demais-parametros` | 200 | 100 | 0.8 |
| `/sisvan/estado-nutricional` | 200 | 20 | 0.4 |
| `/arboviroses/zikavirus` | 200 | 100 | 0.4 |
| `/arboviroses/dengue` | 200 | 100 | 1.2 |
| `/arboviroses/chikungunya` | 200 | 100 | 0.8 |
| `/daf/estoque-medicamentos-bnafar-horus` | 200 | 100 | 0.7 |
| `/macrorregiao-e-regiao-de-saude/municipio` | 200 | 100 | 0.4 |
| `/assistencia-a-saude/hospitais-e-leitos` | 200 | 100 | 0.7 |
| `/vacinacao/doses-aplicadas-pni-2020` | 200 | 100 | 0.7 |
| `/vacinacao/doses-aplicadas-pni-2021` | 200 | 100 | 0.7 |
| `/vacinacao/doses-aplicadas-pni-2022` | 200 | 100 | 0.7 |
| `/vacinacao/doses-aplicadas-pni-2023` | 200 | 100 | 0.6 |
| `/vacinacao/doses-aplicadas-pni-2024` | 200 | 100 | 0.8 |
| `/vacinacao/doses-aplicadas-pni-2025` | 200 | 100 | 0.9 |
| `/vacinacao/doses-aplicadas-pni-2026` | 200 | 100 | 0.9 |
| `/economia-da-saude/bps` | 200 | 100 | 0.6 |
| `/economia-da-saude/sistema-de-apuracao-e-gestao-de-custos-do-sus-apurasus` | 200 | 100 | 0.5 |
| `/outros-temas/ced` | 200 | 100 | 0.3 |
| `/prevencao-e-promocao/distribuicao-epi-insumo` | 200 | 100 | 0.4 |
| `/saude-indigena/sasisus-esgotamento-sanitario` | 200 | 35 | 0.4 |
| `/saude-indigena/sasi-sus-gerenciamento-de-residuos-solidos` | 200 | 35 | 0.6 |
| `/saude-indigena/acompanhamento-obra-infraestrutura-saude` | 200 | 0 | 0.3 |
| `/saude-indigena/planilha-de-fornecimento-e-monitoramento-da-qualidade-da-agua-acesso-a-agua` | 200 | 34 | 0.4 |
| `/saude-indigena/planilha-registros-habilitacao-recebimento-incentivo` | 200 | 100 | 0.3 |
| `/saude-indigena/indicadores-enfrentamento-monitoramento-covid19-indigenas` | 200 | 100 | 0.4 |
| `/saude-indigena/sistema-de-atencao-a-saude-indigena-modulo-de-vigilancia-alimentar-e-nutricional` | 200 | 100 | 0.6 |
| `/atencao-primaria/enani-2019` | 200 | 10 | 0.9 |
| `/atencao-primaria/pmmb-consolidado` | 200 | 100 | 0.7 |
| `/educacao-em-saude/pvc` | 200 | 100 | 0.3 |
| `/atencao-primaria/pmmb-serie-historica` | 200 | 100 | 0.4 |
| `/atencao-primaria/pmmb-relacao-nominal-coparticipacao` | 200 | 100 | 0.3 |
| `/atencao-primaria/pmmb-relatorio-historico-cadastro-cnes` | 200 | 0 | 0.3 |
| `/atencao-primaria/pmmb-especialista-consolidado` | 200 | 100 | 0.5 |
| `/atencao-primaria/pmmb-especialista-serie-historica` | 200 | 100 | 0.5 |
| `/atencao-primaria/pmmb-relacao-nominal-ativo` | 200 | 100 | 0.5 |
| `/vacinacao/esavi` | 200 | 100 | 0.9 |
| `/vacinacao/sistema-de-informacao-de-insumos-estrategicos` | 200 | 100 | 0.3 |
| `/arboviroses/febre-amarela-humanos-primatas-nao-humanos` | 200 | 100 | 0.3 |
| `/arboviroses/febre-amarela-epzootias` | 200 | 100 | 0.4 |
| `/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2020` | 200 | 100 | 0.7 |
| `/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2021` | 200 | 100 | 0.9 |
| `/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2022` | 200 | 100 | 0.7 |
| `/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2023` | 200 | 100 | 1.2 |
| `/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2024` | 200 | 100 | 1.0 |
| `/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-mortalidade` | 200 | 100 | 1.0 |
| `/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-nascidos-vivos` | 200 | 0 | 0.3 |
| `/vigilancia-e-meio-ambiente/srag-2009-2012` | 200 | 100 | 1.0 |
| `/vigilancia-e-meio-ambiente/srag-2013-2018` | 200 | 100 | 0.9 |
| `/vigilancia-e-meio-ambiente/srag-2019-2026` | 200 | 100 | 1.2 |
| `/vigilancia-e-meio-ambiente/mpox` | 200 | 100 | 0.7 |
| `/assistencia-a-saude/unidade-basicas-de-saude` | 200 | 100 | 0.3 |
| `/saude-indigena/siasi-acompanhamento-gestacional` | 200 | 100 | 0.6 |
| `/saude-indigena/siasi-modulo-morbidades` | 200 | 100 | 0.6 |
| `/saude-indigena/sesai-atendimentos` | 200 | 99 | 0.5 |
| `/saude-indigena/sesai-recursos-humanos` | 200 | 99 | 0.4 |
| `/saude-indigena/siasi-modulo-saude-bucal-ficha3` | 200 | 100 | 0.5 |
| `/saude-indigena/siasi-modulo-saude-bucal-ficha4` | 200 | 100 | 0.6 |
| `/saude-indigena/siasi-modulo-saude-bucal-ficha7` | 200 | 100 | 0.6 |
| `/saude-indigena/sesai-acidentes-ofidicos` | 200 | 100 | 0.3 |
| `/saude-indigena/sesai-arboviroses` | 200 | 100 | 0.4 |
| `/saude-indigena/sesai-assistencia-farmaceutica` | 200 | 100 | 0.3 |
| `/saude-indigena/sesai-cobertura-vacinal` | 200 | 100 | 0.4 |
| `/saude-indigena/sesai-covid19` | 200 | 100 | 0.5 |
| `/saude-indigena/sesai-demografico` | 200 | 100 | 0.5 |
| `/saude-indigena/sesai-doencas-diarreicas-agudas` | 200 | 100 | 0.4 |
| `/saude-indigena/sesai-doencas-imunopreveniveis` | 200 | 100 | 0.4 |
| `/saude-indigena/sesai-doencas-zoonoticas` | 200 | 100 | 0.4 |
| `/saude-indigena/sesai-hepatites-virais` | 200 | 0 | 0.3 |
| `/saude-indigena/sesai-obitos` | 200 | 0 | 0.3 |
| `/saude-indigena/sesai-doencas-respiratorias` | 200 | 100 | 0.5 |
| `/ciencia-tecnologia/dgits-contribuicoes-consultas-publicas` | 200 | 100 | 0.3 |
| `/ciencia-tecnologia/dgits-controle-demandas-conitec` | 200 | 100 | 0.3 |
| `/ciencia-tecnologia/dgits-controle-pcdt` | 200 | 83 | 0.3 |
| `/ciencia-tecnologia/dgits-tecnologias-diretrizes` | 200 | 10 | 0.3 |
| `/ciencia-tecnologia/plataformabr-pesquisa-saude` | 200 | 0 | 0.3 |
| `/ciencia-tecnologia/plataformabr-projeto-aprovado` | 200 | 0 | 0.3 |
| `/ouvidoria/ouvidor2` | 200 | 100 | 0.5 |
| `/ouvidoria/ouvidor3` | 200 | 100 | 0.5 |
| `/assistencia-a-saude/registro-de-ocupacao-hospitalar-covid-19` | 200 | 100 | 0.5 |
| `/atencao-primaria/cadastro-vinculado-programa-previne-brasil` | 200 | 100 | 0.3 |
| `/atencao-primaria/indicador-desempenho-programa-previne-brasil` | 200 | 100 | 0.5 |
| `/atencao-primaria/pmmb-especialista-relacao-nominal-ativo` | 200 | 100 | 0.4 |
| `/atencao-primaria/pmme-instituicoes-formadoras` | 200 | 100 | 0.4 |
| `/atencao-primaria/siaps-atendimento-individual` | 200 | 100 | 0.5 |
| `/assistencia-a-saude/cnes-equipamentos` | 200 | 1 | 0.3 |
| `/assistencia-a-saude/cnes-estabelecimentos` | 200 | 3 | 0.3 |
| `/assistencia-a-saude/cnes-leitos` | 200 | 1 | 0.3 |
| `/assistencia-a-saude/cnes-profissionais` | 200 | 1 | 0.3 |
| `/assistencia-a-saude/cnes-servicos-especializados` | 200 | 3 | 0.3 |
| `/assistencia-a-saude/sia-procedimentos-ambulatoriais` | 200 | 1 | 0.3 |
| `/assistencia-a-saude/sih-procedimentos-hospitalares` | 200 | 1 | 0.3 |
| `/atencao-primaria/siaps-cadastro-individual` | 200 | 100 | 0.5 |

## `/cnes/tipounidades`

Obtém todos os tipos de unidade.

- URL: `https://apidadosabertos.saude.gov.br/cnes/tipounidades`
- HTTP: 200
- Envelope: `{"tipos_unidade": "array[39]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `codigo_tipo_unidade` | integer | `80` |
| `descricao_tipo_unidade` | string | `"LABORATORIO DE SAUDE PUBLICA"` |

## `/cnes/tipounidades/{codigo_tipo_unidade}`

Obtém tipo de unidade utilizando o código do tipo da unidade.

- URL: `https://apidadosabertos.saude.gov.br/cnes/tipounidades/80`
- HTTP: 200
- Envelope: `{"codigo_tipo_unidade": 80, "descricao_tipo_unidade": "LABORATORIO DE SAUDE PUBLICA"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `codigo_tipo_unidade` | integer | `80` |
| `descricao_tipo_unidade` | string | `"LABORATORIO DE SAUDE PUBLICA"` |

## `/cnes/estabelecimentos`

Obtém todos os estabelecimentos.

- URL: `https://apidadosabertos.saude.gov.br/cnes/estabelecimentos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"estabelecimentos": "array[20]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `codigo_cnes` | integer | `9629866` |
| `numero_cnpj_entidade` | null | `null` |
| `nome_razao_social` | string | `"FERNANDO NUNES AGUIAR"` |
| `nome_fantasia` | string | `"FERNANDO NUNES AGUIAR"` |
| `natureza_organizacao_entidade` | null | `null` |
| `tipo_gestao` | string | `"M"` |
| `descricao_nivel_hierarquia` | null | `null` |
| `descricao_esfera_administrativa` | string | `"MUNICIPAL"` |
| `codigo_tipo_unidade` | integer | `22` |
| `codigo_cep_estabelecimento` | string | `"27910000"` |
| `endereco_estabelecimento` | string | `"RUA TEIXEIRA DE GOUVEIA"` |
| `numero_estabelecimento` | string | `"1536"` |
| `bairro_estabelecimento` | string | `"CENTRO"` |
| `numero_telefone_estabelecimento` | null \| string | `"(22) 2765-5417"` |
| `latitude_estabelecimento_decimo_grau` | number | `-22.381815423315402` |
| `longitude_estabelecimento_decimo_grau` | number | `-41.777400970458984` |
| `endereco_email_estabelecimento` | null \| string | `"fernando.nunesaguiar@gmail.com"` |
| `numero_cnpj` | null \| string | `"24072393000107"` |
| `codigo_identificador_turno_atendimento` | string | `"01"` |
| `descricao_turno_atendimento` | string | `"ATENDIMENTO SOMENTE PELA MANHA"` |
| `estabelecimento_faz_atendimento_ambulatorial_sus` | string | `"NAO"` |
| `codigo_estabelecimento_saude` | string | `"3302409629866"` |
| `codigo_uf` | integer | `33` |
| `codigo_municipio` | integer | `330240` |
| `descricao_natureza_juridica_estabelecimento` | string | `"4000"` |
| `codigo_motivo_desabilitacao_estabelecimento` | null \| string | `"04"` |
| `estabelecimento_possui_centro_cirurgico` | integer | `0` |
| `estabelecimento_possui_centro_obstetrico` | integer | `0` |
| `estabelecimento_possui_centro_neonatal` | integer | `0` |
| `estabelecimento_possui_atendimento_hospitalar` | integer | `0` |
| `estabelecimento_possui_servico_apoio` | integer | `0` |
| `estabelecimento_possui_atendimento_ambulatorial` | integer | `0` |
| `codigo_atividade_ensino_unidade` | string | `"04"` |
| `codigo_natureza_organizacao_unidade` | null | `null` |
| `codigo_nivel_hierarquia_unidade` | null | `null` |
| `codigo_esfera_administrativa_unidade` | string | `"M "` |
| `data_atualizacao` | string | `"2025-09-03"` |

## `/cnes/estabelecimentos/{codigo_cnes}`

Obtém estabelecimento utilizando o código CNES.

- URL: `https://apidadosabertos.saude.gov.br/cnes/estabelecimentos/9629866`
- HTTP: 200
- Envelope: `{"codigo_cnes": 9629866, "numero_cnpj_entidade": null, "nome_razao_social": "FERNANDO NUNES AGUIAR", "nome_fantasia": "FERNANDO NUNES AGUIAR", "natureza_organizacao_entidade": null, "tipo_gestao": "M", "descricao_nivel_hierarquia": null, "descricao_esfera_administrativa": "MUNICIPAL", "codigo_tipo_unidade": 22, "codigo_cep_estabelecimento": "27910000", "endereco_estabelecimento": "RUA TEIXEIRA DE GOUVEIA", "numero_estabelecimento": "1536", "bairro_estabelecimento": "CENTRO", "numero_telefone_estabelecimento": "(22) 2765-5417", "latitude_estabelecimento_decimo_grau": -22.381815423315402, "longitude_estabelecimento_decimo_grau": -41.777400970458984, "endereco_email_estabelecimento": "fernando.nunesaguiar@gmail.com", "numero_cnpj": null, "codigo_identificador_turno_atendimento": "01", "descricao_turno_atendimento": "ATENDIMENTO SOMENTE PELA MANHA", "estabelecimento_faz_atendimento_ambulatorial_sus": "NAO", "codigo_estabelecimento_saude": "3302409629866", "codigo_uf": 33, "codigo_municipio": 330240, "descricao_natureza_juridica_estabelecimento": "4000", "codigo_motivo_desabilitacao_estabelecimento": null, "estabelecimento_possui_centro_cirurgico": 0, "estabelecimento_possui_centro_obstetrico": 0, "estabelecimento_possui_centro_neonatal": 0, "estabelecimento_possui_atendimento_hospitalar": 0, "estabelecimento_possui_servico_apoio": 0, "estabelecimento_possui_atendimento_ambulatorial": 0, "codigo_atividade_ensino_unidade": "04", "codigo_natureza_organizacao_unidade": null, "codigo_nivel_hierarquia_unidade": null, "codigo_esfera_administrativa_unidade": "M ", "data_atualizacao": "2025-09-03"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `codigo_cnes` | integer | `9629866` |
| `numero_cnpj_entidade` | null | `null` |
| `nome_razao_social` | string | `"FERNANDO NUNES AGUIAR"` |
| `nome_fantasia` | string | `"FERNANDO NUNES AGUIAR"` |
| `natureza_organizacao_entidade` | null | `null` |
| `tipo_gestao` | string | `"M"` |
| `descricao_nivel_hierarquia` | null | `null` |
| `descricao_esfera_administrativa` | string | `"MUNICIPAL"` |
| `codigo_tipo_unidade` | integer | `22` |
| `codigo_cep_estabelecimento` | string | `"27910000"` |
| `endereco_estabelecimento` | string | `"RUA TEIXEIRA DE GOUVEIA"` |
| `numero_estabelecimento` | string | `"1536"` |
| `bairro_estabelecimento` | string | `"CENTRO"` |
| `numero_telefone_estabelecimento` | string | `"(22) 2765-5417"` |
| `latitude_estabelecimento_decimo_grau` | number | `-22.381815423315402` |
| `longitude_estabelecimento_decimo_grau` | number | `-41.777400970458984` |
| `endereco_email_estabelecimento` | string | `"fernando.nunesaguiar@gmail.com"` |
| `numero_cnpj` | null | `null` |
| `codigo_identificador_turno_atendimento` | string | `"01"` |
| `descricao_turno_atendimento` | string | `"ATENDIMENTO SOMENTE PELA MANHA"` |
| `estabelecimento_faz_atendimento_ambulatorial_sus` | string | `"NAO"` |
| `codigo_estabelecimento_saude` | string | `"3302409629866"` |
| `codigo_uf` | integer | `33` |
| `codigo_municipio` | integer | `330240` |
| `descricao_natureza_juridica_estabelecimento` | string | `"4000"` |
| `codigo_motivo_desabilitacao_estabelecimento` | null | `null` |
| `estabelecimento_possui_centro_cirurgico` | integer | `0` |
| `estabelecimento_possui_centro_obstetrico` | integer | `0` |
| `estabelecimento_possui_centro_neonatal` | integer | `0` |
| `estabelecimento_possui_atendimento_hospitalar` | integer | `0` |
| `estabelecimento_possui_servico_apoio` | integer | `0` |
| `estabelecimento_possui_atendimento_ambulatorial` | integer | `0` |
| `codigo_atividade_ensino_unidade` | string | `"04"` |
| `codigo_natureza_organizacao_unidade` | null | `null` |
| `codigo_nivel_hierarquia_unidade` | null | `null` |
| `codigo_esfera_administrativa_unidade` | string | `"M "` |
| `data_atualizacao` | string | `"2025-09-03"` |

## `/sisagua/vigilancia-parametros-basicos`

Obtém lista de parâmetros básicos de vigilância das instituições

- URL: `https://apidadosabertos.saude.gov.br/sisagua/vigilancia-parametros-basicos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"parametros": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `regiao_geografica` | string | `"NORDESTE"` |
| `uf` | string | `"PE"` |
| `regional_de_saude` | string | `"I REGIONAL DE SAUDE"` |
| `municipio` | string | `"CABO DE SANTO AGOSTINHO"` |
| `codigo_ibge` | integer \| null | `260290` |
| `numero_da_amostra` | string | `"262092026"` |
| `motivo_da_coleta` | string | `"Rotina"` |
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `codigo_forma_de_abastecimento` | string | `"S260290000003"` |
| `nome_da_forma_de_abastecimento` | string | `"PIRAPAMA"` |
| `nome_da_eta_uta` | null \| string | `"ESTAÇÃO DE TRATAMENTO DE MDO"` |
| `ano` | integer | `2026` |
| `mes` | integer | `9` |
| `data_da_coleta` | string | `"2026-09-15"` |
| `hora_da_coleta` | string | `"14:20"` |
| `data_do_laudo` | string | `"2026-09-16"` |
| `data_de_registro_no_sisagua` | string | `"2026-09-17"` |
| `procedencia_da_coleta` | string | `"SISTEMA DE DISTRIBUIÇÃO"` |
| `ponto_de_coleta` | null \| string | `"Cavalete/Hidrômetro"` |
| `descricao_do_local` | null \| string | `"1ª TRAVESSA DA RUA 53 N. 06"` |
| `zona` | null \| string | `"Urbana"` |
| `categoria_area` | null \| string | `"Bairro"` |
| `area` | null \| string | `"SAO FRANCISCO"` |
| `tipo_do_local` | null \| string | `"Outro"` |
| `local` | null \| string | `"TAPACURA Z 2 D 8 B"` |
| `latitude` | null \| number | `-16.754144` |
| `longitude` | null \| number | `-41.507629` |
| `parametro` | string | `"Turbidez (uT)"` |
| `analise_realizada` | null \| string | `"EM_CAMPO"` |
| `data_da_analise` | null \| string | `"2026-09-15"` |
| `ld` | null | `null` |
| `lq` | null | `null` |
| `resultado` | string | `"0,90"` |
| `providencia` | null | `null` |

## `/sisagua/controle-semestral`

Obtém lista de parâmetros de controle semestral

- URL: `https://apidadosabertos.saude.gov.br/sisagua/controle-semestral?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"parametros": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `regiao_geografica` | string | `"SUDESTE"` |
| `uf` | string | `"SP"` |
| `regional_de_saude` | string | `"GVS XXIX  - SÃO JOSÉ DO RIO PRETO"` |
| `municipio` | string | `"CATANDUVA"` |
| `codigo_ibge` | integer | `351110` |
| `tipo_da_instituicao` | string | `"Serviço Municipal e outros"` |
| `sigla_da_instituicao` | null \| string | `"SABESP"` |
| `nome_da_instituicao` | string | `"SUPERINTENDENCIA DE AGUA E ESGOTO DE CATANDUVA"` |
| `cnpj_da_instituicao` | integer | `10559279000100` |
| `nome_do_escritorio_regional_local` | null \| string | `"LUCIANOPOLIS SABESP"` |
| `cnpj_do_escritorio_regional_local` | integer \| null | `43776517054786` |
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `codigo_forma_de_abastecimento` | string | `"S351110000039"` |
| `nome_da_forma_de_abastecimento` | string | `"ELDORADO"` |
| `nome_da_eta_uta` | null \| string | `"UTA UC4"` |
| `ano_de_referencia` | integer | `2026` |
| `semestre_de_referencia` | integer | `1` |
| `data_de_registro` | string | `"2026-09-13"` |
| `data_de_preenchimento_do_relatorio_semestral` | string | `"2026-05-07"` |
| `data_da_coleta` | string | `"2026-01-26"` |
| `data_da_analise` | string | `"2026-02-03"` |
| `ponto_de_monitoramento` | string | `"SAÍDA DO TRATAMENTO"` |
| `grupo_de_parametros` | string | `"Parâmetros Organolépticos"` |
| `parametro` | string | `"Sulfeto de hidrogênio"` |
| `ld` | null \| number | `0.204` |
| `lq` | null \| number | `0.002` |
| `resultado` | number | `-1.0` |
| `trimestre_de_referencia` | null \| string | `"PRIMEIRO_TRIMESTRE"` |
| `tipo_de_captacao` | null \| string | `"SUBTERRANEO"` |
| `categoria_do_manancial_superficial` | null \| string | `"rio"` |
| `nome_do_manancial_superficial` | null \| string | `"RIO JAGUARI-MIRIM"` |
| `categoria_do_ponto_de_captacao_subterranea` | null \| string | `"POÇO ARTESIANO"` |
| `nome_do_ponto_de_captacao_subterranea` | null \| string | `"P1 - PAULISTANIA"` |
| `amostra` | null \| string | `"AMOSTRA 1"` |
| `unidade` | null \| string | `"mg/L"` |
| `vmp` | null \| string | `"0.05"` |

## `/sisagua/controle-mensal-parametros-basicos`

Obtém lista de parâmetros básicos de controle mensal coletado das instituições.

- URL: `https://apidadosabertos.saude.gov.br/sisagua/controle-mensal-parametros-basicos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"parametros": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `regiao_geografica` | string | `"SUDESTE"` |
| `uf` | string | `"MG"` |
| `regional_de_saude` | string | `"BELO HORIZONTE"` |
| `codigo_ibge` | integer | `314480` |
| `municipio` | string | `"NOVA LIMA"` |
| `tipo_da_instituicao` | string | `"Local"` |
| `sigla_da_instituicao` | null \| string | `"COPASA"` |
| `nome_da_instituicao` | string | `"VALE SA"` |
| `cnpj_da_instituicao` | integer | `33592510000154` |
| `nome_do_escritorio_regional_local` | null \| string | `"DISTRITO DO RIO VERDE"` |
| `cnpj_do_escritorio_regional_local` | integer \| null | `17281106000103` |
| `tipo_da_forma_de_abastecimento` | string | `"SAC"` |
| `codigo_forma_de_abastecimento` | string | `"C314480000046"` |
| `nome_da_forma_de_abastecimento` | string | `"MINA TERMINAL FERROVIÁRIO DE ANDAIME"` |
| `nome_da_eta_uta` | null \| string | `"TMIB"` |
| `tipo_de_filtracao` | null \| string | `"FILTRAÇÃO RÁPIDA"` |
| `ano_de_referencia` | integer | `2022` |
| `mes_de_referencia` | integer | `8` |
| `ponto_de_monitoramento` | string | `"PONTO DE CONSUMO"` |
| `parametro` | string | `"pH"` |
| `campo` | string | `"Número de dados > 9,0"` |
| `valor` | number | `0.0` |

## `/sisagua/pontos-de-captacao`

Dados sobre os pontos de captação de água para consumo humano registrados nos sistemas e soluções alternativas de abastecimento de água cadastrados no SISAGUA.

- URL: `https://apidadosabertos.saude.gov.br/sisagua/pontos-de-captacao?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pontos_de_captacao": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nome_da_forma_de_abastecimento` | string | `"SAA DE CUITEGI"` |
| `codigo_forma_de_abastecimento` | string | `"S250520000001"` |
| `municipio` | string | `"CUITEGI"` |
| `regional_de_saude` | string | `"02 GERENCIA REGIONAL DE SAUDE"` |
| `codigo_do_ibge` | string | `"250520"` |
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `nome_do_escritorio_regional_local` | string | `"CAGEPA COMPANHIA DE AGUA E ESGOTO DA PARAIBA"` |
| `cnpj_do_escritorio_regional_local` | string | `"2168943000153.0"` |
| `categoria_do_manancial_superficial` | string | `"barragem"` |
| `longitude` | string | `"-35,49"` |
| `vazao` | string | `"215.0"` |
| `latitude` | string | `"-6,8547"` |
| `nome_da_instiuicao` | string | `"COMPANHIA DE AGUA E ESGOTO DA PARAIBA"` |
| `regiao_geografica` | string | `"NORDESTE"` |
| `categoria_do_ponto_de_captacao_subterraneo` | null | `null` |
| `tipo_da_instituicao` | string | `"Regional"` |
| `nome_do_manancial_superficial` | string | `"TAUA"` |
| `tipo_de_captacao` | string | `"SUPERFICIAL"` |
| `nome_do_ponto_de_captacao_subterraneo` | null | `null` |
| `uf` | string | `"PB"` |
| `nome_da_eta_uta` | string | `"ETA DE CUITEGÍ"` |
| `ano_de_referencia` | string | `"2014"` |
| `sigla_da_instituicao` | string | `"CAGEPA"` |
| `outorga` | string | `"S"` |

## `/sisagua/cadastro-carro-pipa-populacao`

Dados cadastrais sobre Carros-Pipa utilizados para abastecimento de água para consumo humano, com informações sobre a população atendida por cada um deles

- URL: `https://apidadosabertos.saude.gov.br/sisagua/cadastro-carro-pipa-populacao?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisagua_cadastro_carro_pipa_populacao": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `tipo_de_responsavel` | string | `"PJ"` |
| `numero_da_autorizacao` | string | `"001/2023"` |
| `nome_da_instituicao` | string | `"SECRETARIA DE EDUCACAO E QUALIDADE DE ENSINO DO AMAZONAS"` |
| `codigo_do_carro_pipa` | string | `"P130353000006"` |
| `regiao_geografica` | string | `"NORTE"` |
| `data_inicio_de_autorizacao` | string | `"2024/07/01 00:00:00.000"` |
| `placa` | string | `"JWV7H47"` |
| `finalidade` | string | `"Prestador serviço"` |
| `nome_do_responsavel_pelo_carro_pipa` | string | `null` |
| `municipio` | string | `"PRESIDENTE FIGUEIREDO"` |
| `cnpj_do_escritorio_regionallocal` | string | `"4312419000130.0"` |
| `tipo_da_instituicao` | string | `"Regional"` |
| `sigla_da_instituicao` | string | `"SEDUC"` |
| `regional_de_saude` | string | `"UNICA"` |
| `codigo_ibge` | string | `"130353"` |
| `data_de_preenchimento` | string | `"2024/09/03 00:00:00.000"` |
| `nome_do_escritorio_regionallocal` | string | `"REGIONAL UNICA"` |
| `data_fim_da_autorizacao` | string | `"2024/12/30 00:00:00.000"` |
| `responsavel_pelas_informacoes` | string | `"TASSIANE ALMANDA DE OLIVEIRA"` |
| `uf` | string | `"AM"` |
| `n_de_pessoas_abastecidas_estimativa` | null \| string | `"2000.0"` |
| `data_de_criacao` | string | `"2024/09/26 10:49:03.000"` |
| `cnpj_da_instituicao` | string | `"4312419000130.0"` |

## `/sisagua/cadastro-carro-pipa-procedencia`

SISAGUA - Cadastro Carro Pipa Procedência

- URL: `https://apidadosabertos.saude.gov.br/sisagua/cadastro-carro-pipa-procedencia?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisagua_cadastro_carro_pipa_procedencia": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `c011` | string | `null` |
| `c006` | string | `"PMO6209"` |
| `c009` | string | `"SISTEMA ITAUNA"` |
| `c004` | string | `"230390"` |
| `c003` | string | `"CHAVAL"` |
| `c007` | string | `"SAA"` |
| `c005` | string | `"P230390000002"` |
| `c010` | string | `"2023.0"` |
| `c000` | string | `"NORDESTE"` |
| `c008` | string | `"S230205000001"` |
| `c012` | string | `null` |
| `c001` | string | `"CE"` |
| `c002` | string | `"16 REGIONAL DE SAUDE CAMOCIM"` |

## `/sisagua/controle-mensal-amostras-fora-do-padrao`

Dados detalhados sobre as análises de qualidade da água de responsabilidade dos prestadores de serviço que não atenderam ao padrão de potabilidade, informados em frequência mensal.

- URL: `https://apidadosabertos.saude.gov.br/sisagua/controle-mensal-amostras-fora-do-padrao?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisagua_controle_mensal_amostras_fora_padrao": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `regiao_geografica` | string | `"SUDESTE"` |
| `sigla_da_instituicao` | string | `"SABESP"` |
| `data_de_preenchimento_do_relatorio_mensal` | string | `"2016/01/08 00:00:00.000"` |
| `tipo_da_instituicao` | string | `"Regional"` |
| `latitude` | null \| string | `"-24,0"` |
| `codigo_forma_de_abastecimento` | string | `"S351925000003"` |
| `zona` | string | `"Urbana"` |
| `parametro` | string | `"Bactérias Heterotróficas (UFC/mL)"` |
| `cnpj_da_instituicao` | string | `"43776517000180.0"` |
| `nome_do_escritorio_regionallocal` | string | `"IARAS SABESP"` |
| `ponto_de_monitoramento` | string | `"SISTEMA DE DISTRIBUIÇÃO"` |
| `area` | string | `"CENTRO"` |
| `providencia_do_controle` | string | `"Ajuste na Cloração, inspeção no local e recoleta"` |
| `data_de_registro` | string | `"2016/01/08 00:00:00.000"` |
| `nome_da_forma_de_abastecimento` | string | `"SISTEMA IARAS"` |
| `categoria_area` | string | `"Bairro"` |
| `resultado` | string | `"880"` |
| `local` | string | `"PINHEIRO MACHADO"` |
| `regional_de_saude` | string | `"GVS XVI - BOTUCATU E SGVS XVI AVARÉ"` |
| `mes_de_referencia` | string | `"10"` |
| `endereco` | null \| string | `"226"` |
| `municipio` | string | `"IARAS"` |
| `ano_de_referencia` | string | `"2014"` |
| `nome_da_instituicao` | string | `"COMPANHIA DE SANEAMENTO BASICO DO ESTADO DE SAO PAULO"` |
| `longitude` | null \| string | `"-54,0"` |
| `data_da_coleta` | string | `"2014/10/23 00:00:00.000"` |
| `cnpj_do_escritorio_regionallocal` | string | `"10193181000173.0"` |
| `codigo_ibge` | string | `"351925"` |
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `uf` | string | `"SP"` |
| `tipo_do_local` | string | `"Casa"` |

## `/sisagua/controle-mensal-demais-parametros`

Dados das análises de qualidade da água de média/alta complexidade, realizado pelas instituições responsáveis por SAA e SAC, em frequência mensal ou inferior.

- URL: `https://apidadosabertos.saude.gov.br/sisagua/controle-mensal-demais-parametros?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisagua_controle_mensal_demais_parametros": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `nome_da_forma_de_abastecimento` | string | `"CACIQUE  DOBLE"` |
| `sigla_da_instituicao` | string | `"CORSAN"` |
| `regional_de_saude` | string | `"6ª CRS"` |
| `regiao_geografica` | string | `"SUL"` |
| `unidade` | string | `"E.coli/100mL"` |
| `data_da_coleta` | string | `"2014/05/30 00:00:00.000"` |
| `nome_do_escritorio_regionallocal` | string | `"SUPERINTENDENCIA REGIONAL PLANALTO SURPLA"` |
| `nome_da_instituicao` | string | `"COMPANHIA RIOGRANDENSE DE SANEAMENTO"` |
| `data_de_registro` | string | `"2015/03/31 00:00:00.000"` |
| `parametro` | string | `"Escherichia coli"` |
| `ano_de_referencia` | string | `"2014"` |
| `codigo_forma_de_abastecimento` | string | `"S430320000001"` |
| `nome_do_manancial_superficial` | null | `null` |
| `tipo_de_captacao` | string | `"SUBTERRANEO"` |
| `data_de_preenchimento_do_relatorio_mensal` | string | `"2015/03/31 00:00:00.000"` |
| `municipio` | string | `"CACIQUE DOBLE"` |
| `cnpj_da_instituicao` | string | `"92802784000190.0"` |
| `cnpj_do_escritorio_regionallocal` | string | `"92802784036380.0"` |
| `resultado` | string | `"1"` |
| `mes_de_referencia` | string | `"5"` |
| `tipo_da_instituicao` | string | `"Empresa Estadual"` |
| `nome_do_ponto_de_captacao_subterranea` | string | `"CDO-01"` |
| `nome_da_eta__uta` | null \| string | `"CDO-01"` |
| `categoria_do_manancial_superficial` | null | `null` |
| `uf` | string | `"RS"` |
| `codigo_ibge` | string | `"430320"` |
| `categoria_do_ponto_de_captacao_subterranea` | string | `"POÇO ARTESIANO"` |

## `/sisagua/controle-mensal-infraestrutura-operacional`

Dados sobre as condições operacionais e de infraestrutura dos sistemas e soluções de abastecimento de água para consumo humano, informados pelo prestador de serviço em frequência mensal.

- URL: `https://apidadosabertos.saude.gov.br/sisagua/controle-mensal-infraestrutura-operacional?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisagua_mensal_infraestrutura_operacional": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `local` | string | `"RESIDENCIA"` |
| `numero_de_eventos_de_falta_de_agua` | null \| string | `"0"` |
| `cnpj_do_escritorio_regionallocal` | string | `"43776517055910.0"` |
| `area` | string | `"CENTRO"` |
| `nome_da_forma_de_abastecimento` | string | `"ICEM"` |
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `data_de_preenchimento_do_relatorio_mensal` | string | `"2019/02/07 00:00:00.000"` |
| `numero_de_reclamacoes_de_cor_da_agua` | null \| string | `"0"` |
| `mes_de_referencia` | string | `"1"` |
| `nome_do_escritorio_regionallocal` | string | `"ICEM SABESP"` |
| `numero_de_reclamacao_de_gosto_e_ou_odor` | null \| string | `"1"` |
| `ano_de_referencia` | string | `"2019"` |
| `regiao_geografica` | string | `"SUDESTE"` |
| `numero_de_reparos_na_rede_somente_para_saa` | null \| string | `"0"` |
| `tipo_da_instituicao` | string | `"Regional"` |
| `tipo_do_local` | string | `"Casa"` |
| `categoria_area` | string | `"Bairro"` |
| `zona` | string | `"Urbana"` |
| `cnpj_da_instituicao` | string | `"43776517000180.0"` |
| `codigo_ibge` | string | `"351980"` |
| `codigo_forma_de_abastecimento` | string | `"S351980000001"` |
| `sigla_da_instituicao` | string | `"SABESP"` |
| `numero_de_eventos_de_intermitencia_somente_para_saa` | null \| string | `"0"` |
| `nome_da_instituicao` | string | `"COMPANHIA DE SANEAMENTO BASICO DO ESTADO DE SAO PAULO"` |
| `regional_de_saude` | string | `"GVS XXIX  - SÃO JOSÉ DO RIO PRETO"` |
| `uf` | string | `"SP"` |
| `data_de_registro` | string | `"2019/02/08 00:00:00.000"` |
| `municipio` | string | `"ICEM"` |

## `/sisagua/controle-mensal-plano-amostragem`

Dados sobre os quantitativos mínimos de análises definidos para os prestadores de serviço, por forma de abastecimento, parâmetro de qualidade da água e ponto de monitoramento, com respectivas frequências de amostragem.

- URL: `https://apidadosabertos.saude.gov.br/sisagua/controle-mensal-plano-amostragem?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisagua_controle_mensal_plano_amostragem": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `data_de_registro_no_sisagua` | string | `"2023/01/04 17:54:03.000"` |
| `regiao_geografica` | string | `"SUL"` |
| `captacao_superficial` | string | `"Não"` |
| `ano_de_referencia` | string | `"2023"` |
| `cnpj_da_instituicao` | string | `"92802784000190.0"` |
| `razao_habitantesdomicilio` | null | `null` |
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `uf` | string | `"RS"` |
| `municipio` | string | `"CHAPADA"` |
| `campo` | string | `"Frequência"` |
| `nome_do_escritorio_regionallocal` | string | `"SUPERINTENDENCIA REGIONAL PLANALTO SURPLA"` |
| `codigo_ibge` | string | `"430530"` |
| `parameto` | string | `"Residual de Desinfetante"` |
| `captacao_de_agua_de_chuva` | null \| string | `"Não"` |
| `cnpj_do_escritorio_regionallocal` | string | `"92802784036380.0"` |
| `numero_de_economias_residenciais_domicilios_permanentes` | null | `null` |
| `nome_da_forma_de_abastecimento` | string | `"CHAPADA"` |
| `ponto_de_monitoramento` | string | `"SAÍDA DO TRATAMENTO"` |
| `nome_da_etauta` | null \| string | `"CHA-02B"` |
| `populacao_abastecida_estimada` | null | `null` |
| `codigo_forma_de_abastecimento` | string | `"S430530000001"` |
| `captacao_subterranea` | string | `"Sim"` |
| `regional_de_saude` | string | `"15ª CRS"` |
| `tempo_medio_diario_de_funcionamento` | null \| string | `"11:00"` |
| `nome_da_instiuicao` | string | `"COMPANHIA RIOGRANDENSE DE SANEAMENTO"` |
| `numero_de_filtros` | null \| string | `"8.0"` |
| `tipo_de_filtracao` | string | `"SEM FILTRAÇÃO"` |
| `sigla_da_instituicao` | string | `"CORSAN"` |
| `tipo_da_instituicao` | string | `"Regional"` |
| `valor` | string | `"Semanal"` |

## `/sisagua/populacao-abastecida`

Dados anuais sobre as formas de abastecimento de água para consumo humano (SAA, SAC e SAI), com informações sobre a população atendida por cada uma delas.

- URL: `https://apidadosabertos.saude.gov.br/sisagua/populacao-abastecida?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisagua_populacao_abastecida": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `filtracao` | string | `"Sim"` |
| `numero_de_economias_residenciais_domicilios_permanentes` | null \| string | `"8880.0"` |
| `populacao_rural` | null | `null` |
| `cisterna` | string | `null` |
| `codigo_forma_de_abastecimento` | string | `"S270240000002"` |
| `caixa_dagua` | string | `null` |
| `pop_recebe_agua_de_saa` | string | `null` |
| `carro_pipa` | string | `null` |
| `regiao_geografica` | string | `"NORDESTE"` |
| `numero_de_economias_residenciais_de_uso_ocasional` | null \| string | `"0.0"` |
| `nome_da_forma_de_abastecimento` | string | `"SAA DE DELMIRO GOUVEIA ADUTORA"` |
| `chafariz` | string | `null` |
| `regional_de_saude` | string | `"10 REGIÃO DEG AL"` |
| `data_de_preenchimento` | string | `"2014/02/18 00:00:00.000"` |
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `codigo_ibge` | string | `"270240"` |
| `outro_tipo_de_suprimento` | string | `null` |
| `desinfeccao` | string | `"Sim"` |
| `municipio` | string | `"DELMIRO GOUVEIA"` |
| `ano_de_referencia` | string | `"2014"` |
| `pop_recebe_agua_de_saasac` | string | `null` |
| `fonte` | string | `null` |
| `sem_reservacao` | string | `null` |
| `captacao_de_agua_de_chuva` | string | `null` |
| `tipo_da_instituicao` | string | `"Regional"` |
| `nome_da_instituicao` | string | `"COMPANHIA DE SANEAMENTO DE ALAGOAS"` |
| `sigla_da_instituicao` | string | `"CASAL"` |
| `populacao_urbana` | null | `null` |
| `canalizacao` | string | `null` |
| `uf` | string | `"AL"` |
| `nome_do_escritorio_regionallocal` | string | `"UNIDADE SERTAO DELMIRO GOUVEIA"` |
| `cnpj_do_escritorio_regionallocal` | string | `"12294708000181.0"` |
| `data_de_registro_no_sisagua` | string | `"2014/02/18 14:12:25.000"` |
| `captacao_superficial` | string | `"Sim"` |
| `captacao_subterranea` | string | `"Não"` |
| `cnpj_da_instituicao` | string | `"12294708000181.0"` |
| `populacao_estimada` | string | `"32234"` |

## `/sisagua/tratamento-de-agua`

Dados sobre o tratamento de água empregado nos sistemas e soluções alternativas de abastecimento de água para consumo humano, informados pelo prestador de serviço em frequência anual.

- URL: `https://apidadosabertos.saude.gov.br/sisagua/tratamento-de-agua?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisagua_tratamento_agua": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `email` | string | `"US068@CORSAN.COM.BR"` |
| `codigo_ibge` | string | `"270240"` |
| `desinf_com_ozonio` | string | `"N"` |
| `uf` | string | `"AL"` |
| `municipio` | string | `"DELMIRO GOUVEIA"` |
| `cnpj_da_instituicao` | string | `"12294708000181.0"` |
| `numero_do_conselho_de_classe` | string | `"05302606"` |
| `etapa_desinfeccao` | string | `"S"` |
| `codigo_forma_de_abastecimento` | string | `"S270240000002"` |
| `responsavel_tecnico` | string | `"JOAO NETO"` |
| `cisterna` | string | `null` |
| `regiao_geografica` | string | `"NORDESTE"` |
| `nome_do_escritorio_regionallocal` | string | `"UNIDADE SERTAO DELMIRO GOUVEIA"` |
| `outro_tipo_de_suprimento` | string | `null` |
| `etapa_fluoretacao` | string | `"N"` |
| `rad_dioxido_de_cloro` | string | `"N"` |
| `etapa_floculacao` | string | `"S"` |
| `desinf_com_cloramina` | string | `"N"` |
| `carro_pipa` | string | `null` |
| `polimero_com_epicloridrina` | string | `"N"` |
| `etapa_decantacao` | string | `"S"` |
| `nome_da_instituicao` | string | `"COMPANHIA DE SANEAMENTO DE ALAGOAS"` |
| `regional_de_saude` | string | `"10 REGIÃO DEG AL"` |
| `fonte` | string | `null` |
| `polimero_com_acrilamida` | string | `"N"` |
| `data_de_preenchimento` | string | `"2014/02/18 00:00:00.000"` |
| `desinf_com_dioxido_cloro` | string | `"N"` |
| `rad_cloro_res_livre` | string | `"S"` |
| `etapa_pre_oxidacao` | string | `"N"` |
| `impedimento_de_monitoramento_por_unidade_filtrante` | string | `"N"` |
| `chafariz` | string | `null` |
| `captacao_superficial` | string | `"Sim"` |
| `telefone` | null \| string | `"36412819"` |
| `outra_etapa_tratamento` | string | `"GRADEAMENTO CAIXA DE AREIA"` |
| `ano_de_referencia` | string | `"2014"` |
| `numero_de_filtros` | null \| string | `"4"` |
| `cep` | null | `null` |
| `etapa_desfluoretacao` | string | `"N"` |
| `data_de_registro_no_sisagua` | string | `"2014/02/18 14:12:25.000"` |
| `outro_desinfetante` | string | `"HIPOCLORO DE CALCIO"` |
| `rad_cloro_res_combinado` | string | `"N"` |
| `canalizacao` | string | `null` |
| `numero` | string | `"220"` |
| `etapa_flotacao` | string | `"N"` |
| `nome_da_forma_de_abastecimento` | string | `"SAA DE DELMIRO GOUVEIA ADUTORA"` |
| `sigla_da_instituicao` | string | `"CASAL"` |
| `tipo_de_filtracao` | string | `"FILTRAÇÃO RÁPIDA"` |
| `captacao_de_agua_de_chuva` | string | `null` |
| `tempo_medio_diario_de_funcionamento` | string | `"24:00"` |
| `formacao` | string | `"Engenharia Química"` |
| `captacao_subterranea` | string | `"Não"` |
| `ddd` | null \| string | `"82"` |
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `etapa_mistura_rap_e_coag` | string | `"S"` |
| `endereco` | string | `"AV OLAVO BILAC"` |
| `desinf_com_uv` | string | `"N"` |
| `vazao_de_agua_tratada` | string | `"247.2"` |
| `tipo_da_instituicao` | string | `"Regional"` |
| `art` | string | `"87613"` |
| `desinf_com_cloro_gashipoc` | string | `"S"` |
| `cnpj_do_escritorio_regionallocal` | string | `"12294708000181.0"` |
| `nome_da_eta` | string | `"DELMIRO GOUVEIA ADUTORA"` |
| `desinf_com_isocianuratos_clorados` | string | `"N"` |

## `/sisagua/vigilancia-cianobacterias-e-cianotoxinas`

Dados sobre as análises de cianobactérias e cianotoxinas realizadas pelo setor saúde.

- URL: `https://apidadosabertos.saude.gov.br/sisagua/vigilancia-cianobacterias-e-cianotoxinas?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisagua_vigilancia_cianobacterias_cianotoxinas": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `parametro_ciano` | string | `"Cilindrospermopsinas (µg/L)"` |
| `nome_da_etauta` | string | `"PIRAPAMA"` |
| `hora_da_coleta` | string | `"09:40"` |
| `descricao_do_local` | string | `"RUA SEVERINO PERINA, 1043"` |
| `codigo_forma_de_abastecimento` | string | `"S353770000001"` |
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `mes` | string | `"10"` |
| `data_da_coleta` | string | `"2014/10/21 00:00:00.000"` |
| `regional_de_saude` | string | `"GVS XI - ARAÇATUBA"` |
| `categoria_area` | string | `"Bairro"` |
| `resultado` | string | `"0,00"` |
| `motivo_da_coleta` | string | `"Rotina"` |
| `data_de_registro_no_sisagua` | string | `"2014/11/11 08:51:26.000"` |
| `grupo` | string | `"Cianotoxinas"` |
| `ano` | string | `"2014"` |
| `codigo_ibge` | string | `"353770"` |
| `data_do_laudo` | string | `"2014/10/24 00:00:00.000"` |
| `latitude` | null \| string | `"-13.507345"` |
| `municipio` | string | `"PIACATU"` |
| `zona` | string | `"Urbana"` |
| `local` | string | `"PRACA DA MATRIZ"` |
| `nome_da_forma_de_abastecimento` | string | `"PIACATU(19)"` |
| `tipo_do_local` | string | `"Praça"` |
| `uf` | string | `"SP"` |
| `longitude` | null \| string | `"-48.739203"` |
| `procedencia_da_coleta` | string | `"SISTEMA DE DISTRIBUIÇÃO"` |
| `area` | string | `"CENTRO"` |
| `numero_da_amostra` | string | `"30"` |
| `ponto_de_coleta` | string | `"Cavalete/Hidrômetro"` |
| `regiao_geografica` | string | `"SUDESTE"` |

## `/sisagua/vigilancia-demais-parametros`

Dados sobre as análises de qualidade da água de alta complexidade realizadas pelo setor saúde.

- URL: `https://apidadosabertos.saude.gov.br/sisagua/vigilancia-demais-parametros?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisagua_demais_parametros": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `descricao_do_local` | string | `"AV. BRASIL, QUADRA 03, LOTE 03, Nº 2.240W (MERCADO PRESTÍGI…` |
| `area` | string | `"JARDIM EUROPA"` |
| `grupo_de_parametros` | string | `"Agrotóxicos"` |
| `lq` | string | `"0,10"` |
| `longitude` | null \| string | `"-56.1040277"` |
| `parametro_demais_parametros` | string | `"Terbufós - VMP: 1,2 µg/L"` |
| `codigo_ibge` | string | `"510622"` |
| `mes` | string | `"11"` |
| `latitude` | null \| string | `"-13.8330277"` |
| `resultado` | string | `"MENOR_LQ"` |
| `data_da_coleta` | string | `"2014/11/18 00:00:00.000"` |
| `procedencia_da_coleta` | string | `"SISTEMA DE DISTRIBUIÇÃO"` |
| `zona` | string | `"Urbana"` |
| `numero_da_amostra` | string | `"03 A"` |
| `municipio` | string | `"NOVA MUTUM"` |
| `tipo_do_local` | string | `"Estabelecimento de saúde"` |
| `nome_da_forma_de_abastecimento` | string | `"SERV. AUTONOMO AGUA E ESGOTO"` |
| `nome_da_etauta` | string | `"ETA DE AIQUARA"` |
| `uf` | string | `"MT"` |
| `regional_de_saude` | string | `"ERS SINOP"` |
| `hora_da_coleta` | string | `"14:05"` |
| `tipo_da_forma_de_abastecimento` | string | `"SAA"` |
| `data_da_analise` | string | `"21/01/2015"` |
| `ld` | string | `"0,10"` |
| `codigo_forma_de_abastecimento` | string | `"S510622000003"` |
| `motivo_da_coleta` | string | `"Rotina"` |
| `local` | string | `"HOSPITAL JORGE NOVIS LARGO DO CARANGUEIJO"` |
| `regiao_geografica` | string | `"CENTRO-OESTE"` |
| `categoria_area` | string | `"Bairro"` |
| `ano` | string | `"2014"` |
| `data_do_laudo` | string | `"2015/01/21 00:00:00.000"` |
| `ponto_de_coleta` | string | `"Cavalete/Hidrômetro"` |
| `data_de_registro_no_sisagua` | string | `"2015/07/14 10:31:51.000"` |

## `/sisvan/estado-nutricional`

Obtém informações de acompanhamento de estado nutricional.

- URL: `https://apidadosabertos.saude.gov.br/sisvan/estado-nutricional?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"estados_nutricionais": "array[20]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `status_participacao` | null | `null` |
| `codigo_municipio` | integer | `354130` |
| `uf` | string | `"SP"` |
| `municipio` | string | `"PRESIDENTE EPITACIO"` |
| `codigo_cnes` | null \| string | `"5654637"` |
| `idade` | integer | `10` |
| `codigo_fase_vida` | number | `6.0` |
| `fase_vida` | string | `"ADOLESCENTE"` |
| `sexo` | string | `"F"` |
| `codigo_raca_cor` | string | `"99"` |
| `raca_cor` | string | `"SEM INFORMACAO"` |
| `codigo_povo_comunidade` | null | `null` |
| `povo_comunidade` | string | `"NÃO INFORMADO"` |
| `codigo_escolaridade` | integer \| null | `99` |
| `escolaridade` | string | `"SEM INFORMAÇÃO"` |
| `data_acompanhamento` | string | `"2008-03-09"` |
| `ano_mes_competencia` | string | `"200803"` |
| `peso` | string | `"30"` |
| `altura` | string | `"1.26"` |
| `imc` | string | `"18.9"` |
| `imc_pre_gestacional` | null | `null` |
| `peso_x_idade` | null \| string | `"Peso adequado para idade"` |
| `peso_x_altura` | null \| string | `"Peso Adequado ou Eutrofico"` |
| `crianca_altura_x_idade` | null \| string | `"Baixa estatura para idade"` |
| `crianca_imc_x_idade` | null \| string | `"Eutrofia"` |
| `adolescente_altura_x_idade` | null \| string | `"Baixa estatura para idade"` |
| `adolescente_imc_x_idade` | null \| string | `"Eutrofia"` |
| `codigo_estado_nutricional_adulto` | null \| string | `"Sobrepeso"` |
| `codigo_estado_nutricional_idoso` | null | `null` |
| `codigo_estado_nutricional_imc_gestante` | null | `null` |
| `codigo_sistema_origem_acompanhamento` | integer | `2` |
| `sistema_origem_acompanhamento` | string | `"AUXILIO BRASIL"` |
| `codigo_sequencial_acompanhamento` | integer | `36722185` |

## `/arboviroses/zikavirus`

Lista de notificações de arbovirose Zikavirus por ano e município

- URL: `https://apidadosabertos.saude.gov.br/arboviroses/zikavirus?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"zikavirus": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `tp_not` | string | `"2"` |
| `id_agravo` | string | `"A928"` |
| `cs_suspeit` | string | `"nan"` |
| `dt_notific` | string | `"2016-01-01"` |
| `sem_not` | string | `"201552"` |
| `nu_ano` | string | `"2016"` |
| `sg_uf_not` | string | `"17"` |
| `id_municip` | string | `"170230"` |
| `id_regiona` | string | `"nan"` |
| `dt_sin_pri` | string | `"2016-01-01"` |
| `sem_pri` | string | `"201552"` |
| `nu_idade_n` | string | `"4116"` |
| `cs_sexo` | string | `"M"` |
| `cs_gestant` | string | `"6"` |
| `cs_raca` | string | `"nan"` |
| `cs_escol_n` | string | `"nan"` |
| `sg_uf` | string | `"17"` |
| `id_mn_resi` | string | `"170230"` |
| `id_rg_resi` | string | `"nan"` |
| `id_pais` | string | `"1"` |
| `nduplic_n` | string | `"nan"` |
| `in_vincula` | string | `"nan"` |
| `dt_invest` | string | `"nan"` |
| `id_ocupa_n` | string | `"nan"` |
| `classi_fin` | string | `"8"` |
| `criterio` | string | `"nan"` |
| `tpautocto` | string | `"nan"` |
| `coufinf` | string | `"nan"` |
| `copaisinf` | string | `"0"` |
| `comuninf` | string | `"nan"` |
| `doenca_tra` | string | `"nan"` |
| `evolucao` | string | `"nan"` |
| `dt_obito` | string | `"nan"` |
| `dt_encerra` | string | `"2016-03-07"` |
| `cs_flxret` | string | `"0"` |
| `flxrecebi` | string | `"2"` |
| `tp_sistema` | string | `"1"` |
| `tpuninot` | string | `"nan"` |
| `id_unidade` | null | `null` |
| `ano_nasc` | null | `null` |
| `dt_digita` | null | `null` |

## `/arboviroses/dengue`

Lista de notificações de arbovirose Dengue por ano e município

- URL: `https://apidadosabertos.saude.gov.br/arboviroses/dengue?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"dengue": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `tp_not` | string | `"2"` |
| `id_agravo` | string | `"A90"` |
| `dt_notific` | string | `"2026-03-20"` |
| `sem_not` | string | `"202611"` |
| `nu_ano` | string | `"2026"` |
| `sg_uf_not` | string | `"15"` |
| `id_municip` | string | `"150080"` |
| `id_regiona` | string | `"1484"` |
| `id_unidade` | string | `"0942979"` |
| `dt_sin_pri` | string | `"2026-03-16"` |
| `sem_pri` | string | `"202611"` |
| `nu_idade_n` | string | `"4051"` |
| `cs_sexo` | string | `"F"` |
| `cs_gestant` | string | `"5"` |
| `cs_raca` | string | `"4"` |
| `cs_escol_n` | string | `"6"` |
| `sg_uf` | string | `"15"` |
| `id_mn_resi` | string | `"150080"` |
| `id_rg_resi` | string | `"1484"` |
| `id_pais` | string | `"1"` |
| `nduplic_n` | string | `"nan"` |
| `dt_digita` | string | `"2026-03-25"` |
| `cs_flxret` | string | `"1"` |
| `flxrecebi` | string | `"nan"` |
| `migrado_w` | string | `"nan"` |
| `dt_invest` | string | `"2026-03-20"` |
| `id_ocupa_n` | string | `"nan"` |
| `dt_soro` | string | `"2026-03-23"` |
| `resul_soro` | string | `"1"` |
| `histopa_n` | string | `"nan"` |
| `dt_viral` | string | `"nan"` |
| `resul_vi_n` | string | `"nan"` |
| `sorotipo` | string | `"nan"` |
| `imunoh_n` | string | `"nan"` |
| `dt_pcr` | string | `"nan"` |
| `resul_pcr_` | string | `"nan"` |
| `classi_fin` | string | `"10"` |
| `criterio` | string | `"1"` |
| `tpautocto` | string | `"nan"` |
| `coufinf` | string | `"nan"` |
| `copaisinf` | string | `"nan"` |
| `comuninf` | string | `"nan"` |
| `doenca_tra` | string | `"nan"` |
| `evolucao` | string | `"1"` |
| `dt_obito` | string | `"nan"` |
| `dt_encerra` | string | `"2026-05-13"` |
| `mani_hemor` | string | `"nan"` |
| `epistaxe` | string | `"nan"` |
| `gengivo` | string | `"nan"` |
| `metro` | string | `"nan"` |
| `petequias` | string | `"nan"` |
| `hematura` | string | `"nan"` |
| `sangram` | string | `"nan"` |
| `laco_n` | string | `"nan"` |
| `plasmatico` | string | `"nan"` |
| `evidencia` | string | `"nan"` |
| `plaq_menor` | string | `"nan"` |
| `con_fhd` | string | `"nan"` |
| `complica` | string | `"nan"` |
| `hospitaliz` | string | `"nan"` |
| `dt_interna` | string | `"nan"` |
| `uf` | string | `"nan"` |
| `municipio` | string | `"nan"` |
| `ano_nasc` | string | `"1975"` |
| `febre` | string | `"1"` |
| `mialgia` | string | `"1"` |
| `cefaleia` | string | `"1"` |
| `exantema` | string | `"2"` |
| `vomito` | string | `"2"` |
| `nausea` | string | `"1"` |
| `dor_costas` | string | `"1"` |
| `conjuntvit` | string | `"2"` |
| `artrite` | string | `"1"` |
| `artralgia` | string | `"1"` |
| `petequia_n` | string | `"2"` |
| `leucopenia` | string | `"2"` |
| `laco` | string | `"2"` |
| `dor_retro` | string | `"1"` |
| `diabetes` | string | `"2"` |
| `hematolog` | string | `"2"` |
| `hepatopat` | string | `"2"` |
| `renal` | string | `"2"` |
| `hipertensa` | string | `"2"` |
| `acido_pept` | string | `"2"` |
| `auto_imune` | string | `"2"` |
| `dt_chik_s1` | string | `"nan"` |
| `dt_chik_s2` | string | `"nan"` |
| `dt_prnt` | string | `"nan"` |
| `res_chiks1` | string | `"nan"` |
| `res_chiks2` | string | `"nan"` |
| `resul_prnt` | string | `"nan"` |
| `dt_ns1` | string | `"nan"` |
| `resul_ns1` | string | `"nan"` |
| `clinc_chik` | string | `"nan"` |
| `alrm_hipot` | string | `"nan"` |
| `alrm_plaq` | string | `"nan"` |
| `alrm_vom` | string | `"nan"` |
| `alrm_sang` | string | `"nan"` |
| `alrm_hemat` | string | `"nan"` |
| `alrm_abdom` | string | `"nan"` |
| `alrm_letar` | string | `"nan"` |
| `alrm_hepat` | string | `"nan"` |
| `alrm_liq` | string | `"nan"` |
| `dt_alrm` | string | `"nan"` |
| `grav_pulso` | string | `"nan"` |
| `grav_conv` | string | `"nan"` |
| `grav_ench` | string | `"nan"` |
| `grav_insuf` | string | `"nan"` |
| `grav_taqui` | string | `"nan"` |
| `grav_extre` | string | `"nan"` |
| `grav_hipot` | string | `"nan"` |
| `grav_hemat` | string | `"nan"` |
| `grav_melen` | string | `"nan"` |
| `grav_metro` | string | `"nan"` |
| `grav_sang` | string | `"nan"` |
| `grav_ast` | string | `"nan"` |
| `grav_mioc` | string | `"nan"` |
| `grav_consc` | string | `"nan"` |
| `grav_orgao` | string | `"nan"` |
| `dt_grav` | string | `"nan"` |
| `tp_sistema` | string | `"2"` |
| `acido_pept_c121` | null | `null` |
| `cs_escolar` | null | `null` |
| `nu_idade` | null | `null` |
| `id_dg_not` | null | `null` |
| `id_ev_not` | null | `null` |
| `ant_dt_inv` | null | `null` |
| `ocupacao` | null | `null` |
| `dengue` | null | `null` |
| `ano` | null | `null` |
| `vacinado` | null | `null` |
| `dt_dose` | null | `null` |
| `dt_febre` | null | `null` |
| `duracao` | null | `null` |
| `dor` | null | `null` |
| `prostacao` | null | `null` |
| `nauseas` | null | `null` |
| `diarreia` | null | `null` |
| `outros` | null | `null` |
| `sin_out` | null | `null` |
| `outros_m` | null | `null` |
| `outros_m_d` | null | `null` |
| `ascite` | null | `null` |
| `pleural` | null | `null` |
| `pericardi` | null | `null` |
| `abdominal` | null | `null` |
| `hepato` | null | `null` |
| `miocardi` | null | `null` |
| `hipotensao` | null | `null` |
| `choque` | null | `null` |
| `manifesta` | null | `null` |
| `insuficien` | null | `null` |
| `outro_s` | null | `null` |
| `outro_s_d` | null | `null` |
| `dt_choque` | null | `null` |
| `dt_col_hem` | null | `null` |
| `hema_maior` | null | `null` |
| `dt_col_plq` | null | `null` |
| `palq_maior` | null | `null` |
| `dt_col_he2` | null | `null` |
| `hema_menor` | null | `null` |
| `dt_col_pl2` | null | `null` |
| `dt_soro1` | null | `null` |
| `dt_soro2` | null | `null` |
| `dt_soror1` | null | `null` |
| `dt_soror2` | null | `null` |
| `s1_igm` | null | `null` |
| `s1_igg` | null | `null` |
| `s2_igm` | null | `null` |
| `s2_igg` | null | `null` |
| `s1_tit1` | null | `null` |
| `s2_tit1` | null | `null` |
| `material` | null | `null` |
| `soro1` | null | `null` |
| `soro2` | null | `null` |
| `tecidos` | null | `null` |
| `resul_vira` | null | `null` |
| `histopa` | null | `null` |
| `imunoh` | null | `null` |
| `amos_pcr` | null | `null` |
| `resul_pcr` | null | `null` |
| `amos_out` | null | `null` |
| `tecnica` | null | `null` |
| `resul_out` | null | `null` |
| `con_classi` | null | `null` |
| `con_criter` | null | `null` |
| `con_inf_mu` | null | `null` |
| `con_inf_uf` | null | `null` |
| `con_inf_pa` | null | `null` |
| `con_doenca` | null | `null` |
| `con_evoluc` | null | `null` |
| `con_dt_obi` | null | `null` |
| `con_dt_enc` | null | `null` |
| `in_vincula` | null | `null` |
| `nduplic` | null | `null` |
| `in_aids` | null | `null` |

## `/arboviroses/chikungunya`

Lista de notificações de arbovirose Chikungunya por ano e município

- URL: `https://apidadosabertos.saude.gov.br/arboviroses/chikungunya?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"chikungunya": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `tp_not` | string | `"2"` |
| `id_agravo` | string | `"A92."` |
| `dt_notific` | string | `"2016-02-24"` |
| `sem_not` | string | `"201608"` |
| `nu_ano` | string | `"2016"` |
| `sg_uf_not` | string | `"51"` |
| `id_municip` | integer | `510263` |
| `id_regiona` | string | `"1585"` |
| `id_unidade` | null | `null` |
| `dt_sin_pri` | string | `"2016-02-24"` |
| `sem_pri` | string | `"201608"` |
| `nu_idade_n` | number | `4015.0` |
| `cs_sexo` | string | `"F"` |
| `cs_gestant` | string | `"5"` |
| `cs_raca` | string | `"4"` |
| `cs_escol_n` | string | `"02"` |
| `sg_uf` | string | `"51"` |
| `id_mn_resi` | string | `"510263"` |
| `id_rg_resi` | string | `"1585"` |
| `id_pais` | string | `"1"` |
| `dt_invest` | string | `"2016-02-24"` |
| `id_ocupa_n` | string | `"nan"` |
| `febre` | null | `null` |
| `mialgia` | null | `null` |
| `cefaleia` | null | `null` |
| `exantema` | null | `null` |
| `vomito` | null | `null` |
| `nausea` | null | `null` |
| `dor_costas` | null | `null` |
| `conjuntvit` | null | `null` |
| `artrite` | null | `null` |
| `artralgia` | null | `null` |
| `petequia_n` | null | `null` |
| `leucopenia` | null | `null` |
| `laco` | null | `null` |
| `dor_retro` | null | `null` |
| `diabetes` | null | `null` |
| `hematolog` | null | `null` |
| `hepatopat` | null | `null` |
| `renal` | null | `null` |
| `hipertensa` | null | `null` |
| `acido_pept` | null | `null` |
| `auto_imune` | null | `null` |
| `dt_chik_s1` | null | `null` |
| `dt_chik_s2` | null | `null` |
| `dt_prnt` | null | `null` |
| `res_chiks1` | null | `null` |
| `res_chiks2` | null | `null` |
| `resul_prnt` | null | `null` |
| `dt_soro` | null | `null` |
| `resul_soro` | null | `null` |
| `dt_ns1` | null | `null` |
| `resul_ns1` | null | `null` |
| `dt_viral` | null | `null` |
| `resul_vi_n` | null | `null` |
| `dt_pcr` | null | `null` |
| `resul_pcr_` | null | `null` |
| `sorotipo` | null | `null` |
| `histopa_n` | null | `null` |
| `imunoh_n` | null | `null` |
| `hospitaliz` | null | `null` |
| `dt_interna` | null | `null` |
| `uf` | null | `null` |
| `municipio` | null | `null` |
| `tpautocto` | string | `"nan"` |
| `coufinf` | string | `"nan"` |
| `copaisinf` | string | `"nan"` |
| `comuninf` | string | `"nan"` |
| `classi_fin` | string | `"2"` |
| `criterio` | string | `"2"` |
| `doenca_tra` | string | `"nan"` |
| `clinc_chik` | null | `null` |
| `evolucao` | string | `"1"` |
| `dt_obito` | string | `"nan"` |
| `dt_encerra` | string | `"2016-04-26"` |
| `alrm_hipot` | null | `null` |
| `alrm_plaq` | null | `null` |
| `alrm_vom` | null | `null` |
| `alrm_sang` | null | `null` |
| `alrm_hemat` | null | `null` |
| `alrm_abdom` | null | `null` |
| `alrm_letar` | null | `null` |
| `alrm_hepat` | null | `null` |
| `alrm_liq` | null | `null` |
| `dt_alrm` | null | `null` |
| `grav_pulso` | null | `null` |
| `grav_conv` | null | `null` |
| `grav_ench` | null | `null` |
| `grav_insuf` | null | `null` |
| `grav_taqui` | null | `null` |
| `grav_extre` | null | `null` |
| `grav_hipot` | null | `null` |
| `grav_hemat` | null | `null` |
| `grav_melen` | null | `null` |
| `grav_metro` | null | `null` |
| `grav_sang` | null | `null` |
| `grav_ast` | null | `null` |
| `grav_mioc` | null | `null` |
| `grav_consc` | null | `null` |
| `grav_orgao` | null | `null` |
| `dt_grav` | null | `null` |
| `mani_hemor` | null | `null` |
| `epistaxe` | null | `null` |
| `gengivo` | null | `null` |
| `metro` | null | `null` |
| `petequias` | null | `null` |
| `hematura` | null | `null` |
| `sangram` | null | `null` |
| `laco_n` | null | `null` |
| `plasmatico` | null | `null` |
| `evidencia` | null | `null` |
| `plaq_menor` | null | `null` |
| `con_fhd` | null | `null` |
| `complica` | null | `null` |
| `tp_sistema` | string | `"nan"` |
| `nduplic_n` | string | `"nan"` |
| `cs_suspeit` | string | `"nan"` |
| `in_vincula` | string | `"nan"` |
| `cs_flxret` | string | `"0"` |
| `flxrecebi` | string | `"2"` |
| `tpuninot` | string | `"nan"` |
| `ano_nasc` | null | `null` |
| `nu_lote_i` | null | `null` |
| `dt_digita` | null | `null` |
| `migrado_w` | null | `null` |

## `/daf/estoque-medicamentos-bnafar-horus`

Obtém base de estoque de medicamentos do Sistema Nacional de Gestão da Assistência Farmacêutica (Hórus)

- URL: `https://apidadosabertos.saude.gov.br/daf/estoque-medicamentos-bnafar-horus?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"parametros": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `codigo_uf` | integer | `35` |
| `codigo_municipio` | integer | `352000` |
| `codigo_cnes` | integer | `8471223` |
| `data_posicao_estoque` | string | `"2026-09-17"` |
| `codigo_catmat` | string | `"BR0293892U0067"` |
| `quantidade_estoque` | number | `0.0` |
| `numero_lote` | string | `"2420940"` |
| `data_validade` | string | `"2026-09-30 00:00:00-03"` |
| `tipo_produto` | string | `"O"` |
| `sigla_programa_saude` | string | `"NI"` |
| `descricao_programa_saude` | string | `"NÃO INFORMADO"` |
| `sigla_sistema_origem` | string | `"SI_BNAFAR"` |
| `descricao_produto` | string | `"ACEBROFILINA 10 MG/ML XAROPE  120 ML"` |
| `municipio` | string | `"IGARACU DO TIETE"` |
| `uf` | string | `"SP"` |
| `razao_social` | string | `"FARMACIA MUNICIPAL"` |
| `nome_fantasia` | string | `"FARMACIA MUNICIPAL"` |
| `cep` | string | `"17350254"` |
| `logradouro` | string | `"RUA FERNANDO JATOBA"` |
| `numero_endereco` | string | `"352"` |
| `bairro` | string | `"CENTRO"` |
| `telefone` | string | `"14-36441282"` |
| `latitude` | number | `-22.512279438717208` |
| `longitude` | number | `-48.5610294342041` |
| `email` | null | `null` |

## `/macrorregiao-e-regiao-de-saude/municipio`

Obtém lista de municípios com as informações de macrorregião e região de saúde

- URL: `https://apidadosabertos.saude.gov.br/macrorregiao-e-regiao-de-saude/municipio?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"macrorregiao_regiao_saude_municipios": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `codigo_regiao_pais` | string | `"1"` |
| `regiao_pais` | string | `"Norte"` |
| `codigo_uf` | string | `"12"` |
| `uf` | string | `"Acre"` |
| `codigo_macrorregiao_saude` | string | `"1201"` |
| `macrorregiao_saude` | string | `"MACRO UNICA - AC"` |
| `codigo_regiao_saude` | string | `"12002"` |
| `regiao_saude` | string | `"BAIXO ACRE E PURUS"` |
| `codigo_municipio` | string | `"120001"` |
| `municipio` | string | `"AC - ACRELANDIA"` |
| `populacao_estimada_ibge_2022` | integer | `14021` |

## `/assistencia-a-saude/hospitais-e-leitos`

Obtém lista de dados gerais dos estabelecimentos hospitalares, leitos gerais e complementares, bem como informações de contato com os estabelecimentos como endereço, telefone e e-mail

- URL: `https://apidadosabertos.saude.gov.br/assistencia-a-saude/hospitais-e-leitos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"hospitais_leitos": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nome_da_regiao_do_brasil_onde_fica_o_hospital` | string | `"CENTRO-OESTE"` |
| `unidade_da_federacao_onde_fica_o_hospital` | string | `"GO"` |
| `nome_do_municipio_onde_fica_o_hospital` | string | `"GOIANIA"` |
| `motivo_da_desabilitacao_do_hospital,_caso_esteja_desabilitado` | null | `null` |
| `nome_do_hospital` | string | `"HOSPITAL DO RIM"` |
| `nome_da_razao_social_do_hospital` | string | `"INSTITUTO DE UROLOGIA E NEFROLOGIA DE GOIANIA LTDA"` |
| `tipo_da_gestao_do_hospital` | string | `"M"` |
| `codigo_do_tipo_da_unidade` | string | `"05"` |
| `descricao_do_tipo_da_unidade` | string | `"HOSPITAL GERAL"` |
| `natureza_juridica_do_hospital` | string | `"2062"` |
| `descricao_da_natureza_juridica_do_hosptial` | string | `"HOSPITAL_PRIVADO"` |
| `enderco_do_hospital` | string | `"ALAMEDA DAS ROSAS"` |
| `numero_do_endereco_do_hospital` | string | `"2041"` |
| `complemento_do_endereco_do_hospital` | null \| string | `"CASA"` |
| `nome_do_bairro_do_endereco_do_hosptial` | string | `"SETOR OESTE"` |
| `numero_do_cep_do_hospital` | string | `"74125010"` |
| `quantidade_total_de_leitos_do_hosptial` | number | `29.0` |
| `quantidade_total_de_leitos_sus_do_hosptial` | number | `1.0` |
| `quantidade_de_leitos_de_uti_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_sus_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_adulto_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_sus_adulto_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_pediatrico_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_sus_pediatrico_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_neonatal_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_sus_neonatal_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_queimado_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_sus_queimado_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_coronariana_do_hosptial` | number | `0.0` |
| `quantidade_de_leitos_de_uti_sus_coronariana_do_hosptial` | number | `0.0` |
| `codigo_ibge_do_municipio` | null | `null` |

## `/vacinacao/doses-aplicadas-pni-2020`

Doses aplicadas pelo Programa de Nacional Imunizações (PNI) - 2020

- URL: `https://apidadosabertos.saude.gov.br/vacinacao/doses-aplicadas-pni-2020?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"doses_aplicadas_pni": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nome_pais_paciente` | string | `"BRASIL"` |
| `sexo_paciente` | string | `"M"` |
| `nome_etnia_indigena_paciente` | null | `null` |
| `codigo_origem_registro` | null \| string | `"01"` |
| `descricao_nacionalidade_paciente` | string | `"B"` |
| `codigo_condicao_maternal` | null \| string | `"1"` |
| `nome_fantasia_estabelecimento` | string | `"UBS DA MARAFUNDA UBATUBA"` |
| `numero_idade_paciente` | string | `"0"` |
| `razao_social_estabelecimento` | string | `"PREFEITURA MUNICIPAL DA ESTANCIA BALNEARIA DE UBATUBA"` |
| `numero_cep_paciente` | null \| string | `"07793"` |
| `codigo_vacina_fabricante` | null \| string | `"149"` |
| `uf_estabelecimento` | string | `"SP"` |
| `codigo_natureza_estabelecimento` | string | `"1"` |
| `codigo_paciente` | string | `"09ed32dc5fa27ca86a0d1e0ebb991805e4514ff22967fd808605577ea7b…` |
| `uf_paciente` | string | `"SP"` |
| `nome_da__estabelecimento` | string | `"SAO PAULO"` |
| `descricao_natureza_estabelecimento` | string | `"ADMINISTRACAO PUBLICA"` |
| `codigo_municipio_estabelecimento` | string | `"355540"` |
| `nome_uf_paciente` | string | `"SAO PAULO"` |
| `codigo_municipio_paciente` | string | `"350920"` |
| `descricao_sistema_origem` | string | `"ESUS APS - NACIONAL (OFFLINE)"` |
| `descricao_condicao_maternal` | null \| string | `"Nenhuma"` |
| `nome_municipio_paciente` | string | `"CAJAMAR"` |
| `codigo_local_aplicacao` | string | `"0"` |
| `data_deletado_rnds` | null | `null` |
| `data_vacina` | string | `"2020-01-17 00:00:00-03"` |
| `st_documento` | string | `"final"` |
| `codigo_sistema_origem` | string | `"18602"` |
| `codigo_lote_vacina` | null \| string | `"185VRT007E"` |
| `codigo_vacina` | string | `"45"` |
| `descricao_vacina_fabricante` | null \| string | `"FIOCRUZ/BIOMANGUINHOS"` |

## `/vacinacao/doses-aplicadas-pni-2021`

Doses aplicadas pelo Programa de Nacional Imunizações (PNI) - 2021

- URL: `https://apidadosabertos.saude.gov.br/vacinacao/doses-aplicadas-pni-2021?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"doses_aplicadas_pni": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `tipo_sexo_paciente` | string | `"M"` |
| `codigo_via_administracao` | null \| string | `"0"` |
| `codigo_origem_registro` | null \| string | `"01"` |
| `data_vacina` | string | `"2021-01-13 00:00:00-03"` |
| `nome_municipio_estabelecimento` | string | `"CAMPO DO MEIO"` |
| `nome_uf_estabelecimento` | string | `"MINAS GERAIS"` |
| `nome_etnia_indigena_paciente` | null | `null` |
| `descricao_sistema_origem` | string | `"ESUS APS - NACIONAL (OFFLINE)"` |
| `uf_paciente` | null \| string | `"MG"` |
| `nome_pais_paciente` | null \| string | `"BRASIL"` |
| `codigo_troca_documento` | null \| string | `"5a2c8ed4-c4a0-4ca6-b14d-699eab836e34-i0b0"` |
| `data_entrada_rnds` | string | `"2023-02-18 06:27:31.034-03"` |
| `nome_fantasia_estalecimento` | string | `"PSF CENTRAL"` |
| `codigo_tipo_estabelecimento` | null \| string | `"02"` |
| `codigo_pais_paciente` | null \| string | `"10"` |
| `descricao_via_administracao` | null \| string | `"Sem registro no sistema de informação de origem"` |
| `codigo_etnia_indigena_paciente` | null | `null` |
| `codigo_natureza_estabelecimento` | null \| string | `"1"` |
| `descricao_nacionalidade_paciente` | string | `"B"` |
| `descricao_natureza_estabelecimento` | null \| string | `"ADMINISTRACAO PUBLICA"` |
| `codigo_cnes_estabelecimento` | string | `"2198010"` |
| `st_documento` | string | `"final"` |
| `sg_uf_estabelecimento` | string | `"MG"` |
| `codigo_vacina_fabricante` | null \| string | `"Organization/61189445000156"` |
| `descricao_tipo_estabelecimento` | null \| string | `"CENTRO DE SAUDE/UNIDADE BASICA"` |
| `codigo_sistema_origem` | string | `"18602"` |
| `codigo_municipio_estabelecimento` | string | `"311130"` |
| `nome_raca_cor_paciente` | string | `"PARDA"` |
| `codigo_vacina_grupo_atendimento` | null \| string | `"000926"` |
| `codigo_documento` | string | `"1fd991c7-0c01-4a1e-848e-634e1f2a8130-i0b0"` |

## `/vacinacao/doses-aplicadas-pni-2022`

Doses aplicadas pelo Programa de Nacional Imunizações (PNI) - 2022

- URL: `https://apidadosabertos.saude.gov.br/vacinacao/doses-aplicadas-pni-2022?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"doses_aplicadas_pni": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `codigo_origem_registro` | null \| string | `"01"` |
| `nome_municipio_paciente` | null \| string | `"PARAIBA DO SUL"` |
| `tipo__sexo_paciente` | string | `"M"` |
| `descricao_condicao_maternal` | null | `null` |
| `codigo_vacina` | string | `"22"` |
| `codigo_condicao_maternal` | null | `null` |
| `codigo_etnia_indigena_paciente` | null | `null` |
| `codigo_municipio_estabelecimento` | string | `"330370"` |
| `codigo_vacina_grupo_atendimento` | null \| string | `"000201"` |
| `uf_estabelecimento` | string | `"RIO DE JANEIRO"` |
| `uf_paciente` | null \| string | `"RJ"` |
| `codigo_tipo_estabelecimento` | null \| string | `"02"` |
| `codigo_raca_cor_paciente` | string | `"02"` |
| `codigo_local_aplicacao` | null \| string | `"0"` |
| `descricao_natureza_estabelecimento` | null \| string | `"ADMINISTRACAO PUBLICA"` |
| `cnes_estabelecimento` | string | `"2276216"` |
| `data_vacina` | string | `"2022-01-20 00:00:00-03"` |
| `nome_fantasia_estabelecimento` | string | `"UBS PALHAS LILIAN SALGADO"` |
| `nome_pais_paciente` | null \| string | `"BRASIL"` |
| `descricao_sistema_origem` | string | `"ESUS APS - NACIONAL (OFFLINE)"` |
| `descricao_local_aplicacao` | null \| string | `"Sem registro no sistema de informação de origem"` |
| `codigo_documento` | string | `"58c5ddd2-2712-461c-b53f-3b2256001a56-i0b0"` |
| `codigo_sistema_origem` | string | `"18602"` |
| `codigo_natureza_estabelecimento` | null \| string | `"1"` |
| `idade_paciente` | string | `"0"` |
| `codigo_estrategia_vacinacao` | string | `"1"` |
| `codigo_vacina_fabricante` | null \| string | `"Organization/28290"` |
| `descricao_nacionalidade_paciente` | string | `"B"` |
| `cep_paciente` | null \| string | `"25850"` |

## `/vacinacao/doses-aplicadas-pni-2023`

Doses aplicadas pelo Programa de Nacional Imunizações (PNI) - 2023

- URL: `https://apidadosabertos.saude.gov.br/vacinacao/doses-aplicadas-pni-2023?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"doses_aplicadas_pni": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `codigo_etnia_indigena_paciente` | null | `null` |
| `descricao_local_aplicacao` | null \| string | `"Sem registro no sistema de informação de origem"` |
| `uf_paciente` | string | `"GOIAS"` |
| `uf_estabelecimento` | string | `"GO"` |
| `data_entrada_rnds` | string | `"2023-01-27 16:19:38.865-03"` |
| `codigo_vacina_fabricante` | null \| string | `"PFIZER MANUFACTURING BELGIUM NV/61072393000133"` |
| `codigo_dose_vacina` | string | `"1"` |
| `codigo_condicao_maternal` | null \| string | `"1"` |
| `codigo_via_administracao` | null \| string | `"0"` |
| `codigo_cnes_estabelecimento` | string | `"2384213"` |
| `idade_paciente` | string | `"0"` |
| `cep_paciente` | null \| string | `"76393"` |
| `no_razao_social_estabelecimento` | string | `"PREFEITURA MUNICIPAL DE VILA PROPICIO"` |
| `situacao_documento` | string | `"final"` |
| `codigo_troca_documento` | null \| string | `"61a4cdbf-5c64-4dfc-9b3d-8baeee95a604-i0b0"` |
| `nome_uf_estabelecimento` | string | `"GOIAS"` |
| `descricao_vacina_fabricante` | null \| string | `"PANACEA"` |
| `codigo_natureza_estabelecimento` | null \| string | `"1"` |
| `codigo_vacina` | string | `"42"` |
| `codigo_origem_registro` | null \| string | `"01"` |
| `codigo_paciente` | string | `"6d30b3331f3533d300b2bc1d93c3cb63bb16fd27f4a15e99eeca7fb1e9b…` |
| `codigo_municipio_paciente` | string | `"522230"` |
| `municipio_estabelecimento` | string | `"VILA PROPICIO"` |
| `data_vacina` | string | `"2023-01-04 00:00:00-03"` |
| `codigo_sistema_origem` | string | `"18602"` |
| `descricao_sistema_origem` | string | `"ESUS APS - NACIONAL (OFFLINE)"` |
| `descricao_natureza_estabelecimento` | null \| string | `"ADMINISTRACAO PUBLICA"` |
| `nome_fantasia_estalecimento` | string | `"UNIDADE BASICA DE SAUDE DONA JULIA GONCALVES VILA PROPICIO"` |
| `pais_paciente` | string | `"BRASIL"` |

## `/vacinacao/doses-aplicadas-pni-2024`

Dose aplicadas pelo Programa Nacional de Imunizações (PNI) - 2024

- URL: `https://apidadosabertos.saude.gov.br/vacinacao/doses-aplicadas-pni-2024?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"doses_aplicadas_pni": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `descricao_natureza_estabelecimento` | null \| string | `"ADMINISTRACAO PUBLICA"` |
| `codigo_via_administracao` | null \| string | `"0"` |
| `nome_pais_paciente` | null \| string | `"BRASIL"` |
| `codigo_origem_registro` | null \| string | `"01"` |
| `codigo_pais_paciente` | null \| string | `"10"` |
| `nome_raca_cor_paciente` | string | `"SEM INFORMACAO"` |
| `codigo_vacina_fabricante` | null \| string | `"163"` |
| `data_vacina` | string | `"2024-01-29 00:00:00-03"` |
| `codigo_condicao_maternal` | null \| string | `"1"` |
| `nome_razao_social_estabelecimento` | string | `"PREFEITURA DO MUNICIPIO DE SAO PAULO"` |
| `sigla_uf_estabelecimento` | string | `"SP"` |
| `nome_municipio_estabelecimento` | string | `"SAO PAULO"` |
| `codigo_sistema_origem` | string | `"29376"` |
| `status_documento` | string | `"final"` |
| `descricao_tipo_estabelecimento` | null \| string | `"CENTRO DE SAUDE/UNIDADE BASICA"` |
| `codigo_documento` | string | `"fd19c272-31ea-48aa-bf73-92783f31d3e2-i0b0"` |
| `codigo_municipio_estabelecimento` | string | `"355030"` |
| `data_deletado_rnds` | null | `null` |
| `nome_uf_paciente` | null \| string | `"SAO PAULO"` |
| `numero_cep_paciente` | null \| string | `"05729"` |
| `codigo_etnia_indigena_paciente` | null \| string | `"0208"` |
| `descricao_local_aplicacao` | null \| string | `"Sem registro no sistema de informação de origem"` |
| `numero_idade_paciente` | string | `"4"` |
| `codigo_lote_vacina` | null \| string | `"1802P131"` |
| `codigo_cnes_estabelecimento` | string | `"2788470"` |
| `descricao_vacina_fabricante` | null \| string | `"SERUM INSTITUTE OF INDIA LTD."` |
| `codigo_tipo_estabelecimento` | null \| string | `"02"` |
| `codigo_natureza_estabelecimento` | null \| string | `"1"` |
| `codigo_raca_cor_paciente` | string | `"99"` |
| `codigo_paciente` | string | `"592fc482c704efb3e05bf47cb1dc9824af37e094f74ee31255da68d73ce…` |
| `descricao_sistema_origem` | string | `"SIGA Saúde"` |
| `codigo_municipio_paciente` | null \| string | `"355030"` |
| `nome_municipio_paciente` | null \| string | `"SAO PAULO"` |
| `nome_fantasia_estalecimento` | string | `"UBS REAL PARQUE PAULO MANGABEIRA ALBERNAZ FILHO"` |
| `descricao_condicao_maternal` | null \| string | `"Nenhuma"` |
| `codigo_local_aplicacao` | null \| string | `"0"` |
| `sigla_uf_paciente` | null \| string | `"SP"` |
| `nome_uf_estabelecimento` | string | `"SAO PAULO"` |
| `codigo_vacina` | string | `"28"` |
| `descricao_via_administracao` | null \| string | `"Sem registro no sistema de informação de origem"` |
| `codigo_estrategia_vacinacao` | string | `"1"` |
| `descricao_origem_registro` | null \| string | `"Registro anterior/Transcrição de caderneta"` |
| `data_entrada_rnds` | string | `"2024-03-12 04:01:17-03"` |
| `nome_etnia_indigena_paciente` | null \| string | `"TICUNA (TIKUNA, TUKUNA, MAGUTA)"` |
| `tipo_sexo_paciente` | string | `"M"` |
| `descricao_nacionalidade_paciente` | string | `"B"` |
| `codigo_troca_documento` | null \| string | `"77ffee99-a131-4094-8196-82ac753e83a0-i0b0"` |
| `codigo_dose_vacina` | string | `"7"` |

## `/vacinacao/doses-aplicadas-pni-2025`

Dose aplicadas pelo Programa Nacional de Imunizações (PNI) - 2025

- URL: `https://apidadosabertos.saude.gov.br/vacinacao/doses-aplicadas-pni-2025?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"doses_aplicadas_pni": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `descricao_natureza_estabelecimento` | null \| string | `"ADMINISTRACAO PUBLICA"` |
| `codigo_via_administracao` | null \| string | `"10890"` |
| `nome_pais_paciente` | null \| string | `"BRASIL"` |
| `codigo_origem_registro` | null \| string | `"01"` |
| `codigo_pais_paciente` | null \| string | `"10"` |
| `nome_raca_cor_paciente` | string | `"BRANCA"` |
| `codigo_vacina_fabricante` | null \| string | `"152"` |
| `data_vacina` | string | `"2025-08-20 00:00:00-03"` |
| `codigo_condicao_maternal` | null \| string | `"1"` |
| `nome_razao_social_estabelecimento` | string | `"PREFEITURA MUNICIPAL DE CAXIAS DO SUL"` |
| `sigla_uf_estabelecimento` | string | `"RS"` |
| `nome_municipio_estabelecimento` | string | `"CAXIAS DO SUL"` |
| `codigo_sistema_origem` | string | `"16341"` |
| `status_documento` | string | `"final"` |
| `descricao_tipo_estabelecimento` | null \| string | `"CENTRO DE SAUDE/UNIDADE BASICA"` |
| `codigo_documento` | string | `"aaf823a4-3dd7-4f8c-a680-f78caeff325a-i0b0"` |
| `codigo_municipio_estabelecimento` | string | `"430510"` |
| `data_deletado_rnds` | null | `null` |
| `nome_uf_paciente` | null \| string | `"RIO GRANDE DO SUL"` |
| `numero_cep_paciente` | null \| string | `"95010"` |
| `codigo_etnia_indigena_paciente` | null \| string | `"0208"` |
| `descricao_local_aplicacao` | null \| string | `"Deltóide Direito"` |
| `numero_idade_paciente` | string | `"94"` |
| `codigo_lote_vacina` | null \| string | `"2501389/00"` |
| `codigo_cnes_estabelecimento` | string | `"2239272"` |
| `descricao_vacina_fabricante` | null \| string | `"FUNDACAO BUTANTAN"` |
| `codigo_tipo_estabelecimento` | null \| string | `"02"` |
| `codigo_natureza_estabelecimento` | null \| string | `"1"` |
| `codigo_raca_cor_paciente` | string | `"01"` |
| `codigo_vacina_grupo_atendimento` | null \| string | `"000210"` |
| `codigo_paciente` | string | `"6e0d038934f248d2452806b2d4569001f25b61ec3d0339ba58d4f8a3339…` |
| `descricao_sistema_origem` | string | `"Novo PNI"` |
| `codigo_municipio_paciente` | null \| string | `"430510"` |
| `nome_municipio_paciente` | null \| string | `"CAXIAS DO SUL"` |
| `nome_fantasia_estalecimento` | string | `"UBS REOLON"` |
| `descricao_condicao_maternal` | null \| string | `"Nenhuma"` |
| `codigo_local_aplicacao` | null \| string | `"1"` |
| `sigla_uf_paciente` | null \| string | `"RS"` |
| `nome_uf_estabelecimento` | string | `"RIO GRANDE DO SUL"` |
| `codigo_vacina` | string | `"33"` |
| `descricao_via_administracao` | null \| string | `"Intramuscular"` |
| `codigo_estrategia_vacinacao` | null \| string | `"1"` |
| `descricao_origem_registro` | null \| string | `"Registro anterior/Transcrição de caderneta"` |
| `data_entrada_rnds` | string | `"2025-08-20 16:16:47-03"` |
| `nome_etnia_indigena_paciente` | null \| string | `"TICUNA (TIKUNA, TUKUNA, MAGUTA)"` |
| `tipo_sexo_paciente` | string | `"F"` |
| `descricao_nacionalidade_paciente` | string | `"B"` |
| `codigo_troca_documento` | null \| string | `"61cea95e-1ab4-4a54-9c13-e07af1bf575e-i0b0"` |
| `codigo_dose_vacina` | string | `"9"` |

## `/vacinacao/doses-aplicadas-pni-2026`

Dose aplicadas pelo Programa Nacional de Imunizações (PNI) - 2026

- URL: `https://apidadosabertos.saude.gov.br/vacinacao/doses-aplicadas-pni-2026?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"doses_aplicadas_pni": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `descricao_natureza_estabelecimento` | string | `"ADMINISTRACAO PUBLICA"` |
| `codigo_via_administracao` | string | `"10890"` |
| `nome_pais_paciente` | null \| string | `"BRASIL"` |
| `codigo_origem_registro` | null \| string | `"01"` |
| `codigo_pais_paciente` | null \| string | `"10"` |
| `nome_raca_cor_paciente` | string | `"SEM INFORMACAO"` |
| `codigo_vacina_fabricante` | null \| string | `"152"` |
| `data_vacina` | string | `"2026-05-25 00:00:00-03"` |
| `codigo_condicao_maternal` | null \| string | `"1"` |
| `nome_razao_social_estabelecimento` | string | `"PREFEITURA DO MUNICIPIO DE SAO PAULO"` |
| `sigla_uf_estabelecimento` | string | `"SP"` |
| `nome_municipio_estabelecimento` | string | `"SAO PAULO"` |
| `codigo_sistema_origem` | string | `"16341"` |
| `status_documento` | string | `"final"` |
| `descricao_tipo_estabelecimento` | string | `"CENTRO DE SAUDE/UNIDADE BASICA"` |
| `codigo_documento` | string | `"ab1b4600-ba45-477a-99e9-42816a5af325-i0b0"` |
| `codigo_municipio_estabelecimento` | string | `"355030"` |
| `data_deletado_rnds` | null | `null` |
| `nome_uf_paciente` | null \| string | `"SAO PAULO"` |
| `numero_cep_paciente` | null \| string | `"03414010"` |
| `codigo_etnia_indigena_paciente` | null \| string | `"0238"` |
| `descricao_local_aplicacao` | string | `"Deltóide Direito"` |
| `numero_idade_paciente` | string | `"4"` |
| `codigo_lote_vacina` | string | `"2602123/00"` |
| `codigo_cnes_estabelecimento` | string | `"2788896"` |
| `descricao_vacina_fabricante` | null \| string | `"FUNDACAO BUTANTAN"` |
| `codigo_tipo_estabelecimento` | string | `"02"` |
| `codigo_natureza_estabelecimento` | string | `"1"` |
| `codigo_raca_cor_paciente` | string | `"99"` |
| `codigo_vacina_grupo_atendimento` | null \| string | `"000210"` |
| `codigo_paciente` | string | `"f99a65b4a655b633d590c4c20a2e00b1c0fec550928a8a3ee32d53d5c1a…` |
| `descricao_sistema_origem` | string | `"Novo PNI"` |
| `codigo_municipio_paciente` | null \| string | `"355030"` |
| `nome_municipio_paciente` | null \| string | `"SAO PAULO"` |
| `nome_fantasia_estalecimento` | string | `"UBS VILA FORMOSA II"` |
| `descricao_condicao_maternal` | null \| string | `"Nenhuma"` |
| `codigo_local_aplicacao` | string | `"1"` |
| `sigla_uf_paciente` | null \| string | `"SP"` |
| `nome_uf_estabelecimento` | string | `"SAO PAULO"` |
| `codigo_vacina` | string | `"33"` |
| `descricao_via_administracao` | null \| string | `"Intramuscular"` |
| `codigo_estrategia_vacinacao` | null \| string | `"1"` |
| `descricao_origem_registro` | null \| string | `"Registro anterior/Transcrição de caderneta"` |
| `data_entrada_rnds` | string | `"2026-05-25 17:59:45-03"` |
| `nome_etnia_indigena_paciente` | null \| string | `"WAPIXANA (UAPIXANA, VAPIDIANA, WAPISIANA, WAPISHANA)"` |
| `tipo_sexo_paciente` | string | `"M"` |
| `descricao_nacionalidade_paciente` | string | `"B"` |
| `codigo_troca_documento` | null \| string | `"7981d63d-b709-4750-9349-52d819672a62-i0b0"` |
| `codigo_dose_vacina` | string | `"9"` |

## `/economia-da-saude/bps`

Banco de Preços em Saúde (BPS) com parâmetros de pesquisa alinhados ao consultarMaterial e campos em camelCase.

- URL: `https://apidadosabertos.saude.gov.br/economia-da-saude/bps?codigoCatmat=267512&pagina=1&tamanhoPagina=100`
- HTTP: 200
- Envelope: `{"bps": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `anoCompra` | integer | `2026` |
| `nomeInstituicao` | string | `"CONSORCIO INTERMUNICIPAL DO VALE DO SAO FRANCISCO - CONIVAL…` |
| `cnpjInstituicao` | string | `"28715986000103"` |
| `municipio` | string | `"AMPARO DE SAO FRANCISCO"` |
| `estado` | string | `"SE"` |
| `dataCompra` | string | `"2026-07-14"` |
| `dataInsercao` | string | `"2026-07-29"` |
| `codigoCatmat` | string | `"267512"` |
| `descricaoItem` | string | `"AMITRIPTILINA CLORIDRATO, DOSAGEM:25 MG"` |
| `unidadeFornecimento` | string | `"COMPRIMIDO"` |
| `generico` | null \| string | `"S"` |
| `registroAnvisa` | null \| string | `"1558400670029"` |
| `modalidade` | string | `"Pregão"` |
| `tipoCompra` | string | `"ADMINISTRATIVA"` |
| `capacidade` | null | `null` |
| `unidadeMedidaCapacidade` | string | `"COMPRIMIDO"` |
| `cnpjFornecedor` | string | `"08778201000126"` |
| `nomeFornecedor` | string | `"DROGAFONTE LTDA"` |
| `cnpjFabricante` | string | `"05161069000110"` |
| `nomeFabricante` | string | `"BRAINFARMA INDUSTRIA QUIMICA E FARMACEUTICA S.A."` |
| `quantidade` | integer | `5310720` |
| `precoUnitario` | number | `0.0353` |
| `precoTotal` | number | `187468.416` |
| `siglaUnidadeMedida` | null | `null` |
| `codigoClasse` | string | `"6505"` |
| `nomeClasse` | string | `"DROGAS E MEDICAMENTOS"` |
| `codigoGrupo` | string | `"65"` |
| `nomeGrupo` | string | `"Equipamentos e artigos para uso médico, dentário e veterina…` |
| `numeroProcessoCompra` | string | `"01.28.01.2026"` |
| `esfera` | string | `"MUNICIPAL"` |
| `numeroAta` | null \| string | `"N° 65 á 82 /2026"` |
| `validadeCompra` | integer | `12` |
| `codigoPdm` | string | `"5134"` |
| `nomePdm` | string | `"AMITRIPTILINA CLORIDRATO"` |
| `observacoes` | null \| string | `"Registro de preço para aquisição de medicamentos - Pregão e…` |

## `/economia-da-saude/sistema-de-apuracao-e-gestao-de-custos-do-sus-apurasus`

Número de unidades de saúde usando o ApuraSUS por tipo de estabelecimento. Base de dados de custos em saúde, disponível para alimentação gratuita para todos os estabelecimentos de saúde

- URL: `https://apidadosabertos.saude.gov.br/economia-da-saude/sistema-de-apuracao-e-gestao-de-custos-do-sus-apurasus?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"unidades_apurasus": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nome_fantasia_da_unidade` | null \| string | `"INSTITUTO DE PERINATOLOGIA DA BAHIA - IPERBA - GD"` |
| `unidade_da_federacao` | null \| string | `"Bahia"` |
| `codigo_ibge` | null \| string | `"292740"` |
| `bairro` | null \| string | `"BROTAS"` |
| `cnes` | null \| string | `"0003794"` |
| `latitude` | null \| string | `"12.985.343.165.979.300"` |
| `uf` | null \| string | `"BA"` |
| `municipio` | null \| string | `"Salvador"` |
| `longitude` | null \| string | `"-3.847.686.767.578.120"` |

## `/outros-temas/ced`

CED - Sistema de controle de demandas abertas para a equipe de banco de dados, GAAD.

- URL: `https://apidadosabertos.saude.gov.br/outros-temas/ced?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"ced": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nome_sistema` | string | `"Sistema de Gestão Documental do FNS"` |
| `gestor` | string | `"PATRICK HERINGER REIS"` |
| `sigla_sistema` | string | `"FNSDOC"` |

## `/prevencao-e-promocao/distribuicao-epi-insumo`

Esta base de dados possui informações sobre os equipamentos de proteção individual (EPI) e insumos de saúde distribuídos em razão do combate à emergência de saúde pública de importância internacional decorrente da Covid-19.

- URL: `https://apidadosabertos.saude.gov.br/prevencao-e-promocao/distribuicao-epi-insumo?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"distribuicao_epi_insumo": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `quantidade` | string | `"9,6"` |
| `unidade` | string | `"Litro"` |
| `material` | string | `"Álcool"` |
| `numero_do_pedido` | string | `"308748"` |
| `data_de_saida` | string | `"19/03/2020"` |
| `status` | string | `"Entregue"` |
| `requisitante_destino` | string | `"Acre"` |

## `/saude-indigena/sasisus-esgotamento-sanitario`

Caracterização das formas de esgotamento sanitário nas aldeias agregadas por Dsei.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sasisus-esgotamento-sanitario?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"esgotamento_sanitario": "array[35]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `exist_estrut_perc_ald_sem_estrutura` | string | `"0%"` |
| `est_conserv_estrut_perc_ald_estrut_exist_regular` | string | `"91%"` |
| `tipo_trat_esgoto_perc_ald_tratamento_por_fossa_filtro_sumidouro` | string | `"0%"` |
| `est_conserv_estrut_perc_ald_estrut_exist_requer_interd_subst` | string | `"0%"` |
| `tipo_trat_esgoto_perc_ald_destinacao_nos_corpos_hidricos` | string | `"0%"` |
| `tipo_trat_esgoto_perc_ald_sem_informacao` | string | `"100%"` |
| `exist_estrut_perc_ald_melhorias_sanits_domic_mds_indiv_coletiv` | string | `"0%"` |
| `exist_estrut_perc_ald_coleta_pela_rede_publica` | string | `"9%"` |
| `est_conserv_estrut_perc_ald_onde_nao_existe_estrut_tratamento` | string | `"0%"` |
| `est_conserv_estrut_perc_ald_estrut_exist_satisfatoria` | string | `"0%"` |
| `exist_estrut_perc_ald_coleta_pela_rede_sesai` | string | `"0%"` |
| `exist_estrut_perc_ald_sem_informacao` | string | `"0%"` |
| `tipo_trat_esgoto_perc_ald_tratamento_por_fossa_seca` | string | `"0%"` |
| `est_conserv_estrut_perc_ald_sem_informacao_sobre_a_estrutura` | string | `"0%"` |
| `est_conserv_estrut_perc_ald_estrut_exist_insatisfatoria` | string | `"9%"` |
| `est_conserv_estrut_perc_ald_estrut_exist_requer_manutencao` | string | `"0%"` |
| `distrito_sanitario_especial_indigena` | string | `"ALAGOAS E SERGIPE"` |
| `tipo_trat_esgoto_perc_ald_tratamento_por_fossa_rudimentar` | string | `"0%"` |
| `tipo_trat_esgoto_perc_ald_tratamento_por_fossa_sumidouro` | string | `"0%"` |
| `tipo_trat_esgoto_perc_ald_sem_tratamento` | string | `"0%"` |
| `tipo_trat_esgoto_perc_ald_atendidas_por_concessionaria` | string | `"0%"` |
| `exist_estrut_perc_ald_casinha_latrina` | string | `"0%"` |
| `exist_estrut_perc_ald_banheiro_particular` | string | `"91%"` |

## `/saude-indigena/sasi-sus-gerenciamento-de-residuos-solidos`

Caracterização das formas de gerenciamento de resíduos sólidos nas aldeias, por Dsei.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sasi-sus-gerenciamento-de-residuos-solidos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"gerenciamento_residuos_solidos": "array[35]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `coleta_e_destinacao_de_residuos_solidos_percentual_de_aldeias_onde_o_dsei_e_o_principal_responsavel` | string | `"0%"` |
| `coleta_e_destinacao_de_residuos_solidos_percentual_de_aldeias_onde_nao_ha_informacao_sobre_os_responsaveis` | string | `"39%"` |
| `coleta_e_destinacao_de_residuos_solidos_percentual_de_aldeias_onde_os_catadores_sao_os_principais_responsaveis` | string | `"0%"` |
| `coleta_e_destinacao_de_residuos_solidos_percentual_de_aldeias_onde_a_prefeitura_e_a_principal_responsavel` | string | `"61%"` |
| `coleta_e_destinacao_de_residuos_solidos_percentual_de_aldeias_onde_a_propria_aldeia_e_a_principal_responsavel` | string | `"0%"` |
| `destinacao_dos_residuos_organicos_percentual_de_aldeias_que_destinam_os_residuos_organicos_junto_com_os_residuos_comuns` | string | `"0%"` |
| `destinacao_dos_residuos_organicos_percentual_de_aldeias_que_destinam_os_residuos_organicos_no_lixao_da_aldeia` | string | `"0%"` |
| `destinacao_dos_residuos_organicos_percentual_de_aldeias_que_destinam_os_residuos_organicos_na_mata_longe_das_aldeias` | string | `"0%"` |
| `destinacao_dos_residuos_organicos_percentual_de_aldeias_que_utilizam_os_residuos_organicos_para_alimentacao_de_animais` | string | `"100%"` |
| `destinacao_dos_residuos_organicos_percentual_de_aldeias_que_utilizam_os_residuos_organicos_para_compostagem` | string | `"0%"` |
| `destinacao_dos_residuos_organicos_percentual_de_aldeias_sem_informacao_sobre_a_destinacao_dos_residuos_organicos` | string | `"0%"` |
| `distrito_sanitario_especial_indigena_dsei` | string | `"ALAGOAS E SERGIPE"` |
| `logistica_reversa_percentual_de_aldeias_que_realizam_logistica_reserva` | string | `"0%"` |
| `possui_coleta_seletiva_implantada_percentual_de_aldeias_que_nao_possuem_coleta_seletiva` | string | `"100%"` |
| `possui_coleta_seletiva_implantada_percentual_de_aldeias_que_possuem_coleta_seletiva` | string | `"0%"` |
| `possui_coleta_seletiva_implantada_percentual_de_aldeias_sem_informacao_sobre_coleta_seletiva` | string | `"0%"` |
| `possui_vala_construida_pela_comunidade_percentual_de_aldeias_com_presenca_de_valas_construidas_pela_comunidade` | string | `"45%"` |
| `possui_vala_construida_pela_comunidade_percentual_de_aldeias_que_nao_possuem_valas_construidas_pela_comunidade` | string | `"55%"` |
| `possui_vala_construida_pela_comunidade_percentual_de_aldeias_sem_informacoes_sobre_valas_construidas_pela_comunidade` | string | `"0%"` |
| `pratica_de_queima_de_residuos_pela_comunidade_percentual_de_aldeias_que_possuem_a_pratica_de_queima_dos_residuos` | string | `"55%"` |
| `pratica_de_queima_de_residuos_pela_comunidade_percentual_de_aldeias_que_nao_possuem_a_pratica_de_queima_dos_residuos` | string | `"45%"` |
| `pratica_de_queima_de_residuos_pela_comunidade_percentual_de_aldeias_sem_informacao_sobre_a_pratica_de_queima_dos_residuos` | string | `"0%"` |

## `/saude-indigena/acompanhamento-obra-infraestrutura-saude`

Microdados dos acompanhamentos de Obras de Infraestruturas de Saúde e Saneamento da Secretaria de Saúde Indígena.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/acompanhamento-obra-infraestrutura-saude?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"acompanhamento_obra_infraestruturas_saude": "array[0]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `acompanhamento_obra_infraestruturas_saude` | array | `[]` |

## `/saude-indigena/planilha-de-fornecimento-e-monitoramento-da-qualidade-da-agua-acesso-a-agua`

Microdados dos acompanhamentos de Fornecimento e Monitoramento da Qualidade da Água da Secretaria de Saúde Indígena.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/planilha-de-fornecimento-e-monitoramento-da-qualidade-da-agua-acesso-a-agua?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"fornecimento_monitoramento_qualidade_acesso_agua": "array[34]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `populacao_total` | string | `"13243"` |
| `_de_aldeias_monitoradas_em_relacao_ao_total` | string | `"4%"` |
| `sem_info_pop` | string | `"0"` |
| `_aldeia_sem_fornecimento` | string | `"0%"` |
| `pop_total_com_infraestrutura_de_abastecimento` | string | `"10798"` |
| `n_aldeias_pmqai` | string | `"32"` |
| `requer_substituicao_pop` | null \| string | `"179"` |
| `_aldeias_com_infraestrutura` | string | `"58%"` |
| `numero_de_aldeias` | string | `"33"` |
| `satisfatorio_pop` | string | `"7949"` |
| `soma_de_infraestrutura_saasac` | string | `"19"` |
| `satisfatorio__aldeia` | string | `"48%"` |
| `dsei` | string | `"ALAGOAS E SERGIPE"` |
| `_aldeia_abastecimento_caminhao_pipa` | string | `"42,4%"` |
| `pop_total_abastecimento_por_caminhao_pipa` | null \| string | `"2445"` |
| `_de_aldeias_monitoradas_em_relacao_ao_pmqai_planejado` | string | `"4%"` |
| `requer_manutencao_pop` | string | `"2849"` |
| `media_do_numero_de_aldeias_monitoradas_no_mes_com_analise_dos_6` | string | `"1"` |
| `pop_sem_fornecimento` | string | `"0"` |
| `requer_manutencao__aldeia` | string | `"9%"` |
| `requer_substituicao__aldeia` | string | `"0%"` |
| `sem_info__aldeia` | string | `"0%"` |

## `/saude-indigena/planilha-registros-habilitacao-recebimento-incentivo`

Estabelecimentos de saúde habilitados ao recebimento do IAE-PI

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/planilha-registros-habilitacao-recebimento-incentivo?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"registros_habilitacao_recebimento_incentivo": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `municipio` | string | `"Água Branca"` |
| `estado` | string | `"ALAGOAS - AL"` |
| `cnes` | string | `"3798593"` |
| `situacao` | string | `"HABILITADO"` |
| `tipo_estabelecimento` | string | `"CAPS I"` |
| `regiao` | string | `"NORDESTE"` |
| `dsei` | string | `"DSEI ALAGOAS E SERGIPE"` |
| `nome_do_estabelecimento` | string | `"CENTRO DE ATENCAO PSICOSSOCIAL JOYCE DE MILLE"` |
| `mesano_publicacao` | string | `"nov/19"` |
| `portaria` | string | `"PORTARIA Nº 2.968, DE 11 DE NOVEMBRO DE 2019"` |

## `/saude-indigena/indicadores-enfrentamento-monitoramento-covid19-indigenas`

Dados referentes aos indicadores de enfrentamento e monitoramento à Covid-19 dos Povos Indígenas Brasileiros

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/indicadores-enfrentamento-monitoramento-covid19-indigenas?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"indicadores_enfrentamento_monitoramento_covid19_indigenas": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `dsei` | string | `"ALAGOAS E SERGIPE"` |
| `quantidade` | string | `"1"` |
| `tipo_de_vinculo` | string | `"CONTRATO TERCEIRIZADO - DECRETO NÂº 2.271/97"` |
| `atuacao` | string | `"CASAI"` |
| `categoria_profissional` | string | `"MOTORISTA"` |

## `/saude-indigena/sistema-de-atencao-a-saude-indigena-modulo-de-vigilancia-alimentar-e-nutricional`

Os dados disponibilizados são referentes ao módulo de Vigilância Alimentar e Nutricional (VAN) da base nacional do Sistema de Atenção à Saúde Indígena (Siasi) de crianças indígenas menores de 5 anos.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sistema-de-atencao-a-saude-indigena-modulo-de-vigilancia-alimentar-e-nutricional?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"siasi_modulo_van": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `gestao_do_dsei` | string | `"ALAGOAS E SERGIPE"` |
| `descricao_do_polo_base` | string | `"KALANKÓ"` |
| `nome_da_terra_indigena` | string | `"A qualificar para validação"` |
| `codigo_do_ibge` | string | `"270010"` |
| `nome_do_municipio` | string | `"AGUA BRANCA"` |
| `sigla_da_uf` | string | `"AL"` |
| `data_de_nascimento` | string | `"2020/07/15 00:00:00.000"` |
| `tipo_sexo` | string | `"M"` |
| `data_de_atendimento` | string | `"2022/12/29 00:00:00.000"` |
| `mes_de_atendimento` | string | `"12"` |
| `ano_de_atendimento` | string | `"2022"` |
| `idade_em_meses_no_atendimento` | number | `29.0` |
| `numero_do_peso` | string | `"12,00"` |
| `numero_da_altura` | string | `"88,00"` |
| `idade_no_atendimento` | number | `2.0` |
| `descricao_do_tipo_de_acompanhamento_nutricional` | string | `"Visita Domiciliar"` |
| `tipo_de_aleitamento` | string | `"Alimentação Complementar"` |
| `descricao_peso_idade` | string | `"PESO ADEQUADO PARA A IDADE"` |
| `descricao_estatura_idade` | string | `"ESTATURA ADEQUADA PARA A IDADE"` |
| `descricao_imc_idade` | string | `"EUTROFIA"` |
| `codigo_do_profissional` | string | `"11298"` |
| `codigo_cbo_da_familia` | string | `"5151"` |
| `descricao_do_cbo_da_familia` | string | `"TRABALHADORES EM SERVIÇOS DE PROMOÇÃO E APOIO À SAÚDE"` |
| `codigo_cbo_da_ocupacao` | string | `"515125"` |
| `descricao_do_cbo_da_ocupacao` | string | `"Agente indígena de saúde"` |

## `/atencao-primaria/enani-2019`

Base com estudo nacional de alimentação e nutrição infantil: ENANI-2019

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/enani-2019?limit=10&offset=0`
- HTTP: 200
- Envelope: `{"enani": "array[10]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `i063_18m_objetos` | string | `"Ainda não"` |
| `l13_menos18_sentiu_fome` | string | `"Não"` |
| `m1006_p06` | string | `"NA"` |
| `x07_total_criancas` | string | `"2"` |
| `vd_supl1_com_vite` | string | `"Sim"` |
| `vd_supl1_multivitaminico_com_minerais` | string | `"Sim"` |
| `i047_12m_pedidos` | string | `"NA"` |
| `n05_suco` | string | `"Às vezes"` |
| `vd_pla_final` | string | `"485000"` |
| `vd_supl1_somente_zinco` | string | `"Não"` |
| `i117_59m_figuras` | string | `"NA"` |
| `u03a_puncao_motivo` | null \| string | `"ACESSO VENOSO DIFICIL"` |
| `e189_nao_sabe` | string | `"Não"` |
| `peso_crianca_y_13` | string | `"1265,96752307336"` |
| `h129_alergia_nao_sabe` | string | `"NA"` |
| `k179_alimento_nao_sabe` | string | `"Não"` |
| `w01a_qual_outro` | null | `null` |
| `r05_vcr` | string | `"Não"` |
| `vd_supl1_com_vitb5` | string | `"Sim"` |
| `i010_4m_cabeca` | string | `"NA"` |
| `peso_crianca_setor` | string | `"7,21428571428571"` |
| `i119_59m_sabe` | string | `"NA"` |
| `grupo10` | string | `"Sim"` |
| `peso_crianca_y_1b` | string | `"1225,45717959063"` |
| `h212_internado_intestinais` | string | `"Não"` |
| `grupo9b` | string | `"Sim"` |
| `vd_supl1_com_vitk` | string | `"Não"` |
| `i056_15m_escadas` | string | `"NA"` |
| `s35_altura_padrao` | string | `"NA"` |
| `e01_leite_peito` | string | `"Não"` |
| `grupo21` | string | `"Sim"` |
| `i021_6m_olha` | string | `"NA"` |
| `p12_lixo` | string | `"Coletado diretamente por serviço de limpeza"` |
| `s00e_data_altura` | string | `"22072019"` |
| `e20_iogurte` | string | `"Não"` |
| `i000d_data_ajustada` | string | `"11092017"` |
| `vd_anthro_zwfl` | string | `"-0,3"` |
| `h01_semanas_gravidez` | string | `"38"` |
| `j0506_rel_protestante_historica` | string | `"Não"` |
| `p02a_outro` | null | `null` |
| `u05_braco` | string | `"Esquerdo"` |
| `vd_supl1_ferro_nao_sus` | string | `"Não"` |
| `s02a_medida2_realizada` | string | `"Sim"` |
| `vd_vita_final` | string | `"0,23"` |
| `vd_supl1_com_vitc` | string | `"Não"` |
| `i075_24m_ajuda` | string | `"NA"` |
| `k243_utilizou_bico` | string | `"Não"` |
| `peso_crianca_y_20` | string | `"1116,25497434697"` |
| `j03_cor` | string | `"Parda (mulata, cabocla, cafuza, mameluca ou mestiça)"` |
| `i000e_semanas_gravidez` | string | `"38"` |
| `vd_hb_fonte` | string | `"Coleta"` |
| `o06_refrigerantes_variedade` | string | `"Concordo totalmente"` |
| `i071_24m_sozinha` | string | `"NA"` |
| `vd_supl1_com_vitb2` | string | `"Sim"` |
| `p08_banheiros_exclusivo` | string | `"1"` |
| `i028_6m_mao` | string | `"NA"` |
| `k175_alimento_acucar` | string | `"Não"` |
| `grupo1c` | string | `"Sim"` |
| `i000b_data_do_dia` | string | `"22072019"` |
| `n16_forcar_comer` | string | `"NA"` |
| `s11_altura_observacoes` | null | `null` |
| `m1007_p07` | string | `"NA"` |
| `vd_supl1_somente_vitc` | string | `"Não"` |
| `total_12p` | string | `"12"` |
| `vd_linfo_final` | string | `"4192"` |
| `e06_leite_vaca_po` | string | `"Não"` |
| `peso_crianca_y_5` | string | `"1131,73726687159"` |
| `vd_supl1_com_selenio` | string | `"Não"` |
| `i005_2m_maos` | string | `"NA"` |
| `vd_supl1_vita_indep_mega_nutrisus` | string | `"Sim"` |
| `vd_d053_almoco` | string | `"NA"` |
| `vd_num_supl` | string | `"3"` |
| `vd_supl1_multivitaminico_sem_minerais_bc` | string | `"Não"` |
| `vd_imc_mae` | string | `"21,2498555475457"` |
| `e26_feijao` | string | `"Sim"` |
| `i060_18m_corre` | string | `"Um pouco"` |
| `b05a_idade_em_meses` | string | `"22 meses"` |
| `vd_supl1_multivitaminico_sem_minerais` | string | `"Não"` |
| `i007_2m_sentada` | string | `"NA"` |
| `bb04_idade_da_mae` | string | `"27"` |
| `h10a_consulta_outro` | null | `null` |
| `i089_30m_responde` | string | `"NA"` |
| `i9941_cafe_manha` | string | `"NA"` |
| `r14_celular` | string | `"Pré-pago"` |
| `k27_idade_medida` | string | `"Meses"` |
| `k19_somente_medida` | string | `"Dias"` |
| `peso_crianca_y_22` | string | `"1163,15806149153"` |
| `l10_menos18_insuficiente` | string | `"Não"` |
| `q033_beneficio_prefeitura` | string | `"Não"` |
| `q01_recebe_beneficio` | string | `"Sim"` |
| `peso_crianca_y_9a` | string | `"1457,48973249519"` |
| `h20_outro_problema` | string | `"Não"` |
| `i029_6m_puxa` | string | `"NA"` |
| `i062_18m_chuta` | string | `"Um pouco"` |
| `h07_chupeta_medida1` | string | `"NA"` |
| `m1020_p20` | string | `"NA"` |
| `u30b_volume_edta` | string | `"NA"` |
| `m1011_p11` | string | `"NA"` |
| `h211_internado_respiratoria` | string | `"Não"` |
| `grupo1b` | string | `"Sim"` |
| `idade_anos_comp` | string | `"1"` |
| `s09_altura_feita_corrigida` | string | `"Deitada"` |
| `vd_supl1_com_vitb1` | string | `"Sim"` |
| `k07_peso_final` | string | `"68"` |
| `u27a_coleta_hora` | string | `"NA"` |
| `vd_supl1_multivitaminico_sem_minerais_abcdek` | string | `"Não"` |
| `datablb` | string | `"22072019"` |
| `e32_suco_industrializado` | string | `"Não"` |
| `vd_ien_tercos` | string | `"1º"` |
| `i101_48m_responde` | string | `"NA"` |
| `h10b3_sindrome_fibrose` | string | `"Não"` |
| `e02_agua` | string | `"Sim"` |
| `e30_hamburger` | string | `"Não"` |
| `i043_12m_mama` | string | `"NA"` |
| `id_upa_anon` | string | `"10718"` |
| `r06_lavadora` | string | `"Não"` |
| `vd_zhaz` | string | `"-0,1"` |
| `vd_mono_final` | string | `"868"` |
| `i037_9m_sons` | string | `"NA"` |
| `vd_linftp_final` | string | `"NA"` |
| `vd_d054_lanche_tarde` | string | `"NA"` |
| `i095_36m_responde` | string | `"NA"` |
| `o01_frutas_comprar` | string | `"Discordo totalmente"` |
| `i106_48m_urinar` | string | `"NA"` |
| `vd_supl1_multi_sem_com_minerais` | string | `"Sim"` |
| `i113_59m_ontem` | string | `"NA"` |
| `i041_12m_puxa` | string | `"NA"` |
| `t03a_peso_padrao` | string | `"Sim, foi feita seguindo o protocolo (mínimo de roupas)"` |
| `d04_refeicao` | string | `"NA"` |
| `i055_15m_corre` | string | `"NA"` |
| `m02_quem_cozinha` | string | `"Pessoa 1"` |
| `e183_peneira` | string | `"Não"` |
| `i9944_lanche_tarde` | string | `"NA"` |
| `i081_30m_atencao` | string | `"NA"` |
| `vd_suplemento_comercial` | string | `"Sim"` |
| `u26_puncao` | string | `"NA"` |
| `vd_vitb1_final` | string | `"77"` |
| `i018_4m_procura` | string | `"NA"` |
| `m1004_p04` | string | `"NA"` |
| `r04_geladeira` | string | `"Sim"` |
| `i9945_jantar` | string | `"NA"` |
| `vd_zn_final` | string | `"89,5"` |
| `vd_vite_fonte` | string | `"Coleta"` |
| `n06_refrigerantes` | string | `"Raramente"` |
| `peso_crianca_y_18` | string | `"1136,22025471506"` |
| `vd_vita_fonte` | string | `"Coleta"` |
| `id_resp_anon` | string | `"10951000401"` |
| `s02_peso_medida1` | string | `"11,5"` |
| `b06a_porque` | null | `null` |
| `grupo16` | string | `"Sim"` |
| `vd_dummy_domic_ien` | string | `"1"` |
| `l01_morador_alim_acabassem` | string | `"Sim"` |
| `d05a_refeicao_outra` | null | `null` |
| `t04a_altura_motivo` | null | `null` |
| `vd_vcm_final` | string | `"73,1"` |
| `vd_pcr_fonte` | string | `"Coleta"` |
| `j0503_rel_evangelica_pentecostal` | string | `"Sim"` |
| `g150_vitaminas` | string | `"Sim"` |
| `u22_recoleta_realizada` | string | `"NA"` |
| `m05_organiza` | string | `"Sim, sempre"` |
| `t03b01_roupa_bermuda_de_brim` | string | `"NA"` |
| `q07_renda_faixa` | string | `"Até R$ 1.000,00"` |
| `h126_alergia_frutas` | string | `"NA"` |
| `r03_radio` | string | `"Não"` |
| `s28_peso_observacoes` | null | `null` |
| `e10_formula_infantil` | string | `"Não"` |
| `i004_2m_cabeca` | string | `"NA"` |
| `vd_supl1_com_calcio` | string | `"Não"` |
| `vd_supl1_multivitaminico_sem_minerais_abcde` | string | `"Não"` |
| `i025_6m_segura` | string | `"NA"` |
| `h10b5_sindrome_autismo` | string | `"Não"` |
| `p10_esgoto` | string | `"Fossa rudimentar"` |
| `u24b_refeicao_minuto` | string | `"NA"` |
| `vd_supl1_vita_nao_sus` | string | `"Não"` |
| `h121_alergia_leite` | string | `"NA"` |
| `i116_59m_copia` | string | `"NA"` |
| `s24_peso_padrao` | string | `"NA"` |
| `s29a_medida1_peso_refeita` | string | `"Não foi refeita ou não se aplica"` |
| `peso_crianca_y_21` | string | `"1160,45122011024"` |
| `vd_linfat_final` | string | `"NA"` |
| `idade` | null \| string | `"1a10m"` |
| `vd_ebia_categ` | string | `"Insegurança leve"` |
| `h14_tosse` | string | `"Sim"` |
| `i013_4m_sentada` | string | `"NA"` |
| `e04_agua_com_acucar` | string | `"Não"` |
| `s07b_descreva_crianca_altura` | null \| string | `"CRIANCA AGITADA"` |
| `u03_puncao` | string | `"Não"` |
| `vd_ferri_fonte` | string | `"Coleta"` |
| `q034_beneficio_estado` | string | `"Não"` |
| `q035_pensao` | string | `"Não"` |
| `vd_supl1_com_cobre` | string | `"Não"` |
| `i049_12m_escadas` | string | `"NA"` |
| `k172_alimento_formulas` | string | `"Não"` |
| `s03_peso_medida2` | string | `"11,4"` |
| `j0504_rel_espirita_kardecista` | string | `"Não"` |
| `e27_carne` | string | `"Sim"` |
| `i054_15m_pedidos` | string | `"NA"` |
| `r01_televisao` | string | `"1 aparelho"` |
| `d05_quais_refeicoes` | null \| string | `"B"` |
| `i086_30m_perguntas` | string | `"NA"` |
| `n13_comer_bala` | string | `"NA"` |
| `b02_sexo` | string | `"Masculino"` |
| `grupo12` | string | `"Sim"` |
| `q06_renda` | string | `"900"` |
| `n04_feijao` | string | `"Sempre"` |
| `n11_pegar_refrigerante` | string | `"NA"` |
| `i107_48m_regras` | string | `"NA"` |
| `u23_febre_diarreia` | string | `"NA"` |
| `vd_supl1_multivitaminico_sem_minerais_b` | string | `"Não"` |
| `l14_menos18_sem_comer` | string | `"Não"` |
| `i016_4m_barriga` | string | `"NA"` |
| `m03_alimentos_basicos` | string | `"Sim, sempre"` |
| `h16_canseira` | string | `"Não"` |
| `vd_supl1_exclusivamente_vita` | string | `"Não"` |
| `peso_crianca_y_9b` | string | `"1294,69586663512"` |
| `q039_nao_sabe` | string | `"Não"` |
| `q037_outro_beneficio` | string | `"Não"` |
| `i000_2m_faz` | string | `"NA"` |
| `vd_supl1_com_cipro` | string | `"Não"` |
| `f001_esta_usando` | string | `"Sim"` |
| `j10_serie` | string | `"1°ano do ensino médio"` |
| `o05_refrigerantes_comprar` | string | `"Concordo totalmente"` |
| `i045_12m_sons` | string | `"NA"` |
| `t03b_quais_das_seguintes_pecas` | null | `null` |
| `u08a_observacoes` | null | `null` |
| `n10_guardar_frutas` | string | `"NA"` |
| `e34_macarrao` | string | `"Não"` |
| `grupo19` | string | `"Sim"` |
| `s33a_altura_medida4` | string | `"NA"` |
| `vd_bastp_final` | string | `"0"` |
| `vd_chcm_final` | string | `"34,3"` |
| `grupo13` | string | `"Sim"` |
| `grupo18` | string | `"Sim"` |
| `h10b9_sindrome_nao_sabe` | string | `"Não"` |
| `e07_leite_vaca_liquido` | string | `"Sim"` |
| `i993_faltou_alguma_refeicao` | string | `"Não"` |
| `q032_bpc_loas` | string | `"Não"` |
| `i103_48m_desenha` | string | `"NA"` |
| `h125_alergia_trigo` | string | `"NA"` |
| `l11_menos18_diminuiu` | string | `"Não"` |
| `i032_9m_mao` | string | `"NA"` |
| `vd_supl1_bc_cipro` | string | `"Não"` |
| `vd_eosp_final` | string | `"2,4"` |
| `u28_braco` | string | `"NA"` |
| `vd_supl1_com_fosforo` | string | `"Não"` |
| `n17_comer_menos` | string | `"NA"` |
| `vd_dummy_gravida` | string | `"0"` |
| `vd_vitb6_fonte` | string | `"Coleta"` |
| `l05_adulto_saltou_refeicao` | string | `"Não"` |
| `k14_ainda` | string | `"Não"` |
| `p07_dormitorios` | string | `"1"` |
| `n15_come_suficiente` | string | `"NA"` |
| `k06_peso_engravidar` | string | `"48"` |
| `vd_mielop_final` | string | `"NA"` |
| `k13_tempo_medida` | string | `"Horas"` |
| `u22a_recoleta_motivo` | string | `"NA"` |
| `estrato_sel_anon` | string | `"1041"` |
| `h20a_problema_outro` | null \| string | `"ESCABIOSE"` |
| `vd_vitb1_fonte` | string | `"Coleta"` |
| `u29_tubos` | string | `"NA"` |
| `p06_cozinha` | string | `"Sim"` |
| `grupo3` | string | `"Sim"` |
| `i109_48m_figuras` | string | `"NA"` |
| `k11_amamentou` | string | `"Sim"` |
| `k248_utilizou_nao` | string | `"Sim"` |
| `s02b_descreva_crianca` | null | `null` |
| `vd_supl1_com_vitb3` | string | `"Sim"` |
| `b04_idade` | string | `"1"` |
| `s21c_idade_recalculada_peso` | string | `"NA"` |
| `i044_12m_olha` | string | `"NA"` |
| `w01_motivo` | string | `"Completa, mas falta o exame de sangue"` |
| `l12_menos18_saltou_refeicao` | string | `"Não"` |
| `u27b_coleta_minuto` | string | `"NA"` |
| `e23_cenoura` | string | `"Não"` |
| `p05_comodos` | string | `"5"` |
| `j0502_rel_evangelica_tradicional` | string | `"Não"` |
| `i064_18m_corpo` | string | `"Ainda não"` |
| `e08_leite_soja_po` | string | `"Não"` |
| `s33_altura_medida3` | string | `"NA"` |
| `k04_prenatal_semanas` | string | `"7"` |
| `vd_segp_final` | string | `"52,4"` |
| `s21a_pode_informar_peso` | string | `"NA"` |
| `id_domic_anon` | string | `"109510004"` |
| `t03b06_roupa_outra` | string | `"NA"` |
| `h128_alergia_outro` | string | `"NA"` |
| `vd_supl1_multivitaminico_sem_minerais_outros` | string | `"Não"` |
| `i035_9m_mama` | string | `"NA"` |
| `p11a_agua_outra` | null | `null` |
| `r07_micro_ondas` | string | `"Não"` |
| `m1008_p08` | string | `"NA"` |
| `peso_crianca_y_11` | string | `"1337,77078486162"` |
| `vd_supl1_somente_vitd` | string | `"Não"` |
| `peso_crianca_y_14` | string | `"1133,55963929134"` |
| `n09_balas` | string | `"Nunca"` |
| `h21a_doenca_outra` | null | `null` |
| `q031_programa_bolsa_familia` | string | `"Sim"` |
| `s08_altura_medida2` | string | `"86,1"` |
| `vd_metap_final` | string | `"NA"` |
| `i052_15m_sons` | string | `"NA"` |
| `peso_crianca` | string | `"859,598538120578"` |
| `h213_internado_acidente` | string | `"Sim"` |
| `peso_crianca_y_16` | string | `"1117,03885163964"` |
| `i023_6m_brinquedo` | string | `"NA"` |
| `m1001_p01` | string | `"NA"` |
| `h215_internado_outras` | string | `"Não"` |
| `vd_meta_final` | string | `"NA"` |
| `e214a_nao_comeu` | string | `"Sim"` |
| `grupo5` | string | `"Sim"` |
| `k18_somente` | string | `"3"` |
| `i008_2m_sons` | string | `"NA"` |
| `vd_leuco_final` | string | `"11270"` |
| `m1014_p14` | string | `"NA"` |
| `vd_supl1_com_zinco` | string | `"Sim"` |
| `q03_quais_beneficios` | null \| string | `"A"` |
| `j0505_rel_afro_brasileira` | string | `"Não"` |
| `t03b05_roupa_tenis_sapato` | string | `"NA"` |
| `e03_filtrada_fervida` | string | `"Não"` |
| `vd_supl1_com_vita` | string | `"Sim"` |
| `i069_18m_ajuda` | string | `"Ainda não"` |
| `l09_menos18_saudavel` | string | `"Não"` |
| `grupo1a` | string | `"Sim"` |
| `i051_15m_olha` | string | `"NA"` |
| `vd_zimc` | string | `"-0,2"` |
| `u07b_volume_edta` | string | `"2"` |
| `m1013_p13` | string | `"NA"` |
| `vd_supl1_com_iodo` | string | `"Não"` |
| `i096_36m_conta` | string | `"NA"` |
| `u07a_volume_trace` | string | `"5"` |
| `e212a_feito_em_casa` | string | `"Não"` |
| `e39_mamadeira` | string | `"Sim"` |
| `k08_quilos` | string | `"20"` |
| `s00c_data_peso` | string | `"22072019"` |
| `k16_liquido` | string | `"Sim"` |
| `vd_supl1_exclusivamente_vitd` | string | `"Não"` |
| `h19_febre` | string | `"Sim"` |
| `h02_peso` | string | `"2900"` |
| `i068_18m_combina` | string | `"Ainda não"` |
| `j06_ocupacao` | string | `"Desempregado e ativamente procurando por trabalho"` |
| `s39b_medida2_altura_refeita` | string | `"Não foi refeita ou não se aplica"` |
| `u07_volume` | string | `"7"` |
| `k20_doou` | string | `"Não"` |
| `j04_vive` | string | `"Sim"` |
| `n12_comer_biscoitos` | string | `"NA"` |
| `t06b_qual_das_pecas` | string | `"NA"` |
| `vd_suplemento_sus` | string | `"Sim"` |
| `i053_15m_anda` | string | `"NA"` |
| `t06a_altura_padrao` | string | `"Sim, foi feita seguindo o protocolo (mínimo de roupas)"` |
| `i027_6m_sentada` | string | `"NA"` |
| `u04b_coleta_minuto` | string | `"48"` |
| `l08_adulto_sem_comer` | string | `"Não"` |
| `vd_supl1_com_cromo` | string | `"Não"` |
| `e21_arroz` | string | `"Sim"` |
| `vd_supl1_com_vitb6` | string | `"Não"` |
| `i026_6m_bracos` | string | `"NA"` |
| `vd_dummy_domic_ebia` | string | `"1"` |
| `i036_9m_olha` | string | `"NA"` |
| `m01_costuma_cozinhar` | string | `"Sim, todos os dias da semana"` |
| `vd_supl1_outros_supl` | string | `"Não"` |
| `i9943_almoco` | string | `"NA"` |
| `x08_total_maes_resp` | string | `"1"` |
| `i079_24m_linhas` | string | `"NA"` |
| `j0510_rel_ns_nqr` | string | `"Não"` |
| `vd_vb12_final` | string | `"422"` |
| `p11_agua` | string | `"Poço ou nascente na propriedade"` |
| `r13_internet_celular` | string | `"Não"` |
| `e24_couve` | string | `"Não"` |
| `e38_farinhas` | string | `"Não"` |
| `h15_respiracao` | string | `"Não"` |
| `p02_tipo_de_domicilio` | string | `"Apartamento"` |
| `u26a_puncao_motivo` | null | `null` |
| `i105_48m_ontem` | string | `"NA"` |
| `s31c_idade_recalculada_alt` | string | `"NA"` |
| `setor_anon` | string | `"10951"` |
| `k244_utilizou_bomba` | string | `"Não"` |
| `i030_9m_bracos` | string | `"NA"` |
| `i033_9m_puxa` | string | `"NA"` |
| `vd_vit25_final` | string | `"55,3"` |
| `i110_59m_conta` | string | `"NA"` |
| `s22_permissao_peso` | string | `"NA"` |
| `vd_seg_final` | string | `"5905"` |
| `vd_supl1_com_vitb7` | string | `"Não"` |
| `peso_crianca_y_19` | string | `"1135,8638493108"` |
| `peso_crianca_y_7` | string | `"1272,96504192487"` |
| `datahorapedido_r` | null \| string | `"26/09/2019 16:28"` |
| `vd_afoli_fonte` | string | `"Coleta"` |
| `i094_36m_compara` | string | `"NA"` |
| `grupo4` | string | `"Sim"` |
| `g151_sache` | string | `"Não"` |
| `m1022_p22` | string | `"NA"` |
| `r08_telefone_fixo` | string | `"Não"` |
| `vd_hcm_final` | string | `"25,1"` |
| `i087_30m_explicar` | string | `"NA"` |
| `peso_crianca_y_4` | string | `"1205,44262835817"` |
| `i088_30m_compara` | string | `"NA"` |
| `m10_quem_divide` | null \| string | `"AF"` |
| `s39_altura_observacoes` | null | `null` |
| `s00f_idade_altura` | string | `"679"` |
| `j09_frequenta` | string | `"Já frequentou"` |
| `i083_30m_linhas` | string | `"NA"` |
| `j07_nao_empregado` | string | `"NA"` |
| `i090_36m_fala` | string | `"NA"` |
| `vd_d051_cafe_manha` | string | `"NA"` |
| `vd_basop_final` | string | `"0,3"` |
| `k173_alimento_cha` | string | `"Não"` |
| `u02a_coleta_motivo` | string | `"NA"` |
| `q03a_qual_outro` | null | `null` |
| `i077_24m_atencao` | string | `"NA"` |
| `vd_ien_escore` | string | `"-0,348026193972459"` |
| `vd_zbfa` | string | `"NA"` |
| `i042_12m_brinca` | string | `"NA"` |
| `m1002_p02` | string | `"NA"` |
| `i065_18m_sozinha` | string | `"Ainda não"` |
| `k28_aleitamento` | string | `"Mais ou menos"` |
| `vd_vb12_fonte` | string | `"Coleta"` |
| `j0501_rel_catolica` | string | `"Não"` |
| `i034_9m_brinca` | string | `"NA"` |
| `i058_15m_objetos` | string | `"NA"` |
| `r10_ar_condicionado` | string | `"Sim"` |
| `i098_36m_plural` | string | `"NA"` |
| `peso_setor_ajuste1` | string | `"119,152272610773"` |
| `t06_altura_medida2` | string | `"153,9"` |
| `vd_supl1_multivitaminico_com_minerais_bcferro` | string | `"Não"` |
| `h06_chupeta_comecou` | string | `"NA"` |
| `vd_supl1_somente_vita` | string | `"Sim"` |
| `q036_aposentadoria` | string | `"Não"` |
| `vd_supl1_com_vitd` | string | `"Sim"` |
| `t01_foi_pesada` | string | `"Sim"` |
| `s07_altura_medida1` | string | `"86"` |
| `m1017_p17` | string | `"NA"` |
| `h11_alergia` | string | `"Não"` |
| `vd_supl1_com_ferro` | string | `"Sim"` |
| `h216_internado_nao` | string | `"Não"` |
| `i048_12m_corre` | string | `"NA"` |
| `m11_quem_decide` | string | `"Pessoa 1"` |
| `peso_crianca_y_10` | string | `"1355,23329571831"` |
| `e05_cha` | string | `"Não"` |
| `k247_utilizou_copo` | string | `"Não"` |
| `m1015_p15` | string | `"NA"` |
| `t05_altura_medida1` | string | `"153,7"` |
| `r02_automoveis` | string | `"Nenhum automóvel"` |
| `p01_respondente` | string | `"Pessoa 1"` |
| `vd_prematura_igb` | string | `"Não"` |
| `u31a_observacoes` | null | `null` |
| `i011_4m_maos` | string | `"NA"` |
| `grupo9a` | string | `"Sim"` |
| `i017_4m_brinquedo` | string | `"NA"` |
| `peso_crianca_y_3` | string | `"1283,48488591922"` |
| `h12a_alergia_outro` | null | `null` |
| `i080_30m_cor` | string | `"NA"` |
| `grupo14` | string | `"Sim"` |
| `i000c_idade_em_meses` | string | `"22"` |
| `b06_numero_mae` | string | `"1"` |
| `k10_meses` | string | `"NA"` |
| `s01a_peso_motivo` | null | `null` |
| `k26_idade` | string | `"11"` |
| `h12_alergias` | null | `null` |
| `i9946_ceia` | string | `"NA"` |
| `e211a_pao_frances` | string | `"Não"` |
| `s10_altura_padrao` | string | `"Sim, foi feita seguindo o protocolo"` |
| `p04_aluguel` | string | `"NA"` |
| `grupo8` | string | `"Sim"` |
| `vd_pcr_final` | string | `"0,25"` |
| `grupo6` | string | `"Sim"` |
| `n03_verduras` | string | `"Nunca"` |
| `l02_morador_alim_acabaram` | string | `"Não"` |
| `t03b03_roupa_calca_de_brim` | string | `"NA"` |
| `m1016_p16` | string | `"NA"` |
| `r09_microcomputador` | string | `"Sim"` |
| `vd_supl1_com_ferro_indep_nutrisus` | string | `"Sim"` |
| `i102_48m_conta` | string | `"NA"` |
| `s04_peso_padrao` | string | `"Não, a criança estava com roupas leves (camiseta e short)"` |
| `vd_zhfa` | string | `"NA"` |
| `m07_sabe_basico` | string | `"Sim"` |
| `h03_altura` | string | `"49"` |
| `k21_recebeu` | string | `"Não"` |
| `e17_sal_vezes` | string | `"1"` |
| `b03_relacao` | string | `"Filho(a), enteado(a)"` |
| `peso_crianca_y_15` | string | `"1269,04677641023"` |
| `x06_total_pessoas` | string | `"4"` |
| `vd_d056_outra` | string | `"NA"` |
| `vd_supl1_somente_ferro` | string | `"Não"` |
| `vd_supl1_exclusivamente_ferro` | string | `"Não"` |
| `vd_supl1_somente_vitsad` | string | `"Não"` |
| `i073_24m_pula` | string | `"NA"` |
| `i097_36m_desenha` | string | `"NA"` |
| `e182_amassada` | string | `"Não"` |
| `u09a_refeicao_hora` | string | `"12"` |
| `grupo17` | string | `"Sim"` |
| `m1012_p12` | string | `"NA"` |
| `vd_supl1_multivitaminico_sem_minerais_abcd` | string | `"Não"` |
| `k22_amamentou` | string | `"Não"` |
| `t03_peso_medida2` | string | `"50,2"` |
| `i082_30m_nome` | string | `"NA"` |
| `h122_alergia_ovos` | string | `"NA"` |
| `u24a_refeicao_hora` | string | `"NA"` |
| `l06_adulto_comeu_menos` | string | `"Não"` |
| `i031_9m_sentada` | string | `"NA"` |
| `vd_linfop_final` | string | `"37,2"` |
| `r11_tv_a_cabo` | string | `"Não"` |
| `u06_tubos` | string | `"2"` |
| `peso_crianca_y_8` | string | `"1208,81226766186"` |
| `i040_12m_mao` | string | `"NA"` |
| `m1018_p18` | string | `"NA"` |
| `u02b_qual_outro_motivo` | null | `null` |
| `grupo20` | string | `"Sim"` |
| `h10b1_sindrome_nao` | string | `"Sim"` |
| `e28_figado` | string | `"Não"` |
| `s31a_pode_informar_altura` | string | `"NA"` |
| `h124_alergia_sementes` | string | `"NA"` |
| `h127_alergia_feijoes` | string | `"NA"` |
| `t03b02_roupa_bota` | string | `"NA"` |
| `i059_15m_corpo` | string | `"NA"` |
| `l04_morador_insuficiente` | string | `"Sim"` |
| `b06b_mae_responsavel` | string | `"01"` |
| `peso_crianca_y_6` | string | `"1205,02909554738"` |
| `vd_zwaz` | string | `"-0,2"` |
| `e181_pedacos` | string | `"Sim"` |
| `s39a_medida1_altura_refeita` | string | `"Não foi refeita ou não se aplica"` |
| `i115_59m_regras` | string | `"NA"` |
| `b00_numero` | string | `"02"` |
| `i014_4m_sons` | string | `"NA"` |
| `vd_bbb07_mae_resp1` | string | `"Mãe"` |
| `o03_frutas_variedade` | string | `"Discordo totalmente"` |
| `o07_refrigerantes_baratos` | string | `"Concordo parcialmente"` |
| `vd_idade_2cat` | string | `"1"` |
| `k174_alimento_agua` | string | `"Sim"` |
| `bbb08_numero_mais_novo1` | string | `"2"` |
| `g001_usou` | string | `"Não"` |
| `j05a_religiao_outra` | null | `null` |
| `k176_alimento_outro` | string | `"Não"` |
| `vd_hb_final` | string | `"10,8"` |
| `vd_d059_nao_sabe` | string | `"NA"` |
| `b05_data` | string | `"11092017"` |
| `i9947_outros` | string | `"NA"` |
| `k01_gestacoes` | string | `"2"` |
| `u22b_qual_outro_motivo` | null | `null` |
| `a00_regiao` | string | `"Norte"` |
| `m1021_p21` | string | `"NA"` |
| `vd_monop_final` | string | `"7,7"` |
| `h21_internado` | string | `"C"` |
| `m08_adiantar_etapas` | string | `"Não"` |
| `vd_d055_jantar` | string | `"NA"` |
| `peso_crianca_calib` | string | `"952,024118212783"` |
| `j0507_rel_budista` | string | `"Não"` |
| `i099_36m_ontem` | string | `"NA"` |
| `k17a_alimento_qual_outro` | null | `null` |
| `k171_alimento_leite` | string | `"Não"` |
| `k17_alimento` | null \| string | `"D"` |
| `t01a_peso_motivo` | null | `null` |
| `vd_ien_decimos` | string | `"2º"` |
| `k24_utilizou` | null \| string | `"H"` |
| `i074_24m_combina` | string | `"NA"` |
| `grupo22` | string | `"Sim"` |
| `h10b_sindrome_de_down` | string | `"A"` |
| `s06_foi_medida` | string | `"Sim"` |
| `i012_4m_ri` | string | `"NA"` |
| `i020_6m_sons` | string | `"NA"` |
| `vd_supl1_com_vitb9` | string | `"Não"` |
| `m1010_p10` | string | `"NA"` |
| `d02_matriculado` | string | `"Não, nunca frequentou"` |
| `peso_crianca_y_17` | string | `"1115,6228922382"` |
| `k12_tempo` | string | `"1"` |
| `t04_foi_medida` | string | `"Sim"` |
| `i091_36m_lava` | string | `"NA"` |
| `p03_ocupacao` | string | `"Cedido de outra forma"` |
| `r12_internet_domicilio` | string | `"Não"` |
| `s06a_altura_motivo` | null | `null` |
| `vd_ferri_final` | string | `"8,3"` |
| `vd_supl1_sobreposicao` | string | `"Sim"` |
| `p09_banheiros_chuveiro` | string | `"1"` |
| `e25_verduras` | string | `"Não"` |
| `vd_supl1_com_vitb8` | string | `"Não"` |
| `e33_refrigerante` | string | `"Sim"` |
| `vd_suplemento` | string | `"Sim"` |
| `k245_utilizou_mamadeira` | string | `"Não"` |
| `j05_religiao` | string | `"C"` |
| `i003_2m_vira` | string | `"NA"` |
| `d01_cor` | string | `"Branca"` |
| `bbb08a_numero_mais_velho1` | string | `"3"` |
| `h13_diarreia` | string | `"Não"` |
| `s23_peso_medida3` | string | `"NA"` |
| `peso_crianca_y_1a` | string | `"1192,20266393483"` |
| `i994_qual_refeicao` | null | `null` |
| `datahorapedido` | null \| string | `"22/07/2019 18:13"` |
| `s00d_idade_peso` | string | `"679"` |
| `m1003_p03` | string | `"NA"` |
| `vd_baso_final` | string | `"34"` |
| `h05_chupeta_usou` | string | `"Recusou o uso de chupeta"` |
| `i111_59m_desenha` | string | `"NA"` |
| `m09_atividades_divididas` | string | `"Não"` |
| `i9942_lanche_manha` | string | `"NA"` |
| `l07_adulto_sentiu_fome` | string | `"Não"` |
| `vd_selen_final` | string | `"60,5"` |
| `i057_15m_chuta` | string | `"NA"` |
| `vd_supl1_exclusivamente_vitc` | string | `"Não"` |
| `e213a_industrializado` | string | `"Não"` |
| `h10b4_sindrome_fenilcetonuria` | string | `"Não"` |
| `i085_30m_lava` | string | `"NA"` |
| `h219_internado_nao_sabe` | string | `"Não"` |
| `vd_zn_fonte` | string | `"Coleta"` |
| `vd_supl1_ferro_sus` | string | `"Não"` |
| `vd_supl1_multivitaminico_sem_minerais_ade` | string | `"Não"` |
| `i076_24m_cor` | string | `"NA"` |
| `h09_chupeta_medida2` | string | `"NA"` |
| `e40_adocado` | string | `"Sim"` |
| `i104_48m_plural` | string | `"NA"` |
| `vd_ien_quartos` | string | `"1º"` |
| `t03b04_roupa_casaco_jaqueta` | string | `"NA"` |
| `k05_prenatal_consultas` | string | `"8"` |
| `u04a_coleta_hora` | string | `"15"` |
| `e37_tempero` | string | `"Não"` |
| `m1009_p09` | string | `"NA"` |
| `p13_energia_eletrica` | string | `"Rede geral (companhia distribuidora)"` |
| `n07_biscoitos` | string | `"Sempre"` |
| `q04_quantos_moradores` | string | `"3"` |
| `s01_foi_pesada` | string | `"Sim"` |
| `vd_supl1_com_manganes` | string | `"Não"` |
| `i022_6m_barriga` | string | `"NA"` |
| `n02_legumes` | string | `"Nunca"` |
| `i006_2m_ri` | string | `"NA"` |
| `h17_nariz` | string | `"Não"` |
| `s05_peso_observacoes` | null | `null` |
| `i100_48m_compara` | string | `"NA"` |
| `grupo7` | string | `"Sim"` |
| `k25_mamadeira` | string | `"Sim, ainda usa"` |
| `e36_bala` | string | `"Sim"` |
| `vd_supl1_com_magnesio` | string | `"Não"` |
| `j08_ler` | string | `"Sim"` |
| `i114_59m_urinar` | string | `"NA"` |
| `i093_36m_explicar` | string | `"NA"` |
| `vd_selen_fonte` | string | `"Coleta"` |
| `i009_2m_olha` | string | `"NA"` |
| `l03_morador_saudavel` | string | `"Sim"` |
| `h123_alergia_peixes` | string | `"NA"` |
| `e09_leite_soja_liquido` | string | `"Não"` |
| `k09_licenca` | string | `"NA"` |
| `e16_comida_sal` | string | `"Sim"` |
| `u09b_refeicao_minuto` | string | `"40"` |
| `j0509_rel_outra_religiao` | string | `"Não"` |
| `k02_filhos_vivos` | string | `"2"` |
| `i078_24m_nome` | string | `"NA"` |
| `e18_oferecida` | string | `"A"` |
| `m04_confiante` | string | `"Sim, para todos esses alimentos"` |
| `n14_comer_comida` | string | `"NA"` |
| `h08_chupeta_parou` | string | `"NA"` |
| `k23_deixou` | string | `"Não"` |
| `d06a_qual_outra` | null | `null` |
| `n08_salgadinhos` | string | `"Sempre"` |
| `vd_d052_lanche_manha` | string | `"NA"` |
| `u30a_volume_trace` | string | `"NA"` |
| `k246_utilizou_sondinha` | string | `"Não"` |
| `grupo2` | string | `"Sim"` |
| `m1019_p19` | string | `"NA"` |
| `i092_36m_perguntas` | string | `"NA"` |
| `m06_facilidade` | string | `"Sim, para todos esses alimentos"` |
| `d06_relacao_responsavel` | string | `"NA"` |
| `j07a_nao_outra` | null | `null` |
| `peso_crianca_y_12` | string | `"1176,15209761954"` |
| `h18_ronqueira` | string | `"Não"` |
| `e19_mingau` | string | `"Não"` |
| `vd_ien_quintos` | string | `"1º"` |
| `vd_ebia_escore` | string | `"3"` |
| `o02_frutas_qualidade` | string | `"Discordo totalmente"` |
| `e219a_nao_sabe` | string | `"Não"` |
| `i015_4m_olha` | string | `"NA"` |
| `e35_biscoito` | string | `"Sim"` |
| `a11_situacao` | string | `"Urbano"` |
| `h10b2_sindrome_down` | string | `"Não"` |
| `i050_15m_mama` | string | `"NA"` |
| `i070_24m_corpo` | string | `"NA"` |
| `vd_supl1_com_molibdenio` | string | `"Não"` |
| `i072_24m_eu` | string | `"NA"` |
| `k241_utilizou_concha` | string | `"Não"` |
| `o04_frutas_baratas` | string | `"Discordo totalmente"` |
| `h214_internado_alergias` | string | `"Não"` |
| `i002_2m_segue` | string | `"NA"` |
| `i039_9m_pedidos` | string | `"NA"` |
| `t03c_qual_outra_roupa` | null | `null` |
| `u02_coleta_realizada` | string | `"Sim"` |
| `vd_vite_final` | string | `"6,4"` |
| `k03_prenatal` | string | `"Sim"` |
| `k29_alimentacao` | string | `"Não"` |
| `i019_4m_segura` | string | `"NA"` |
| `vd_rbc_final` | string | `"4,31"` |
| `vd_eos_final` | string | `"270"` |
| `i118_59m_colore` | string | `"NA"` |
| `vd_afoli_final` | string | `"11,28"` |
| `i084_30m_fala` | string | `"NA"` |
| `e184_liquidificada` | string | `"Não"` |
| `s29b_medida2_peso_refeita` | string | `"Não foi refeita ou não se aplica"` |
| `e185_caldo` | string | `"Não"` |
| `grupo11` | string | `"Sim"` |
| `i024_6m_procura` | string | `"NA"` |
| `t02_peso_medida1` | string | `"50,2"` |
| `u01_febre_diarreia` | string | `"Não"` |
| `k249_utilizou_nao_sabe` | string | `"Não"` |
| `h10_consulta` | string | `"Centro de Especialidades, Policlínica pública ou PAM – Post…` |
| `e13_fruta_vezes` | string | `"1"` |
| `i066_18m_eu` | string | `"Ainda não"` |
| `k15_recebeu` | string | `"Não"` |
| `m12_despesas` | string | `"Pessoa 1"` |
| `vd_rdw_final` | string | `"15,9"` |
| `s23a_peso_medida4` | string | `"NA"` |
| `e12_fruta_inteira` | string | `"Sim"` |
| `peso_crianca_y_2` | string | `"1229,43604768866"` |
| `id_anon` | string | `"10951000402"` |
| `e11_suco` | string | `"Não"` |
| `p12a_lixo_qual_outro` | null | `null` |
| `i001_2m_feliz` | string | `"NA"` |
| `n01_frutas` | string | `"Às vezes"` |
| `vd_supl1_vita_sus` | string | `"Sim"` |
| `vd_bast_final` | string | `"0"` |
| `a06_domicilio` | string | `"0004"` |
| `m1005_p05` | string | `"NA"` |
| `i067_18m_pula` | string | `"Ainda não"` |
| `e21a_pao` | string | `"D"` |
| `grupo15` | string | `"Sim"` |
| `i038_9m_anda` | string | `"NA"` |
| `i061_18m_escadas` | string | `"Um pouco"` |
| `i108_48m_copia` | string | `"NA"` |
| `k242_utilizou_protetor` | string | `"Não"` |
| `vd_ht_final` | string | `"31,5"` |
| `p10a_esgoto_outra` | null | `null` |
| `i112_59m_plural` | string | `"NA"` |
| `s07a_altura2_realizada` | string | `"Sim"` |
| `e14_manga` | string | `"Não"` |
| `u30_volume` | string | `"NA"` |
| `e22_legumes` | string | `"Não"` |
| `j0508_rel_sem_religiao` | string | `"Não"` |
| `e29_ovo` | string | `"Não"` |
| `vd_supl1_com_vitb12` | string | `"Não"` |
| `t06c_qual_outra` | null | `null` |
| `posestrato` | string | `"NorteMasculino3"` |
| `e31_salgadinhos` | string | `"Não"` |
| `d03_duracao` | string | `"NA"` |
| `vd_vit25_fonte` | string | `"Coleta"` |
| `h04_parto` | string | `"Cesariana de urgência (Não agendada)"` |
| `vd_vitb6_final` | string | `"36,5"` |
| `i046_12m_anda` | string | `"NA"` |
| `vd_mielo_final` | string | `"NA"` |
| `peso_crianca_y_1c` | string | `"1104,65027369481"` |

## `/atencao-primaria/pmmb-consolidado`

Programas de Provimento Federal - Programa Mais Médicos para o Brasil (PMMB) e Programa Médicos pelo Brasil (PMpB)

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/pmmb-consolidado?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pmmb": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nivel` | string | `"MUNICIPAL"` |
| `regiao` | string | `"CENTRO-OESTE"` |
| `uf` | string | `"DF"` |
| `cir` | string | `"DISTRITO FEDERAL"` |
| `co_ibge` | integer | `530010` |
| `municipio_dsei` | string | `"BRASILIA"` |
| `amazonia_legal` | null \| string | `"Fora da Amazonia Legal"` |
| `faixa_fronteira` | string | `"Fora da Faixa de Fronteira"` |
| `categoria_ivs` | string | `"4 - Baixa vulnerabilidade"` |
| `cobertura` | number | `492000.0` |
| `ativas_ff` | number | `142.0` |
| `ativas_coparticipacao` | number | `33.0` |
| `total_vagas_ativas` | number | `175.0` |
| `ampliacao_ecr` | number | `4.0` |
| `ampliacao_eapp` | number | `5.0` |
| `equipe_esf` | number | `166.0` |
| `equipe_emsi` | number | `0.0` |
| `total_ocupadas` | number | `173.0` |
| `em_processo_ocupacao` | number | `2.0` |
| `total_desocupadas` | number | `0.0` |
| `ativos_ppf` | null | `null` |
| `ativos_crm_pmm` | number | `120.0` |
| `ativos_intercambista_pmm` | number | `26.0` |
| `ativos_esf` | number | `164.0` |
| `ativos_emsi` | number | `0.0` |
| `ativos_eapp` | number | `5.0` |
| `ativos_ecr` | number | `4.0` |
| `ativos_fem` | number | `112.0` |
| `ativos_masc` | number | `61.0` |
| `ativos_sem_inf_sx` | number | `0.0` |
| `ativos_branca` | number | `88.0` |
| `ativos_preta_parda` | number | `29.0` |
| `ativos_indigena` | number | `1.0` |
| `ativos_amarela` | number | `51.0` |
| `ativos_sem_inf_rc` | number | `4.0` |
| `dt_geracao` | string | `"2026-09-11"` |
| `dt_referencia` | string | `"2026-09-11"` |
| `id_20_24` | number | `0.0` |
| `id_25_29` | number | `22.0` |
| `id_30_34` | number | `48.0` |
| `id_35_39` | number | `38.0` |
| `id_40_44` | number | `21.0` |
| `id_45_49` | number | `17.0` |
| `id_50_54` | number | `8.0` |
| `id_55_59` | number | `12.0` |
| `id_60_64` | number | `3.0` |
| `id_65_69` | number | `2.0` |
| `id_70_74` | number | `0.0` |
| `id_75_79` | number | `0.0` |
| `id_80_mais` | number | `0.0` |
| `nac_boliviano` | number | `0.0` |
| `nac_brasileiro` | number | `0.0` |
| `nac_outros` | number | `173.0` |
| `ativos_celetista_mfc` | number | `18.0` |
| `ativos_vinculados` | null | `null` |
| `nac_cubano` | number | `0.0` |
| `nac_venezuelano` | number | `0.0` |
| `ativos_tutores` | number | `7.0` |

## `/educacao-em-saude/pvc`

Programa De Volta Para Casa (PVC)

- URL: `https://apidadosabertos.saude.gov.br/educacao-em-saude/pvc?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pvc": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `co_uf` | integer | `27` |
| `nu_ano` | integer | `2026` |
| `nu_mes` | integer | `1` |
| `nu_beneficiario` | integer | `14` |
| `vl_total` | number | `10570.0` |

## `/atencao-primaria/pmmb-serie-historica`

Série histórica de profissionais vinculados ao PMMB

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/pmmb-serie-historica?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pmmb_serie_historica": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `regiao` | string | `"NORTE"` |
| `uf` | string | `"AP"` |
| `municipio_dsei` | string | `"AMAPA E NORTE DO PARA"` |
| `ibge` | number | `2.0` |
| `prof_crm_brasil_pmmb` | number | `0.0` |
| `prof_inter_pmmb` | number | `0.0` |
| `prof_cooperados_pmmb` | number | `3.0` |
| `prof_provab` | number | `0.0` |
| `total_prof_ativos` | number | `3.0` |
| `dt_referencia` | string | `"29/11/2013"` |
| `prof_bolsista_vinculados` | number | `0.0` |
| `prof_celetista_vinculados` | number | `0.0` |
| `prof_tutor_vinculados` | number | `0.0` |

## `/atencao-primaria/pmmb-relacao-nominal-coparticipacao`

Lista de profissionais ativos no PMMB com dados de coparticipação nominal

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/pmmb-relacao-nominal-coparticipacao?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pmmb_relacao_nominal_coparticipacao": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `co_ibge` | integer | `110002` |
| `no_municipio` | string | `"ARIQUEMES"` |
| `profissional` | string | `"FREKCIONE NUNES SILVA"` |
| `inicio_atividades` | string | `"2026-05-19"` |
| `dt_referencia` | string | `"2026-07-31"` |
| `dt_atualizacao` | string | `"2026-08-15"` |

## `/atencao-primaria/pmmb-relatorio-historico-cadastro-cnes`

Lista de profissionais do PMMB por estabelecimento CNES

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/pmmb-relatorio-historico-cadastro-cnes?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pmmb_relatorio_historico_cadastro_cnes": "array[0]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `pmmb_relatorio_historico_cadastro_cnes` | array | `[]` |

## `/atencao-primaria/pmmb-especialista-consolidado`

Dados consolidados de especialistas do PMMB por estabelecimento

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/pmmb-especialista-consolidado?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pmmb_especialista_consolidado": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `cnes` | integer | `485` |
| `estabelecimento` | string | `"FUNDACAO ALTINO VENTURA"` |
| `tipo_pratica` | null \| string | `"CIRURGICA"` |
| `curso` | string | `"01. ANESTESIOLOGIA PERIOPERATÓRIA E SEDAÇÃO SEGURA"` |
| `faixa_atracao` | string | `"FAIXA 2"` |
| `co_ibge` | integer | `261160` |
| `tipo_municipio` | string | `"CAPITAL"` |
| `nivel_vaga` | string | `"DUPLA"` |
| `categoria_ivs` | string | `"3 - MEDIA VULNERABILIDADE"` |
| `amazonia_legal` | string | `"FORA DA AMAZONIA LEGAL"` |
| `regiao_saude` | string | `"RECIFE"` |
| `qtd_ativos` | integer | `3` |
| `qtd_feminino` | integer | `2` |
| `qtd_masculino` | integer | `1` |
| `qtd_sexo_n_informado` | integer | `0` |
| `qtd_ciclo_1` | integer | `0` |
| `qtd_ciclo_2` | integer | `0` |
| `qtd_ciclo_3` | integer | `3` |

## `/atencao-primaria/pmmb-especialista-serie-historica`

Programa Mais Médicos - Especialistas Série Histórica

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/pmmb-especialista-serie-historica?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pmmb_especialista_serie_historica": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `co_cnes` | null | `null` |
| `tipo_estabelecimento` | null | `null` |
| `curso` | string | `"03. Cirurgia Oncológica Avançada"` |
| `faixa_atracao` | string | `"FAIXA 2"` |
| `co_ibge` | integer | `120040` |
| `competencia` | string | `"dez/25"` |
| `estabelecimento` | null | `null` |
| `municipio` | string | `"RIO BRANCO"` |
| `uf` | string | `"AC"` |
| `regiao` | string | `"NORTE"` |
| `regiao_saude` | string | `"BAIXO ACRE E PURUS"` |
| `qtd_ativos` | integer | `1` |
| `qtd_feminino` | integer | `0` |
| `qtd_masculino` | integer | `1` |
| `qtd_sexo_nao_informado` | integer | `0` |
| `ivs` | string | `"3 - Média vulnerabilidade"` |

## `/atencao-primaria/pmmb-relacao-nominal-ativo`

Profissionais ativos no Programa Mais Médicos para o Brasil (PMMB)

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/pmmb-relacao-nominal-ativo?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pmmb_profissionais_ativos": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `crm` | string | `"0056650"` |
| `perfil` | string | `"CRM BRASIL"` |
| `ciclo` | string | `"36"` |
| `uf` | string | `"MG"` |
| `co_ibge` | integer | `314330` |
| `municipio_dsei` | string | `"MONTES CLAROS"` |
| `dt_atualizacao` | string | `"2026-09-11"` |
| `inicio_atividade` | string | `"2024-01-01"` |
| `eixo_integracao` | string | `"FORMACAO"` |
| `tipo_equipe` | string | `"70 - eSF"` |
| `nivel` | null \| string | `"DSEI"` |
| `raca_cor` | string | `"BRANCA"` |
| `sexo` | string | `"FEMININO"` |
| `nacionalidade` | string | `"BRASILEIRA"` |
| `faixa_etaria` | string | `"45 a 49 anos"` |
| `programa_vaga` | string | `"PMM"` |
| `no_profissional` | string | `"MONICA MENDES VIEIRA"` |

## `/vacinacao/esavi`

Evento supostamente atribuível à vacinação ou imunização (ESAVI) é qualquer ocorrência médica indesejada após a vacinação, não possuindo necessariamente uma relação causal com o uso de uma vacina ou outro imunobiológico (imunoglobulinas e soros heterólogos).

- URL: `https://apidadosabertos.saude.gov.br/vacinacao/esavi?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"esavi": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `descricao_tipo_encerramento` | null \| string | `"#1: MUNICIPAL"` |
| `descricao_estrangeiro` | null \| string | `"Não"` |
| `descricao_evolucao_caso` | null \| string | `"Cura sem sequelas"` |
| `data_inicio_ea` | string | `"#1: 12/04/2021 \| #2: 12/04/2021"` |
| `hora_duracao_ea` | string | `"#1: 0 \| #2: 0"` |
| `descricao_imuno` | string | `"#1:Covid-19-Covishield-Oxford/Fiocruz"` |
| `descricao_relacao_imuno` | string | `"#1:Suspeito"` |
| `nome_estado_estab_atendimento` | null \| string | `"#1: Minas Gerais"` |
| `descricao_tipo_ea` | string | `"#1: Evento Adverso \| #2: Evento Adverso"` |
| `descricao_gestante` | null \| string | `"Não"` |
| `st_comunidade_tradicional` | null \| string | `"POVOS INDIGENAS"` |
| `nome_estado` | string | `"Paraná"` |
| `descricao_diagnostico` | null \| string | `"#1: Y598 - Efeitos adversos de outras vacinas e substâncias…` |
| `numero_idade` | string | `"66"` |
| `descricao_mulher_amamentando` | null \| string | `"Não"` |
| `descricao_evento_adverso` | string | `"#1: Calafrios, Artralgia"` |
| `descricao_encerramento_grave` | null \| string | `"#1: Não"` |
| `descricao_class_gravidade_ea` | string | `"#1: Não grave \| #2: Não grave"` |
| `descricao_minuto_reacao_intervalo_admin_ea` | string | `"#1: 0 \| #2: 0"` |
| `descricao_not_mae_filho` | string | `"Não"` |
| `descricao_hora_inicio_ea` | string | `"-"` |
| `descricao_hora_terminome_ea` | string | `"-"` |
| `hora_aplica_imuno` | string | `"#1:10:22"` |
| `numero_notificacao` | string | `"00000831efeb56369c6c54b6b566d122bc1be2415bdbc7c1ce138419dcd…` |
| `descricao_lote_imuno` | string | `"#1:CTMAV520"` |
| `nome_mun_estab_atendimento` | null \| string | `"#1: Senador Firmino"` |
| `descricao_dose_imuno` | string | `"#1:D1 - 1ª Dose"` |
| `descricao_medicamento_uso` | null \| string | `"Não"` |
| `data_recebimento_notificacao` | null \| string | `"23/08/2021"` |
| `descricao_atendimento_medico` | null \| string | `"Não"` |
| `numero_mes_gestacao_mae` | null \| string | `"1"` |
| `descricao_sexo` | string | `"Feminino"` |
| `numero_mes_gestante` | null \| string | `"1"` |
| `data_investigacao` | null \| string | `"25/08/2021"` |
| `descricao_dia_duracao_ea` | string | `"-"` |
| `data_terminome_ea` | string | `"-"` |
| `descricao_mae_amamentando` | null \| string | `"Não"` |
| `descricao_profissional_saude` | string | `"Não"` |
| `descricao_doencas_pre_existentes` | null \| string | `"#1: D699 - Afecção hemorrágica não especificada"` |
| `descricao_casualidade` | string | `"#1: A.1- Reações inerentes ao produto, conforme literatura"` |
| `data_alta_atendimento` | null \| string | `"-"` |
| `nome_mun_notificacao` | string | `"Curitiba"` |
| `descricao_relacao_medicamento` | null \| string | `"#1: Suspeito"` |
| `descricao_dia_reacao_intervalo_admin_ea` | string | `"-"` |
| `codigo_imuno` | string | `"#1:85"` |
| `data_notificacao` | string | `"13/04/2021"` |
| `descricao_medicamento` | null \| string | `"#1: AMITRIPTILINA 25MG"` |
| `descricao_raca_cor_mae` | null \| string | `"Branca"` |
| `data_desfecho` | null \| string | `"09/05/2021"` |
| `descricao_situacao_notificacao` | string | `"Encerrado"` |
| `descricao_raca_cor` | string | `"Branca"` |
| `descricao_hora_reacao_intervalo_admin_ea` | string | `"#1: 0 \| #2: 0"` |
| `descricao_via_admin_imuno` | string | `"#1:IM - Intramuscular"` |
| `descricao_reacao_ea` | string | `"#1: Calafrios \| #2: Artralgia"` |
| `descricao_crianca_aleitamento` | null \| string | `"Não"` |
| `descricao_profissional_seguranca` | string | `"Não"` |
| `nome_mun_mae` | null \| string | `"São Martinho"` |
| `descricao_minuto_duracao_ea` | string | `"-"` |
| `descricao_nome_fabricante` | string | `"#1:fiocruz"` |
| `descricao_mae_gestante` | null \| string | `"Não"` |
| `data_admissao_atendimento` | null \| string | `"#1: 14/05/2021"` |
| `data_encerramento` | null \| string | `"#1: 09/05/2021"` |
| `descricao_estrategia_imuno` | string | `"#1:Campanha seletiva"` |
| `nome_estado_notificacao` | string | `"Paraná"` |
| `descricao_local_aplica_imuno` | string | `"#1:DD - Deltóide Direito"` |
| `data_aplicacao_imuno` | string | `"#1:12/04/2021"` |
| `codigo_reacao_ea` | string | `"#1: 10040559 \| #2: 10003239"` |
| `descricao_versao_medra` | null \| string | `"Versão não definida"` |
| `nome_municipio` | string | `"Curitiba"` |
| `nome_estado_mae` | null \| string | `"Santa Catarina"` |
| `descricao_tipo_atendimento` | null \| string | `"#1: Ambulatório/consultório"` |
| `descricao_gravidade_ea` | string | `"-"` |
| `descricao_conduta` | string | `"#1: Esquema Mantido"` |

## `/vacinacao/sistema-de-informacao-de-insumos-estrategicos`

Monitoramento dos dados de doses distribuídas

- URL: `https://apidadosabertos.saude.gov.br/vacinacao/sistema-de-informacao-de-insumos-estrategicos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sies": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `tx_area` | string | `"IMUNOBIOLOGICO"` |
| `qtde` | string | `"40000"` |
| `mes` | string | `"12"` |
| `ibge` | string | `"410690"` |
| `origem` | string | `"Distribuido"` |
| `tx_sigla` | string | `"SES-PR"` |
| `ano` | string | `"2021"` |
| `tx_insumo` | string | `"VACINA ORAL CONTRA POLIOMIELITE"` |

## `/arboviroses/febre-amarela-humanos-primatas-nao-humanos`

Notificações de casos suspeitos da doença de febre amarela em humanos e em primatas não-humanos

- URL: `https://apidadosabertos.saude.gov.br/arboviroses/febre-amarela-humanos-primatas-nao-humanos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"febre_amarela_humanos_primatas": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `mun_lpi` | string | `"ALTO ALEGRE"` |
| `mes_is` | integer \| null | `11` |
| `sexo` | string | `"M"` |
| `dt_is` | null \| string | `"29/11/1994"` |
| `cod_mun_lpi` | integer | `140005` |
| `idade` | integer \| null | `19` |
| `dt_obito` | null \| string | `"01/12/1994"` |
| `macrorreg_lpi` | string | `"N"` |
| `ano_is` | integer | `1994` |
| `se_is` | integer \| null | `48` |
| `monitoramento_is` | string | `"1994/1995"` |
| `uf_lpi` | string | `"RR"` |
| `obito` | string | `"SIM"` |
| `cod_uf_lpi` | integer | `14` |

## `/arboviroses/febre-amarela-epzootias`

Ocorrências de epzootias de febre amarela por local e período

- URL: `https://apidadosabertos.saude.gov.br/arboviroses/febre-amarela-epzootias?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"febre_amarela_epzootias": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `macrorreg_ocor` | string | `"CO"` |
| `cod_uf_ocor` | integer | `52` |
| `uf_ocor` | string | `"GO"` |
| `cod_mun_ocor` | integer | `521100` |
| `mun_ocor` | string | `"ITAPIRAPUÃ"` |
| `data_ocor` | null \| string | `"14/11/2002"` |
| `se_ocor` | integer \| null | `46` |
| `mes_ocor` | integer \| null | `2` |
| `ano_ocor` | integer | `2000` |
| `monitoramento_ocor` | string | `"1999/2000"` |

## `/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2020`

Base de dados de SG de casos leves e moderados suspeitos de covid-19, a partir da incorporação do sistema e-SUS Notifica.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2020?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"notificacoes_sindrome_gripal_leve": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `excluido` | string | `"false"` |
| `codigo_estado_teste_4` | null | `null` |
| `outro_busca_ativa_assintomatico` | null | `null` |
| `evolucao_caso` | null \| string | `"Cancelado"` |
| `lote_segunda_dose` | null | `null` |
| `codigo_busca_ativa_assintomatico` | null | `null` |
| `codigo_tipo_teste_3` | null | `null` |
| `estado_notificacao` | string | `"Acre"` |
| `codigo_laboratorio_segunda_dose` | null | `null` |
| `lote_primeira_dose` | null | `null` |
| `raca_cor` | null \| string | `"Parda"` |
| `codigo_doses_vacina` | null | `null` |
| `data_notificacao` | string | `"2020-08-26"` |
| `condicoes` | null \| string | `"Doenças respiratórias crônicas descompensadas"` |
| `data_segunda_dose` | null | `null` |
| `profissional_saude` | string | `"Não"` |
| `outro_triagem_populacao_especifica` | null | `null` |
| `idade` | null \| string | `"33"` |
| `classificacao_final` | null \| string | `"Descartado"` |
| `codigo_fabricante_teste_4` | null | `null` |
| `codigo_local_realizacao_testagem` | null | `null` |
| `data_encerramento` | null \| string | `"2020-07-24"` |
| `sexo` | string | `"Feminino"` |
| `codigo_recebeu_vacina` | null | `null` |
| `sintomas` | string | `"Outros"` |
| `total_testes_realizados` | string | `"1"` |
| `codigo_estado_teste_1` | null \| string | `"3"` |
| `outros_sintomas` | null \| string | `"SEM SINTOMAS"` |
| `codigofabricanteteste1` | null | `null` |
| `codigo_tipo_teste_2` | null \| string | `"8"` |
| `data_coleta_teste_1` | null \| string | `"2020-08-25"` |
| `data_coleta_teste_2` | null \| string | `"2020-11-16"` |
| `codigo_fabricante_teste_2` | null | `null` |
| `profissional_seguranca` | null \| string | `"Não"` |
| `cbo` | null \| string | `"5153 - Auxiliar da área social"` |
| `validado` | string | `"false"` |
| `municipio` | string | `"Tarauacá"` |
| `codigo_resultado_teste_3` | null | `null` |
| `estado` | string | `"Acre"` |
| `data_coleta_teste_3` | null | `null` |
| `estado_notificacao_ibge` | null | `null` |
| `municipio_ibge` | null | `null` |
| `codigo_resultado_teste_1` | null \| string | `"2"` |
| `codigo_resultado_teste_2` | null \| string | `"2"` |
| `outras_condicoes` | null | `null` |
| `data_primeira_dose` | null | `null` |
| `outro_local_realizacao_testagem` | null | `null` |
| `codigo_laboratorio_primeira_dose` | null | `null` |
| `codigo_estado_teste_2` | null \| string | `"1"` |
| `codigo_contem_comunidade_tradicional` | null | `null` |
| `codigo_fabricante_teste_3` | null | `null` |
| `codigo_tipo_teste_1` | null \| string | `"5"` |
| `municipio_notificacao` | string | `"Rio Branco"` |
| `codigo_resultado_teste_4` | null | `null` |
| `codigo_estado_teste_3` | null | `null` |
| `data_coleta_teste_4` | null | `null` |
| `estado_ibge` | null | `null` |
| `origem` | string | `"parse-cloud"` |
| `data_inicio_sintomas` | string | `"2020-08-17"` |
| `codigo_tipo_teste_4` | null | `null` |
| `municipio_notificacao_ibge` | null | `null` |
| `codigo_estrategia_covid` | null | `null` |
| `codigo_triagem_populacao_especifica` | null | `null` |

## `/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2021`

Base de dados de SG de casos leves e moderados suspeitos de covid-19, a partir da incorporação do sistema e-SUS Notifica.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2021?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"notificacoes_sindrome_gripal_leve": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `excluido` | string | `"false"` |
| `codigo_estado_teste_4` | null | `null` |
| `outro_busca_ativa_assintomatico` | null | `null` |
| `evolucao_caso` | null \| string | `"Cura"` |
| `lote_segunda_dose` | null \| string | `"212VCD001ZVB"` |
| `codigo_busca_ativa_assintomatico` | null | `null` |
| `codigo_tipo_teste_3` | null | `null` |
| `estado_notificacao` | string | `"Acre"` |
| `codigo_laboratorio_segunda_dose` | null \| string | `"ASTRAZENECA/FIOCRUZ"` |
| `lote_primeira_dose` | null \| string | `"4120Z025"` |
| `raca_cor` | null \| string | `"Parda"` |
| `codigo_doses_vacina` | null \| string | `"2,1"` |
| `data_notificacao` | string | `"2020-08-25"` |
| `condicoes` | null \| string | `"Doenças cardíacas crônicas, Diabetes"` |
| `data_segunda_dose` | null \| string | `"2021-06-07"` |
| `profissional_saude` | string | `"Não"` |
| `outro_triagem_populacao_especifica` | null | `null` |
| `idade` | null \| string | `"35"` |
| `classificacao_final` | null \| string | `"Confirmado Laboratorial"` |
| `codigo_fabricante_teste_4` | null | `null` |
| `codigo_local_realizacao_testagem` | null \| string | `"1"` |
| `data_encerramento` | null \| string | `"2021-09-20"` |
| `sexo` | string | `"Masculino"` |
| `codigo_recebeu_vacina` | null \| string | `"3"` |
| `sintomas` | string | `"Outros, Tosse"` |
| `total_testes_realizados` | string | `"1"` |
| `codigo_estado_teste_1` | null \| string | `"3"` |
| `outros_sintomas` | null \| string | `"DOR NO CORPO, DOR NA NUCA, CORIZA"` |
| `codigofabricanteteste1` | null | `null` |
| `codigo_tipo_teste_2` | null \| string | `"7"` |
| `data_coleta_teste_1` | null \| string | `"2020-08-25"` |
| `data_coleta_teste_2` | null \| string | `"2021-01-29"` |
| `codigo_fabricante_teste_2` | null | `null` |
| `profissional_seguranca` | null \| string | `"Não"` |
| `cbo` | null \| string | `"2321 - Professores do ensino médio"` |
| `validado` | string | `"false"` |
| `municipio` | string | `"Sena Madureira"` |
| `codigo_resultado_teste_3` | null | `null` |
| `estado` | string | `"Acre"` |
| `data_coleta_teste_3` | null | `null` |
| `estado_notificacao_ibge` | null \| string | `"AC"` |
| `municipio_ibge` | null \| string | `"1200708"` |
| `codigo_resultado_teste_1` | null \| string | `"1"` |
| `codigo_resultado_teste_2` | null \| string | `"2"` |
| `outras_condicoes` | null | `null` |
| `data_primeira_dose` | null \| string | `"2021-03-12"` |
| `outro_local_realizacao_testagem` | null | `null` |
| `codigo_laboratorio_primeira_dose` | null \| string | `"ASTRAZENECA/FIOCRUZ"` |
| `codigo_estado_teste_2` | null \| string | `"3"` |
| `codigo_contem_comunidade_tradicional` | null \| string | `"2"` |
| `codigo_fabricante_teste_3` | null | `null` |
| `codigo_tipo_teste_1` | null \| string | `"1"` |
| `municipio_notificacao` | string | `"Bujari"` |
| `codigo_resultado_teste_4` | null | `null` |
| `codigo_estado_teste_3` | null | `null` |
| `data_coleta_teste_4` | null | `null` |
| `estado_ibge` | null \| string | `"AC"` |
| `origem` | string | `"parse-cloud"` |
| `data_inicio_sintomas` | string | `"2020-08-21"` |
| `codigo_tipo_teste_4` | null | `null` |
| `municipio_notificacao_ibge` | null \| string | `"1200302"` |
| `codigo_estrategia_covid` | null \| string | `"1"` |
| `codigo_triagem_populacao_especifica` | null | `null` |

## `/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2022`

Base de dados de SG de casos leves e moderados suspeitos de covid-19, a partir da incorporação do sistema e-SUS Notifica.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2022?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"notificacoes_sindrome_gripal_leve": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `excluido` | string | `"false"` |
| `codigo_estado_teste_4` | null | `null` |
| `outro_busca_ativa_assintomatico` | null | `null` |
| `evolucao_caso` | null \| string | `"Cura"` |
| `lote_segunda_dose` | null \| string | `"28230BD"` |
| `codigo_busca_ativa_assintomatico` | null | `null` |
| `codigo_tipo_teste_3` | null | `null` |
| `estado_notificacao` | string | `"Acre"` |
| `codigo_laboratorio_segunda_dose` | null \| string | `"PFIZER"` |
| `lote_primeira_dose` | null \| string | `"EY0586"` |
| `raca_cor` | string | `"Parda"` |
| `codigo_doses_vacina` | null \| string | `"1,2"` |
| `data_notificacao` | string | `"2022-01-26"` |
| `condicoes` | null \| string | `"Diabetes"` |
| `data_segunda_dose` | null \| string | `"2021-09-09"` |
| `profissional_saude` | string | `"Não"` |
| `outro_triagem_populacao_especifica` | null | `null` |
| `idade` | null \| string | `"30"` |
| `classificacao_final` | null \| string | `"Confirmado Laboratorial"` |
| `codigo_fabricante_teste_4` | null | `null` |
| `codigo_local_realizacao_testagem` | null \| string | `"1"` |
| `data_encerramento` | null \| string | `"2022-02-10"` |
| `sexo` | string | `"Feminino"` |
| `codigo_recebeu_vacina` | null \| string | `"1"` |
| `sintomas` | string | `"Assintomático"` |
| `total_testes_realizados` | string | `"1"` |
| `codigo_estado_teste_1` | null \| string | `"3"` |
| `outros_sintomas` | null \| string | `"DOR TORACICA + DORSALGIA + VOMITO"` |
| `codigofabricanteteste1` | null \| string | `"915"` |
| `codigo_tipo_teste_2` | null \| string | `"3"` |
| `data_coleta_teste_1` | null \| string | `"2022-01-24"` |
| `data_coleta_teste_2` | null \| string | `"2021-12-16"` |
| `codigo_fabricante_teste_2` | null \| string | `"915"` |
| `profissional_seguranca` | string | `"Não"` |
| `cbo` | null \| string | `"5199 - Outros trabalhadores dos serviços"` |
| `validado` | string | `"false"` |
| `municipio` | string | `"Rio Branco"` |
| `codigo_resultado_teste_3` | null | `null` |
| `estado` | string | `"Acre"` |
| `data_coleta_teste_3` | null | `null` |
| `estado_notificacao_ibge` | null \| string | `"AC"` |
| `municipio_ibge` | null \| string | `"1200401"` |
| `codigo_resultado_teste_1` | null \| string | `"1"` |
| `codigo_resultado_teste_2` | null \| string | `"2"` |
| `outras_condicoes` | null \| string | `"HIPERTENSAO"` |
| `data_primeira_dose` | null \| string | `"2021-07-08"` |
| `outro_local_realizacao_testagem` | null | `null` |
| `codigo_laboratorio_primeira_dose` | null \| string | `"PFIZER"` |
| `codigo_estado_teste_2` | null \| string | `"3"` |
| `codigo_contem_comunidade_tradicional` | null \| string | `"2"` |
| `codigo_fabricante_teste_3` | null | `null` |
| `codigo_tipo_teste_1` | null \| string | `"3"` |
| `municipio_notificacao` | string | `"Rio Branco"` |
| `codigo_resultado_teste_4` | null | `null` |
| `codigo_estado_teste_3` | null | `null` |
| `data_coleta_teste_4` | null | `null` |
| `estado_ibge` | null \| string | `"AC"` |
| `origem` | string | `"parse-cloud"` |
| `data_inicio_sintomas` | null \| string | `"2020-11-12"` |
| `codigo_tipo_teste_4` | null | `null` |
| `municipio_notificacao_ibge` | null \| string | `"1200401"` |
| `codigo_estrategia_covid` | null \| string | `"1"` |
| `codigo_triagem_populacao_especifica` | null \| string | `"4"` |

## `/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2023`

Base de dados de SG de casos leves e moderados suspeitos de covid-19, a partir da incorporação do sistema e-SUS Notifica.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2023?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"notificacoes_sindrome_gripal_leve": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `excluido` | string | `"false"` |
| `codigo_estado_teste_4` | null | `null` |
| `outro_busca_ativa_assintomatico` | null \| string | `"PROTOCOLO DE INTERNACAO"` |
| `evolucao_caso` | null \| string | `"Cura"` |
| `lote_segunda_dose` | null \| string | `"FM3809"` |
| `codigo_busca_ativa_assintomatico` | null \| string | `"4"` |
| `codigo_tipo_teste_3` | null | `null` |
| `estado_notificacao` | string | `"Acre"` |
| `codigo_laboratorio_segunda_dose` | null \| string | `"PFIZER"` |
| `lote_primeira_dose` | null \| string | `"FA9096"` |
| `raca_cor` | string | `"Parda"` |
| `codigo_doses_vacina` | null \| string | `"1,2"` |
| `data_notificacao` | string | `"2022-11-01"` |
| `condicoes` | null \| string | `"Doenças respiratórias crônicas descompensadas"` |
| `data_segunda_dose` | null \| string | `"2021-12-22"` |
| `profissional_saude` | string | `"Não"` |
| `outro_triagem_populacao_especifica` | null | `null` |
| `idade` | null \| string | `"20"` |
| `classificacao_final` | null \| string | `"Confirmado Laboratorial"` |
| `codigo_fabricante_teste_4` | null | `null` |
| `codigo_local_realizacao_testagem` | string | `"1"` |
| `data_encerramento` | null \| string | `"2022-11-30"` |
| `sexo` | string | `"Feminino"` |
| `codigo_recebeu_vacina` | null \| string | `"1"` |
| `sintomas` | string | `"Coriza, Dor de Cabeça, Dor de Garganta, Outros"` |
| `total_testes_realizados` | string | `"1"` |
| `codigo_estado_teste_1` | null \| string | `"3"` |
| `outros_sintomas` | null \| string | `"DOR NO CORPO"` |
| `codigofabricanteteste1` | null \| string | `"915"` |
| `codigo_tipo_teste_2` | null \| string | `"3"` |
| `data_coleta_teste_1` | null \| string | `"2022-11-01"` |
| `data_coleta_teste_2` | null | `null` |
| `codigo_fabricante_teste_2` | null | `null` |
| `profissional_seguranca` | string | `"Não"` |
| `cbo` | null \| string | `"5199 - Outros trabalhadores dos serviços"` |
| `validado` | string | `"false"` |
| `municipio` | string | `"Rio Branco"` |
| `codigo_resultado_teste_3` | null | `null` |
| `estado` | string | `"Acre"` |
| `data_coleta_teste_3` | null | `null` |
| `estado_notificacao_ibge` | string | `"AC"` |
| `municipio_ibge` | string | `"1200401"` |
| `codigo_resultado_teste_1` | null \| string | `"1"` |
| `codigo_resultado_teste_2` | null | `null` |
| `outras_condicoes` | null \| string | `"hipertensão"` |
| `data_primeira_dose` | null \| string | `"2021-07-26"` |
| `outro_local_realizacao_testagem` | null | `null` |
| `codigo_laboratorio_primeira_dose` | null \| string | `"PFIZER"` |
| `codigo_estado_teste_2` | null \| string | `"1"` |
| `codigo_contem_comunidade_tradicional` | string | `"2"` |
| `codigo_fabricante_teste_3` | null | `null` |
| `codigo_tipo_teste_1` | null \| string | `"3"` |
| `municipio_notificacao` | string | `"Rio Branco"` |
| `codigo_resultado_teste_4` | null | `null` |
| `codigo_estado_teste_3` | null | `null` |
| `data_coleta_teste_4` | null | `null` |
| `estado_ibge` | string | `"AC"` |
| `origem` | string | `"parse-cloud"` |
| `data_inicio_sintomas` | null \| string | `"2022-10-27"` |
| `codigo_tipo_teste_4` | null | `null` |
| `municipio_notificacao_ibge` | string | `"1200401"` |
| `codigo_estrategia_covid` | string | `"1"` |
| `codigo_triagem_populacao_especifica` | null | `null` |

## `/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2024`

Base de dados de SG de casos leves e moderados suspeitos de covid-19, a partir da incorporação do sistema e-SUS Notifica.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/notificacoes-de-sindrome-gripal-leve-2024?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"notificacoes_sindrome_gripal_leve": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `excluido` | string | `"false"` |
| `codigo_estado_teste_4` | null | `null` |
| `outro_busca_ativa_assintomatico` | null \| string | `"PROTOCOLO DE INTERNAÇÃO"` |
| `evolucao_caso` | null \| string | `"Cura"` |
| `lote_segunda_dose` | null \| string | `"210213"` |
| `codigo_busca_ativa_assintomatico` | null \| string | `"4"` |
| `codigo_tipo_teste_3` | null \| string | `"3"` |
| `estado_notificacao` | string | `"Acre"` |
| `codigo_laboratorio_segunda_dose` | null \| string | `"SINOVAC/BUTANTAN"` |
| `lote_primeira_dose` | null \| string | `"FD7209"` |
| `raca_cor` | string | `"Parda"` |
| `codigo_doses_vacina` | null \| string | `"1"` |
| `data_notificacao` | string | `"2022-01-10"` |
| `condicoes` | null \| string | `"Outros"` |
| `data_segunda_dose` | null \| string | `"2021-08-06"` |
| `profissional_saude` | string | `"Não"` |
| `outro_triagem_populacao_especifica` | null | `null` |
| `idade` | null \| string | `"40"` |
| `classificacao_final` | null \| string | `"Confirmado Laboratorial"` |
| `codigo_fabricante_teste_4` | null | `null` |
| `codigo_local_realizacao_testagem` | string | `"1"` |
| `data_encerramento` | null \| string | `"2024-04-25"` |
| `sexo` | string | `"Feminino"` |
| `codigo_recebeu_vacina` | null \| string | `"1"` |
| `sintomas` | string | `"Dor de Cabeça, Tosse, Febre, Dispneia, Dor de Garganta, Out…` |
| `total_testes_realizados` | string | `"1"` |
| `codigo_estado_teste_1` | null \| string | `"3"` |
| `outros_sintomas` | null \| string | `"DOR TORACICA"` |
| `codigofabricanteteste1` | null \| string | `"915"` |
| `codigo_tipo_teste_2` | null \| string | `"5"` |
| `data_coleta_teste_1` | null \| string | `"2021-01-10"` |
| `data_coleta_teste_2` | null \| string | `"2022-01-20"` |
| `codigo_fabricante_teste_2` | null \| string | `"915"` |
| `profissional_seguranca` | string | `"Não"` |
| `cbo` | null \| string | `"5151 - Trabalhadores em serviços de promoção e apoio à saúd…` |
| `validado` | string | `"false"` |
| `municipio` | string | `"Brasiléia"` |
| `codigo_resultado_teste_3` | null \| string | `"1"` |
| `estado` | string | `"Acre"` |
| `data_coleta_teste_3` | null \| string | `"2022-08-01"` |
| `estado_notificacao_ibge` | string | `"AC"` |
| `municipio_ibge` | string | `"1200104"` |
| `codigo_resultado_teste_1` | null \| string | `"1"` |
| `codigo_resultado_teste_2` | null \| string | `"2"` |
| `outras_condicoes` | null \| string | `"HIPERTENSÃO"` |
| `data_primeira_dose` | null \| string | `"2021-08-26"` |
| `outro_local_realizacao_testagem` | null | `null` |
| `codigo_laboratorio_primeira_dose` | null \| string | `"PFIZER"` |
| `codigo_estado_teste_2` | null \| string | `"3"` |
| `codigo_contem_comunidade_tradicional` | string | `"2"` |
| `codigo_fabricante_teste_3` | null \| string | `"915"` |
| `codigo_tipo_teste_1` | null \| string | `"3"` |
| `municipio_notificacao` | string | `"Brasiléia"` |
| `codigo_resultado_teste_4` | null | `null` |
| `codigo_estado_teste_3` | null \| string | `"3"` |
| `data_coleta_teste_4` | null | `null` |
| `estado_ibge` | string | `"AC"` |
| `origem` | string | `"parse-cloud"` |
| `data_inicio_sintomas` | null \| string | `"2022-01-06"` |
| `codigo_tipo_teste_4` | null | `null` |
| `municipio_notificacao_ibge` | string | `"1200104"` |
| `codigo_estrategia_covid` | string | `"1"` |
| `codigo_triagem_populacao_especifica` | null | `null` |

## `/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-mortalidade`

O Sistema de Informação sobre Mortalidade (SIM), desenvolvido pelo Ministério da Saúde em 1975, é produto da unificação de mais de quarenta modelos de Declaração de Óbito utilizados ao longo dos anos, para coletar dados sobre mortalidade no país.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-mortalidade?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sim": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `racacor` | string | `"1"` |
| `dtconinv` | null \| string | `"08052025"` |
| `gravidez` | null \| string | `"1"` |
| `peso` | null \| string | `"0528"` |
| `fonteinv` | null \| string | `"6"` |
| `dtrecebim` | string | `"13062025"` |
| `idademae` | null \| string | `"25"` |
| `dtrecoriga` | string | `"27052025"` |
| `atestante` | null \| string | `"5"` |
| `comunsvoim` | null \| string | `"231140"` |
| `horaobito` | string | `"1627"` |
| `contador` | string | `"2"` |
| `linhaii` | null \| string | `"*I251*I10X"` |
| `altcausa` | null \| string | `"2"` |
| `causabas` | string | `"W189"` |
| `versaosist` | string | `"3.2.30"` |
| `idade` | string | `"494"` |
| `natural` | null \| string | `"841"` |
| `morteparto` | null \| string | `"3"` |
| `ocup` | null \| string | `"111410"` |
| `acidtrab` | null \| string | `"2"` |
| `tp_altera` | null \| string | `"09"` |
| `atestado` | string | `"T793/S065 /W189 / /I251*I10"` |
| `difdata` | string | `"061"` |
| `necropsia` | null \| string | `"9"` |
| `codmunres` | string | `"410690"` |
| `obitopuerp` | null \| string | `"3"` |
| `dtinvestig` | null \| string | `"02012025"` |
| `tppos` | null \| string | `"N"` |
| `qtdfilmort` | null \| string | `"00"` |
| `fonte` | null \| string | `"1"` |
| `seriescfal` | null \| string | `"8"` |
| `dtcadinf` | null \| string | `"10032025"` |
| `ocupmae` | null \| string | `"999992"` |
| `escmaeagr1` | null \| string | `"03"` |
| `opor_do` | string | `"44"` |
| `fontes` | null \| string | `"XXSXXX"` |
| `codmunnatu` | null \| string | `"412550"` |
| `assistmed` | null \| string | `"1"` |
| `codestab` | null \| string | `"0015334"` |
| `linhab` | null \| string | `"*S065"` |
| `obitoparto` | null \| string | `"3"` |
| `escmae2010` | null \| string | `"2"` |
| `dtcadinv` | null \| string | `"08052025"` |
| `causamat` | null | `null` |
| `dtcadastro` | string | `"26052025"` |
| `estciv` | null \| string | `"4"` |
| `tpnivelinv` | null \| string | `"M"` |
| `dtconcaso` | null \| string | `"10032025"` |
| `tpresginfo` | null | `null` |
| `qtdfilvivo` | null \| string | `"03"` |
| `dtatestado` | null \| string | `"13042025"` |
| `exame` | null | `null` |
| `versaoscb` | null \| string | `"3.4"` |
| `cb_alt` | null \| string | `"B342"` |
| `obitograv` | null \| string | `"2"` |
| `linhac` | null \| string | `"*W189"` |
| `cb_pre` | null | `null` |
| `gestacao` | null \| string | `"2"` |
| `origem` | string | `"1"` |
| `seriescmae` | null \| string | `"6"` |
| `semagestac` | null \| string | `"25"` |
| `causabas_o` | string | `"W189"` |
| `tipobito` | string | `"2"` |
| `cirurgia` | null | `null` |
| `tpmorteoco` | null \| string | `"8"` |
| `parto` | null \| string | `"2"` |
| `esc2010` | null \| string | `"5"` |
| `sexo` | string | `"2"` |
| `linhaa` | null \| string | `"*T793"` |
| `stcodifica` | string | `"S"` |
| `linhad` | null \| string | `"*W130"` |
| `lococor` | string | `"1"` |
| `circobito` | null \| string | `"9"` |
| `dtobito` | string | `"13042025"` |
| `tpobitocor` | null \| string | `"9"` |
| `numerolote` | string | `"20250041"` |
| `codificado` | string | `"S"` |
| `dtnasc` | string | `"10051930"` |
| `stdoepidem` | string | `"0"` |
| `escmae` | null \| string | `"3"` |
| `codmunocor` | string | `"410690"` |
| `nudiasobco` | null \| string | `"107"` |
| `esc` | null \| string | `"5"` |
| `escfalagr1` | null \| string | `"08"` |
| `stdonova` | string | `"1"` |

## `/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-nascidos-vivos`

O Sistema de Informações sobre Nascidos Vivos (Sinasc), foi implantado oficialmente a partir de 1990, com o objetivo de coletar dados sobre os nascimentos informados em todo território nacional e fornecer dados sobre natalidade para todos os níveis do Sistema de Saúde.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/sistema-de-informacao-sobre-nascidos-vivos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sinasc": "array[0]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `sinasc` | array | `[]` |

## `/vigilancia-e-meio-ambiente/srag-2009-2012`

Legado dos bancos de dados (BD) epidemiológicos de SRAG, da rede de vigilância da Influenza e outros vírus respiratórios, desde o início da sua implantação.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/srag-2009-2012?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"srag_2009_2012": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `imunodepre` | null \| string | `"2"` |
| `ds_outsub` | null | `null` |
| `doenca_tra` | null \| string | `"2"` |
| `outro_sin` | null \| string | `"1"` |
| `dt_pcr` | null \| string | `"19/03/2012"` |
| `obesidade` | null \| string | `"2"` |
| `dt_sin_pri` | string | `"22/02/2012"` |
| `classi_fin` | null \| string | `"3"` |
| `dt_entuti` | null \| string | `"22/08/2012"` |
| `dt_saiduti` | null \| string | `"07/09/2012"` |
| `dispneia` | null \| string | `"1"` |
| `cardiopati` | null \| string | `"2"` |
| `dt_outmet` | null | `null` |
| `uti` | null \| string | `"1"` |
| `cult_out` | null \| string | `"SANGUE"` |
| `dt_antivir` | null \| string | `"14/10/2012"` |
| `hem_tipo_n` | null | `null` |
| `ds_outmet` | null | `null` |
| `out_metodo` | null \| string | `"2"` |
| `srag2012final` | string | `"1"` |
| `criterio` | null \| string | `"1"` |
| `diarreia` | null \| string | `"2"` |
| `res_fluasu` | null | `null` |
| `saturacao` | null \| string | `"2"` |
| `hospital` | string | `"1"` |
| `cult_res` | null \| string | `"3"` |
| `dt_pcr_1` | null \| string | `"09/01/2013"` |
| `co_mu_inte` | null \| string | `"110030"` |
| `tpautocto` | null \| string | `"3"` |
| `pcr` | null \| string | `"1"` |
| `dt_obito` | null \| string | `"11/03/2012"` |
| `pcr_tipo_n` | null \| string | `"1"` |
| `tipo_pcr` | null \| string | `"2"` |
| `cult_amost` | null \| string | `"6"` |
| `dt_cultura` | null \| string | `"21/06/2012"` |
| `coriza` | null \| string | `"1"` |
| `ifi` | null \| string | `"1"` |
| `hepatica` | null \| string | `"2"` |
| `nu_idade_n` | string | `"4023"` |
| `co_uf_inte` | null \| string | `"11"` |
| `res_para2` | null \| string | `"2"` |
| `puerpera` | null \| string | `"2"` |
| `cs_sexo` | string | `"F"` |
| `garganta` | null \| string | `"1"` |
| `hema_etiol` | null | `null` |
| `res_adno` | null \| string | `"2"` |
| `hema_res` | null | `null` |
| `cs_escol_n` | null \| string | `"3"` |
| `hem_tipo_h` | null | `null` |
| `pcr_res` | null \| string | `"4"` |
| `desc_resp` | null \| string | `"1"` |
| `res_flua` | null \| string | `"2"` |
| `res_para1` | null \| string | `"2"` |
| `pcr_amostr` | null \| string | `"9"` |
| `dt_ifi` | null \| string | `"08/11/2012"` |
| `dt_notific` | string | `"23/02/2012"` |
| `suport_ven` | null \| string | `"2"` |
| `id_ocupa_n` | null \| string | `"2424"` |
| `ds_oageeti` | null | `null` |
| `tosse` | null \| string | `"1"` |
| `artralgia` | null \| string | `"2"` |
| `outro_des` | null \| string | `"HEMOPTIASE"` |
| `antiviral` | null \| string | `"2"` |
| `febre` | null \| string | `"1"` |
| `res_outro` | null \| string | `"2"` |
| `classi_out` | null \| string | `"HMPV"` |
| `neurologic` | null \| string | `"2"` |
| `cs_gestant` | string | `"3"` |
| `pcr_out` | null | `null` |
| `pcr_etiol` | null \| string | `"1"` |
| `amostra` | null \| string | `"9"` |
| `calafrio` | null \| string | `"2"` |
| `sg_uf_not` | string | `"11"` |
| `id_mn_resi` | string | `"110030"` |
| `tabagismo` | null \| string | `"1"` |
| `out_morbi` | null \| string | `"2"` |
| `dt_encerra` | null \| string | `"27/02/2014"` |
| `conjuntiv` | null \| string | `"2"` |
| `metabolica` | null \| string | `"2"` |
| `nu_ano` | string | `"2012"` |
| `dt_nasc` | null \| string | `"27/10/1988"` |
| `pcr_tipo_h` | null \| string | `"1"` |
| `evolucao` | null \| string | `"3"` |
| `res_para3` | null \| string | `"2"` |
| `obes_imc` | null \| string | `"48"` |
| `pneumopati` | null \| string | `"2"` |
| `id_municip` | string | `"110030"` |
| `cs_raca` | null \| string | `"4"` |
| `sem_not` | string | `"201208"` |
| `raiox_out` | null \| string | `"INFILTRADO DIFUSO BILATERAL"` |
| `sind_down` | null \| string | `"2"` |
| `dt_raiox` | null \| string | `"16/04/2012"` |
| `out_amost` | null | `null` |
| `morb_desc` | null \| string | `"HIV POSITIVO"` |
| `dt_digita` | string | `"12/04/2012"` |
| `res_vsr` | null \| string | `"2"` |
| `dt_hemaglu` | null | `null` |
| `out_antiv` | null | `null` |
| `mialgia` | null \| string | `"2"` |
| `raiox_res` | null \| string | `"5"` |
| `dt_interna` | null \| string | `"23/02/2012"` |
| `dt_coleta` | null \| string | `"05/11/2012"` |
| `vacina` | null \| string | `"9"` |
| `sg_uf` | string | `"11"` |
| `hemoglobi` | null \| string | `"2"` |
| `res_flub` | null \| string | `"2"` |
| `st_tipofi` | string | `"1"` |
| `renal` | null \| string | `"2"` |

## `/vigilancia-e-meio-ambiente/srag-2013-2018`

Legado dos bancos de dados (BD) epidemiológicos de SRAG, da rede de vigilância da Influenza e outros vírus respiratórios, desde o início da sua implantação.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/srag-2013-2018?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"srag_2013_2018": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `imunodepre` | string | `"2"` |
| `ds_outsub` | null | `null` |
| `doenca_tra` | null | `null` |
| `outro_sin` | null \| string | `"1"` |
| `dt_pcr` | null | `null` |
| `obesidade` | null \| string | `"2"` |
| `dt_sin_pri` | string | `"27/04/2018"` |
| `classi_fin` | string | `"4"` |
| `dt_entuti` | null \| string | `"11/03/2018"` |
| `dt_saiduti` | null \| string | `"08/05/2018"` |
| `dispneia` | null \| string | `"1"` |
| `cardiopati` | string | `"2"` |
| `dt_outmet` | null | `null` |
| `uti` | null \| string | `"2"` |
| `cult_out` | null | `null` |
| `dt_antivir` | null \| string | `"11/03/2018"` |
| `hem_tipo_n` | null | `null` |
| `ds_outmet` | null | `null` |
| `out_metodo` | null \| string | `"2"` |
| `srag2018final` | string | `"1"` |
| `criterio` | string | `"2"` |
| `diarreia` | null | `null` |
| `res_fluasu` | null \| string | `"1"` |
| `saturacao` | string | `"2"` |
| `hospital` | string | `"1"` |
| `cult_res` | null | `null` |
| `dt_pcr_1` | null \| string | `"20/03/2018"` |
| `co_mu_inte` | null \| string | `"110001"` |
| `tpautocto` | null | `null` |
| `pcr` | null \| string | `"1"` |
| `dt_obito` | null \| string | `"20/03/2018"` |
| `pcr_tipo_n` | null | `null` |
| `tipo_pcr` | null \| string | `"2"` |
| `cult_amost` | null | `null` |
| `dt_cultura` | null | `null` |
| `coriza` | null | `null` |
| `ifi` | null \| string | `"2"` |
| `hepatica` | null \| string | `"2"` |
| `nu_idade_n` | string | `"4035"` |
| `co_uf_inte` | null \| string | `"11"` |
| `res_para2` | null \| string | `"2"` |
| `puerpera` | string | `"2"` |
| `cs_sexo` | string | `"F"` |
| `garganta` | string | `"2"` |
| `hema_etiol` | null | `null` |
| `res_adno` | null \| string | `"2"` |
| `hema_res` | null | `null` |
| `cs_escol_n` | null \| string | `"3"` |
| `hem_tipo_h` | null | `null` |
| `pcr_res` | null | `null` |
| `desc_resp` | string | `"1"` |
| `res_flua` | null \| string | `"2"` |
| `res_para1` | null \| string | `"2"` |
| `pcr_amostr` | null | `null` |
| `dt_ifi` | null \| string | `"31/01/2018"` |
| `dt_notific` | string | `"27/04/2018"` |
| `suport_ven` | string | `"1"` |
| `id_ocupa_n` | null | `null` |
| `ds_oageeti` | null | `null` |
| `tosse` | string | `"2"` |
| `artralgia` | null | `null` |
| `outro_des` | null \| string | `"CEFALEIA"` |
| `antiviral` | null \| string | `"1"` |
| `febre` | string | `"1"` |
| `res_outro` | null \| string | `"2"` |
| `classi_out` | null | `null` |
| `neurologic` | string | `"2"` |
| `cs_gestant` | string | `"5"` |
| `pcr_out` | null | `null` |
| `pcr_etiol` | null | `null` |
| `amostra` | string | `"1"` |
| `calafrio` | null | `null` |
| `sg_uf_not` | string | `"11"` |
| `id_mn_resi` | string | `"110001"` |
| `tabagismo` | null | `null` |
| `out_morbi` | null \| string | `"2"` |
| `dt_encerra` | string | `"11/09/2018"` |
| `conjuntiv` | null | `null` |
| `metabolica` | null \| string | `"2"` |
| `nu_ano` | string | `"2018"` |
| `dt_nasc` | string | `"22/02/1983"` |
| `pcr_tipo_h` | null | `null` |
| `evolucao` | string | `"1"` |
| `res_para3` | null \| string | `"2"` |
| `obes_imc` | null \| string | `"40"` |
| `pneumopati` | null \| string | `"2"` |
| `id_municip` | string | `"110001"` |
| `cs_raca` | null \| string | `"4"` |
| `sem_not` | string | `"201817"` |
| `raiox_out` | null \| string | `"PNM"` |
| `sind_down` | string | `"2"` |
| `dt_raiox` | null \| string | `"03/07/2018"` |
| `out_amost` | null \| string | `"ASPIRADO TRAQUEAL"` |
| `morb_desc` | null \| string | `"BRONCOEDISPLASIA PREMATURIDADE"` |
| `dt_digita` | string | `"28/05/2018"` |
| `res_vsr` | null \| string | `"2"` |
| `dt_hemaglu` | null | `null` |
| `out_antiv` | null \| string | `"TAMIFLU"` |
| `mialgia` | null \| string | `"1"` |
| `raiox_res` | null \| string | `"2"` |
| `dt_interna` | null \| string | `"27/04/2018"` |
| `dt_coleta` | null \| string | `"13/03/2018"` |
| `vacina` | null \| string | `"2"` |
| `sg_uf` | string | `"11"` |
| `hemoglobi` | null | `null` |
| `res_flub` | null \| string | `"2"` |
| `st_tipofi` | string | `"2"` |
| `renal` | string | `"2"` |

## `/vigilancia-e-meio-ambiente/srag-2019-2026`

Legado dos bancos de dados (BD) epidemiológicos de SRAG, da rede de vigilância da Influenza e outros vírus respiratórios, desde o início da sua implantação.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/srag-2019-2026?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"srag_2019_2026": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nu_notific` | string | `"315478195042"` |
| `dt_notific` | string | `"2018-12-30"` |
| `sem_not` | string | `"02"` |
| `dt_sin_pri` | string | `"2019-01-06"` |
| `sem_pri` | string | `"02"` |
| `sg_uf_not` | null \| string | `"MG"` |
| `id_regiona` | null \| string | `"BELO HORIZONTE"` |
| `co_regiona` | null \| string | `"1449"` |
| `id_municip` | null \| string | `"BELO HORIZONTE"` |
| `co_mun_not` | null \| string | `"310620"` |
| `cs_sexo` | string | `"M"` |
| `dt_nasc` | string | `"1988-03-17"` |
| `nu_idade_n` | string | `"30"` |
| `tp_idade` | string | `"3"` |
| `cod_idade` | string | `"3030"` |
| `cs_gestant` | string | `"6"` |
| `cs_raca` | null \| string | `"1"` |
| `cs_etinia` | null | `null` |
| `cs_escol_n` | null \| string | `"2"` |
| `id_pais` | null \| string | `"BRASIL"` |
| `co_pais` | null \| string | `"1"` |
| `sg_uf` | string | `"MG"` |
| `id_rg_resi` | null \| string | `"BELO HORIZONTE"` |
| `co_rg_resi` | null \| string | `"1449"` |
| `id_mn_resi` | string | `"RIBEIRAO DAS NEVES"` |
| `co_mun_res` | string | `"315460"` |
| `cs_zona` | string | `"1"` |
| `nosocomial` | null \| string | `"2"` |
| `ave_suino` | null \| string | `"2"` |
| `febre` | string | `"1"` |
| `tosse` | string | `"1"` |
| `garganta` | null \| string | `"2"` |
| `dispneia` | string | `"1"` |
| `desc_resp` | string | `"1"` |
| `saturacao` | string | `"1"` |
| `diarreia` | null \| string | `"2"` |
| `vomito` | null \| string | `"2"` |
| `outro_sin` | null \| string | `"1"` |
| `outro_des` | null \| string | `"DERRAME PLEURAL"` |
| `fator_risc` | null \| string | `"1"` |
| `puerpera` | null \| string | `"2"` |
| `cardiopati` | null \| string | `"2"` |
| `hematologi` | null \| string | `"2"` |
| `sind_down` | null \| string | `"2"` |
| `hepatica` | null \| string | `"1"` |
| `asma` | null \| string | `"2"` |
| `diabetes` | null \| string | `"2"` |
| `neurologic` | null \| string | `"2"` |
| `pneumopati` | null \| string | `"2"` |
| `imunodepre` | null \| string | `"1"` |
| `renal` | null \| string | `"2"` |
| `obesidade` | null \| string | `"2"` |
| `obes_imc` | null \| string | `"25.00"` |
| `out_morbi` | null \| string | `"1"` |
| `morb_desc` | null \| string | `"VARIZES NO ESTOMAGO"` |
| `tabag` | null | `null` |
| `vacina` | null \| string | `"2"` |
| `dt_ut_dose` | null \| string | `"2018-04-23"` |
| `mae_vac` | null \| string | `"9"` |
| `dt_vac_mae` | null | `null` |
| `m_amamenta` | null \| string | `"9"` |
| `dt_doseuni` | null | `null` |
| `dt_1_dose` | null \| string | `"2018-05-23"` |
| `dt_2_dose` | null \| string | `"2018-07-03"` |
| `antiviral` | string | `"1"` |
| `tp_antivir` | null \| string | `"1"` |
| `out_antiv` | null | `null` |
| `dt_antivir` | null \| string | `"2019-01-07"` |
| `hospital` | string | `"1"` |
| `dt_interna` | null \| string | `"2019-01-06"` |
| `sg_uf_inte` | null \| string | `"MG"` |
| `id_rg_inte` | null \| string | `"BELO HORIZONTE"` |
| `co_rg_inte` | null \| string | `"1449"` |
| `id_mn_inte` | null \| string | `"BELO HORIZONTE"` |
| `co_mu_inte` | null \| string | `"310620"` |
| `nm_un_inte` | null \| string | `"UNIDADE DE PRONTO ATENDIMENTO LESTE"` |
| `uti` | null \| string | `"2"` |
| `dt_entuti` | null \| string | `"2019-01-01"` |
| `dt_saiduti` | null \| string | `"2019-01-09"` |
| `suport_ven` | null \| string | `"2"` |
| `raiox_res` | null \| string | `"5.0000000000"` |
| `raiox_out` | null \| string | `"DERRAME PLEURAL"` |
| `dt_raiox` | null \| string | `"2019-01-06"` |
| `amostra` | null \| string | `"2"` |
| `dt_coleta` | null \| string | `"2019-01-02"` |
| `tp_amostra` | null \| string | `"1"` |
| `out_amost` | null \| string | `"SECRECAO TRAQUEAL"` |
| `pcr_resul` | null \| string | `"4"` |
| `dt_pcr` | null \| string | `"2019-01-08"` |
| `pos_pcrflu` | null \| string | `"2"` |
| `tp_flu_pcr` | null \| string | `"2"` |
| `pcr_fluasu` | null \| string | `"1"` |
| `fluasu_out` | null | `null` |
| `pcr_flubli` | null | `null` |
| `flubli_out` | null | `null` |
| `pos_pcrout` | null \| string | `"1"` |
| `pcr_vsr` | null \| string | `"1"` |
| `pcr_para1` | null \| string | `"1"` |
| `pcr_para2` | null | `null` |
| `pcr_para3` | null \| string | `"1"` |
| `pcr_para4` | null | `null` |
| `pcr_adeno` | null \| string | `"1"` |
| `pcr_metap` | null \| string | `"1"` |
| `pcr_boca` | null | `null` |
| `pcr_rino` | null \| string | `"1"` |
| `pcr_outro` | null | `null` |
| `ds_pcr_out` | null | `null` |
| `classi_fin` | null \| string | `"4"` |
| `classi_out` | null | `null` |
| `criterio` | null \| string | `"3"` |
| `evolucao` | null \| string | `"1"` |
| `dt_evoluca` | null \| string | `"2019-01-25"` |
| `dt_encerra` | null \| string | `"2019-02-15"` |
| `dt_digita` | null \| string | `"2019-03-14"` |
| `histo_vgm` | string | `"0"` |
| `pais_vgm` | null | `null` |
| `co_ps_vgm` | null | `null` |
| `lo_ps_vgm` | null | `null` |
| `dt_vgm` | null | `null` |
| `dt_rt_vgm` | null | `null` |
| `pcr_sars2` | null | `null` |
| `pac_cocbo` | null | `null` |
| `pac_dscbo` | null | `null` |
| `out_anim` | null | `null` |
| `dor_abd` | null | `null` |
| `fadiga` | null | `null` |
| `perd_olft` | null | `null` |
| `perd_pala` | null | `null` |
| `tomo_res` | null | `null` |
| `tomo_out` | null | `null` |
| `dt_tomo` | null | `null` |
| `tp_tes_an` | null \| string | `"1"` |
| `dt_res_an` | null \| string | `"2019-01-10"` |
| `res_an` | null \| string | `"4"` |
| `pos_an_flu` | null \| string | `"2"` |
| `tp_flu_an` | null | `null` |
| `pos_an_out` | null \| string | `"1"` |
| `an_sars2` | null | `null` |
| `an_vsr` | null \| string | `"1"` |
| `an_para1` | null | `null` |
| `an_para2` | null | `null` |
| `an_para3` | null | `null` |
| `an_adeno` | null | `null` |
| `an_outro` | null | `null` |
| `ds_an_out` | null | `null` |
| `tp_am_sor` | null | `null` |
| `sor_out` | null | `null` |
| `dt_co_sor` | null | `null` |
| `tp_sor` | null | `null` |
| `out_sor` | null | `null` |
| `dt_res` | null | `null` |
| `res_igg` | null | `null` |
| `res_igm` | null | `null` |
| `res_iga` | null | `null` |
| `pov_ct` | null \| string | `"2"` |
| `tp_pov_ct` | null | `null` |
| `tem_cpf` | null \| string | `"1"` |
| `estrang` | null \| string | `"2"` |
| `vacina_cov` | null \| string | `"9"` |
| `dose_1_cov` | null | `null` |
| `dose_2_cov` | null | `null` |
| `dose_ref` | null | `null` |
| `dose_2ref` | null | `null` |
| `dose_adic` | null | `null` |
| `dos_re_bi` | null | `null` |
| `fab_cov_1` | null | `null` |
| `fab_cov_2` | null | `null` |
| `fab_covrf` | null | `null` |
| `fab_covrf2` | null | `null` |
| `fab_adic` | null | `null` |
| `fab_re_bi` | null | `null` |
| `lote_1_cov` | null | `null` |
| `lote_2_cov` | null | `null` |
| `lote_ref` | null | `null` |
| `lote_ref2` | null | `null` |
| `lote_adic` | null | `null` |
| `lot_re_bi` | null | `null` |
| `fnt_in_cov` | null \| string | `"1"` |
| `trat_cov` | null | `null` |
| `tipo_trat` | null | `null` |
| `dt_trt_cov` | null | `null` |
| `out_trat` | null | `null` |
| `surto_sg` | null | `null` |
| `co_detec` | null | `null` |
| `vg_oms` | null | `null` |
| `vg_omsout` | null | `null` |
| `vg_lin` | null | `null` |
| `vg_met` | null | `null` |
| `vg_metout` | null | `null` |
| `vg_dtres` | null | `null` |
| `vg_enc` | null | `null` |
| `vg_reinf` | null | `null` |
| `vg_codest` | null | `null` |
| `reinf` | null \| string | `"2"` |

## `/vigilancia-e-meio-ambiente/mpox`

O Projeto e-SUS Sinan tem como objetivo modernizar o Sistema de Informação de Agravos de Notificação (Sinan), além de registrar em tempo real as notificações das doenças e agravos que compõem a lista nacional de notificação compulsória e substituir as versões vigentes (Sinan NET e Sinan Online) do sistema Sinan, bem como os aplicativos auxiliares.

- URL: `https://apidadosabertos.saude.gov.br/vigilancia-e-meio-ambiente/mpox?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"mpox": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `htlv` | string | `"2"` |
| `dt_interna` | null \| string | `"2022-11-15"` |
| `pac_imunossup` | string | `"9"` |
| `donovanose` | string | `"2"` |
| `hpv` | string | `"2"` |
| `dt_sin_pri` | null \| string | `"2022-11-08"` |
| `uti` | string | `"9"` |
| `cs_raca` | string | `"4"` |
| `linfogranuloma` | string | `"2"` |
| `co_uf_res` | string | `"15"` |
| `dip` | string | `"2"` |
| `data_vacina` | null | `null` |
| `caract_genomica` | string | `"0"` |
| `classi_fin` | string | `"8"` |
| `cs_sexo` | string | `"1"` |
| `orienta_sexual` | string | `"9"` |
| `doenca_tra1` | string | `"9"` |
| `dt_coleta` | null \| string | `"2022-10-06"` |
| `clado` | string | `"0"` |
| `nu_idade_n` | string | `"28"` |
| `transm` | string | `"8"` |
| `clamidea` | string | `"2"` |
| `hiv` | string | `"9"` |
| `evolucao` | string | `"0"` |
| `verruga_genital` | string | `"2"` |
| `id_mn_resi` | string | `"150815"` |
| `estrangeiro` | string | `"2"` |
| `cancro_mole` | string | `"2"` |
| `vacina` | string | `"0"` |
| `sg_uf_not` | string | `"PA"` |
| `comp_sexual` | string | `"9"` |
| `vinculo_epi` | string | `"2"` |
| `profis_saude` | null \| string | `"2"` |
| `contag_cd4` | null \| string | `"0"` |
| `trichomomas_vaginals` | string | `"2"` |
| `gonorreia` | string | `"2"` |
| `id_municip` | string | `"150360"` |
| `ist_ativa` | string | `"9"` |
| `cs_gestant` | string | `"7"` |
| `contat_animal` | string | `"0"` |
| `dt_notific` | string | `"2022-11-15"` |
| `met_lab` | string | `"0"` |
| `ident_genero` | string | `"9"` |
| `resultado_exa_lab` | string | `"4"` |
| `outro_des` | null \| string | `"PRURIDO"` |
| `tp_amost` | string | `"0"` |
| `dt_evolucao` | null | `null` |
| `mycoplasma_genital` | string | `"2"` |
| `sintoma` | null \| string | `"FEBRE, LESAO CUTANEA"` |
| `local_cont` | null \| string | `"9"` |
| `sg_uf` | string | `"PA"` |
| `hospital` | string | `"1"` |
| `sifilis` | string | `"2"` |
| `herpes_genital` | string | `"2"` |
| `dt_conclusao` | null \| string | `"2023-01-14"` |

## `/assistencia-a-saude/unidade-basicas-de-saude`

Relação de Unidades Básicas de Saúde - UBS cadastradas no CNES

- URL: `https://apidadosabertos.saude.gov.br/assistencia-a-saude/unidade-basicas-de-saude?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"ubs": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `ibge` | string | `"260290"` |
| `bairro` | string | `"PONTE DOS CARVALHOS"` |
| `logradouro` | string | `"RUA DO CEMITERIO"` |
| `cnes` | string | `"0000302"` |
| `uf` | string | `"26"` |
| `latitude` | null \| string | `"-8,21811"` |
| `longitude` | null \| string | `"-35,22944"` |
| `nome` | string | `"USF SANTO ESTEVAO"` |

## `/saude-indigena/siasi-acompanhamento-gestacional`

Apresenta microdados de informações registradas no Módulo de Gestação e Acompanhamento Gestacional do Sistema de Atenção à Saúde Indígena (SIASI). Dados referem-se aos registros de acompanhamento de gestações de mulheres indígenas residentes em aldeias ou acampamentos, cuja gestação foi finalizada no ano de referência.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/siasi-acompanhamento-gestacional?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"siasi_acompanhamento_gestacional": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `gestao_do_dsei` | string | `"ALAGOAS E SERGIPE"` |
| `codigo_da_gestao_do_dsei` | string | `"1"` |
| `codigo_do_polo_base` | string | `"1588"` |
| `descricao_do_polo_base` | string | `"KARIRI-XOKÓ"` |
| `codigo_da_terra_indigena` | string | `"254"` |
| `nome_da_terra_indigena` | string | `"KARIRI-XOCÓ"` |
| `codigo_do_ibge` | string | `"270750"` |
| `nome_do_municipio` | string | `"PORTO REAL DO COLEGIO"` |
| `sigla_da_uf` | string | `"AL"` |
| `data_de_nascimento` | string | `"2002-06-19"` |
| `tipo_sexo` | string | `"N"` |
| `codigo_da_localidade` | string | `"ALD"` |
| `data_da_ultima_menstruacao` | string | `"2020-10-15"` |
| `data_da_finalizacao` | string | `"2021-07-21"` |
| `data_do_acompanhamento` | string | `"2021-02-08"` |
| `status_risco_gestacional` | string | `"B"` |
| `tipo_do_local_de_atendimento` | string | `"PL"` |
| `codigo_do_profissional` | string | `"11505"` |
| `codigo_cbo_da_familia` | string | `"2235"` |
| `descricao_do_cbo_da_familia` | string | `"ENFERMEIROS E AFINS"` |
| `codigo_cbo_da_ocupacao` | string | `"223505"` |
| `descricao_do_cbo_da_ocupacao` | string | `"Enfermeiro"` |
| `status_do_motivo_da_finalizacao` | string | `"NAS"` |

## `/saude-indigena/siasi-modulo-morbidades`

Apresenta microdados de informações registradas Módulo Módulo de Morbidades no Sistema de Atenção à Saúde Indígena (SIASI) para o CID-X n°Z001-Exame de rotina de saúde da criança, referente aos acompanhamentos de crianças menores de um ano.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/siasi-modulo-morbidades?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"siasi_modulo_morbidades": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `gestao_do_dsei` | string | `"LESTE DE RORAIMA"` |
| `codigo_da_gestao_do_dsei` | string | `"15"` |
| `codigo_do_polo_base` | string | `"1661"` |
| `descricao_do_polo_base` | string | `"MATIRI"` |
| `codigo_da_terra_indigena` | string | `"441"` |
| `nome_da_terra_indigena` | string | `"RAPOSA SERRA DO SOL"` |
| `codigo_do_ibge` | string | `"140040"` |
| `nome_do_municipio` | string | `"NORMANDIA"` |
| `sigla_da_uf` | string | `"RR"` |
| `data_de_nascimento` | string | `"2014-12-20"` |
| `tipo_sexo` | string | `"F"` |
| `codigo_da_localidade` | string | `"ALD"` |
| `codigo_do_cid10` | string | `"Z00.1"` |
| `nome_da_categoria_e_subcategoria` | string | `"Exame de rotina de saude da crianca"` |
| `codigo_da_categoria_pai` | string | `"Z00"` |
| `data_de_atendimento` | string | `"2028-12-20"` |
| `mes_de_atendimento` | string | `"12"` |
| `ano_de_atendimento` | string | `"2020"` |
| `idade_no_atendimento_em_dias` | number | `381.0` |
| `faixa_etaria_no_atendimento` | null \| string | `"270-364 dias"` |
| `codigo_cbo_da_ocupacao` | null \| string | `"223505"` |
| `descricao_do_cbo_da_ocupacao` | null \| string | `"Enfermeiro"` |
| `codigo_da_familia_cbo` | null \| string | `"2235"` |
| `descricao_do_cbo_da_familia` | null \| string | `"ENFERMEIROS E AFINS"` |

## `/saude-indigena/sesai-atendimentos`

Microdados extraídos do SIASI representam registros sistematizados de atendimentos coletivos realizados pelas Equipes Multidisciplinares de Saúde Indígena (EMSI), com foco na atenção básica e na promoção da saúde dos povos indígenas. As informações estão segmentadas por faixa etária e abrangem os territórios indígenas em nível nacional.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-atendimentos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_atendimentos": "array[99]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `ds_dsei` | string | `"ALAGOAS E SERGIPE"` |
| `ds_polo_base` | string | `"ACONÃ"` |
| `no_aldeia` | string | `"ACONÃ"` |
| `nu_mes` | number | `1.0` |
| `no_municipio` | string | `"TRAIPU"` |
| `sg_uf` | string | `"AL"` |
| `no_terra_indigena` | string | `"ACONÃ"` |
| `ds_cbo_familia` | string | `"MÉDICOS CLÍNICOS"` |
| `ds_cbo_ocupacao` | string | `"Médico clínico"` |
| `categoria_siconv` | string | `"1 - Número de atendimentos de Médicos (as)"` |
| `qt_faixa_etaria_0_4` | number | `7.0` |
| `qt_faixa_etaria_5_9` | number | `4.0` |
| `qt_faixa_etaria_10_19` | number | `2.0` |
| `qt_faixa_etaria_20_29` | number | `10.0` |
| `qt_faixa_etaria_30_59` | number | `17.0` |
| `qt_faixa_etaria_60_mais` | number | `4.0` |
| `qt_faixa_etaria_ignorado` | number | `0.0` |
| `todos` | number | `44.0` |
| `ds_tipo_aldeia` | string | `"Aldeia"` |

## `/saude-indigena/sesai-recursos-humanos`

O SESAI-RH é o sistema oficial utilizado pela Secretaria de Saúde Indígena (SESAI) para o gerenciamento dos recursos humanos que atuam na atenção à saúde indígena no Brasil. Ele centraliza e organiza informações cadastrais, funcionais e contratuais dos profissionais vinculados aos Distritos Sanitários Especiais Indígenas (DSEI).

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-recursos-humanos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_recursos_humanos": "array[99]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `co_colaborador_desidentificado` | string | `"F3B411386377271ED72E676017B5D57E812FB498"` |
| `ds_dsei` | string | `"XINGU"` |
| `no_tipo_vinculo` | string | `"CONVÊNIO ONG"` |
| `tp_atuacao1` | string | `"GESTÃO DE CONVÊNIO"` |
| `no_categoria` | string | `"AUXILIAR DE ESCRITÓRIO, EM GERAL"` |
| `ds_escolaridade` | string | `"ENSINO MEDIO"` |
| `indigena` | string | `"SIM"` |
| `faixa_etaria` | string | `"18 a 19"` |
| `sg_sexo` | string | `"F"` |

## `/saude-indigena/siasi-modulo-saude-bucal-ficha3`

Microdados de informações registradas no Módulo de Saúde Bucal do Sistema de Informação da Atenção à Saúde Indígena (SIASI). Ficha 3 – Consolidado Mensal de Odontologia – Atividades Coletivas, que possibilitam a análise das características das atividades de educação em saúde, de escovação dental supervisionada, de aplicação coletiva de flúor gel e quanto a distribuição de material de higiene bucal.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/siasi-modulo-saude-bucal-ficha3?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"siasi_modulo_saude_bucal_ficha3": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `dsei_gestao` | string | `"MARANHÃO"` |
| `co_dsei_gestao` | string | `"19"` |
| `co_polo_base` | string | `"1732"` |
| `polo_base` | string | `"GRAJAÚ"` |
| `co_aldeia` | string | `"60064"` |
| `aldeia` | string | `"PATIZAL"` |
| `co_terra_indigena` | string | `"53"` |
| `no_municipio` | string | `"GRAJAU"` |
| `sg_uf` | string | `"MA"` |
| `nu_ano` | string | `"2022"` |
| `educ_prof_medio_comunidade` | number | `1.0` |
| `educ_prof_medio_estab` | number | `0.0` |
| `educ_prof_superior_comunidade` | number | `1.0` |
| `educ_prof_superior_estab` | number | `0.0` |
| `educ_escovacao_dental_superv` | number | `0.0` |
| `aplicacao_topica_fluor` | number | `0.0` |
| `escova_dental_distribuida` | number | `12.0` |
| `creme_dental_distribuido` | number | `12.0` |
| `fio_dental_distribuido` | number | `0.0` |

## `/saude-indigena/siasi-modulo-saude-bucal-ficha4`

Microdados de informações registradas no Módulo de Saúde Bucal do Sistema de Informação da Atenção à Saúde Indígena (SIASI). Ficha 4 - Ficha odontológica individual, que possibilitam a análise das características demográficas da população atendida bem como informações relacionadas a presença de má-formação orofaciais, uso e necessidade de prótese dentária e fluorose dentária.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/siasi-modulo-saude-bucal-ficha4?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"siasi_modulo_saude_bucal_ficha4": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `gestao_do_dsei` | string | `"ALTO RIO SOLIMÕES"` |
| `codigo_da_gestao_do_dsei` | string | `"7"` |
| `codigo_do_polo_base` | string | `"1565"` |
| `descricao_do_polo_base` | string | `"SÃO PAULO DE OLIVENÇA"` |
| `codigo_do_ibge` | string | `"130390"` |
| `nome_do_municipio` | string | `"SAO PAULO DE OLIVENCA"` |
| `sigla_da_uf` | string | `"AM"` |
| `tipo_sexo` | string | `"F"` |
| `codigo_da_terra_indigena` | string | `"365"` |
| `nome_da_terra_indigena` | string | `"NOVA ESPERANÇA DO RIO JANDIATUBA"` |
| `codigo_da_localidade` | string | `"ALD"` |
| `data_da_consulta` | null | `null` |
| `codigo_do_profissional` | string | `"8701"` |
| `codigo_cbo_da_familia` | string | `"2232"` |
| `descricao_do_cbo_da_familia` | string | `"CIRURGIÕES-DENTISTAS"` |
| `codigo_cbo_da_ocupacao` | string | `"223272"` |
| `descricao_do_cbo_da_ocupacao` | string | `"Cirurgião dentista de saúde coletiva"` |
| `codigo_do_tipo_protese_necess_sup` | string | `"1"` |
| `necessidade_sup` | string | `"Necessidade de prótese parcial"` |
| `codigo_tipo_protese_uso_sup` | string | `"0"` |
| `uso_sup` | string | `"Não usa prótese"` |
| `codigo_do_tipo_protese_necess_inf` | string | `"1"` |
| `necess_inf` | string | `"Necessidade de prótese parcial"` |
| `codigo_do_tipo_protese_uso_inf` | string | `"0"` |
| `uso_inf` | string | `"Uso de prótese parcial"` |
| `codigo_tipo_fluorose` | null \| string | `"0"` |
| `descricao_tipo_fluorose` | null \| string | `"Normal"` |
| `status_ma_formacao` | string | `"N"` |
| `data_de_nascimento` | string | `"1997-01-10"` |
| `idade_na_consulta` | string | `"27"` |

## `/saude-indigena/siasi-modulo-saude-bucal-ficha7`

Microdados de informações registradas no Módulo de Saúde Bucal do Sistema de Informação da Atenção à Saúde Indígena (SIASI). Ficha 7 - Consolidado Mensal de Odontologia – Procedimentos Individuais, que possibilitam a análise das características dos atendimentos e procedimentos odontológicos realizados pelas Equipes Multidisciplinares de saúde Indígena (EMSI).

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/siasi-modulo-saude-bucal-ficha7?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"siasi_modulo_saude_bucal_ficha7": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `gestao_do_dsei` | string | `"LITORAL SUL"` |
| `codigo_da_gestao_do_dsei` | string | `"35"` |
| `nome_do_municipio` | string | `"PARATY"` |
| `sigla_da_uf` | string | `"RJ"` |
| `nome_da_terra_indigena` | string | `"PARATI-MIRIM"` |
| `codigo_do_polo_base` | string | `"1633"` |
| `descricao_do_polo_base` | string | `"ANGRA DOS REIS"` |
| `codigo_da_aldeia` | string | `"49658"` |
| `descricao_da_aldeia` | string | `"ITAXI MIRIM"` |
| `codigo_da_terra_indigena` | string | `"389"` |
| `codigo_do_ibge` | string | `"330380"` |
| `numero_do_mes` | string | `"3"` |
| `numero_do_ano` | string | `"2020"` |
| `consulta_odontologica_programada` | number | `3.0` |
| `consultas_atendidas_por_agendamento` | number | `6.0` |
| `demanda_espontanea` | number | `2.0` |
| `aplicacao_terapeutica_de_fluor` | number | `5.0` |
| `aplicacao_cariostatico` | number | `0.0` |
| `aplicacao_selante` | number | `0.0` |
| `evidencia_placa_bacteriana` | number | `0.0` |
| `rap_supragengival` | number | `0.0` |
| `rap_suibgengival` | number | `0.0` |
| `protese_complemento_dentino` | number | `0.0` |
| `tratamento_restauracao_atraumatico` | number | `2.0` |
| `restauracao_ionomero_de_vidro` | number | `0.0` |
| `restauracao_de_resiona` | number | `2.0` |
| `restrauracao_amalgama` | number | `0.0` |
| `outra_restauracao` | number | `0.0` |
| `pulpotomia` | number | `0.0` |
| `exodontia_decidup` | number | `0.0` |
| `exodontia_permanente` | number | `2.0` |
| `outro_procedimento_cirurgico` | number | `1.0` |
| `sutura` | number | `2.0` |
| `tratamento_alveolite` | number | `0.0` |
| `outro_procedimento_urgencia` | number | `0.0` |
| `endodontia` | number | `0.0` |
| `periodontia` | number | `0.0` |
| `protese` | number | `0.0` |
| `cirurgia_buco_maxilo_facial` | number | `0.0` |
| `ortodontia` | number | `0.0` |
| `radiologia` | number | `0.0` |
| `analgesico` | number | `2.0` |
| `anti-inflamatorio` | number | `0.0` |
| `antibiotico` | number | `2.0` |
| `outra_prescricao` | number | `0.0` |
| `tatramento_odontologico_basico` | number | `2.0` |

## `/saude-indigena/sesai-acidentes-ofidicos`

Armazena registros de acidentes ofidicos ocorridos em indigenas registrados no Sistema de Informacao da Atencao a Saude dos Povos Indigenas (Siasi).

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-acidentes-ofidicos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_acidentes_ofidicos": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `dsei_gestao` | string | `"LESTE DE RORAIMA"` |
| `ds_polo_base` | string | `"JACAMIM"` |
| `co_municipio_ibge` | integer | `140015` |
| `no_municipio` | string | `"BONFIM"` |
| `sg_uf` | string | `"RR"` |
| `tp_sexo` | string | `"F"` |
| `idade` | integer | `22` |
| `faixa_etaria` | string | `"20-24 ANOS"` |
| `co_cid10` | string | `"X29.4"` |
| `no_categoria_subcategoria` | string | `"Contato com animais ou plantas venenosos, sem especificacao…` |
| `dt_atendimento` | string | `"2022-07-16 00:00:00"` |

## `/saude-indigena/sesai-arboviroses`

Armazena dados dos casos de Dengue, Zika Virus, Chihungunya e Febre Amarela e outras arboviroses registrados na populacao indigena assistida pelo Subsistema de Atencao a Saude Indigena (SasiSUS) e disponibilizados pelo Sistema de Informacao da Atencao a Saude Indigena (Siasi).

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-arboviroses?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_arboviroses": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `dsei_gestao` | string | `"INTERIOR SUL"` |
| `ds_polo_base` | string | `"PASSO FUNDO"` |
| `co_municipio_ibge` | integer | `430580` |
| `no_municipio` | string | `"CONSTANTINA"` |
| `sg_uf` | string | `"RS"` |
| `tp_sexo` | string | `"F"` |
| `idade` | integer | `26` |
| `faixa_etaria` | string | `"25-29 ANOS"` |
| `co_cid10` | string | `"A90"` |
| `no_categoria_subcategoria` | string | `"Dengue [dengue classico]"` |
| `dt_atendimento` | string | `"2022-12-12 00:00:00"` |

## `/saude-indigena/sesai-assistencia-farmaceutica`

Armazena o registro, o controle e o monitoramento das atividades relacionadas ao ciclo da assistencia farmaceutica, contemplando os processos de recebimento, armazenamento, movimentacao, distribuicao e dispensacao de medicamentos e insumos em saude.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-assistencia-farmaceutica?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_assistencia_farmaceutica": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `dsei` | string | `"ALAGOAS E SERGIPE"` |
| `material` | string | `"ACETATO DE MEDROXIPROGESTERONA 150MG/1ML"` |
| `unidade_de_medida` | string | `"FR-AMP."` |
| `qtd_entregue` | integer | `110` |

## `/saude-indigena/sesai-cobertura-vacinal`

Armazena a base de Coberturas Vacinais, no ano de 2022 dos Distritos Sanitarios Especiais Indigenas (Dsei) no ambito do Plano de Dados Abertos (PDA).

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-cobertura-vacinal?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_cobertura_vacinal": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `ano` | integer | `2022` |
| `uf` | string | `"AL"` |
| `dsei` | string | `"ALAGOAS E SERGIPE"` |
| `polo` | string | `"KATOKINN"` |
| `polio` | number | `90.5` |
| `pnm_10v` | number | `83.9` |
| `pnm_23v` | number | `91.2` |
| `penta` | number | `98.3` |
| `bcg` | number | `98.7` |
| `vhb` | number | `93.6` |
| `fa` | number | `97.0` |
| `vorh` | number | `75.0` |
| `dt` | number | `79.8` |
| `menigo_c` | number | `100.0` |
| `meningo_acwy` | number | `42.1` |
| `hpv` | number | `52.0` |
| `varicela` | number | `95.3` |
| `vha` | number | `98.5` |
| `influ` | number | `88.5` |
| `trip_viral` | number | `94.9` |
| `homogeneidade_do_polo` | number | `35.3` |

## `/saude-indigena/sesai-covid19`

Armazena os registros de COVID-19 ocorridos em indigenas registrados na Plataforma de Emergencia em Saude Indigena.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-covid19?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_covid19": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `co_dsei` | integer | `28` |
| `ds_dsei` | string | `"MÉDIO RIO SOLIMÕES E AFLUENTES"` |
| `co_polo_base` | integer | `1779` |
| `ds_polo_base` | string | `"CARAUARÍ"` |
| `co_seq_covid` | integer | `288739582` |
| `tp_sexo` | string | `"M"` |
| `st_gestante` | string | `"A"` |
| `faixa_etaria` | string | `"15-19 ANOS"` |
| `st_assintomatico` | string | `"N"` |
| `dt_sintomas` | null \| string | `"2020-01-31 00:00:00"` |
| `dt_notificacao` | string | `"2020-02-08 00:00:00"` |
| `st_sg` | string | `"S"` |
| `st_srag` | string | `"N"` |
| `st_hospitalizado` | string | `"S"` |
| `st_classificao` | string | `"Confirmado Lab"` |
| `st_doenca_cardiovascular` | null \| string | `"S"` |
| `st_diabetes` | null \| string | `"S"` |
| `st_doenca_hepatica` | null | `null` |
| `st_doenca_neurologica` | null \| string | `"S"` |
| `st_renal` | null \| string | `"S"` |
| `st_pulmonar` | null \| string | `"S"` |
| `st_neoplasia` | null | `null` |
| `st_obesidade` | null | `null` |

## `/saude-indigena/sesai-demografico`

Armazena dados demograficos da populacao assistida com o SIASI.

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-demografico?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_demografico": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `dsei_gestao` | string | `"ALTO RIO JURUÁ"` |
| `co_dsei_gestao` | integer | `4` |
| `co_seq_dsei` | integer | `4` |
| `co_seq_polo_base` | integer | `1570` |
| `ds_polo_base` | string | `"FEIJÓ"` |
| `co_municipio_ibge` | integer | `120030` |
| `no_municipio` | string | `"FEIJO"` |
| `sg_uf` | string | `"AC"` |
| `st_indigena` | string | `"S"` |
| `dt_nascimento` | string | `"6/1/1901 00:00:00"` |
| `co_seq_terra_indigena` | integer | `256` |
| `no_terra_indigena` | string | `"KATUKINA/KAXINAWÁ"` |
| `tp_sexo` | string | `"F"` |
| `nu_residencia` | string | `"10"` |
| `nu_familia` | string | `"1"` |
| `st_indio` | string | `"V"` |
| `idade` | integer | `121` |
| `faixa_etaria` | string | `"80 ANOS OU MAIS"` |

## `/saude-indigena/sesai-doencas-diarreicas-agudas`

Armazena registros de Doencas Diarreicas Agudas ocorridos em indigenas registrados no Sistema de Informacao da Atencao a Saude dos Povos Indigenas (Siasi).

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-doencas-diarreicas-agudas?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_doencas_diarreicas_agudas": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `dsei_gestao` | string | `"ARAGUAIA"` |
| `ds_polo_base` | string | `"CONFRESA"` |
| `co_municipio_ibge` | integer | `510677` |
| `no_municipio` | string | `"PORTO ALEGRE DO NORTE"` |
| `sg_uf` | string | `"MT"` |
| `tp_sexo` | string | `"M"` |
| `co_cid10` | string | `"A04.9"` |
| `no_categoria_subcategoria` | string | `"Infeccao intestinal bacteriana nao especificada"` |
| `dt_atendimento` | string | `"2022-04-05 00:00:00"` |
| `idade` | integer | `11` |
| `faixa_etaria` | string | `"10-14 ANOS"` |

## `/saude-indigena/sesai-doencas-imunopreveniveis`

Armazena registros doencas imunopreveniveis ocorridos em indigenas registrados no Sistema de Informacao da Atencao a Saude dos Povos Indigenas (Siasi).

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-doencas-imunopreveniveis?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_doencas_imunopreveniveis": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `dsei_gestao` | string | `"ARAGUAIA"` |
| `ds_polo_base` | string | `"CONFRESA"` |
| `co_municipio_ibge` | integer | `510677` |
| `no_municipio` | string | `"PORTO ALEGRE DO NORTE"` |
| `sg_uf` | string | `"MT"` |
| `tp_sexo` | string | `"M"` |
| `idade` | integer | `23` |
| `faixa_etaria` | string | `"20-24 ANOS"` |
| `co_cid10` | string | `"J11.8"` |
| `no_categoria_subcategoria` | string | `"Influenza [gripe] com outras manifestacoes, devida a virus …` |
| `dt_atendimento` | string | `"2022-12-14 00:00:00"` |

## `/saude-indigena/sesai-doencas-zoonoticas`

Armazena registros de acidentes ofidicos ocorridos em indigenas registrados no Sistema de Informacao da Atencao a Saude dos Povos Indigenas (Siasi).

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-doencas-zoonoticas?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_doencas_zoonoticas": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `dsei_gestao` | string | `"XINGU"` |
| `ds_polo_base` | string | `"DIAUARUM"` |
| `co_municipio_ibge` | integer | `510706` |
| `no_municipio` | string | `"QUERENCIA"` |
| `sg_uf` | string | `"MT"` |
| `tp_sexo` | string | `"M"` |
| `idade` | integer | `40` |
| `faixa_etaria` | string | `"40-44 ANOS"` |
| `co_cid10` | string | `"B55"` |
| `no_categoria_subcategoria` | string | `"Leishmaniose"` |
| `dt_atendimento` | string | `"2022-07-22 00:00:00"` |

## `/saude-indigena/sesai-hepatites-virais`

Armazena os registros de hepatites virais ocorridos em indigenas registrados no Sistema de Informacao da Atencao a Saude dos Povos Indigenas (Siasi).

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-hepatites-virais?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_hepatites_virais": "array[0]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `sesai_hepatites_virais` | array | `[]` |

## `/saude-indigena/sesai-obitos`

Armazena registros de obitos ocorridos em indigenas registrados no Sistema de Informacao da Atencao a Saude dos Povos Indigenas (Siasi).

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-obitos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_obitos": "array[0]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `sesai_obitos` | array | `[]` |

## `/saude-indigena/sesai-doencas-respiratorias`

Registros de doenças respiratórias em indígenas registrados no Siasi

- URL: `https://apidadosabertos.saude.gov.br/saude-indigena/sesai-doencas-respiratorias?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sesai_doencas_respiratorias": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `dsei_gestao` | string | `"XAVANTE"` |
| `cod_dsei` | number | `31.0` |
| `ds_polo_base` | string | `"SÃO MARCOS"` |
| `co_municipio_ibge` | number | `510180.0` |
| `no_municipio` | string | `"BARRA DO GARCAS"` |
| `sg_uf` | string | `"MT"` |
| `tp_sexo` | string | `"F"` |
| `co_cid10` | string | `"J00"` |
| `no_categoria_subcategoria` | string | `"Nasofaringite aguda [resfriado comum]"` |
| `dt_atendimento` | string | `"2022-06-03 00:00:00"` |
| `dt_primeiro_sintoma` | string | `"2022-06-02 00:00:00"` |
| `tp_criterio_confirmacao` | string | `"CLI"` |
| `faixa_etaria` | string | `"1-4 ANOS"` |

## `/ciencia-tecnologia/dgits-contribuicoes-consultas-publicas`

A Conitec é um órgão colegiado permanente, integrante da estrutura do Ministério da Saúde, e tem por objetivo assessorar a Pasta nas atribuições relativas à incorporação, exclusão ou alteração de tecnologias em saúde, pelo SUS, bem como na constituição ou alteração de Protocolos Clínicos e Diretrizes Terapêuticas (PCDT). As Consultas Públicas da Conitec referente as tecnologias estão na plataforma Participa + Brasil.

- URL: `https://apidadosabertos.saude.gov.br/ciencia-tecnologia/dgits-contribuicoes-consultas-publicas?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"dgits_contribuicoes_consultas_publicas": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `ano` | string | `"2013"` |
| `numero_da_semana_epidemiologica_e_ano` | string | `"42/2013"` |
| `nome_da_tecnologia` | string | `"Exame e Aconselhamento genético de doenças raras."` |
| `total` | number | `43.0` |
| `data_da_consulta` | string | `"2013-11-20"` |

## `/ciencia-tecnologia/dgits-controle-demandas-conitec`

A Conitec é um órgão colegiado permanente, integrante da estrutura do Ministério da Saúde, e tem por objetivo assessorar a Pasta nas atribuições relativas à incorporação, exclusão ou alteração de tecnologias em saúde, pelo SUS, bem como na constituição ou alteração de Protocolos Clínicos e Diretrizes Terapêuticas (PCDT). Estão apresentadas nestes dados a seção somente as demandas de tecnologias já avaliadas ou em avaliação. Assim, aquelas que estão em análise de conformidade ou que já foram consideradas não conformes, nos termos da legislação vigente, não estão computadas.

- URL: `https://apidadosabertos.saude.gov.br/ciencia-tecnologia/dgits-controle-demandas-conitec?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"dgits_controle_demandas_conitec": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `origem` | string | `"Interna"` |
| `data_do_protocolo` | string | `"2012-01-01"` |
| `tipo_de_tecnologia` | string | `"Medicamento"` |
| `tema_da_saude` | string | `"Reumatologia"` |
| `nome_do_demandante` | string | `"Secretaria de Estado de Saúde de Minas Gerais  SES/MG"` |

## `/ciencia-tecnologia/dgits-controle-pcdt`

A Conitec é um órgão colegiado permanente, integrante da estrutura do Ministério da Saúde, e tem por objetivo assessorar a Pasta nas atribuições relativas à incorporação, exclusão ou alteração de tecnologias em saúde, pelo SUS, bem como na constituição ou alteração de Protocolos Clínicos e Diretrizes Terapêuticas (PCDT).

- URL: `https://apidadosabertos.saude.gov.br/ciencia-tecnologia/dgits-controle-pcdt?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"dgits_controle_pcdt": "array[83]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `descricao_do_nome` | string | `"Acidentes Escorpiônicos"` |
| `status` | string | `"Aprovado*"` |
| `descricao_do_tipo` | string | `"PCDT"` |

## `/ciencia-tecnologia/dgits-tecnologias-diretrizes`

O Monitoramento do Horizonte Tecnológico (MHT) tem como objetivo identificar tecnologias novas e emergentes (em estágio de desenvolvimento) e prever os impactos que possam causar no sistema de saúde. O documento disponibilizado foi elaborado com base nas evidências disponíveis, com a finalidade de informar à sociedade quanto aos potenciais das tecnologias em desenvolvimento para o tratamento da Covid-19.

- URL: `https://apidadosabertos.saude.gov.br/ciencia-tecnologia/dgits-tecnologias-diretrizes?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"dgits_tecnologias_diretrizes": "array[10]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `quantidade` | string | `"15.0"` |
| `tecnologias_diretrizes_covid19` | string | `"Nirmatrelvir/Ritonavir para o tratamento da Covid-19 para p…` |
| `demandante` | string | `"Secretaria de Ciência, Tecnologia e Inovação e do Complexo …` |
| `analise_inicial_conitec` | string | `"Favorável à manutenção da incorporação"` |
| `relatorio_recomendacao_inicial` | string | `"Relatório de recomendação inicial"` |
| `relatorios_sociedade` | string | `"Relatório para a Sociedade"` |
| `consulta_publica` | string | `"Realizada de 26 a 15/01/2024"` |
| `contribuicões_experiencia_opiniao` | string | `"Experiêcia e opinião"` |
| `contribuicões_tecnico_cientificas` | string | `"Técnico e científico"` |
| `analise_final_conitec` | string | `"Favorável à manutenção da incorporação"` |
| `relatorio_recomendacao_final` | string | `"Relatório de recomendação Final"` |
| `decisao_ministerio_da_saude` | string | `"Manutenção da incorporação"` |
| `decisao_ministerio_da_saude_relatorio` | string | `"Relatório com decisão"` |
| `decisao_ministerio_da_saude_portarias` | string | `"Portaria SCTIE/MS nº 9 - Publicada em 29/05/2024"` |
| `notas_tecnicas` | string | `"-"` |
| `despacho` | string | `"-"` |

## `/ciencia-tecnologia/plataformabr-pesquisa-saude`

Pesquisas em saúde financiadas e acompanhadas pelo Decit/SCTIE/MS, com filtros por UF da pesquisa e ano de publicação do edital.

- URL: `https://apidadosabertos.saude.gov.br/ciencia-tecnologia/plataformabr-pesquisa-saude?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"plataformabr_pesquisa_saude": "array[0]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `plataformabr_pesquisa_saude` | array | `[]` |

## `/ciencia-tecnologia/plataformabr-projeto-aprovado`

Projetos de pesquisa aprovados pelo CEP/INAEP via Plataforma Brasil, com filtros por UF proponente, ano do parecer e UF do CEP.

- URL: `https://apidadosabertos.saude.gov.br/ciencia-tecnologia/plataformabr-projeto-aprovado?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"plataformabr_projeto_aprovado": "array[0]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `plataformabr_projeto_aprovado` | array | `[]` |

## `/ouvidoria/ouvidor2`

Manifestações registradas na Ouvidoria, com filtros por UF de origem, UF de destino, esfera da origem e status da manifestação.

- URL: `https://apidadosabertos.saude.gov.br/ouvidoria/ouvidor2?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"ouvidor2": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `data_manifestacao` | string | `"2025-05-12"` |
| `canal_entrada` | string | `"PESSOALMENTE"` |
| `classificacao_manifestacao` | string | `"SOLICITACAO"` |
| `ouvidoria_origem` | string | `"SECRETARIA MUNICIPAL DE SAÚDE DE MONTES CLAROS"` |
| `municipio_ouvidoria_origem` | string | `"MONTES CLAROS"` |
| `uf_ouvidoria_origem` | string | `"MG"` |
| `esfera_ouvidoria_origem` | string | `"MUNICIPAL"` |
| `ouvidoria_destino` | string | `"SECRETARIA MUNICIPAL DE SAÚDE DE MONTES CLAROS"` |
| `municipio_ouvidoria_destino` | string | `"MONTES CLAROS"` |
| `uf_ouvidoria_destino` | string | `"MG"` |
| `esfera_ouvidoria_destino` | string | `"MUNICIPAL"` |
| `status_manifestacao` | string | `"CONCLUIDA"` |
| `assunto` | string | `"ASSISTÊNCIA FARMACÊUTICA"` |
| `subassunto1` | string | `"COMPONENTE ESTRATÉGICO"` |
| `subassunto2` | string | `"COMPONENTE ESTRATÉGICO"` |
| `subassunto3` | string | `"FÁRMACO"` |
| `farmaco` | string | `"DAPAGLIFLOZINA"` |
| `daps` | null \| string | `"CEM - CENTRO DE ESPECIALIDADES MÉDICAS"` |
| `uf_manifestante` | null | `null` |
| `municipio_manifestante` | null | `null` |
| `nivel_ouvidoria_destino` | null | `null` |
| `subassunto4` | null | `null` |
| `subassunto5` | null | `null` |
| `subassunto6` | null | `null` |
| `doenca` | null | `null` |
| `medicamento` | null | `null` |
| `status_problema` | null | `null` |

## `/ouvidoria/ouvidor3`

Manifestações registradas na Ouvidoria com detalhes sobre problemas de saúde, com filtros por canal de entrada, UF e esfera de origem/destino e status.

- URL: `https://apidadosabertos.saude.gov.br/ouvidoria/ouvidor3?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"ouvidor3": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `data_manifestacao` | string | `"2027-07-12"` |
| `canal_entrada` | string | `"INTEGRAÇÃO"` |
| `classificacao_manifestacao` | string | `"RECLAMAÇÃO"` |
| `uf_manifestante` | null \| string | `"MG"` |
| `municipio_manifestante` | null \| string | `"JUIZ DE FORA"` |
| `ouvidoria_origem` | string | `"OUVIDORIA GERAL DO SUS"` |
| `municipio_ouvidoria_origem` | string | `"BRASILIA"` |
| `uf_ouvidoria_origem` | string | `"DF"` |
| `esfera_ouvidoria_origem` | string | `"FEDERAL"` |
| `ouvidoria_destino` | string | `"OUVIDORIA GERAL DO SUS"` |
| `municipio_ouvidoria_destino` | string | `"BRASILIA"` |
| `uf_ouvidoria_destino` | string | `"DF"` |
| `esfera_ouvidoria_destino` | string | `"FEDERAL"` |
| `nivel_ouvidoria_destino` | string | `"OUVIDORIA"` |
| `status_manifestacao` | string | `"CONCLUÍDA"` |
| `assunto` | string | `"ATENÇÃO À SAÚDE"` |
| `subassunto1` | string | `"ASSISTÊNCIA FARMACÊUTICA"` |
| `subassunto2` | null \| string | `"PROGRAMA FARMÁCIA POPULAR DO BRASIL"` |
| `subassunto3` | null \| string | `"COMPRA - DISPENSAÇÃO"` |
| `subassunto4` | null \| string | `"PRODUTOS PARA SAÚDE"` |
| `subassunto5` | null \| string | `"FRALDA GERIÁTRICA"` |
| `subassunto6` | null \| string | `"COLANGIOPANCREATOGRAFIA RETRÓGRADA"` |
| `doenca` | null \| string | `"NÃO INFORMADO"` |
| `medicamento` | null \| string | `"ITRACONAZOL 100 MG CÁPSULA"` |
| `status_problema` | string | `"PRODUTO INDISPONÍVEL"` |

## `/assistencia-a-saude/registro-de-ocupacao-hospitalar-covid-19`

Registro de Ocupação Hospitalar COVID-19

- URL: `https://apidadosabertos.saude.gov.br/assistencia-a-saude/registro-de-ocupacao-hospitalar-covid-19?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"registro_ocupacao_hospitalar_covid19": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `estado` | string | `"Minas Gerais"` |
| `saidasuspeitaobitos` | string | `"0.0"` |
| `saidasuspeitaaltas` | string | `"0.0"` |
| `validado` | string | `"False"` |
| `ocupacaoconfirmadocli` | string | `"0.0"` |
| `ocupacaocovidcli` | null \| string | `"0.0"` |
| `saidaconfirmadaobitos` | string | `"0.0"` |
| `saidaconfirmadaaltas` | string | `"0.0"` |
| `ocupacaoconfirmadouti` | string | `"0.0"` |
| `ocupacaosuspeitouti` | string | `"0.0"` |
| `cnes` | string | `"2796341"` |
| `municipio` | string | `"Paraguaçu"` |
| `ocupacaocoviduti` | null \| string | `"0.0"` |
| `excluido` | string | `"False"` |
| `ocupacaosuspeitocli` | string | `"5.0"` |
| `ocupacaohospitalarcli` | null \| string | `"4.0"` |
| `ocupacaohospitalaruti` | null \| string | `"0.0"` |
| `origem` | string | `"parse-cloud"` |
| `municipionotificacao` | string | `"Paraguaçu"` |
| `estadonotificacao` | string | `"Minas Gerais"` |
| `datanotificacao` | string | `"2021-11-26T03:00:00.000Z"` |

## `/atencao-primaria/cadastro-vinculado-programa-previne-brasil`

Esta base de dados disponibiliza os resultados Cadastro Vinculado do Programa Previne Brasil, que fazia parte do modelo de cofinanciamento federal adotado na Atenção Primária à Saúde a partir da Portaria Nº 2.979, de novembro de 2019.

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/cadastro-vinculado-programa-previne-brasil?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisab_cadastro_vinculado": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `competencia_referencia` | integer | `202301` |
| `sigla_unidade_federacao` | string | `"MG"` |
| `codigo_municipio_ibge` | integer | `312560` |
| `nome_municipio` | string | `"FELISBURGO"` |
| `estimativa_populacional_ibge` | integer | `6489` |
| `tipo_equipe` | integer | `70` |
| `sigla_equipe` | string | `"eSF"` |
| `situacao_equipe` | string | `"homologadas"` |
| `pessoas_vinculadas_criterios_ponderacao` | string | `"Sim"` |
| `pessoas_vinculadas_equipe_municipio` | number | `4349.0` |

## `/atencao-primaria/indicador-desempenho-programa-previne-brasil`

Esta base de dados disponibiliza os resultados dos indicadores de desempenho do Programa Previne Brasil, que faziam parte do modelo de cofinanciamento federal adotado na Atenção Primária à Saúde a partir da Portaria Nº 2.979, de novembro de 2019.

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/indicador-desempenho-programa-previne-brasil?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sisab_indicador_desempenho": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `uf` | string | `"RO"` |
| `municipio` | string | `"ALTA FLORESTA D'OESTE"` |
| `codigo_tipo_indicador` | integer | `10` |
| `numerador` | number | `57.0` |
| `denominador_utilizador` | number | `113.0` |
| `percentual_quadrimestre` | number | `50.0` |
| `visao_equipe` | string | `"homologadas"` |
| `denominador_identificado` | number | `80.0` |
| `denominador_estimado` | number | `113.0` |
| `cadastro` | number | `22423.0` |
| `base_externa` | integer | `108` |
| `populacao` | integer | `21494` |
| `quadrimestre` | string | `"2024Q1"` |
| `codigo_municipio` | integer | `110001` |
| `competencia` | integer | `202404` |
| `percentual` | integer | `71` |

## `/atencao-primaria/pmmb-especialista-relacao-nominal-ativo`

Programa Mais Médicos - Profissional Ativo Especialista

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/pmmb-especialista-relacao-nominal-ativo?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pmmb_especialista_relacao_nominal_ativo": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `co_ibge` | integer | `270430` |
| `co_cnes` | integer | `2720035` |
| `estabelecimento` | string | `"HOSPITAL ESCOLA DR HELVIO AUTO"` |
| `tipo_pratica` | null \| string | `"AMBULATORIAL"` |
| `cota_medico` | string | `"AC"` |
| `faixa_atracao` | string | `"FAIXA 2"` |
| `curso` | string | `"07. COLONOSCOPIA DIAGNÓSTICA E TERAPÊUTICA NO SUS"` |
| `uf` | string | `"AL"` |
| `municipio` | string | `"MACEIO"` |
| `regiao_saude` | string | `"1A REGIAO DE SAUDE"` |
| `nome` | string | `"IGOR LOGETTO CAETITE GOMES"` |
| `sexo` | string | `"HOMENS"` |
| `raca_cor` | string | `"BRANCA"` |
| `crm` | integer | `25023` |
| `dt_inicio_atividade` | string | `"2025-09-22"` |
| `ciclo` | integer | `1` |
| `regiao` | string | `"NORDESTE"` |
| `dt_referencia` | string | `"2026-11-09"` |

## `/atencao-primaria/pmme-instituicoes-formadoras`

Instituições formadoras dos especialistas do PMME

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/pmme-instituicoes-formadoras?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"pmme_instituicoes_formadoras": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `no_especialista` | string | `"ABDON MOREIRA LUSTOSA"` |
| `no_rede_formadora` | string | `"HU-BRASIL"` |
| `no_instituicao_formadora` | string | `"HOSPITAL UNIVERSITÁRIO JÚLIO MARIA BANDEIRA DE MELLO"` |

## `/atencao-primaria/siaps-atendimento-individual`

SIAPS - Modelo de Informação de Atendimento Individual (MIAI)

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/siaps-atendimento-individual?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"siaps_atendimento_individual": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `co_uf_ibge` | integer | `42` |
| `regiao` | string | `"4 - SUL"` |
| `unidade_federativa` | string | `"42 - SC"` |
| `competencia_siaps` | integer | `202512` |
| `regiao_de_saude` | string | `"42006 - MEDIO VALE DO ITAJAI"` |
| `municipio` | string | `"421820"` |
| `raca_cor` | string | `"4 - PARDA"` |
| `sexo` | string | `"1 - FEMININO"` |
| `escolaridade` | string | `"NAO INFORMADO"` |
| `faixa_etaria` | string | `"20 a 39 ANOS"` |
| `capitulo_de_cid_e_ciap2` | string | `"W - GRAVIDEZ PARTO E PLANEAMENTO FAMILIAR"` |
| `categoria_profissional` | string | `"MEDICO"` |
| `nacionalidade` | string | `"1 - BRASILEIRA"` |
| `local_de_atendimento` | string | `"01 - UBS"` |
| `tipo_de_atendimento` | string | `"DEMANDA PROGRAMADA"` |
| `tipo_de_estabelecimento` | string | `" 02 - CENTRO DE SAUDE/UNIDADE BASICA"` |
| `tipo_de_equipe` | string | `"EQUIPE DE SAUDE DA FAMILIA"` |
| `qtd_registros_atendimento` | number | `10.0` |
| `qtd_pessoas_atendidas` | number | `7.0` |

## `/assistencia-a-saude/cnes-equipamentos`

Informações dos equipamentos cadastrados nos estabelecimentos de saúde, incluindo tipo de equipamento, quantidade existente, quantidade em uso e demais características registradas no CNES.

- URL: `https://apidadosabertos.saude.gov.br/assistencia-a-saude/cnes-equipamentos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"cnes_equipamentos": "array[1]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nu_comp` | integer | `200801` |
| `co_ibge` | integer | `522150` |
| `co_cnes` | string | `"2570416"` |
| `no_fantasia` | string | `"CENTER CLINICA IZAURA"` |
| `tp_unidade` | string | `"05 - HOSPITAL GERAL"` |
| `ds_class_estab` | string | `"-"` |
| `no_grupo_nat_jur` | string | `"PRIVADO"` |
| `tp_equipamento` | string | `"5  - MANUTENCAO DA VIDA"` |
| `ds_equipamento` | string | `"58 - Incubadora"` |
| `qt_existente` | integer | `1` |
| `qt_uso` | integer | `1` |
| `disp_sus` | string | `"SIM"` |

## `/assistencia-a-saude/cnes-estabelecimentos`

Informações essenciais sobre unidades ativas/desativadas do CNES, incluindo localização, gestão, natureza jurídica e tipo de estabelecimento.

- URL: `https://apidadosabertos.saude.gov.br/assistencia-a-saude/cnes-estabelecimentos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"cnes_estabelecimentos": "array[3]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nu_comp` | integer | `202308` |
| `co_ibge` | integer | `521975` |
| `co_cnes` | string | `"9902775"` |
| `no_fantasia` | string | `"UNIDADE AMBULATORIAL EXTENSAO HMSAD"` |
| `no_empresarial` | string | `"PREFEITURA MUNICIPAL DE SANTO ANTONIO DO DESCOBERTO"` |
| `nu_cnpj` | null | `null` |
| `nu_cnpj_mantenedora` | null \| string | `"00097857000171"` |
| `tp_gestao` | string | `"MUNICIPAL"` |
| `tp_unidade` | string | `"02 - CENTRO DE SAUDE/UNIDADE BASICA"` |
| `ds_class_estab` | string | `"016 - AMBULATORIO"` |
| `ds_natureza_juridica` | string | `"1244 - MUNICIPIO"` |
| `no_grupo_nat_jur` | string | `"PUBLICO"` |
| `no_logradouro` | string | `"QUADRA 07 LOTE 05 A 10"` |
| `nu_endereco` | string | `"0510"` |
| `ds_complemento` | null \| string | `"ANA BEATRIZ I"` |
| `nu_cep` | string | `"72904212"` |
| `nu_telefone` | null \| string | `"53 33056871"` |
| `ds_email` | null \| string | `"DEGG@IBEST.COM.BR"` |
| `nu_latitude` | number | `-15.946350832905628` |
| `nu_longitude` | number | `-48.298773765563965` |
| `ds_status` | string | `"ATIVO"` |

## `/assistencia-a-saude/cnes-leitos`

Informações dos estabelecimentos com leitos hospitalares, incluindo tipo do leito, quantitativo existente e quantitativo destinado ao SUS.

- URL: `https://apidadosabertos.saude.gov.br/assistencia-a-saude/cnes-leitos?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"cnes_leitos": "array[1]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nu_comp` | integer | `200803` |
| `co_ibge` | integer | `311090` |
| `co_cnes` | string | `"2775921"` |
| `tp_unidade` | string | `"05 - HOSPITAL GERAL"` |
| `ds_class_estab` | string | `"-"` |
| `no_grupo_nat_jur` | string | `"SEM FINS LUCRATIVOS"` |
| `tp_leito` | string | `"1  - ESPEC - CIRURGICO"` |
| `ds_leito` | string | `"03 - CIRURGIA GERAL"` |
| `qt_existente` | integer | `2` |
| `qt_sus` | integer | `2` |

## `/assistencia-a-saude/cnes-profissionais`

Informações dos profissionais e equipes cadastrados nos estabelecimentos de saúde, incluindo ocupação, vínculo, carga horária e composição das equipes registradas no CNES.

- URL: `https://apidadosabertos.saude.gov.br/assistencia-a-saude/cnes-profissionais?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"cnes_profissionais": "array[1]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nu_comp` | integer | `200912` |
| `co_ibge` | integer | `150553` |
| `co_cnes` | string | `"2615746"` |
| `no_fantasia` | string | `"HOSPITAL MUNICIPAL DE PARAUAPEBAS HMP"` |
| `no_razao_social` | string | `"PREFEITURA MUNICIPAL DE PARAUAPEBAS"` |
| `nu_cnpj` | null | `null` |
| `nu_cnpj_mantenedora` | string | `"22980999000115"` |
| `tp_gestao` | string | `"MUNICIPAL"` |
| `no_profissional` | string | `"LOUDES GONCALVES BARBOSA"` |
| `nu_carga_horaria_outro` | integer | `0` |
| `nu_carga_horaria_ambul` | integer | `0` |
| `nu_carga_hor_hosp_sus` | integer | `30` |
| `nu_carga_horaria_total` | integer | `30` |
| `ds_cbo` | string | `"322230 - AUXILIAR DE ENFERMAGEM"` |
| `st_atende_sus` | string | `"SIM"` |
| `co_ind_vinculo` | string | `"010300"` |
| `ds_vinculo` | string | `"VINCULO EMPREGATICIO CONTRATADO TEMPORÁRIO OU POR PRAZO/TEM…` |
| `dt_entrada_equipe` | null | `null` |
| `dt_deslig_equipe` | null | `null` |
| `co_ine` | string | `"-"` |
| `co_area_equipe` | string | `"-"` |
| `no_area_equipe` | string | `"-"` |
| `tp_equipe` | string | `"-"` |
| `ds_subtipo_equipe` | string | `"-"` |
| `dt_ativacao_equipe` | null | `null` |
| `dt_desat_equipe` | null | `null` |

## `/assistencia-a-saude/cnes-servicos-especializados`

Informações dos serviços especializados cadastrados nos estabelecimentos de saúde, incluindo código, descrição, classificação e demais características dos serviços disponibilizados.

- URL: `https://apidadosabertos.saude.gov.br/assistencia-a-saude/cnes-servicos-especializados?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"cnes_servicos_especializados": "array[3]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nu_comp` | integer | `200806` |
| `co_ibge` | integer | `354340` |
| `co_cnes` | string | `"2043548"` |
| `no_fantasia` | string | `"LAB J SABBAG"` |
| `tp_unidade` | string | `"39 - UNIDADE DE APOIO DIAGNOSE E TERAPIA (SADT ISOLADO)"` |
| `ds_class_estab` | string | `"-"` |
| `no_grupo_nat_jur` | string | `"PRIVADO"` |
| `ds_servico` | string | `"145 - SERVICO DE DIAGNOSTICO DE LABORATORIO CLINICO"` |
| `ds_classificacao` | string | `"001 - EXAMES BIOQUIMICOS"` |
| `ds_serv_amb_nao_sus` | string | `"NAO"` |
| `ds_serv_amb_sus` | string | `"SIM"` |
| `ds_serv_hosp_nao_sus` | string | `"NAO"` |
| `ds_serv_hosp_sus` | string | `"NAO"` |
| `tp_servico` | string | `"PROPRIO"` |
| `co_servico` | string | `"145"` |
| `co_classificacao` | string | `"001"` |
| `tp_caracteristica` | string | `"1"` |
| `nu_seq_processo` | integer | `14320` |

## `/assistencia-a-saude/sia-procedimentos-ambulatoriais`

Produção ambulatorial do SUS, contendo procedimentos realizados pelos estabelecimentos de saúde, município, CNES, tipo de estabelecimento, natureza jurídica, complexidade, quantidade produzida e valores aprovados no SIA/SUS.

- URL: `https://apidadosabertos.saude.gov.br/assistencia-a-saude/sia-procedimentos-ambulatoriais?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sia_procedimentos_ambulatoriais": "array[1]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nu_ano` | integer | `2017` |
| `nu_comp` | integer | `201703` |
| `co_ibge` | integer | `432240` |
| `co_cnes` | string | `"2247259"` |
| `no_fantasia` | string | `"ESF 15 HIPICA I E II"` |
| `nu_cnpj_executante` | string | `"88131164000107"` |
| `ds_natureza_juridica` | string | `"1244 - MUNICIPIO"` |
| `ds_grupo_nat_jur` | string | `"PUBLICO"` |
| `ds_procedimento` | string | `"0301040079 - ESCUTA INICIAL / ORIENTAÇÃO (ACOLHIMENTO A DEM…` |
| `ds_complex_procedimento` | string | `"1 - Atenção Básica"` |
| `qt_procedimento` | integer | `354` |
| `nu_valor_procedimento` | number | `0.0` |
| `ds_tp_unidade` | string | `"02 - CENTRO DE SAUDE/UNIDADE BASICA"` |
| `co_pa_proc_id` | string | `"0301040079"` |
| `co_tp_unidade` | string | `"02"` |
| `co_natureza_jur` | string | `"1244"` |
| `co_pa_complexidade` | integer | `1` |

## `/assistencia-a-saude/sih-procedimentos-hospitalares`

Produção hospitalar do SUS, contendo procedimentos realizados nas internações hospitalares, CNES, município, natureza jurídica, financiamento, complexidade, quantidade de AIH e valores aprovados no SIH/SUS.

- URL: `https://apidadosabertos.saude.gov.br/assistencia-a-saude/sih-procedimentos-hospitalares?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"sih_procedimentos_hospitalares": "array[1]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `nu_ano` | integer | `2023` |
| `nu_comp` | integer | `202303` |
| `co_ibge` | integer | `410400` |
| `co_cnes` | string | `"0013633"` |
| `nu_cnpj` | string | `"07088017000191"` |
| `no_fantasia` | string | `"HOSPITAL ANGELINA CARON"` |
| `ds_natureza_juridica` | string | `"3999 - ASSOCIACAO PRIVADA"` |
| `ds_grupo_nat_jur` | string | `"SEM FINS LUCRATIVOS"` |
| `co_ibge_pac` | string | `"410580"` |
| `ds_financiamento` | string | `"06 - Média e Alta Complexidade (MAC)"` |
| `ds_procedimento` | string | `"0410010014 - DRENAGEM DE ABSCESSO DE MAMA"` |
| `ds_complex_procedimento` | string | `"02 - M dia Complexidade"` |
| `qt_procedimento` | integer | `2` |
| `nu_valor_procedimento` | number | `636.86` |
| `co_complexidade` | string | `"02"` |
| `co_financiamento` | string | `"06"` |
| `co_proc_realizado` | string | `"0410010014"` |

## `/atencao-primaria/siaps-cadastro-individual`

SIAPS - Modelo de Informação de Cadastro Individual (MICI)

- URL: `https://apidadosabertos.saude.gov.br/atencao-primaria/siaps-cadastro-individual?limit=100&offset=0`
- HTTP: 200
- Envelope: `{"siaps_cadastro_individual": "array[100]"}`

| Campo | Tipo | Exemplo |
|---|---|---|
| `regiao` | string | `"2 - NORDESTE"` |
| `unidade_federativa` | string | `"23 - CE"` |
| `competencia_siaps` | integer | `202606` |
| `regiao_de_saude` | string | `"23001 - 1ª RS FORTALEZA"` |
| `municipio` | string | `"230630"` |
| `raca_cor` | string | `"1 - BRANCA"` |
| `sexo` | string | `"1 - FEMININO"` |
| `escolaridade` | string | `"SEM ESCOLARIDADE"` |
| `faixa_etaria` | string | `"10 A 19 ANOS"` |
| `nacionalidade` | string | `"1 - BRASILEIRA"` |
| `membro_de_povo_ou_comunidade_tradicional` | string | `"NAO"` |
| `pessoa_em_situacao_de_rua` | string | `"NAO"` |
| `pessoa_com_deficiencia` | string | `"NAO"` |
| `situacao_no_mercado_de_trabalho` | string | `"DESEMPREGADO"` |
| `tipo_de_estabelecimento` | string | `" 02 - CENTRO DE SAUDE/UNIDADE BASICA"` |
| `tipo_de_equipe` | string | `"EQUIPE DE SAUDE DA FAMILIA"` |
| `qtd_pessoas_cadastradas` | number | `1.0` |
