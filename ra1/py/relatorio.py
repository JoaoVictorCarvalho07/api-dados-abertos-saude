from config import PASTA_SAIDAS


def tabela(df):
    return df.to_markdown(index=False)


def salvar(nome_arquivo, titulo, secoes):
    PASTA_SAIDAS.mkdir(parents=True, exist_ok=True)
    partes = [f"# {titulo}", ""]
    for subtitulo, conteudo in secoes:
        partes += [f"## {subtitulo}", "", conteudo, ""]
    destino = PASTA_SAIDAS / nome_arquivo
    destino.write_text("\n".join(partes), encoding="utf-8")
    return destino
