# Revisão de usabilidade do planejador — 23/10/2026

Escopo exclusivo do planejador. Os arquivos e o comportamento dos painéis gerencial/comercial não foram modificados. A integração descrita em AVALIACAO.md continua sendo uma proposta para outro projeto.

## Alterações

- Um card abre a filha indicada, com número fixo na ficha. Cadastro compartilhado fica claramente separado dos campos individuais. A visão de grupo permanece disponível e mantém as principais de cada coluna.
- Busca, status e agenda verificam cada filha, em conjunto. A grade informa as OSs correspondentes e mantém a projeção principal; fases/calendário exibem somente as filhas correspondentes.
- A confirmação registra data informada, momento da operação, nome local do planejador, revisão e conteúdo conferido. Edições posteriores preservam a data e exibem “Alterado”. Confirmações antigas sem conteúdo registrado são identificadas como anteriores. O nome informado não representa autenticação.
- Replicação exige confirmação e não copia a conferência. Pedidos múltiplos continuam com datas e observações próprias. A matriz permite marcar e conferir várias OSs.
- OSs sem status ou sem fase cadastrada aparecem em “Sem status / A definir”. Arraste dentro da fase ordena a OS individual, sem alterar Status; ↑/↓ oferece alternativa de teclado/clique.
- A seleção é limpa quando muda a carteira, o filtro, a ordem, a rotina ou a visão. Comandos de linha atuam apenas nos registros visíveis.
- Larguras ajustáveis no cabeçalho, por arraste ou setas quando o separador está focado. Componente e OS podem ficar fixos durante a rolagem horizontal.
- Densidades Compacta/Confortável, texto limitado a uma/duas linhas e conteúdo integral no editor e no título. Mantidos clique único, sugestões, texto livre, Ctrl C/V, Ctrl D, desfazer/refazer e edição em lote por coluna selecionada.
- Matriz expandida utiliza a rolagem horizontal da grade, conservando identificação fixa por OS. No diálogo, a ficha dispõe de rolagem própria.
- Cards compactos priorizam a próxima ação, com responsável e prazo separados. Calendário diferencia ação, verificação, conclusão/PR e peças por rótulo, símbolo e cor; a data do evento aparece explicitamente.
- Rotina, visão, carteira, densidade, larguras e fixação são retomadas e seguem no backup JSON. Referência e demais datas usam apresentação brasileira.
- Ajuda e rodapé atualizados para a interação atual.

## Validação

`python3 build.py`, `node --check combined.js` e `node test-planner.cjs`.

50 verificações de comportamento passaram, incluindo contexto por filha, filtros correlacionados, confirmação e alterações posteriores, seleção oculta, arquivamento/desfazer, ordenação individual sem alteração de status, pedidos, calendário, colagem de bloco, edição em lote, restauração JSON e quarentena. Outros 359 manipuladores gerados foram verificados quanto à sintaxe. A verificação remota de interface é registrada após a publicação.

## Limites mantidos

Armazenamento local no navegador e backup JSON. Sem autenticação, concorrência entre pessoas, consulta online ao SAP/PartsVis ou sincronização com o gerencial. Dados de demonstração exclusivamente fictícios. Quarentena preserva os dados após sinalizar o vencimento dos 50 dias.
