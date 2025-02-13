```markdown
# Agentic RAG

Cette leçon offre une vue d'ensemble complète de l'Agentic Retrieval-Augmented Generation (Agentic RAG), un paradigme émergent en intelligence artificielle où les modèles de langage de grande taille (LLMs) planifient de manière autonome leurs prochaines étapes tout en extrayant des informations à partir de sources externes. Contrairement aux schémas statiques de type "recherche puis lecture", l'Agentic RAG implique des appels itératifs au LLM, entrecoupés d'appels à des outils ou fonctions et de productions structurées. Le système évalue les résultats, affine les requêtes, invoque des outils supplémentaires si nécessaire, et poursuit ce cycle jusqu'à obtenir une solution satisfaisante.

## Introduction

Cette leçon abordera :

- **Comprendre l'Agentic RAG :** Découvrir ce paradigme émergent en IA où les modèles de langage de grande taille (LLMs) planifient de manière autonome leurs prochaines étapes tout en extrayant des données de sources externes.
- **Maîtriser le style itératif Maker-Checker :** Comprendre la boucle d'appels itératifs au LLM, entrecoupés d'appels à des outils ou fonctions et de productions structurées, conçue pour améliorer la précision et gérer les requêtes mal formées.
- **Explorer des applications pratiques :** Identifier les scénarios où l'Agentic RAG excelle, tels que les environnements axés sur la précision, les interactions complexes avec des bases de données et les flux de travail prolongés.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez/comment :

- **Comprendre l'Agentic RAG :** Découvrir ce paradigme émergent en IA où les modèles de langage de grande taille (LLMs) planifient de manière autonome leurs prochaines étapes tout en extrayant des données de sources externes.
- **Style itératif Maker-Checker :** Assimiler le concept d'une boucle d'appels itératifs au LLM, entrecoupés d'appels à des outils ou fonctions et de productions structurées, conçue pour améliorer la précision et gérer les requêtes mal formées.
- **Prendre en charge le processus de raisonnement :** Comprendre la capacité du système à prendre en charge son processus de raisonnement, en décidant de la manière d'aborder les problèmes sans s'appuyer sur des chemins prédéfinis.
- **Flux de travail :** Comprendre comment un modèle agentique décide de manière autonome d'extraire des rapports sur les tendances du marché, d'identifier des données concurrentielles, de corréler des métriques de vente internes, de synthétiser les conclusions et d'évaluer la stratégie.
- **Boucles itératives, intégration d'outils et mémoire :** Découvrir comment le système repose sur un modèle d'interaction en boucle, en maintenant l'état et la mémoire au fil des étapes pour éviter les boucles répétitives et prendre des décisions éclairées.
- **Gérer les modes d'échec et l'auto-correction :** Explorer les mécanismes robustes d'auto-correction du système, y compris l'itération et la reconsidération, l'utilisation d'outils de diagnostic et le recours à une supervision humaine si nécessaire.
- **Limites de l'autonomie :** Comprendre les limites de l'Agentic RAG, en mettant l'accent sur l'autonomie spécifique au domaine, la dépendance à l'infrastructure et le respect des garde-fous.
- **Cas d'utilisation pratiques et valeur :** Identifier les scénarios où l'Agentic RAG excelle, tels que les environnements axés sur la précision, les interactions complexes avec des bases de données et les flux de travail prolongés.
- **Gouvernance, transparence et confiance :** Découvrir l'importance de la gouvernance et de la transparence, y compris le raisonnement explicable, le contrôle des biais et la supervision humaine.

## Qu'est-ce que l'Agentic RAG ?

L'Agentic Retrieval-Augmented Generation (Agentic RAG) est un paradigme émergent en intelligence artificielle où les modèles de langage de grande taille (LLMs) planifient de manière autonome leurs prochaines étapes tout en extrayant des informations à partir de sources externes. Contrairement aux schémas statiques de type "recherche puis lecture", l'Agentic RAG implique des appels itératifs au LLM, entrecoupés d'appels à des outils ou fonctions et de productions structurées. Le système évalue les résultats, affine les requêtes, invoque des outils supplémentaires si nécessaire, et poursuit ce cycle jusqu'à obtenir une solution satisfaisante. Ce style itératif "maker-checker" améliore la précision, gère les requêtes mal formées et garantit des résultats de haute qualité.

Le système prend activement en charge son processus de raisonnement, réécrit les requêtes échouées, choisit différentes méthodes de recherche et intègre plusieurs outils—tels que la recherche vectorielle dans Azure AI Search, des bases de données SQL ou des API personnalisées—avant de finaliser sa réponse. La qualité distinctive d'un système agentique est sa capacité à prendre en charge son processus de raisonnement. Les implémentations traditionnelles de RAG reposent sur des chemins prédéfinis, mais un système agentique détermine de manière autonome la séquence des étapes en fonction de la qualité des informations qu'il trouve.

## Définir l'Agentic Retrieval-Augmented Generation (Agentic RAG)

L'Agentic Retrieval-Augmented Generation (Agentic RAG) est un paradigme émergent dans le développement de l'IA où les LLMs ne se contentent pas d'extraire des informations de sources de données externes, mais planifient également leurs prochaines étapes de manière autonome. Contrairement aux schémas statiques de type "recherche puis lecture" ou aux séquences de prompts soigneusement scriptées, l'Agentic RAG repose sur une boucle d'appels itératifs au LLM, entrecoupés d'appels à des outils ou fonctions et de productions structurées. À chaque étape, le système évalue les résultats obtenus, décide de raffiner ses requêtes, invoque des outils supplémentaires si nécessaire, et poursuit ce cycle jusqu'à atteindre une solution satisfaisante.

Ce style itératif "maker-checker" est conçu pour améliorer la précision, gérer les requêtes mal formées aux bases de données structurées (par exemple, NL2SQL), et garantir des résultats équilibrés et de haute qualité. Plutôt que de s'appuyer uniquement sur des chaînes de prompts soigneusement conçues, le système prend activement en charge son processus de raisonnement. Il peut réécrire des requêtes échouées, choisir différentes méthodes de recherche et intégrer plusieurs outils—tels que la recherche vectorielle dans Azure AI Search, des bases de données SQL ou des API personnalisées—avant de finaliser sa réponse. Cela élimine le besoin de cadres d'orchestration excessivement complexes. À la place, une boucle relativement simple de "appel LLM → utilisation d'outil → appel LLM → …" peut produire des résultats sophistiqués et bien fondés.

![Agentic RAG Core Loop](../../../05-agentic-rag/images/agentic-rag-core-loop.png)

## Prendre en charge le processus de raisonnement

La qualité distinctive qui rend un système "agentique" est sa capacité à prendre en charge son processus de raisonnement. Les implémentations traditionnelles de RAG dépendent souvent de chemins prédéfinis par des humains pour le modèle : une chaîne de raisonnement qui décrit quoi récupérer et quand. Mais lorsqu'un système est véritablement agentique, il décide en interne de la manière d'aborder le problème. Il ne fait pas qu'exécuter un script ; il détermine de manière autonome la séquence des étapes en fonction de la qualité des informations qu'il trouve.

Par exemple, s'il est demandé de créer une stratégie de lancement de produit, il ne se contente pas de s'appuyer sur un prompt décrivant tout le flux de travail de recherche et de prise de décision. Au lieu de cela, le modèle agentique décide de manière autonome de :

1. Récupérer des rapports sur les tendances actuelles du marché à l'aide de Bing Web Grounding.
2. Identifier des données pertinentes sur les concurrents à l'aide d'Azure AI Search.
3. Corréler des métriques historiques de ventes internes à l'aide d'Azure SQL Database.
4. Synthétiser les conclusions en une stratégie cohérente orchestrée via Azure OpenAI Service.
5. Évaluer la stratégie pour détecter des lacunes ou incohérences, ce qui peut entraîner une nouvelle série de recherches si nécessaire.

Toutes ces étapes—affiner les requêtes, choisir les sources, itérer jusqu'à être "satisfait" de la réponse—sont décidées par le modèle, et non pré-scriptées par un humain.

## Boucles itératives, intégration d'outils et mémoire

![Tool Integration Architecture](../../../05-agentic-rag/images/tool-integration.png)

Un système agentique repose sur un modèle d'interaction en boucle :

- **Appel initial :** L'objectif de l'utilisateur (alias le prompt utilisateur) est présenté au LLM.
- **Invocation d'outils :** Si le modèle identifie des informations manquantes ou des instructions ambiguës, il sélectionne un outil ou une méthode de recherche—comme une requête dans une base de données vectorielle (par exemple, Azure AI Search Hybrid search sur des données privées) ou un appel structuré SQL—pour recueillir plus de contexte.
- **Évaluation et raffinement :** Après avoir examiné les données retournées, le modèle décide si les informations sont suffisantes. Sinon, il affine la requête, essaie un outil différent ou ajuste son approche.
- **Répétition jusqu'à satisfaction :** Ce cycle continue jusqu'à ce que le modèle détermine qu'il dispose de suffisamment de clarté et d'éléments probants pour fournir une réponse finale bien raisonnée.
- **Mémoire et état :** Comme le système maintient l'état et la mémoire au fil des étapes, il peut se souvenir des tentatives précédentes et de leurs résultats, évitant les boucles répétitives et prenant des décisions plus éclairées au fur et à mesure.

Au fil du temps, cela crée une impression de compréhension évolutive, permettant au modèle de naviguer dans des tâches complexes et multi-étapes sans qu'un humain ait besoin d'intervenir constamment ou de reformuler le prompt.

## Gérer les modes d'échec et l'auto-correction

L'autonomie de l'Agentic RAG comprend également des mécanismes robustes d'auto-correction. Lorsque le système atteint des impasses—comme récupérer des documents non pertinents ou rencontrer des requêtes mal formées—il peut :

- **Itérer et reconsidérer :** Au lieu de fournir des réponses peu utiles, le modèle tente de nouvelles stratégies de recherche, réécrit des requêtes pour les bases de données ou explore des ensembles de données alternatifs.
- **Utiliser des outils de diagnostic :** Le système peut invoquer des fonctions supplémentaires conçues pour l'aider à déboguer ses étapes de raisonnement ou confirmer l'exactitude des données récupérées. Des outils comme Azure AI Tracing seront importants pour permettre une observabilité et une surveillance robustes.
- **Recourir à une supervision humaine :** Pour des scénarios critiques ou des échecs répétés, le modèle peut signaler une incertitude et demander une orientation humaine. Une fois que l'humain fournit un retour correctif, le modèle peut intégrer cette leçon pour l'avenir.

Cette approche itérative et dynamique permet au modèle de s'améliorer continuellement, garantissant qu'il ne s'agit pas seulement d'un système "one-shot", mais d'un système qui apprend de ses erreurs au cours d'une session donnée.

![Self Correction Mechanism](../../../05-agentic-rag/images/self-correction.png)

## Limites de l'autonomie

Malgré son autonomie dans une tâche, l'Agentic RAG n'est pas synonyme d'intelligence artificielle générale. Ses capacités "agentiques" sont limitées aux outils, sources de données et politiques fournies par les développeurs humains. Il ne peut pas inventer ses propres outils ou sortir des limites du domaine qui lui ont été fixées. Il excelle plutôt à orchestrer dynamiquement les ressources disponibles.

Les principales différences avec des formes d'IA plus avancées incluent :

1. **Autonomie spécifique au domaine :** Les systèmes Agentic RAG se concentrent sur l'atteinte d'objectifs définis par l'utilisateur dans un domaine connu, en employant des stratégies comme la réécriture de requêtes ou la sélection d'outils pour améliorer les résultats.
2. **Dépendance à l'infrastructure :** Les capacités du système dépendent des outils et des données intégrés par les développeurs. Il ne peut pas dépasser ces limites sans intervention humaine.
3. **Respect des garde-fous :** Les directives éthiques, les règles de conformité et les politiques d'entreprise restent très importantes. La liberté de l'agent est toujours contrainte par des mesures de sécurité et des mécanismes de supervision (du moins, espérons-le).

## Cas d'utilisation pratiques et valeur

L'Agentic RAG excelle dans les scénarios nécessitant un raffinement itératif et une grande précision :

1. **Environnements axés sur la précision :** Dans les vérifications de conformité, les analyses réglementaires ou les recherches juridiques, le modèle agentique peut vérifier les faits à plusieurs reprises, consulter de multiples sources et réécrire des requêtes jusqu'à produire une réponse soigneusement vérifiée.
2. **Interactions complexes avec des bases de données :** Lorsqu'il s'agit de données structurées où les requêtes échouent souvent ou nécessitent des ajustements, le système peut affiner ses requêtes de manière autonome en utilisant Azure SQL ou Microsoft Fabric OneLake, garantissant que la récupération finale correspond à l'intention de l'utilisateur.
3. **Flux de travail prolongés :** Les sessions de longue durée peuvent évoluer à mesure que de nouvelles informations apparaissent. L'Agentic RAG peut intégrer continuellement de nouvelles données, ajustant ses stratégies à mesure qu'il en apprend davantage sur le problème.

## Gouvernance, transparence et confiance

À mesure que ces systèmes deviennent plus autonomes dans leur raisonnement, la gouvernance et la transparence sont cruciales :

- **Raisonnement explicable :** Le modèle peut fournir une trace d'audit des requêtes qu'il a effectuées, des sources qu'il a consultées et des étapes de raisonnement qu'il a suivies pour parvenir à sa conclusion. Des outils comme Azure AI Content Safety et Azure AI Tracing / GenAIOps peuvent aider à maintenir la transparence et à atténuer les risques.
- **Contrôle des biais et récupération équilibrée :** Les développeurs peuvent ajuster les stratégies de récupération pour s'assurer que des sources de données équilibrées et représentatives sont prises en compte, et auditer régulièrement les résultats pour détecter des biais ou des schémas déséquilibrés à l'aide de modèles personnalisés pour des organisations avancées en science des données utilisant Azure Machine Learning.
- **Supervision humaine et conformité :** Pour les tâches sensibles, la révision humaine reste essentielle. L'Agentic RAG ne remplace pas le jugement humain dans les décisions critiques—il l'augmente en fournissant des options plus soigneusement vérifiées.

Disposer d'outils qui fournissent un enregistrement clair des actions est essentiel. Sans eux, déboguer un processus multi-étapes peut être très difficile. Voir ci-dessous un exemple d'exécution d'agent par Literal AI (l'entreprise derrière Chainlit) :

![AgentRunExample](../../../05-agentic-rag/images/AgentRunExample.png)

![AgentRunExample2](../../../05-agentic-rag/images/AgentRunExample2.png)

## Conclusion

L'Agentic RAG représente une évolution naturelle dans la manière dont les systèmes d'IA gèrent des tâches complexes et intensives en données. En adoptant un modèle d'interaction en boucle, en sélectionnant de manière autonome des outils et en affinant les requêtes jusqu'à obtenir un résultat de haute qualité, le système va au-delà du simple suivi de prompts statiques pour devenir un décideur plus adaptatif et conscient du contexte. Bien qu'encore limité par des infrastructures et des directives éthiques définies par l'humain, ces capacités agentiques permettent des interactions IA plus riches, plus dynamiques et, en fin de compte, plus utiles pour les entreprises et les utilisateurs finaux.

## Ressources supplémentaires

- Implémenter le Retrieval Augmented Generation (RAG) avec Azure OpenAI Service : Apprenez à utiliser vos propres données avec le service Azure OpenAI. [Ce module Microsoft Learn fournit un guide complet sur l'implémentation de RAG](https://learn.microsoft.com/training/modules/use-own-data-azure-openai)
- Évaluation des applications d'IA générative avec Azure AI Foundry : Cet article couvre l'évaluation et la comparaison des modèles sur des ensembles de données disponibles publiquement, y compris [les applications d'IA agentique et les architectures RAG](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [What is Agentic RAG | Weaviate](https://weaviate.io/blog/what-is-agentic-rag)
- [Agentic RAG: A Complete Guide to Agent-Based Retrieval Augmented Generation – News from generation RAG](https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/)
- [Agentic RAG: turbocharge your RAG with query reformulation and self-query! Hugging Face Open-Source AI Cookbook](https://huggingface.co/learn/cookbook/agent_rag)
- [Adding Agentic Layers to RAG](https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U)
- [The Future of Knowledge Assistants: Jerry Liu](https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s)
- [How to Build Agentic RAG Systems](https://www.youtube.com/watch?v=AOSjiXP1jmQ)
- [Using Azure AI Foundry Agent Service to scale your AI agents](https://ignite.microsoft.com/en-US/sessions/BRK102?source=sessions)

### Articles académiques

- [2303.17651 Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- [2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- [2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.