```markdown
# Metacognición en Agentes de IA

## Introducción

¡Bienvenido a la lección sobre metacognición en agentes de IA! Este capítulo está diseñado para principiantes que tienen curiosidad sobre cómo los agentes de IA pueden reflexionar sobre sus propios procesos de pensamiento. Al final de esta lección, comprenderás conceptos clave y estarás equipado con ejemplos prácticos para aplicar la metacognición en el diseño de agentes de IA.

## Objetivos de Aprendizaje

Después de completar esta lección, serás capaz de:

1. Comprender las implicaciones de los bucles de razonamiento en las definiciones de agentes.
2. Utilizar técnicas de planificación y evaluación para ayudar a agentes autocorrectivos.
3. Crear tus propios agentes capaces de manipular código para realizar tareas.

## Introducción a la Metacognición

La metacognición se refiere a los procesos cognitivos de orden superior que implican reflexionar sobre el propio pensamiento. Para los agentes de IA, esto significa ser capaces de evaluar y ajustar sus acciones basándose en la autoconciencia y experiencias pasadas.

### ¿Qué es la Metacognición?

La metacognición, o "pensar sobre el pensamiento", es un proceso cognitivo de orden superior que implica la autoconciencia y la autorregulación de los propios procesos cognitivos. En el ámbito de la IA, la metacognición permite a los agentes evaluar y adaptar sus estrategias y acciones, lo que conduce a capacidades mejoradas de resolución de problemas y toma de decisiones. Al comprender la metacognición, puedes diseñar agentes de IA que no solo sean más inteligentes, sino también más adaptables y eficientes.

### Importancia de la Metacognición en Agentes de IA

La metacognición desempeña un papel crucial en el diseño de agentes de IA por varias razones:

![Importancia de la Metacognición](../../../09-metacognition/images/importance-of-metacognition.png)

- **Auto-reflexión**: Los agentes pueden evaluar su propio desempeño e identificar áreas de mejora.
- **Adaptabilidad**: Los agentes pueden modificar sus estrategias basándose en experiencias pasadas y entornos cambiantes.
- **Corrección de errores**: Los agentes pueden detectar y corregir errores de forma autónoma, lo que lleva a resultados más precisos.
- **Gestión de recursos**: Los agentes pueden optimizar el uso de recursos, como tiempo y poder computacional, mediante la planificación y evaluación de sus acciones.

## Componentes de un Agente de IA

Antes de profundizar en los procesos metacognitivos, es esencial comprender los componentes básicos de un agente de IA. Un agente de IA típicamente consta de:

- **Persona**: La personalidad y características del agente, que definen cómo interactúa con los usuarios.
- **Herramientas**: Las capacidades y funciones que el agente puede realizar.
- **Habilidades**: El conocimiento y la experiencia que posee el agente.

Estos componentes trabajan juntos para crear una "unidad de experiencia" que puede realizar tareas específicas.

**Ejemplo**: Considera un agente de viajes, un servicio que no solo planifica tus vacaciones, sino que también ajusta su camino basado en datos en tiempo real y experiencias de clientes anteriores.

### Ejemplo: Metacognición en un Servicio de Agente de Viajes

Imagina que estás diseñando un servicio de agente de viajes impulsado por IA. Este agente, "Agente de Viajes", ayuda a los usuarios a planificar sus vacaciones. Para incorporar metacognición, el Agente de Viajes necesita evaluar y ajustar sus acciones basándose en la autoconciencia y experiencias pasadas. Aquí se muestra cómo la metacognición podría desempeñar un papel:

#### Tarea Actual

La tarea actual es ayudar a un usuario a planificar un viaje a París.

#### Pasos para Completar la Tarea

1. **Recopilar Preferencias del Usuario**: Preguntar al usuario sobre sus fechas de viaje, presupuesto, intereses (por ejemplo, museos, gastronomía, compras) y cualquier requisito específico.
2. **Recuperar Información**: Buscar opciones de vuelos, alojamientos, atracciones y restaurantes que coincidan con las preferencias del usuario.
3. **Generar Recomendaciones**: Proporcionar un itinerario personalizado con detalles de vuelos, reservas de hoteles y actividades sugeridas.
4. **Ajustar Basado en Retroalimentación**: Solicitar al usuario comentarios sobre las recomendaciones y realizar los ajustes necesarios.

#### Recursos Necesarios

- Acceso a bases de datos de reservas de vuelos y hoteles.
- Información sobre atracciones y restaurantes en París.
- Datos de retroalimentación de usuarios de interacciones previas.

#### Experiencia y Auto-reflexión

El Agente de Viajes utiliza la metacognición para evaluar su desempeño y aprender de experiencias pasadas. Por ejemplo:

1. **Analizar la Retroalimentación del Usuario**: El Agente de Viajes revisa los comentarios de los usuarios para determinar qué recomendaciones fueron bien recibidas y cuáles no. Ajusta sus futuras sugerencias en consecuencia.
2. **Adaptabilidad**: Si un usuario ha mencionado previamente que no le gustan los lugares concurridos, el Agente de Viajes evitará recomendar sitios turísticos populares en horas pico en el futuro.
3. **Corrección de Errores**: Si el Agente de Viajes cometió un error en una reserva pasada, como sugerir un hotel que estaba completamente reservado, aprende a verificar la disponibilidad más rigurosamente antes de hacer recomendaciones.

#### Ejemplo Práctico para Desarrolladores

Aquí tienes un ejemplo simplificado de cómo podría verse el código del Agente de Viajes al incorporar metacognición:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Por Qué Importa la Metacognición

- **Auto-reflexión**: Los agentes pueden analizar su desempeño e identificar áreas de mejora.
- **Adaptabilidad**: Los agentes pueden modificar estrategias basándose en retroalimentación y condiciones cambiantes.
- **Corrección de Errores**: Los agentes pueden detectar y corregir errores de forma autónoma.
- **Gestión de Recursos**: Los agentes pueden optimizar el uso de recursos, como tiempo y poder computacional.

Al incorporar la metacognición, el Agente de Viajes puede proporcionar recomendaciones de viaje más personalizadas y precisas, mejorando la experiencia general del usuario.

---

## 2. Planificación en Agentes

La planificación es un componente crítico del comportamiento de los agentes de IA. Implica delinear los pasos necesarios para alcanzar un objetivo, considerando el estado actual, los recursos y los posibles obstáculos.

### Elementos de la Planificación

- **Tarea Actual**: Definir claramente la tarea.
- **Pasos para Completar la Tarea**: Dividir la tarea en pasos manejables.
- **Recursos Necesarios**: Identificar los recursos necesarios.
- **Experiencia**: Utilizar experiencias pasadas para informar la planificación.

**Ejemplo**: Aquí están los pasos que el Agente de Viajes necesita tomar para ayudar a un usuario a planificar su viaje de manera efectiva:

### Pasos para el Agente de Viajes

1. **Recopilar Preferencias del Usuario**
   - Preguntar al usuario detalles sobre sus fechas de viaje, presupuesto, intereses y cualquier requisito específico.
   - Ejemplos: "¿Cuándo planeas viajar?" "¿Cuál es tu rango de presupuesto?" "¿Qué actividades disfrutas en vacaciones?"

2. **Recuperar Información**
   - Buscar opciones de viaje relevantes basándose en las preferencias del usuario.
   - **Vuelos**: Buscar vuelos disponibles dentro del presupuesto y las fechas preferidas del usuario.
   - **Alojamientos**: Encontrar hoteles o propiedades en alquiler que coincidan con las preferencias del usuario en ubicación, precio y comodidades.
   - **Atracciones y Restaurantes**: Identificar atracciones populares, actividades y opciones de comida que se alineen con los intereses del usuario.

3. **Generar Recomendaciones**
   - Compilar la información recuperada en un itinerario personalizado.
   - Proporcionar detalles como opciones de vuelos, reservas de hoteles y actividades sugeridas, asegurándose de adaptar las recomendaciones a las preferencias del usuario.

4. **Presentar el Itinerario al Usuario**
   - Compartir el itinerario propuesto con el usuario para su revisión.
   - Ejemplo: "Aquí tienes un itinerario sugerido para tu viaje a París. Incluye detalles de vuelos, reservas de hotel y una lista de actividades y restaurantes recomendados. ¡Déjame saber qué opinas!"

5. **Recopilar Retroalimentación**
   - Preguntar al usuario por comentarios sobre el itinerario propuesto.
   - Ejemplos: "¿Te gustan las opciones de vuelo?" "¿Es adecuado el hotel para tus necesidades?" "¿Hay actividades que te gustaría añadir o eliminar?"

6. **Ajustar Basado en Retroalimentación**
   - Modificar el itinerario basándose en los comentarios del usuario.
   - Realizar los cambios necesarios en las recomendaciones de vuelos, alojamiento y actividades para que coincidan mejor con las preferencias del usuario.

7. **Confirmación Final**
   - Presentar el itinerario actualizado al usuario para su confirmación final.
   - Ejemplo: "He realizado los ajustes basándome en tus comentarios. Aquí está el itinerario actualizado. ¿Todo se ve bien para ti?"

8. **Reservar y Confirmar**
   - Una vez que el usuario apruebe el itinerario, proceder con la reserva de vuelos, alojamientos y cualquier actividad planificada.
   - Enviar detalles de confirmación al usuario.

9. **Proveer Soporte Continuo**
   - Permanecer disponible para asistir al usuario con cualquier cambio o solicitud adicional antes y durante su viaje.
   - Ejemplo: "Si necesitas más ayuda durante tu viaje, ¡no dudes en contactarme en cualquier momento!"

### Ejemplo de Interacción

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage within a booing request
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```
```
```markdown
El agente de viajes formula nuevas consultas de búsqueda basadas en los comentarios de los usuarios.  
- Ejemplo: ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```  
- **Herramienta**: El agente de viajes utiliza algoritmos para clasificar y filtrar nuevos resultados de búsqueda, enfatizando la relevancia basada en los comentarios de los usuarios.  
- Ejemplo: ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```  
- **Evaluación**: El agente de viajes evalúa continuamente la relevancia y precisión de sus recomendaciones analizando los comentarios de los usuarios y realizando los ajustes necesarios.  
- Ejemplo: ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```  

#### Ejemplo práctico  
Aquí hay un ejemplo simplificado de código Python que incorpora el enfoque Corrective RAG en el agente de viajes:  
```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```  

### Carga de contexto preventiva  
La carga de contexto preventiva implica cargar información de contexto relevante o antecedentes en el modelo antes de procesar una consulta. Esto significa que el modelo tiene acceso a esta información desde el inicio, lo que puede ayudarle a generar respuestas más informadas sin necesidad de recuperar datos adicionales durante el proceso.  

Aquí hay un ejemplo simplificado de cómo podría verse una carga de contexto preventiva para una aplicación de agente de viajes en Python:  
```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```  

#### Explicación  
1. **Inicialización (`__init__` method)**: The `TravelAgent` class pre-loads a dictionary containing information about popular destinations such as Paris, Tokyo, New York, and Sydney. This dictionary includes details like the country, currency, language, and major attractions for each destination.

2. **Retrieving Information (`get_destination_info` method)**: When a user queries about a specific destination, the `get_destination_info` method)**: Este método obtiene la información relevante del diccionario de contexto precargado. Al precargar el contexto, la aplicación del agente de viajes puede responder rápidamente a las consultas de los usuarios sin tener que recuperar esta información de una fuente externa en tiempo real. Esto hace que la aplicación sea más eficiente y receptiva.  

### Iniciar el plan con un objetivo antes de iterar  
Iniciar un plan con un objetivo implica comenzar con un resultado claro u objetivo en mente. Al definir este objetivo desde el principio, el modelo puede usarlo como un principio guía durante todo el proceso iterativo. Esto ayuda a garantizar que cada iteración se acerque más a lograr el resultado deseado, haciendo que el proceso sea más eficiente y enfocado.  

Aquí hay un ejemplo de cómo podrías iniciar un plan de viaje con un objetivo antes de iterar para un agente de viajes en Python:  

### Escenario  
Un agente de viajes quiere planificar unas vacaciones personalizadas para un cliente. El objetivo es crear un itinerario de viaje que maximice la satisfacción del cliente en función de sus preferencias y presupuesto.  

### Pasos  
1. Definir las preferencias y el presupuesto del cliente.  
2. Iniciar el plan inicial basado en estas preferencias.  
3. Iterar para refinar el plan, optimizándolo para la satisfacción del cliente.  

#### Código Python  
```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Example usage
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```  

#### Explicación del código  
1. **Inicialización (`__init__` method)**: The `TravelAgent` class is initialized with a list of potential destinations, each having attributes like name, cost, and activity type.

2. **Bootstrapping the Plan (`bootstrap_plan` method)**: This method creates an initial travel plan based on the client's preferences and budget. It iterates through the list of destinations and adds them to the plan if they match the client's preferences and fit within the budget.

3. **Matching Preferences (`match_preferences` method)**: This method checks if a destination matches the client's preferences.

4. **Iterating the Plan (`iterate_plan` method)**: This method refines the initial plan by trying to replace each destination in the plan with a better match, considering the client's preferences and budget constraints.

5. **Calculating Cost (`calculate_cost` method)**: Este método calcula el costo total del plan actual, incluido un posible nuevo destino.  

#### Uso del ejemplo  
- **Plan inicial**: El agente de viajes crea un plan inicial basado en las preferencias del cliente para hacer turismo y un presupuesto de $2000.  
- **Plan refinado**: El agente de viajes itera el plan, optimizándolo para las preferencias y el presupuesto del cliente.  

Al iniciar el plan con un objetivo claro (por ejemplo, maximizar la satisfacción del cliente) y iterar para refinar el plan, el agente de viajes puede crear un itinerario de viaje personalizado y optimizado para el cliente. Este enfoque asegura que el plan de viaje se alinee con las preferencias y el presupuesto del cliente desde el principio y mejore con cada iteración.  

### Aprovechar los LLM para reordenar y puntuar  
Los modelos de lenguaje de gran escala (LLM, por sus siglas en inglés) pueden usarse para reordenar y puntuar evaluando la relevancia y calidad de los documentos recuperados o respuestas generadas. Así es como funciona:  

**Recuperación:** El paso inicial de recuperación obtiene un conjunto de documentos o respuestas candidatas basados en la consulta.  
**Reordenamiento:** El LLM evalúa estos candidatos y los reordena en función de su relevancia y calidad. Este paso asegura que la información más relevante y de alta calidad se presente primero.  
**Puntuación:** El LLM asigna puntajes a cada candidato, reflejando su relevancia y calidad. Esto ayuda a seleccionar la mejor respuesta o documento para el usuario.  

Al aprovechar los LLM para reordenar y puntuar, el sistema puede proporcionar información más precisa y contextualmente relevante, mejorando la experiencia general del usuario.  

Aquí hay un ejemplo de cómo un agente de viajes podría usar un modelo de lenguaje de gran escala (LLM) para reordenar y puntuar destinos de viaje basados en las preferencias del usuario en Python:  

#### Escenario - Viajes basados en preferencias  
Un agente de viajes quiere recomendar los mejores destinos de viaje a un cliente basado en sus preferencias. El LLM ayudará a reordenar y puntuar los destinos para asegurar que se presenten las opciones más relevantes.  

#### Pasos:  
1. Recopilar las preferencias del usuario.  
2. Recuperar una lista de posibles destinos de viaje.  
3. Usar el LLM para reordenar y puntuar los destinos basados en las preferencias del usuario.  

Aquí se explica cómo puedes actualizar el ejemplo anterior para usar los servicios de Azure OpenAI:  

#### Requisitos  
1. Necesitas una suscripción a Azure.  
2. Crear un recurso de Azure OpenAI y obtener tu clave API.  

#### Código Python de ejemplo  
```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Example usage
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```  

#### Explicación del código - Preference Booker  
1. **Inicialización**: El método `TravelAgent` class is initialized with a list of potential travel destinations, each having attributes like name and description.

2. **Getting Recommendations (`get_recommendations` method)**: This method generates a prompt for the Azure OpenAI service based on the user's preferences and makes an HTTP POST request to the Azure OpenAI API to get re-ranked and scored destinations.

3. **Generating Prompt (`generate_prompt` method)**: This method constructs a prompt for the Azure OpenAI, including the user's preferences and the list of destinations. The prompt guides the model to re-rank and score the destinations based on the provided preferences.

4. **API Call**: The `requests` library is used to make an HTTP POST request to the Azure OpenAI API endpoint. The response contains the re-ranked and scored destinations.

5. **Example Usage**: The travel agent collects user preferences (e.g., interest in sightseeing and diverse culture) and uses the Azure OpenAI service to get re-ranked and scored recommendations for travel destinations.

Make sure to replace `your_azure_openai_api_key` with your actual Azure OpenAI API key and `https://your-endpoint.com/...` debe reemplazarse con la URL real del punto de conexión de tu implementación de Azure OpenAI.  

Al aprovechar el LLM para reordenar y puntuar, el agente de viajes puede proporcionar recomendaciones de viaje más personalizadas y relevantes a los clientes, mejorando su experiencia general.  
```
los mejores museos en París?"). - **Intención de Navegación**: El usuario quiere navegar a un sitio web o página específica (por ejemplo, "sitio web oficial del Museo del Louvre"). - **Intención Transaccional**: El usuario busca realizar una transacción, como reservar un vuelo o hacer una compra (por ejemplo, "Reservar un vuelo a París"). 2. **Conciencia del Contexto**: - Analizar el contexto de la consulta del usuario ayuda a identificar con precisión su intención. Esto incluye considerar interacciones previas, preferencias del usuario y los detalles específicos de la consulta actual. 3. **Procesamiento de Lenguaje Natural (NLP)**: - Se emplean técnicas de NLP para comprender e interpretar las consultas en lenguaje natural proporcionadas por los usuarios. Esto incluye tareas como reconocimiento de entidades, análisis de sentimientos y análisis de consultas. 4. **Personalización**: - Personalizar los resultados de búsqueda en función del historial, preferencias y retroalimentación del usuario mejora la relevancia de la información recuperada. #### Ejemplo Práctico: Búsqueda con Intención en Agente de Viajes Tomemos como ejemplo un Agente de Viajes para ver cómo se puede implementar la búsqueda con intención. 1. **Recolección de Preferencias del Usuario** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **Comprensión de la Intención del Usuario** ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ``` 3. **Conciencia del Contexto** ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ``` 4. **Búsqueda y Personalización de Resultados** ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ``` 5. **Ejemplo de Uso** ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ``` --- ## 4. Generación de Código como Herramienta Los agentes generadores de código utilizan modelos de IA para escribir y ejecutar código, resolviendo problemas complejos y automatizando tareas. ### Agentes Generadores de Código Los agentes generadores de código utilizan modelos de IA generativa para escribir y ejecutar código. Estos agentes pueden resolver problemas complejos, automatizar tareas y proporcionar información valiosa al generar y ejecutar código en varios lenguajes de programación. #### Aplicaciones Prácticas 1. **Generación Automática de Código**: Generar fragmentos de código para tareas específicas, como análisis de datos, scraping web o aprendizaje automático. 2. **SQL como RAG**: Usar consultas SQL para recuperar y manipular datos de bases de datos. 3. **Resolución de Problemas**: Crear y ejecutar código para resolver problemas específicos, como optimizar algoritmos o analizar datos. #### Ejemplo: Agente Generador de Código para Análisis de Datos Imagina que estás diseñando un agente generador de código. Así es como podría funcionar: 1. **Tarea**: Analizar un conjunto de datos para identificar tendencias y patrones. 2. **Pasos**: - Cargar el conjunto de datos en una herramienta de análisis de datos. - Generar consultas SQL para filtrar y agregar los datos. - Ejecutar las consultas y recuperar los resultados. - Usar los resultados para generar visualizaciones y conocimientos. 3. **Recursos Requeridos**: Acceso al conjunto de datos, herramientas de análisis de datos y capacidades de SQL. 4. **Experiencia**: Usar resultados de análisis anteriores para mejorar la precisión y relevancia de análisis futuros. ### Ejemplo: Agente Generador de Código para Agente de Viajes En este ejemplo, diseñaremos un agente generador de código, Agente de Viajes, para ayudar a los usuarios a planificar sus viajes generando y ejecutando código. Este agente puede manejar tareas como buscar opciones de viaje, filtrar resultados y compilar un itinerario utilizando IA generativa. #### Resumen del Agente Generador de Código 1. **Recolección de Preferencias del Usuario**: Recopila la información del usuario, como destino, fechas de viaje, presupuesto e intereses. 2. **Generación de Código para Recuperar Datos**: Genera fragmentos de código para recuperar datos sobre vuelos, hoteles y atracciones. 3. **Ejecución del Código Generado**: Ejecuta el código generado para obtener información en tiempo real. 4. **Generación de Itinerario**: Compila los datos obtenidos en un plan de viaje personalizado. 5. **Ajustes Basados en Retroalimentación**: Recibe retroalimentación del usuario y regenera el código si es necesario para refinar los resultados. #### Implementación Paso a Paso 1. **Recolección de Preferencias del Usuario** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **Generación de Código para Recuperar Datos** ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ``` 3. **Ejecución del Código Generado** ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ``` 4. **Generación de Itinerario** ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ``` 5. **Ajustes Basados en Retroalimentación** ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ``` ### Aprovechando la Conciencia del Entorno y el Razonamiento Basarse en el esquema de la tabla puede mejorar el proceso de generación de consultas al aprovechar la conciencia del entorno y el razonamiento. Aquí hay un ejemplo de cómo se puede hacer: 1. **Comprensión del Esquema**: El sistema comprenderá el esquema de la tabla y usará esta información para fundamentar la generación de consultas. 2. **Ajustes Basados en Retroalimentación**: El sistema ajustará las preferencias del usuario en función de la retroalimentación y razonará sobre qué campos en el esquema necesitan ser actualizados. 3. **Generación y Ejecución de Consultas**: El sistema generará y ejecutará consultas para recuperar datos actualizados de vuelos y hoteles en función de las nuevas preferencias. Aquí hay un ejemplo de código Python actualizado que incorpora estos conceptos: ```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
``` #### Explicación - Reserva Basada en Retroalimentación 1. **Conciencia del Esquema**: El método `schema` dictionary defines how preferences should be adjusted based on feedback. It includes fields like `favorites` and `avoid`, with corresponding adjustments.
2. **Adjusting Preferences (`adjust_based_on_feedback` method)**: This method adjusts preferences based on user feedback and the schema.
3. **Environment-Based Adjustments (`adjust_based_on_environment` personaliza los ajustes en función del esquema y la retroalimentación. 4. **Generación y Ejecución de Consultas**: El sistema genera código para recuperar datos actualizados de vuelos y hoteles en función de las preferencias ajustadas y simula la ejecución de estas consultas. 5. **Generación de Itinerario**: El sistema crea un itinerario actualizado basado en los nuevos datos de vuelos, hoteles y atracciones. Al hacer que el sistema sea consciente del entorno y razone en función del esquema, puede generar consultas más precisas y relevantes, lo que lleva a mejores recomendaciones de viaje y una experiencia más personalizada para el usuario. ### Uso de SQL como Técnica de Recuperación Aumentada por Generación (RAG) SQL (Lenguaje de Consulta Estructurado) es una herramienta poderosa para interactuar con bases de datos. Cuando se utiliza como parte de un enfoque de Recuperación Aumentada por Generación (RAG), SQL puede recuperar datos relevantes de bases de datos para informar y generar respuestas o acciones en agentes de IA. Exploremos cómo se puede usar SQL como técnica RAG en el contexto del Agente de Viajes. #### Conceptos Clave 1. **Interacción con Bases de Datos**: - SQL se utiliza para consultar bases de datos, recuperar información relevante y manipular datos. - Ejemplo: Recuperar detalles de vuelos, información de hoteles y atracciones de una base de datos de viajes. 2. **Integración con RAG**: - Las consultas SQL se generan en función de la entrada y las preferencias del usuario. - Los datos recuperados se utilizan para generar recomendaciones o acciones personalizadas. 3. **Generación Dinámica de Consultas**: - El agente de IA genera consultas SQL dinámicas en función del contexto y las necesidades del usuario. - Ejemplo: Personalizar consultas SQL para filtrar resultados en función del presupuesto, fechas e intereses. #### Aplicaciones - **Generación Automática de Código**: Generar fragmentos de código para tareas específicas. - **SQL como RAG**: Usar consultas SQL para manipular datos. - **Resolución de Problemas**: Crear y ejecutar código para resolver problemas. **Ejemplo**: Un agente de análisis de datos: 1. **Tarea**: Analizar un conjunto de datos para encontrar tendencias. 2. **Pasos**: - Cargar el conjunto de datos. - Generar consultas SQL para filtrar datos. - Ejecutar consultas y recuperar resultados. - Generar visualizaciones y conocimientos. 3. **Recursos**: Acceso al conjunto de datos, capacidades de SQL. 4. **Experiencia**: Usar resultados pasados para mejorar futuros análisis. #### Ejemplo Práctico: Uso de SQL en Agente de Viajes 1. **Recolección de Preferencias del Usuario** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **Generación de Consultas SQL** ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ``` 3. **Ejecución de Consultas SQL** ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ``` 4. **Generación de Recomendaciones** ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ``` #### Ejemplo de Consultas SQL 1. **Consulta de Vuelos** ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ``` 2. **Consulta de Hoteles** ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ``` 3. **Consulta de Atracciones** ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ``` Al aprovechar SQL como parte de la técnica de Recuperación Aumentada por Generación (RAG), agentes de IA como Agente de Viajes pueden recuperar y utilizar dinámicamente datos relevantes para proporcionar recomendaciones precisas y personalizadas. ### Conclusión La metacognición es una herramienta poderosa que puede mejorar significativamente las capacidades de los agentes de IA. Al incorporar procesos metacognitivos, puedes diseñar agentes que sean más inteligentes, adaptables y eficientes. Usa los recursos adicionales para explorar más el fascinante mundo de la metacognición en agentes de IA.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.