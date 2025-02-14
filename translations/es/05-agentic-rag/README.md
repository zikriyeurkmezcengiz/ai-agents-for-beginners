# Agentic RAG

Esta lección ofrece una visión completa de Agentic Retrieval-Augmented Generation (Agentic RAG), un paradigma emergente de IA en el que los modelos de lenguaje grandes (LLMs) planifican de forma autónoma sus próximos pasos mientras extraen información de fuentes externas. A diferencia de los patrones estáticos de recuperación y lectura, Agentic RAG implica llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas. El sistema evalúa los resultados, refina consultas, invoca herramientas adicionales si es necesario y continúa este ciclo hasta alcanzar una solución satisfactoria.

## Introducción

Esta lección cubrirá:

- **Entender Agentic RAG:** Aprende sobre este paradigma emergente en IA donde los modelos de lenguaje grandes (LLMs) planifican de forma autónoma sus próximos pasos mientras obtienen información de fuentes de datos externas.
- **Comprender el estilo iterativo Maker-Checker:** Entiende el ciclo de llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas, diseñado para mejorar la precisión y manejar consultas malformadas.
- **Explorar aplicaciones prácticas:** Identifica escenarios donde Agentic RAG sobresale, como entornos donde la precisión es clave, interacciones complejas con bases de datos y flujos de trabajo extensos.

## Objetivos de aprendizaje

Al completar esta lección, sabrás cómo/entenderás:

- **Comprender Agentic RAG:** Aprende sobre este paradigma emergente en IA donde los modelos de lenguaje grandes (LLMs) planifican de forma autónoma sus próximos pasos mientras obtienen información de fuentes de datos externas.
- **Estilo iterativo Maker-Checker:** Comprende el concepto de un ciclo de llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas, diseñado para mejorar la precisión y manejar consultas malformadas.
- **Controlar el proceso de razonamiento:** Entiende la capacidad del sistema para hacerse cargo de su propio proceso de razonamiento, tomando decisiones sobre cómo abordar problemas sin depender de caminos predefinidos.
- **Flujo de trabajo:** Aprende cómo un modelo agente decide de forma independiente recuperar informes de tendencias de mercado, identificar datos de competidores, correlacionar métricas internas de ventas, sintetizar hallazgos y evaluar estrategias.
- **Bucles iterativos, integración de herramientas y memoria:** Descubre cómo el sistema se basa en un patrón de interacción en bucle, manteniendo estado y memoria a lo largo de los pasos para evitar repeticiones y tomar decisiones informadas.
- **Manejo de modos de fallo y autocorrección:** Explora los mecanismos robustos de autocorrección del sistema, incluyendo iteración y reconsulta, uso de herramientas de diagnóstico y recurrir a supervisión humana cuando sea necesario.
- **Límites de la agencia:** Comprende las limitaciones de Agentic RAG, centrándote en la autonomía específica del dominio, la dependencia de infraestructura y el respeto a las directrices.
- **Casos de uso prácticos y valor:** Identifica escenarios donde Agentic RAG brilla, como entornos donde la precisión es esencial, interacciones complejas con bases de datos y flujos de trabajo extensos.
- **Gobernanza, transparencia y confianza:** Aprende sobre la importancia de la gobernanza y la transparencia, incluyendo razonamiento explicable, control de sesgos y supervisión humana.

## ¿Qué es Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) es un paradigma emergente en IA donde los modelos de lenguaje grandes (LLMs) planifican de forma autónoma sus próximos pasos mientras extraen información de fuentes externas. A diferencia de los patrones estáticos de recuperación y lectura, Agentic RAG implica llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas. El sistema evalúa los resultados, refina consultas, invoca herramientas adicionales si es necesario y continúa este ciclo hasta lograr una solución satisfactoria. Este estilo iterativo “maker-checker” mejora la precisión, maneja consultas malformadas y garantiza resultados de alta calidad.

El sistema asume activamente el control de su proceso de razonamiento, reescribiendo consultas fallidas, eligiendo diferentes métodos de recuperación e integrando múltiples herramientas, como búsquedas vectoriales en Azure AI Search, bases de datos SQL o APIs personalizadas, antes de finalizar su respuesta. La cualidad distintiva de un sistema agente es su capacidad para controlar su proceso de razonamiento. Las implementaciones tradicionales de RAG dependen de caminos predefinidos, pero un sistema agente determina de forma autónoma la secuencia de pasos en función de la calidad de la información que encuentra.

## Definiendo Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) es un paradigma emergente en el desarrollo de IA donde los LLMs no solo obtienen información de fuentes de datos externas, sino que también planifican de forma autónoma sus próximos pasos. A diferencia de los patrones estáticos de recuperación y lectura o las secuencias de prompts cuidadosamente diseñadas, Agentic RAG implica un ciclo de llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas. En cada paso, el sistema evalúa los resultados obtenidos, decide si refinar sus consultas, invoca herramientas adicionales si es necesario y continúa este ciclo hasta lograr una solución satisfactoria.

Este estilo iterativo “maker-checker” está diseñado para mejorar la precisión, manejar consultas malformadas a bases de datos estructuradas (por ejemplo, NL2SQL) y garantizar resultados equilibrados y de alta calidad. En lugar de depender únicamente de cadenas de prompts cuidadosamente diseñadas, el sistema asume activamente el control de su proceso de razonamiento. Puede reescribir consultas que fallan, elegir diferentes métodos de recuperación e integrar múltiples herramientas, como búsquedas vectoriales en Azure AI Search, bases de datos SQL o APIs personalizadas, antes de finalizar su respuesta. Esto elimina la necesidad de marcos de orquestación excesivamente complejos. En cambio, un bucle relativamente simple de “llamada al LLM → uso de herramienta → llamada al LLM → …” puede generar salidas sofisticadas y bien fundamentadas.

![Ciclo central de Agentic RAG](../../../translated_images/agentic-rag-core-loop.2224925a913fb3439f518bda61a40096ddf6aa432a11c9b5bba8d0d625e47b79.es.png)

## Controlar el proceso de razonamiento

La cualidad distintiva que hace que un sistema sea “agente” es su capacidad para controlar su propio proceso de razonamiento. Las implementaciones tradicionales de RAG a menudo dependen de que los humanos definan previamente un camino para el modelo: una cadena de razonamiento que describe qué recuperar y cuándo.  
Pero cuando un sistema es verdaderamente agente, decide internamente cómo abordar el problema. No solo ejecuta un guion; determina de forma autónoma la secuencia de pasos en función de la calidad de la información que encuentra.  
Por ejemplo, si se le pide que cree una estrategia de lanzamiento de producto, no se basa únicamente en un prompt que detalle todo el flujo de trabajo de investigación y toma de decisiones. En cambio, el modelo agente decide de forma independiente:

1. Recuperar informes de tendencias actuales del mercado usando Bing Web Grounding.
2. Identificar datos relevantes de competidores usando Azure AI Search.
3. Correlacionar métricas internas de ventas históricas usando Azure SQL Database.
4. Sintetizar los hallazgos en una estrategia cohesiva orquestada mediante Azure OpenAI Service.
5. Evaluar la estrategia en busca de brechas o inconsistencias, iniciando otra ronda de recuperación si es necesario.

Todos estos pasos—refinar consultas, elegir fuentes, iterar hasta estar “satisfecho” con la respuesta—son decididos por el modelo, no predefinidos por un humano.

## Bucles iterativos, integración de herramientas y memoria

![Arquitectura de integración de herramientas](../../../translated_images/tool-integration.7b05a923e3278bf1fd2972faa228fb2ac725f166ed084362b031a24bffd26287.es.png)

Un sistema agente se basa en un patrón de interacción en bucle:

- **Llamada inicial:** El objetivo del usuario (es decir, el prompt del usuario) se presenta al LLM.
- **Invocación de herramientas:** Si el modelo identifica información faltante o instrucciones ambiguas, selecciona una herramienta o método de recuperación—como una consulta a una base de datos vectorial (por ejemplo, Azure AI Search Hybrid Search sobre datos privados) o una llamada estructurada a SQL—para obtener más contexto.
- **Evaluación y refinamiento:** Tras revisar los datos obtenidos, el modelo decide si la información es suficiente. Si no, refina la consulta, prueba una herramienta diferente o ajusta su enfoque.
- **Repetir hasta estar satisfecho:** Este ciclo continúa hasta que el modelo determina que tiene suficiente claridad y evidencia para entregar una respuesta final bien fundamentada.
- **Memoria y estado:** Dado que el sistema mantiene estado y memoria a lo largo de los pasos, puede recordar intentos previos y sus resultados, evitando bucles repetitivos y tomando decisiones más informadas a medida que avanza.

Con el tiempo, esto crea un sentido de comprensión evolutiva, permitiendo al modelo navegar tareas complejas y de múltiples pasos sin requerir que un humano intervenga constantemente o redefina el prompt.

## Manejo de modos de fallo y autocorrección

La autonomía de Agentic RAG también incluye mecanismos robustos de autocorrección. Cuando el sistema se encuentra con obstáculos—como recuperar documentos irrelevantes o enfrentar consultas malformadas—puede:

- **Iterar y reconsultar:** En lugar de devolver respuestas de bajo valor, el modelo intenta nuevas estrategias de búsqueda, reescribe consultas a bases de datos o explora conjuntos de datos alternativos.
- **Usar herramientas de diagnóstico:** El sistema puede invocar funciones adicionales diseñadas para ayudarle a depurar sus pasos de razonamiento o confirmar la corrección de los datos obtenidos. Herramientas como Azure AI Tracing serán importantes para habilitar una observabilidad y monitoreo robustos.
- **Recurrir a supervisión humana:** Para escenarios críticos o que fallan repetidamente, el modelo puede señalar incertidumbre y solicitar orientación humana. Una vez que el humano proporciona retroalimentación correctiva, el modelo puede incorporar esa lección en adelante.

Este enfoque iterativo y dinámico permite al modelo mejorar continuamente, asegurando que no sea solo un sistema de un intento, sino uno que aprende de sus errores durante una sesión determinada.

![Mecanismo de autocorrección](../../../translated_images/self-correction.3d42c31baf4a476bb89313cec58efb196b0e97959c04d7439cc23d27ef1242ac.es.png)

## Límites de la agencia

A pesar de su autonomía dentro de una tarea, Agentic RAG no es análogo a la Inteligencia General Artificial. Sus capacidades “agentes” están confinadas a las herramientas, fuentes de datos y políticas proporcionadas por los desarrolladores humanos. No puede inventar sus propias herramientas ni operar fuera de los límites del dominio establecidos. Más bien, sobresale en la orquestación dinámica de los recursos disponibles.  
Las diferencias clave con formas más avanzadas de IA incluyen:

1. **Autonomía específica del dominio:** Los sistemas Agentic RAG están enfocados en lograr objetivos definidos por el usuario dentro de un dominio conocido, empleando estrategias como la reescritura de consultas o la selección de herramientas para mejorar los resultados.
2. **Dependencia de infraestructura:** Las capacidades del sistema dependen de las herramientas y datos integrados por los desarrolladores. No puede superar estos límites sin intervención humana.
3. **Respeto a las directrices:** Las pautas éticas, reglas de cumplimiento y políticas empresariales siguen siendo muy importantes. La libertad del agente siempre está limitada por medidas de seguridad y mecanismos de supervisión (¿esperemos?).

## Casos de uso prácticos y valor

Agentic RAG sobresale en escenarios que requieren refinamiento iterativo y precisión:

1. **Entornos donde la precisión es clave:** En verificaciones de cumplimiento, análisis regulatorio o investigaciones legales, el modelo agente puede verificar repetidamente hechos, consultar múltiples fuentes y reescribir consultas hasta producir una respuesta completamente revisada.
2. **Interacciones complejas con bases de datos:** Al trabajar con datos estructurados donde las consultas a menudo pueden fallar o necesitar ajustes, el sistema puede refinar autónomamente sus consultas usando Azure SQL o Microsoft Fabric OneLake, asegurando que la recuperación final se alinee con la intención del usuario.
3. **Flujos de trabajo extensos:** Las sesiones más largas pueden evolucionar a medida que surgen nuevas informaciones. Agentic RAG puede incorporar continuamente nuevos datos, ajustando estrategias a medida que aprende más sobre el problema.

## Gobernanza, transparencia y confianza

A medida que estos sistemas se vuelven más autónomos en su razonamiento, la gobernanza y la transparencia son cruciales:

- **Razonamiento explicable:** El modelo puede proporcionar un registro de auditoría de las consultas que realizó, las fuentes que consultó y los pasos de razonamiento que siguió para llegar a su conclusión. Herramientas como Azure AI Content Safety y Azure AI Tracing / GenAIOps pueden ayudar a mantener la transparencia y mitigar riesgos.
- **Control de sesgos y recuperación equilibrada:** Los desarrolladores pueden ajustar estrategias de recuperación para garantizar que se consideren fuentes de datos equilibradas y representativas, y auditar regularmente las salidas para detectar sesgos o patrones desbalanceados usando modelos personalizados para organizaciones avanzadas de ciencia de datos con Azure Machine Learning.
- **Supervisión humana y cumplimiento:** Para tareas sensibles, la revisión humana sigue siendo esencial. Agentic RAG no reemplaza el juicio humano en decisiones críticas, sino que lo complementa entregando opciones más exhaustivamente revisadas.

Tener herramientas que proporcionen un registro claro de acciones es esencial. Sin ellas, depurar un proceso de múltiples pasos puede ser muy difícil. A continuación, un ejemplo de ejecución de un agente de Literal AI (la empresa detrás de Chainlit):

![Ejemplo de ejecución de agente](../../../translated_images/AgentRunExample.27e2df23ad898772d1b3e7a3e3cd4615378e10dfda87ae8f06b4748bf8eea97d.es.png)

![Ejemplo de ejecución de agente 2](../../../translated_images/AgentRunExample2.c0e8c78b1f2540a641515e60035abcc6a9c5e3688bae143eb6c559dd37cdee9f.es.png)

## Conclusión

Agentic RAG representa una evolución natural en cómo los sistemas de IA manejan tareas complejas e intensivas en datos. Al adoptar un patrón de interacción en bucle, seleccionar herramientas de forma autónoma y refinar consultas hasta lograr un resultado de alta calidad, el sistema va más allá de simplemente seguir prompts estáticos, convirtiéndose en un tomador de decisiones más adaptable y consciente del contexto. Aunque sigue estando limitado por infraestructuras definidas por humanos y pautas éticas, estas capacidades agentes permiten interacciones de IA más ricas, dinámicas y, en última instancia, más útiles tanto para empresas como para usuarios finales.

## Recursos adicionales

- Implementar Retrieval Augmented Generation (RAG) con Azure OpenAI Service: Aprende cómo usar tus propios datos con Azure OpenAI Service. [Este módulo de Microsoft Learn proporciona una guía completa sobre cómo implementar RAG](https://learn.microsoft.com/training/modules/use-own-data-azure-openai)
- Evaluación de aplicaciones de IA generativa con Azure AI Foundry: Este artículo cubre la evaluación y comparación de modelos en conjuntos de datos públicos, incluyendo [aplicaciones de IA agente y arquitecturas RAG](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [What is Agentic RAG | Weaviate](https://weaviate.io/blog/what-is-agentic-rag)
- [Agentic RAG: A Complete Guide to Agent-Based Retrieval Augmented Generation – News from generation RAG](https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/)
- [Agentic RAG: turbocharge your RAG with query reformulation and self-query! Hugging Face Open-Source AI Cookbook](https://huggingface.co/learn/cookbook/agent_rag)
- [Adding Agentic Layers to RAG](https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U)
- [The Future of Knowledge Assistants: Jerry Liu](https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s)
- [How to Build Agentic RAG Systems](https://www.youtube.com/watch?v=AOSjiXP1jmQ)
- [Using Azure AI Foundry Agent Service to scale your AI agents](https://ignite.microsoft.com/sessions/BRK102?source=sessions)

### Artículos académicos

- [2303.17651 Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- [2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- [2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.