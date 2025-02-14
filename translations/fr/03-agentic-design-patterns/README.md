# Principes de Conception Agentique pour l'IA

## Introduction

Il existe de nombreuses façons d'aborder la création de systèmes d'IA agentique. Étant donné que l'ambiguïté est une caractéristique inhérente et non un défaut dans la conception de l'IA générative, il est parfois difficile pour les ingénieurs de savoir par où commencer. Nous avons élaboré un ensemble de principes de conception UX centrés sur l'humain pour permettre aux développeurs de créer des systèmes agentiques centrés sur les utilisateurs, répondant à leurs besoins professionnels. Ces principes de conception ne constituent pas une architecture prescriptive, mais plutôt un point de départ pour les équipes qui définissent et construisent des expériences d'agents.

En général, les agents devraient :

- Élargir et amplifier les capacités humaines (brainstorming, résolution de problèmes, automatisation, etc.)
- Combler les lacunes en matière de connaissances (me mettre à jour sur des domaines de connaissance, traduction, etc.)
- Faciliter et soutenir la collaboration en respectant les préférences individuelles pour travailler avec d'autres
- Nous rendre meilleurs (par exemple, coach de vie/gestionnaire de tâches, nous aider à apprendre la régulation émotionnelle et des compétences de pleine conscience, renforcer la résilience, etc.)

## Cette Leçon Couvre

- Quels sont les Principes de Conception Agentique
- Quelles sont les directives à suivre pour mettre en œuvre ces principes de conception
- Quels sont des exemples d'utilisation de ces principes de conception

## Objectifs d'Apprentissage

Après avoir terminé cette leçon, vous serez en mesure de :

1. Expliquer ce que sont les Principes de Conception Agentique
2. Expliquer les directives pour utiliser les Principes de Conception Agentique
3. Comprendre comment construire un agent en utilisant les Principes de Conception Agentique

## Les Principes de Conception Agentique

![Principes de Conception Agentique](../../../translated_images/agentic-design-principles.png?WT.19d6373397ba872c62b9237a927d1261a67e21e7c8e83274e53494a65e520a08.fr.mc_id=academic-105485-koreyst)

### Agent (Espace)

C'est l'environnement dans lequel l'agent opère. Ces principes guident la manière dont nous concevons les agents pour interagir dans des mondes physiques et numériques.

- **Connecter, pas isoler** – aider à connecter les personnes à d'autres personnes, événements et connaissances exploitables pour favoriser la collaboration et le lien.
  - Les agents aident à relier événements, connaissances et individus.
  - Les agents rapprochent les gens. Ils ne sont pas conçus pour remplacer ou minimiser les individus.
- **Facilement accessible mais parfois invisible** – l'agent opère principalement en arrière-plan et n'intervient que lorsqu'il est pertinent et approprié.
  - L'agent est facilement accessible et repérable par les utilisateurs autorisés sur n'importe quel appareil ou plateforme.
  - L'agent prend en charge des entrées et sorties multimodales (son, voix, texte, etc.).
  - L'agent peut passer de manière fluide de l'avant-plan à l'arrière-plan ; de proactif à réactif, en fonction de son évaluation des besoins de l'utilisateur.
  - L'agent peut fonctionner de manière invisible, mais son processus en arrière-plan et sa collaboration avec d'autres agents sont transparents et contrôlables par l'utilisateur.

### Agent (Temps)

C'est ainsi que l'agent fonctionne au fil du temps. Ces principes guident la manière dont nous concevons les agents interagissant à travers le passé, le présent et le futur.

- **Passé** : Réfléchir à l'historique incluant état et contexte.
  - L'agent fournit des résultats plus pertinents grâce à l'analyse de données historiques plus riches au-delà de l'événement, des personnes ou des états.
  - L'agent établit des connexions à partir d'événements passés et réfléchit activement à sa mémoire pour interagir avec les situations actuelles.
- **Présent** : Encourager plutôt que notifier.
  - L'agent adopte une approche globale pour interagir avec les personnes. Lorsqu'un événement se produit, il va au-delà de la notification statique ou d'autres formalités statiques. Il peut simplifier les flux ou générer des indices dynamiques pour attirer l'attention de l'utilisateur au bon moment.
  - L'agent délivre des informations en fonction du contexte, des changements sociaux et culturels, et adaptées aux intentions de l'utilisateur.
  - L'interaction avec l'agent peut être progressive, évoluant en complexité pour autonomiser les utilisateurs sur le long terme.
- **Futur** : S'adapter et évoluer.
  - L'agent s'adapte à divers appareils, plateformes et modalités.
  - L'agent s'adapte au comportement de l'utilisateur, aux besoins d'accessibilité, et est librement personnalisable.
  - L'agent se façonne et évolue grâce à une interaction continue avec l'utilisateur.

### Agent (Noyau)

Ce sont les éléments clés au cœur de la conception d'un agent.

- **Accepter l'incertitude mais établir la confiance**.
  - Un certain niveau d'incertitude de l'agent est attendu. L'incertitude est un élément clé de la conception des agents.
  - La confiance et la transparence sont des couches fondamentales dans la conception des agents.
  - Les humains contrôlent quand l'agent est activé/désactivé, et le statut de l'agent est clairement visible à tout moment.

## Les Directives Pour Mettre en Œuvre Ces Principes

Lorsque vous utilisez les principes de conception ci-dessus, suivez les directives suivantes :

1. **Transparence** : Informez l'utilisateur que l'IA est impliquée, comment elle fonctionne (y compris ses actions passées), et comment donner des retours et modifier le système.
2. **Contrôle** : Permettez à l'utilisateur de personnaliser, spécifier ses préférences et personnaliser, et d'avoir le contrôle sur le système et ses attributs (y compris la possibilité d'oublier).
3. **Cohérence** : Visez des expériences cohérentes et multimodales sur tous les appareils et points d'accès. Utilisez des éléments d'interface utilisateur/UX familiers lorsque cela est possible (par exemple, une icône de microphone pour l'interaction vocale) et réduisez autant que possible la charge cognitive de l'utilisateur (par exemple, privilégiez des réponses concises, des aides visuelles et du contenu « En savoir plus »).

## Comment Concevoir un Agent de Voyage en Utilisant Ces Principes et Directives

Imaginez que vous concevez un Agent de Voyage, voici comment vous pourriez envisager d'utiliser les Principes de Conception et les Directives :

1. **Transparence** – Informez l'utilisateur que l'Agent de Voyage est un agent activé par l'IA. Fournissez des instructions de base pour démarrer (par exemple, un message de « Bonjour », des exemples de requêtes). Documentez cela clairement sur la page produit. Montrez la liste des requêtes posées par l'utilisateur dans le passé. Expliquez clairement comment donner des retours (pouce levé et baissé, bouton « Envoyer un retour », etc.). Indiquez clairement si l'agent a des restrictions d'utilisation ou de sujet.
2. **Contrôle** – Assurez-vous qu'il est clair comment l'utilisateur peut modifier l'agent après sa création, par exemple avec des invites système. Permettez à l'utilisateur de choisir le niveau de détail de l'agent, son style d'écriture, et toute restriction sur ce dont l'agent ne doit pas parler. Autorisez l'utilisateur à consulter et supprimer tout fichier ou donnée associé(e), les requêtes et les conversations passées.
3. **Cohérence** – Assurez-vous que les icônes pour Partager une Requête, ajouter un fichier ou une photo, et taguer quelqu'un ou quelque chose sont standards et reconnaissables. Utilisez l'icône de trombone pour indiquer le téléversement/partage de fichier avec l'agent, et une icône d'image pour indiquer le téléversement de graphiques.

## Ressources Supplémentaires
- [Practices for Governing Agentic AI Systems | OpenAI](https://openai.com)
- [The HAX Toolkit Project - Microsoft Research](https://microsoft.com)
- [Responsible AI Toolbox](https://responsibleaitoolbox.ai)
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées découlant de l'utilisation de cette traduction.