```markdown
# Explorer les frameworks d'agents IA

Les frameworks d'agents IA sont des plateformes logicielles conçues pour simplifier la création, le déploiement et la gestion des agents IA. Ces frameworks offrent aux développeurs des composants préconstruits, des abstractions et des outils qui facilitent le développement de systèmes IA complexes.

Ces frameworks permettent aux développeurs de se concentrer sur les aspects uniques de leurs applications en fournissant des approches standardisées pour relever les défis courants dans le développement d'agents IA. Ils améliorent la scalabilité, l'accessibilité et l'efficacité dans la construction de systèmes IA.

## Introduction

Cette leçon couvrira :

- Ce que sont les frameworks d'agents IA et ce qu'ils permettent aux développeurs de réaliser.
- Comment les équipes peuvent les utiliser pour prototyper rapidement, itérer et améliorer les capacités de leurs agents.
- Les différences entre les frameworks et outils créés par Microsoft ([Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)).
- Est-il possible d'intégrer directement les outils de l'écosystème Azure existants ou faut-il des solutions autonomes ?
- Qu'est-ce que le service Azure AI Agents et comment cela peut-il vous aider ?

## Objectifs d'apprentissage

Les objectifs de cette leçon sont de vous aider à comprendre :

- Le rôle des frameworks d'agents IA dans le développement IA.
- Comment exploiter ces frameworks pour construire des agents intelligents.
- Les principales capacités qu'ils permettent.
- Les différences entre Autogen, Semantic Kernel et Azure AI Agent Service.

## Que sont les frameworks d'agents IA et que permettent-ils aux développeurs ?

Les frameworks IA traditionnels peuvent vous aider à intégrer l'IA dans vos applications et à les améliorer de plusieurs façons :

- **Personnalisation** : L'IA peut analyser le comportement et les préférences des utilisateurs pour fournir des recommandations, du contenu et des expériences personnalisés.  
Exemple : Les services de streaming comme Netflix utilisent l'IA pour suggérer des films et des séries en fonction de l'historique de visionnage, améliorant ainsi l'engagement et la satisfaction des utilisateurs.
- **Automatisation et efficacité** : L'IA peut automatiser les tâches répétitives, rationaliser les flux de travail et améliorer l'efficacité opérationnelle.  
Exemple : Les applications de service client utilisent des chatbots IA pour gérer les questions courantes, réduisant les temps de réponse et libérant les agents humains pour des problèmes plus complexes.
- **Amélioration de l'expérience utilisateur** : L'IA peut améliorer l'expérience utilisateur globale grâce à des fonctionnalités intelligentes comme la reconnaissance vocale, le traitement du langage naturel et la saisie prédictive.  
Exemple : Les assistants virtuels comme Siri et Google Assistant utilisent l'IA pour comprendre et répondre aux commandes vocales, facilitant ainsi l'interaction des utilisateurs avec leurs appareils.

### Cela semble génial, non ? Alors pourquoi avons-nous besoin de frameworks d'agents IA ?

Les frameworks d'agents IA vont au-delà des simples frameworks IA. Ils sont conçus pour permettre la création d'agents intelligents capables d'interagir avec les utilisateurs, d'autres agents et leur environnement pour atteindre des objectifs spécifiques. Ces agents peuvent présenter un comportement autonome, prendre des décisions et s'adapter à des conditions changeantes. Voici quelques-unes des principales capacités qu'ils permettent :

- **Collaboration et coordination entre agents** : Permet la création de plusieurs agents IA capables de travailler ensemble, de communiquer et de se coordonner pour résoudre des tâches complexes.
- **Automatisation et gestion des tâches** : Fournit des mécanismes pour automatiser les flux de travail multi-étapes, déléguer des tâches et gérer dynamiquement les tâches entre les agents.
- **Compréhension contextuelle et adaptation** : Équipe les agents de la capacité à comprendre le contexte, à s'adapter à des environnements changeants et à prendre des décisions basées sur des informations en temps réel.

En résumé, les agents permettent de faire plus, de pousser l'automatisation à un niveau supérieur, et de créer des systèmes plus intelligents capables de s'adapter et d'apprendre de leur environnement.

## Comment prototyper rapidement, itérer et améliorer les capacités de l'agent ?

Ce domaine évolue rapidement, mais il existe des éléments communs à la plupart des frameworks d'agents IA qui peuvent vous aider à prototyper et itérer rapidement, notamment les composants modulaires, les outils collaboratifs et l'apprentissage en temps réel. Examinons ces éléments :

- **Utilisez des composants modulaires** : Les frameworks IA offrent des composants préconstruits tels que des invites, des analyseurs et une gestion de la mémoire.
- **Exploitez les outils collaboratifs** : Concevez des agents avec des rôles et des tâches spécifiques, ce qui permet de tester et d'affiner les flux de travail collaboratifs.
- **Apprenez en temps réel** : Mettez en œuvre des boucles de rétroaction où les agents apprennent des interactions et ajustent leur comportement de manière dynamique.

### Utilisez des composants modulaires

Des frameworks comme LangChain et Microsoft Semantic Kernel proposent des composants préconstruits tels que des invites, des analyseurs et une gestion de la mémoire.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent assembler rapidement ces composants pour créer un prototype fonctionnel sans partir de zéro, ce qui permet une expérimentation et une itération rapides.

**Comment cela fonctionne en pratique** : Vous pouvez utiliser un analyseur préconstruit pour extraire des informations des entrées utilisateur, un module de mémoire pour stocker et récupérer des données, et un générateur d'invites pour interagir avec les utilisateurs, le tout sans avoir à construire ces composants de zéro.

**Exemple de code**. Voici un exemple montrant comment utiliser un analyseur préconstruit pour extraire des informations des entrées utilisateur :

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

Cet exemple illustre comment exploiter un analyseur préconstruit pour extraire des informations clés des entrées utilisateur, telles que l'origine, la destination et la date d'une demande de réservation de vol. Cette approche modulaire vous permet de vous concentrer sur la logique de haut niveau.

### Exploitez les outils collaboratifs

Des frameworks comme CrewAI et Microsoft Autogen facilitent la création de plusieurs agents capables de travailler ensemble.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent concevoir des agents avec des rôles et des tâches spécifiques, leur permettant de tester et d'affiner les flux de travail collaboratifs et d'améliorer l'efficacité globale du système.

**Comment cela fonctionne en pratique** : Vous pouvez créer une équipe d'agents où chaque agent a une fonction spécialisée, telle que la récupération de données, l'analyse ou la prise de décision. Ces agents peuvent communiquer et partager des informations pour atteindre un objectif commun, comme répondre à une question utilisateur ou accomplir une tâche.

**Exemple de code (Autogen)** :

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

Dans ce code, vous voyez comment créer une tâche impliquant plusieurs agents travaillant ensemble pour analyser des données. Chaque agent remplit une fonction spécifique, et la tâche est exécutée en coordonnant les agents pour atteindre le résultat souhaité. En créant des agents dédiés avec des rôles spécialisés, vous pouvez améliorer l'efficacité et les performances des tâches.

### Apprenez en temps réel

Les frameworks avancés offrent des capacités de compréhension contextuelle et d'adaptation en temps réel.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent mettre en œuvre des boucles de rétroaction où les agents apprennent des interactions et ajustent leur comportement de manière dynamique, ce qui conduit à une amélioration continue et à un affinage des capacités.

**Comment cela fonctionne en pratique** : Les agents peuvent analyser les retours des utilisateurs, les données environnementales et les résultats des tâches pour mettre à jour leur base de connaissances, ajuster leurs algorithmes de prise de décision et améliorer leurs performances au fil du temps. Ce processus d'apprentissage itératif permet aux agents de s'adapter aux conditions changeantes et aux préférences des utilisateurs, améliorant ainsi l'efficacité globale du système.

## Quelles sont les différences entre les frameworks Autogen, Semantic Kernel et Azure AI Agent Service ?

Il existe plusieurs façons de comparer ces frameworks, mais examinons quelques différences clés en termes de conception, de capacités et de cas d'utilisation cible :

### Autogen

Framework open-source développé par le laboratoire AI Frontiers de Microsoft Research. Il se concentre sur des applications agentiques distribuées et pilotées par des événements, permettant l'intégration de plusieurs LLMs et SLMs, d'outils, et de modèles de conception multi-agents avancés.

Autogen est basé sur le concept central d'agents, qui sont des entités autonomes capables de percevoir leur environnement, de prendre des décisions et d'agir pour atteindre des objectifs spécifiques. Les agents communiquent via des messages asynchrones, ce qui leur permet de fonctionner indépendamment et en parallèle, améliorant ainsi la scalabilité et la réactivité du système.

Les agents sont basés sur le [modèle d'acteur](https://en.wikipedia.org/wiki/Actor_model). Selon Wikipédia, un acteur est _l'élément de base du calcul concurrent. En réponse à un message qu'il reçoit, un acteur peut : prendre des décisions locales, créer d'autres acteurs, envoyer d'autres messages et déterminer comment répondre au prochain message reçu_.

**Cas d'utilisation** : Automatisation de la génération de code, des tâches d'analyse de données, et création d'agents personnalisés pour des fonctions de planification et de recherche.

Voici quelques concepts clés d'Autogen :

- **Agents** : Un agent est une entité logicielle qui : 
  - **Communique via des messages**, ces messages pouvant être synchrones ou asynchrones.
  - **Maintient son propre état**, qui peut être modifié par des messages entrants.
  - **Effectue des actions** en réponse aux messages reçus ou aux changements de son état. Ces actions peuvent modifier l'état de l'agent et produire des effets externes, tels que la mise à jour des journaux de messages, l'envoi de nouveaux messages, l'exécution de code ou l'appel d'API.
    
  Voici un court extrait de code montrant comment créer votre propre agent avec des capacités de chat :

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    Dans ce code, `MyAssistant` has been created and inherits from `RoutedAgent`. It has a message handler that prints the content of the message and then sends a response using the `AssistantAgent` delegate. Especially note how we assign to `self._delegate` an instance of `AssistantAgent` représente un agent préconstruit capable de gérer des complétions de chat.

    Passons à l'enregistrement de ce type d'agent dans Autogen et lançons le programme :

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Ici, l'agent est enregistré auprès de l'environnement d'exécution, puis un message est envoyé à l'agent, produisant la sortie suivante :

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-agents** : Autogen prend en charge la création de plusieurs agents pouvant travailler ensemble pour accomplir des tâches complexes. Vous pouvez définir différents types d'agents avec des fonctions et rôles spécialisés, tels que la récupération de données, l'analyse, la prise de décision et l'interaction utilisateur. Voici un exemple de création d'un système multi-agents :

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    Dans cet exemple, un `GroupChatManager` est enregistré auprès de l'environnement d'exécution. Ce gestionnaire coordonne les interactions entre différents types d'agents, comme les rédacteurs, les illustrateurs, les éditeurs et les utilisateurs.

- **Environnement d'exécution des agents** : Le framework fournit un environnement d'exécution qui permet la communication entre les agents, gère leurs identités et cycles de vie, et applique des frontières de sécurité et de confidentialité. Deux types d'environnements d'exécution sont disponibles :
  - **Environnement autonome** : Idéal pour les applications monoprocédé où tous les agents sont implémentés dans le même langage de programmation et s'exécutent dans le même processus. Voici une illustration de son fonctionnement :
  
  ![Environnement autonome](https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg)   
Application stack

    *Les agents communiquent via des messages à travers l'environnement d'exécution, qui gère leur cycle de vie.*

  - **Environnement distribué**, adapté aux applications multiprocédés où les agents peuvent être implémentés dans différents langages de programmation et s'exécuter sur des machines différentes. Voici une illustration de son fonctionnement :
  
  ![Environnement distribué](https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg)

### Semantic Kernel + Framework d'agents

Semantic Kernel se compose de deux éléments : le framework d'agents Semantic Kernel et le Semantic Kernel lui-même.

Commençons par parler de Semantic Kernel. Ses concepts clés incluent :

- **Connexions** : Interface avec des services IA externes et des sources de données.

    ```csharp
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    Cet exemple montre comment créer un kernel et ajouter un service de complétion de chat. Semantic Kernel établit une connexion avec un service IA externe, ici Azure OpenAI Chat Completion.

- **Plugins** : Encapsulent des fonctions que l'application peut utiliser. Il existe des plugins prêts à l'emploi ainsi que des plugins personnalisables. Le concept de "fonctions sémantiques" est également présent. Ces fonctions utilisent des informations sémantiques pour aider Semantic Kernel à déterminer quand elles doivent être appelées. Exemple :

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // Register the function
    kernel.CreateSemanticFunction(
        promptTemplate: skPrompt,
        functionName: "SummarizeText",
        pluginName: "SemanticFunctions"
    );
    ```

    Ici, une invite modèle `skPrompt` that leaves room for the user to input text, `$userInput`. Then you register the function `SummarizeText` with the plugin `SemanticFunctions` est définie. Le nom de la fonction aide Semantic Kernel à comprendre son rôle.

- **Fonctions natives** : Des fonctions que le framework peut appeler directement pour effectuer des tâches. Exemple d'une fonction récupérant le contenu d'un fichier :

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";
    
    var nativeFunctions = new NativeFunctions();
    kernel.ImportFunctions(nativeFunctions, plugInName);
    ```

- **Planificateur** : Orchestration des plans d'exécution et stratégies basées sur les entrées utilisateur. Exemple de plan :

    ```csharp
    string planDefinition = "Read content from a local file and summarize the content.";
    SequentialPlanner sequentialPlanner = new SequentialPlanner(kernel);
    
    string assetsFolder = @"../../assets";
    string fileName = Path.Combine(assetsFolder,"docs","06_SemanticKernel", "aci_documentation.txt");
    
    ContextVariables contextVariables = new ContextVariables();
    contextVariables.Add("fileName", fileName);
    
    var customPlan = await sequentialPlanner.CreatePlanAsync(planDefinition);
    
    // Execute the plan
    KernelResult kernelResult = await kernel.RunAsync(contextVariables, customPlan);
    Console.WriteLine($"Summarization: {kernelResult.GetValue<string>()}");
    ```

    Notez `planDefinition` which is a simple instruction for the planner to follow. The appropriate functions are then called based on this plan, in this case our semantic function `SummarizeText` and the native function `RetrieveLocalFile`.
- **Mémoire** : Simplifie la gestion du contexte pour les applications IA. Exemple de stockage d'informations dans une collection mémoire :

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/en-us/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/en-us/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    Ces faits sont stockés dans `SummarizedAzureDocs`. Cet exemple montre comment stocker des informations pour que le LLM puisse les utiliser.

Qu'en est-il du framework d'agents ?

### Azure AI Agent Service

Azure AI Agent Service est une nouveauté introduite lors de Microsoft Ignite 2024. Il permet de développer et déployer des agents IA avec des modèles plus flexibles, comme l'appel direct de LLM open-source tels que Llama 3, Mistral et Cohere.

Ce service offre des mécanismes de sécurité d'entreprise renforcés et des méthodes de stockage des données adaptées aux applications d'entreprise.

Il fonctionne directement avec des frameworks d'orchestration multi-agents comme Autogen et Semantic Kernel.

Ce service est actuellement en aperçu public et prend en charge Python et C# pour la création d'agents.

#### Concepts clés

Azure AI Agent Service repose sur les concepts suivants :

- **Agent** : Intégré avec Azure AI Foundry. Un agent agit comme un microservice intelligent pour répondre aux questions, exécuter des actions ou automatiser des flux de travail. Exemple :

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Cet exemple montre un agent équipé pour effectuer des tâches d'interprétation de code.

- **Threads et messages** : Représentent une conversation ou interaction entre un agent et un utilisateur. Exemple :

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Ici, un thread est créé, un message est envoyé et l'agent traite ce message. Les messages indiquent la progression de la conversation.

- **Intégration avec d'autres frameworks IA** : Azure AI Agent Service peut interagir avec Autogen et Semantic Kernel.

**Cas d'utilisation** : Conçu pour des applications d'entreprise nécessitant un déploiement d'agents IA sécurisé, évolutif et flexible.

---

## Quelle est la différence entre ces frameworks ?

Bien qu'il y ait des chevauchements entre ces frameworks, leurs conceptions, capacités et cas d'utilisation cibles diffèrent :

- **Autogen** : Conçu pour des applications agentiques distribuées et pilotées par des événements, avec des modèles de conception multi-agents avancés.
- **Semantic Kernel** : Se concentre sur la compréhension et la génération de contenu textuel humain, l'automatisation de workflows complexes et l'initiation de tâches.
- **Azure AI Agent Service** : Offre des modèles flexibles, une sécurité renforcée et un stockage adapté aux entreprises.

Toujours incertain sur le choix ? Examinons quelques cas d'utilisation :

### Cas d'utilisation

> Q : Mon équipe travaille sur un projet impliquant l'automatisation de la génération de code et des tâches d'analyse de données. Quel framework devrions-nous utiliser ?  
> R : Autogen serait un bon choix, car il se concentre sur des applications agentiques distribuées et prend en charge des modèles de conception multi-agents avancés.

> Q : Pourquoi Autogen est-il meilleur que Semantic Kernel et Azure AI Agent Service pour ce cas d'utilisation ?  
> R : Autogen est spécifiquement conçu pour des applications agentiques distribuées et pilotées par des événements, ce qui le rend idéal pour automatiser la génération de code et les tâches d'analyse de données.

> Q : Azure AI Agent Service pourrait-il également convenir ici ?  
> R : Oui, Azure AI Agent Service prend également en charge ces tâches, mais il est davantage adapté aux applications d'entreprise nécessitant un déploiement d'agents IA sécurisé et évolutif.

> Q : Donc, si je veux aller vers une solution d'entreprise, je devrais choisir Azure AI Agent Service ?  
> R : Oui, Azure AI Agent Service est conçu pour les applications d'entreprise nécessitant une sécurité renforcée et une flexibilité accrue.

---

Résumé des différences clés dans un tableau :

| Framework             | Focus                                         | Concepts clés                 | Cas d'utilisation                         |
|-----------------------|-----------------------------------------------|--------------------------------|-------------------------------------------|
| **Autogen**           | Applications agentiques distribuées          | Agents, fonctions, données    | Génération de code, analyse de données    |
| **Semantic Kernel**   | Compréhension et génération de contenu        | Plugins, mémoire, planificateur | Compréhension du langage, génération de contenu |
| **Azure AI Agent Service** | Modèles flexibles, sécurité d'entreprise | Agents, threads, intégration  | Déploiement sécurisé et évolutif         |

---

### Cas d'utilisation idéal pour chaque framework :

- **Autogen** : Applications agentiques distribuées, modèles multi-agents avancés. Idéal pour la génération de code et l'analyse de données.
- **Semantic Kernel** : Automatisation de workflows complexes, compréhension du langage naturel.
- **Azure AI Agent Service** : Déploiement d'agents IA sécurisés et évolutifs, adapté aux besoins des entreprises
basé sur les objectifs du projet. Idéal pour la compréhension du langage naturel, la génération de contenu. - **Azure AI Agent Service** : Modèles flexibles, mécanismes de sécurité d'entreprise, méthodes de stockage de données. Idéal pour le déploiement sécurisé, évolutif et flexible d'agents IA dans des applications d'entreprise.  

## Puis-je intégrer directement mes outils existants de l'écosystème Azure, ou ai-je besoin de solutions autonomes ?  
La réponse est oui, vous pouvez intégrer vos outils existants de l'écosystème Azure directement avec Azure AI Agent Service, notamment parce qu'il a été conçu pour fonctionner de manière transparente avec d'autres services Azure. Vous pourriez, par exemple, intégrer Bing, Azure AI Search et Azure Functions. Il existe également une intégration approfondie avec Azure AI Foundry.  

Pour Autogen et Semantic Kernel, vous pouvez également intégrer des services Azure, mais cela peut nécessiter d'appeler les services Azure depuis votre code. Une autre manière d'intégrer consiste à utiliser les SDK Azure pour interagir avec les services Azure depuis vos agents. De plus, comme mentionné, vous pouvez utiliser Azure AI Agent Service comme orchestrateur pour vos agents créés dans Autogen ou Semantic Kernel, ce qui permettrait un accès facile à l'écosystème Azure.  

## Références  
- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)  
- [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/)  
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp)  
- [4] - [Azure AI Agent service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)  
- [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)  

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.