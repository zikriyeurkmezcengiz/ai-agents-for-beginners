```markdown
# Explora los Marcos de Trabajo para Agentes de IA

Los marcos de trabajo para agentes de IA son plataformas de software diseñadas para simplificar la creación, implementación y gestión de agentes de IA. Estos marcos proporcionan a los desarrolladores componentes preconstruidos, abstracciones y herramientas que agilizan el desarrollo de sistemas de IA complejos.

Estos marcos ayudan a los desarrolladores a centrarse en los aspectos únicos de sus aplicaciones al proporcionar enfoques estandarizados para los desafíos comunes en el desarrollo de agentes de IA. Mejoran la escalabilidad, accesibilidad y eficiencia en la construcción de sistemas de IA.

## Introducción

Esta lección cubrirá:

- ¿Qué son los marcos de trabajo para agentes de IA y qué permiten hacer a los desarrolladores?
- ¿Cómo pueden los equipos utilizarlos para prototipar rápidamente, iterar y mejorar las capacidades de mis agentes?
- ¿Cuáles son las diferencias entre los marcos y herramientas creados por Microsoft ([Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service))?
- ¿Puedo integrar directamente mis herramientas existentes del ecosistema de Azure, o necesito soluciones independientes?
- ¿Qué es el servicio Azure AI Agents y cómo me ayuda?

## Objetivos de aprendizaje

Los objetivos de esta lección son ayudarte a comprender:

- El papel de los marcos de trabajo para agentes de IA en el desarrollo de IA.
- Cómo aprovechar los marcos de trabajo para agentes de IA para construir agentes inteligentes.
- Capacidades clave habilitadas por los marcos de trabajo para agentes de IA.
- Las diferencias entre Autogen, Semantic Kernel y Azure AI Agent Service.

## ¿Qué son los marcos de trabajo para agentes de IA y qué permiten hacer a los desarrolladores?

Los marcos de trabajo tradicionales de IA pueden ayudarte a integrar IA en tus aplicaciones y mejorar estas aplicaciones de las siguientes maneras:

- **Personalización**: La IA puede analizar el comportamiento y las preferencias de los usuarios para proporcionar recomendaciones, contenido y experiencias personalizadas.  
Ejemplo: Los servicios de streaming como Netflix utilizan IA para sugerir películas y programas basados en el historial de visualización, mejorando el compromiso y la satisfacción del usuario.
- **Automatización y eficiencia**: La IA puede automatizar tareas repetitivas, optimizar flujos de trabajo y mejorar la eficiencia operativa.  
Ejemplo: Las aplicaciones de servicio al cliente utilizan chatbots impulsados por IA para manejar consultas comunes, reduciendo los tiempos de respuesta y liberando a los agentes humanos para problemas más complejos.
- **Experiencia de usuario mejorada**: La IA puede mejorar la experiencia general del usuario al proporcionar funciones inteligentes como reconocimiento de voz, procesamiento de lenguaje natural y texto predictivo.  
Ejemplo: Asistentes virtuales como Siri y Google Assistant utilizan IA para entender y responder a comandos de voz, facilitando la interacción de los usuarios con sus dispositivos.

### Suena genial, ¿verdad? Entonces, ¿por qué necesitamos marcos de trabajo para agentes de IA?

Los marcos de trabajo para agentes de IA representan algo más que simples marcos de IA. Están diseñados para habilitar la creación de agentes inteligentes que puedan interactuar con usuarios, otros agentes y el entorno para lograr objetivos específicos. Estos agentes pueden exhibir comportamientos autónomos, tomar decisiones y adaptarse a condiciones cambiantes. Veamos algunas capacidades clave habilitadas por los marcos de trabajo para agentes de IA:

- **Colaboración y coordinación entre agentes**: Permiten la creación de múltiples agentes de IA que pueden trabajar juntos, comunicarse y coordinarse para resolver tareas complejas.
- **Automatización y gestión de tareas**: Proporcionan mecanismos para automatizar flujos de trabajo de varios pasos, delegación de tareas y gestión dinámica de tareas entre agentes.
- **Comprensión y adaptación contextual**: Equipan a los agentes con la capacidad de entender el contexto, adaptarse a entornos cambiantes y tomar decisiones basadas en información en tiempo real.

En resumen, los agentes te permiten hacer más, llevar la automatización al siguiente nivel, y crear sistemas más inteligentes que puedan adaptarse y aprender de su entorno.

## ¿Cómo prototipar rápidamente, iterar y mejorar las capacidades del agente?

Este es un campo en constante evolución, pero hay algunos aspectos comunes en la mayoría de los marcos de trabajo para agentes de IA que pueden ayudarte a prototipar e iterar rápidamente, como los componentes modulares, herramientas colaborativas y el aprendizaje en tiempo real. Profundicemos en estos aspectos:

- **Usa componentes modulares**: Los marcos de IA ofrecen componentes preconstruidos como prompts, analizadores y gestión de memoria.
- **Aprovecha herramientas colaborativas**: Diseña agentes con roles y tareas específicas, lo que permite probar y refinar flujos de trabajo colaborativos.
- **Aprende en tiempo real**: Implementa bucles de retroalimentación donde los agentes aprenden de las interacciones y ajustan su comportamiento dinámicamente.

### Usa componentes modulares

Marcos como LangChain y Microsoft Semantic Kernel ofrecen componentes preconstruidos como prompts, analizadores y gestión de memoria.

**Cómo pueden usarlo los equipos**: Los equipos pueden ensamblar rápidamente estos componentes para crear un prototipo funcional sin comenzar desde cero, permitiendo una experimentación e iteración rápidas.

**Cómo funciona en la práctica**: Puedes usar un analizador preconstruido para extraer información de la entrada del usuario, un módulo de memoria para almacenar y recuperar datos, y un generador de prompts para interactuar con los usuarios, todo sin necesidad de construir estos componentes desde cero.

**Ejemplo de código**. Veamos un ejemplo de cómo puedes usar un analizador preconstruido para extraer información de la entrada del usuario:

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

Lo que puedes observar en este ejemplo es cómo aprovechar un analizador preconstruido para extraer información clave de la entrada del usuario, como el origen, destino y fecha de una solicitud de reserva de vuelo. Este enfoque modular te permite centrarte en la lógica de alto nivel.

### Aprovecha herramientas colaborativas

Marcos como CrewAI y Microsoft Autogen facilitan la creación de múltiples agentes que pueden trabajar juntos.

**Cómo pueden usarlo los equipos**: Los equipos pueden diseñar agentes con roles y tareas específicas, lo que les permite probar y refinar flujos de trabajo colaborativos y mejorar la eficiencia general del sistema.

**Cómo funciona en la práctica**: Puedes crear un equipo de agentes donde cada agente tenga una función especializada, como recuperación de datos, análisis o toma de decisiones. Estos agentes pueden comunicarse y compartir información para lograr un objetivo común, como responder a una consulta del usuario o completar una tarea.

**Ejemplo de código (Autogen)**:

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

Lo que ves en el código anterior es cómo puedes crear una tarea que involucra múltiples agentes trabajando juntos para analizar datos. Cada agente realiza una función específica, y la tarea se ejecuta coordinando los agentes para lograr el resultado deseado. Al crear agentes dedicados con roles especializados, puedes mejorar la eficiencia y el rendimiento de las tareas.

### Aprende en tiempo real

Los marcos avanzados proporcionan capacidades para la comprensión del contexto y la adaptación en tiempo real.

**Cómo pueden usarlo los equipos**: Los equipos pueden implementar bucles de retroalimentación donde los agentes aprenden de las interacciones y ajustan su comportamiento dinámicamente, lo que lleva a una mejora continua y refinamiento de capacidades.

**Cómo funciona en la práctica**: Los agentes pueden analizar la retroalimentación del usuario, datos del entorno y resultados de tareas para actualizar su base de conocimiento, ajustar algoritmos de toma de decisiones y mejorar el rendimiento con el tiempo. Este proceso de aprendizaje iterativo permite a los agentes adaptarse a condiciones cambiantes y preferencias del usuario, mejorando la efectividad general del sistema.

## ¿Cuáles son las diferencias entre los marcos Autogen, Semantic Kernel y Azure AI Agent Service?

Existen muchas formas de comparar estos marcos, pero veamos algunas diferencias clave en términos de su diseño, capacidades y casos de uso objetivo:

### Autogen

Un marco de trabajo de código abierto desarrollado por el laboratorio AI Frontiers de Microsoft Research. Se centra en aplicaciones *agénticas* distribuidas y basadas en eventos, permitiendo múltiples LLMs y SLMs, herramientas y patrones avanzados de diseño multiagente.

Autogen se basa en el concepto central de agentes, que son entidades autónomas capaces de percibir su entorno, tomar decisiones y realizar acciones para lograr objetivos específicos. Los agentes se comunican mediante mensajes asincrónicos, lo que les permite trabajar de manera independiente y en paralelo, mejorando la escalabilidad y capacidad de respuesta del sistema.

Los agentes están basados en el [modelo de actor](https://en.wikipedia.org/wiki/Actor_model). Según Wikipedia, un actor es _el bloque de construcción básico de la computación concurrente. En respuesta a un mensaje recibido, un actor puede: tomar decisiones locales, crear más actores, enviar más mensajes y determinar cómo responder al próximo mensaje recibido_.

**Casos de uso**: Automatización de generación de código, tareas de análisis de datos y construcción de agentes personalizados para funciones de planificación e investigación.

Aquí hay algunos conceptos centrales importantes de Autogen:

- **Agentes**. Un agente es una entidad de software que: 
  - **Se comunica mediante mensajes**, que pueden ser sincrónicos o asincrónicos.
  - **Mantiene su propio estado**, que puede ser modificado por mensajes entrantes.
  - **Realiza acciones** en respuesta a mensajes recibidos o cambios en su estado. Estas acciones pueden modificar el estado del agente y producir efectos externos, como actualizar registros de mensajes, enviar nuevos mensajes, ejecutar código o realizar llamadas a API.

  Aquí tienes un pequeño fragmento de código en el que creas tu propio agente con capacidades de chat:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    En el código anterior, `MyAssistant` has been created and inherits from `RoutedAgent`. It has a message handler that prints the content of the message and then sends a response using the `AssistantAgent` delegate. Especially note how we assign to `self._delegate` an instance of `AssistantAgent`, que es un agente preconstruido que puede manejar completaciones de chat.

    Informemos a Autogen sobre este tipo de agente y pongamos en marcha el programa a continuación:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    En el código anterior, el agente se registra con el runtime y luego se envía un mensaje al agente, lo que resulta en la salida siguiente:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multiagentes**. Autogen admite la creación de múltiples agentes que pueden trabajar juntos para lograr tareas complejas. Los agentes pueden comunicarse, compartir información y coordinar sus acciones para resolver problemas de manera más eficiente. Para crear un sistema multiagente, puedes definir diferentes tipos de agentes con funciones y roles especializados, como recuperación de datos, análisis, toma de decisiones e interacción con el usuario. Veamos cómo se ve tal creación para tener una idea:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    Arriba tenemos un `GroupChatManager` que está registrado con el runtime. Este gestor es responsable de coordinar las interacciones entre diferentes tipos de agentes, como escritores, ilustradores, editores y usuarios.

- **Runtime del agente**. El marco proporciona un entorno de runtime, habilitando la comunicación entre agentes, gestionando sus identidades y ciclos de vida, y aplicando límites de seguridad y privacidad. Esto significa que puedes ejecutar tus agentes en un entorno seguro y controlado, asegurando que puedan interactuar de manera segura y eficiente. Hay dos runtimes de interés:
  - **Runtime independiente**. Es una buena opción para aplicaciones de un solo proceso donde todos los agentes están implementados en el mismo lenguaje de programación y se ejecutan en el mismo proceso. Aquí tienes una ilustración de cómo funciona:
  
  ![Runtime independiente](https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg)   
Pila de aplicaciones

    *Los agentes se comunican mediante mensajes a través del runtime, y el runtime gestiona el ciclo de vida de los agentes.*

  - **Runtime distribuido**, es adecuado para aplicaciones multiproceso donde los agentes pueden estar implementados en diferentes lenguajes de programación y ejecutarse en diferentes máquinas. Aquí tienes una ilustración de cómo funciona:
  
  ![Runtime distribuido](https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg)

## Semantic Kernel + Marco de Trabajo para Agentes

Semantic Kernel consta de dos partes: el marco de trabajo para agentes Semantic Kernel y el propio Semantic Kernel.

Primero hablemos del Semantic Kernel. Tiene los siguientes conceptos centrales:

- **Conexiones**: Es una interfaz con servicios de IA externos y fuentes de datos.

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

    Aquí tienes un ejemplo sencillo de cómo puedes crear un kernel y agregar un servicio de completado de chat. Semantic Kernel crea una conexión a un servicio de IA externo, en este caso, Azure OpenAI Chat Completion.

- **Plugins**: Encapsulan funciones que una aplicación puede usar. Hay tanto plugins predefinidos como plugins que puedes crear tú mismo. Hay un concepto aquí llamado "funciones semánticas". Lo que las hace semánticas es que proporcionas información semántica que ayuda a Semantic Kernel a determinar que esta función necesita ser llamada. Aquí tienes un ejemplo:

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

    Aquí, primero tienes un prompt de plantilla `skPrompt` that leaves room for the user to input text, `$userInput`. Then you register the function `SummarizeText` with the plugin `SemanticFunctions`. Nota el nombre de la función que ayuda a Semantic Kernel a entender qué hace la función y cuándo debe ser llamada.

- **Función nativa**: También hay funciones nativas que el marco puede llamar directamente para llevar a cabo la tarea. Aquí tienes un ejemplo de una función que recupera el contenido de un archivo:

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

- **Planificador**: El planificador orquesta planes de ejecución y estrategias basadas en la entrada del usuario. La idea es expresar cómo deben llevarse a cabo las cosas, lo que luego sirve como instrucción para que Semantic Kernel lo siga. Luego invoca las funciones necesarias para llevar a cabo la tarea. Aquí tienes un ejemplo de tal plan:

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

    Nota especialmente `planDefinition` which is a simple instruction for the planner to follow. The appropriate functions are then called based on this plan, in this case our semantic function `SummarizeText` and the native function `RetrieveLocalFile`.
- **Memoria**: Abstrae y simplifica la gestión del contexto para aplicaciones de IA. La idea de la memoria es que esto es algo que el LLM debería conocer. Puedes almacenar esta información en un vector store, que termina siendo una base de datos en memoria o una base de datos vectorial o similar. Aquí tienes un ejemplo de un escenario muy simplificado donde se agregan *hechos* a la memoria:

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

    Estos hechos luego se almacenan en la colección de memoria `SummarizedAzureDocs`. Este es un ejemplo muy simplificado, pero puedes ver cómo puedes almacenar información en la memoria para que el LLM la utilice.

Entonces, esas son las bases del marco Semantic Kernel, ¿qué hay del marco de trabajo para agentes?
 
## Azure AI Agent Service

Azure AI Agent Service es una adición más reciente, presentada en Microsoft Ignite 2024. Permite el desarrollo y la implementación de agentes de IA con modelos más flexibles, como llamar directamente a LLMs de código abierto como Llama 3, Mistral y Cohere.

Azure AI Agent Service proporciona mecanismos de seguridad empresarial más sólidos y métodos de almacenamiento de datos, lo que lo hace adecuado para aplicaciones empresariales. 

Funciona directamente con marcos de orquestación multiagente como Autogen y Semantic Kernel. 

Este servicio está actualmente en Public Preview y admite Python y C# para construir agentes.

### Conceptos centrales

Azure AI Agent Service tiene los siguientes conceptos centrales:

- **Agente**. Azure AI Agent Service se integra con Azure AI Foundry. Dentro de AI Foundry, un agente de IA actúa como un microservicio "inteligente" que puede usarse para responder preguntas (RAG), realizar acciones o automatizar completamente flujos de trabajo. Logra esto combinando el poder de los modelos de IA generativa con herramientas que le permiten acceder e interactuar con fuentes de datos del mundo real. Aquí tienes un ejemplo de un agente:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    En este ejemplo, se crea un agente con el modelo `gpt-4o-mini`, a name `my-agent`, and instructions `You are helpful agent`. El agente está equipado con herramientas y recursos para realizar tareas de interpretación de código.

- **Hilo y mensajes**. El hilo es otro concepto importante. Representa una conversación o interacción entre un agente y un usuario. Los hilos pueden usarse para rastrear el progreso de una conversación, almacenar información de contexto y gestionar el estado de la interacción. Aquí tienes un ejemplo de un hilo:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    En el código anterior, se crea un hilo. Luego, se envía un mensaje al hilo. Al llamar a `create_and_process_run`, se le pide al agente que realice un trabajo en el hilo. Finalmente, se recuperan y registran los mensajes para ver la respuesta del agente. Los mensajes indican el progreso de la conversación entre el usuario y el agente. También es importante entender que los mensajes pueden ser de diferentes tipos, como texto, imagen o archivo, que es el resultado del trabajo del agente, por ejemplo, una imagen o una respuesta en texto. Como desarrollador, luego puedes usar esta información para procesar aún más la respuesta o presentarla al usuario.

- **Integración con otros marcos de IA**. Azure AI Agent Service puede interactuar con otros marcos como Autogen y Semantic Kernel, lo que significa que puedes construir parte de tu aplicación en uno de estos marcos y, por ejemplo, usar el servicio de agente como orquestador, o puedes construir todo en el servicio de agente.

**Casos de uso**: Azure AI Agent Service está diseñado para aplicaciones empresariales que requieren una implementación segura, escalable y flexible de agentes de IA.

## ¿Cuál es la diferencia entre estos marcos?

Parece que hay mucho solapamiento entre estos marcos, pero hay algunas diferencias clave en términos de su diseño, capacidades y casos de uso objetivo:

- **Autogen**: Se centra en aplicaciones *agénticas* distribuidas y basadas en eventos, habilitando múltiples LLMs y SLMs, herramientas y patrones avanzados de diseño multiagente.
- **Semantic Kernel**: Se centra en comprender y generar contenido textual similar al humano al capturar significados semánticos más profundos. Está diseñado para automatizar flujos de trabajo complejos e iniciar tareas basadas en objetivos de proyectos.
- **Azure AI Agent Service**: Ofrece modelos más flexibles, como llamar directamente a LLMs de código abierto como Llama 3, Mistral y Cohere. Proporciona mecanismos de seguridad empresarial más sólidos y métodos de almacenamiento de datos, lo que lo hace adecuado para aplicaciones empresariales.

¿Todavía no estás seguro de cuál elegir?

### Casos de uso

Veamos si podemos ayudarte revisando algunos casos de uso comunes:

> P: Mi equipo está trabajando en un proyecto que implica la automatización de la generación de código y tareas de análisis de datos.
basado en los objetivos del proyecto. Ideal para la comprensión del lenguaje natural, generación de contenido.  
- **Azure AI Agent Service**: Modelos flexibles, mecanismos de seguridad empresarial, métodos de almacenamiento de datos. Ideal para el despliegue seguro, escalable y flexible de agentes de IA en aplicaciones empresariales.  

## ¿Puedo integrar directamente mis herramientas existentes del ecosistema de Azure, o necesito soluciones independientes?  
La respuesta es sí, puedes integrar tus herramientas existentes del ecosistema de Azure directamente con Azure AI Agent Service, especialmente porque ha sido diseñado para trabajar de manera fluida con otros servicios de Azure. Por ejemplo, podrías integrar Bing, Azure AI Search y Azure Functions. También hay una integración profunda con Azure AI Foundry.  

Para Autogen y Semantic Kernel, también puedes integrarlos con servicios de Azure, pero puede requerir que llames a los servicios de Azure desde tu código. Otra forma de integrar es usar los SDKs de Azure para interactuar con los servicios de Azure desde tus agentes.  

Además, como se mencionó, puedes usar Azure AI Agent Service como un orquestador para tus agentes construidos en Autogen o Semantic Kernel, lo que proporcionaría un acceso fácil al ecosistema de Azure.  

## Referencias  
- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)  
- [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/)  
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp)  
- [4] - [Azure AI Agent service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)  
- [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)  

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.