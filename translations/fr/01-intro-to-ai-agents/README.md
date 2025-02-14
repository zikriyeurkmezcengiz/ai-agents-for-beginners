# Introduction aux Agents IA et Cas d'Utilisation des Agents

Bienvenue dans le cours "Agents IA pour Débutants" ! Ce cours vous offre des connaissances fondamentales et des exemples pratiques pour construire avec des Agents IA.

Rejoignez la [communauté Discord Azure AI](https://discord.gg/kzRShWzttr) pour rencontrer d'autres apprenants, des créateurs d'Agents IA, et poser toutes vos questions sur ce cours.

Pour débuter ce cours, nous allons d'abord mieux comprendre ce que sont les Agents IA et comment nous pouvons les utiliser dans les applications et les flux de travail que nous concevons.

## Introduction

Cette leçon couvre :

- Qu'est-ce qu'un Agent IA et quels sont les différents types d'agents ?
- Quels cas d'utilisation sont les mieux adaptés aux Agents IA et comment peuvent-ils nous aider ?
- Quels sont certains des éléments de base à prendre en compte lors de la conception de solutions agentiques ?

## Objectifs d'Apprentissage
À la fin de cette leçon, vous devriez être capable de :

- Comprendre les concepts des Agents IA et en quoi ils diffèrent des autres solutions d'IA.
- Utiliser les Agents IA de manière efficace.
- Concevoir des solutions agentiques de manière productive pour les utilisateurs et les clients.

## Définir les Agents IA et les Types d'Agents IA

### Qu'est-ce qu'un Agent IA ?

Les Agents IA sont des **systèmes** qui permettent aux **Modèles de Langage de Grande Taille (LLMs)** de **réaliser des actions** en étendant leurs capacités grâce à l'accès à des **outils** et à des **connaissances**.

Décomposons cette définition en parties plus simples :

- **Système** - Il est important de considérer les agents non pas comme un simple composant, mais comme un système composé de plusieurs éléments. À un niveau basique, les composants d'un Agent IA sont :
  - **Environnement** - L'espace défini où l'Agent IA opère. Par exemple, si nous avions un Agent IA de réservation de voyages, l'environnement pourrait être le système de réservation utilisé par l'agent pour accomplir ses tâches.
  - **Capteurs** - Les environnements contiennent des informations et fournissent des retours. Les Agents IA utilisent des capteurs pour recueillir et interpréter ces informations sur l'état actuel de l'environnement. Dans l'exemple de l'agent de réservation, le système de réservation peut fournir des informations comme la disponibilité des hôtels ou les prix des vols.
  - **Actionneurs** - Une fois que l'Agent IA reçoit l'état actuel de l'environnement, il détermine quelle action effectuer pour modifier cet environnement en fonction de la tâche actuelle. Pour l'agent de réservation, cela pourrait être de réserver une chambre disponible pour l'utilisateur.

![Qu'est-ce qu'un Agent IA ?](../../../translated_images/what-are-ai-agents.125520f55950b252a429b04a9f41e0152d4dafa1f1bd9081f4f574631acb759e.fr.png?WT.mc_id=academic-105485-koreyst)

**Modèles de Langage de Grande Taille** - Le concept d'agents existait avant la création des LLMs. L'avantage de construire des Agents IA avec des LLMs réside dans leur capacité à interpréter le langage humain et les données. Cette capacité leur permet d'interpréter les informations environnementales et de définir un plan pour modifier l'environnement.

**Réaliser des Actions** - En dehors des systèmes d'Agents IA, les LLMs sont limités aux situations où l'action consiste à générer du contenu ou des informations en réponse à une demande de l'utilisateur. Dans les systèmes d'Agents IA, les LLMs peuvent accomplir des tâches en interprétant la demande de l'utilisateur et en utilisant les outils disponibles dans leur environnement.

**Accès aux Outils** - Les outils auxquels le LLM a accès sont définis par 1) l'environnement dans lequel il opère et 2) le développeur de l'Agent IA. Dans l'exemple de l'agent de voyage, les outils de l'agent sont limités par les opérations disponibles dans le système de réservation, et/ou le développeur peut limiter l'accès de l'agent aux vols uniquement.

**Connaissances** - En dehors des informations fournies par l'environnement, les Agents IA peuvent également récupérer des connaissances provenant d'autres systèmes, services, outils, et même d'autres agents. Dans l'exemple de l'agent de voyage, ces connaissances pourraient inclure les préférences de voyage de l'utilisateur situées dans une base de données client.

### Les différents types d'agents

Maintenant que nous avons une définition générale des Agents IA, examinons quelques types spécifiques d'agents et comment ils pourraient être appliqués à un agent de réservation de voyages.

| **Type d'Agent**              | **Description**                                                                                                                       | **Exemple**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agents Réflexes Simples**   | Réalisent des actions immédiates basées sur des règles prédéfinies.                                                                    | L'agent de voyage interprète le contexte d'un e-mail et transfère les plaintes liées aux voyages au service client.                                                                                                           |
| **Agents Réflexes Basés sur un Modèle** | Réalisent des actions basées sur un modèle du monde et les changements de ce modèle.                                              | L'agent de voyage priorise les itinéraires avec des variations importantes de prix grâce à l'accès à des données historiques sur les prix.                                                                                   |
| **Agents Basés sur des Objectifs** | Créent des plans pour atteindre des objectifs spécifiques en interprétant l'objectif et en déterminant les actions nécessaires pour y parvenir. | L'agent de voyage organise un trajet en déterminant les arrangements nécessaires (voiture, transports publics, vols) pour aller de l'emplacement actuel à la destination.                                                     |
| **Agents Basés sur l'Utilité** | Prennent en compte les préférences et évaluent numériquement les compromis pour déterminer comment atteindre leurs objectifs.           | L'agent de voyage maximise l'utilité en pesant la commodité contre le coût lors de la réservation de voyages.                                                                                                                 |
| **Agents Apprenants**         | S'améliorent au fil du temps en répondant aux retours et en ajustant leurs actions en conséquence.                                     | L'agent de voyage s'améliore en utilisant les retours des clients recueillis via des enquêtes post-voyage pour ajuster les futures réservations.                                                                             |
| **Agents Hiérarchiques**      | Comprennent plusieurs agents dans un système hiérarchisé, où des agents de haut niveau divisent les tâches en sous-tâches pour les agents de niveau inférieur. | L'agent de voyage annule un voyage en décomposant la tâche en sous-tâches (par exemple, annuler des réservations spécifiques) et en demandant à des agents de niveau inférieur de les exécuter, tout en rapportant au niveau supérieur. |
| **Systèmes Multi-Agents (MAS)** | Les agents réalisent des tâches de manière indépendante, soit de façon coopérative, soit de façon compétitive.                        | Coopératif : Plusieurs agents réservent des services de voyage spécifiques comme des hôtels, des vols, et des divertissements. Compétitif : Plusieurs agents gèrent et se disputent un calendrier partagé pour réserver des clients dans un hôtel. |

## Quand Utiliser les Agents IA

Dans la section précédente, nous avons utilisé l'exemple de l'Agent de Voyage pour expliquer comment les différents types d'agents peuvent être utilisés dans diverses situations de réservation. Nous continuerons d'utiliser cette application tout au long du cours.

Examinons maintenant les types de cas d'utilisation pour lesquels les Agents IA sont les mieux adaptés :

![Quand utiliser les Agents IA ?](../../../translated_images/when-to-use-ai-agents.912b9a02e9e0e2af45a3e24faa4e912e334ec23f21f0cf5cb040b7e899b09cd0.fr.png?WT.mc_id=academic-105485-koreyst)

- **Problèmes Ouverts** - permettant au LLM de déterminer les étapes nécessaires pour accomplir une tâche, car elles ne peuvent pas toujours être codées en dur dans un flux de travail.
- **Processus Multi-Étapes** - tâches nécessitant un certain niveau de complexité, où l'Agent IA doit utiliser des outils ou des informations sur plusieurs itérations plutôt que sur une seule récupération.
- **Amélioration au Fil du Temps** - tâches où l'agent peut s'améliorer en recevant des retours de son environnement ou de ses utilisateurs afin de fournir une meilleure utilité.

Nous aborderons plus en détail les considérations relatives à l'utilisation des Agents IA dans la leçon sur la Création d'Agents IA de Confiance.

## Bases des Solutions Agentiques

### Développement d'Agents

La première étape pour concevoir un système d'Agent IA est de définir les outils, actions et comportements. Dans ce cours, nous nous concentrons sur l'utilisation du **service Azure AI Agent** pour définir nos agents. Il propose des fonctionnalités telles que :

- La sélection de modèles ouverts comme OpenAI, Mistral, et Llama
- L'utilisation de données sous licence via des fournisseurs comme Tripadvisor
- L'utilisation d'outils standardisés OpenAPI 3.0

### Modèles Agentiques

La communication avec les LLMs se fait via des prompts. Étant donné la nature semi-autonome des Agents IA, il n'est pas toujours possible ou nécessaire de reformuler manuellement les prompts après un changement dans l'environnement. Nous utilisons des **Modèles Agentiques** qui permettent de formuler des prompts pour le LLM sur plusieurs étapes de manière plus évolutive.

Ce cours est structuré autour de certains des modèles agentiques populaires actuels.

### Cadres Agentiques

Les Cadres Agentiques permettent aux développeurs d'implémenter des modèles agentiques via du code. Ces cadres offrent des modèles, des plugins, et des outils pour une meilleure collaboration entre les Agents IA. Ces avantages incluent une meilleure observabilité et une résolution des problèmes plus efficace pour les systèmes d'Agents IA.

Dans ce cours, nous explorerons le cadre AutoGen basé sur la recherche ainsi que le cadre prêt pour la production proposé par Semantic Kernel.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.