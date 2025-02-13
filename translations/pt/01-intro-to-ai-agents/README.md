# Introdução a Agentes de IA e Casos de Uso

Bem-vindo ao curso "Agentes de IA para Iniciantes"! Este curso fornece conhecimentos fundamentais e exemplos práticos para a construção de Agentes de IA.

Junte-se à [Comunidade do Discord do Azure AI](https://discord.gg/kzRShWzttr) para conhecer outros alunos, construtores de Agentes de IA e tirar quaisquer dúvidas que você tenha sobre este curso.

Para começar este curso, vamos primeiro entender melhor o que são os Agentes de IA e como podemos utilizá-los em aplicações e fluxos de trabalho que criamos.

## Introdução

Esta lição aborda:

- O que são Agentes de IA e quais são os diferentes tipos de agentes?
- Quais casos de uso são mais indicados para Agentes de IA e como eles podem nos ajudar?
- Quais são alguns dos componentes básicos ao projetar Soluções Agênticas?

## Objetivos de Aprendizado
Após concluir esta lição, você deverá ser capaz de:

- Compreender os conceitos de Agentes de IA e como eles diferem de outras soluções de IA.
- Aplicar Agentes de IA de maneira mais eficiente.
- Projetar soluções agênticas produtivamente para usuários e clientes.

## Definindo Agentes de IA e Tipos de Agentes de IA

### O que são Agentes de IA?

Agentes de IA são **sistemas** que permitem que **Modelos de Linguagem de Grande Escala (LLMs)** **executem ações** ao estender suas capacidades, dando aos LLMs **acesso a ferramentas** e **conhecimento**.

Vamos dividir essa definição em partes menores:

- **Sistema** - É importante pensar nos agentes não apenas como um único componente, mas como um sistema composto por muitos componentes. No nível básico, os componentes de um Agente de IA são:
  - **Ambiente** - O espaço definido onde o Agente de IA está operando. Por exemplo, se tivermos um Agente de IA para reservas de viagens, o ambiente pode ser o sistema de reservas de viagens que o agente usa para completar tarefas.
  - **Sensores** - Os ambientes possuem informações e fornecem feedback. Agentes de IA usam sensores para coletar e interpretar essas informações sobre o estado atual do ambiente. No exemplo do Agente de Reservas de Viagens, o sistema de reservas pode fornecer informações como disponibilidade de hotéis ou preços de passagens aéreas.
  - **Atuadores** - Depois que o Agente de IA recebe o estado atual do ambiente, ele determina qual ação realizar para alterar o ambiente em relação à tarefa atual. No caso do Agente de Reservas de Viagens, isso pode ser reservar um quarto disponível para o usuário.

![O que são Agentes de IA?](../../../translated_images/what-are-ai-agents.png?WT.7f2607783e984be0cfb6dd064ad20389d37cf6d1d28bc5d5a3c648ef353bde89.pt.mc_id=academic-105485-koreyst)

**Modelos de Linguagem de Grande Escala (LLMs)** - O conceito de agentes existia antes da criação dos LLMs. A vantagem de construir Agentes de IA com LLMs é sua capacidade de interpretar linguagem humana e dados. Essa habilidade permite que os LLMs interpretem informações do ambiente e definam um plano para alterar o ambiente.

**Executar Ações** - Fora dos sistemas de Agentes de IA, os LLMs são limitados a situações onde a ação é gerar conteúdo ou informações com base em um comando do usuário. Dentro dos sistemas de Agentes de IA, os LLMs podem realizar tarefas interpretando o pedido do usuário e utilizando ferramentas disponíveis no ambiente.

**Acesso a Ferramentas** - As ferramentas às quais o LLM tem acesso são definidas por 1) o ambiente em que está operando e 2) o desenvolvedor do Agente de IA. No exemplo do agente de viagens, as ferramentas do agente são limitadas pelas operações disponíveis no sistema de reservas e/ou o desenvolvedor pode limitar o acesso do agente a ferramentas relacionadas a voos.

**Conhecimento** - Além das informações fornecidas pelo ambiente, os Agentes de IA também podem recuperar conhecimento de outros sistemas, serviços, ferramentas e até outros agentes. No exemplo do agente de viagens, esse conhecimento pode incluir informações sobre as preferências de viagem do usuário localizadas em um banco de dados de clientes.

### Os diferentes tipos de agentes

Agora que temos uma definição geral de Agentes de IA, vamos analisar alguns tipos específicos de agentes e como eles seriam aplicados a um agente de reservas de viagens.

| **Tipo de Agente**            | **Descrição**                                                                                                                       | **Exemplo**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agentes de Reflexo Simples**| Executam ações imediatas com base em regras predefinidas.                                                                             | O agente de viagens interpreta o contexto de um e-mail e encaminha reclamações de viagem para o atendimento ao cliente.                                                                                                        |
| **Agentes Baseados em Modelo**| Executam ações com base em um modelo do mundo e mudanças nesse modelo.                                                               | O agente de viagens prioriza rotas com mudanças significativas de preço com base no acesso a dados históricos de preços.                                                                                                      |
| **Agentes Baseados em Objetivos** | Criam planos para atingir objetivos específicos, interpretando o objetivo e determinando as ações necessárias para alcançá-lo.       | O agente de viagens reserva uma jornada determinando os arranjos de viagem necessários (carro, transporte público, voos) do local atual ao destino.                                                                           |
| **Agentes Baseados em Utilidade** | Consideram preferências e ponderam trade-offs numericamente para determinar como atingir objetivos.                                 | O agente de viagens maximiza a utilidade ao ponderar conveniência versus custo ao reservar viagens.                                                                                                                           |
| **Agentes de Aprendizado**    | Melhoram com o tempo, respondendo a feedbacks e ajustando ações de acordo.                                                           | O agente de viagens melhora usando o feedback de clientes de pesquisas pós-viagem para fazer ajustes em reservas futuras.                                                                                                     |
| **Agentes Hierárquicos**      | Apresentam múltiplos agentes em um sistema hierárquico, com agentes de nível superior dividindo tarefas em subtarefas para agentes de nível inferior completarem. | O agente de viagens cancela uma viagem dividindo a tarefa em subtarefas (por exemplo, cancelar reservas específicas) e permitindo que agentes de nível inferior as concluam, reportando de volta ao agente de nível superior. |
| **Sistemas Multiagentes (MAS)**| Agentes completam tarefas de forma independente, cooperativa ou competitiva.                                                        | Cooperativo: Múltiplos agentes reservam serviços específicos de viagem, como hotéis, voos e entretenimento. Competitivo: Múltiplos agentes gerenciam e competem por um calendário compartilhado de reservas de hotel.          |

## Quando Usar Agentes de IA

Na seção anterior, usamos o caso de uso do Agente de Viagens para explicar como diferentes tipos de agentes podem ser usados em cenários variados de reservas de viagem. Continuaremos utilizando este exemplo ao longo do curso.

Vamos analisar os tipos de casos de uso que são mais adequados para Agentes de IA:

![Quando usar Agentes de IA?](../../../translated_images/when-to-use-ai-agents.png?WT.1681e3f19611f820ee4331ab494b50ebc6f09b2fb4df3a5f4dac5458316263ad.pt.mc_id=academic-105485-koreyst)

- **Problemas Abertos** - permitindo que o LLM determine os passos necessários para completar uma tarefa, pois nem sempre é possível codificar isso diretamente em um fluxo de trabalho.
- **Processos com Múltiplas Etapas** - tarefas que exigem um nível de complexidade em que o Agente de IA precisa usar ferramentas ou informações ao longo de várias interações, em vez de uma única busca.
- **Melhoria ao Longo do Tempo** - tarefas onde o agente pode melhorar ao longo do tempo ao receber feedback do ambiente ou dos usuários para oferecer melhor utilidade.

Abordamos mais considerações sobre o uso de Agentes de IA na lição Construindo Agentes de IA Confiáveis.

## Fundamentos das Soluções Agênticas

### Desenvolvimento de Agentes

O primeiro passo ao projetar um sistema de Agente de IA é definir as ferramentas, ações e comportamentos. Neste curso, focamos no uso do **Azure AI Agent Service** para definir nossos Agentes. Ele oferece recursos como:

- Seleção de Modelos Abertos, como OpenAI, Mistral e Llama
- Uso de Dados Licenciados por meio de provedores como Tripadvisor
- Uso de ferramentas padronizadas OpenAPI 3.0

### Padrões Agênticos

A comunicação com LLMs é feita por meio de prompts. Dada a natureza semi-autônoma dos Agentes de IA, nem sempre é possível ou necessário reformular manualmente o prompt do LLM após uma mudança no ambiente. Utilizamos **Padrões Agênticos** que permitem que o LLM seja orientado ao longo de várias etapas de maneira mais escalável.

Este curso é dividido em alguns dos padrões agênticos populares atuais.

### Frameworks Agênticos

Frameworks Agênticos permitem que os desenvolvedores implementem padrões agênticos por meio de código. Esses frameworks oferecem templates, plugins e ferramentas para uma melhor colaboração com Agentes de IA. Esses benefícios proporcionam maior observabilidade e resolução de problemas em sistemas de Agentes de IA.

Neste curso, exploraremos o framework AutoGen, baseado em pesquisa, e o framework Agent, pronto para produção, do Semantic Kernel.

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.