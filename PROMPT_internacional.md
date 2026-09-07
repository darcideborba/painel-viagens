# Prompt para gerar o painel de viagens internacionais

Prompt reutilizável e parametrizado. Os campos entre colchetes devem ser preenchidos antes do uso; os demais podem ser mantidos como estão.

---

## Prompt completo

```
Monte um painel interativo de viagens internacionais em HTML, combinando prazo de
compra e melhores preços, com seleção comentada dos melhores destinos. Destaque os
lugares onde eu possa me comunicar em inglês e destaque se é necessário visto e qual
o grau de dificuldade em obtê-lo.

## 1. Parâmetros da viagem

- Origem: [Brasília (BSB); considere também sair de Guarulhos com conexão doméstica
  comprada em separado, quando isso for mais barato]
- Janela de planejamento: [ano de 2027]
- Duração: [9 noites]
- Viajantes: [1 adulto], classe econômica
- Teto orçamentário: [R$ 12.000 por pessoa, considerando passagem mais hospedagem]
- Perfil: pesquisador em administração pública, transformação digital e governo
  digital, com interesse em visitar universidades, escolas de governo, laboratórios
  de inovação pública, agências de governo digital e organismos internacionais

## 2. Pesquisa a realizar antes de construir o painel

Pesquise na web e colete dados verificáveis, citando as fontes. Organize a pesquisa
em quatro frentes, que podem ser executadas em paralelo por subagentes:

**Frente 1 — Vistos.** Para portador de passaporte comum brasileiro, em viagem de
turismo: regime aplicável (isenção, autorização eletrônica do tipo ETA, eTA, ETIAS,
NZeTA ou K-ETA, visto eletrônico, visa on arrival ou visto consular presencial),
prazo de estada permitido, custo em moeda local e em reais, prazo de emissão,
documentos exigidos e um grau de dificuldade de 1 a 5, em que 1 significa nada a
providenciar além do passaporte e 5 significa entrevista consular, longa espera e
risco real de recusa. Confirme especificamente, com fontes de 2025 ou posteriores, os
pontos que mudaram recentemente: status operacional do ETIAS e do EES na União
Europeia; ETA do Reino Unido; exigência de visto para o México e existência de visto
eletrônico; elegibilidade brasileira ao eTA canadense; custo e fila de entrevista do
visto americano, incluindo eventuais taxas novas; isenção japonesa e exigência de
passaporte biométrico; e exigência de certificado internacional de vacinação contra
febre amarela para quem parte do Brasil. Priorize fontes oficiais: ministérios de
relações exteriores, sites consulares, gov.uk, travel.state.gov, canada.ca e o Portal
Consular do Itamaraty. Advirta quando o Portal Consular estiver desatualizado em
relação à fonte do próprio país.

**Frente 2 — Passagens aéreas.** Faixas de preço de ida e volta em reais, com valor
promocional, mediano e de alta temporada; melhores e piores meses para voar;
companhias que operam a rota, número mínimo de conexões e tempo total de voo desde a
origem; existência de voo direto do Brasil; e antecedência ideal de compra por grupo
de destino. Compare explicitamente o preço saindo da origem contra o preço saindo do
principal hub internacional do país, para identificar em quais rotas compensa comprar
o trecho doméstico em separado. Considere novas rotas anunciadas que possam pressionar
preços no período. Distinga com clareza o que é dado observado do que é estimativa,
e registre que não há inventário aéreo público para o ano-alvo quando for o caso.

**Frente 3 — Custo de solo.** Diária de hotel de padrão médio, de 3 a 4 estrelas, bem
localizado e com nota igual ou superior a 8,0 em plataforma de reserva; total da
hospedagem para a duração definida; custo diário no destino cobrindo alimentação,
transporte urbano e uma atração por dia; índice comparativo de custo de vida, citando
a fonte; temporada mais barata e mais cara; e observação sobre segurança urbana
sempre que for fator material para viajante solo. Informe explicitamente as cotações
de câmbio utilizadas e a data da coleta.

**Frente 4 — Inglês e interesse acadêmico-institucional.** Estatuto do inglês em cada
destino, distinguindo língua oficial ou nativa, língua franca de facto e língua
estrangeira, com a posição e a faixa no EF English Proficiency Index mais recente,
identificando a edição citada. Avalie em uma ou duas frases a viabilidade prática de
circular apenas em inglês em hotel, restaurante, transporte público e museus, e
sinalize quando o índice subestimar ou superestimar a experiência do visitante.
Identifique instituições concretas visitáveis, com nome e site, e conferências
recorrentes relevantes do campo, com nome e mês típico. Registre a posição do país no
UN E-Government Development Index e no OECD Digital Government Index mais recentes.

## 3. Modelo de pontuação

Avalie de 15 a 25 destinos, cobrindo América do Sul, América Central e do Norte,
Caribe, Europa, África, Oriente Médio, Ásia e Oceania. Atribua a cada destino quatro
notas de 0 a 10 e combine-as com os pesos abaixo:

- Custo total da viagem: 30%. Some passagem de ida e volta, hospedagem e custo diário
  multiplicado pelos dias, e normalize linearmente entre o destino mais barato, que
  recebe 10, e o mais caro, que recebe 1.
- Uso do inglês: 25%. Língua oficial ou nativa recebe 10; língua franca de facto com
  interface plenamente anglófona recebe de 8 a 9; língua estrangeira com difusão alta
  recebe de 7 a 8; difusão moderada recebe 5; difusão baixa recebe de 2 a 3.
- Visto: 20%. Converta a dificuldade de 1 a 5 em nota, na escala 1 para 10, 2 para 8,
  3 para 5, 4 para 3 e 5 para 1.
- Interesse acadêmico e institucional: 25%. Pondere densidade de instituições
  visitáveis, presença de organismos internacionais, existência de programa formal de
  visitas técnicas, eventos recorrentes do campo e posição nos índices de governo
  digital.

Mostre a fórmula e as notas parciais no próprio painel, de modo que a pontuação seja
auditável e o leitor possa discordar de um peso específico sem perder o resto.

## 4. Estrutura do painel

Arquivo HTML único e autocontido, em português do Brasil, com todo o CSS e o
JavaScript embutidos e a biblioteca de gráficos incorporada no próprio arquivo, para
funcionar sem conexão. Nenhum uso de localStorage ou sessionStorage. As seções, nesta
ordem:

1. **Cabeçalho** com título, uma frase de método e etiquetas com os parâmetros fixados.
2. **Parâmetros de leitura**: seletor de cenário tarifário, com as opções mediana,
   promocional e alta temporada, que recalcula toda a página; seletor de ordenação por
   pontuação, custo, inglês, visto ou interesse; e três filtros de marcação, para
   mostrar apenas o que cabe no teto, apenas inglês pleno e apenas visto de
   dificuldade 1 ou 2.
3. **Indicadores** em cartões: destinos avaliados, quantos cabem no teto no cenário
   corrente, melhor pontuação, menor custo total, quantos dispensam visto e taxa e
   quantos têm inglês pleno.
4. **Tabela-ranking** com posição, destino e código IATA, passagem, hospedagem, total,
   etiqueta de inglês, etiqueta e círculos de dificuldade de visto, círculos de
   interesse acadêmico e barra de pontuação. Linhas acima do teto ficam esmaecidas e
   recebem marcação. Clicar em uma linha abre a ficha do destino. Inclua nota de
   rodapé explicando a leitura dos círculos.
5. **Gráfico de dispersão** de custo total contra pontuação, com rótulo em cada ponto
   e cores distintas para o que cabe e o que não cabe no teto.
6. **Ficha do destino** em três colunas: composição do custo com totais; prazo e
   sazonalidade, com janela de compra, melhores e piores meses e faixas promocional e
   de alta; uso do inglês com a nota e o texto analítico; visto com regime, custo,
   prazo e texto explicativo; segurança para viajante solo; interesse
   acadêmico-institucional com os dois índices e a lista de instituições; eventos
   recorrentes; e um destaque de ponto de atenção quando houver.
7. **Calendário tarifário** em forma de matriz de destinos por meses, marcando em cor
   de destaque os melhores meses e em cor de alerta os piores, com legenda.
8. **Prazos**: tabela de janela de compra por grupo de destino e linha do tempo de
   providências, do prazo mais longo ao mais curto, sinalizando por cor o que é
   crítico. Comente criticamente as regras genéricas de antecedência de compra
   divulgadas por agregadores internacionais, explicando por que elas não se aplicam
   bem a voos de longo curso partindo do Brasil.
9. **Notas de leitura** em destaques curtos, com os achados que mudam a decisão.
10. **Rodapé** com fontes de preço, fontes de visto, índices utilizados, cotações de
    câmbio, data da coleta e ressalva metodológica sobre o caráter projetivo das
    faixas de preço.

## 5. Padrão visual

Fundo #f7f7f5, cartões brancos com borda #e3e3de e raio de 11 a 14 pixels, tinta
#1a1a18, texto secundário #6b6b66, acento verde #1f5c46 com fundo suave #e8f1ed,
destaque dourado #8a6a1f com fundo #fdf6e6 e alerta #8c2f2f com fundo #fbefef. Fonte
de sistema, corpo de 15 pixels, tabelas de 13,5 pixels, rótulos de seção em maiúsculas
de 11,5 pixels com espaçamento entre letras. Layout de no máximo 1140 pixels de
largura, responsivo, com as grades de duas e três colunas colapsando em uma coluna em
telas estreitas. Números com variante tabular e alinhamento à direita.

## 6. Padrão de redação

Português do Brasil, registro formal, denso e coeso, adequado a relatório técnico.
Não use travessão longo: prefira vírgula, ponto e vírgula ou reestruture a frase.
Evite construções genéricas e o tom de texto gerado automaticamente. Cada afirmação
numérica deve ter origem rastreável até uma das fontes citadas no rodapé. Quando um
dado for estimativa e não observação, diga isso.

## 7. Entregáveis

1. O painel em HTML, autocontido.
2. Um relatório analítico em Markdown que acompanhe o painel, com método, ranking
   completo em tabela, seleção comentada dividida entre primeira linha, segunda linha
   por vantagem específica e destinos a descartar, seção sobre o que mudou em matéria
   de visto, seção sobre prazo de compra e sazonalidade, e a lista de fontes.

Salve os dois arquivos em [C:\Users\darci\Dropbox\Mine\Viagens], usando sufixo de
versão em vez de sobrescrever arquivos existentes, e entregue-os também na conversa.
Antes de finalizar, renderize o HTML em navegador headless, verifique que não há erro
de console, confira a consistência dos totais e capture uma imagem para inspeção
visual.
```

---

## Observações de uso

**Sobre o teto orçamentário.** O corte por teto é o parâmetro que mais altera o
resultado. Com teto baixo, o modelo empurra a seleção para África, Ásia de custo baixo
e Caribe alcançável por hub próximo; com teto alto, Europa Ocidental e América do
Norte voltam a competir. Convém rodar o painel duas vezes, com tetos distintos, quando
a decisão orçamentária ainda estiver aberta.

**Sobre os pesos.** Os pesos de 30, 25, 20 e 25 refletem uma preferência específica.
Quem privilegiar preço acima de tudo deve elevar o custo para 45% e reduzir o interesse
acadêmico para 10%; quem estiver planejando missão técnica deve fazer o inverso. Como
o painel exibe as notas parciais, é possível recalcular manualmente sem regerar o
arquivo.

**Sobre a validade temporal.** Regras de visto e faixas tarifárias envelhecem rápido.
O bloco da frente 1 lista explicitamente os pontos que mudaram entre 2024 e 2026;
essa lista precisa ser revista a cada nova execução, substituindo-se os itens já
resolvidos pelos que estiverem em transição no momento.

**Adaptações fáceis.** O mesmo prompt serve para viagens nacionais, bastando remover
as frentes de visto e de inglês e substituir o interesse acadêmico por outro critério;
para viagens em família, ajustando duração, número de viajantes e acrescentando
documentação de menores; e para seleção de destinos de missão institucional,
elevando o peso do interesse acadêmico e acrescentando uma frente de pesquisa sobre
calendário de eventos com datas confirmadas.
