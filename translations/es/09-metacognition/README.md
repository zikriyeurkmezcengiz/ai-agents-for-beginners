```markdown
# Metacognición en Agentes de IA

## Introducción

¡Bienvenido a la lección sobre metacognición en agentes de IA! Este capítulo está diseñado para principiantes curiosos sobre cómo los agentes de IA pueden reflexionar sobre sus propios procesos de pensamiento. Al final de esta lección, comprenderás conceptos clave y estarás equipado con ejemplos prácticos para aplicar la metacognición en el diseño de agentes de IA.

## Objetivos de Aprendizaje

Después de completar esta lección, serás capaz de:

1. Comprender las implicaciones de los bucles de razonamiento en las definiciones de agentes.
2. Utilizar técnicas de planificación y evaluación para ayudar a los agentes a autocorregirse.
3. Crear tus propios agentes capaces de manipular código para realizar tareas.

## Introducción a la Metacognición

La metacognición se refiere a los procesos cognitivos de orden superior que implican pensar sobre el propio pensamiento. Para los agentes de IA, esto significa ser capaces de evaluar y ajustar sus acciones basándose en la autoconciencia y experiencias pasadas.

### ¿Qué es la Metacognición?

La metacognición, o "pensar sobre el pensamiento", es un proceso cognitivo de orden superior que implica autoconciencia y autorregulación de los propios procesos cognitivos. En el ámbito de la IA, la metacognición capacita a los agentes para evaluar y adaptar sus estrategias y acciones, lo que lleva a una mejora en la resolución de problemas y en la toma de decisiones. Al comprender la metacognición, puedes diseñar agentes de IA que no solo sean más inteligentes, sino también más adaptables y eficientes.

### Importancia de la Metacognición en los Agentes de IA

La metacognición desempeña un papel crucial en el diseño de agentes de IA por varias razones:

![Importancia de la Metacognición](../../../translated_images/importance-of-metacognition.e351a5983bb745d60a1a60185391a39a6751d033c8c1948ceb6ad04eff7dbeac.es.png)

- **Autorreflexión**: Los agentes pueden evaluar su propio desempeño e identificar áreas de mejora.
- **Adaptabilidad**: Los agentes pueden modificar sus estrategias basándose en experiencias pasadas y entornos cambiantes.
- **Corrección de Errores**: Los agentes pueden detectar y corregir errores de manera autónoma, lo que conduce a resultados más precisos.
- **Gestión de Recursos**: Los agentes pueden optimizar el uso de recursos, como tiempo y poder computacional, planificando y evaluando sus acciones.

## Componentes de un Agente de IA

Antes de profundizar en los procesos metacognitivos, es esencial entender los componentes básicos de un agente de IA. Un agente de IA típicamente consta de:

- **Persona**: La personalidad y características del agente, que definen cómo interactúa con los usuarios.
- **Herramientas**: Las capacidades y funciones que el agente puede realizar.
- **Habilidades**: El conocimiento y la experiencia que posee el agente.

Estos componentes trabajan juntos para crear una "unidad de experiencia" que puede realizar tareas específicas.

**Ejemplo**: Considera un agente de viajes, que no solo planea tus vacaciones, sino que también ajusta su ruta basándose en datos en tiempo real y experiencias previas de clientes.

### Ejemplo: Metacognición en un Servicio de Agente de Viajes

Imagina que estás diseñando un servicio de agente de viajes impulsado por IA. Este agente, llamado "Agente de Viajes", ayuda a los usuarios a planificar sus vacaciones. Para incorporar metacognición, el Agente de Viajes necesita evaluar y ajustar sus acciones basándose en la autoconciencia y experiencias pasadas. Así es como la metacognición podría desempeñar un papel:

#### Tarea Actual

La tarea actual es ayudar a un usuario a planificar un viaje a París.

#### Pasos para Completar la Tarea

1. **Recopilar Preferencias del Usuario**: Preguntar al usuario sobre sus fechas de viaje, presupuesto, intereses (por ejemplo, museos, gastronomía, compras) y cualquier requisito específico.
2. **Recuperar Información**: Buscar opciones de vuelos, alojamientos, atracciones y restaurantes que coincidan con las preferencias del usuario.
3. **Generar Recomendaciones**: Proporcionar un itinerario personalizado con detalles de vuelos, reservas de hotel y actividades sugeridas.
4. **Ajustar Basándose en Comentarios**: Solicitar comentarios del usuario sobre las recomendaciones y realizar los ajustes necesarios.

#### Recursos Necesarios

- Acceso a bases de datos de reservas de vuelos y hoteles.
- Información sobre atracciones y restaurantes en París.
- Datos de retroalimentación de usuarios de interacciones previas.

#### Experiencia y Autorreflexión

El Agente de Viajes utiliza la metacognición para evaluar su desempeño y aprender de experiencias pasadas. Por ejemplo:

1. **Análisis de Retroalimentación del Usuario**: El Agente de Viajes revisa los comentarios de los usuarios para determinar qué recomendaciones fueron bien recibidas y cuáles no. Ajusta sus futuras sugerencias en consecuencia.
2. **Adaptabilidad**: Si un usuario ha mencionado previamente que no le gustan los lugares concurridos, el Agente de Viajes evitará recomendar puntos turísticos populares en horas pico en el futuro.
3. **Corrección de Errores**: Si el Agente de Viajes cometió un error en una reserva anterior, como sugerir un hotel que estaba completamente reservado, aprende a verificar la disponibilidad con mayor rigor antes de hacer recomendaciones.

#### Ejemplo Práctico para Desarrolladores

Aquí tienes un ejemplo simplificado de cómo podría lucir el código del Agente de Viajes al incorporar metacognición:

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

- **Autorreflexión**: Los agentes pueden analizar su desempeño e identificar áreas de mejora.
- **Adaptabilidad**: Los agentes pueden modificar estrategias basándose en comentarios y condiciones cambiantes.
- **Corrección de Errores**: Los agentes pueden detectar y corregir errores de manera autónoma.
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

**Ejemplo**: Aquí están los pasos que el Agente de Viajes necesita seguir para ayudar a un usuario a planificar su viaje de manera efectiva:

### Pasos para el Agente de Viajes

1. **Recopilar Preferencias del Usuario**
   - Preguntar al usuario sobre detalles como fechas de viaje, presupuesto, intereses y requisitos específicos.
   - Ejemplos: "¿Cuándo planeas viajar?" "¿Cuál es tu rango de presupuesto?" "¿Qué actividades disfrutas en vacaciones?"

2. **Recuperar Información**
   - Buscar opciones de viaje relevantes basándose en las preferencias del usuario.
   - **Vuelos**: Buscar vuelos disponibles dentro del presupuesto y las fechas preferidas del usuario.
   - **Alojamientos**: Encontrar hoteles o propiedades de alquiler que coincidan con las preferencias del usuario en cuanto a ubicación, precio y comodidades.
   - **Atracciones y Restaurantes**: Identificar atracciones populares, actividades y opciones gastronómicas que se alineen con los intereses del usuario.

3. **Generar Recomendaciones**
   - Compilar la información recuperada en un itinerario personalizado.
   - Proporcionar detalles como opciones de vuelos, reservas de hotel y actividades sugeridas, asegurándose de adaptar las recomendaciones a las preferencias del usuario.

4. **Presentar el Itinerario al Usuario**
   - Compartir el itinerario propuesto con el usuario para su revisión.
   - Ejemplo: "Aquí tienes un itinerario sugerido para tu viaje a París. Incluye detalles de vuelos, reservas de hotel y una lista de actividades y restaurantes recomendados. ¡Hazme saber tus comentarios!"

5. **Recopilar Comentarios**
   - Preguntar al usuario sobre el itinerario propuesto.
   - Ejemplos: "¿Te gustan las opciones de vuelo?" "¿El hotel es adecuado para tus necesidades?" "¿Hay actividades que te gustaría agregar o eliminar?"

6. **Ajustar Basándose en Comentarios**
   - Modificar el itinerario según los comentarios del usuario.
   - Realizar los cambios necesarios en las recomendaciones de vuelos, alojamiento y actividades para alinearse mejor con las preferencias del usuario.

7. **Confirmación Final**
   - Presentar el itinerario actualizado al usuario para confirmación final.
   - Ejemplo: "He realizado los ajustes según tus comentarios. Aquí tienes el itinerario actualizado. ¿Todo se ve bien para ti?"

8. **Reservar y Confirmar Reservas**
   - Una vez que el usuario apruebe el itinerario, proceder con la reserva de vuelos, alojamientos y actividades planificadas.
   - Enviar detalles de confirmación al usuario.

9. **Proporcionar Soporte Continuo**
   - Permanecer disponible para ayudar al usuario con cualquier cambio o solicitud adicional antes y durante su viaje.
   - Ejemplo: "Si necesitas más ayuda durante tu viaje, ¡no dudes en contactarme en cualquier momento!"

### Interacción Ejemplo

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
La carga de contexto preventiva implica cargar información relevante de contexto o antecedentes en el modelo antes de procesar una consulta. Esto significa que el modelo tiene acceso a esta información desde el inicio, lo que puede ayudarlo a generar respuestas más informadas sin necesidad de recuperar datos adicionales durante el proceso.  

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
Iniciar un plan con un objetivo implica comenzar con un resultado claro u objetivo en mente. Al definir este objetivo desde el principio, el modelo puede usarlo como un principio guía a lo largo del proceso iterativo. Esto ayuda a garantizar que cada iteración se acerque más a lograr el resultado deseado, haciendo que el proceso sea más eficiente y enfocado.  

Aquí hay un ejemplo de cómo se podría iniciar un plan de viaje con un objetivo antes de iterar para un agente de viajes en Python:  

### Escenario  
Un agente de viajes quiere planificar unas vacaciones personalizadas para un cliente. El objetivo es crear un itinerario de viaje que maximice la satisfacción del cliente en función de sus preferencias y presupuesto.  

### Pasos  
1. Definir las preferencias y el presupuesto del cliente.  
2. Iniciar el plan inicial basado en estas preferencias.  
3. Iterar para refinar el plan, optimizándolo para la satisfacción del cliente.  

#### Código en Python  
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

5. **Calculating Cost (`calculate_cost` method)**: Este método calcula el costo total del plan actual, incluyendo un posible nuevo destino.  

#### Ejemplo de uso  
- **Plan inicial**: El agente de viajes crea un plan inicial basado en las preferencias del cliente para hacer turismo y un presupuesto de $2000.  
- **Plan refinado**: El agente de viajes itera el plan, optimizándolo para las preferencias y el presupuesto del cliente.  

Al iniciar el plan con un objetivo claro (por ejemplo, maximizar la satisfacción del cliente) e iterar para refinar el plan, el agente de viajes puede crear un itinerario de viaje personalizado y optimizado para el cliente. Este enfoque asegura que el plan de viaje se alinee con las preferencias y el presupuesto del cliente desde el principio y mejore con cada iteración.  

### Aprovechar LLM para reordenar y puntuar  
Los modelos de lenguaje extenso (LLM) pueden utilizarse para reordenar y puntuar evaluando la relevancia y calidad de los documentos recuperados o las respuestas generadas. Así es como funciona:  

**Recuperación:** El paso inicial de recuperación obtiene un conjunto de documentos o respuestas candidatos basados en la consulta.  
**Reordenamiento:** El LLM evalúa estos candidatos y los reordena en función de su relevancia y calidad. Este paso asegura que la información más relevante y de alta calidad se presente primero.  
**Puntuación:** El LLM asigna puntajes a cada candidato, reflejando su relevancia y calidad. Esto ayuda a seleccionar la mejor respuesta o documento para el usuario.  

Al aprovechar los LLM para reordenar y puntuar, el sistema puede proporcionar información más precisa y contextualmente relevante, mejorando la experiencia general del usuario.  

Aquí hay un ejemplo de cómo un agente de viajes podría usar un modelo de lenguaje extenso (LLM) para reordenar y puntuar destinos de viaje basados en las preferencias del usuario en Python:  

#### Escenario - Viajes basados en preferencias  
Un agente de viajes quiere recomendar los mejores destinos de viaje a un cliente basado en sus preferencias. El LLM ayudará a reordenar y puntuar los destinos para asegurar que se presenten las opciones más relevantes.  

#### Pasos:  
1. Recopilar las preferencias del usuario.  
2. Recuperar una lista de posibles destinos de viaje.  
3. Usar el LLM para reordenar y puntuar los destinos basados en las preferencias del usuario.  

Aquí se explica cómo puedes actualizar el ejemplo anterior para usar Azure OpenAI Services:  

#### Requisitos  
1. Necesitas tener una suscripción a Azure.  
2. Crear un recurso de Azure OpenAI y obtener tu clave API.  

#### Código de ejemplo en Python  
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
1. **Inicialización**: El `TravelAgent` class is initialized with a list of potential travel destinations, each having attributes like name and description.

2. **Getting Recommendations (`get_recommendations` method)**: This method generates a prompt for the Azure OpenAI service based on the user's preferences and makes an HTTP POST request to the Azure OpenAI API to get re-ranked and scored destinations.

3. **Generating Prompt (`generate_prompt` method)**: This method constructs a prompt for the Azure OpenAI, including the user's preferences and the list of destinations. The prompt guides the model to re-rank and score the destinations based on the provided preferences.

4. **API Call**: The `requests` library is used to make an HTTP POST request to the Azure OpenAI API endpoint. The response contains the re-ranked and scored destinations.

5. **Example Usage**: The travel agent collects user preferences (e.g., interest in sightseeing and diverse culture) and uses the Azure OpenAI service to get re-ranked and scored recommendations for travel destinations.

Make sure to replace `your_azure_openai_api_key` with your actual Azure OpenAI API key and `https://your-endpoint.com/...` con la URL del endpoint real de tu implementación de Azure OpenAI.  

Al aprovechar el LLM para reordenar y puntuar, el agente de viajes puede proporcionar recomendaciones de viaje más personalizadas y relevantes a los clientes, mejorando su experiencia general.  

### RAG: Técnica de solicitud vs herramienta  
La generación aumentada por recuperación (RAG) puede ser tanto una técnica de solicitud como una herramienta en el desarrollo de agentes de IA. Comprender la distinción entre las dos puede ayudarte a aprovechar RAG de manera más efectiva en tus proyectos.  

#### RAG como técnica de solicitud  
**¿Qué es?**  
- Como técnica de solicitud, RAG implica formular consultas o solicitudes específicas para guiar la recuperación de información relevante de un corpus o base de datos grande. Esta información se utiliza luego para generar respuestas o acciones.  

**Cómo funciona:**  
1. **Formular solicitudes**: Crear solicitudes o consultas bien estructuradas basadas en la tarea en cuestión o la entrada del usuario.  
2. **Recuperar información**: Usar las solicitudes para buscar datos relevantes de una base de conocimiento o conjunto de datos preexistente.  
3. **Generar respuesta**: Combinar la información recuperada con modelos de IA generativa para producir una respuesta completa y coherente.  

**Ejemplo en agente de viajes**:  
- Entrada del usuario: "Quiero visitar museos en París."  
- Solicitud: "Encuentra los mejores museos en París."  
- Información recuperada: Detalles sobre el Museo del Louvre, Musée d'Orsay, etc.  
- Respuesta generada: "Aquí tienes algunos de los mejores museos en París: Museo del Louvre, Musée d'Orsay y Centro Pompidou."  

#### RAG como herramienta  
**¿Qué es?**  
- Como herramienta, RAG es un sistema integrado que automatiza el proceso de recuperación y generación, facilitando a los desarrolladores implementar funcionalidades complejas de IA sin tener que formular manualmente solicitudes para cada consulta.  

**Cómo funciona:**  
1. **Integración**: Incorporar RAG dentro de la arquitectura del agente de IA, permitiéndole manejar automáticamente las tareas de recuperación y generación.  
2. **Automatización**: La herramienta gestiona todo el proceso, desde recibir la entrada del usuario hasta generar la respuesta final, sin requerir solicitudes explícitas para cada paso.  
3. **Eficiencia**: Mejora el rendimiento del agente al agilizar el proceso de recuperación y generación, permitiendo respuestas más rápidas y precisas.  

**Ejemplo en agente de viajes**:  
- Entrada del usuario: "Quiero visitar museos en París."  
- Herramienta RAG: Recupera automáticamente información sobre museos y genera una respuesta.  
- Respuesta generada: "Aquí tienes algunos de los mejores museos en París: Museo del Louvre, Musée d'Orsay y Centro Pompidou."  

### Comparación  

| Aspecto                | Técnica de solicitud                                      | Herramienta                                           |  
|------------------------|----------------------------------------------------------|------------------------------------------------------|  
| **Manual vs Automático** | Formulación manual de solicitudes para cada consulta.    | Proceso automatizado de recuperación y generación.   |  
| **Control**            | Ofrece más control sobre el proceso de recuperación.      | Agiliza y automatiza la recuperación y generación.   |  
| **Flexibilidad**       | Permite solicitudes personalizadas según necesidades específicas. | Más eficiente para implementaciones a gran escala. |  
| **Complejidad**        | Requiere creación y ajuste de solicitudes.                | Más fácil de integrar en la arquitectura del agente. |  

### Ejemplos prácticos  
**Ejemplo de técnica de solicitud:**  
```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```  

**Ejemplo de herramienta:**  
```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```  

### Evaluación de relevancia  
Evaluar la relevancia es un aspecto crucial del rendimiento de los agentes de IA. Asegura que la información recuperada y generada por el agente sea adecuada, precisa y útil para el usuario. Exploremos cómo evaluar la relevancia en agentes de IA, incluyendo ejemplos prácticos y técnicas.  

#### Conceptos clave en la evaluación de relevancia  
1. **Conciencia del contexto**:  
   - El agente debe comprender el contexto de la consulta del usuario para recuperar y generar información relevante.  
   - Ejemplo: Si un usuario pregunta por "mejores restaurantes en París", el agente debe considerar las preferencias del usuario, como el tipo de cocina y presupuesto.  

2. **Precisión**:  
   - La información proporcionada por el agente debe ser correcta y actualizada.  
   - Ejemplo: Recomendar restaurantes actualmente abiertos con buenas reseñas en lugar de opciones desactualizadas o cerradas.  

3. **Intención del usuario**:  
   - El agente debe inferir la intención del usuario detrás de la consulta para proporcionar la información más relevante.  
   - Ejemplo: Si un usuario pide "hoteles económicos", el agente debe priorizar opciones asequibles.  

4. **Bucle de retroalimentación**:  
   - Recopilar y analizar continuamente comentarios de los usuarios ayuda al agente a refinar su proceso de evaluación de relevancia.  
   - Ejemplo: Incorporar calificaciones y comentarios de los usuarios sobre recomendaciones anteriores para mejorar respuestas futuras.  

#### Técnicas prácticas para evaluar relevancia  
1. **Puntuación de relevancia**:  
   - Asignar un puntaje de relevancia a cada elemento recuperado según qué tan bien coincide con la consulta y preferencias del usuario.  
   - Ejemplo: ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```  

2. **Filtrado y clasificación**:  
   - Filtrar elementos irrelevantes y clasificar los restantes según sus puntajes de relevancia.  
   - Ejemplo: ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Return top 10 relevant items
     ```  

3. **Procesamiento de lenguaje natural (NLP)**:  
   - Usar técnicas de NLP para comprender la consulta del usuario y recuperar información relevante.  
   - Ejemplo: ```python
     def process_query(query):
         # Use NLP to extract key information from the user's query
         processed_query = nlp(query)
         return processed_query
     ```  

4. **Integración de retroalimentación del usuario**:  
   - Recopilar comentarios de los usuarios sobre las recomendaciones proporcionadas y usarlos para ajustar evaluaciones de relevancia futuras.  
   - Ejemplo: ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```  

#### Ejemplo: Evaluación de relevancia en agente de viajes  
Aquí hay un ejemplo práctico de cómo el agente de viajes puede evaluar la relevancia de las recomendaciones de viaje:  
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
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Return top 10 relevant items

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

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
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```  

### Búsqueda con intención  
Buscar con intención implica comprender e interpretar el propósito o meta subyacente detrás de la consulta de un usuario para recuperar y generar la información más relevante y útil. Este enfoque va más allá de simplemente coincidir palabras clave y se centra en captar las necesidades reales y el contexto del usuario.  

#### Conceptos clave en la búsqueda con intención  
1. **Comprender la intención del usuario**:  
   - La intención del usuario puede categorizarse en tres tipos principales: informativa, de navegación y transaccional.  
   - **Intención informativa**: El usuario busca información sobre un tema (por ejemplo, "¿Cuáles son...").
```
Translation for chunk 3 skipped due to timeout.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.