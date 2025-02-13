```markdown
# Metakognition in KI-Agenten

## Einführung
Willkommen zur Lektion über Metakognition in KI-Agenten! Dieses Kapitel ist für Anfänger gedacht, die neugierig darauf sind, wie KI-Agenten über ihre eigenen Denkprozesse nachdenken können. Am Ende dieser Lektion werden Sie die wichtigsten Konzepte verstehen und praktische Beispiele kennen, um Metakognition im Design von KI-Agenten anzuwenden.

## Lernziele
Nach Abschluss dieser Lektion werden Sie in der Lage sein:
1. Die Auswirkungen von Denk-Schleifen in Agentendefinitionen zu verstehen.
2. Planungs- und Bewertungstechniken zu nutzen, um selbstkorrigierende Agenten zu unterstützen.
3. Eigene Agenten zu erstellen, die in der Lage sind, Code zu manipulieren, um Aufgaben zu erledigen.

## Einführung in Metakognition
Metakognition bezieht sich auf die höhergeordneten kognitiven Prozesse, die das Nachdenken über das eigene Denken beinhalten. Für KI-Agenten bedeutet dies, dass sie in der Lage sind, ihre Handlungen basierend auf Selbstbewusstsein und vergangenen Erfahrungen zu bewerten und anzupassen.

### Was ist Metakognition?
Metakognition, oder "Denken über das Denken", ist ein höherer kognitiver Prozess, der Selbstbewusstsein und Selbstregulation der eigenen kognitiven Prozesse umfasst. Im Bereich der KI befähigt Metakognition Agenten, ihre Strategien und Handlungen zu bewerten und anzupassen, was zu verbesserten Problemlösungs- und Entscheidungsfähigkeiten führt. Durch das Verständnis von Metakognition können Sie KI-Agenten entwerfen, die nicht nur intelligenter, sondern auch anpassungsfähiger und effizienter sind.

### Bedeutung der Metakognition in KI-Agenten
Metakognition spielt aus mehreren Gründen eine entscheidende Rolle im Design von KI-Agenten:

![Bedeutung der Metakognition](../../../translated_images/importance-of-metacognition.e351a5983bb745d60a1a60185391a39a6751d033c8c1948ceb6ad04eff7dbeac.de.png)
- **Selbstreflexion**: Agenten können ihre eigene Leistung bewerten und Verbesserungsbereiche identifizieren.
- **Anpassungsfähigkeit**: Agenten können ihre Strategien basierend auf vergangenen Erfahrungen und sich ändernden Umgebungen anpassen.
- **Fehlerkorrektur**: Agenten können Fehler autonom erkennen und korrigieren, was zu genaueren Ergebnissen führt.
- **Ressourcenmanagement**: Agenten können die Nutzung von Ressourcen wie Zeit und Rechenleistung durch Planung und Bewertung ihrer Handlungen optimieren.

## Komponenten eines KI-Agenten
Bevor wir uns mit metakognitiven Prozessen befassen, ist es wichtig, die grundlegenden Komponenten eines KI-Agenten zu verstehen. Ein KI-Agent besteht typischerweise aus:
- **Persona**: Die Persönlichkeit und Eigenschaften des Agenten, die definieren, wie er mit Benutzern interagiert.
- **Werkzeuge**: Die Fähigkeiten und Funktionen, die der Agent ausführen kann.
- **Fähigkeiten**: Das Wissen und die Expertise, die der Agent besitzt.

Diese Komponenten arbeiten zusammen, um eine "Expertise-Einheit" zu schaffen, die spezifische Aufgaben ausführen kann.

**Beispiel**: Betrachten Sie einen Reiseagenten, der nicht nur Ihren Urlaub plant, sondern auch seine Route basierend auf Echtzeitdaten und Erfahrungen aus früheren Kundenreisen anpasst.

### Beispiel: Metakognition in einem Reiseagenten-Service
Stellen Sie sich vor, Sie entwerfen einen Reiseagenten-Service, der von KI betrieben wird. Dieser Agent, "Reiseagent", hilft Benutzern bei der Urlaubsplanung. Um Metakognition zu integrieren, muss der Reiseagent seine Handlungen basierend auf Selbstbewusstsein und vergangenen Erfahrungen bewerten und anpassen.

#### Aktuelle Aufgabe
Die aktuelle Aufgabe besteht darin, einem Benutzer bei der Planung einer Reise nach Paris zu helfen.

#### Schritte zur Erledigung der Aufgabe
1. **Benutzerpräferenzen sammeln**: Den Benutzer nach seinen Reisedaten, Budget, Interessen (z. B. Museen, Küche, Shopping) und spezifischen Anforderungen fragen.
2. **Informationen abrufen**: Nach Flugoptionen, Unterkünften, Sehenswürdigkeiten und Restaurants suchen, die den Präferenzen des Benutzers entsprechen.
3. **Empfehlungen generieren**: Einen personalisierten Reiseplan mit Flugdaten, Hotelreservierungen und vorgeschlagenen Aktivitäten erstellen.
4. **Anpassung basierend auf Feedback**: Den Benutzer um Feedback zu den Empfehlungen bitten und notwendige Anpassungen vornehmen.

#### Erforderliche Ressourcen
- Zugriff auf Flug- und Hotelbuchungsdatenbanken.
- Informationen zu Pariser Sehenswürdigkeiten und Restaurants.
- Benutzerfeedback-Daten aus früheren Interaktionen.

#### Erfahrung und Selbstreflexion
Der Reiseagent nutzt Metakognition, um seine Leistung zu bewerten und aus vergangenen Erfahrungen zu lernen. Zum Beispiel:
1. **Analyse des Benutzerfeedbacks**: Der Reiseagent überprüft das Feedback der Benutzer, um festzustellen, welche Empfehlungen gut ankamen und welche nicht. Er passt seine zukünftigen Vorschläge entsprechend an.
2. **Anpassungsfähigkeit**: Wenn ein Benutzer zuvor eine Abneigung gegen überfüllte Orte geäußert hat, vermeidet der Reiseagent, beliebte Touristenattraktionen zu Stoßzeiten zu empfehlen.
3. **Fehlerkorrektur**: Wenn der Reiseagent in der Vergangenheit einen Fehler bei einer Buchung gemacht hat, wie z. B. das Vorschlagen eines ausgebuchten Hotels, lernt er, die Verfügbarkeit vor der Empfehlung gründlicher zu überprüfen.

#### Praktisches Entwicklerbeispiel
Hier ist ein vereinfachtes Beispiel, wie der Code des Reiseagenten aussehen könnte, wenn Metakognition integriert wird:

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

#### Warum Metakognition wichtig ist
- **Selbstreflexion**: Agenten können ihre Leistung analysieren und Verbesserungsbereiche identifizieren.
- **Anpassungsfähigkeit**: Agenten können Strategien basierend auf Feedback und sich ändernden Bedingungen anpassen.
- **Fehlerkorrektur**: Agenten können Fehler autonom erkennen und korrigieren.
- **Ressourcenmanagement**: Agenten können Ressourcen wie Zeit und Rechenleistung optimieren.

Durch die Integration von Metakognition kann der Reiseagent personalisierte und genauere Reiseempfehlungen bieten, was das Benutzererlebnis insgesamt verbessert.

---

## 2. Planung in Agenten
Planung ist eine kritische Komponente des Verhaltens von KI-Agenten. Sie beinhaltet die Festlegung der Schritte, die erforderlich sind, um ein Ziel zu erreichen, unter Berücksichtigung des aktuellen Zustands, der Ressourcen und möglicher Hindernisse.

### Elemente der Planung
- **Aktuelle Aufgabe**: Die Aufgabe klar definieren.
- **Schritte zur Erledigung der Aufgabe**: Die Aufgabe in überschaubare Schritte unterteilen.
- **Erforderliche Ressourcen**: Notwendige Ressourcen identifizieren.
- **Erfahrung**: Vergangene Erfahrungen nutzen, um die Planung zu informieren.

**Beispiel**: Hier sind die Schritte, die der Reiseagent unternehmen muss, um einem Benutzer effektiv bei der Reiseplanung zu helfen:

### Schritte für den Reiseagenten
1. **Benutzerpräferenzen sammeln**
   - Den Benutzer nach Details zu Reisedaten, Budget, Interessen und spezifischen Anforderungen fragen.
   - Beispiele: "Wann planen Sie zu reisen?" "Was ist Ihre Budgetspanne?" "Welche Aktivitäten genießen Sie im Urlaub?"
2. **Informationen abrufen**
   - Nach relevanten Reiseoptionen basierend auf den Präferenzen des Benutzers suchen.
   - **Flüge**: Nach verfügbaren Flügen innerhalb des Budgets und der bevorzugten Reisedaten suchen.
   - **Unterkünfte**: Hotels oder Mietobjekte finden, die den Präferenzen des Benutzers hinsichtlich Lage, Preis und Ausstattung entsprechen.
   - **Sehenswürdigkeiten und Restaurants**: Beliebte Sehenswürdigkeiten, Aktivitäten und Speiseoptionen identifizieren, die den Interessen des Benutzers entsprechen.
3. **Empfehlungen generieren**
   - Die abgerufenen Informationen in einen personalisierten Reiseplan zusammenstellen.
   - Details wie Flugoptionen, Hotelreservierungen und vorgeschlagene Aktivitäten bereitstellen, wobei die Empfehlungen auf die Präferenzen des Benutzers zugeschnitten werden.
4. **Reiseplan dem Benutzer präsentieren**
   - Den vorgeschlagenen Reiseplan dem Benutzer zur Überprüfung teilen.
   - Beispiel: "Hier ist ein vorgeschlagener Reiseplan für Ihre Reise nach Paris. Er enthält Flugdaten, Hotelbuchungen und eine Liste empfohlener Aktivitäten und Restaurants. Teilen Sie mir Ihre Meinung mit!"
5. **Feedback sammeln**
   - Den Benutzer um Feedback zum vorgeschlagenen Reiseplan bitten.
   - Beispiele: "Gefällt Ihnen die Flugauswahl?" "Ist das Hotel für Ihre Bedürfnisse geeignet?" "Gibt es Aktivitäten, die Sie hinzufügen oder entfernen möchten?"
6. **Anpassung basierend auf Feedback**
   - Den Reiseplan basierend auf dem Feedback des Benutzers anpassen.
   - Notwendige Änderungen an Flug-, Unterkunfts- und Aktivitätsempfehlungen vornehmen, um die Präferenzen des Benutzers besser zu erfüllen.
7. **Endgültige Bestätigung**
   - Den aktualisierten Reiseplan dem Benutzer zur endgültigen Bestätigung präsentieren.
   - Beispiel: "Ich habe die Anpassungen basierend auf Ihrem Feedback vorgenommen. Hier ist der aktualisierte Reiseplan. Ist alles in Ordnung für Sie?"
8. **Buchungen vornehmen und bestätigen**
   - Sobald der Benutzer den Reiseplan genehmigt, Flüge, Unterkünfte und vorgeplante Aktivitäten buchen.
   - Bestätigungsdetails an den Benutzer senden.
9. **Laufender Support**
   - Verfügbar bleiben, um dem Benutzer bei Änderungen oder zusätzlichen Anforderungen vor und während der Reise zu helfen.
   - Beispiel: "Wenn Sie während Ihrer Reise weitere Unterstützung benötigen, können Sie sich jederzeit an mich wenden!"

### Beispielinteraktion
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
Reisebüro formuliert neue Suchanfragen basierend auf Nutzerfeedback.  
- Beispiel: ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```  
- **Tool**: Das Reisebüro verwendet Algorithmen, um neue Suchergebnisse zu bewerten und zu filtern, wobei der Schwerpunkt auf der Relevanz basierend auf dem Nutzerfeedback liegt.  
- Beispiel: ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```  
- **Bewertung**: Das Reisebüro bewertet kontinuierlich die Relevanz und Genauigkeit seiner Empfehlungen, indem es Nutzerfeedback analysiert und notwendige Anpassungen vornimmt.  
- Beispiel: ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```  

#### Praktisches Beispiel  
Hier ist ein vereinfachtes Python-Code-Beispiel, das den Corrective-RAG-Ansatz im Reisebüro integriert:  
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

### Präventives Kontextladen  
Präventives Kontextladen bedeutet, relevante Kontexte oder Hintergrundinformationen in das Modell zu laden, bevor eine Anfrage verarbeitet wird. Dadurch hat das Modell von Anfang an Zugriff auf diese Informationen, was ihm hilft, fundiertere Antworten zu generieren, ohne während des Prozesses zusätzliche Daten abrufen zu müssen.  

Hier ist ein vereinfachtes Beispiel, wie ein präventives Kontextladen für eine Reisebüroanwendung in Python aussehen könnte:  
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

#### Erklärung  
1. **Initialisierung (`__init__` method)**: The `TravelAgent` class pre-loads a dictionary containing information about popular destinations such as Paris, Tokyo, New York, and Sydney. This dictionary includes details like the country, currency, language, and major attractions for each destination.

2. **Retrieving Information (`get_destination_info` method)**: When a user queries about a specific destination, the `get_destination_info` Methode)**: Diese Methode ruft die relevanten Informationen aus dem vorab geladenen Kontext-Wörterbuch ab. Durch das Vorladen des Kontexts kann die Reisebüroanwendung schnell auf Nutzeranfragen reagieren, ohne diese Informationen in Echtzeit aus einer externen Quelle abrufen zu müssen. Dies macht die Anwendung effizienter und reaktionsschneller.  

### Einen Plan mit einem Ziel vor dem Iterieren starten  
Einen Plan mit einem Ziel zu starten bedeutet, mit einem klaren Ziel oder angestrebten Ergebnis zu beginnen. Durch die Definition dieses Ziels im Voraus kann das Modell es als Leitprinzip während des gesamten iterativen Prozesses nutzen. Dies hilft sicherzustellen, dass jede Iteration dem gewünschten Ergebnis näherkommt, wodurch der Prozess effizienter und zielgerichteter wird.  

Hier ist ein Beispiel, wie Sie einen Reiseplan mit einem Ziel vor dem Iterieren für ein Reisebüro in Python starten könnten:  

### Szenario  
Ein Reisebüro möchte einen individuellen Urlaub für einen Kunden planen. Das Ziel ist es, eine Reiseplanung zu erstellen, die die Zufriedenheit des Kunden basierend auf seinen Vorlieben und seinem Budget maximiert.  

### Schritte  
1. Definieren Sie die Vorlieben und das Budget des Kunden.  
2. Starten Sie den anfänglichen Plan basierend auf diesen Vorlieben.  
3. Iterieren Sie, um den Plan zu verfeinern und die Zufriedenheit des Kunden zu optimieren.  

#### Python-Code  
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

#### Code-Erklärung  
1. **Initialisierung (`__init__` method)**: The `TravelAgent` class is initialized with a list of potential destinations, each having attributes like name, cost, and activity type.

2. **Bootstrapping the Plan (`bootstrap_plan` method)**: This method creates an initial travel plan based on the client's preferences and budget. It iterates through the list of destinations and adds them to the plan if they match the client's preferences and fit within the budget.

3. **Matching Preferences (`match_preferences` method)**: This method checks if a destination matches the client's preferences.

4. **Iterating the Plan (`iterate_plan` method)**: This method refines the initial plan by trying to replace each destination in the plan with a better match, considering the client's preferences and budget constraints.

5. **Calculating Cost (`calculate_cost` Methode)**: Diese Methode berechnet die Gesamtkosten des aktuellen Plans, einschließlich eines potenziellen neuen Ziels.  

#### Beispielverwendung  
- **Anfänglicher Plan**: Das Reisebüro erstellt einen anfänglichen Plan basierend auf den Vorlieben des Kunden für Sehenswürdigkeiten und einem Budget von $2000.  
- **Verfeinerter Plan**: Das Reisebüro iteriert den Plan und optimiert ihn basierend auf den Vorlieben und dem Budget des Kunden.  

Durch das Starten des Plans mit einem klaren Ziel (z. B. Maximierung der Kundenzufriedenheit) und das Iterieren zur Verfeinerung des Plans kann das Reisebüro eine individuelle und optimierte Reiseplanung für den Kunden erstellen. Dieser Ansatz stellt sicher, dass der Reiseplan von Anfang an den Vorlieben und dem Budget des Kunden entspricht und sich mit jeder Iteration verbessert.  

### Nutzung von LLM für Neusortierung und Bewertung  
Große Sprachmodelle (LLMs) können zur Neusortierung und Bewertung verwendet werden, indem sie die Relevanz und Qualität abgerufener Dokumente oder generierter Antworten bewerten. So funktioniert es:  

**Abruf:** Der erste Abrufschritt ruft eine Reihe von Kandidatendokumenten oder -antworten basierend auf der Anfrage ab.  
**Neusortierung:** Das LLM bewertet diese Kandidaten und sortiert sie basierend auf ihrer Relevanz und Qualität neu. Dieser Schritt stellt sicher, dass die relevantesten und qualitativ hochwertigsten Informationen zuerst präsentiert werden.  
**Bewertung:** Das LLM weist jedem Kandidaten Bewertungen zu, die ihre Relevanz und Qualität widerspiegeln. Dies hilft dabei, die beste Antwort oder das beste Dokument für den Nutzer auszuwählen.  

Durch die Nutzung von LLMs zur Neusortierung und Bewertung kann das System genauere und kontextuell relevante Informationen bereitstellen, was die allgemeine Nutzererfahrung verbessert.  

Hier ist ein Beispiel, wie ein Reisebüro ein großes Sprachmodell (LLM) zur Neusortierung und Bewertung von Reisezielen basierend auf den Vorlieben des Nutzers in Python verwenden könnte:  

#### Szenario - Reisen basierend auf Vorlieben  
Ein Reisebüro möchte dem Kunden die besten Reiseziele basierend auf seinen Vorlieben empfehlen. Das LLM hilft dabei, die Ziele neu zu sortieren und zu bewerten, um sicherzustellen, dass die relevantesten Optionen präsentiert werden.  

#### Schritte:  
1. Sammeln Sie die Vorlieben des Nutzers.  
2. Rufen Sie eine Liste potenzieller Reiseziele ab.  
3. Verwenden Sie das LLM, um die Reiseziele basierend auf den Nutzerpräferenzen neu zu sortieren und zu bewerten.  

Hier ist, wie Sie das vorherige Beispiel aktualisieren können, um Azure OpenAI Services zu nutzen:  

#### Anforderungen  
1. Sie benötigen ein Azure-Abonnement.  
2. Erstellen Sie eine Azure OpenAI-Ressource und erhalten Sie Ihren API-Schlüssel.  

#### Beispiel-Python-Code  
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

#### Code-Erklärung - Präferenzbucher  
1. **Initialisierung**: Ersetzen Sie `TravelAgent` class is initialized with a list of potential travel destinations, each having attributes like name and description.

2. **Getting Recommendations (`get_recommendations` method)**: This method generates a prompt for the Azure OpenAI service based on the user's preferences and makes an HTTP POST request to the Azure OpenAI API to get re-ranked and scored destinations.

3. **Generating Prompt (`generate_prompt` method)**: This method constructs a prompt for the Azure OpenAI, including the user's preferences and the list of destinations. The prompt guides the model to re-rank and score the destinations based on the provided preferences.

4. **API Call**: The `requests` library is used to make an HTTP POST request to the Azure OpenAI API endpoint. The response contains the re-ranked and scored destinations.

5. **Example Usage**: The travel agent collects user preferences (e.g., interest in sightseeing and diverse culture) and uses the Azure OpenAI service to get re-ranked and scored recommendations for travel destinations.

Make sure to replace `your_azure_openai_api_key` with your actual Azure OpenAI API key and `https://your-endpoint.com/...` mit der tatsächlichen Endpunkt-URL Ihrer Azure OpenAI-Bereitstellung.  

Durch die Nutzung des LLM zur Neusortierung und Bewertung kann das Reisebüro personalisiertere und relevantere Reiseempfehlungen für Kunden bereitstellen und so deren Gesamterfahrung verbessern.  
```
```markdown
die besten Museen in Paris?"). - **Navigationsabsicht**: Der Benutzer möchte zu einer bestimmten Website oder Seite navigieren (z. B. "Offizielle Website des Louvre-Museums"). - **Transaktionsabsicht**: Der Benutzer beabsichtigt, eine Transaktion durchzuführen, wie z. B. einen Flug zu buchen oder einen Kauf zu tätigen (z. B. "Buche einen Flug nach Paris"). 2. **Kontextbewusstsein**: - Die Analyse des Kontexts der Benutzeranfrage hilft dabei, die Absicht genau zu identifizieren. Dies beinhaltet die Berücksichtigung vorheriger Interaktionen, Benutzerpräferenzen und spezifischer Details der aktuellen Anfrage. 3. **Natural Language Processing (NLP)**: - NLP-Techniken werden eingesetzt, um die von Benutzern bereitgestellten Anfragen in natürlicher Sprache zu verstehen und zu interpretieren. Dazu gehören Aufgaben wie Entitätserkennung, Sentimentanalyse und Abfrageanalyse. 4. **Personalisierung**: - Die Personalisierung der Suchergebnisse basierend auf der Historie, den Präferenzen und dem Feedback des Benutzers verbessert die Relevanz der abgerufenen Informationen. #### Praktisches Beispiel: Suche mit Absicht im Reisebüro Lassen Sie uns das Reisebüro als Beispiel nehmen, um zu sehen, wie die Suche mit Absicht implementiert werden kann. 1. **Sammeln von Benutzerpräferenzen** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **Verstehen der Benutzerabsicht** ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ``` 3. **Kontextbewusstsein** ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ``` 4. **Suche und Personalisierung der Ergebnisse** ```python
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
   ``` 5. **Beispielnutzung** ```python
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
   ``` --- ## 4. Code als Werkzeug generieren Code-generierende Agenten verwenden KI-Modelle, um Code zu schreiben und auszuführen, komplexe Probleme zu lösen und Aufgaben zu automatisieren. ### Code-generierende Agenten Code-generierende Agenten verwenden generative KI-Modelle, um Code zu schreiben und auszuführen. Diese Agenten können komplexe Probleme lösen, Aufgaben automatisieren und wertvolle Einblicke liefern, indem sie Code in verschiedenen Programmiersprachen generieren und ausführen. #### Praktische Anwendungen 1. **Automatische Codegenerierung**: Generieren von Codeschnipseln für spezifische Aufgaben wie Datenanalyse, Web-Scraping oder maschinelles Lernen. 2. **SQL als RAG**: Verwenden von SQL-Abfragen, um Daten aus Datenbanken abzurufen und zu manipulieren. 3. **Problemlösung**: Erstellen und Ausführen von Code zur Lösung spezifischer Probleme, wie z. B. Optimierung von Algorithmen oder Datenanalyse. #### Beispiel: Code-generierender Agent für Datenanalyse Stellen Sie sich vor, Sie entwerfen einen Code-generierenden Agenten. So könnte er funktionieren: 1. **Aufgabe**: Analysieren eines Datensatzes, um Trends und Muster zu identifizieren. 2. **Schritte**: - Laden des Datensatzes in ein Datenanalysetool. - Generieren von SQL-Abfragen, um die Daten zu filtern und zu aggregieren. - Ausführen der Abfragen und Abrufen der Ergebnisse. - Verwenden der Ergebnisse zur Erstellung von Visualisierungen und Erkenntnissen. 3. **Erforderliche Ressourcen**: Zugriff auf den Datensatz, Datenanalysetools und SQL-Fähigkeiten. 4. **Erfahrung**: Verwenden vergangener Analyseergebnisse, um die Genauigkeit und Relevanz zukünftiger Analysen zu verbessern. ### Beispiel: Code-generierender Agent für Reisebüro In diesem Beispiel entwerfen wir einen Code-generierenden Agenten, Reisebüro, um Benutzern bei der Reiseplanung zu helfen, indem er Code generiert und ausführt. Dieser Agent kann Aufgaben wie das Abrufen von Reiseoptionen, Filtern von Ergebnissen und Zusammenstellen eines Reiseplans mithilfe generativer KI übernehmen. #### Überblick über den Code-generierenden Agenten 1. **Sammeln von Benutzerpräferenzen**: Sammelt Benutzereingaben wie Ziel, Reisedaten, Budget und Interessen. 2. **Generieren von Code zum Abrufen von Daten**: Generiert Codeschnipsel, um Daten zu Flügen, Hotels und Attraktionen abzurufen. 3. **Ausführen des generierten Codes**: Führt den generierten Code aus, um Echtzeitinformationen abzurufen. 4. **Erstellen eines Reiseplans**: Stellt die abgerufenen Daten zu einem personalisierten Reiseplan zusammen. 5. **Anpassen basierend auf Feedback**: Erhält Benutzerfeedback und generiert bei Bedarf Code neu, um die Ergebnisse zu verfeinern. #### Schritt-für-Schritt-Implementierung 1. **Sammeln von Benutzerpräferenzen** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **Generieren von Code zum Abrufen von Daten** ```python
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
   ``` 3. **Ausführen des generierten Codes** ```python
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
   ``` 4. **Erstellen eines Reiseplans** ```python
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
   ``` 5. **Anpassen basierend auf Feedback** ```python
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
   ``` ### Nutzung von Umweltbewusstsein und logischem Denken Basierend auf dem Schema der Tabelle kann der Prozess der Abfragegenerierung durch die Nutzung von Umweltbewusstsein und logischem Denken verbessert werden. Hier ist ein Beispiel, wie dies erreicht werden kann: 1. **Verstehen des Schemas**: Das System versteht das Schema der Tabelle und nutzt diese Informationen, um die Abfragegenerierung zu begründen. 2. **Anpassen basierend auf Feedback**: Das System passt Benutzerpräferenzen basierend auf Feedback an und überlegt, welche Felder im Schema aktualisiert werden müssen. 3. **Generieren und Ausführen von Abfragen**: Das System generiert und führt Abfragen aus, um aktualisierte Flug- und Hoteldaten basierend auf den neuen Präferenzen abzurufen. Hier ist ein aktualisiertes Python-Codebeispiel, das diese Konzepte integriert: ```python
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
``` #### Erklärung - Buchung basierend auf Feedback 1. **Schema-Bewusstsein**: Die Methode `schema` dictionary defines how preferences should be adjusted based on feedback. It includes fields like `favorites` and `avoid`, with corresponding adjustments.
2. **Adjusting Preferences (`adjust_based_on_feedback` method)**: This method adjusts preferences based on user feedback and the schema.
3. **Environment-Based Adjustments (`adjust_based_on_environment`): Diese Methode passt die Anpassungen basierend auf dem Schema und dem Feedback an. 4. **Generieren und Ausführen von Abfragen**: Das System generiert Code, um aktualisierte Flug- und Hoteldaten basierend auf den angepassten Präferenzen abzurufen, und simuliert die Ausführung dieser Abfragen. 5. **Erstellen eines Reiseplans**: Das System erstellt einen aktualisierten Reiseplan basierend auf den neuen Flug-, Hotel- und Attraktionsdaten. Indem das System umweltbewusst wird und auf Basis des Schemas logisch denkt, kann es genauere und relevantere Abfragen generieren, was zu besseren Reiseempfehlungen und einem personalisierteren Benutzererlebnis führt. ### Verwendung von SQL als Retrieval-Augmented Generation (RAG)-Technik SQL (Structured Query Language) ist ein leistungsstarkes Werkzeug für die Interaktion mit Datenbanken. Wenn SQL als Teil eines Retrieval-Augmented Generation (RAG)-Ansatzes verwendet wird, kann es relevante Daten aus Datenbanken abrufen, um Antworten oder Aktionen in KI-Agenten zu informieren und zu generieren. Lassen Sie uns untersuchen, wie SQL als RAG-Technik im Kontext des Reisebüros verwendet werden kann. #### Schlüsselkonzepte 1. **Datenbankinteraktion**: - SQL wird verwendet, um Datenbanken abzufragen, relevante Informationen abzurufen und Daten zu manipulieren. - Beispiel: Abrufen von Flugdaten, Hotelinformationen und Attraktionen aus einer Reisedatenbank. 2. **Integration mit RAG**: - SQL-Abfragen werden basierend auf Benutzereingaben und -präferenzen generiert. - Die abgerufenen Daten werden dann verwendet, um personalisierte Empfehlungen oder Aktionen zu generieren. 3. **Dynamische Abfragegenerierung**: - Der KI-Agent generiert dynamische SQL-Abfragen basierend auf dem Kontext und den Bedürfnissen des Benutzers. - Beispiel: Anpassen von SQL-Abfragen, um Ergebnisse basierend auf Budget, Daten und Interessen zu filtern. #### Anwendungen - **Automatische Codegenerierung**: Generieren von Codeschnipseln für spezifische Aufgaben. - **SQL als RAG**: Verwenden von SQL-Abfragen zur Datenmanipulation. - **Problemlösung**: Erstellen und Ausführen von Code zur Lösung von Problemen. **Beispiel**: Ein Datenanalyse-Agent: 1. **Aufgabe**: Analysieren eines Datensatzes, um Trends zu finden. 2. **Schritte**: - Laden des Datensatzes. - Generieren von SQL-Abfragen zur Filterung von Daten. - Ausführen von Abfragen und Abrufen von Ergebnissen. - Generieren von Visualisierungen und Erkenntnissen. 3. **Ressourcen**: Zugriff auf Datensätze, SQL-Fähigkeiten. 4. **Erfahrung**: Verwenden vergangener Ergebnisse, um zukünftige Analysen zu verbessern. #### Praktisches Beispiel: Verwendung von SQL im Reisebüro 1. **Sammeln von Benutzerpräferenzen** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **Generieren von SQL-Abfragen** ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ``` 3. **Ausführen von SQL-Abfragen** ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ``` 4. **Generieren von Empfehlungen** ```python
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
   ``` #### Beispiel-SQL-Abfragen 1. **Flugabfrage** ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ``` 2. **Hotelabfrage** ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ``` 3. **Attraktionsabfrage** ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ``` Durch die Nutzung von SQL als Teil der Retrieval-Augmented Generation (RAG)-Technik können KI-Agenten wie das Reisebüro dynamisch relevante Daten abrufen und nutzen, um genaue und personalisierte Empfehlungen bereitzustellen. ### Fazit Metakognition ist ein leistungsstarkes Werkzeug, das die Fähigkeiten von KI-Agenten erheblich verbessern kann. Durch die Integration metakognitiver Prozesse können Sie Agenten entwerfen, die intelligenter, anpassungsfähiger und effizienter sind. Verwenden Sie die zusätzlichen Ressourcen, um die faszinierende Welt der Metakognition in KI-Agenten weiter zu erkunden.
```

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.