# Introducción a los Agentes de IA y Casos de Uso

¡Bienvenido al curso "Agentes de IA para Principiantes"! Este curso te proporciona conocimientos fundamentales y ejemplos prácticos para construir con Agentes de IA.

Únete a la [Comunidad de Azure AI en Discord](https://discord.gg/kzRShWzttr) para conocer a otros estudiantes, constructores de Agentes de IA y resolver cualquier duda que tengas sobre este curso.

Para comenzar este curso, empezaremos por comprender mejor qué son los Agentes de IA y cómo podemos utilizarlos en las aplicaciones y flujos de trabajo que construimos.

## Introducción

Esta lección cubre:

- ¿Qué son los Agentes de IA y cuáles son los diferentes tipos de agentes?
- ¿Qué casos de uso son ideales para los Agentes de IA y cómo pueden ayudarnos?
- ¿Cuáles son algunos de los bloques básicos al diseñar Soluciones Agénticas?

## Objetivos de Aprendizaje

Al finalizar esta lección, deberías ser capaz de:

- Comprender los conceptos de Agentes de IA y cómo se diferencian de otras soluciones de IA.
- Aplicar los Agentes de IA de manera eficiente.
- Diseñar soluciones agénticas de manera productiva para usuarios y clientes.

## Definiendo Agentes de IA y Tipos de Agentes de IA

### ¿Qué son los Agentes de IA?

Los Agentes de IA son **sistemas** que permiten que los **Modelos de Lenguaje Extenso (LLMs)** **realicen acciones** extendiendo sus capacidades al proporcionarles **acceso a herramientas** y **conocimientos**.

Desglosemos esta definición en partes más pequeñas:

- **Sistema** - Es importante pensar en los agentes no solo como un componente único, sino como un sistema compuesto por muchos componentes. A nivel básico, los componentes de un Agente de IA son:
  - **Entorno** - El espacio definido donde opera el Agente de IA. Por ejemplo, si tuviéramos un Agente de Reservas de Viajes, el entorno podría ser el sistema de reservas que el Agente de IA utiliza para completar tareas.
  - **Sensores** - Los entornos contienen información y proporcionan retroalimentación. Los Agentes de IA utilizan sensores para recopilar e interpretar esta información sobre el estado actual del entorno. En el ejemplo del Agente de Reservas de Viajes, el sistema de reservas puede proporcionar información como la disponibilidad de hoteles o precios de vuelos.
  - **Actuadores** - Una vez que el Agente de IA recibe el estado actual del entorno, determina qué acción realizar para cambiar el entorno según la tarea actual. En el caso del Agente de Reservas de Viajes, podría ser reservar una habitación disponible para el usuario.

![¿Qué son los Agentes de IA?](../../../translated_images/what-are-ai-agents.png?WT.7f2607783e984be0cfb6dd064ad20389d37cf6d1d28bc5d5a3c648ef353bde89.es.mc_id=academic-105485-koreyst)

**Modelos de Lenguaje Extenso** - El concepto de agentes existía antes de la creación de los LLMs. La ventaja de construir Agentes de IA con LLMs es su capacidad para interpretar el lenguaje humano y los datos. Esta capacidad permite a los LLMs interpretar información del entorno y definir un plan para cambiarlo.

**Realizar Acciones** - Fuera de los sistemas de Agentes de IA, los LLMs están limitados a situaciones donde la acción es generar contenido o información basada en un aviso del usuario. Dentro de los sistemas de Agentes de IA, los LLMs pueden completar tareas interpretando la solicitud del usuario y utilizando herramientas disponibles en su entorno.

**Acceso a Herramientas** - Las herramientas a las que el LLM tiene acceso están definidas por 1) el entorno en el que opera y 2) el desarrollador del Agente de IA. En nuestro ejemplo del Agente de Viajes, las herramientas del agente están limitadas por las operaciones disponibles en el sistema de reservas, y/o el desarrollador puede restringir el acceso del agente a herramientas relacionadas con vuelos.

**Conocimiento** - Además de la información proporcionada por el entorno, los Agentes de IA también pueden recuperar conocimientos de otros sistemas, servicios, herramientas e incluso otros agentes. En el ejemplo del Agente de Viajes, este conocimiento podría incluir las preferencias de viaje del usuario almacenadas en una base de datos de clientes.

### Los diferentes tipos de agentes

Ahora que tenemos una definición general de los Agentes de IA, veamos algunos tipos específicos de agentes y cómo se aplicarían a un Agente de Reservas de Viajes.

| **Tipo de Agente**            | **Descripción**                                                                                                                       | **Ejemplo**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agentes de Reflejo Simple** | Realizan acciones inmediatas basadas en reglas predefinidas.                                                                           | El agente de viajes interpreta el contexto de un correo electrónico y reenvía quejas de viajes al servicio al cliente.                                                                                                       |
| **Agentes de Reflejo Basados en Modelos** | Realizan acciones basadas en un modelo del mundo y los cambios en ese modelo.                                                        | El agente de viajes prioriza rutas con cambios significativos en precios basándose en datos históricos de precios.                                                                                                           |
| **Agentes Basados en Metas**  | Crean planes para alcanzar metas específicas interpretando la meta y determinando las acciones necesarias para lograrla.              | El agente de viajes organiza un viaje determinando los arreglos necesarios (auto, transporte público, vuelos) desde la ubicación actual hasta el destino.                                                                    |
| **Agentes Basados en Utilidad** | Consideran preferencias y evalúan compensaciones numéricamente para determinar cómo alcanzar metas.                                    | El agente de viajes maximiza la utilidad al sopesar conveniencia frente a costo al reservar viajes.                                                                                                                           |
| **Agentes de Aprendizaje**    | Mejoran con el tiempo respondiendo a retroalimentación y ajustando acciones en consecuencia.                                           | El agente de viajes mejora utilizando retroalimentación de encuestas posteriores al viaje para ajustar futuras reservas.                                                                                                      |
| **Agentes Jerárquicos**       | Incluyen múltiples agentes en un sistema escalonado, donde los agentes de nivel superior dividen tareas en subtareas para que los agentes de nivel inferior las completen. | El agente de viajes cancela un viaje dividiendo la tarea en subtareas (por ejemplo, cancelar reservas específicas) y asignando a agentes de nivel inferior completarlas, informando al agente de nivel superior.               |
| **Sistemas Multi-Agente (MAS)** | Los agentes completan tareas de manera independiente, ya sea cooperativa o competitivamente.                                           | Cooperativo: Múltiples agentes reservan servicios específicos de viaje como hoteles, vuelos y entretenimiento. Competitivo: Múltiples agentes gestionan y compiten por un calendario compartido de reservas de hotel.         |

## Cuándo Usar Agentes de IA

En la sección anterior, utilizamos el caso de uso del Agente de Viajes para explicar cómo los diferentes tipos de agentes pueden ser utilizados en distintos escenarios de reserva de viajes. Continuaremos utilizando esta aplicación a lo largo del curso.

Veamos los tipos de casos de uso para los que los Agentes de IA son más adecuados:

![¿Cuándo usar Agentes de IA?](../../../translated_images/when-to-use-ai-agents.png?WT.1681e3f19611f820ee4331ab494b50ebc6f09b2fb4df3a5f4dac5458316263ad.es.mc_id=academic-105485-koreyst)

- **Problemas Abiertos** - Permitir que el LLM determine los pasos necesarios para completar una tarea, ya que no siempre se pueden codificar directamente en un flujo de trabajo.
- **Procesos de Múltiples Pasos** - Tareas que requieren un nivel de complejidad en el que el Agente de IA necesita utilizar herramientas o información a lo largo de múltiples interacciones en lugar de una sola consulta.
- **Mejora con el Tiempo** - Tareas donde el agente puede mejorar con el tiempo al recibir retroalimentación de su entorno o de los usuarios para proporcionar una mejor utilidad.

Cubrimos más consideraciones sobre el uso de Agentes de IA en la lección de Construcción de Agentes de IA Confiables.

## Fundamentos de las Soluciones Agénticas

### Desarrollo de Agentes

El primer paso para diseñar un sistema de Agente de IA es definir las herramientas, acciones y comportamientos. En este curso, nos enfocamos en usar el **Azure AI Agent Service** para definir nuestros agentes. Ofrece características como:

- Selección de Modelos Abiertos como OpenAI, Mistral y Llama
- Uso de Datos con Licencia a través de proveedores como Tripadvisor
- Uso de herramientas estandarizadas OpenAPI 3.0

### Patrones Agénticos

La comunicación con los LLMs se realiza mediante prompts. Dada la naturaleza semiautónoma de los Agentes de IA, no siempre es posible o necesario volver a rediseñar manualmente el prompt después de un cambio en el entorno. Usamos **Patrones Agénticos** que nos permiten realizar prompts al LLM a lo largo de múltiples pasos de una manera más escalable.

Este curso está dividido en algunos de los patrones agénticos más populares en la actualidad.

### Frameworks Agénticos

Los Frameworks Agénticos permiten a los desarrolladores implementar patrones agénticos a través de código. Estos frameworks ofrecen plantillas, plugins y herramientas para una mejor colaboración de los Agentes de IA. Estos beneficios proporcionan capacidades para una mejor observabilidad y solución de problemas en sistemas de Agentes de IA.

En este curso, exploraremos el framework de investigación AutoGen y el framework listo para producción Agent de Semantic Kernel.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.