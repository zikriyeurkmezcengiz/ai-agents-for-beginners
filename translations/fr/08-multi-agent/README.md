```markdown
# Modèles de conception multi-agents

Dès que vous commencez à travailler sur un projet impliquant plusieurs agents, vous devez envisager le modèle de conception multi-agents. Cependant, il peut ne pas être immédiatement évident de savoir quand passer à des multi-agents et quels en sont les avantages.

## Introduction

Dans cette leçon, nous cherchons à répondre aux questions suivantes :

- Quels sont les scénarios où les multi-agents sont applicables ?  
- Quels sont les avantages d'utiliser des multi-agents plutôt qu'un agent unique effectuant plusieurs tâches ?  
- Quels sont les éléments constitutifs pour mettre en œuvre le modèle de conception multi-agents ?  
- Comment avoir une visibilité sur la manière dont les agents interagissent entre eux ?

## Objectifs d'apprentissage

Après cette leçon, vous devriez être capable de :

- Identifier les scénarios où les multi-agents sont applicables.  
- Reconnaître les avantages d'utiliser des multi-agents par rapport à un agent unique.  
- Comprendre les éléments constitutifs pour mettre en œuvre le modèle de conception multi-agents.  

Quelle est la vision globale ?

*Les multi-agents sont un modèle de conception permettant à plusieurs agents de collaborer pour atteindre un objectif commun.*

Ce modèle est largement utilisé dans divers domaines, notamment la robotique, les systèmes autonomes et l'informatique distribuée.

## Scénarios où les multi-agents sont applicables

Alors, quels scénarios sont de bons cas d'utilisation pour les multi-agents ? La réponse est qu'il existe de nombreux scénarios où l'emploi de plusieurs agents est bénéfique, notamment dans les cas suivants :

- **Charges de travail importantes** : Les charges de travail volumineuses peuvent être divisées en tâches plus petites et attribuées à différents agents, permettant un traitement parallèle et une exécution plus rapide. Par exemple, dans le cas d'une tâche importante de traitement de données.
- **Tâches complexes** : Les tâches complexes, comme les charges de travail importantes, peuvent être décomposées en sous-tâches plus petites et attribuées à différents agents, chacun se spécialisant dans un aspect spécifique de la tâche. Un bon exemple est celui des véhicules autonomes où différents agents gèrent la navigation, la détection d'obstacles et la communication avec d'autres véhicules.
- **Expertise diversifiée** : Différents agents peuvent avoir une expertise variée, leur permettant de gérer différents aspects d'une tâche plus efficacement qu'un agent unique. Par exemple, dans le domaine de la santé, des agents peuvent gérer le diagnostic, les plans de traitement et la surveillance des patients.

## Avantages d'utiliser des multi-agents par rapport à un agent unique

Un système à agent unique peut fonctionner correctement pour des tâches simples, mais pour des tâches plus complexes, l'utilisation de plusieurs agents peut offrir plusieurs avantages :

- **Spécialisation** : Chaque agent peut être spécialisé pour une tâche spécifique. Un agent unique manquant de spécialisation risque de se retrouver confus face à une tâche complexe et pourrait, par exemple, effectuer une tâche pour laquelle il n'est pas le mieux adapté.
- **Évolutivité** : Il est plus facile d'évoluer en ajoutant des agents supplémentaires plutôt qu'en surchargeant un agent unique.
- **Tolérance aux pannes** : Si un agent échoue, les autres peuvent continuer à fonctionner, garantissant la fiabilité du système.

Prenons un exemple : réserver un voyage pour un utilisateur. Un système à agent unique devrait gérer tous les aspects du processus de réservation, de la recherche des vols à la réservation des hôtels et des voitures de location. Pour ce faire, cet agent unique devrait disposer d'outils pour gérer toutes ces tâches, ce qui pourrait entraîner un système complexe et monolithique, difficile à maintenir et à faire évoluer. Un système multi-agents, en revanche, pourrait inclure différents agents spécialisés dans la recherche de vols, la réservation d'hôtels et de voitures de location. Cela rendrait le système plus modulaire, plus facile à maintenir et évolutif.

Comparez cela à une agence de voyages gérée comme un commerce familial versus une agence fonctionnant en franchise. Le commerce familial aurait un agent unique gérant tous les aspects du processus de réservation, tandis que la franchise aurait différents agents s'occupant de différents aspects.

## Éléments constitutifs pour mettre en œuvre le modèle de conception multi-agents

Avant de pouvoir mettre en œuvre le modèle de conception multi-agents, vous devez comprendre les éléments constitutifs qui le composent.

Prenons l'exemple concret de la réservation d'un voyage pour un utilisateur. Dans ce cas, les éléments constitutifs incluraient :

- **Communication entre agents** : Les agents chargés de trouver des vols, de réserver des hôtels et des voitures de location doivent communiquer et partager des informations sur les préférences et les contraintes de l'utilisateur. Cela signifie qu'il faut décider des protocoles et des méthodes de communication. Par exemple, l'agent chargé de trouver des vols doit communiquer avec celui chargé de réserver les hôtels pour s'assurer que l'hôtel est réservé aux mêmes dates que le vol.
- **Mécanismes de coordination** : Les agents doivent coordonner leurs actions pour respecter les préférences et les contraintes de l'utilisateur. Par exemple, un utilisateur pourrait préférer un hôtel proche de l'aéroport, tandis qu'une contrainte pourrait être que les voitures de location ne sont disponibles qu'à l'aéroport.
- **Architecture des agents** : Les agents doivent disposer d'une structure interne leur permettant de prendre des décisions et d'apprendre de leurs interactions avec l'utilisateur. Par exemple, l'agent chargé de trouver des vols pourrait utiliser un modèle d'apprentissage automatique pour recommander des vols en fonction des préférences passées de l'utilisateur.
- **Visibilité des interactions multi-agents** : Vous devez avoir une visibilité sur la manière dont les agents interagissent entre eux. Cela implique d'avoir des outils et techniques pour suivre les activités et interactions des agents, comme des outils de journalisation, de visualisation et des métriques de performance.
- **Modèles multi-agents** : Il existe différents modèles pour mettre en œuvre des systèmes multi-agents, tels que des architectures centralisées, décentralisées ou hybrides. Vous devez choisir le modèle qui convient le mieux à votre cas d'utilisation.
- **Humain dans la boucle** : Dans la plupart des cas, un humain interviendra à certains moments, et vous devez instruire les agents sur le moment où demander une intervention humaine. Par exemple, un utilisateur pourrait demander un hôtel ou un vol spécifique que les agents n'ont pas recommandé ou demander une confirmation avant de réserver.

## Visibilité des interactions multi-agents

Il est crucial d'avoir une visibilité sur la manière dont les agents interagissent entre eux. Cette visibilité est essentielle pour déboguer, optimiser et garantir l'efficacité globale du système. Pour cela, vous devez disposer d'outils et de techniques pour suivre les activités et interactions des agents.

Par exemple, dans le cas de la réservation d'un voyage, vous pourriez avoir un tableau de bord affichant l'état de chaque agent, les préférences et contraintes de l'utilisateur, ainsi que les interactions entre les agents. Ce tableau de bord pourrait montrer les dates de voyage de l'utilisateur, les vols recommandés par l'agent de vol, les hôtels recommandés par l'agent hôtelier et les voitures de location recommandées par l'agent de location. Cela vous donnerait une vue claire de la manière dont les agents interagissent et si les préférences et contraintes de l'utilisateur sont respectées.

Regardons chaque aspect plus en détail :

- **Outils de journalisation et de surveillance** : Vous voulez consigner chaque action effectuée par un agent. Une entrée de journal pourrait contenir des informations sur l'agent ayant pris l'action, l'action elle-même, l'heure et le résultat de l'action.
- **Outils de visualisation** : Ces outils permettent de voir les interactions entre agents de manière plus intuitive. Par exemple, vous pourriez avoir un graphique montrant le flux d'informations entre les agents.
- **Métriques de performance** : Les métriques de performance permettent de suivre l'efficacité du système multi-agents, comme le temps nécessaire pour accomplir une tâche, le nombre de tâches effectuées par unité de temps ou encore la précision des recommandations faites par les agents.

## Modèles multi-agents

Explorons quelques modèles concrets pour créer des applications multi-agents. Voici quelques modèles intéressants à considérer :

### Chat de groupe

Ce modèle est utile pour créer une application de chat de groupe où plusieurs agents peuvent communiquer entre eux. Les cas d'utilisation typiques incluent la collaboration en équipe, le support client et les réseaux sociaux.

Dans ce modèle, chaque agent représente un utilisateur dans le chat de groupe, et les messages sont échangés entre les agents via un protocole de messagerie. Les agents peuvent envoyer des messages au groupe, recevoir des messages du groupe et répondre à d'autres agents.

Ce modèle peut être mis en œuvre à l'aide d'une architecture centralisée où tous les messages transitent par un serveur central, ou d'une architecture décentralisée où les messages sont échangés directement.

![Chat de groupe](../../../translated_images/multi-agent-group-chat.82d537c5c8dc833abbd252033e60874bc9d00df7193888b3377f8426449a0b20.fr.png)

### Passation de tâche

Ce modèle est utile pour créer une application où plusieurs agents peuvent se transmettre des tâches.

Les cas d'utilisation typiques incluent le support client, la gestion des tâches et l'automatisation des flux de travail.

Dans ce modèle, chaque agent représente une tâche ou une étape dans un flux de travail, et les agents peuvent se transmettre des tâches en fonction de règles prédéfinies.

![Passation de tâche](../../../translated_images/multi-agent-hand-off.ed4f0a5a58614a8a3e962fc476187e630a3ba309d066e460f017b503d0b84cfc.fr.png)

### Filtrage collaboratif

Ce modèle est utile pour créer une application où plusieurs agents peuvent collaborer pour faire des recommandations aux utilisateurs.

Pourquoi faire collaborer plusieurs agents ? Parce que chaque agent peut avoir une expertise différente et contribuer au processus de recommandation de manière unique.

Prenons l'exemple d'un utilisateur cherchant une recommandation sur la meilleure action à acheter en bourse :

- **Expert du secteur** : Un agent pourrait être expert dans un secteur spécifique.  
- **Analyse technique** : Un autre agent pourrait être expert en analyse technique.  
- **Analyse fondamentale** : Un autre agent pourrait être expert en analyse fondamentale. En collaborant, ces agents peuvent fournir une recommandation plus complète à l'utilisateur.

![Recommandation](../../../translated_images/multi-agent-filtering.719217d169391ddb118bbb726b19d4d89ee139f960f8749ccb2400efb4d0ce79.fr.png)

## Scénario : Processus de remboursement

Considérons un scénario où un client cherche à obtenir un remboursement pour un produit. Plusieurs agents peuvent être impliqués dans ce processus, mais nous allons les diviser entre agents spécifiques au processus et agents généraux pouvant être utilisés ailleurs.

**Agents spécifiques au processus de remboursement** :

Voici quelques agents pouvant être impliqués dans le processus de remboursement :

- **Agent client** : Représente le client et est responsable de l'initiation du processus de remboursement.  
- **Agent vendeur** : Représente le vendeur et est responsable du traitement du remboursement.  
- **Agent de paiement** : Représente le processus de paiement et est responsable du remboursement du paiement au client.  
- **Agent de résolution** : Représente le processus de résolution et est responsable de résoudre tout problème survenant durant le processus de remboursement.  
- **Agent de conformité** : Représente le processus de conformité et est responsable de garantir que le processus respecte les réglementations et politiques.

**Agents généraux** :

Ces agents peuvent être utilisés dans d'autres parties de votre entreprise :

- **Agent d'expédition** : Responsable de l'expédition du produit au vendeur. Peut être utilisé pour les remboursements ou pour l'expédition générale lors d'un achat.  
- **Agent de retour d'information** : Collecte les retours d'expérience du client. Peut être sollicité à tout moment, pas seulement lors d'un remboursement.  
- **Agent d'escalade** : Gère l'escalade des problèmes à un niveau supérieur de support. Peut être utilisé pour tout processus nécessitant une escalade.  
- **Agent de notification** : Envoie des notifications au client à différentes étapes du processus de remboursement.  
- **Agent d'analyse** : Analyse les données relatives au processus de remboursement.  
- **Agent d'audit** : Vérifie que le processus de remboursement est correctement exécuté.  
- **Agent de reporting** : Génère des rapports sur le processus de remboursement.  
- **Agent de connaissances** : Maintient une base de connaissances sur les remboursements et d'autres processus de l'entreprise.  
- **Agent de sécurité** : Assure la sécurité du processus de remboursement.  
- **Agent de qualité** : Veille à la qualité du processus de remboursement.

Avec cette liste d'agents, à la fois spécifiques et généraux, vous devriez avoir une idée de comment structurer les agents dans un système multi-agents.

## Exercice

Quel serait un bon exercice pour cette leçon ?

Concevez un système multi-agents pour un processus de support client. Identifiez les agents impliqués, leurs rôles et responsabilités, et comment ils interagissent entre eux. Prenez en compte à la fois les agents spécifiques au support client et les agents généraux pouvant être utilisés ailleurs dans votre entreprise.

> Réfléchissez avant de lire la solution ci-dessous, vous pourriez avoir besoin de plus d'agents que prévu.

> TIP : Pensez aux différentes étapes du processus de support client ainsi qu'aux agents nécessaires pour tout système.

## Solution

[Solution](./solution/solution.md)

## Vérifications des connaissances

Question : Quand devriez-vous envisager d'utiliser des multi-agents ?

- [] A1 : Lorsque vous avez une charge de travail réduite et une tâche simple.  
- [] A2 : Lorsque vous avez une charge de travail importante.  
- [] A3 : Lorsque vous avez une tâche simple.

[Solution quiz](./solution/solution-quiz.md)

## Résumé

Dans cette leçon, nous avons exploré le modèle de conception multi-agents, y compris les scénarios où les multi-agents sont applicables, les avantages d'utiliser des multi-agents par rapport à un agent unique, les éléments constitutifs pour mettre en œuvre le modèle de conception multi-agents, et comment avoir une visibilité sur la manière dont les agents interagissent entre eux.

## Ressources supplémentaires

- [Autogen design patterns](https://microsoft.github.io/autogen/0.4.0.dev4/user-guide/core-user-guide/design-patterns/index.html)  
- [Agentic design patterns](https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/)
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées découlant de l'utilisation de cette traduction.