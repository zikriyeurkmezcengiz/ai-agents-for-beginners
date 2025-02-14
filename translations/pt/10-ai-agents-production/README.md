# Agentes de IA em Produção

## Introdução

Esta lição abordará:

- Como planejar de forma eficaz a implantação do seu Agente de IA em produção.
- Erros e problemas comuns que você pode enfrentar ao implantar seu Agente de IA em produção.
- Como gerenciar custos mantendo o desempenho do seu Agente de IA.

## Objetivos de Aprendizado

Após concluir esta lição, você saberá/entenderá:

- Técnicas para melhorar o desempenho, os custos e a eficácia de um sistema de Agente de IA em produção.
- O que avaliar e como avaliar seus Agentes de IA.
- Como controlar custos ao implantar Agentes de IA em produção.

É importante implantar Agentes de IA que sejam confiáveis. Confira a lição "Construindo Agentes de IA Confiáveis" para saber mais.

## Avaliando Agentes de IA

Antes, durante e depois de implantar Agentes de IA, é fundamental ter um sistema adequado para avaliá-los. Isso garantirá que seu sistema esteja alinhado com seus objetivos e os de seus usuários.

Para avaliar um Agente de IA, é importante ter a capacidade de avaliar não apenas o resultado do agente, mas todo o sistema em que ele opera. Isso inclui, mas não se limita a:

- A solicitação inicial ao modelo.
- A capacidade do agente de identificar a intenção do usuário.
- A capacidade do agente de identificar a ferramenta certa para realizar a tarefa.
- A resposta da ferramenta à solicitação do agente.
- A capacidade do agente de interpretar a resposta da ferramenta.
- O feedback do usuário à resposta do agente.

Isso permite identificar áreas de melhoria de forma mais modular. Assim, você pode monitorar o impacto de mudanças nos modelos, prompts, ferramentas e outros componentes com maior eficiência.

## Problemas Comuns e Soluções Potenciais com Agentes de IA

| **Problema**                                   | **Solução Potencial**                                                                                                                                                                                                     |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agente de IA não realiza tarefas de forma consistente | - Refinar o prompt fornecido ao Agente de IA; seja claro sobre os objetivos.<br>- Identificar onde dividir as tarefas em subtarefas e delegá-las a múltiplos agentes pode ser útil.                                         |
| Agente de IA entrando em loops contínuos       | - Certifique-se de ter condições e termos de encerramento claros para que o Agente saiba quando parar o processo.<br>- Para tarefas complexas que exigem raciocínio e planejamento, utilize um modelo maior especializado nessas tarefas. |
| Chamadas de ferramentas pelo Agente de IA não estão funcionando bem | - Teste e valide a saída da ferramenta fora do sistema do agente.<br>- Refine os parâmetros definidos, prompts e nomes das ferramentas.                                                                                     |
| Sistema de múltiplos agentes não está funcionando de forma consistente | - Refinar os prompts fornecidos a cada agente para garantir que sejam específicos e distintos entre si.<br>- Construir um sistema hierárquico usando um agente "roteador" ou controlador para determinar qual agente é o mais adequado. |

## Gerenciamento de Custos

Aqui estão algumas estratégias para gerenciar os custos ao implantar Agentes de IA em produção:

- **Cachear Respostas** - Identificar solicitações e tarefas comuns e fornecer as respostas antes que elas passem pelo seu sistema de agentes é uma boa maneira de reduzir o volume de solicitações semelhantes. Você pode até implementar um fluxo para identificar quão semelhante uma solicitação é em relação às solicitações em cache, usando modelos de IA mais básicos.

- **Usar Modelos Menores** - Modelos de Linguagem Pequenos (SLMs) podem ter um bom desempenho em certos casos de uso de agentes e reduzirão significativamente os custos. Como mencionado anteriormente, construir um sistema de avaliação para determinar e comparar o desempenho em relação a modelos maiores é a melhor maneira de entender quão bem um SLM funcionará no seu caso de uso.

- **Usar um Modelo Roteador** - Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Você pode usar um LLM/SLM ou uma função serverless para rotear solicitações com base na complexidade para os modelos mais adequados. Isso ajudará a reduzir custos enquanto garante o desempenho nas tarefas certas.

## Parabéns

Esta é, atualmente, a última lição de "Agentes de IA para Iniciantes".

Planejamos continuar adicionando lições com base no feedback e nas mudanças desta indústria em constante crescimento, então volte a nos visitar em breve.

Se você deseja continuar aprendendo e desenvolvendo com Agentes de IA, participe do [Azure AI Community Discord](https://discord.gg/kzRShWzttr).

Realizamos workshops, mesas-redondas da comunidade e sessões de "pergunte-me qualquer coisa" por lá.

Também temos uma coleção de aprendizado com materiais adicionais que podem ajudar você a começar a construir Agentes de IA em produção.

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.