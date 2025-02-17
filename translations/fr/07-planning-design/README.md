# Conception de la Planification

## Introduction

Cette leçon couvrira :

* Définir un objectif global clair et diviser une tâche complexe en tâches gérables.
* Exploiter des sorties structurées pour des réponses plus fiables et lisibles par machine.
* Appliquer une approche orientée événements pour gérer des tâches dynamiques et des entrées inattendues.

## Objectifs d'Apprentissage

Après avoir terminé cette leçon, vous comprendrez :

* Comment identifier et définir un objectif global pour un agent IA, en veillant à ce qu'il sache précisément ce qu'il doit accomplir.
* Comment décomposer une tâche complexe en sous-tâches gérables et les organiser dans une séquence logique.
* Comment équiper les agents des bons outils (par exemple, outils de recherche ou d'analyse de données), décider quand et comment les utiliser, et gérer les situations imprévues.
* Comment évaluer les résultats des sous-tâches, mesurer les performances et itérer sur les actions pour améliorer le résultat final.

## Définir l'Objectif Global et Décomposer une Tâche

![Définir les Objectifs et les Tâches](../../../translated_images/defining-goals-tasks.dcc1181bbdb194704ae0fb3363371562949e8b03fd2fadc256218aaadf84a9f4.fr.png)

La plupart des tâches du monde réel sont trop complexes pour être abordées en une seule étape. Un agent IA a besoin d'un objectif concis pour guider sa planification et ses actions. Par exemple, considérez l'objectif suivant :

    "Générer un itinéraire de voyage de 3 jours."

Bien que cet objectif soit simple à énoncer, il nécessite encore d'être précisé. Plus l'objectif est clair, mieux l'agent (et les collaborateurs humains, le cas échéant) pourra se concentrer sur l'obtention du bon résultat, comme créer un itinéraire complet avec des options de vol, des recommandations d'hôtels et des suggestions d'activités.

### Décomposition des Tâches

Les tâches volumineuses ou complexes deviennent plus faciles à gérer lorsqu'elles sont divisées en sous-tâches orientées vers des objectifs spécifiques.  
Pour l'exemple de l'itinéraire de voyage, vous pourriez décomposer l'objectif en :

* Réservation de Vols
* Réservation d'Hôtels
* Location de Voiture
* Personnalisation

Chaque sous-tâche peut ensuite être traitée par des agents ou des processus dédiés. Un agent pourrait se spécialiser dans la recherche des meilleures offres de vols, un autre dans les réservations d'hôtels, etc. Un agent coordinateur ou "en aval" peut ensuite compiler ces résultats en un itinéraire cohérent pour l'utilisateur final.

Cette approche modulaire permet également des améliorations progressives. Par exemple, vous pourriez ajouter des agents spécialisés pour les recommandations culinaires ou les suggestions d'activités locales, et affiner l'itinéraire au fil du temps.

### Sortie Structurée

Les modèles de langage avancés (LLMs) peuvent générer des sorties structurées (par exemple, JSON) qui sont plus faciles à analyser et à traiter par des agents ou services en aval. Cela est particulièrement utile dans un contexte multi-agent, où ces tâches peuvent être exécutées après réception de la sortie de planification. Consultez ce [blogpost](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/cookbook/structured-output-agent.html) pour un aperçu rapide.

Voici un exemple de snippet Python qui illustre un agent de planification simple décomposant un objectif en sous-tâches et générant un plan structuré :

### Agent de Planification avec Orchestration Multi-Agent

Dans cet exemple, un agent routeur sémantique reçoit une demande utilisateur (par exemple, "J'ai besoin d'un plan d'hôtel pour mon voyage.").

Le planificateur :

* Reçoit le Plan d'Hôtel : Le planificateur prend le message de l'utilisateur et, sur la base d'une invite système (y compris les détails des agents disponibles), génère un plan de voyage structuré.
* Liste les Agents et Leurs Outils : Le registre des agents contient une liste d'agents (par exemple, pour les vols, hôtels, locations de voitures et activités) ainsi que les fonctions ou outils qu'ils proposent.
* Route le Plan vers les Agents Concernés : En fonction du nombre de sous-tâches, le planificateur envoie soit directement le message à un agent dédié (pour des scénarios de tâche unique), soit coordonne via un gestionnaire de discussion de groupe pour une collaboration multi-agent.
* Résume le Résultat : Enfin, le planificateur résume le plan généré pour plus de clarté.  
Voici un exemple de code Python illustrant ces étapes :

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

Voici la sortie du code ci-dessus, que vous pouvez ensuite utiliser pour router vers `assigned_agent` et résumer le plan de voyage pour l'utilisateur final :

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Un exemple de notebook contenant cet extrait de code est disponible [ici](../../../07-planning-design/code_samples/07-autogen.ipynb).

### Planification Itérative

Certaines tâches nécessitent des allers-retours ou une re-planification, où le résultat d'une sous-tâche influence la suivante. Par exemple, si l'agent découvre un format de données inattendu lors de la réservation de vols, il pourrait devoir adapter sa stratégie avant de passer à la réservation d'hôtels.

De plus, les retours utilisateurs (par exemple, un humain décidant de préférer un vol plus tôt) peuvent déclencher une re-planification partielle. Cette approche dynamique et itérative garantit que la solution finale s'aligne sur les contraintes du monde réel et les préférences évolutives des utilisateurs.

Exemple de code :

    ```python
    from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
    #.. same as previous code and pass on the user history, current plan 
    messages = [
        SystemMessage(content="""You are a planner agent to optimize the 
        Your job is to decide which agents to run based on the user's request.
        Below are the available agents specialised in different tasks:
        - FlightBooking: For booking flights and providing flight information
        - HotelBooking: For booking hotels and providing hotel information
        - CarRental: For booking cars and providing car rental information
        - ActivitiesBooking: For booking activities and providing activity information
        - DestinationInfo: For providing information about destinations
        - DefaultAgent: For handling general requests""", source="system"),
        UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
        AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
    ]
    # .. re-plan and send the tasks to respective agents
    ```

Pour une planification plus complète, consultez le [Blogpost Magnetic One](https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks) pour résoudre des tâches complexes.

## Résumé

Dans cet article, nous avons examiné un exemple de création d'un planificateur capable de sélectionner dynamiquement les agents disponibles définis. La sortie du planificateur décompose les tâches et attribue les agents pour qu'ils soient exécutés. On suppose que les agents ont accès aux fonctions/outils nécessaires pour effectuer la tâche. En plus des agents, vous pouvez inclure d'autres modèles comme la réflexion, le résumé, ou un chat en round-robin pour personnaliser davantage.

## Ressources Supplémentaires

* L'utilisation de modèles de raisonnement o1 a prouvé des avancées significatives dans la planification de tâches complexes - TODO : Partager un exemple ?

* Autogen Magnetic One - Un système multi-agent généraliste pour résoudre des tâches complexes, qui a obtenu des résultats impressionnants sur plusieurs benchmarks exigeants. Référence : [autogen-magentic-one](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one). Dans cette implémentation, l'orchestrateur crée un plan spécifique à la tâche et délègue ces tâches aux agents disponibles. En plus de la planification, l'orchestrateur utilise un mécanisme de suivi pour surveiller l'avancement des tâches et re-planifier si nécessaire.
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.