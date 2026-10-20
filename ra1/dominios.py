UF_POR_CODIGO = {
    "11": "RO", "12": "AC", "13": "AM", "14": "RR", "15": "PA", "16": "AP", "17": "TO",
    "21": "MA", "22": "PI", "23": "CE", "24": "RN", "25": "PB", "26": "PE", "27": "AL", "28": "SE", "29": "BA",
    "31": "MG", "32": "ES", "33": "RJ", "35": "SP",
    "41": "PR", "42": "SC", "43": "RS",
    "50": "MS", "51": "MT", "52": "GO", "53": "DF",
}

REGIAO_POR_PRIMEIRO_DIGITO = {
    "1": "Norte",
    "2": "Nordeste",
    "3": "Sudeste",
    "4": "Sul",
    "5": "Centro-Oeste",
}

CLASSIFICACAO_FINAL = {
    "5": "Descartado",
    "8": "Inconclusivo",
    "10": "Dengue",
    "11": "Dengue com sinais de alarme",
    "12": "Dengue grave",
    "13": "Chikungunya",
}
CLASSIFICACOES_COM_GRAVIDADE = {"10", "11", "12"}
CLASSIFICACOES_GRAVES = {"11", "12"}

CRITERIO_CONFIRMACAO = {
    "1": "Laboratorial",
    "2": "Clínico-epidemiológico",
    "3": "Em investigação",
}

EVOLUCAO = {
    "1": "Cura",
    "2": "Óbito pelo agravo",
    "3": "Óbito por outras causas",
    "4": "Óbito em investigação",
    "9": "Ignorado",
}

SEXO = {"M": "Masculino", "F": "Feminino", "I": "Ignorado"}

SIM_NAO_IGNORADO = {"1": True, "2": False}
CODIGOS_SIM_NAO_IGNORADO = {"1", "2", "9"}

GESTANTE_EM_GESTACAO = {"1", "2", "3", "4"}

UNIDADE_IDADE_EM_ANOS = {"1": 1 / (24 * 365), "2": 1 / 365, "3": 1 / 12, "4": 1}

FAIXAS_ETARIAS = [0, 5, 15, 30, 45, 60, 75, 121]
ROTULOS_FAIXAS_ETARIAS = ["0-4", "5-14", "15-29", "30-44", "45-59", "60-74", "75+"]
