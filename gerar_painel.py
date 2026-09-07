#!/usr/bin/env python3
"""
Gerador do Painel de Viagens (nacional e internacional).

Não existe uma API de preços de passagens aéreas gratuita e estável
para consumo direto sem contrato comercial (ex.: Amadeus, Skyscanner
Partner API exigem credenciais pagas ou aprovação de parceria). Na
versão original, a pesquisa de preços e destinos era feita por um
assistente de IA (Claude, via Cowork) a partir dos prompts em
PROMPT_nacional.md e PROMPT_internacional.md.

Este script automatiza a parte reprodutível: lê os dados de viagens
(rotas, preços levantados, pontuação por critério) de um arquivo JSON
local e monta o HTML final, no layout do painel publicado neste
repositório. A função `carregar_dados()` é o ponto de extensão: plugue
aqui uma API de passagens com credenciais próprias, ou um arquivo CSV
mantido manualmente (ver historico_precos exemplo).

Uso:
    python gerar_painel.py nacional        # gera na raiz (index.html)
    python gerar_painel.py internacional   # gera em internacional/index.html
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os
import sys

DADOS_PADRAO = {
    "nacional": "dados_nacional.json",
    "internacional": "dados_internacional.json",
}


def carregar_dados(modo: str) -> list[dict]:
    """
    Carrega os destinos/rotas avaliados de um arquivo JSON local.

    Cada item é um dicionário livre, por exemplo:
      {"destino": "Porto Alegre", "origem": "Brasília", "preco": 850,
       "data_ida": "2026-10-06", "pontuacao": 8.5, "observacoes": "..."}

    Ponto de extensão: substitua por uma consulta real a uma API de
    passagens (com suas próprias credenciais) sempre que quiser
    automatizar totalmente a coleta de preços.
    """
    arquivo = DADOS_PADRAO[modo]
    if not os.path.exists(arquivo):
        print(f"[aviso] {arquivo} não encontrado — gerando painel vazio como exemplo.")
        return []
    with open(arquivo, encoding="utf-8") as f:
        return json.load(f)


def render_card(item: dict) -> str:
    destino = html.escape(str(item.get("destino", "")))
    preco = item.get("preco")
    preco_fmt = f"R$ {preco:,.0f}".replace(",", ".") if isinstance(preco, (int, float)) else "—"
    data_ida = html.escape(str(item.get("data_ida", "")))
    pontuacao = item.get("pontuacao", "")
    observacoes = html.escape(str(item.get("observacoes", "")))
    return f"""
      <div class="card">
        <div class="card-title">{destino}</div>
        <div class="card-meta">Ida: {data_ida} — {preco_fmt} — nota {pontuacao}</div>
        <div class="card-summary">{observacoes}</div>
      </div>"""


def montar_html(modo: str, itens: list[dict], data_geracao: str) -> str:
    titulo = "Painel de Viagens Nacionais" if modo == "nacional" else "Painel de Viagens Internacionais"
    cards = "\n".join(render_card(i) for i in itens) or "<p class='muted'>Nenhum destino cadastrado nesta rodada.</p>"
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo} — Darci de Borba</title>
<style>
  :root{{--verde:#1f5c46; --fundo:#f6f5f2; --papel:#ffffff; --borda:#dcd9d2; --texto:#1c1c1a; --suave:#5f5c56;}}
  *{{box-sizing:border-box;}}
  body{{margin:0; background:var(--fundo); color:var(--texto);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; line-height:1.55;}}
  .wrap{{max-width:1180px; margin:0 auto; padding:28px 22px 70px;}}
  h1{{font-size:25px; margin:0 0 6px;}}
  .sub{{color:var(--suave); font-size:0.95rem; margin-bottom:24px;}}
  .grid{{display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:14px;}}
  .card{{background:var(--papel); border:1px solid var(--borda); border-radius:10px; padding:16px;}}
  .card-title{{font-weight:700; margin-bottom:4px;}}
  .card-meta{{font-size:0.82rem; color:var(--suave);}}
  .card-summary{{font-size:0.88rem; margin-top:8px;}}
  .muted{{color:var(--suave);}}
</style>
</head>
<body>
<div class="wrap">
  <h1>{titulo}</h1>
  <div class="sub">Origem: Brasília (BSB) — gerado em {data_geracao}</div>
  <div class="grid">{cards}
  </div>
</div>
</body>
</html>"""


def main() -> None:
    modo = sys.argv[1] if len(sys.argv) > 1 else "nacional"
    if modo not in DADOS_PADRAO:
        print("Uso: python gerar_painel.py [nacional|internacional]")
        sys.exit(1)
    data_geracao = dt.date.today().strftime("%d/%m/%Y")
    itens = carregar_dados(modo)
    pagina = montar_html(modo, itens, data_geracao)
    destino = "index.html" if modo == "nacional" else "internacional/index.html"
    os.makedirs(os.path.dirname(destino) or ".", exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(pagina)
    print(f"{destino} atualizado.")


if __name__ == "__main__":
    main()
