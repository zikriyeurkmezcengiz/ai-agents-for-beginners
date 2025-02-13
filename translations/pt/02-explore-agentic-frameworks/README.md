# Explorar Frameworks de Agentes de IA

Frameworks de agentes de IA são plataformas de software projetadas para simplificar a criação, implantação e gerenciamento de agentes de IA. Esses frameworks fornecem aos desenvolvedores componentes pré-construídos, abstrações e ferramentas que agilizam o desenvolvimento de sistemas complexos de IA.

Eles ajudam os desenvolvedores a se concentrarem nos aspectos únicos de suas aplicações, oferecendo abordagens padronizadas para desafios comuns no desenvolvimento de agentes de IA. Esses frameworks melhoram a escalabilidade, acessibilidade e eficiência na construção de sistemas de IA.

## Introdução

Esta lição abordará:

- O que são frameworks de agentes de IA e o que permitem que os desenvolvedores façam?
- Como as equipes podem usá-los para prototipar rapidamente, iterar e melhorar as capacidades do meu agente?
- Quais são as diferenças entre os frameworks e ferramentas criados pela Microsoft ([Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service))?
- Posso integrar diretamente minhas ferramentas existentes do ecossistema Azure ou preciso de soluções independentes?
- O que é o serviço Azure AI Agents e como isso me ajuda?

## Objetivos de aprendizado

Os objetivos desta lição são ajudá-lo a entender:

- O papel dos frameworks de agentes de IA no desenvolvimento de IA.
- Como aproveitar frameworks de agentes de IA para construir agentes inteligentes.
- Capacidades principais habilitadas por frameworks de agentes de IA.
- As diferenças entre Autogen, Semantic Kernel e Azure AI Agent Service.

## O que são frameworks de agentes de IA e o que permitem que os desenvolvedores façam?

Frameworks tradicionais de IA podem ajudar você a integrar IA em seus aplicativos e melhorar esses aplicativos das seguintes maneiras:

- **Personalização**: A IA pode analisar o comportamento e as preferências do usuário para fornecer recomendações, conteúdos e experiências personalizadas.  
Exemplo: Serviços de streaming como Netflix usam IA para sugerir filmes e séries com base no histórico de visualização, aumentando o engajamento e a satisfação do usuário.

- **Automação e Eficiência**: A IA pode automatizar tarefas repetitivas, otimizar fluxos de trabalho e melhorar a eficiência operacional.  
Exemplo: Aplicativos de atendimento ao cliente usam chatbots com IA para lidar com consultas comuns, reduzindo o tempo de resposta e liberando agentes humanos para questões mais complexas.

- **Melhoria na Experiência do Usuário**: A IA pode aprimorar a experiência geral do usuário, fornecendo recursos inteligentes, como reconhecimento de voz, processamento de linguagem natural e texto preditivo.  
Exemplo: Assistentes virtuais como Siri e Google Assistant usam IA para entender e responder a comandos de voz, facilitando a interação dos usuários com seus dispositivos.

### Isso tudo parece ótimo, certo? Então por que precisamos de frameworks de agentes de IA?

Frameworks de agentes de IA representam algo além dos frameworks tradicionais de IA. Eles são projetados para permitir a criação de agentes inteligentes que podem interagir com usuários, outros agentes e o ambiente para alcançar objetivos específicos. Esses agentes podem exibir comportamento autônomo, tomar decisões e se adaptar a condições em constante mudança. Vamos examinar algumas capacidades principais habilitadas pelos frameworks de agentes de IA:

- **Colaboração e Coordenação entre Agentes**: Permitem a criação de múltiplos agentes de IA que podem trabalhar juntos, se comunicar e coordenar para resolver tarefas complexas.
- **Automação e Gerenciamento de Tarefas**: Fornecem mecanismos para automatizar fluxos de trabalho de múltiplas etapas, delegação de tarefas e gerenciamento dinâmico de tarefas entre agentes.
- **Compreensão Contextual e Adaptação**: Equipam os agentes com a capacidade de entender o contexto, se adaptar a ambientes em mudança e tomar decisões com base em informações em tempo real.

Em resumo, os agentes permitem que você faça mais, leve a automação para o próximo nível e crie sistemas mais inteligentes que podem se adaptar e aprender com seu ambiente.

## Como prototipar rapidamente, iterar e melhorar as capacidades do agente?

Este é um cenário em rápida evolução, mas existem alguns elementos comuns na maioria dos frameworks de agentes de IA que podem ajudar você a prototipar e iterar rapidamente, como componentes modulares, ferramentas colaborativas e aprendizado em tempo real. Vamos explorar esses elementos:

- **Use Componentes Modulares**: Frameworks de IA oferecem componentes pré-construídos, como prompts, analisadores e gerenciamento de memória.
- **Aproveite Ferramentas Colaborativas**: Projete agentes com papéis e tarefas específicas, permitindo testar e refinar fluxos de trabalho colaborativos.
- **Aprenda em Tempo Real**: Implemente loops de feedback onde os agentes aprendem com interações e ajustam seu comportamento dinamicamente.

### Use Componentes Modulares

Frameworks como LangChain e Microsoft Semantic Kernel oferecem componentes pré-construídos, como prompts, analisadores e gerenciamento de memória.

**Como as equipes podem usá-los**: As equipes podem montar rapidamente esses componentes para criar um protótipo funcional sem começar do zero, permitindo experimentação e iteração rápidas.

**Como funciona na prática**: Você pode usar um analisador pré-construído para extrair informações da entrada do usuário, um módulo de memória para armazenar e recuperar dados e um gerador de prompts para interagir com os usuários, tudo isso sem precisar construir esses componentes do zero.

**Exemplo de código**: Vamos ver um exemplo de como você pode usar um analisador pré-construído para extrair informações da entrada do usuário:

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

O que você pode ver neste exemplo é como você pode aproveitar um analisador pré-construído para extrair informações-chave da entrada do usuário, como origem, destino e data de uma solicitação de reserva de voo. Essa abordagem modular permite que você se concentre na lógica de alto nível.

### Aproveite Ferramentas Colaborativas

Frameworks como CrewAI e Microsoft Autogen facilitam a criação de múltiplos agentes que podem trabalhar juntos.

**Como as equipes podem usá-los**: As equipes podem projetar agentes com funções e tarefas específicas, permitindo testar e refinar fluxos de trabalho colaborativos e melhorar a eficiência geral do sistema.

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

O que você vê no código acima é como você pode criar uma tarefa que envolve múltiplos agentes trabalhando juntos para analisar dados. Cada agente desempenha uma função específica, e a tarefa é executada coordenando os agentes para alcançar o resultado desejado. Criando agentes dedicados com funções especializadas, você pode melhorar a eficiência e o desempenho das tarefas.

### Aprenda em Tempo Real

Frameworks avançados fornecem capacidades para compreensão de contexto em tempo real e adaptação.

**Como as equipes podem usá-los**: As equipes podem implementar loops de feedback onde os agentes aprendem com interações e ajustam seu comportamento dinamicamente, levando a uma melhoria contínua e refinamento das capacidades.

**Como funciona na prática**: Agentes podem analisar o feedback do usuário, dados do ambiente e resultados de tarefas para atualizar sua base de conhecimento, ajustar algoritmos de tomada de decisão e melhorar o desempenho ao longo do tempo. Esse processo de aprendizado iterativo permite que os agentes se adaptem a condições em mudança e preferências dos usuários, melhorando a eficácia geral do sistema.

## Quais são as diferenças entre os frameworks Autogen, Semantic Kernel e Azure AI Agent Service?

Existem várias formas de comparar esses frameworks, mas vamos analisar algumas diferenças principais em termos de design, capacidades e casos de uso:

### Autogen

Framework de código aberto desenvolvido pelo AI Frontiers Lab da Microsoft Research. Focado em aplicações *agênticas* distribuídas e orientadas a eventos, permitindo múltiplos LLMs e SLMs, ferramentas e padrões avançados de design multi-agente.

Autogen é baseado no conceito central de agentes, que são entidades autônomas capazes de perceber seu ambiente, tomar decisões e realizar ações para alcançar objetivos específicos. Os agentes se comunicam por meio de mensagens assíncronas, permitindo que trabalhem de forma independente e em paralelo, melhorando a escalabilidade e a capacidade de resposta do sistema.

Os agentes são baseados no [modelo de ator](https://en.wikipedia.org/wiki/Actor_model). Segundo a Wikipedia, um ator é _a unidade básica de computação concorrente. Em resposta a uma mensagem recebida, um ator pode: tomar decisões locais, criar mais atores, enviar mais mensagens e determinar como responder à próxima mensagem recebida_.

**Casos de Uso**: Automação de geração de código, tarefas de análise de dados e construção de agentes personalizados para funções de planejamento e pesquisa.

...


com base nas metas do projeto. Ideal para compreensão de linguagem natural, geração de conteúdo. - **Azure AI Agent Service**: Modelos flexíveis, mecanismos de segurança empresarial, métodos de armazenamento de dados. Ideal para implantação segura, escalável e flexível de agentes de IA em aplicações empresariais. ## Posso integrar diretamente minhas ferramentas existentes do ecossistema Azure ou preciso de soluções independentes? A resposta é sim, você pode integrar diretamente suas ferramentas existentes do ecossistema Azure com o Azure AI Agent Service, especialmente porque ele foi projetado para funcionar perfeitamente com outros serviços Azure. Você poderia, por exemplo, integrar Bing, Azure AI Search e Azure Functions. Há também uma integração profunda com o Azure AI Foundry. Para Autogen e Semantic Kernel, você também pode integrar com serviços Azure, mas pode ser necessário chamar os serviços Azure a partir do seu código. Outra maneira de integrar é usar os SDKs do Azure para interagir com os serviços Azure a partir dos seus agentes. Além disso, como foi mencionado, você pode usar o Azure AI Agent Service como um orquestrador para seus agentes construídos no Autogen ou Semantic Kernel, o que proporcionaria fácil acesso ao ecossistema Azure. ## Referências - [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357) - [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/) - [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp) - [4] - [Azure AI Agent service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview) - [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para alcançar precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.