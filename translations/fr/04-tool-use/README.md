```markdown
# Modèle de Conception pour l'Utilisation d'Outils  

## Introduction

Dans cette leçon, nous allons chercher à répondre aux questions suivantes :

- Qu'est-ce que le modèle de conception pour l'utilisation d'outils ?
- Quels sont les cas d'utilisation auxquels il peut s'appliquer ?
- Quels sont les éléments nécessaires pour implémenter ce modèle de conception ?
- Quelles sont les considérations particulières pour utiliser ce modèle de conception afin de construire des agents d'IA fiables ?

## Objectifs d'Apprentissage

Après avoir terminé cette leçon, vous serez capable de :

- Définir le modèle de conception pour l'utilisation d'outils et son objectif.
- Identifier les cas d'utilisation où ce modèle de conception est applicable.
- Comprendre les éléments clés nécessaires pour implémenter le modèle de conception.
- Reconnaître les considérations pour garantir la fiabilité des agents d'IA utilisant ce modèle.

## Qu'est-ce que le Modèle de Conception pour l'Utilisation d'Outils ?

Le **Modèle de Conception pour l'Utilisation d'Outils** se concentre sur la capacité des LLMs (modèles de langage de grande taille) à interagir avec des outils externes pour atteindre des objectifs spécifiques. Les outils sont des morceaux de code qui peuvent être exécutés par un agent pour effectuer des actions. Un outil peut être une fonction simple, comme une calculatrice, ou un appel d'API vers un service tiers, tel qu'une recherche de prix d'actions ou une prévision météorologique. Dans le contexte des agents d'IA, les outils sont conçus pour être exécutés par des agents en réponse à des **appels de fonction générés par le modèle**.

## À quels cas d'utilisation cela peut-il s'appliquer ?

Les agents d'IA peuvent utiliser des outils pour accomplir des tâches complexes, récupérer des informations ou prendre des décisions. Le modèle de conception pour l'utilisation d'outils est souvent utilisé dans des scénarios nécessitant une interaction dynamique avec des systèmes externes, tels que des bases de données, des services web ou des interpréteurs de code. Cette capacité est utile pour de nombreux cas d'utilisation différents, notamment :

- **Récupération Dynamique d'Informations :** Les agents peuvent interroger des API externes ou des bases de données pour obtenir des données actualisées (par exemple, interroger une base de données SQLite pour une analyse de données, récupérer des prix d'actions ou des informations météorologiques).
- **Exécution et Interprétation de Code :** Les agents peuvent exécuter du code ou des scripts pour résoudre des problèmes mathématiques, générer des rapports ou effectuer des simulations.
- **Automatisation de Flux de Travail :** Automatiser des flux de travail répétitifs ou multi-étapes en intégrant des outils comme des planificateurs de tâches, des services de messagerie ou des pipelines de données.
- **Support Client :** Les agents peuvent interagir avec des systèmes CRM, des plateformes de gestion de tickets ou des bases de connaissances pour résoudre les demandes des utilisateurs.
- **Génération et Édition de Contenu :** Les agents peuvent utiliser des outils comme des correcteurs grammaticaux, des résumeurs de texte ou des évaluateurs de sécurité de contenu pour aider dans les tâches de création de contenu.

## Quels sont les éléments nécessaires pour implémenter le modèle de conception pour l'utilisation d'outils ?

### Appel de Fonctions/Outils

L'appel de fonctions est le principal moyen permettant aux LLMs d'interagir avec des outils. Vous verrez souvent les termes "Fonction" et "Outil" utilisés de manière interchangeable, car les "fonctions" (blocs de code réutilisable) sont les "outils" qu'utilisent les agents pour accomplir des tâches. Pour qu'une fonction soit invoquée, un LLM doit comparer la requête de l'utilisateur à la description de la fonction. Pour ce faire, un schéma contenant les descriptions de toutes les fonctions disponibles est envoyé au LLM. Le LLM sélectionne ensuite la fonction la plus appropriée pour la tâche et renvoie son nom ainsi que ses arguments. La fonction sélectionnée est exécutée, sa réponse est renvoyée au LLM, qui utilise l'information pour répondre à la demande de l'utilisateur.

Pour que les développeurs puissent implémenter l'appel de fonctions pour les agents, vous aurez besoin de :

1. Un modèle LLM prenant en charge l'appel de fonctions
2. Un schéma contenant les descriptions des fonctions
3. Le code de chaque fonction décrite

Prenons l'exemple d'obtenir l'heure actuelle dans une ville pour illustrer :

- **Initialiser un LLM prenant en charge l'appel de fonctions :**

    Tous les modèles ne prennent pas en charge l'appel de fonctions, il est donc important de vérifier que le LLM que vous utilisez le fait. [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) prend en charge l'appel de fonctions. Nous pouvons commencer par initialiser le client Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

- **Créer un Schéma de Fonction :**

    Ensuite, nous définirons un schéma JSON contenant le nom de la fonction, une description de ce que fait la fonction, ainsi que les noms et descriptions des paramètres de la fonction. 
    Nous transmettrons ensuite ce schéma au client créé ci-dessus, avec la requête de l'utilisateur pour trouver l'heure à San Francisco. Ce qui est important à noter, c'est qu'un **appel d'outil** est ce qui est renvoyé, **pas** la réponse finale à la question. Comme mentionné précédemment, le LLM renvoie le nom de la fonction qu'il a sélectionnée pour la tâche, ainsi que les arguments qui lui seront passés.

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
- **Le code de la fonction nécessaire pour accomplir la tâche :**

    Maintenant que le LLM a choisi quelle fonction doit être exécutée, le code qui accomplit la tâche doit être implémenté et exécuté.
    Nous pouvons implémenter le code pour obtenir l'heure actuelle en Python. Nous devrons également écrire le code pour extraire le nom et les arguments de la réponse du message afin d'obtenir le résultat final.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

    ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

    ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

L'appel de fonctions est au cœur de la conception de la plupart des agents utilisant des outils, sinon tous. Cependant, l'implémenter à partir de zéro peut parfois être un défi.
Comme nous l'avons appris dans la [Leçon 2](../../../02-explore-agentic-frameworks), les frameworks agentiques nous fournissent des blocs de construction préconstruits pour implémenter l'utilisation d'outils.

### Exemples d'Utilisation d'Outils avec des Frameworks Agentiques

- ### **[Semantic Kernel](https://learn.microsoft.com/azure/ai-services/agents/overview)**

    Semantic Kernel est un framework open-source pour les développeurs .NET, Python et Java travaillant avec des LLMs. Il simplifie le processus d'utilisation de l'appel de fonctions en décrivant automatiquement vos fonctions et leurs paramètres au modèle via un processus appelé [sérialisation](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions). Il gère également la communication entre le modèle et votre code. Un autre avantage d'utiliser un framework agentique comme Semantic Kernel est qu'il vous permet d'accéder à des outils préconstruits comme [File Search](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py) et [Code Interpreter](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py).

    Le diagramme suivant illustre le processus d'appel de fonctions avec Semantic Kernel :

    ![appel de fonctions](../../../translated_images/functioncalling-diagram.b5493ea5154ad8e3e4940d2e36a49101eec1398948e5d1039942203b4f5a4209.fr.png)

    Dans Semantic Kernel, les fonctions/outils sont appelés [Plugins](https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python). Nous pouvons convertir la fonction `get_current_time` function we saw earlier into a plugin by turning it into a class with the function in it. We can also import the `kernel_function` avec un décorateur qui prend la description de la fonction. Lorsque vous créez ensuite un kernel avec le GetCurrentTimePlugin, le kernel sérialisera automatiquement la fonction et ses paramètres, créant ainsi le schéma à envoyer au LLM.

    ```python
    from semantic_kernel.functions import kernel_function

    class GetCurrentTimePlugin:
        async def __init__(self, location):
            self.location = location

        @kernel_function(
            description="Get the current time for a given location"
        )
        def get_current_time(location: str = ""):
            ...

    ```

    ```python 
    from semantic_kernel import Kernel

    # Create the kernel
    kernel = Kernel()

    # Create the plugin
    get_current_time_plugin = GetCurrentTimePlugin(location)

    # Add the plugin to the kernel
    kernel.add_plugin(get_current_time_plugin)
    ```
  
- ### **[Azure AI Agent Service](https://learn.microsoft.com/azure/ai-services/agents/overview)**

    Azure AI Agent Service est un framework agentique plus récent conçu pour permettre aux développeurs de construire, déployer et faire évoluer des agents d'IA de haute qualité et extensibles sans avoir à gérer les ressources de calcul et de stockage sous-jacentes. Il est particulièrement utile pour les applications d'entreprise, car il s'agit d'un service entièrement géré avec une sécurité de niveau entreprise.

    Comparé au développement direct avec l'API LLM, Azure AI Agent Service offre plusieurs avantages, notamment :
  - Appels d'outils automatiques – plus besoin d'analyser un appel d'outil, d'invoquer l'outil et de gérer la réponse ; tout cela est désormais effectué côté serveur.
  - Gestion sécurisée des données – au lieu de gérer votre propre état de conversation, vous pouvez vous appuyer sur les threads pour stocker toutes les informations nécessaires.
  - Outils prêts à l'emploi – des outils que vous pouvez utiliser pour interagir avec vos sources de données, comme Bing, Azure AI Search et Azure Functions.

    Les outils disponibles dans Azure AI Agent Service peuvent être divisés en deux catégories :

    1. Outils de Connaissances :
        - [Recherche avec Bing](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview)
        - [File Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview)
        - [Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search)

    2. Outils d'Action :
        - [Appel de Fonctions](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview)
        - [Interprète de Code](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview)
        - [Outils Définis par OpenAI](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview)
        - [Azure Functions](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview)

    Le Service Agent vous permet d'utiliser ces outils ensemble en tant que `toolset`. It also utilizes `threads` which keep track of the history of messages from a particular conversation.

    Imagine you are a sales agent at a company called Contoso. You want to develop a conversational agent that can answer questions about your sales data.

    The image below illustrates how you could use Azure AI Agent Service to analyze your sales data:

    ![Agentic Service In Action](../../../translated_images/agent-service-in-action.jpg?WT.858cf9f67cc5c7f16ff3660d3df11c90e8cda37025bea4db5c4a59d2facce09a.fr.mc_id=academic-105485-koreyst)

    To use any of these tools with the service we can create a client and define a tool or toolset. To implement this practically we can use the Python code below. The LLM will be able to look at the toolset and decide whether to use the user created function, `fetch_sales_data_using_sqlite_query`, ou l'Interprète de Code préconstruit, en fonction de la requête de l'utilisateur.

    ```python 
    import os
    from azure.ai.projects import AIProjectClient
    from azure.identity import DefaultAzureCredential
    from fecth_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fecth_sales_data_functions.py file.
    from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

    project_client = AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str=os.environ["PROJECT_CONNECTION_STRING"],
    )

    # Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
    fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
    toolset = ToolSet()
    toolset.add(fetch_data_function)

    # Initialize Code Interpreter tool and adding it to the toolset. 
    code_interpreter = code_interpreter = CodeInterpreterTool()
    toolset = ToolSet()
    toolset.add(code_interpreter)

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
        toolset=toolset
    )
    ```

## Quelles sont les considérations particulières pour utiliser le Modèle de Conception pour l'Utilisation d'Outils afin de construire des agents d'IA fiables ?

Une préoccupation courante avec le SQL généré dynamiquement par les LLMs est la sécurité, en particulier le risque d'injection SQL ou d'actions malveillantes, comme la suppression ou la modification de la base de données. Bien que ces préoccupations soient valables, elles peuvent être efficacement atténuées en configurant correctement les permissions d'accès à la base de données. Pour la plupart des bases de données, cela implique de configurer la base de données en lecture seule. Pour des services de bases de données comme PostgreSQL ou Azure SQL, l'application doit se voir attribuer un rôle en lecture seule (SELECT).

Exécuter l'application dans un environnement sécurisé renforce encore davantage la protection. Dans les scénarios d'entreprise, les données sont généralement extraites et transformées à partir de systèmes opérationnels dans une base de données ou un entrepôt de données en lecture seule avec un schéma convivial. Cette approche garantit que les données sont sécurisées, optimisées pour la performance et l'accessibilité, et que l'application dispose d'un accès restreint en lecture seule.

## Ressources Supplémentaires

- [Atelier Azure AI Agents Service](https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/)
- [Atelier Multi-Agent Contoso Creative Writer](https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop)
- [Tutoriel d'Appel de Fonction Semantic Kernel](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)
- [Interprète de Code Semantic Kernel](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)
- [Outils Autogen](https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html)
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.