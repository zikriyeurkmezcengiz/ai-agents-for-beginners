# Introduction aux Agents IA et Cas d'Utilisation des Agents

Bienvenue dans le cours "Agents IA pour Débutants" ! Ce cours vous offre des connaissances fondamentales et des exemples pratiques pour créer des solutions avec des Agents IA.

Rejoignez la [Communauté Discord Azure AI](https://discord.gg/kzRShWzttr) pour rencontrer d'autres apprenants, des créateurs d'Agents IA, et poser toutes vos questions sur ce cours.

Pour commencer ce cours, nous allons d'abord mieux comprendre ce que sont les Agents IA et comment nous pouvons les utiliser dans les applications et les flux de travail que nous développons.

## Introduction

Cette leçon couvre :

- Qu'est-ce qu'un Agent IA et quels sont les différents types d'agents ?
- Quels cas d'utilisation conviennent le mieux aux Agents IA et comment peuvent-ils nous aider ?
- Quels sont certains des éléments de base à prendre en compte lors de la conception de solutions "agentiques" ?

## Objectifs d'Apprentissage

Après avoir terminé cette leçon, vous devriez être capable de :

- Comprendre les concepts liés aux Agents IA et leurs différences par rapport à d'autres solutions IA.
- Appliquer les Agents IA de manière efficace.
- Concevoir des solutions "agentiques" productives pour les utilisateurs et les clients.

## Définir les Agents IA et leurs Types

### Qu'est-ce qu'un Agent IA ?

Les Agents IA sont des **systèmes** qui permettent aux **Modèles de Langage Étendu (LLMs)** d’**effectuer des actions** en étendant leurs capacités grâce à l'accès à des **outils** et des **connaissances**.

Décortiquons cette définition en plusieurs parties :

- **Système** - Il est essentiel de considérer les agents non pas comme un simple composant unique, mais comme un système composé de plusieurs éléments. À un niveau basique, les composants d'un Agent IA sont :
  - **Environnement** - L'espace défini où l'Agent IA opère. Par exemple, si nous avions un Agent IA pour la réservation de voyages, l'environnement pourrait être le système de réservation de voyages que l'Agent IA utilise pour accomplir ses tâches.
  - **Capteurs** - Les environnements contiennent des informations et fournissent des retours. Les Agents IA utilisent des capteurs pour collecter et interpréter ces informations sur l'état actuel de l'environnement. Dans l'exemple de l'Agent de Réservation de Voyages, le système de réservation peut fournir des informations comme la disponibilité des hôtels ou les prix des vols.
  - **Actionneurs** - Une fois que l'Agent IA reçoit l'état actuel de l'environnement, il détermine quelle action accomplir pour modifier l'environnement en fonction de la tâche actuelle. Pour l'Agent de Réservation de Voyages, cela pourrait être de réserver une chambre disponible pour l'utilisateur.

![Qu'est-ce qu'un Agent IA ?](../../../translated_images/what-are-ai-agents.png?WT.7f2607783e984be0cfb6dd064ad20389d37cf6d1d28bc5d5a3c648ef353bde89.fr.mc_id=academic-105485-koreyst)

**Modèles de Langage Étendu (LLMs)** - Le concept d'agents existait avant la création des LLMs. L'avantage de construire des Agents IA avec des LLMs réside dans leur capacité à interpréter le langage humain et les données. Cette capacité leur permet d’interpréter les informations environnementales et de définir un plan pour modifier l’environnement.

**Effectuer des Actions** - En dehors des systèmes d'Agents IA, les LLMs sont limités à des situations où l'action consiste à générer du contenu ou des informations basées sur une invite utilisateur. Dans les systèmes d'Agents IA, les LLMs peuvent accomplir des tâches en interprétant la demande de l'utilisateur et en utilisant les outils disponibles dans leur environnement.

**Accès aux Outils** - Les outils auxquels le LLM a accès sont définis par 1) l'environnement dans lequel il opère et 2) le développeur de l'Agent IA. Pour notre exemple d'agent de voyage, les outils de l'agent sont limités par les opérations disponibles dans le système de réservation et/ou le développeur peut restreindre l'accès de l'agent aux outils pour les vols uniquement.

**Connaissances** - En plus des informations fournies par l'environnement, les Agents IA peuvent également récupérer des connaissances provenant d'autres systèmes, services, outils, voire d'autres agents. Dans l'exemple de l'agent de voyage, ces connaissances pourraient inclure les préférences de voyage de l'utilisateur situées dans une base de données client.

### Les différents types d'agents

Maintenant que nous avons une définition générale des Agents IA, examinons quelques types spécifiques d'agents et comment ils pourraient être appliqués à un agent de réservation de voyages.

| **Type d'Agent**              | **Description**                                                                                                                       | **Exemple**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agents Réflexes Simples**   | Effectuent des actions immédiates basées sur des règles prédéfinies.                                                                   | L'agent de voyage interprète le contexte d'un e-mail et transfère les plaintes liées aux voyages au service client.                                                                                                           |
| **Agents Réflexes Basés sur un Modèle** | Effectuent des actions basées sur un modèle du monde et les changements apportés à ce modèle.                                                 | L'agent de voyage priorise les itinéraires avec des changements significatifs de prix en se basant sur l'accès aux données historiques des prix.                                                                             |
| **Agents Basés sur des Objectifs**     | Créent des plans pour atteindre des objectifs spécifiques en interprétant l'objectif et en déterminant les actions nécessaires pour y parvenir. | L'agent de voyage réserve un trajet en déterminant les arrangements nécessaires (voiture, transports publics, vols) pour aller de l'emplacement actuel à la destination.                                                     |
| **Agents Basés sur l'Utilité**        | Prennent en compte les préférences et évaluent les compromis de manière numérique pour déterminer comment atteindre les objectifs.              | L'agent de voyage maximise l'utilité en évaluant la commodité par rapport au coût lors de la réservation de voyages.                                                                                                         |
| **Agents Apprenants**                | S'améliorent avec le temps en répondant aux retours et en ajustant leurs actions en conséquence.                                               | L'agent de voyage s'améliore grâce aux retours des clients issus des enquêtes post-voyage pour ajuster les futures réservations.                                                                                             |
| **Agents Hiérarchiques**             | Incluent plusieurs agents dans un système hiérarchique, où des agents de niveau supérieur décomposent les tâches en sous-tâches pour les agents de niveau inférieur. | L'agent de voyage annule un voyage en divisant la tâche en sous-tâches (par exemple, annuler des réservations spécifiques) et en confiant leur exécution à des agents de niveau inférieur, qui rapportent ensuite au niveau supérieur. |
| **Systèmes Multi-Agents (MAS)**      | Les agents accomplissent des tâches de manière indépendante, soit de façon coopérative, soit compétitive.                                         | Coopératif : Plusieurs agents réservent des services spécifiques comme les hôtels, les vols et les divertissements. Compétitif : Plusieurs agents gèrent et rivalisent sur un calendrier partagé de réservation d'hôtel pour inscrire les clients. |

## Quand Utiliser des Agents IA

Dans la section précédente, nous avons utilisé l'exemple de l'Agent de Voyage pour expliquer comment les différents types d'agents peuvent être utilisés dans divers scénarios de réservation de voyages. Nous continuerons à utiliser cette application tout au long du cours.

Voyons maintenant les types de cas d'utilisation pour lesquels les Agents IA sont les plus adaptés :

![Quand utiliser des Agents IA ?](../../../translated_images/when-to-use-ai-agents.png?WT.1681e3f19611f820ee4331ab494b50ebc6f09b2fb4df3a5f4dac5458316263ad.fr.mc_id=academic-105485-koreyst)

- **Problèmes Ouverts** - Permettre au LLM de déterminer les étapes nécessaires pour accomplir une tâche lorsqu'elles ne peuvent pas toujours être codées en dur dans un flux de travail.
- **Processus Multi-Étapes** - Tâches nécessitant un certain niveau de complexité où l'Agent IA doit utiliser des outils ou des informations sur plusieurs interactions plutôt qu'une récupération en une seule étape.
- **Amélioration au Fil du Temps** - Tâches où l'agent peut s'améliorer au fil du temps en recevant des retours de son environnement ou des utilisateurs pour offrir une meilleure utilité.

Nous abordons davantage les considérations liées à l'utilisation des Agents IA dans la leçon "Construire des Agents IA de Confiance".

## Bases des Solutions Agentiques

### Développement d'Agents

La première étape dans la conception d'un système d'Agent IA est de définir les outils, les actions et les comportements. Dans ce cours, nous nous concentrons sur l'utilisation du **Azure AI Agent Service** pour définir nos Agents. Ce service propose des fonctionnalités telles que :

- La sélection de modèles ouverts comme OpenAI, Mistral et Llama
- L'utilisation de données sous licence via des fournisseurs comme Tripadvisor
- L'utilisation d'outils standardisés OpenAPI 3.0

### Modèles Agentiques

La communication avec les LLMs se fait via des invites. Compte tenu de la nature semi-autonome des Agents IA, il n'est pas toujours possible ou nécessaire de reformuler manuellement l'invite après un changement dans l'environnement. Nous utilisons des **Modèles Agentiques** qui permettent de formuler des invites pour le LLM sur plusieurs étapes de manière plus évolutive.

Ce cours est divisé en plusieurs modèles agentiques populaires actuels.

### Cadres Agentiques

Les Cadres Agentiques permettent aux développeurs d'implémenter des modèles agentiques via du code. Ces cadres offrent des modèles, des plugins et des outils pour une meilleure collaboration entre Agents IA. Ces avantages incluent des capacités accrues pour une meilleure observabilité et un dépannage des systèmes d'Agents IA.

Dans ce cours, nous explorerons le cadre AutoGen basé sur la recherche et le cadre Agent prêt pour la production de Semantic Kernel.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées découlant de l'utilisation de cette traduction.