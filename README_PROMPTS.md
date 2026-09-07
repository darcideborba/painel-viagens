# Sobre os prompts deste painel

Diferente dos demais painéis, para viagens já existiam os prompts originais salvos por Darci de Borba (arquivos `Prompt_Painel_Viagens.md` e `Prompt_Painel_Viagens_Internacionais_v1.md`, na pasta Dropbox/Mine/Viagens), reproduzidos aqui sem alteração como `PROMPT_nacional.md` e `PROMPT_internacional.md`.

Não havia script Python/R salvo para este painel: a coleta de preços e a montagem do HTML eram feitas diretamente pelo assistente de IA (Claude, via Cowork), a partir desses prompts. O script `gerar_painel.py` neste repositório automatiza a parte de templating; a função de busca de preços é um ponto de extensão (ver comentários no script), já que não há uma API de preços de passagens gratuita e estável para uso direto.
