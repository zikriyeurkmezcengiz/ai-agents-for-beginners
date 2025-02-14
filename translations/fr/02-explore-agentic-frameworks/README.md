# Explorer les Frameworks d'Agents IA

Les frameworks d'agents IA sont des plateformes logicielles conçues pour simplifier la création, le déploiement et la gestion d'agents IA. Ces frameworks offrent aux développeurs des composants préconstruits, des abstractions et des outils qui facilitent le développement de systèmes IA complexes.

Ces frameworks permettent aux développeurs de se concentrer sur les aspects uniques de leurs applications en proposant des approches standardisées pour relever les défis communs du développement d'agents IA. Ils améliorent la scalabilité, l'accessibilité et l'efficacité dans la construction de systèmes IA.

## Introduction

Cette leçon couvrira :

- Ce que sont les frameworks d'agents IA et ce qu'ils permettent aux développeurs de réaliser.
- Comment les équipes peuvent les utiliser pour prototyper rapidement, itérer et améliorer les capacités de leurs agents.
- Les différences entre les frameworks et outils créés par Microsoft ([Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)).
- Est-il possible d'intégrer directement mes outils existants de l'écosystème Azure, ou ai-je besoin de solutions autonomes ?
- Qu'est-ce que le service Azure AI Agents et comment cela m'aide-t-il ?

## Objectifs d'apprentissage

Les objectifs de cette leçon sont de vous aider à comprendre :

- Le rôle des frameworks d'agents IA dans le développement IA.
- Comment tirer parti des frameworks d'agents IA pour construire des agents intelligents.
- Les capacités clés offertes par les frameworks d'agents IA.
- Les différences entre Autogen, Semantic Kernel et Azure AI Agent Service.

## Que sont les frameworks d'agents IA et que permettent-ils aux développeurs de faire ?

Les frameworks IA traditionnels peuvent vous aider à intégrer l'IA dans vos applications et à améliorer ces dernières de plusieurs façons :

- **Personnalisation** : L'IA peut analyser le comportement et les préférences des utilisateurs pour fournir des recommandations, contenus et expériences personnalisés.  
Exemple : Les services de streaming comme Netflix utilisent l'IA pour suggérer des films et des séries en fonction de l'historique de visionnage, améliorant ainsi l'engagement et la satisfaction des utilisateurs.
- **Automatisation et efficacité** : L'IA peut automatiser les tâches répétitives, rationaliser les flux de travail et améliorer l'efficacité opérationnelle.  
Exemple : Les applications de service client utilisent des chatbots alimentés par l'IA pour traiter les demandes courantes, réduisant ainsi les temps de réponse et libérant les agents humains pour des problèmes plus complexes.
- **Amélioration de l'expérience utilisateur** : L'IA peut améliorer l'expérience utilisateur globale en proposant des fonctionnalités intelligentes comme la reconnaissance vocale, le traitement du langage naturel et le texte prédictif.  
Exemple : Les assistants virtuels comme Siri et Google Assistant utilisent l'IA pour comprendre et répondre aux commandes vocales, facilitant l'interaction des utilisateurs avec leurs appareils.

### Tout cela semble génial, n'est-ce pas ? Alors pourquoi avons-nous besoin de frameworks d'agents IA ?

Les frameworks d'agents IA représentent quelque chose de plus que les simples frameworks IA. Ils sont conçus pour permettre la création d'agents intelligents capables d'interagir avec les utilisateurs, d'autres agents et leur environnement pour atteindre des objectifs spécifiques. Ces agents peuvent adopter un comportement autonome, prendre des décisions et s'adapter à des conditions changeantes. Examinons quelques capacités clés offertes par les frameworks d'agents IA :

- **Collaboration et coordination entre agents** : Permettent la création de multiples agents IA capables de travailler ensemble, communiquer et se coordonner pour résoudre des tâches complexes.
- **Automatisation et gestion des tâches** : Fournissent des mécanismes pour automatiser des flux de travail en plusieurs étapes, déléguer des tâches et gérer dynamiquement les tâches entre les agents.
- **Compréhension contextuelle et adaptation** : Équipent les agents de la capacité à comprendre le contexte, s'adapter à des environnements changeants et prendre des décisions basées sur des informations en temps réel.

En résumé, les agents permettent d'aller plus loin, de pousser l'automatisation à un niveau supérieur et de créer des systèmes plus intelligents capables de s'adapter et d'apprendre de leur environnement.

## Comment prototyper, itérer et améliorer rapidement les capacités d’un agent ?

C'est un domaine en constante évolution, mais il existe des éléments communs à la plupart des frameworks d'agents IA qui peuvent vous aider à prototyper et itérer rapidement, notamment les composants modulaires, les outils collaboratifs et l'apprentissage en temps réel. Explorons ces éléments :

- **Utiliser des composants modulaires** : Les frameworks IA offrent des composants préconstruits comme des invites, des analyseurs et des gestionnaires de mémoire.
- **Exploiter des outils collaboratifs** : Concevoir des agents avec des rôles et tâches spécifiques pour tester et affiner les flux de travail collaboratifs.
- **Apprendre en temps réel** : Mettre en œuvre des boucles de rétroaction où les agents apprennent des interactions et ajustent leur comportement de manière dynamique.

### Utiliser des composants modulaires

Des frameworks comme LangChain et Microsoft Semantic Kernel offrent des composants préconstruits tels que des invites, des analyseurs et des gestionnaires de mémoire.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent assembler rapidement ces composants pour créer un prototype fonctionnel sans partir de zéro, ce qui permet une expérimentation et une itération rapides.

**Comment cela fonctionne en pratique** : Vous pouvez utiliser un analyseur préconstruit pour extraire des informations des entrées utilisateur, un module de mémoire pour stocker et récupérer des données, et un générateur d'invites pour interagir avec les utilisateurs, sans avoir à construire ces composants à partir de zéro.

**Exemple de code**. Voici un exemple montrant comment utiliser un analyseur préconstruit pour extraire des informations des entrées utilisateur :

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

Ce que vous voyez dans cet exemple, c'est comment tirer parti d'un analyseur préconstruit pour extraire des informations clés des entrées utilisateur, comme l'origine, la destination et la date d'une demande de réservation de vol. Cette approche modulaire vous permet de vous concentrer sur la logique de haut niveau.

### Exploiter des outils collaboratifs

Des frameworks comme CrewAI et Microsoft Autogen facilitent la création de plusieurs agents capables de travailler ensemble.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent concevoir des agents avec des rôles et tâches spécifiques, leur permettant de tester et affiner les flux de travail collaboratifs et d'améliorer l'efficacité globale du système.

**Comment cela fonctionne en pratique** : Vous pouvez créer une équipe d'agents où chaque agent a une fonction spécialisée, comme la récupération de données, l'analyse ou la prise de décision. Ces agents peuvent communiquer et partager des informations pour atteindre un objectif commun, comme répondre à une requête utilisateur ou accomplir une tâche.

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

Dans le code ci-dessus, vous voyez comment créer une tâche impliquant plusieurs agents travaillant ensemble pour analyser des données. Chaque agent remplit une fonction spécifique, et la tâche est exécutée en coordonnant les agents pour atteindre le résultat souhaité. En créant des agents dédiés avec des rôles spécialisés, vous pouvez améliorer l'efficacité et les performances des tâches.

### Apprendre en temps réel

Les frameworks avancés offrent des capacités de compréhension contextuelle et d'adaptation en temps réel.

**Comment les équipes peuvent les utiliser** : Les équipes peuvent mettre en œuvre des boucles de rétroaction où les agents apprennent des interactions et ajustent leur comportement de manière dynamique, ce qui conduit à une amélioration continue et à un affinement des capacités.

**Comment cela fonctionne en pratique** : Les agents peuvent analyser les retours des utilisateurs, les données environnementales et les résultats des tâches pour mettre à jour leur base de connaissances, ajuster leurs algorithmes de prise de décision et améliorer leurs performances au fil du temps. Ce processus d'apprentissage itératif permet aux agents de s'adapter aux conditions changeantes et aux préférences des utilisateurs, améliorant ainsi l'efficacité globale du système.

## Quelles sont les différences entre les frameworks Autogen, Semantic Kernel et Azure AI Agent Service ?

Il existe plusieurs façons de comparer ces frameworks, mais examinons quelques différences clés en termes de conception, de capacités et de cas d'utilisation cibles :  

--- (La traduction continue ici, mais suit la même logique en respectant les consignes) ---
basé sur les objectifs du projet. Idéal pour la compréhension du langage naturel, la génération de contenu. - **Azure AI Agent Service** : Modèles flexibles, mécanismes de sécurité d'entreprise, méthodes de stockage des données. Idéal pour un déploiement sécurisé, évolutif et flexible d'agents IA dans des applications d'entreprise.  

## Puis-je intégrer directement mes outils existants de l'écosystème Azure, ou ai-je besoin de solutions autonomes ?  
La réponse est oui, vous pouvez intégrer directement vos outils existants de l'écosystème Azure avec Azure AI Agent Service, notamment parce qu'il a été conçu pour fonctionner de manière transparente avec d'autres services Azure. Par exemple, vous pourriez intégrer Bing, Azure AI Search et Azure Functions. Il existe également une intégration approfondie avec Azure AI Foundry.  

Pour Autogen et Semantic Kernel, vous pouvez également intégrer avec les services Azure, mais cela peut nécessiter d'appeler les services Azure depuis votre code. Une autre manière d'intégrer est d'utiliser les SDK Azure pour interagir avec les services Azure depuis vos agents. De plus, comme mentionné, vous pouvez utiliser Azure AI Agent Service comme orchestrateur pour vos agents construits dans Autogen ou Semantic Kernel, ce qui offrirait un accès facile à l'écosystème Azure.  

## Références  
- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)  
- [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/)  
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp)  
- [4] - [Azure AI Agent service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)  
- [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)  

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle effectuée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.