```markdown
# Agentic RAG

Esta lección ofrece una visión completa de Agentic Retrieval-Augmented Generation (Agentic RAG), un paradigma emergente de inteligencia artificial donde los modelos de lenguaje grande (LLMs) planifican autónomamente sus próximos pasos mientras obtienen información de fuentes externas. A diferencia de los patrones estáticos de "recuperar y luego leer", Agentic RAG implica llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas. El sistema evalúa los resultados, refina las consultas, invoca herramientas adicionales si es necesario y continúa este ciclo hasta lograr una solución satisfactoria.

## Introducción

Esta lección cubrirá:

- **Comprender Agentic RAG:** Aprende sobre este paradigma emergente en IA donde los modelos de lenguaje grande (LLMs) planifican autónomamente sus próximos pasos mientras obtienen información de fuentes de datos externas.
- **Entender el Estilo Iterativo Maker-Checker:** Comprende el ciclo de llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas, diseñadas para mejorar la precisión y manejar consultas mal formadas.
- **Explorar Aplicaciones Prácticas:** Identifica escenarios donde Agentic RAG sobresale, como entornos donde la precisión es primordial, interacciones complejas con bases de datos y flujos de trabajo extendidos.

## Objetivos de Aprendizaje

Al completar esta lección, sabrás cómo/entenderás:

- **Comprender Agentic RAG:** Aprende sobre este paradigma emergente en IA donde los modelos de lenguaje grande (LLMs) planifican autónomamente sus próximos pasos mientras obtienen información de fuentes de datos externas.
- **Estilo Iterativo Maker-Checker:** Entiende el concepto de un ciclo de llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas, diseñadas para mejorar la precisión y manejar consultas mal formadas.
- **Asumir el Proceso de Razonamiento:** Comprende la capacidad del sistema para asumir su propio proceso de razonamiento, tomando decisiones sobre cómo abordar problemas sin depender de caminos predefinidos.
- **Flujo de Trabajo:** Entiende cómo un modelo agentic decide de forma independiente recuperar informes de tendencias de mercado, identificar datos de competidores, correlacionar métricas internas de ventas, sintetizar hallazgos y evaluar la estrategia.
- **Bucles Iterativos, Integración de Herramientas y Memoria:** Aprende sobre la dependencia del sistema en un patrón de interacción en bucle, manteniendo el estado y la memoria a través de los pasos para evitar bucles repetitivos y tomar decisiones informadas.
- **Manejo de Modos de Falla y Auto-Corrección:** Explora los robustos mecanismos de auto-corrección del sistema, incluyendo iteración y reconsulta, uso de herramientas de diagnóstico y recurrir a supervisión humana si es necesario.
- **Límites de la Autonomía:** Comprende las limitaciones de Agentic RAG, enfocándose en la autonomía específica de dominio, la dependencia de la infraestructura y el respeto por las directrices de seguridad.
- **Casos de Uso Prácticos y Valor:** Identifica escenarios donde Agentic RAG sobresale, como entornos donde la precisión es primordial, interacciones complejas con bases de datos y flujos de trabajo extendidos.
- **Gobernanza, Transparencia y Confianza:** Aprende sobre la importancia de la gobernanza y la transparencia, incluyendo razonamiento explicable, control de sesgos y supervisión humana.

## ¿Qué es Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) es un paradigma emergente de inteligencia artificial donde los modelos de lenguaje grande (LLMs) planifican autónomamente sus próximos pasos mientras obtienen información de fuentes externas. A diferencia de los patrones estáticos de "recuperar y luego leer", Agentic RAG implica llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas. El sistema evalúa los resultados, refina las consultas, invoca herramientas adicionales si es necesario y continúa este ciclo hasta lograr una solución satisfactoria. Este estilo iterativo "maker-checker" mejora la precisión, maneja consultas mal formadas y asegura resultados de alta calidad.

El sistema asume activamente su proceso de razonamiento, reescribiendo consultas fallidas, eligiendo diferentes métodos de recuperación e integrando múltiples herramientas, como búsqueda vectorial en Azure AI Search, bases de datos SQL o APIs personalizadas, antes de finalizar su respuesta. La cualidad distintiva de un sistema agentic es su capacidad para asumir su proceso de razonamiento. Las implementaciones tradicionales de RAG dependen de caminos predefinidos, pero un sistema agentic determina autónomamente la secuencia de pasos en función de la calidad de la información que encuentra.

## Definiendo Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) es un paradigma emergente en el desarrollo de IA donde los LLMs no solo obtienen información de fuentes de datos externas, sino que también planifican autónomamente sus próximos pasos. A diferencia de los patrones estáticos de "recuperar y luego leer" o las secuencias de prompts cuidadosamente diseñadas, Agentic RAG implica un ciclo de llamadas iterativas al LLM, intercaladas con llamadas a herramientas o funciones y salidas estructuradas. En cada paso, el sistema evalúa los resultados obtenidos, decide si refinar sus consultas, invoca herramientas adicionales si es necesario y continúa este ciclo hasta lograr una solución satisfactoria.

Este estilo iterativo "maker-checker" está diseñado para mejorar la precisión, manejar consultas mal formadas hacia bases de datos estructuradas (por ejemplo, NL2SQL) y asegurar resultados equilibrados y de alta calidad. En lugar de depender únicamente de cadenas de prompts cuidadosamente diseñadas, el sistema asume activamente su proceso de razonamiento. Puede reescribir consultas que fallan, elegir diferentes métodos de recuperación e integrar múltiples herramientas, como búsqueda vectorial en Azure AI Search, bases de datos SQL o APIs personalizadas, antes de finalizar su respuesta. Esto elimina la necesidad de marcos de orquestación demasiado complejos. En su lugar, un bucle relativamente simple de "llamada LLM → uso de herramienta → llamada LLM → …" puede generar salidas sofisticadas y bien fundamentadas.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.2224925a913fb3439f518bda61a40096ddf6aa432a11c9b5bba8d0d625e47b79.es.png)

## Asumir el Proceso de Razonamiento

La cualidad distintiva que hace que un sistema sea “agentic” es su capacidad para asumir su propio proceso de razonamiento. Las implementaciones tradicionales de RAG a menudo dependen de que los humanos predefinan un camino para el modelo: una cadena de pensamiento que detalla qué recuperar y cuándo. Pero cuando un sistema es verdaderamente agentic, decide internamente cómo abordar el problema. No solo ejecuta un guion; determina autónomamente la secuencia de pasos en función de la calidad de la información que encuentra.

Por ejemplo, si se le pide que cree una estrategia de lanzamiento de producto, no depende únicamente de un prompt que detalle todo el flujo de trabajo de investigación y toma de decisiones. En su lugar, el modelo agentic decide de manera independiente:

1. Recuperar informes de tendencias de mercado actuales usando Bing Web Grounding.
2. Identificar datos relevantes de competidores usando Azure AI Search.
3. Correlacionar métricas históricas internas de ventas usando Azure SQL Database.
4. Sintetizar los hallazgos en una estrategia cohesiva orquestada a través de Azure OpenAI Service.
5. Evaluar la estrategia en busca de brechas o inconsistencias, lo que podría llevar a otra ronda de recuperación si es necesario.

Todos estos pasos—refinar consultas, elegir fuentes, iterar hasta estar “satisfecho” con la respuesta—son decididos por el modelo, no predefinidos por un humano.

## Bucles Iterativos, Integración de Herramientas y Memoria

![Tool Integration Architecture](../../../translated_images/tool-integration.7b05a923e3278bf1fd2972faa228fb2ac725f166ed084362b031a24bffd26287.es.png)

Un sistema agentic se basa en un patrón de interacción en bucle:

- **Llamada Inicial:** El objetivo del usuario (es decir, el prompt del usuario) se presenta al LLM.
- **Invocación de Herramientas:** Si el modelo identifica información faltante o instrucciones ambiguas, selecciona una herramienta o método de recuperación, como una consulta a una base de datos vectorial (por ejemplo, Azure AI Search Hybrid search sobre datos privados) o una llamada SQL estructurada, para obtener más contexto.
- **Evaluación y Refinamiento:** Después de revisar los datos devueltos, el modelo decide si la información es suficiente. Si no, refina la consulta, prueba con una herramienta diferente o ajusta su enfoque.
- **Repetir Hasta Estar Satisfecho:** Este ciclo continúa hasta que el modelo determina que tiene suficiente claridad y evidencia para entregar una respuesta final bien razonada.
- **Memoria y Estado:** Debido a que el sistema mantiene estado y memoria a través de los pasos, puede recordar intentos previos y sus resultados, evitando bucles repetitivos y tomando decisiones más informadas a medida que avanza.

Con el tiempo, esto crea un sentido de comprensión en evolución, permitiendo que el modelo navegue tareas complejas y de múltiples pasos sin requerir que un humano intervenga constantemente o rediseñe el prompt.

## Manejo de Modos de Falla y Auto-Corrección

La autonomía de Agentic RAG también incluye mecanismos robustos de auto-corrección. Cuando el sistema se encuentra con callejones sin salida, como recuperar documentos irrelevantes o enfrentar consultas mal formadas, puede:

- **Iterar y Reconsultar:** En lugar de devolver respuestas de bajo valor, el modelo intenta nuevas estrategias de búsqueda, reescribe consultas a bases de datos o explora conjuntos de datos alternativos.
- **Usar Herramientas de Diagnóstico:** El sistema puede invocar funciones adicionales diseñadas para ayudarle a depurar sus pasos de razonamiento o confirmar la corrección de los datos recuperados. Herramientas como Azure AI Tracing serán importantes para habilitar una observabilidad y monitoreo robustos.
- **Recurrir a Supervisión Humana:** Para escenarios de alto riesgo o fallos repetidos, el modelo podría señalar incertidumbre y solicitar orientación humana. Una vez que el humano proporciona retroalimentación correctiva, el modelo puede incorporar esa lección en adelante.

Este enfoque iterativo y dinámico permite que el modelo mejore continuamente, asegurando que no sea solo un sistema de una sola ejecución, sino uno que aprende de sus errores dentro de una sesión dada.

![Self Correction Mechanism](../../../translated_images/self-correction.3d42c31baf4a476bb89313cec58efb196b0e97959c04d7439cc23d27ef1242ac.es.png)

## Límites de la Autonomía

A pesar de su autonomía dentro de una tarea, Agentic RAG no es análogo a la Inteligencia Artificial General. Sus capacidades "agentic" están confinadas a las herramientas, fuentes de datos y políticas proporcionadas por los desarrolladores humanos. No puede inventar sus propias herramientas ni salirse de los límites del dominio que se le han establecido. Más bien, sobresale al orquestar dinámicamente los recursos disponibles.

Diferencias clave con formas más avanzadas de IA incluyen:

1. **Autonomía Específica de Dominio:** Los sistemas Agentic RAG se enfocan en lograr objetivos definidos por el usuario dentro de un dominio conocido, empleando estrategias como reescritura de consultas o selección de herramientas para mejorar los resultados.
2. **Dependencia de Infraestructura:** Las capacidades del sistema dependen de las herramientas y datos integrados por los desarrolladores. No puede superar estos límites sin intervención humana.
3. **Respeto por las Directrices:** Las pautas éticas, reglas de cumplimiento y políticas empresariales siguen siendo muy importantes. La libertad del agente siempre está restringida por medidas de seguridad y mecanismos de supervisión (¿esperemos?).

## Casos de Uso Prácticos y Valor

Agentic RAG sobresale en escenarios que requieren refinamiento iterativo y precisión:

1. **Entornos donde la Precisión es Primordial:** En verificaciones de cumplimiento, análisis regulatorios o investigación legal, el modelo agentic puede verificar repetidamente los hechos, consultar múltiples fuentes y reescribir consultas hasta producir una respuesta minuciosamente verificada.

2. **Interacciones Complejas con Bases de Datos:** Al trabajar con datos estructurados donde las consultas pueden fallar o necesitar ajustes frecuentes, el sistema puede refinar autónomamente sus consultas usando Azure SQL o Microsoft Fabric OneLake, asegurando que la recuperación final se alinee con la intención del usuario.

3. **Flujos de Trabajo Extendidos:** Las sesiones de mayor duración pueden evolucionar a medida que surgen nuevas informaciones. Agentic RAG puede incorporar continuamente nuevos datos, ajustando estrategias a medida que aprende más sobre el problema en cuestión.

## Gobernanza, Transparencia y Confianza

A medida que estos sistemas se vuelven más autónomos en su razonamiento, la gobernanza y la transparencia son cruciales:

- **Razonamiento Explicable:** El modelo puede proporcionar un registro de auditoría de las consultas que realizó, las fuentes que consultó y los pasos de razonamiento que tomó para llegar a su conclusión. Herramientas como Azure AI Content Safety y Azure AI Tracing / GenAIOps pueden ayudar a mantener la transparencia y mitigar riesgos.
- **Control de Sesgos y Recuperación Equilibrada:** Los desarrolladores pueden ajustar estrategias de recuperación para asegurar que se consideren fuentes de datos equilibradas y representativas, y auditar regularmente las salidas para detectar sesgos o patrones desequilibrados utilizando modelos personalizados para organizaciones avanzadas de ciencia de datos con Azure Machine Learning.
- **Supervisión Humana y Cumplimiento:** Para tareas sensibles, la revisión humana sigue siendo esencial. Agentic RAG no reemplaza el juicio humano en decisiones críticas; lo complementa al entregar opciones más minuciosamente evaluadas.

Tener herramientas que proporcionen un registro claro de las acciones es esencial. Sin ellas, depurar un proceso de múltiples pasos puede ser muy difícil. A continuación, un ejemplo de una ejecución de agente de Literal AI (empresa detrás de Chainlit):

![AgentRunExample](../../../translated_images/AgentRunExample.27e2df23ad898772d1b3e7a3e3cd4615378e10dfda87ae8f06b4748bf8eea97d.es.png)

![AgentRunExample2](../../../translated_images/AgentRunExample2.c0e8c78b1f2540a641515e60035abcc6a9c5e3688bae143eb6c559dd37cdee9f.es.png)

## Conclusión

Agentic RAG representa una evolución natural en cómo los sistemas de IA manejan tareas complejas y que requieren gran cantidad de datos. Al adoptar un patrón de interacción en bucle, seleccionar herramientas autónomamente y refinar consultas hasta lograr un resultado de alta calidad, el sistema va más allá de simplemente seguir prompts estáticos para convertirse en un tomador de decisiones más adaptativo y consciente del contexto. Aunque todavía está limitado por infraestructuras y directrices éticas definidas por humanos, estas capacidades agentic permiten interacciones de IA más ricas, dinámicas y, en última instancia, más útiles tanto para empresas como para usuarios finales.

## Recursos Adicionales

- Implementar Retrieval Augmented Generation (RAG) con Azure OpenAI Service: Aprende cómo usar tus propios datos con Azure OpenAI Service. [Este módulo de Microsoft Learn ofrece una guía completa sobre cómo implementar RAG](https://learn.microsoft.com/training/modules/use-own-data-azure-openai)
- Evaluación de aplicaciones de IA generativa con Azure AI Foundry: Este artículo cubre la evaluación y comparación de modelos en conjuntos de datos públicos, incluyendo [aplicaciones Agentic AI y arquitecturas RAG](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [What is Agentic RAG | Weaviate](https://weaviate.io/blog/what-is-agentic-rag)
- [Agentic RAG: A Complete Guide to Agent-Based Retrieval Augmented Generation – News from generation RAG](https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/)
- [Agentic RAG: turbocharge your RAG with query reformulation and self-query! Hugging Face Open-Source AI Cookbook](https://huggingface.co/learn/cookbook/agent_rag)
- [Adding Agentic Layers to RAG](https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U)
- [The Future of Knowledge Assistants: Jerry Liu](https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s)
- [How to Build Agentic RAG Systems](https://www.youtube.com/watch?v=AOSjiXP1jmQ)
- [Using Azure AI Foundry Agent Service to scale your AI agents](https://ignite.microsoft.com/en-US/sessions/BRK102?source=sessions)

### Artículos Académicos

- [2303.17651 Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- [2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- [2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)
```

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.