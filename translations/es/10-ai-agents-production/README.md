# Agentes de IA en Producción

## Introducción

Esta lección cubrirá:

- Cómo planificar de manera efectiva el despliegue de tu Agente de IA en producción.
- Errores comunes y problemas que podrías enfrentar al desplegar tu Agente de IA en producción.
- Cómo gestionar costos mientras mantienes el rendimiento de tu Agente de IA.

## Objetivos de Aprendizaje

Al completar esta lección, sabrás cómo/entenderás:

- Técnicas para mejorar el rendimiento, los costos y la efectividad de un sistema de Agentes de IA en producción.
- Qué evaluar y cómo evaluar tus Agentes de IA.
- Cómo controlar los costos al desplegar Agentes de IA en producción.

Es importante desplegar Agentes de IA confiables. Consulta también la lección "Construyendo Agentes de IA Confiables".

## Evaluando Agentes de IA

Antes, durante y después de desplegar Agentes de IA, es fundamental tener un sistema adecuado para evaluarlos. Esto asegurará que tu sistema esté alineado con tus objetivos y los de tus usuarios.

Para evaluar un Agente de IA, es importante tener la capacidad de evaluar no solo la salida del agente, sino todo el sistema en el que opera tu Agente de IA. Esto incluye, pero no se limita a:

- La solicitud inicial al modelo.
- La capacidad del agente para identificar la intención del usuario.
- La capacidad del agente para identificar la herramienta adecuada para realizar la tarea.
- La respuesta de la herramienta a la solicitud del agente.
- La capacidad del agente para interpretar la respuesta de la herramienta.
- La retroalimentación del usuario a la respuesta del agente.

Esto te permitirá identificar áreas de mejora de manera más modular. Luego, puedes monitorear el efecto de los cambios en modelos, indicaciones, herramientas y otros componentes con mayor eficiencia.

## Problemas Comunes y Soluciones Potenciales con Agentes de IA

| **Problema**                                   | **Solución Potencial**                                                                                                                                                                                                     |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| El Agente de IA no realiza tareas de forma consistente | - Refina el prompt dado al Agente de IA; sé claro con los objetivos.<br>- Identifica si dividir las tareas en subtareas y manejarlas con múltiples agentes puede ser útil.                                                      |
| El Agente de IA entra en bucles continuos      | - Asegúrate de tener términos y condiciones claros de finalización para que el Agente sepa cuándo detener el proceso.<br>- Para tareas complejas que requieren razonamiento y planificación, usa un modelo más grande especializado en tareas de razonamiento. |
| Las llamadas a herramientas del Agente de IA no funcionan bien | - Prueba y valida la salida de la herramienta fuera del sistema del agente.<br>- Refina los parámetros definidos, los prompts y los nombres de las herramientas.                                                                                        |
| El sistema multi-agente no funciona de forma consistente | - Refina los prompts dados a cada agente para asegurarte de que sean específicos y distintos entre sí.<br>- Construye un sistema jerárquico usando un agente "enrutador" o controlador para determinar cuál agente es el correcto.         |

## Gestión de Costos

Aquí tienes algunas estrategias para gestionar los costos de desplegar Agentes de IA en producción:

- **Almacenamiento en Caché de Respuestas** - Identificar solicitudes y tareas comunes y proporcionar las respuestas antes de que pasen por tu sistema agentivo es una buena forma de reducir el volumen de solicitudes similares. Incluso puedes implementar un flujo para identificar qué tan similar es una solicitud a tus solicitudes en caché utilizando modelos de IA más básicos.

- **Uso de Modelos Más Pequeños** - Los Modelos de Lenguaje Pequeños (SLMs) pueden funcionar bien en ciertos casos de uso agentivos y reducirán significativamente los costos. Como se mencionó antes, construir un sistema de evaluación para determinar y comparar el rendimiento frente a modelos más grandes es la mejor manera de entender qué tan bien funcionará un SLM en tu caso de uso.

- **Uso de un Modelo Enrutador** - Una estrategia similar es usar una diversidad de modelos y tamaños. Puedes usar un LLM/SLM o una función sin servidor para enrutar solicitudes según su complejidad a los modelos más adecuados. Esto también ayudará a reducir costos mientras se garantiza el rendimiento en las tareas adecuadas.

## Felicitaciones  

Esta es actualmente la última lección de "Agentes de IA para Principiantes".

Planeamos seguir agregando lecciones basadas en comentarios y cambios en esta industria en constante crecimiento, así que vuelve a visitarnos en un futuro cercano.

Si deseas continuar aprendiendo y construyendo con Agentes de IA, únete al [Azure AI Community Discord](https://discord.gg/kzRShWzttr).

Allí organizamos talleres, mesas redondas comunitarias y sesiones de "pregúntame cualquier cosa".

También contamos con una colección de materiales de aprendizaje adicionales que pueden ayudarte a comenzar a construir Agentes de IA en producción.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.