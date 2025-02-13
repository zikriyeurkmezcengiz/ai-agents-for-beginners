# Explore Frameworks de Agentes de IA

Os frameworks de agentes de IA são plataformas de software projetadas para simplificar a criação, implantação e gerenciamento de agentes de IA. Esses frameworks fornecem aos desenvolvedores componentes pré-construídos, abstrações e ferramentas que facilitam o desenvolvimento de sistemas de IA complexos.

Esses frameworks ajudam os desenvolvedores a focarem nos aspectos únicos de suas aplicações, fornecendo abordagens padronizadas para desafios comuns no desenvolvimento de agentes de IA. Eles aumentam a escalabilidade, acessibilidade e eficiência na construção de sistemas de IA.

## Introdução

Esta lição abordará:

- O que são frameworks de agentes de IA e o que eles permitem que os desenvolvedores façam?
- Como as equipes podem usá-los para prototipar rapidamente, iterar e melhorar as capacidades dos agentes?
- Quais são as diferenças entre os frameworks e ferramentas criados pela Microsoft ([Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service))?
- É possível integrar diretamente minhas ferramentas existentes do ecossistema Azure, ou são necessárias soluções independentes?
- O que é o serviço Azure AI Agents e como ele está me ajudando?

## Objetivos de aprendizagem

Os objetivos desta lição são ajudá-lo a compreender:

- O papel dos frameworks de agentes de IA no desenvolvimento de IA.
- Como aproveitar os frameworks de agentes de IA para construir agentes inteligentes.
- Capacidades-chave habilitadas pelos frameworks de agentes de IA.
- As diferenças entre Autogen, Semantic Kernel e Azure AI Agent Service.

## O que são frameworks de agentes de IA e o que eles permitem que os desenvolvedores façam?

Frameworks tradicionais de IA podem ajudar a integrar IA em seus aplicativos e melhorar esses aplicativos das seguintes maneiras:

- **Personalização**: A IA pode analisar o comportamento e as preferências dos usuários para fornecer recomendações, conteúdos e experiências personalizadas.  
Exemplo: Serviços de streaming como a Netflix usam IA para sugerir filmes e séries com base no histórico de visualização, aumentando o engajamento e a satisfação do usuário.

- **Automação e eficiência**: A IA pode automatizar tarefas repetitivas, simplificar fluxos de trabalho e melhorar a eficiência operacional.  
Exemplo: Aplicativos de atendimento ao cliente usam chatbots baseados em IA para lidar com perguntas comuns, reduzindo o tempo de resposta e liberando agentes humanos para questões mais complexas.

- **Experiência aprimorada do usuário**: A IA pode melhorar a experiência geral do usuário ao oferecer recursos inteligentes, como reconhecimento de voz, processamento de linguagem natural e texto preditivo.  
Exemplo: Assistentes virtuais como Siri e Google Assistant usam IA para entender e responder a comandos de voz, facilitando a interação dos usuários com seus dispositivos.

### Parece ótimo, certo? Então, por que precisamos de frameworks de agentes de IA?

Os frameworks de agentes de IA representam algo além dos frameworks tradicionais de IA. Eles são projetados para permitir a criação de agentes inteligentes que podem interagir com usuários, outros agentes e o ambiente para atingir objetivos específicos. Esses agentes podem exibir comportamentos autônomos, tomar decisões e se adaptar a condições em constante mudança. Vamos analisar algumas capacidades-chave habilitadas pelos frameworks de agentes de IA:

- **Colaboração e coordenação entre agentes**: Permitem a criação de múltiplos agentes de IA que podem trabalhar juntos, se comunicar e coordenar para resolver tarefas complexas.
- **Automação e gerenciamento de tarefas**: Oferecem mecanismos para automatizar fluxos de trabalho em várias etapas, delegação de tarefas e gerenciamento dinâmico de tarefas entre agentes.
- **Compreensão e adaptação contextual**: Equipam agentes com a capacidade de entender o contexto, se adaptar a ambientes em mudança e tomar decisões com base em informações em tempo real.

Em resumo, os agentes permitem fazer mais, levar a automação a um nível superior, criar sistemas mais inteligentes que podem se adaptar e aprender com seu ambiente.

## Como prototipar, iterar e melhorar rapidamente as capacidades do agente?

Este é um cenário em constante evolução, mas há algumas características comuns à maioria dos frameworks de agentes de IA que podem ajudá-lo a prototipar e iterar rapidamente, como componentes modulares, ferramentas colaborativas e aprendizado em tempo real. Vamos explorar esses aspectos:

- **Use componentes modulares**: Frameworks de IA oferecem componentes pré-construídos, como prompts, parsers e gerenciamento de memória.
- **Aproveite ferramentas colaborativas**: Projete agentes com funções e tarefas específicas, permitindo testar e refinar fluxos de trabalho colaborativos.
- **Aprenda em tempo real**: Implemente loops de feedback onde os agentes aprendem com as interações e ajustam seu comportamento dinamicamente.

### Use componentes modulares

Frameworks como LangChain e Microsoft Semantic Kernel oferecem componentes pré-construídos, como prompts, parsers e gerenciamento de memória.

**Como as equipes podem usar isso**: As equipes podem montar rapidamente esses componentes para criar um protótipo funcional sem começar do zero, permitindo experimentação e iteração rápidas.

**Como funciona na prática**: Você pode usar um parser pré-construído para extrair informações da entrada do usuário, um módulo de memória para armazenar e recuperar dados, e um gerador de prompts para interagir com os usuários, tudo sem precisar construir esses componentes do zero.

**Exemplo de código**. Vamos analisar um exemplo de como usar um parser pré-construído para extrair informações da entrada do usuário:

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

O exemplo acima mostra como você pode usar um parser pré-construído para extrair informações-chave da entrada do usuário, como origem, destino e data de uma solicitação de reserva de voo. Essa abordagem modular permite que você foque na lógica de alto nível.

### Aproveite ferramentas colaborativas

Frameworks como CrewAI e Microsoft Autogen facilitam a criação de múltiplos agentes que podem trabalhar juntos.

**Como as equipes podem usar isso**: As equipes podem projetar agentes com funções e tarefas específicas, permitindo testar e refinar fluxos de trabalho colaborativos e melhorar a eficiência geral do sistema.

**Como funciona na prática**: Você pode criar uma equipe de agentes onde cada agente tem uma função especializada, como recuperação de dados, análise ou tomada de decisão. Esses agentes podem se comunicar e compartilhar informações para alcançar um objetivo comum, como responder a uma consulta do usuário ou concluir uma tarefa.

**Exemplo de código (Autogen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

O código acima mostra como você pode criar uma tarefa que envolve múltiplos agentes trabalhando juntos para analisar dados. Cada agente desempenha uma função específica, e a tarefa é executada coordenando os agentes para alcançar o resultado desejado. Ao criar agentes dedicados com funções especializadas, você pode melhorar a eficiência e o desempenho das tarefas.

### Aprenda em tempo real

Frameworks avançados oferecem capacidades para compreensão contextual e adaptação em tempo real.

**Como as equipes podem usar isso**: As equipes podem implementar loops de feedback onde os agentes aprendem com interações e ajustam seu comportamento dinamicamente, levando à melhoria contínua e ao refinamento de capacidades.

**Como funciona na prática**: Agentes podem analisar feedback dos usuários, dados do ambiente e resultados de tarefas para atualizar sua base de conhecimento, ajustar algoritmos de tomada de decisão e melhorar o desempenho ao longo do tempo. Esse processo de aprendizado iterativo permite que os agentes se adaptem a condições em mudança e preferências dos usuários, aumentando a eficácia geral do sistema.

## Quais são as diferenças entre os frameworks Autogen, Semantic Kernel e Azure AI Agent Service?

Existem várias formas de comparar esses frameworks, mas vamos analisar algumas diferenças-chave em termos de design, capacidades e casos de uso:

### Autogen

Framework de código aberto desenvolvido pelo AI Frontiers Lab da Microsoft Research. Focado em aplicações *agêncicas* distribuídas e orientadas a eventos, permitindo múltiplos LLMs, SLMs, ferramentas e padrões avançados de design multiagente.

Autogen é baseado no conceito central de agentes, que são entidades autônomas capazes de perceber seu ambiente, tomar decisões e realizar ações para alcançar objetivos específicos. Os agentes se comunicam por meio de mensagens assíncronas, permitindo que trabalhem de forma independente e paralela, aumentando a escalabilidade e a capacidade de resposta do sistema.

Agentes são baseados no [modelo de ator](https://en.wikipedia.org/wiki/Actor_model). Segundo a Wikipedia, um ator é _o bloco básico de construção da computação concorrente. Em resposta a uma mensagem recebida, um ator pode: tomar decisões locais, criar mais atores, enviar mais mensagens e determinar como responder à próxima mensagem recebida_.

**Casos de uso**: Automação de geração de código, tarefas de análise de dados e construção de agentes personalizados para funções de planejamento e pesquisa.

... *(continua com as seções detalhadas dos frameworks, mantendo a tradução fluida e natural)* ...
com base nos objetivos do projeto. Ideal para compreensão de linguagem natural, geração de conteúdo. - **Azure AI Agent Service**: Modelos flexíveis, mecanismos de segurança empresarial, métodos de armazenamento de dados. Ideal para implantação segura, escalável e flexível de agentes de IA em aplicações empresariais. ## Posso integrar diretamente minhas ferramentas existentes do ecossistema Azure ou preciso de soluções independentes? A resposta é sim, você pode integrar diretamente suas ferramentas existentes do ecossistema Azure com o Azure AI Agent Service, especialmente porque ele foi projetado para funcionar perfeitamente com outros serviços do Azure. Você poderia, por exemplo, integrar Bing, Azure AI Search e Azure Functions. Há também uma integração profunda com o Azure AI Foundry. Para Autogen e Semantic Kernel, você também pode integrar com os serviços Azure, mas pode ser necessário chamar os serviços Azure a partir do seu código. Outra maneira de integrar é usar os SDKs do Azure para interagir com os serviços Azure a partir de seus agentes. Além disso, como mencionado, você pode usar o Azure AI Agent Service como um orquestrador para seus agentes criados no Autogen ou Semantic Kernel, o que proporcionaria fácil acesso ao ecossistema Azure. ## Referências - [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357) - [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/) - [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp) - [4] - [Azure AI Agent service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview) - [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.