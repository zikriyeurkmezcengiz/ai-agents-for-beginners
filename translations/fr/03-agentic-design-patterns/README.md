```markdown
# Principes de Conception Agentique pour l'IA

## Introduction

Il existe de nombreuses façons d’envisager la construction de systèmes d’IA agentiques. Étant donné que l’ambiguïté est une caractéristique, et non un défaut, dans la conception de l’IA générative, il est parfois difficile pour les ingénieurs de savoir par où commencer. Nous avons créé un ensemble de principes de conception UX centrés sur l’humain pour permettre aux développeurs de concevoir des systèmes agentiques centrés sur le client afin de répondre à leurs besoins commerciaux. Ces principes de conception ne constituent pas une architecture prescriptive, mais plutôt un point de départ pour les équipes qui définissent et développent des expériences avec des agents.

En général, les agents doivent :

- Élargir et amplifier les capacités humaines (brainstorming, résolution de problèmes, automatisation, etc.)
- Combler les lacunes en matière de connaissances (me mettre à jour sur des domaines de connaissances, traduction, etc.)
- Faciliter et soutenir la collaboration de manière à respecter nos préférences individuelles pour travailler avec les autres
- Faire de nous des versions améliorées de nous-mêmes (par exemple, coach de vie/gestionnaire de tâches, nous aider à apprendre des compétences de régulation émotionnelle et de pleine conscience, développer la résilience, etc.)

## Ce que cette leçon couvrira

- Quels sont les Principes de Conception Agentique
- Quelles sont les lignes directrices à suivre lors de la mise en œuvre de ces principes de conception
- Quels sont quelques exemples d’utilisation de ces principes de conception

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous serez capable de :

1. Expliquer ce que sont les Principes de Conception Agentique
2. Expliquer les lignes directrices pour utiliser les Principes de Conception Agentique
3. Comprendre comment concevoir un agent en utilisant les Principes de Conception Agentique

## Les Principes de Conception Agentique

![Principes de Conception Agentique](../../../translated_images/agentic-design-principles.png?WT.19d6373397ba872c62b9237a927d1261a67e21e7c8e83274e53494a65e520a08.fr.mc_id=academic-105485-koreyst)

### Agent (Espace)

C’est l’environnement dans lequel l’agent opère. Ces principes guident la manière dont nous concevons les agents pour interagir dans les mondes physiques et numériques.

- **Connecter, pas isoler** – aider à connecter les gens à d’autres personnes, événements et connaissances exploitables pour permettre la collaboration et la connexion.
  - Les agents aident à relier les événements, les connaissances et les personnes.
  - Les agents rapprochent les gens. Ils ne sont pas conçus pour remplacer ou dévaloriser les humains.
- **Facilement accessible mais parfois invisible** – l’agent fonctionne en grande partie en arrière-plan et n’intervient que lorsque cela est pertinent et approprié.
  - L’agent est facilement accessible et disponible pour les utilisateurs autorisés sur n’importe quel appareil ou plateforme.
  - L’agent prend en charge les entrées et sorties multimodales (son, voix, texte, etc.).
  - L’agent peut passer de manière fluide entre premier plan et arrière-plan, entre proactif et réactif, en fonction de la perception des besoins de l’utilisateur.
  - L’agent peut fonctionner sous une forme invisible, mais son chemin de traitement en arrière-plan et sa collaboration avec d’autres agents restent transparents et contrôlables par l’utilisateur.

### Agent (Temps)

Cela concerne la manière dont l’agent opère dans le temps. Ces principes guident la conception des agents qui interagissent à travers le passé, le présent et le futur.

- **Passé** : Réflexion sur l’historique, qui inclut à la fois l’état et le contexte.
  - L’agent fournit des résultats plus pertinents en s’appuyant sur une analyse de données historiques plus riches, au-delà des simples événements, personnes ou états.
  - L’agent crée des connexions à partir d’événements passés et réfléchit activement à sa mémoire pour interagir avec les situations actuelles.
- **Présent** : Inciter plus que notifier.
  - L’agent adopte une approche globale pour interagir avec les personnes. Lorsqu’un événement se produit, il va au-delà de la simple notification statique ou autre formalité. Il peut simplifier les flux ou générer dynamiquement des indices pour attirer l’attention de l’utilisateur au bon moment.
  - L’agent fournit des informations en fonction du contexte environnemental, des changements sociaux et culturels, et adaptées à l’intention de l’utilisateur.
  - Les interactions avec l’agent peuvent évoluer progressivement, gagnant en complexité pour autonomiser les utilisateurs sur le long terme.
- **Futur** : S’adapter et évoluer.
  - L’agent s’adapte à divers appareils, plateformes et modalités.
  - L’agent s’ajuste au comportement des utilisateurs, à leurs besoins en matière d’accessibilité, et est entièrement personnalisable.
  - L’agent se façonne et évolue grâce à une interaction continue avec les utilisateurs.

### Agent (Noyau)

Ce sont les éléments clés au cœur de la conception d’un agent.

- **Accepter l’incertitude tout en établissant la confiance**.
  - Un certain niveau d’incertitude de l’agent est attendu. L’incertitude est un élément clé de la conception des agents.
  - La confiance et la transparence sont des fondements essentiels de la conception des agents.
  - Les humains ont le contrôle sur l’activation/désactivation de l’agent, et le statut de l’agent est toujours clairement visible.

## Lignes directrices pour mettre en œuvre ces principes

Lorsque vous appliquez les principes de conception ci-dessus, suivez ces lignes directrices :

1. **Transparence** : Informez l’utilisateur que l’IA est impliquée, expliquez son fonctionnement (y compris ses actions passées), et indiquez comment fournir des retours ou modifier le système.
2. **Contrôle** : Permettez à l’utilisateur de personnaliser, spécifier ses préférences, et avoir le contrôle sur le système et ses attributs (y compris la possibilité d’oublier).
3. **Cohérence** : Visez des expériences cohérentes et multimodales sur tous les appareils et points d’accès. Utilisez des éléments d’interface utilisateur/expérience utilisateur familiers lorsque c’est possible (par exemple, une icône de microphone pour l’interaction vocale) et réduisez autant que possible la charge cognitive de l’utilisateur (par exemple, optez pour des réponses concises, des aides visuelles et du contenu « En savoir plus »).

## Comment concevoir un agent de voyage en utilisant ces principes et lignes directrices

Imaginez que vous concevez un agent de voyage. Voici comment vous pourriez appliquer les Principes de Conception et les Lignes Directrices :

1. **Transparence** – Informez l’utilisateur que l’agent de voyage est alimenté par une IA. Fournissez des instructions de base pour commencer (par exemple, un message de bienvenue, des exemples de requêtes). Documentez cela clairement sur la page produit. Affichez la liste des requêtes posées par l’utilisateur dans le passé. Expliquez clairement comment donner des retours (pouces en l’air ou en bas, bouton « Envoyer un retour », etc.). Indiquez clairement si l’agent a des restrictions d’utilisation ou de sujet.
2. **Contrôle** – Assurez-vous qu’il est clair pour l’utilisateur comment modifier l’agent après sa création, par exemple avec des invites système. Permettez à l’utilisateur de choisir le niveau de détail des réponses de l’agent, son style d’écriture, et de définir des sujets à éviter. Autorisez l’utilisateur à consulter et supprimer les fichiers ou données associés, les requêtes et les conversations passées.
3. **Cohérence** – Assurez-vous que les icônes pour partager une requête, ajouter un fichier ou une photo, et taguer quelqu’un ou quelque chose sont standard et reconnaissables. Utilisez l’icône de trombone pour indiquer le téléversement/partage de fichiers avec l’agent, et une icône d’image pour indiquer le téléversement de graphiques.

## Ressources supplémentaires
- [Practices for Governing Agentic AI Systems | OpenAI](https://openai.com)
- [The HAX Toolkit Project - Microsoft Research](https://microsoft.com)
- [Responsible AI Toolbox](https://responsibleaitoolbox.ai)
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.