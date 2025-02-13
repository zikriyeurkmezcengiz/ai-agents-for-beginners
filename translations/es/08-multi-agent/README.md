```markdown
# Patrones de diseño de múltiples agentes

Tan pronto como comiences a trabajar en un proyecto que involucre múltiples agentes, tendrás que considerar el patrón de diseño de múltiples agentes. Sin embargo, puede que no sea inmediatamente claro cuándo cambiar a múltiples agentes y cuáles son las ventajas.

## Introducción

En esta lección, buscamos responder las siguientes preguntas:

- ¿Cuáles son los escenarios en los que los múltiples agentes son aplicables? 
- ¿Cuáles son las ventajas de usar múltiples agentes en lugar de un solo agente realizando múltiples tareas? 
- ¿Cuáles son los componentes clave para implementar el patrón de diseño de múltiples agentes? 
- ¿Cómo podemos tener visibilidad sobre cómo los múltiples agentes interactúan entre sí?

## Objetivos de aprendizaje

Al finalizar esta lección, deberías ser capaz de:

- Identificar escenarios en los que los múltiples agentes son aplicables.
- Reconocer las ventajas de usar múltiples agentes en lugar de un solo agente.
- Comprender los componentes clave para implementar el patrón de diseño de múltiples agentes.

¿Cuál es el panorama general?

*Los múltiples agentes son un patrón de diseño que permite que varios agentes trabajen juntos para lograr un objetivo común.*

Este patrón se utiliza ampliamente en diversos campos, incluidos la robótica, los sistemas autónomos y la computación distribuida.

## Escenarios donde los múltiples agentes son aplicables

Entonces, ¿en qué escenarios es útil emplear múltiples agentes? La respuesta es que hay muchos casos donde el uso de múltiples agentes es beneficioso, especialmente en los siguientes casos:

- **Grandes cargas de trabajo**: Las grandes cargas de trabajo pueden dividirse en tareas más pequeñas y asignarse a diferentes agentes, lo que permite el procesamiento en paralelo y una finalización más rápida. Un ejemplo de esto sería una tarea de procesamiento de datos a gran escala.
- **Tareas complejas**: Las tareas complejas, al igual que las grandes cargas de trabajo, pueden descomponerse en subtareas más pequeñas y asignarse a diferentes agentes, cada uno especializado en un aspecto específico de la tarea. Un buen ejemplo sería el caso de vehículos autónomos donde diferentes agentes gestionan la navegación, la detección de obstáculos y la comunicación con otros vehículos.
- **Experiencia diversa**: Diferentes agentes pueden tener experiencias diversas, lo que les permite manejar diferentes aspectos de una tarea de manera más efectiva que un solo agente. Un ejemplo sería en el caso del sector salud, donde los agentes pueden gestionar diagnósticos, planes de tratamiento y monitoreo de pacientes.

## Ventajas de usar múltiples agentes en lugar de un solo agente

Un sistema de un solo agente podría funcionar bien para tareas simples, pero para tareas más complejas, el uso de múltiples agentes puede ofrecer varias ventajas:

- **Especialización**: Cada agente puede estar especializado en una tarea específica. La falta de especialización en un solo agente significa que este puede realizar muchas tareas, pero podría confundirse al enfrentarse a una tarea compleja. Por ejemplo, podría terminar realizando una tarea para la que no está mejor preparado.
- **Escalabilidad**: Es más fácil escalar sistemas agregando más agentes en lugar de sobrecargar a un solo agente.
- **Tolerancia a fallos**: Si un agente falla, otros pueden seguir funcionando, garantizando la fiabilidad del sistema.

Tomemos un ejemplo: reservar un viaje para un usuario. Un sistema de un solo agente tendría que manejar todos los aspectos del proceso de reserva, desde encontrar vuelos hasta reservar hoteles y autos de alquiler. Para lograr esto con un solo agente, este necesitaría herramientas para manejar todas estas tareas, lo que podría llevar a un sistema complejo y monolítico difícil de mantener y escalar. Un sistema de múltiples agentes, en cambio, podría tener diferentes agentes especializados en encontrar vuelos, reservar hoteles y autos de alquiler. Esto haría que el sistema fuera más modular, más fácil de mantener y escalable.

Compáralo con una agencia de viajes gestionada como un negocio familiar versus una agencia gestionada como una franquicia. El negocio familiar tendría un solo agente manejando todos los aspectos del proceso de reserva, mientras que la franquicia tendría diferentes agentes encargados de diferentes aspectos del proceso.

## Componentes clave para implementar el patrón de diseño de múltiples agentes

Antes de implementar el patrón de diseño de múltiples agentes, necesitas comprender los componentes clave que lo conforman.

Hagamos esto más concreto observando nuevamente el ejemplo de reservar un viaje para un usuario. En este caso, los componentes clave incluirían:

- **Comunicación entre agentes**: Los agentes encargados de encontrar vuelos, reservar hoteles y autos de alquiler necesitan comunicarse y compartir información sobre las preferencias y restricciones del usuario. Necesitas decidir los protocolos y métodos para esta comunicación. Concretamente, esto significa que el agente encargado de encontrar vuelos necesita comunicarse con el agente encargado de reservar hoteles para asegurarse de que el hotel esté reservado para las mismas fechas que el vuelo. Esto implica decidir *qué información comparten los agentes y cómo la comparten*.
- **Mecanismos de coordinación**: Los agentes necesitan coordinar sus acciones para asegurarse de que se cumplan las preferencias y restricciones del usuario. Por ejemplo, una preferencia del usuario podría ser un hotel cerca del aeropuerto, mientras que una restricción podría ser que solo haya autos de alquiler disponibles en el aeropuerto. Esto implica decidir *cómo los agentes coordinan sus acciones*.
- **Arquitectura de los agentes**: Los agentes necesitan tener una estructura interna para tomar decisiones y aprender de sus interacciones con el usuario. Por ejemplo, el agente encargado de encontrar vuelos necesita tener una estructura interna para decidir qué vuelos recomendar al usuario. Esto implica decidir *cómo los agentes toman decisiones y aprenden de sus interacciones con el usuario*. Un ejemplo podría ser que el agente encargado de encontrar vuelos use un modelo de aprendizaje automático para recomendar vuelos basados en las preferencias pasadas del usuario.
- **Visibilidad en las interacciones de múltiples agentes**: Necesitas tener visibilidad sobre cómo los múltiples agentes interactúan entre sí. Esto implica herramientas y técnicas para rastrear las actividades e interacciones de los agentes, como herramientas de registro y monitoreo, herramientas de visualización y métricas de rendimiento.
- **Patrones de múltiples agentes**: Existen diferentes patrones para implementar sistemas de múltiples agentes, como arquitecturas centralizadas, descentralizadas e híbridas. Necesitas decidir cuál es el patrón que mejor se adapta a tu caso de uso.
- **Intervención humana**: En la mayoría de los casos, habrá un humano en el proceso, y necesitas instruir a los agentes sobre cuándo pedir intervención humana. Esto podría ser, por ejemplo, cuando un usuario solicita un hotel o vuelo específico que los agentes no han recomendado o cuando se requiere confirmación antes de realizar una reserva.

## Visibilidad en las interacciones de múltiples agentes

Es importante tener visibilidad sobre cómo los múltiples agentes interactúan entre sí. Esta visibilidad es esencial para depurar, optimizar y garantizar la efectividad general del sistema. Para lograrlo, necesitas herramientas y técnicas para rastrear las actividades e interacciones de los agentes. Esto podría incluir herramientas de registro y monitoreo, herramientas de visualización y métricas de rendimiento.

Por ejemplo, en el caso de reservar un viaje para un usuario, podrías tener un panel que muestre el estado de cada agente, las preferencias y restricciones del usuario, y las interacciones entre los agentes. Este panel podría mostrar las fechas de viaje del usuario, los vuelos recomendados por el agente de vuelos, los hoteles recomendados por el agente de hoteles y los autos de alquiler recomendados por el agente de autos. Esto te daría una visión clara de cómo los agentes interactúan entre sí y si se están cumpliendo las preferencias y restricciones del usuario.

Veamos cada uno de estos aspectos en más detalle.

- **Herramientas de registro y monitoreo**: Deseas registrar cada acción realizada por un agente. Una entrada de registro podría almacenar información sobre el agente que realizó la acción, la acción realizada, el momento en que se realizó la acción y el resultado de la acción. Esta información puede usarse para depurar, optimizar y más.
- **Herramientas de visualización**: Las herramientas de visualización pueden ayudarte a ver las interacciones entre los agentes de una manera más intuitiva. Por ejemplo, podrías tener un gráfico que muestre el flujo de información entre los agentes. Esto podría ayudarte a identificar cuellos de botella, ineficiencias y otros problemas en el sistema.
- **Métricas de rendimiento**: Las métricas de rendimiento pueden ayudarte a rastrear la efectividad del sistema de múltiples agentes. Por ejemplo, podrías rastrear el tiempo necesario para completar una tarea, la cantidad de tareas completadas por unidad de tiempo y la precisión de las recomendaciones hechas por los agentes. Esta información puede ayudarte a identificar áreas de mejora y optimizar el sistema.

## Patrones de múltiples agentes

Vamos a profundizar en algunos patrones concretos que podemos usar para crear aplicaciones de múltiples agentes. Aquí hay algunos patrones interesantes a considerar:

### Chat grupal

Este patrón es útil cuando deseas crear una aplicación de chat grupal donde múltiples agentes puedan comunicarse entre sí. Los casos de uso típicos para este patrón incluyen colaboración en equipo, soporte al cliente y redes sociales.

En este patrón, cada agente representa a un usuario en el chat grupal, y los mensajes se intercambian entre agentes utilizando un protocolo de mensajería. Los agentes pueden enviar mensajes al chat grupal, recibir mensajes del chat grupal y responder a mensajes de otros agentes.

Este patrón puede implementarse utilizando una arquitectura centralizada donde todos los mensajes se enrutan a través de un servidor central, o una arquitectura descentralizada donde los mensajes se intercambian directamente.

![Chat grupal](../../../translated_images/multi-agent-group-chat.82d537c5c8dc833abbd252033e60874bc9d00df7193888b3377f8426449a0b20.es.png)

### Transferencia de tareas

Este patrón es útil cuando deseas crear una aplicación donde múltiples agentes puedan transferirse tareas entre sí.

Los casos de uso típicos para este patrón incluyen soporte al cliente, gestión de tareas y automatización de flujos de trabajo.

En este patrón, cada agente representa una tarea o un paso en un flujo de trabajo, y los agentes pueden transferirse tareas a otros agentes basándose en reglas predefinidas.

![Transferencia de tareas](../../../translated_images/multi-agent-hand-off.ed4f0a5a58614a8a3e962fc476187e630a3ba309d066e460f017b503d0b84cfc.es.png)

### Filtrado colaborativo

Este patrón es útil cuando deseas crear una aplicación donde múltiples agentes puedan colaborar para hacer recomendaciones a los usuarios.

¿Por qué querrías que múltiples agentes colaboren? Porque cada agente puede tener diferentes especialidades y contribuir al proceso de recomendación de maneras distintas.

Tomemos un ejemplo donde un usuario desea una recomendación sobre la mejor acción para comprar en el mercado bursátil.

- **Experto en la industria**: Un agente podría ser experto en una industria específica.
- **Análisis técnico**: Otro agente podría ser experto en análisis técnico.
- **Análisis fundamental**: Y otro agente podría ser experto en análisis fundamental. Al colaborar, estos agentes pueden proporcionar una recomendación más completa al usuario.

![Recomendación](../../../translated_images/multi-agent-filtering.719217d169391ddb118bbb726b19d4d89ee139f960f8749ccb2400efb4d0ce79.es.png)

## Escenario: Proceso de reembolso

Consideremos un escenario donde un cliente está intentando obtener un reembolso por un producto. Podrían involucrarse varios agentes en este proceso, pero dividámoslos entre agentes específicos para este proceso y agentes generales que pueden usarse en otros procesos.

**Agentes específicos para el proceso de reembolso**:

A continuación, algunos agentes que podrían estar involucrados en el proceso de reembolso:

- **Agente del cliente**: Representa al cliente y es responsable de iniciar el proceso de reembolso.
- **Agente del vendedor**: Representa al vendedor y es responsable de procesar el reembolso.
- **Agente de pagos**: Representa el proceso de pago y es responsable de reembolsar el pago del cliente.
- **Agente de resolución**: Representa el proceso de resolución y es responsable de resolver cualquier problema que surja durante el proceso de reembolso.
- **Agente de cumplimiento**: Representa el proceso de cumplimiento y es responsable de garantizar que el proceso de reembolso cumpla con las regulaciones y políticas.

**Agentes generales**:

Estos agentes pueden usarse en otras partes de tu negocio.

- **Agente de envíos**: Representa el proceso de envío y es responsable de devolver el producto al vendedor. Este agente puede usarse tanto para el proceso de reembolso como para el envío general de un producto, por ejemplo, tras una compra.
- **Agente de retroalimentación**: Representa el proceso de retroalimentación y es responsable de recopilar opiniones del cliente. La retroalimentación podría obtenerse en cualquier momento, no solo durante el proceso de reembolso.
- **Agente de escalamiento**: Representa el proceso de escalamiento y es responsable de escalar problemas a un nivel superior de soporte. Este tipo de agente puede usarse en cualquier proceso donde sea necesario escalar un problema.
- **Agente de notificaciones**: Representa el proceso de notificaciones y es responsable de enviar notificaciones al cliente en varias etapas del proceso de reembolso.
- **Agente de análisis**: Representa el proceso de análisis y es responsable de analizar datos relacionados con el proceso de reembolso.
- **Agente de auditoría**: Representa el proceso de auditoría y es responsable de auditar el proceso de reembolso para garantizar que se esté llevando a cabo correctamente.
- **Agente de reportes**: Representa el proceso de reportes y es responsable de generar informes sobre el proceso de reembolso.
- **Agente de conocimiento**: Representa el proceso de conocimiento y es responsable de mantener una base de conocimientos relacionada con el proceso de reembolso. Este agente podría ser experto tanto en reembolsos como en otras áreas de tu negocio.
- **Agente de seguridad**: Representa el proceso de seguridad y es responsable de garantizar la seguridad del proceso de reembolso.
- **Agente de calidad**: Representa el proceso de calidad y es responsable de garantizar la calidad del proceso de reembolso.

Hay bastantes agentes enumerados arriba, tanto para el proceso específico de reembolso como para los agentes generales que pueden usarse en otras partes de tu negocio. Esperamos que esto te dé una idea de cómo decidir qué agentes usar en tu sistema de múltiples agentes.

## Tarea

¿Cuál sería una buena tarea para esta lección?

Diseña un sistema de múltiples agentes para un proceso de soporte al cliente. Identifica los agentes involucrados en el proceso, sus roles y responsabilidades, y cómo interactúan entre sí. Considera tanto los agentes específicos del proceso de soporte al cliente como los agentes generales que pueden usarse en otras partes de tu negocio.

> Reflexiona antes de leer la solución a continuación; podrías necesitar más agentes de los que crees.

> TIP: Piensa en las diferentes etapas del proceso de soporte al cliente y considera también los agentes necesarios para cualquier sistema.

## Solución

[Solución](./solution/solution.md)

## Verificaciones de conocimiento

Pregunta: ¿Cuándo deberías considerar usar múltiples agentes?

- [] A1: Cuando tienes una pequeña carga de trabajo y una tarea simple.
- [] A2: Cuando tienes una gran carga de trabajo.
- [] A3: Cuando tienes una tarea simple.

[Solución del cuestionario](./solution/solution-quiz.md)

## Resumen

En esta lección, hemos explorado el patrón de diseño de múltiples agentes, incluidos los escenarios donde son aplicables, las ventajas de usar múltiples agentes en lugar de un solo agente, los componentes clave para implementar el patrón de diseño de múltiples agentes y cómo tener visibilidad sobre cómo los múltiples agentes interactúan entre sí.

## Recursos adicionales

- [Autogen design patterns](https://microsoft.github.io/autogen/0.4.0.dev4/user-guide/core-user-guide/design-patterns/index.html)
- [Agentic design patterns](https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/)
```

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.