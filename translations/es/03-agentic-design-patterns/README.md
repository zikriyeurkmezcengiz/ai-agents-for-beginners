# Principios de Diseño Agéntico para IA

## Introducción

Existen muchas formas de abordar la construcción de Sistemas de IA Agénticos. Dado que la ambigüedad es una característica y no un defecto en el diseño de IA Generativa, a veces puede ser difícil para los ingenieros saber por dónde empezar. Hemos creado un conjunto de Principios de Diseño centrados en el usuario para permitir a los desarrolladores construir sistemas agénticos enfocados en el cliente que resuelvan sus necesidades empresariales. Estos principios de diseño no son una arquitectura prescriptiva, sino un punto de partida para los equipos que están definiendo y desarrollando experiencias agénticas.

En general, los agentes deben:

- Ampliar y escalar las capacidades humanas (generación de ideas, resolución de problemas, automatización, etc.)
- Completar vacíos de conocimiento (ponernos al día en dominios de conocimiento, traducción, etc.)
- Facilitar y apoyar la colaboración en las formas en que preferimos trabajar con otros como individuos
- Hacernos mejores versiones de nosotros mismos (por ejemplo, como entrenador de vida/gestor de tareas, ayudándonos a aprender habilidades de regulación emocional y atención plena, fomentando la resiliencia, etc.)

## Esta Lección Cubrirá

- Qué son los Principios de Diseño Agéntico
- Cuáles son algunas pautas a seguir al implementar estos principios de diseño
- Algunos ejemplos de uso de los principios de diseño

## Objetivos de Aprendizaje

Después de completar esta lección, serás capaz de:

1. Explicar qué son los Principios de Diseño Agéntico  
2. Explicar las pautas para usar los Principios de Diseño Agéntico  
3. Comprender cómo construir un agente utilizando los Principios de Diseño Agéntico  

## Los Principios de Diseño Agéntico

![Principios de Diseño Agéntico](../../../translated_images/agentic-design-principles.png?WT.19d6373397ba872c62b9237a927d1261a67e21e7c8e83274e53494a65e520a08.es.mc_id=academic-105485-koreyst)

### Agente (Espacio)

Este es el entorno en el que opera el agente. Estos principios guían cómo diseñamos agentes para interactuar en mundos físicos y digitales.

- **Conectar, no reemplazar** – ayuda a conectar a las personas con otras personas, eventos y conocimiento accionable para habilitar la colaboración y la conexión.
  - Los agentes ayudan a conectar eventos, conocimiento y personas.
  - Los agentes acercan a las personas. No están diseñados para reemplazar ni menospreciar a las personas.
- **Fácilmente accesible pero ocasionalmente invisible** – el agente opera mayormente en segundo plano y solo nos alerta cuando es relevante y apropiado.
  - El agente es fácil de descubrir y accesible para usuarios autorizados en cualquier dispositivo o plataforma.
  - El agente soporta entradas y salidas multimodales (sonido, voz, texto, etc.).
  - El agente puede cambiar sin problemas entre primer plano y segundo plano; entre proactivo y reactivo, dependiendo de su percepción de las necesidades del usuario.
  - El agente puede operar de forma invisible, pero su proceso en segundo plano y su colaboración con otros agentes son transparentes y controlables por el usuario.

### Agente (Tiempo)

Esto se refiere a cómo opera el agente a lo largo del tiempo. Estos principios guían cómo diseñamos agentes que interactúan a través del pasado, presente y futuro.

- **Pasado**: Reflexionando sobre el historial que incluye tanto estado como contexto.
  - El agente proporciona resultados más relevantes basados en el análisis de datos históricos más ricos que van más allá del evento, las personas o los estados.
  - El agente crea conexiones a partir de eventos pasados y reflexiona activamente sobre la memoria para interactuar con situaciones actuales.
- **Ahora**: Más sugerir que notificar.
  - El agente adopta un enfoque integral para interactuar con las personas. Cuando ocurre un evento, el agente va más allá de una notificación estática o cualquier formalidad estática. Puede simplificar flujos o generar dinámicamente indicaciones para dirigir la atención del usuario en el momento adecuado.
  - El agente entrega información basada en el contexto ambiental, cambios sociales y culturales, y está adaptada a la intención del usuario.
  - La interacción del agente puede ser gradual, evolucionando/creciendo en complejidad para empoderar a los usuarios a largo plazo.
- **Futuro**: Adaptarse y evolucionar.
  - El agente se adapta a diversos dispositivos, plataformas y modalidades.
  - El agente se ajusta al comportamiento del usuario, necesidades de accesibilidad y es completamente personalizable.
  - El agente se moldea y evoluciona a través de la interacción continua con el usuario.

### Agente (Núcleo)

Estos son los elementos clave en el núcleo del diseño de un agente.

- **Aceptar la incertidumbre pero establecer confianza**.
  - Se espera cierto nivel de incertidumbre en el agente. La incertidumbre es un elemento clave del diseño agéntico.
  - La confianza y la transparencia son capas fundamentales del diseño del agente.
  - Los humanos tienen el control de cuándo el agente está activado/desactivado, y el estado del agente es claramente visible en todo momento.

## Las Pautas para Implementar Estos Principios

Cuando uses los principios de diseño anteriores, sigue estas pautas:

1. **Transparencia**: Informa al usuario que hay IA involucrada, cómo funciona (incluyendo acciones pasadas) y cómo proporcionar retroalimentación y modificar el sistema.
2. **Control**: Permite al usuario personalizar, especificar preferencias y personalizar, y tener control sobre el sistema y sus atributos (incluyendo la capacidad de olvidar).
3. **Consistencia**: Busca experiencias consistentes y multimodales en dispositivos y puntos de contacto. Usa elementos familiares de UI/UX cuando sea posible (por ejemplo, el ícono de micrófono para interacción por voz) y reduce la carga cognitiva del cliente tanto como sea posible (por ejemplo, respuestas concisas, ayudas visuales y contenido de "Aprender más").

## Cómo Diseñar un Agente de Viajes Usando Estos Principios y Pautas

Imagina que estás diseñando un Agente de Viajes. Así podrías pensar en usar los Principios de Diseño y Pautas:

1. **Transparencia** – Informa al usuario que el Agente de Viajes es un agente habilitado por IA. Proporciona algunas instrucciones básicas para comenzar (por ejemplo, un mensaje de "Hola", ejemplos de indicaciones). Documenta esto claramente en la página del producto. Muestra la lista de indicaciones que el usuario ha solicitado en el pasado. Haz que sea claro cómo dar retroalimentación (pulgares arriba o abajo, botón de Enviar Retroalimentación, etc.). Articula claramente si el agente tiene restricciones de uso o temas.
2. **Control** – Asegúrate de que esté claro cómo el usuario puede modificar el agente después de que ha sido creado, con cosas como el Prompt del Sistema. Permite al usuario elegir qué tan detallado es el agente, su estilo de escritura y cualquier limitación sobre lo que el agente no debe hablar. Permite al usuario ver y eliminar cualquier archivo o dato asociado, indicaciones y conversaciones pasadas.
3. **Consistencia** – Asegúrate de que los íconos para Compartir Indicación, agregar un archivo o foto y etiquetar a alguien o algo sean estándar y reconocibles. Usa el ícono de clip para indicar carga/compartición de archivos con el agente, y un ícono de imagen para indicar la carga de gráficos.

## Recursos Adicionales
- [Practices for Governing Agentic AI Systems | OpenAI](https://openai.com)  
- [The HAX Toolkit Project - Microsoft Research](https://microsoft.com)  
- [Responsible AI Toolbox](https://responsibleaitoolbox.ai)  

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.