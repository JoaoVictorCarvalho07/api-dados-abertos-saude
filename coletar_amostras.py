import json
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE_URL = "https://apidadosabertos.saude.gov.br"
SPEC_URL = f"{BASE_URL}/static/swagger.json"
PASTA = Path(__file__).parent
PASTA_AMOSTRAS = PASTA / "amostras"
TIMEOUT = 180
TENTATIVAS = 3
PARAMETROS_OBRIGATORIOS = {"/economia-da-saude/bps": {"codigoCatmat": "267512"}}


def baixar_json(url):
    ultimo_erro = None
    for tentativa in range(TENTATIVAS):
        inicio = time.time()
        try:
            with urllib.request.urlopen(url, timeout=TIMEOUT) as resposta:
                corpo = resposta.read().decode("utf-8")
                return resposta.status, json.loads(corpo), time.time() - inicio
        except urllib.error.HTTPError as erro:
            corpo = erro.read().decode("utf-8", errors="replace")[:500]
            if erro.code < 500:
                return erro.code, {"erro": corpo}, time.time() - inicio
            ultimo_erro = (erro.code, {"erro": corpo}, time.time() - inicio)
        except Exception as erro:
            ultimo_erro = (None, {"erro": repr(erro)}, time.time() - inicio)
        time.sleep(2 * (tentativa + 1))
    return ultimo_erro


def query_padrao(caminho, parametros):
    pares = [f"{k}={v}" for k, v in PARAMETROS_OBRIGATORIOS.get(caminho, {}).items()]
    for p in parametros:
        if p.get("in") != "query":
            continue
        padrao = p.get("default", p.get("schema", {}).get("default"))
        if padrao is not None:
            pares.append(f"{p['name']}={padrao}")
    return "&".join(pares)


def slug(caminho):
    return re.sub(r"[^a-z0-9]+", "_", caminho.lower()).strip("_")


def primeira_lista(dado):
    if isinstance(dado, list):
        return dado
    if isinstance(dado, dict):
        for valor in dado.values():
            if isinstance(valor, list):
                return valor
    return []


def resolver_path_params(caminho, amostras):
    faltantes = re.findall(r"\{(\w+)\}", caminho)
    if not faltantes:
        return caminho
    pai = caminho.rsplit("/{", 1)[0]
    registros = primeira_lista(amostras.get(pai, {}).get("resposta"))
    for nome in faltantes:
        valor = next((r[nome] for r in registros if isinstance(r, dict) and r.get(nome) not in (None, "")), None)
        if valor is None:
            return None
        caminho = caminho.replace("{" + nome + "}", str(valor))
    return caminho


def coletar(caminho, parametros, amostras):
    concreto = resolver_path_params(caminho, amostras)
    if concreto is None:
        return caminho, {"url": None, "status": None, "resposta": {"erro": "sem valor para parametro de path"}}
    query = query_padrao(caminho, parametros)
    url = f"{BASE_URL}{concreto}" + (f"?{query}" if query else "")
    status, resposta, duracao = baixar_json(url)
    print(f"{status} {duracao:6.1f}s {caminho}", flush=True)
    return caminho, {"url": url, "status": status, "segundos": round(duracao, 1), "resposta": resposta}


def tipo(valor):
    if valor is None:
        return "null"
    if isinstance(valor, bool):
        return "boolean"
    if isinstance(valor, int):
        return "integer"
    if isinstance(valor, float):
        return "number"
    if isinstance(valor, str):
        return "string"
    if isinstance(valor, list):
        return "array"
    return "object"


def esquema_registros(registros):
    campos = {}
    for registro in registros:
        if not isinstance(registro, dict):
            continue
        for chave, valor in registro.items():
            info = campos.setdefault(chave, {"tipos": set(), "exemplo": None})
            info["tipos"].add(tipo(valor))
            if info["exemplo"] in (None, "") and valor not in (None, ""):
                info["exemplo"] = valor
    return campos


def envelope(resposta):
    if isinstance(resposta, dict):
        return {k: (f"array[{len(v)}]" if isinstance(v, list) else v) for k, v in resposta.items()}
    return f"array[{len(resposta)}]" if isinstance(resposta, list) else tipo(resposta)


def escrever_resumo(amostras, spec):
    linhas = ["# Formato das respostas — API de Dados Abertos do Ministério da Saúde", ""]
    linhas.append(f"Fonte: {BASE_URL}/v1/ · spec: {SPEC_URL} · coletado em {time.strftime('%Y-%m-%d %H:%M')}")
    linhas.append("")
    vazias = [c for c, d in amostras.items() if d["status"] == 200 and "{" not in c and not primeira_lista(d["resposta"])]
    if vazias:
        linhas += ["Rotas que respondem 200 com lista vazia (sem dado publicado, formato do registro desconhecido):", ""]
        linhas += [f"- `{c}`" for c in vazias] + [""]
    if PARAMETROS_OBRIGATORIOS:
        linhas += ["Rotas que exigem filtro, chamadas com um valor fixo:", ""]
        linhas += [f"- `{c}`: `{p}`" for c, p in PARAMETROS_OBRIGATORIOS.items()] + [""]
    linhas.append("| Rota | HTTP | Registros | Segundos |")
    linhas.append("|---|---|---|---|")
    for caminho, dado in amostras.items():
        n = len(primeira_lista(dado["resposta"])) if dado["status"] == 200 else "-"
        linhas.append(f"| `{caminho}` | {dado['status']} | {n} | {dado.get('segundos', '-')} |")
    linhas.append("")
    for caminho, dado in amostras.items():
        resumo = spec["paths"][caminho]["get"].get("summary") or spec["paths"][caminho]["get"].get("description") or ""
        linhas += [f"## `{caminho}`", "", resumo.strip(), "", f"- URL: `{dado['url']}`", f"- HTTP: {dado['status']}"]
        if dado["status"] != 200:
            linhas += [f"- Erro: `{str(dado['resposta'].get('erro', ''))[:300]}`", ""]
            continue
        linhas.append(f"- Envelope: `{json.dumps(envelope(dado['resposta']), ensure_ascii=False)}`")
        registros = primeira_lista(dado["resposta"])
        if not registros and isinstance(dado["resposta"], dict):
            registros = [dado["resposta"]]
        linhas += ["", "| Campo | Tipo | Exemplo |", "|---|---|---|"]
        for campo, info in esquema_registros(registros).items():
            exemplo = json.dumps(info["exemplo"], ensure_ascii=False)
            exemplo = (exemplo[:60] + "…") if len(exemplo) > 60 else exemplo
            exemplo = exemplo.replace("|", "\\|")
            tipos = " \\| ".join(sorted(info["tipos"]))
            linhas.append(f"| `{campo}` | {tipos} | `{exemplo}` |")
        linhas.append("")
    (PASTA / "FORMATOS.md").write_text("\n".join(linhas), encoding="utf-8")


def main():
    _, spec, _ = baixar_json(SPEC_URL)
    (PASTA / "swagger.json").write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
    PASTA_AMOSTRAS.mkdir(exist_ok=True)

    rotas = [(c, m["get"].get("parameters", []) + m.get("parameters", [])) for c, m in spec["paths"].items() if "get" in m]
    diretas = [r for r in rotas if "{" not in r[0]]
    com_path = [r for r in rotas if "{" in r[0]]

    amostras = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        for caminho, dado in pool.map(lambda r: coletar(r[0], r[1], amostras), diretas):
            amostras[caminho] = dado
    for caminho, parametros in com_path:
        amostras[caminho] = coletar(caminho, parametros, amostras)[1]

    amostras = {c: amostras[c] for c, _ in rotas}
    for caminho, dado in amostras.items():
        (PASTA_AMOSTRAS / f"{slug(caminho)}.json").write_text(json.dumps(dado, ensure_ascii=False, indent=2), encoding="utf-8")
    escrever_resumo(amostras, spec)

    ok = sum(1 for d in amostras.values() if d["status"] == 200)
    print(f"\n{ok}/{len(amostras)} rotas com HTTP 200")


if __name__ == "__main__":
    main()
