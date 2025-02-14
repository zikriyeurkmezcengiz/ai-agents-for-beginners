# Introducción a los Agentes de IA y Casos de Uso de Agentes

¡Bienvenido al curso "Agentes de IA para Principiantes"! Este curso te proporciona conocimientos fundamentales y ejemplos prácticos para construir con Agentes de IA.

Únete a la [Comunidad de Discord de Azure AI](https://discord.gg/kzRShWzttr) para conocer a otros estudiantes, constructores de Agentes de IA y hacer cualquier pregunta que tengas sobre este curso.

Para comenzar este curso, primero entenderemos mejor qué son los Agentes de IA y cómo podemos utilizarlos en las aplicaciones y flujos de trabajo que construimos.

## Introducción

Esta lección cubre:

- ¿Qué son los Agentes de IA y cuáles son los diferentes tipos de agentes?
- ¿Cuáles son los casos de uso ideales para los Agentes de IA y cómo pueden ayudarnos?
- ¿Cuáles son algunos de los bloques de construcción básicos al diseñar Soluciones Agénticas?

## Objetivos de Aprendizaje
Al completar esta lección, deberías ser capaz de:

- Comprender los conceptos de los Agentes de IA y cómo se diferencian de otras soluciones de IA.
- Aplicar los Agentes de IA de manera más eficiente.
- Diseñar soluciones agénticas de manera productiva tanto para usuarios como para clientes.

## Definiendo Agentes de IA y Tipos de Agentes de IA

### ¿Qué son los Agentes de IA?

Los Agentes de IA son **sistemas** que permiten que los **Modelos de Lenguaje Extensos (LLMs)** **realicen acciones** al ampliar sus capacidades mediante el acceso a **herramientas** y **conocimiento**.

Desglosaremos esta definición en partes más pequeñas:

- **Sistema** - Es importante pensar en los agentes no solo como un componente único, sino como un sistema compuesto por múltiples componentes. A nivel básico, los componentes de un Agente de IA son:
  - **Entorno** - El espacio definido donde opera el Agente de IA. Por ejemplo, si tuviéramos un Agente de IA para reservas de viajes, el entorno podría ser el sistema de reservas que el agente utiliza para completar tareas.
  - **Sensores** - Los entornos tienen información y proporcionan retroalimentación. Los Agentes de IA usan sensores para recopilar e interpretar esta información sobre el estado actual del entorno. En el ejemplo del Agente de Reservas de Viajes, el sistema de reservas podría proporcionar información como la disponibilidad de hoteles o precios de vuelos.
  - **Actuadores** - Una vez que el Agente de IA recibe el estado actual del entorno, para la tarea en curso, el agente determina qué acción realizar para cambiar el entorno. Para el agente de reservas, podría ser reservar una habitación disponible para el usuario.

![¿Qué son los Agentes de IA?](../../../translated_images/what-are-ai-agents.125520f55950b252a429b04a9f41e0152d4dafa1f1bd9081f4f574631acb759e.es.png?WT.mc_id=academic-105485-koreyst)

**Modelos de Lenguaje Extensos** - El concepto de agentes existía antes de la creación de los LLMs. La ventaja de construir Agentes de IA con LLMs es su capacidad para interpretar el lenguaje humano y los datos. Esta capacidad permite a los LLMs interpretar la información del entorno y definir un plan para cambiarlo.

**Realizar Acciones** - Fuera de los sistemas de Agentes de IA, los LLMs están limitados a situaciones donde la acción es generar contenido o información basada en el mensaje del usuario. Dentro de los sistemas de Agentes de IA, los LLMs pueden realizar tareas interpretando la solicitud del usuario y utilizando las herramientas disponibles en su entorno.

**Acceso a Herramientas** - Las herramientas a las que el LLM tiene acceso están definidas por 1) el entorno en el que opera y 2) el desarrollador del Agente de IA. En nuestro ejemplo del agente de viajes, las herramientas del agente están limitadas por las operaciones disponibles en el sistema de reservas, y/o el desarrollador puede limitar el acceso del agente a herramientas específicas como vuelos.

**Conocimiento** - Más allá de la información proporcionada por el entorno, los Agentes de IA también pueden recuperar conocimiento de otros sistemas, servicios, herramientas e incluso otros agentes. En el ejemplo del agente de viajes, este conocimiento podría incluir información sobre las preferencias de viaje del usuario almacenada en una base de datos de clientes.

### Los diferentes tipos de agentes

Ahora que tenemos una definición general de los Agentes de IA, veamos algunos tipos específicos de agentes y cómo se aplicarían a un agente de reservas de viajes.

| **Tipo de Agente**             | **Descripción**                                                                                                                      | **Ejemplo**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agentes de Reflexión Simple** | Realizan acciones inmediatas basadas en reglas predefinidas.                                                                          | El agente de viajes interpreta el contexto de un correo electrónico y reenvía quejas de viaje al servicio al cliente.                                                                                                         |
| **Agentes Basados en Modelos**  | Realizan acciones basadas en un modelo del mundo y los cambios en ese modelo.                                                         | El agente de viajes prioriza rutas con cambios significativos en precios basándose en el acceso a datos históricos de precios.                                                                                                 |
| **Agentes Basados en Objetivos** | Crean planes para alcanzar objetivos específicos interpretando el objetivo y determinando las acciones necesarias para lograrlo.       | El agente de viajes reserva un trayecto determinando los arreglos de viaje necesarios (coche, transporte público, vuelos) desde la ubicación actual hasta el destino.                                                          |
| **Agentes Basados en Utilidad** | Consideran preferencias y evalúan compensaciones numéricamente para determinar cómo alcanzar objetivos.                               | El agente de viajes maximiza la utilidad sopesando comodidad frente a costo al reservar viajes.                                                                                                                               |
| **Agentes de Aprendizaje**      | Mejoran con el tiempo al responder a retroalimentación y ajustar sus acciones en consecuencia.                                        | El agente de viajes mejora utilizando retroalimentación de encuestas post-viaje para hacer ajustes en futuras reservas.                                                                                                        |
| **Agentes Jerárquicos**         | Incluyen múltiples agentes en un sistema escalonado, donde agentes de nivel superior dividen tareas en subtareas para que los agentes de nivel inferior las completen. | El agente de viajes cancela un viaje dividiendo la tarea en subtareas (por ejemplo, cancelar reservas específicas) y permitiendo que agentes de nivel inferior las completen, informando de vuelta al agente de nivel superior. |
| **Sistemas Multi-Agentes (MAS)** | Los agentes completan tareas de forma independiente, ya sea cooperativa o competitivamente.                                          | Cooperativo: Múltiples agentes reservan servicios específicos de viaje como hoteles, vuelos y entretenimiento. Competitivo: Múltiples agentes gestionan y compiten por un calendario compartido de reservas hoteleras para alojar clientes.                         |

## Cuándo Usar Agentes de IA

En la sección anterior, utilizamos el caso de uso del Agente de Viajes para explicar cómo los diferentes tipos de agentes pueden ser utilizados en diversos escenarios de reservas de viaje. Continuaremos usando esta aplicación a lo largo del curso.

Veamos los tipos de casos de uso para los que los Agentes de IA son más adecuados:

![¿Cuándo usar Agentes de IA?](../../../translated_images/when-to-use-ai-agents.912b9a02e9e0e2af45a3e24faa4e912e334ec23f21f0cf5cb040b7e899b09cd0.es.png?WT.mc_id=academic-105485-koreyst)

- **Problemas Abiertos** - Permitir que el LLM determine los pasos necesarios para completar una tarea porque no siempre se puede codificar de manera rígida en un flujo de trabajo.
- **Procesos de Múltiples Pasos** - Tareas que requieren un nivel de complejidad en el que el Agente de IA necesita usar herramientas o información en múltiples interacciones en lugar de una sola recuperación.
- **Mejora con el Tiempo** - Tareas en las que el agente puede mejorar con el tiempo al recibir retroalimentación de su entorno o de los usuarios para proporcionar una mejor utilidad.

Cubrimos más consideraciones sobre el uso de Agentes de IA en la lección Construyendo Agentes de IA Confiables.

## Fundamentos de las Soluciones Agénticas

### Desarrollo de Agentes

El primer paso para diseñar un sistema de Agente de IA es definir las herramientas, acciones y comportamientos. En este curso, nos enfocamos en usar el **Servicio de Agentes de Azure AI** para definir nuestros agentes. Este ofrece características como:

- Selección de Modelos Abiertos como OpenAI, Mistral y Llama
- Uso de Datos Licenciados a través de proveedores como Tripadvisor
- Uso de herramientas estandarizadas de OpenAPI 3.0

### Patrones Agénticos

La comunicación con los LLMs se realiza a través de prompts. Dada la naturaleza semi-autónoma de los Agentes de IA, no siempre es posible o necesario volver a hacer un prompt manualmente después de un cambio en el entorno. Usamos **Patrones Agénticos** que nos permiten hacer prompts al LLM en múltiples pasos de una manera más escalable.

Este curso está dividido en algunos de los patrones agénticos populares actuales.

### Frameworks Agénticos

Los Frameworks Agénticos permiten a los desarrolladores implementar patrones agénticos mediante código. Estos frameworks ofrecen plantillas, plugins y herramientas para mejorar la colaboración entre Agentes de IA. Estos beneficios proporcionan capacidades para una mejor observabilidad y solución de problemas en sistemas de Agentes de IA.

En este curso, exploraremos el framework AutoGen basado en investigación y el framework listo para producción Agent de Semantic Kernel.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automatizada basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.