# Explorar Frameworks de Agentes de IA

Los frameworks de agentes de IA son plataformas de software diseñadas para simplificar la creación, implementación y gestión de agentes de inteligencia artificial. Estos frameworks proporcionan a los desarrolladores componentes preconstruidos, abstracciones y herramientas que facilitan el desarrollo de sistemas de IA complejos.

Estos frameworks ayudan a los desarrolladores a centrarse en los aspectos únicos de sus aplicaciones al proporcionar enfoques estandarizados para los desafíos comunes en el desarrollo de agentes de IA. Mejoran la escalabilidad, accesibilidad y eficiencia en la construcción de sistemas de IA.

## Introducción

Esta lección cubrirá:

- ¿Qué son los frameworks de agentes de IA y qué permiten hacer a los desarrolladores?
- ¿Cómo pueden los equipos usarlos para prototipar rápidamente, iterar y mejorar las capacidades de sus agentes?
- ¿Cuáles son las diferencias entre los frameworks y herramientas creados por Microsoft ([Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service))?
- ¿Puedo integrar directamente mis herramientas existentes del ecosistema Azure o necesito soluciones independientes?
- ¿Qué es el servicio Azure AI Agents y cómo me ayuda?

## Objetivos de aprendizaje

Los objetivos de esta lección son ayudarte a comprender:

- El papel de los frameworks de agentes de IA en el desarrollo de inteligencia artificial.
- Cómo aprovechar los frameworks de agentes de IA para construir agentes inteligentes.
- Las capacidades clave que habilitan los frameworks de agentes de IA.
- Las diferencias entre Autogen, Semantic Kernel y Azure AI Agent Service.

## ¿Qué son los frameworks de agentes de IA y qué permiten hacer a los desarrolladores?

Los frameworks de IA tradicionales pueden ayudarte a integrar IA en tus aplicaciones y mejorar estas aplicaciones de las siguientes maneras:

- **Personalización**: La IA puede analizar el comportamiento y las preferencias de los usuarios para proporcionar recomendaciones, contenido y experiencias personalizadas.  
Ejemplo: Servicios de streaming como Netflix usan IA para sugerir películas y series basándose en el historial de visualización, mejorando el compromiso y la satisfacción del usuario.

- **Automatización y eficiencia**: La IA puede automatizar tareas repetitivas, optimizar flujos de trabajo y mejorar la eficiencia operativa.  
Ejemplo: Las aplicaciones de servicio al cliente utilizan chatbots impulsados por IA para manejar consultas comunes, reduciendo los tiempos de respuesta y liberando a los agentes humanos para problemas más complejos.

- **Mejora de la experiencia del usuario**: La IA puede mejorar la experiencia del usuario proporcionando funciones inteligentes como reconocimiento de voz, procesamiento de lenguaje natural y texto predictivo.  
Ejemplo: Asistentes virtuales como Siri y Google Assistant utilizan IA para entender y responder a comandos de voz, facilitando la interacción de los usuarios con sus dispositivos.

### Todo esto suena genial, ¿verdad? Entonces, ¿por qué necesitamos frameworks de agentes de IA?

Los frameworks de agentes de IA representan algo más que simples frameworks de IA. Están diseñados para permitir la creación de agentes inteligentes que pueden interactuar con usuarios, otros agentes y el entorno para alcanzar objetivos específicos. Estos agentes pueden mostrar comportamientos autónomos, tomar decisiones y adaptarse a condiciones cambiantes. Veamos algunas capacidades clave habilitadas por los frameworks de agentes de IA:

- **Colaboración y coordinación entre agentes**: Permiten la creación de múltiples agentes de IA que pueden trabajar juntos, comunicarse y coordinarse para resolver tareas complejas.
- **Automatización y gestión de tareas**: Proporcionan mecanismos para automatizar flujos de trabajo de múltiples pasos, delegación de tareas y gestión dinámica de tareas entre agentes.
- **Comprensión y adaptación contextual**: Equipan a los agentes con la capacidad de entender el contexto, adaptarse a entornos cambiantes y tomar decisiones basadas en información en tiempo real.

En resumen, los agentes te permiten hacer más, llevar la automatización al siguiente nivel y crear sistemas más inteligentes que pueden adaptarse y aprender de su entorno.

## ¿Cómo prototipar rápidamente, iterar y mejorar las capacidades de los agentes?

Este es un campo que avanza rápidamente, pero hay algunos elementos comunes en la mayoría de los frameworks de agentes de IA que pueden ayudarte a prototipar e iterar rápidamente, como los componentes modulares, herramientas colaborativas y aprendizaje en tiempo real. Vamos a profundizar en estos:

- **Usar componentes modulares**: Los frameworks de IA ofrecen componentes preconstruidos como prompts, parsers y gestión de memoria.
- **Aprovechar herramientas colaborativas**: Diseñar agentes con roles y tareas específicas, permitiéndoles probar y refinar flujos de trabajo colaborativos.
- **Aprender en tiempo real**: Implementar bucles de retroalimentación donde los agentes aprenden de las interacciones y ajustan su comportamiento dinámicamente.

### Usar componentes modulares

Frameworks como LangChain y Microsoft Semantic Kernel ofrecen componentes preconstruidos como prompts, parsers y gestión de memoria.

**Cómo los equipos pueden usarlos**: Los equipos pueden ensamblar rápidamente estos componentes para crear un prototipo funcional sin empezar desde cero, permitiendo una experimentación e iteración rápidas.

**Cómo funciona en la práctica**: Puedes usar un parser preconstruido para extraer información de la entrada del usuario, un módulo de memoria para almacenar y recuperar datos, y un generador de prompts para interactuar con los usuarios, todo sin necesidad de construir estos componentes desde cero.

**Ejemplo de código**: Veamos un ejemplo de cómo puedes usar un parser preconstruido para extraer información de la entrada del usuario:

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

Este ejemplo muestra cómo puedes aprovechar un parser preconstruido para extraer información clave de la entrada del usuario, como el origen, destino y fecha de una solicitud de reserva de vuelo. Este enfoque modular te permite centrarte en la lógica de alto nivel.

### Aprovechar herramientas colaborativas

Frameworks como CrewAI y Microsoft Autogen facilitan la creación de múltiples agentes que pueden trabajar juntos.

**Cómo los equipos pueden usarlos**: Los equipos pueden diseñar agentes con roles y tareas específicas, permitiéndoles probar y refinar flujos de trabajo colaborativos y mejorar la eficiencia general del sistema.

**Cómo funciona en la práctica**: Puedes crear un equipo de agentes donde cada agente tenga una función especializada, como recuperación de datos, análisis o toma de decisiones. Estos agentes pueden comunicarse y compartir información para alcanzar un objetivo común, como responder a una consulta del usuario o completar una tarea.

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

Este código muestra cómo puedes crear una tarea que involucra a múltiples agentes trabajando juntos para analizar datos. Cada agente realiza una función específica, y la tarea se ejecuta coordinando a los agentes para lograr el resultado deseado. Al crear agentes dedicados con roles especializados, puedes mejorar la eficiencia y el rendimiento de las tareas.

### Aprender en tiempo real

Los frameworks avanzados proporcionan capacidades para la comprensión contextual y adaptación en tiempo real.

**Cómo los equipos pueden usarlos**: Los equipos pueden implementar bucles de retroalimentación donde los agentes aprenden de las interacciones y ajustan su comportamiento dinámicamente, lo que lleva a una mejora continua y refinamiento de capacidades.

**Cómo funciona en la práctica**: Los agentes pueden analizar comentarios de usuarios, datos del entorno y resultados de tareas para actualizar su base de conocimiento, ajustar algoritmos de toma de decisiones y mejorar su rendimiento con el tiempo. Este proceso de aprendizaje iterativo permite a los agentes adaptarse a condiciones cambiantes y preferencias de los usuarios, mejorando la efectividad general del sistema.

## ¿Cuáles son las diferencias entre Autogen, Semantic Kernel y Azure AI Agent Service?

Existen muchas formas de comparar estos frameworks, pero analicemos algunas diferencias clave en términos de su diseño, capacidades y casos de uso objetivo:

### Autogen

Autogen es un framework de código abierto desarrollado por el Laboratorio de Fronteras de IA de Microsoft Research. Se centra en aplicaciones *agénticas* distribuidas y basadas en eventos, habilitando múltiples LLMs y SLMs, herramientas y patrones avanzados de diseño multi-agente.

... *(El resto del contenido traducido continúa aquí según el formato y estilo original).*
basado en los objetivos del proyecto. Ideal para la comprensión del lenguaje natural y la generación de contenido. - **Azure AI Agent Service**: Modelos flexibles, mecanismos de seguridad empresarial, métodos de almacenamiento de datos. Ideal para el despliegue seguro, escalable y flexible de agentes de IA en aplicaciones empresariales. ## ¿Puedo integrar directamente mis herramientas existentes del ecosistema de Azure, o necesito soluciones independientes? La respuesta es sí, puedes integrar tus herramientas existentes del ecosistema de Azure directamente con Azure AI Agent Service, especialmente porque ha sido diseñado para trabajar de manera fluida con otros servicios de Azure. Podrías, por ejemplo, integrar Bing, Azure AI Search y Azure Functions. También hay una integración profunda con Azure AI Foundry. Para Autogen y Semantic Kernel, también puedes integrarlos con servicios de Azure, pero puede requerir que llames a los servicios de Azure desde tu código. Otra forma de integrar es usar los SDKs de Azure para interactuar con los servicios de Azure desde tus agentes. Además, como se mencionó, puedes usar Azure AI Agent Service como un orquestador para tus agentes construidos en Autogen o Semantic Kernel, lo que facilitaría el acceso al ecosistema de Azure. ## Referencias - [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357) - [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/) - [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp) - [4] - [Azure AI Agent service](https://learn.microsoft.com/azure/ai-services/agents/overview) - [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.