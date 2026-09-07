# Prompt para gerar o painel interativo de viagens

Prompt parametrizado e reutilizável. Ajuste o bloco de parâmetros e cole o texto inteiro em uma sessão nova.

---

## Prompt

Você é um analista de dados de viagens. Sua tarefa é pesquisar tarifas aéreas e hospedagem e entregar um **painel HTML interativo, autocontido e offline**, salvo na pasta do projeto.

### 1. Parâmetros da pesquisa

| Parâmetro | Valor |
|---|---|
| Origem | Brasília (BSB) |
| Duração da viagem | Cerca de 8 noites |
| Horizonte de planejamento | 6 meses a partir de hoje |
| Passageiros | 1 adulto, sem bagagem despachada |
| Moeda | BRL |
| Restrição de dia da semana | Nenhuma. Busque a melhor condição de preço na semana |
| Perfil de hospedagem | Econômica, priorizando nota igual ou superior a 8 quando houver |
| Pasta de saída | `C:\Users\darci\Dropbox\Mine\Viagens` |

Se algum parâmetro estiver ambíguo, pergunte antes de começar a pesquisa.

### 2. Escopo de destinos

Cubra pelo menos 15 destinos nacionais, misturando três perfis:

- **Praia:** Rio de Janeiro, Salvador, Recife, Maceió, Porto Seguro, Ilhéus, João Pessoa, Natal, Fortaleza, Vitória, Florianópolis, Aracaju
- **Cidade:** Belo Horizonte, São Paulo, Curitiba, Porto Alegre, Belém
- **Natureza:** Foz do Iguaçu, Palmas

Não descarte destinos por intuição. Cote primeiro, filtre depois com dados.

### 3. Método de pesquisa

**Passo 1 - Definir períodos.** Escolha de 6 a 8 semanas de referência distribuídas ao longo do horizonte, cobrindo baixa e alta temporada. Registre a antecedência em dias de cada uma.

**Passo 2 - Matriz de tarifas.** Para cada destino e cada período, consulte o Google Voos e registre a tarifa mínima de ida e volta. Use consultas em lote para reduzir o número de idas ao navegador.

**Passo 3 - Varredura diária.** Nos dois períodos mais baratos da matriz, teste **os sete dias da semana** como data de saída, mantendo a duração. Para cada dia registre:

- o piso da tarifa naquele dia;
- **quantos horários de voo diferentes atingem esse piso**.

Este segundo número é o achado central da análise. Na prática o piso muda pouco entre os dias, mas a quantidade de horários disponíveis nesse piso varia bastante, e é isso que determina se dá para viajar em horário conveniente sem pagar a mais.

**Passo 4 - Sinais de preço.** Capture os avisos do Google do tipo "os preços estão baixos no momento, R$ X abaixo do normal" e "é provável que os preços aumentem". Eles entram no painel como selo do destino.

**Passo 5 - Hospedagem.** Para os destinos mais promissores de cada período, levante de 3 a 6 opções com nome, bairro, nota e preço total do período. Registre explicitamente quando não houver cotação, em vez de estimar.

**Passo 6 - Verificação.** Antes de montar o painel, confira: datas e dias da semana batem; nenhum valor foi inventado; destinos sem dado aparecem como lacuna e não como zero.

### 4. Regras de qualidade dos dados

- Toda tarifa deve vir de uma consulta real. Nunca interpole nem estime.
- Diferencie voo direto de voo com conexão e informe a duração total.
- Sinalize itinerários com tempo desproporcional. Uma tarifa 30% menor com 16 horas de viagem e duas conexões deve ser marcada como desvantajosa.
- Onde faltar dado, o painel mostra a lacuna de forma explícita.

### 5. Especificação do painel

Arquivo HTML único, sem dependências externas, com CSS e JavaScript embutidos. Tema claro. Sem uso de `localStorage`.

**Seções, nesta ordem:**

1. **Cabeçalho** com origem, duração, horizonte e perfil do viajante.

2. **Achado principal** em destaque no topo: um bloco curto explicando, em linguagem direta, o que a análise revelou sobre a relação entre dia da semana, mês e preço. Deve ser a primeira coisa que o leitor lê.

3. **Seletor de período**, em cartões clicáveis. Cada cartão traz as datas, a antecedência em dias, o número de destinos cotados e o menor custo do período. O período recomendado recebe um selo.

4. **Indicadores** do período selecionado: menor custo total, passagem mais barata, antecedência e se houve varredura diária.

5. **Matriz de tarifas** com destinos nas linhas e períodos nas colunas. Escala de cor calculada **por linha**, para comparar o mesmo destino ao longo do tempo. Cada célula é clicável e abre o detalhe daquela combinação. Células sem dado ficam em cinza e não são clicáveis. Inclua legenda.

6. **Filtro por perfil** de destino (todos, praia, cidade, natureza).

7. **Grade de dias da semana** do destino selecionado, quando houver varredura diária. Sete cartões com dia, data, piso e quantidade de voos nesse piso. Destaque o dia com mais horários no piso. Quando não houver varredura, exiba um aviso explicando que a tarifa vem da data de referência.

8. **Detalhe do destino** em duas colunas: à esquerda, os horários de voo com preço, marcando quais atingem a tarifa mínima e quais são diretos; à direita, a lista de hospedagem clicável.

9. **Barra de custo total**, atualizada ao clicar em um hotel. Quando não houver hospedagem cotada, mostre apenas a passagem e diga isso.

10. **Tabela de ranking** do período, ordenada por preço, com coluna de horários no piso, clicável para trocar de destino.

11. **Notas contextuais** que mudam conforme o período selecionado: feriados na janela, alertas de preço, sazonalidade.

12. **Rodapé** com fontes, data da coleta e limitações de cobertura.

**Interações obrigatórias:** trocar período, trocar destino pela matriz, pelo filtro ou pela tabela, e trocar hotel recalculando o total. Toda troca atualiza a página inteira de forma consistente.

**Estilo:** paleta sóbria em verde escuro sobre fundo neutro, tipografia de sistema, números com `font-variant-numeric: tabular-nums`, tabelas com cabeçalho fixo na primeira coluna quando houver rolagem horizontal. Sem emojis. Em português do Brasil, sem travessão longo.

### 6. Entrega

1. Salve o HTML na pasta do projeto com sufixo de versão, por exemplo `Painel_Viagens_BSB_v1.html`. Não sobrescreva versões anteriores.
2. Registre o painel como artefato para visualização no aplicativo.
3. Apresente o arquivo ao usuário.
4. No resumo em texto, entregue: o achado principal, de 3 a 5 combinações recomendadas com valores, e as limitações de cobertura. Seja direto e evite repetir o que já está no painel.

---

## Notas de uso

**Para reproduzir o painel atual sem alterações**, use os parâmetros da tabela como estão e informe que a coleta é de 17 de agosto de 2026.

**Para adaptar a outro contexto**, ajuste origem, duração, horizonte e lista de destinos. O método dos passos 1 a 6 e a especificação da seção 5 permanecem válidos.

**Custo de execução.** A varredura completa consome cerca de 90 a 120 consultas ao Google Voos e de 15 a 25 consultas de hospedagem. Para uma versão mais enxuta, reduza para 4 períodos e 10 destinos, e faça a varredura diária em apenas um período.

**Ponto de atenção.** A tentação natural é fixar dia de saída e retorno logo no início. Isso encarece o resultado e esconde o padrão real. Deixe a restrição de dia por último e só aplique se o usuário pedir.
