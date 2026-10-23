> Atualização de 23/10/2026: os achados abaixo retratam a primeira auditoria. As correções do planejador e suas validações estão em [CORRECOES_PLANEJADOR.md](CORRECOES_PLANEJADOR.md). A integração com o gerencial/comercial continua como proposta, sem implementação.

# Avaliação do planejador e integração com os painéis de OS

**Data:** 23/10/2026. **Ambiente:** navegador remoto Chrome, com dados exclusivamente fictícios.

## 1. Resultado da avaliação

A grade é uma boa base para a rotina do planejador. A digitação contínua, as sugestões, a colagem de blocos, os pedidos múltiplos, a matriz por OS e os comandos de movimentação responderam nos cenários executados. O cabeçalho compacto e a expansão da tabela melhoraram o aproveitamento da tela.

**Minha recomendação é manter a grade como tela principal e corrigir a coerência entre agrupamento, filtros, cards e confirmação antes de conectar o planejador à atualização oficial do gerencial.** Os problemas mais importantes encontrados estão nesses vínculos, e não na aparência dos botões.

A demonstração foi publicada no mesmo repositório dos outros painéis:

- [Mesa do planejador](https://ticgabriel.github.io/painel-demo/planner-demo/).
- [Painel gerencial](https://ticgabriel.github.io/painel-demo/gerencial.html).
- [Painel comercial](https://ticgabriel.github.io/painel-demo/comercial.html).
- [Código da demonstração](https://github.com/Ticgabriel/painel-demo/tree/main/planner-demo).

O teste não implantou sincronização entre os três aplicativos. As alterações feitas no planejador durante a avaliação ficaram no rascunho e nos arquivos sintéticos da sessão, sem atualizar automaticamente o gerencial ou o comercial.

## 2. Dados e método

A base inicial do planejador tem **48 atendimentos e 112 OSs**, com três vendedores e doze clientes fictícios. Inclui linhas com uma, duas ou quatro OSs, pedidos com previsões diferentes, confirmações antigas e vazias, prazos vencidos, observações extensas, registros arquivados e OSs em quarentena. Durante os testes foram criadas linhas e OSs adicionais.

Os registros foram produzidos por um gerador independente, a partir de listas de nomes genéricos, fórmulas numéricas e uma data fixa de demonstração. A geração dos dois JSONs foi repetida e os arquivos coincidiram byte a byte. Uma auditoria verificou os arquivos adicionados ao repositório e não encontrou os nomes de carteiras nem os números completos de OS da base real de referência. O gerador e os hashes dos arquivos estão no projeto.

Nenhuma planilha de trabalho ou JSON real foi incluído no projeto publicado. Os painéis gerencial e comercial já existentes no repositório também se apresentam como demonstrações fictícias; seus arquivos foram consultados para entender o contrato de dados.

Foram usados três tipos de evidência, identificados ao longo deste relatório:

1. **Navegador:** interação real com os controles e inspeção da tela e dos valores apresentados.
2. **Código:** leitura da implementação para explicar comportamentos ou identificar lacunas.
3. **Teste do núcleo de integração:** execução das funções de conciliação e publicação do gerencial com uma resposta fictícia mapeada. Isso não equivale à importação de ponta a ponta pela interface.

A avaliação visual foi feita na janela disponível do navegador remoto, aproximadamente 1.360 × 940 pixels. Não houve validação em celular, leitor de tela ou em diferentes versões de Edge/Chrome. Não foi realizado teste de carga com uma carteira grande no planejador.

## 3. Cobertura funcional

| Área | O que foi executado | Resultado e limite |
|---|---|---|
| Abertura | Abertura da página hospedada e retomada após recarregar | Funcionou; o texto alterado e a rotina criada permaneceram disponíveis. |
| Carteiras | Seleção de vendedor e depois cliente | Funcionou; a seleção foi reduzida de 45 atendimentos ativos para 15 e depois 4. As contagens são de atendimentos, não de OSs. |
| Digitação | Clique único, digitação sequencial de texto completo e Enter | Funcionou. A edição não encerrou após a primeira letra. |
| Sugestões | Digitação parcial, lista automática, seta para baixo e Enter | Funcionou no campo Situação operacional. A escolha permaneceu no campo. |
| Texto livre | Novo texto de componente e observações de pedido | Funcionou. |
| Desfazer/refazer | Alteração de componente e recuperação do valor anterior | Funcionou nos dois sentidos. |
| Seleção de bloco | Duas células de Responsável por Shift + clique | Funcionou; o intervalo foi identificado como 2 × 1. |
| Edição em lote | Abertura do editor a partir do intervalo, escolha de sugestão e aplicação | Identificou Responsável sem exigir nova escolha da coluna; alterou as duas OSs principais correspondentes. |
| Copiar/colar células | Ctrl C sobre o bloco, leitura do texto e Ctrl V com um novo valor | Funcionou; a cópia continha as duas linhas e a colagem preencheu ambas. Não foi usado Excel instalado. |
| Colar tabela | Texto tabulado com cabeçalhos, cliente, vendedor, data e duas OSs | Funcionou; adicionou um atendimento. Os valores operacionais ficaram na primeira OS, com a outra disponível para revisão/replicação. |
| OSs vinculadas | Digitação de `800000101/02/03` e expansão da matriz | Funcionou; a nova OS apareceu com campos independentes e vazios. |
| Matriz | Consulta de três OSs em ordem crescente | Funcionou; preservou os valores distintos. |
| Replicação | Responsável da OS 01 para as OSs 02 e 03 | Funcionou após confirmação. Os três responsáveis passaram a Comercial. A variante de todos os campos não foi executada no navegador. |
| Principal por campo | Escolha da OS 02 para Situação operacional | Funcionou; a grade passou a mostrar o valor da OS 02, sem copiar esse valor às demais. |
| Pedidos de peças | Adição de segundo pedido com número, previsão abreviada e observação | Funcionou; o pedido original e sua previsão foram preservados. |
| Datas | Digitação `301026` e confirmação | Foi exibido `30/10/26`. |
| Calendário de campo | Clique direto no ícone de Prazo da ação | O seletor de data abriu. Não foi exigido duplo clique prévio. |
| Última confirmação | Clique em ✓ Hoje em duas linhas | Atualizou a confirmação. Na medição realizada, a rolagem horizontal ficou em 736 pixels antes e depois. |
| Tabela expandida | Expansão, abertura da ficha e retorno ao modo normal | Funcionou. A ficha apareceu acima da tabela expandida. |
| Cards | Alternância para cards mantendo a carteira selecionada | Funcionou; apresentou os quatro atendimentos filtrados em cards baixos. |
| Quadro por fases | Distribuição de cards por OS | Funcionou, mas revelou os problemas de contexto e de status vazio descritos adiante. |
| Arraste | Tentativa de reordenar cards na mesma fase | A ordem não mudou na tentativa realizada. O arraste permanece sem validação conclusiva; os botões de mover linhas funcionaram. |
| Calendário mensal | Consulta de outubro e novembro, contagens e clique em um dia | Funcionou. No dia testado, distinguiu 3 compromissos de 2 atendimentos e mostrou ação e previsão de peças separadamente. |
| Calendário semanal | Alternância a partir do dia selecionado | Funcionou; exibiu a semana correspondente. |
| Reprovação | Cancelamento e depois confirmação para uma OS agrupada | Cancelar manteve o status anterior. Confirmar retirou somente a OS 01; as OSs 02 e 03 continuaram ativas. |
| Restauração | Consulta da quarentena, escolha de status e retorno | Funcionou; a OS voltou ao mesmo agrupamento, com seus pedidos. |
| Coluna personalizada | Criação de Prioridade local DEMO e inclusão na rotina | Funcionou. |
| Rotina personalizada | Nomeação, salvamento, abertura do backup e nova seleção da rotina | A definição e a coluna foram recuperadas. A rotina selecionada não é retomada automaticamente após recarregar a página. |
| Cadastro de clientes | Inclusão de dois nomes sintéticos por texto colado | O aplicativo confirmou o carregamento. O carregamento por arquivo CSV não foi executado. |
| Fases configuráveis | Abertura da configuração e inspeção de rótulos e seletores | A grade de configuração ficou alinhada. Não foi aplicada uma nova correspondência entre status e fases. |
| Linhas | Criar, copiar, colar, mover e arquivar | Funcionou nos cenários executados. |
| Exclusão | Excluir uma linha e desfazer | A contagem caiu de 47 para 46 linhas visíveis e voltou a 47 ao desfazer. |
| Backup | Salvar JSON, baixar e reabrir o arquivo gerado | Funcionou pelo download alternativo. O navegador remoto não gravou diretamente pelo seletor de arquivo. O JSON reaberto tinha 50 registros, coluna e rotina personalizadas. |
| Exportação | Exportar a tabela filtrada | Foi gerado um TSV. Não houve conferência em Excel instalado. |
| Indicadores | Abertura dos indicadores da seleção | Mostrou contagem, ações vencidas, verificações e registros sem agenda; o significado continua sendo por atendimento/valor principal. |
| Outros painéis | Abertura do gerencial/comercial e busca de OSs sintéticas correspondentes | Funcionou. As alterações do planejador não apareceram automaticamente na publicação comercial. |

Não considero esse quadro uma aprovação de todas as combinações possíveis. Permanecem pendentes, entre outros, arraste conclusivo, replicação de todos os campos, concorrência real entre usuários, limpeza de armazenamento, importações inválidas extensas e uso em diferentes dispositivos.

## 4. Problemas e melhorias priorizadas

**P1:** corrigir antes de usar o controle como fonte oficial de atualização. **P2:** corrigir para tornar a rotina consistente. **P3:** acabamento e facilidade de aprendizado.

| Prioridade | Constatação | Evidência | Impacto | Alteração recomendada |
|---|---|---|---|---|
| P1 | O card de uma OS abre a ficha do atendimento com as referências principais de cada campo, que podem pertencer a outras OSs. | Navegador: ao abrir o card da OS 800000101, Situação operacional apareceu como “Edita OS 800000102”, enquanto Responsável editava a OS 800000101. | O planejador pode atualizar uma OS diferente daquela que acabou de selecionar. | Abrir a ficha no contexto explícito da OS clicada. Exibir seu número de forma fixa no topo. A visão agregada deve ter um comando próprio. |
| P1 | O filtro de status considera o valor principal do atendimento. | Navegador: na carteira do Cliente Demonstração 002, o quadro tinha filhas em Negociação, mas o filtro Negociação da grade retornou nenhum registro. | OSs secundárias ficam invisíveis para o filtro. O calendário herda esse recorte e também pode ocultar compromissos. | Avaliar o filtro em todas as OSs do grupo. Manter o atendimento visível e destacar as OSs correspondentes; oferecer opção de “somente principal” se necessário. |
| P1 | A confirmação atual não identifica, de maneira suficiente para integração, a pessoa que confirmou e a versão do conteúdo confirmado. | Código e contrato do gerencial: o planejador guarda a data; o gerencial exige `by` e trata revisão/etapa da base. | Uma alteração posterior pode viajar com uma confirmação antiga sem indicar claramente que o conteúdo mudou. | Adicionar identidade do planejador, revisão por OS e revisão/hash do conteúdo confirmado. Continuar permitindo editar sem renovar a data, mas distinguir rascunho de conteúdo confirmado. |
| P1 | Não existe ainda um contrato de atualização compatível entre os aplicativos. | Código e teste do núcleo: o backup do planejador tem estrutura diferente; o importador atual recebe respostas XLSX com metadados de rodada. | O backup não pode ser tratado como resposta pronta para o gerencial. | Criar exportação/importação de atualizações com contexto de rodada, catálogo, revisões e prévia de conflitos. |
| P2 | OS sem status aparece em Notificação. | Navegador: a OS 03 recém-adicionada, vazia, apareceu na primeira fase. | O quadro comunica uma fase que não foi informada. | Criar “Sem status / A definir”, fora das fases operacionais. |
| P2 | Uma seleção pode permanecer referindo-se a uma linha que acabou de ser arquivada. | Navegador: após arquivar, o contador ainda indicava uma linha selecionada, embora ela tivesse saído da grade ativa. | Comandos posteriores podem agir sobre um registro fora do contexto visível. | Limpar a seleção ao retirar linhas da visão ou indicar explicitamente os selecionados ocultos. |
| P2 | Textos se quebram em colunas estreitas e elevam muito as linhas. | Inspeção visual: componente, vendedor e cliente ocuparam várias linhas; em torno de nove atendimentos cabiam na área inicial. | Menor densidade e leitura mais lenta. | Larguras mínimas coerentes, limites de uma ou duas linhas, texto integral ao focar e ajuste manual persistente da largura. |
| P2 | A rolagem horizontal faz o usuário perder a identificação do atendimento. | Inspeção visual da grade nas colunas de prazo/confirmação; somente a numeração permanece fixa. | Fica mais difícil saber qual componente/OS está sendo atualizado. | Fixar Componente e OS, com possibilidade de escolher colunas fixas por rotina. Ocultar Vendedor/Cliente nas rotinas em que os filtros já tornam essa informação redundante. |
| P2 | A matriz combina rolagem interna com a rolagem da tabela. | Inspeção visual da expansão. | O usuário precisa controlar duas barras horizontais e percorrer campos distantes. | Sincronizar a posição das colunas ou oferecer uma matriz focada, com cabeçalho e número da OS fixos e seleção de campos por rotina. |
| P2 | Cards são compactos, mas truncam próximo passo e responsável; os tipos de evento do calendário têm pouca diferenciação visual. | Navegador e inspeção visual. | Uma ação longa perde informação; previsão de peças e tarefa exigem mais leitura para serem distinguidas. | Priorizar próxima ação e prazo no card; detalhe curto ao focar. Usar rótulos/ícones e cores discretas por tipo de evento, com legenda. |
| P2 | A preferência de rotina selecionada não é retomada automaticamente. | Recarregamento: a definição personalizada sobreviveu, mas a visualização voltou à rotina padrão. | Repetição de ajustes ao abrir o controle. | Salvar a rotina ativa e preferências de apresentação junto à navegação. |
| P2 | Reordenação por arraste ainda não está demonstrada como confiável. | A tentativa remota não mudou a ordem. | Um comando anunciado pode não responder como o usuário espera. | Reproduzir com indicadores visuais de arraste e destino. Verificar também cards de filhas cuja fase difere do status principal do grupo. Manter os botões de mover como alternativa. |
| P3 | A referência de data no topo depende da apresentação nativa do navegador; no remoto apareceu mês/dia/ano. | Inspeção visual: `10/23/2026`, enquanto a grade mostrou `23/10/26`. | Inconsistência com a convenção usada na operação. | Padronizar o texto visível em PT-BR, mantendo o calendário como apoio. |
| P3 | Alguns textos ainda descrevem comportamentos anteriores. | Rodapé ainda menciona duplo clique como caminho principal; a descrição inicial dos exemplos ainda citava uma planilha, apesar de a base ser gerada. | Dificulta entender o modo atual de uso e a origem dos exemplos. | Atualizar os rótulos. A descrição dos dados fictícios foi ajustada na versão de demonstração; o rodapé continua como melhoria pendente. |

### Decisões de design que eu manteria

A navegação Vendedor/Cliente lado a lado, os avisos sobrepostos, o cabeçalho curto, os ícones com descrição, a tabela expandida, os balões de OS/pedidos e a separação explícita entre editar e confirmar são escolhas adequadas à rotina.

Os cards cabem em pouca altura e ajudam a consultar uma carteira pequena. O quadro por fases é útil para distribuição do trabalho; o calendário é útil para prazos e verificações. Nenhuma dessas visões deve substituir a precisão da grade ou mostrar silenciosamente o valor de outra OS.

## 5. Como integrar os painéis

### 5.1 Responsabilidade de cada aplicativo

| Camada | Papel proposto |
|---|---|
| Base SAP/extrações | Identificação da OS, origem Rentável/Garantia, cliente, máquina, valores, datas sistêmicas, etapa da base e presença na carteira. |
| Mesa do planejador | Registro operacional: situação verificada, observação comercial, próxima ação, responsável, prazo, previsão PR, pedidos de peças, próxima verificação e confirmação. |
| Gerencial | Consolidação, validação de identidade/revisões, conciliação de conflitos, prioridades, histórico e publicação. |
| Comercial | Consulta da publicação aprovada, com distinção entre informação sistêmica, confirmada e alterada desde a confirmação. |

A etapa importada do SAP deve continuar separada do Status do controle. Alterar Status no planejador não deve sobrescrever silenciosamente a etapa sistêmica. Da mesma forma, valores financeiros editados na mesa não devem substituir os valores da base por uma correspondência automática.

Estar no mesmo repositório não cria uma base compartilhada. Hoje são páginas estáticas, com estruturas e ciclos próprios. O rascunho do navegador também não é uma fonte compartilhada entre computadores.

### 5.2 Primeiro caminho recomendado: arquivo de atualizações com conciliação

Recomendo começar com um fluxo manual curto, reutilizando o mecanismo de rodadas e conflitos que o gerencial já possui:

1. O gerencial prepara uma carteira para o planejador, com OSs, identidade dos responsáveis, catálogo de situações, revisão de cada OS e revisão da etapa sistêmica.
2. O planejador abre ou atualiza sua carteira. Os agrupamentos, rotinas e colunas pessoais permanecem como organização local.
3. Ele consulta SAP/PartsVis e preenche a grade normalmente. Alterações ainda não confirmadas ficam como rascunho.
4. Quando confirmar as OSs desejadas, o aplicativo registra quem confirmou, a data/hora e a versão do conteúdo.
5. O comando **Enviar atualizações** gera um arquivo somente com as alterações previstas no contrato, uma entrada por OS completa.
6. O gerencial lê o arquivo, mostra atualizações, duplicatas, divergências e campos que seriam limpos. Aplicar consolida o lote.
7. O gerencial devolve um recibo e produz uma nova publicação comercial. O planejador passa a distinguir confirmado, enviado e recebido.

Esse caminho mantém o envio sob comando do usuário e permite testar o modelo sem iniciar por uma aplicação com servidor e sincronização multiusuário.

O novo arquivo JSON exigirá um importador correspondente no gerencial. Como alternativa de transição, o planejador pode gerar o XLSX de resposta já aceito pelo gerencial, preservando `_Meta`, rodada, origem, revisão e catálogo. Isso facilita a compatibilidade inicial, mas os campos novos continuarão precisando de uma extensão do contrato.

### 5.3 Correspondência de campos

| Mesa do planejador | Destino atual/proposto no gerencial | Regra |
|---|---|---|
| OSs vinculadas / matriz | `records[os]` | Separar cada filha em uma entrada. Não enviar `...01/02` como identificador único. |
| Situação operacional | `op.situationId` | Usar ID do catálogo recebido. Texto livre continua permitido na mesa, mas exige correspondência explícita antes da publicação. |
| Observação Comercial | `op.summary` | Conteúdo apropriado ao painel comercial. |
| Observação interna | `op.internal` | Manter fora da publicação comercial. |
| Próxima ação | `op.nextAction` | Texto registrado pelo planejador. |
| Responsável | `op.actionOwner` | Pode ser função ou texto livre; não identifica quem confirmou. |
| Prazo da Ação | `op.actionDue` | ISO no arquivo; PT-BR na tela. |
| Previsão Conclusão / PR | `op.completion` | Uma previsão por OS; manter a referência da base para comparação. |
| Última confirmação | `confirmed` | Vinculada à versão confirmada, sem renovação implícita ao editar. |
| Identidade do planejador | `by` / `confirmedBy` e `plannerId` | Campo adicional necessário. Não deduzir de Responsável ou Vendedor. |
| Fatura no mês / mês | `op.invoice` / `op.invoiceMonth` | Validar opções e mês; respeitar a origem da previsão existente. |
| Próxima verificação | Extensão estruturada | Não há campo equivalente no conjunto operacional atual. |
| Situação Peças / Pedido | `partsOrders[]`, extensão proposta | Preservar número, previsão, texto e identificador de cada pedido. Nunca achatar definitivamente em um texto único. |
| Status / Reprovado | Status de acompanhamento e evento de quarentena | Não substituir automaticamente etapa SAP nem presença na base. Definir como a reprovação será apresentada no gerencial/comercial. |
| Rotinas, larguras, principal por campo | Preferências da mesa | Não transformar em dados operacionais nem em filtros da publicação. |
| Colunas personalizadas | Campo local ou extensão declarada | Publicar apenas as que forem mapeadas e aprovadas para compartilhamento. |

A escolha da OS principal serve somente para a apresentação. A exportação deve percorrer os dados de todas as filhas elegíveis, independentemente da OS que aparece na célula resumida.

### 5.4 Conteúdo mínimo do contrato

O envelope deve identificar versão do formato, acompanhamento (`instanceId`), rodada, planejador, arquivo/lote e data de geração. Cada entrada deve levar OS completa, origem, revisão recebida, revisão da etapa, valores alterados, identificação dos campos intencionalmente limpos e confirmação associada ao conteúdo.

Convém tratar ausência de campo como **não alterar**. Uma limpeza deve ser explícita. Isso evita apagar dados no gerencial quando uma versão do planejador não conhece determinada coluna.

Para identificar a OS, usar o contexto SAP necessário à operação junto ao número completo, conforme a unicidade da base. Cliente e vendedor são dimensões, não chaves de identidade. Uma troca de carteira deve produzir uma divergência a resolver.

### 5.5 Confirmação, rascunho e publicação

A data antiga deve continuar aparecendo quando a linha for editada, conforme solicitado. Para integrar com segurança, o aplicativo precisa saber também se aquela data ainda corresponde ao conteúdo atual.

Exemplo fictício: uma OS foi confirmada em 20/10; sua previsão foi alterada em 23/10. A tela continua mostrando 20/10, mas identifica a previsão como alterada depois da confirmação. Essa alteração não deve ser apresentada ao comercial como se estivesse confirmada em 20/10.

Uma solução é manter `revision`, `confirmedRevision`, data/hora da confirmação e um retrato/hash dos campos confirmados por OS. O comando de envio informa o que está confirmado e o que ainda é rascunho. Não é necessário obrigar nova confirmação a cada digitação.

### 5.6 Conflitos e regras que devem continuar existindo

O núcleo atual do gerencial já verifica rodada, responsável, confirmação, situação cadastrada, mudança da etapa, revisão, duplicidade e limpeza de campos. Recomendo reaproveitar essas regras.

No teste independente foram executadas oito verificações com a OS fictícia 800000001: atualização aceita, PR mapeada, confirmação registrada, duplicata reconhecida, alteração sem confirmação rejeitada, revisão concorrente identificada, situação desconhecida rejeitada e presença dos valores na publicação comercial produzida em memória.

**Esse resultado demonstra a viabilidade do adaptador; não demonstra integração pronta.** A resposta foi mapeada em um teste do núcleo. A interface do planejador ainda não exporta esse contrato e o gerencial ainda não importa seu backup.

Também precisam de tratamento: OS removida da base, transferência de carteira, confirmação anterior à mudança sistêmica e tentativa de atualizar pai agrupador.

### 5.7 Quarentena e retenção

O planejador tem quarentena de reprovação por 50 dias. O gerencial existente tem outra lógica: ausência nas bases importadas e retenção configurada, atualmente sete dias na demonstração, com regras de agrupamento.

São eventos diferentes. Reprovar não deve equivaler a “ausente do SAP”, excluir definitivamente ou encerrar todas as filhas. Recomendo transmitir uma mudança de acompanhamento por OS, com motivo, entrada em quarentena e eventual restauração. A publicação deve definir como apresentar reprovadas ainda presentes na base.

### 5.8 Evolução futura com serviço compartilhado

Depois de estabilizar o contrato por arquivos, a mesma estrutura pode ser recebida por um serviço autenticado com armazenamento central, acesso por carteira, revisão por OS e registro de alterações. O fluxo passa a ser: salvar rascunho, confirmar, sincronizar e publicar.

O GitHub pode hospedar código e demonstrações fictícias. Ele não deve ser usado como banco de dados operacional público nem receber tokens de escrita embutidos no HTML. A eventual base compartilhada precisa de um serviço próprio e controle de acesso.

## 6. Ordem sugerida para a próxima implementação

1. Corrigir abertura de cards no contexto da OS e filtros que ignoram filhas secundárias.
2. Definir identidade do planejador e vincular confirmação à versão dos dados.
3. Estabilizar larguras, colunas fixas, densidade e comportamento da seleção após arquivar/filtrar.
4. Especificar o contrato de atualização e o mapeamento de catálogos, pedidos, próxima verificação e quarentena.
5. Implementar uma prova de ponta a ponta com duas carteiras fictícias, prévia de conflitos e recibo de importação.
6. Conferir a publicação comercial resultante, especialmente quais dados são confirmados, quais são sistêmicos e quais devem permanecer internos.
7. Só então avaliar sincronização central e uso simultâneo.

## 7. Limites e rastreabilidade

A referência de código consultada para gerencial/comercial foi o commit `0a48884e0f99d8799014ca35ece414d4c4b9cade`. O planejador sintético foi publicado no commit `9d70d2358f0e52a573293182dd39a0a0ab6f69e6`; um complemento documental ajusta somente descrições da demonstração e acrescenta este relatório.

As bases de demonstração dos aplicativos são independentes. Embora as 112 OSs iniciais do planejador existam por número no exemplo do gerencial, os cadastros e valores não devem ser tratados como uma carteira sincronizada. A integração real precisa começar pela distribuição da mesma base e dos mesmos identificadores às duas pontas.

Os testes evidenciam comportamentos dos cenários executados. Arraste permanece sem validação conclusiva; exportação TSV não foi aberta em Excel instalado; não houve teste multiusuário, avaliação móvel ou auditoria completa de acessibilidade. As falhas funcionais descritas neste relatório ainda precisam de implementação e novo teste.
