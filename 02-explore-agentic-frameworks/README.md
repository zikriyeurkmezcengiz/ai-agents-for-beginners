# Explore Ai Agent Frameworks

AI agent frameworks are software platforms designed to simplify the creation, deployment, and management of AI agents. These frameworks provide developers with pre-built components, abstractions, and tools that streamline the development of complex AI systems.

These frameworks help developers focus on the unique aspects of their applications by providing standardized approaches to common challenges in AI agent development. They enhance scalability, accessibility, and efficiency in building AI systems.

## Introduction

This lesson will cover:

- What are AI Agent Frameworks and what do they enable developers to do? 
- How can teams use these to quickly prototype, iterate, and improve my agent’s capabilities?
- What are the difference between the frameworks and tools created by Microsoft ( Autogen / Semantic Kernel / Azure AI Agent Service) 
- Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?
- what is Azure AI Agents service and how is this helping me?

## Learning goals

The goals of this lesson is to help you understand:

- The role of AI Agent Frameworks in AI development.
- How to leverage AI Agent Frameworks to build intelligent agents.
- Key capabilities enabled by AI Agent Frameworks.
- The differences between Autogen, Semantic Kernel, and Azure AI Agent Service.

## What are AI Agent Frameworks and what do they enable developers to do?

Traditional AI Frameworks can help you integrate AI into your apps and make these apps better in the following ways:

- **Personalization**: AI can analyze user behavior and preferences to provide personalized recommendations, content, and experiences.
Example: Streaming services like Netflix use AI to suggest movies and shows based on viewing history, enhancing user engagement and satisfaction.
- **Automation and Efficiency**: AI can automate repetitive tasks, streamline workflows, and improve operational efficiency.
Example: Customer service apps use AI-powered chatbots to handle common inquiries, reducing response times and freeing up human agents for more complex issues.
- **Enhanced User Experience**: AI can improve the overall user experience by providing intelligent features such as voice recognition, natural language processing, and predictive text.
Example: Virtual assistants like Siri and Google Assistant use AI to understand and respond to voice commands, making it easier for users to interact with their devices.

### That all sounds great right, so why we do we need AI Agent Framework?

AI Agent frameworks represent something more than just AI frameworks. They are designed to enable the creation of intelligent agents that can interact with users, other agents, and the environment to achieve specific goals. These agents can exhibit autonomous behavior, make decisions, and adapt to changing conditions. Let's look at some key capabilities enabled by AI Agent Frameworks:

- **Agent Collaboration and Coordination**: Enable the creation of multiple AI agents that can work together, communicate, and coordinate to solve complex tasks.
- **Task Automation and Management**: Provide mechanisms for automating multi-step workflows, task delegation, and dynamic task management among agents.
- **Contextual Understanding and Adaptation**: Equip agents with the ability to understand context, adapt to changing environments, and make decisions based on real-time information.

So in summary, agents allow you to do more, to take automation to the next level, to create more intelligent systems that can adapt and learn from their environment.

## How to quickly prototype, iterate, and improve the agent’s capabilities?

This is fast moving landscape, but there are some things that are common across most AI Agent Frameworks that can help you quickly prototype and iterate namely module components, collaborative tools, and real-time learning. Let's dive into these:

- **Use Modular Components**: AI Frameworks offer pre-built components such as prompts, parsers, and memory management.
- **Leverage Collaborative Tools**: Design agents with specific roles and tasks, enabling them to test and refine collaborative workflows.
- **Learn in Real-Time**: Implement feedback loops where agents learn from interactions and adjust their behavior dynamically.

### Use Modular Components

Frameworks like LangChain and Microsoft Semantic Kernel offer pre-built components such as prompts, parsers, and memory management.

**How teams can use these**: Teams can quickly assemble these components to create a functional prototype without starting from scratch, allowing for rapid experimentation and iteration.

**How it works in practice**: You can use a pre-built parser to extract information from user input, a memory module to store and retrieve data, and a prompt generator to interact with users, all without having to build these components from scratch.

**Example code**. Let's look at an example of how you can use a pre-built parser to extract information from user input:

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

What you can see from this example is how you can leverage a pre-built parser to extract key information from user input, such as the origin, destination, and date of a flight booking request. This modular approach allows you to focus on the high-level logic.

### Leverage Collaborative Tools

Frameworks like CrewAI and Microsoft AutoGen facilitate the creation of multiple agents that can work together.

**How teams can use these**: Teams can design agents with specific roles and tasks, enabling them to test and refine collaborative workflows and improve overall system efficiency.

**How it works in practice**: You can create a team of agents where each agent has a specialized function, such as data retrieval, analysis, or decision-making. These agents can communicate and share information to achieve a common goal, such as answering a user query or completing a task.

**Example code (Autogen)**: 

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

What you see in above code is how you can create a task that involves multiple agents working together to analyze data. Each agent performs a specific function, and the task is executed by coordinating the agents to achieve the desired outcome. By creating dedicated agents with specialized roles, you can improve task efficiency and performance.

### Learn in Real-Time 

Advanced frameworks provide capabilities for real-time context understanding and adaptation. 

**How teams can use these**: Teams can implement feedback loops where agents learn from interactions and adjust their behavior dynamically, leading to continuous improvement and refinement of capabilities.

**How it works in practice**: Agents can analyze user feedback, environmental data, and task outcomes to update their knowledge base, adjust decision-making algorithms, and improve performance over time. This iterative learning process enables agents to adapt to changing conditions and user preferences, enhancing overall system effectiveness.

## What are the differences between the frameworks Autogen, Semantic Kernel and Azure AI Agent Service?

There are many ways to compare these frameworks, but let's look at some key differences in terms of their design, capabilities, and target use cases:

### Autogen

Open-source framework developed by Microsoft Research's AI Frontiers Lab. Focuses on event-driven, distributed agentic applications, enabling multiple LLMs and SLMs, tools, and advanced multi-agent design patterns.

Autogen is built around the core concept of agents, which are autonomous entities that can perceive their environment, make decisions, and take actions to achieve specific goals. Agents communicate through asynchronous messages, allowing them to work independently and in parallel, enhancing system scalability and responsiveness.

Agents are based on the [actor model](https://en.wikipedia.org/wiki/Actor_model). Which according to Wikipedia states that an actor is _the basic building block of concurrent computation. In response to a message it receives, an actor can: make local decisions, create more actors, send more messages, and determine how to respond to the next message received_.

**Use Cases**: Automating code generation, data analysis tasks, and building custom agents for planning and research functions.

**Core Concepts**:
> TODO, explain concepts and code examples 

### Semantic Kernel + Agent Framework

Semantic Kernel consists of two things, the Semantic Kernel Agent Framework and the Semantic Kernel itself.

Let's first talk about the Semantic Kernel. It has the following core concepts:

- **Connections**: This is an interface with external Ai services and data sources.

    ```csharp
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    Here you have a simple example of how you can create a kernel and add a chat completion service. Semantic Kernel creates a connection to an external AI service, in this case, Azure OpenAI Chat Completion.

- **Plugins**: Encapsulate functions that an application can use. There are both ready-made plugins and plugins you can create yourself. There's a concept here called "Semantic functions". What makes it semantic is that you provide it semantic information that helps Semantic Kernel figure out that this function needs to be called. Here's an example:

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // Register the function
    kernel.CreateSemanticFunction(
        promptTemplate: skPrompt,
        functionName: "SummarizeText",
        pluginName: "SemanticFunctions"
    );
    ```

    Here, you first have a template prompt `skPrompt` that leaves room for the user to input text, `$userInput`. Then you register the function `SummarizeText` with the plugin `SemanticFunctions`. Note the name of the function that helps Semantic Kernel understand what the function does and when it should be called.

- **Native function**: There's also native functions that the framework can call directly to carry out the task. Here's an example of such a function retrieving the content from a file:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";
    
    var nativeFunctions = new NativeFunctions();
    kernel.ImportFunctions(nativeFunctions, plugInName);
    ```

- **Planner**: The planner orchestrates execution plans and strategies based on user input. The idea is to express how things should be carried out which then surveys as an instruction for Semantic Kernel to follow. It then invoke the necessary functions to carry out the task. Here' an example of such a plan:

    ```csharp
    string planDefinition = "Read content from a local file and summarize the content.";
    SequentialPlanner sequentialPlanner = new SequentialPlanner(kernel);
    
    string assetsFolder = @"../../assets";
    string fileName = Path.Combine(assetsFolder,"docs","06_SemanticKernel", "aci_documentation.txt");
    
    ContextVariables contextVariables = new ContextVariables();
    contextVariables.Add("fileName", fileName);
    
    var customPlan = await sequentialPlanner.CreatePlanAsync(planDefinition);
    
    // Execute the plan
    KernelResult kernelResult = await kernel.RunAsync(contextVariables, customPlan);
    Console.WriteLine($"Summarization: {kernelResult.GetValue<string>()}");
    ```

    Note especially `planDefinition` which is a simple instruction for the planner to follow. The appropriate functions are then called based on this plan, in this case our semantic function `SummarizeText` and the native function `RetrieveLocalFile`.
- **Memory**:  Abstracts and simplifies context management for AI apps. The idea with memory is that this is something the LLM should know about. You can store this information in a vector store which ends up being an in-memory database or a vector database or similar. Here's an example of a very simplified scenario where *facts* are added to the memory:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/en-us/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/en-us/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    These facts are then stored in the memory collection `SummarizedAzureDocs`. This is a very simplified example, but you can see how you can store information in the memory for the LLM to use.

So that's the basics of the Semantic Kernel framework, what about the Agent Framework?

**Core concepts for Semantic Kernel Agent Framework**:

TODO, add core concepts and code examples

 
### Azure AI Agent Service


> TODO check if this is the correct information, add core concepts and code examples

Azure AI Agent Service is a more recent addition, introduced at Microsoft Ignite 2024. It allows for the development and deployment of AI agents with more flexible models, such as directly calling open-source LLMs like Llama 3, Mistral, and Cohere3. 

Azure AI Agent Service provides stronger enterprise security mechanisms and data storage methods, making it suitable for enterprise applications. 

It works out-of-the-box with multi-agent orchestration frameworks like AutoGen and Semantic Kernel. 

This service is currently in Public Preview and supports Python and C# for building agents

**Core concepts**: Azure AI Agent Service focuses on the following core concepts:

- **Modularity**: Allows developers to define various types of agents for specific tasks, making it easier to adapt the application as requirements evolve or new technologies emerge.
- **Collaboration**: Multiple agents can collaborate on tasks, creating a more sophisticated system with distributed intelligence.
- **Human-Agent** Collaboration: Human-in-the-loop interactions allow agents to work alongside humans to augment decision-making processes4.
- **Process Orchestration**: Agents can coordinate different tasks across systems, tools, and APIs, helping to automate end-to-end processes

**Use Cases**: Azure AI Agent Service is designed for enterprise applications that require secure, scalable, and flexible AI agent deployment.

## What's the difference between these frameworks?

It does sound like there is a lot of overlap between these frameworks, but there are some key differences in terms of their design, capabilities, and target use cases:

- **Autogen**: Focuses on event-driven, distributed agentic applications, enabling multiple LLMs and SLMs, tools, and advanced multi-agent design patterns.
- **Semantic Kernel**: Focuses on understanding and generating human-like text content by capturing deeper semantic meanings. It is designed to automate complex workflows and initiate tasks based on project goals.
- **Azure AI Agent Service**: Provides more flexible models, such as directly calling open-source LLMs like Llama 3, Mistral, and Cohere3. It offers stronger enterprise security mechanisms and data storage methods, making it suitable for enterprise applications.

Still not sure which one to choose? 

### Use Cases

Let's see if we can help you by going through some common use cases:

> Q: My team is working on a project that involves automating code generation and data analysis tasks. Which framework should we use?
>
>A: Autogen would be a good choice for this scenario, as it focuses on event-driven, distributed agentic applications and supports advanced multi-agent design patterns.

> Q: What makes autogen a better choice than Semantic Kernel and Azure AI Agent Service for this use case?
>
> A: Autogen is specifically designed for event-driven, distributed agentic applications, making it well-suited for automating code generation and data analysis tasks. It provides the necessary tools and capabilities to build complex multi-agent systems efficiently.

>Q: Sounds like Azure AI Agent Service could work here too, it tools like code generation and more?
>
> A: Yes, Azure AI Agent Service also supports code generation and data analysis tasks, but it may be more suitable for enterprise applications that require secure, scalable, and flexible AI agent deployment. Autogen is more focused on event-driven, distributed agentic applications and advanced multi-agent design patterns.

> Q: so you are saying if I want to go enterprise, I should go with Azure AI Agent Service?
>
> A: Yes, Azure AI Agent Service is designed for enterprise applications that require secure, scalable, and flexible AI agent deployment. It offers stronger enterprise security mechanisms and data storage methods, making it suitable for enterprise use cases.

Let's summarize the key differences in a table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Autogen | Event-driven, distributed agentic applications | Agents, Personas, Functions, Data | Code generation, data analysis tasks |
| Semantic Kernel | Understanding and generating human-like text content | Agents, Modular Components, Collaboration | Natural language understanding, content generation |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

What's the ideal use case for each of these frameworks?

- **Autogen**: Event-driven, distributed agentic applications, advanced multi-agent design patterns. Ideal for automating code generation, data analysis tasks.
- **Semantic Kernel**: Understanding and generating human-like text content, automating complex workflows, initiating tasks based on project goals. Ideal for natural language understanding, content generation. 
- **Azure AI Agent Service**: Flexible models, enterprise security mechanisms, data storage methods. Ideal for secure, scalable, and flexible AI agent deployment in enterprise applications.

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?

## What is Azure AI Agents service and how is this helping me?

## References

- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)
- [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/)
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp)
- [4] - [Azure AI Agent service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)