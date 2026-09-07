# Painel de Viagens

Painéis em HTML autocontido para planejamento de viagens, com ranking, filtros e ficha por destino, partindo de Brasília (BSB).

- `nacional/index.html` — painel semanal de viagens nacionais (referência: rota POA-BSB).
- `internacional/index.html` — painel de viagens internacionais de longo prazo, cruzando critérios como idioma, facilidade de visto e interesse acadêmico/institucional em governo digital e administração pública.

Gerado com o apoio do Claude (Anthropic), a partir de preferências e critérios de [Darci de Borba](https://www.darcideborba.com.br).

## Visualizar

Abra os arquivos `index.html` de cada subpasta, ou acesse via GitHub Pages (quando habilitado):

- `https://darcideborba.github.io/painel-viagens/` (painel nacional, na raiz)
- `https://darcideborba.github.io/painel-viagens/internacional/`

## Código-fonte e prompts

- `gerar_painel.py` — script Python que monta o HTML a partir de `dados_nacional.json`/`dados_internacional.json`.
- `PROMPT_nacional.md` e `PROMPT_internacional.md` — prompts originais de IA usados para cada painel (ver `README_PROMPTS.md`).

## Licença

Código sob licença MIT (veja `LICENSE`). Preços e disponibilidades são apenas ilustrativos, referentes à data de geração do painel.
