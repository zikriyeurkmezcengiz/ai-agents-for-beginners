# Agentic RAG

Esta lição oferece uma visão abrangente do Agentic Retrieval-Augmented Generation (Agentic RAG), um paradigma emergente de IA onde grandes modelos de linguagem (LLMs) planejam autonomamente seus próximos passos enquanto buscam informações de fontes externas. Diferente dos padrões estáticos de "recuperar e depois ler", o Agentic RAG envolve chamadas iterativas ao LLM, intercaladas com chamadas de ferramentas ou funções e saídas estruturadas. O sistema avalia os resultados, refina consultas, invoca ferramentas adicionais se necessário e continua esse ciclo até alcançar uma solução satisfatória.

## Introdução

Esta lição abordará:

- **Entender o Agentic RAG:** Conheça o paradigma emergente em IA onde grandes modelos de linguagem (LLMs) planejam autonomamente seus próximos passos enquanto buscam informações de fontes externas.
- **Compreender o Estilo Iterativo Maker-Checker:** Entenda o ciclo de chamadas iterativas ao LLM, intercaladas com chamadas de ferramentas ou funções e saídas estruturadas, projetado para melhorar a precisão e lidar com consultas malformadas.
- **Explorar Aplicações Práticas:** Identifique cenários onde o Agentic RAG se destaca, como ambientes onde a precisão é prioritária, interações complexas com bancos de dados e fluxos de trabalho prolongados.

## Objetivos de Aprendizado

Após concluir esta lição, você será capaz de:

- **Compreender o Agentic RAG:** Conhecer o paradigma emergente em IA onde grandes modelos de linguagem (LLMs) planejam autonomamente seus próximos passos enquanto buscam informações de fontes externas.
- **Estilo Iterativo Maker-Checker:** Assimilar o conceito de um ciclo de chamadas iterativas ao LLM, intercaladas com chamadas de ferramentas ou funções e saídas estruturadas, projetado para melhorar a precisão e lidar com consultas malformadas.
- **Assumir o Processo de Raciocínio:** Entender a capacidade do sistema de assumir seu processo de raciocínio, tomando decisões sobre como abordar problemas sem depender de caminhos predefinidos.
- **Fluxo de Trabalho:** Compreender como um modelo agentic decide independentemente recuperar relatórios de tendências de mercado, identificar dados de concorrentes, correlacionar métricas internas de vendas, sintetizar conclusões e avaliar a estratégia.
- **Loops Iterativos, Integração de Ferramentas e Memória:** Aprender sobre a dependência do sistema em um padrão de interação em loop, mantendo estado e memória entre etapas para evitar loops repetitivos e tomar decisões informadas.
- **Lidar com Modos de Falha e Auto-Correção:** Explorar os mecanismos robustos de auto-correção do sistema, incluindo iteração e reconsultas, uso de ferramentas de diagnóstico e recurso à supervisão humana.
- **Limites da Agência:** Entender as limitações do Agentic RAG, focando na autonomia específica do domínio, dependência de infraestrutura e respeito a limites de segurança.
- **Casos de Uso Práticos e Valor:** Identificar cenários onde o Agentic RAG se destaca, como ambientes de alta precisão, interações complexas com bancos de dados e fluxos de trabalho prolongados.
- **Governança, Transparência e Confiança:** Aprender sobre a importância da governança e transparência, incluindo raciocínio explicável, controle de vieses e supervisão humana.

## O que é Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) é um paradigma emergente de IA onde grandes modelos de linguagem (LLMs) planejam autonomamente seus próximos passos enquanto buscam informações de fontes externas. Diferente dos padrões estáticos de "recuperar e depois ler", o Agentic RAG envolve chamadas iterativas ao LLM, intercaladas com chamadas de ferramentas ou funções e saídas estruturadas. O sistema avalia resultados, refina consultas, invoca ferramentas adicionais se necessário e continua esse ciclo até alcançar uma solução satisfatória. Este estilo iterativo “maker-checker” melhora a precisão, lida com consultas malformadas e garante resultados de alta qualidade.

O sistema assume ativamente seu processo de raciocínio, reescrevendo consultas falhas, escolhendo diferentes métodos de recuperação e integrando várias ferramentas—como busca vetorial no Azure AI Search, bancos de dados SQL ou APIs personalizadas—antes de finalizar sua resposta. A qualidade distintiva de um sistema agentic é sua capacidade de assumir o processo de raciocínio. Implementações tradicionais de RAG dependem de caminhos predefinidos, mas um sistema agentic determina autonomamente a sequência de passos com base na qualidade da informação encontrada.

## Definindo Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) é um paradigma emergente no desenvolvimento de IA onde LLMs não apenas buscam informações de fontes externas de dados, mas também planejam autonomamente seus próximos passos. Diferente dos padrões estáticos de "recuperar e depois ler" ou sequências de prompts cuidadosamente roteirizadas, o Agentic RAG envolve um ciclo de chamadas iterativas ao LLM, intercaladas com chamadas de ferramentas ou funções e saídas estruturadas. A cada etapa, o sistema avalia os resultados obtidos, decide se deve refinar suas consultas, invoca ferramentas adicionais se necessário e continua esse ciclo até alcançar uma solução satisfatória.

Este estilo iterativo “maker-checker” foi projetado para melhorar a precisão, lidar com consultas malformadas para bancos de dados estruturados (ex.: NL2SQL) e garantir resultados equilibrados e de alta qualidade. Em vez de depender exclusivamente de cadeias de prompts cuidadosamente elaboradas, o sistema assume ativamente seu processo de raciocínio. Ele pode reescrever consultas que falham, escolher diferentes métodos de recuperação e integrar várias ferramentas—como busca vetorial no Azure AI Search, bancos de dados SQL ou APIs personalizadas—antes de finalizar sua resposta. Isso elimina a necessidade de estruturas de orquestração excessivamente complexas. Em vez disso, um loop relativamente simples de “chamada LLM → uso de ferramenta → chamada LLM → …” pode produzir saídas sofisticadas e bem fundamentadas.

![Agentic RAG Core Loop](../../../05-agentic-rag/images/agentic-rag-core-loop.png)

## Assumindo o Processo de Raciocínio

A qualidade distintiva que torna um sistema “agentic” é sua capacidade de assumir seu processo de raciocínio. Implementações tradicionais de RAG frequentemente dependem de humanos para predefinir um caminho para o modelo: uma cadeia de raciocínio que descreve o que recuperar e quando. Mas quando um sistema é verdadeiramente agentic, ele decide internamente como abordar o problema. Não está apenas executando um script; está determinando autonomamente a sequência de passos com base na qualidade da informação que encontra. 

Por exemplo, se solicitado a criar uma estratégia de lançamento de produto, ele não depende apenas de um prompt que descreva todo o fluxo de trabalho de pesquisa e tomada de decisão. Em vez disso, o modelo agentic decide independentemente:

1. Recuperar relatórios de tendências de mercado atuais usando Bing Web Grounding.
2. Identificar dados relevantes de concorrentes usando Azure AI Search.
3. Correlacionar métricas históricas internas de vendas usando Azure SQL Database.
4. Sintetizar as descobertas em uma estratégia coesa orquestrada via Azure OpenAI Service.
5. Avaliar a estratégia em busca de lacunas ou inconsistências, promovendo outra rodada de recuperação se necessário.

Todas essas etapas—refinar consultas, escolher fontes, iterar até “ficar satisfeito” com a resposta—são decididas pelo modelo, não roteirizadas previamente por um humano.

## Loops Iterativos, Integração de Ferramentas e Memória

![Tool Integration Architecture](../../../05-agentic-rag/images/tool-integration.png)

Um sistema agentic depende de um padrão de interação em loop:

- **Chamada Inicial:** O objetivo do usuário (também conhecido como prompt do usuário) é apresentado ao LLM.
- **Invocação de Ferramenta:** Se o modelo identificar informações ausentes ou instruções ambíguas, ele seleciona uma ferramenta ou método de recuperação—como uma consulta a um banco de dados vetorial (ex.: Azure AI Search Hybrid search sobre dados privados) ou uma chamada SQL estruturada—para obter mais contexto.
- **Avaliação e Refinamento:** Após revisar os dados retornados, o modelo decide se a informação é suficiente. Caso contrário, refina a consulta, tenta uma ferramenta diferente ou ajusta sua abordagem.
- **Repetir Até Satisfação:** Este ciclo continua até que o modelo determine que tem clareza e evidências suficientes para entregar uma resposta final bem fundamentada.
- **Memória e Estado:** Como o sistema mantém estado e memória entre etapas, ele pode lembrar tentativas anteriores e seus resultados, evitando loops repetitivos e tomando decisões mais informadas à medida que avança.

Com o tempo, isso cria um senso de entendimento evolutivo, permitindo que o modelo navegue por tarefas complexas e em várias etapas sem exigir que um humano intervenha constantemente ou reformule o prompt.

## Lidando com Modos de Falha e Auto-Correção

A autonomia do Agentic RAG também envolve mecanismos robustos de auto-correção. Quando o sistema encontra impasses—como recuperação de documentos irrelevantes ou consultas malformadas—ele pode:

- **Iterar e Reconsultar:** Em vez de retornar respostas de baixo valor, o modelo tenta novas estratégias de busca, reescreve consultas a bancos de dados ou examina conjuntos de dados alternativos.
- **Usar Ferramentas de Diagnóstico:** O sistema pode invocar funções adicionais projetadas para ajudá-lo a depurar seus passos de raciocínio ou confirmar a precisão dos dados recuperados. Ferramentas como Azure AI Tracing serão importantes para possibilitar observabilidade e monitoramento robustos.
- **Recorrer à Supervisão Humana:** Para cenários críticos ou falhas recorrentes, o modelo pode sinalizar incertezas e solicitar orientação humana. Uma vez que o humano forneça feedback corretivo, o modelo pode incorporar essa lição para seguir em frente.

Essa abordagem iterativa e dinâmica permite que o modelo melhore continuamente, garantindo que ele não seja apenas um sistema de tentativa única, mas sim um que aprende com seus erros durante uma sessão específica.

![Self Correction Mechanism](../../../05-agentic-rag/images/self-correction.png)

## Limites da Agência

Apesar de sua autonomia dentro de uma tarefa, o Agentic RAG não é equivalente à Inteligência Artificial Geral. Suas capacidades “agentic” estão confinadas às ferramentas, fontes de dados e políticas fornecidas pelos desenvolvedores humanos. Ele não pode inventar suas próprias ferramentas ou ultrapassar os limites do domínio que foram estabelecidos. Em vez disso, destaca-se ao orquestrar dinamicamente os recursos disponíveis.

Diferenças importantes em relação a formas mais avançadas de IA incluem:

1. **Autonomia Específica do Domínio:** Sistemas Agentic RAG são focados em alcançar objetivos definidos pelo usuário dentro de um domínio conhecido, empregando estratégias como reescrita de consultas ou seleção de ferramentas para melhorar os resultados.
2. **Dependência de Infraestrutura:** As capacidades do sistema dependem das ferramentas e dados integrados pelos desenvolvedores. Ele não pode ultrapassar esses limites sem intervenção humana.
3. **Respeito aos Limites:** Diretrizes éticas, regras de conformidade e políticas empresariais permanecem muito importantes. A liberdade do agente é sempre limitada por medidas de segurança e mecanismos de supervisão (esperançosamente?).

## Casos de Uso Práticos e Valor

O Agentic RAG se destaca em cenários que exigem refinamento iterativo e precisão:

1. **Ambientes de Alta Precisão:** Em verificações de conformidade, análises regulatórias ou pesquisas jurídicas, o modelo agentic pode verificar repetidamente fatos, consultar múltiplas fontes e reescrever consultas até produzir uma resposta minuciosamente validada.

2. **Interações Complexas com Bancos de Dados:** Ao lidar com dados estruturados, onde consultas frequentemente falham ou precisam de ajustes, o sistema pode refinar autonomamente suas consultas usando Azure SQL ou Microsoft Fabric OneLake, garantindo que a recuperação final esteja alinhada com a intenção do usuário.

3. **Fluxos de Trabalho Prolongados:** Sessões mais longas podem evoluir à medida que novas informações surgem. O Agentic RAG pode incorporar continuamente novos dados, ajustando estratégias conforme aprende mais sobre o problema.

## Governança, Transparência e Confiança

À medida que esses sistemas se tornam mais autônomos em seu raciocínio, a governança e a transparência são cruciais:

- **Raciocínio Explicável:** O modelo pode fornecer um registro auditável das consultas feitas, das fontes consultadas e dos passos de raciocínio seguidos para chegar à conclusão. Ferramentas como Azure AI Content Safety e Azure AI Tracing / GenAIOps podem ajudar a manter a transparência e mitigar riscos.
- **Controle de Viés e Recuperação Balanceada:** Desenvolvedores podem ajustar estratégias de recuperação para garantir que fontes de dados equilibradas e representativas sejam consideradas, auditando regularmente as saídas para detectar vieses ou padrões enviesados usando modelos personalizados para organizações avançadas de ciência de dados com Azure Machine Learning.
- **Supervisão Humana e Conformidade:** Para tarefas sensíveis, a revisão humana continua sendo essencial. O Agentic RAG não substitui o julgamento humano em decisões críticas—ele o complementa ao oferecer opções mais minuciosamente validadas.

Ter ferramentas que forneçam um registro claro das ações é essencial. Sem elas, depurar um processo em várias etapas pode ser muito difícil. Veja abaixo um exemplo da Literal AI (empresa por trás do Chainlit) para uma execução de agente:

![AgentRunExample](../../../05-agentic-rag/images/AgentRunExample.png)

![AgentRunExample2](../../../05-agentic-rag/images/AgentRunExample2.png)

## Conclusão

O Agentic RAG representa uma evolução natural na forma como sistemas de IA lidam com tarefas complexas e intensivas em dados. Ao adotar um padrão de interação em loop, selecionar ferramentas autonomamente e refinar consultas até alcançar um resultado de alta qualidade, o sistema vai além do simples seguimento de prompts estáticos, tornando-se um tomador de decisões mais adaptável e consciente do contexto. Embora ainda limitado por infraestruturas definidas por humanos e diretrizes éticas, essas capacidades agentic permitem interações de IA mais ricas, dinâmicas e, em última análise, mais úteis para empresas e usuários finais.

## Recursos Adicionais

- Implementar Retrieval Augmented Generation (RAG) com Azure OpenAI Service: Saiba como usar seus próprios dados com o Azure OpenAI Service. [Este módulo do Microsoft Learn oferece um guia abrangente sobre como implementar RAG](https://learn.microsoft.com/training/modules/use-own-data-azure-openai)
- Avaliação de aplicativos de IA generativa com Azure AI Foundry: Este artigo aborda a avaliação e comparação de modelos em conjuntos de dados públicos, incluindo [aplicativos de IA agentic e arquiteturas RAG](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [What is Agentic RAG | Weaviate](https://weaviate.io/blog/what-is-agentic-rag)
- [Agentic RAG: A Complete Guide to Agent-Based Retrieval Augmented Generation – News from generation RAG](https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/)
- [Agentic RAG: turbocharge your RAG with query reformulation and self-query! Hugging Face Open-Source AI Cookbook](https://huggingface.co/learn/cookbook/agent_rag)
- [Adding Agentic Layers to RAG](https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U)
- [The Future of Knowledge Assistants: Jerry Liu](https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s)
- [How to Build Agentic RAG Systems](https://www.youtube.com/watch?v=AOSjiXP1jmQ)
- [Using Azure AI Foundry Agent Service to scale your AI agents](https://ignite.microsoft.com/en-US/sessions/BRK102?source=sessions)

### Artigos Acadêmicos

- [2303.17651 Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- [2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- [2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)
```

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.