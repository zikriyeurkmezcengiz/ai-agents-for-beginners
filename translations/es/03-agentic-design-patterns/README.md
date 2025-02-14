# Principios de Diseño Agéntico para IA

## Introducción

Existen muchas formas de abordar la construcción de Sistemas de IA Agénticos. Dado que la ambigüedad es una característica y no un defecto en el diseño de IA Generativa, a veces es difícil para los ingenieros saber por dónde empezar. Hemos creado un conjunto de Principios de Diseño centrados en el usuario para ayudar a los desarrolladores a construir sistemas agénticos enfocados en los clientes y resolver sus necesidades empresariales. Estos principios de diseño no son una arquitectura prescriptiva, sino más bien un punto de partida para los equipos que están definiendo y construyendo experiencias agénticas.

En general, los agentes deben:

- Ampliar y escalar las capacidades humanas (generación de ideas, resolución de problemas, automatización, etc.)
- Rellenar vacíos de conocimiento (ponerse al día en dominios de conocimiento, traducción, etc.)
- Facilitar y apoyar la colaboración en las formas en que preferimos trabajar con otros
- Ayudarnos a ser mejores versiones de nosotros mismos (por ejemplo, entrenador de vida/gestor de tareas, ayudándonos a aprender habilidades de regulación emocional y mindfulness, construir resiliencia, etc.)

## En Esta Lección Veremos

- Qué son los Principios de Diseño Agéntico
- Qué pautas seguir al implementar estos principios de diseño
- Ejemplos de cómo usar estos principios de diseño

## Objetivos de Aprendizaje

Al completar esta lección, serás capaz de:

1. Explicar qué son los Principios de Diseño Agéntico
2. Explicar las pautas para usar los Principios de Diseño Agéntico
3. Comprender cómo construir un agente utilizando los Principios de Diseño Agéntico

## Los Principios de Diseño Agéntico

![Principios de Diseño Agéntico](../../../translated_images/agentic-design-principles.png?WT.19d6373397ba872c62b9237a927d1261a67e21e7c8e83274e53494a65e520a08.es.mc_id=academic-105485-koreyst)

### Agente (Espacio)

Este es el entorno en el que opera el agente. Estos principios informan cómo diseñamos agentes para interactuar en mundos físicos y digitales.

- **Conectar, no reemplazar** – ayuda a conectar a las personas con otras personas, eventos y conocimientos accionables para facilitar la colaboración y la conexión.
  - Los agentes ayudan a conectar eventos, conocimientos y personas.
  - Los agentes acercan a las personas. No están diseñados para reemplazar o minimizar a las personas.
- **Fácilmente accesible pero ocasionalmente invisible** – el agente opera mayormente en segundo plano y solo interviene cuando es relevante y apropiado.
  - El agente es fácilmente descubrible y accesible para usuarios autorizados en cualquier dispositivo o plataforma.
  - El agente admite entradas y salidas multimodales (sonido, voz, texto, etc.).
  - El agente puede cambiar sin problemas entre primer plano y segundo plano; entre ser proactivo y reactivo, dependiendo de las necesidades del usuario.
  - El agente puede operar de forma invisible, pero su proceso en segundo plano y su colaboración con otros agentes son transparentes y controlables para el usuario.

### Agente (Tiempo)

Esto se refiere a cómo opera el agente a lo largo del tiempo. Estos principios informan cómo diseñamos agentes que interactúan a través del pasado, presente y futuro.

- **Pasado**: Reflexionar sobre la historia que incluye tanto el estado como el contexto.
  - El agente proporciona resultados más relevantes basados en un análisis más rico de datos históricos más allá del evento, personas o estados.
  - El agente crea conexiones a partir de eventos pasados y reflexiona activamente sobre la memoria para interactuar con situaciones actuales.
- **Presente**: Más que notificar, motivar.
  - El agente adopta un enfoque integral para interactuar con las personas. Cuando ocurre un evento, el agente va más allá de una notificación estática u otra formalidad estática. Puede simplificar flujos o generar pistas dinámicamente para dirigir la atención del usuario en el momento adecuado.
  - El agente entrega información basada en el contexto ambiental, cambios sociales y culturales, y adaptada a la intención del usuario.
  - La interacción con el agente puede ser gradual, evolucionando/creciendo en complejidad para empoderar a los usuarios a largo plazo.
- **Futuro**: Adaptarse y evolucionar.
  - El agente se adapta a diversos dispositivos, plataformas y modalidades.
  - El agente se adapta al comportamiento del usuario, a sus necesidades de accesibilidad y es totalmente personalizable.
  - El agente se moldea y evoluciona a través de una interacción continua con el usuario.

### Agente (Núcleo)

Estos son los elementos clave en el núcleo del diseño de un agente.

- **Aceptar la incertidumbre pero establecer confianza**.
  - Se espera cierto nivel de incertidumbre en el agente. La incertidumbre es un elemento clave del diseño agéntico.
  - La confianza y la transparencia son capas fundamentales del diseño de agentes.
  - Los humanos tienen control sobre cuándo el agente está encendido/apagado, y el estado del agente es claramente visible en todo momento.

## Pautas Para Implementar Estos Principios

Cuando utilices los principios de diseño mencionados anteriormente, sigue estas pautas:

1. **Transparencia**: Informa al usuario que se está utilizando IA, cómo funciona (incluidas acciones pasadas) y cómo dar retroalimentación y modificar el sistema.
2. **Control**: Permite que el usuario personalice, especifique preferencias y personalice el sistema y sus atributos (incluida la capacidad de olvidar).
3. **Consistencia**: Busca experiencias consistentes y multimodales en dispositivos y puntos de interacción. Usa elementos de UI/UX familiares cuando sea posible (por ejemplo, ícono de micrófono para interacción por voz) y reduce la carga cognitiva del usuario tanto como sea posible (por ejemplo, respuestas concisas, ayudas visuales y contenido de "Aprender Más").

## Cómo Diseñar un Agente de Viajes Usando Estos Principios y Pautas

Imagina que estás diseñando un Agente de Viajes, así es como podrías pensar en usar los Principios de Diseño y las Pautas:

1. **Transparencia** – Informa al usuario que el Agente de Viajes es un agente habilitado por IA. Proporciona algunas instrucciones básicas sobre cómo empezar (por ejemplo, un mensaje de "Hola", ejemplos de preguntas). Documenta esto claramente en la página del producto. Muestra la lista de preguntas que el usuario ha hecho en el pasado. Deja claro cómo dar retroalimentación (pulgares arriba y abajo, botón "Enviar Comentarios", etc.). Articula claramente si el agente tiene restricciones de uso o de temas.
2. **Control** – Asegúrate de que sea claro cómo el usuario puede modificar el agente después de haber sido creado con cosas como el System Prompt. Permite al usuario elegir cuán detallado es el agente, su estilo de escritura y cualquier limitación sobre qué temas no debe abordar. Permite al usuario ver y eliminar cualquier archivo o dato asociado, preguntas y conversaciones pasadas.
3. **Consistencia** – Asegúrate de que los íconos para Compartir Pregunta, añadir un archivo o foto y etiquetar a alguien o algo sean estándar y reconocibles. Usa el ícono de clip para indicar la carga/compartición de archivos con el agente, y un ícono de imagen para indicar la carga de gráficos.

## Recursos Adicionales
- [Practices for Governing Agentic AI Systems | OpenAI](https://openai.com)
- [The HAX Toolkit Project - Microsoft Research](https://microsoft.com)
- [Responsible AI Toolbox](https://responsibleaitoolbox.ai)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.