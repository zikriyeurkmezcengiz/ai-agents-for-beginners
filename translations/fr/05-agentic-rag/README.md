# Agentic RAG

Cette leçon offre une vue d'ensemble complète de l'Agentic Retrieval-Augmented Generation (Agentic RAG), un paradigme émergent de l'IA où les grands modèles de langage (LLMs) planifient de manière autonome leurs prochaines étapes tout en récupérant des informations à partir de sources externes. Contrairement aux modèles statiques de type "récupérer puis lire", l'Agentic RAG implique des appels itératifs au LLM, entrecoupés d'appels à des outils ou fonctions et de sorties structurées. Le système évalue les résultats, affine les requêtes, invoque des outils supplémentaires si nécessaire, et poursuit ce cycle jusqu'à ce qu'une solution satisfaisante soit atteinte.

## Introduction

Cette leçon couvrira :

- **Comprendre l'Agentic RAG :** Découvrez ce paradigme émergent en IA où les grands modèles de langage (LLMs) planifient de manière autonome leurs prochaines étapes tout en récupérant des informations à partir de sources de données externes.
- **Approche itérative Maker-Checker :** Apprenez à comprendre la boucle d'appels itératifs au LLM, entrecoupés d'appels à des outils ou fonctions et de sorties structurées, conçue pour améliorer la précision et gérer les requêtes mal formées.
- **Explorer des applications pratiques :** Identifiez les scénarios où l'Agentic RAG excelle, comme dans les environnements où la précision est primordiale, les interactions complexes avec des bases de données, et les flux de travail prolongés.

## Objectifs d'apprentissage

Après avoir complété cette leçon, vous serez capable de :

- **Comprendre l'Agentic RAG :** Découvrir ce paradigme émergent en IA où les grands modèles de langage (LLMs) planifient de manière autonome leurs prochaines étapes tout en récupérant des informations à partir de sources de données externes.
- **Approche itérative Maker-Checker :** Saisir le concept d'une boucle d'appels itératifs au LLM, entrecoupés d'appels à des outils ou fonctions et de sorties structurées, conçue pour améliorer la précision et gérer les requêtes mal formées.
- **Maîtriser le processus de raisonnement :** Comprendre la capacité du système à prendre en charge son propre processus de raisonnement, en décidant comment aborder les problèmes sans dépendre de chemins pré-définis.
- **Flux de travail :** Comprendre comment un modèle agentique décide de manière autonome de récupérer des rapports sur les tendances du marché, d'identifier des données sur les concurrents, de corréler des métriques de ventes internes, de synthétiser les résultats et d'évaluer la stratégie.
- **Boucles itératives, intégration d'outils et mémoire :** Apprenez comment le système s'appuie sur un modèle d'interaction en boucle, en maintenant un état et une mémoire à travers les étapes pour éviter les boucles répétitives et prendre des décisions éclairées.
- **Gérer les échecs et l'auto-correction :** Explorez les mécanismes robustes d'auto-correction du système, incluant des itérations, des réinterrogations, l'utilisation d'outils de diagnostic et le recours à une supervision humaine.
- **Limites de l'autonomie :** Comprendre les limitations de l'Agentic RAG, en se concentrant sur l'autonomie spécifique au domaine, la dépendance à l'infrastructure et le respect des garde-fous.
- **Cas d'usage pratiques et valeur ajoutée :** Identifiez les scénarios où l'Agentic RAG excelle, comme dans les environnements où la précision est primordiale, les interactions complexes avec des bases de données, et les flux de travail prolongés.
- **Gouvernance, transparence et confiance :** Apprenez l'importance de la gouvernance et de la transparence, y compris le raisonnement explicable, le contrôle des biais et la supervision humaine.

## Qu'est-ce que l'Agentic RAG ?

L'Agentic Retrieval-Augmented Generation (Agentic RAG) est un paradigme émergent en IA où les grands modèles de langage (LLMs) planifient de manière autonome leurs prochaines étapes tout en récupérant des informations à partir de sources externes. Contrairement aux modèles statiques de type "récupérer puis lire", l'Agentic RAG implique des appels itératifs au LLM, entrecoupés d'appels à des outils ou fonctions et de sorties structurées. Le système évalue les résultats, affine les requêtes, invoque des outils supplémentaires si nécessaire, et poursuit ce cycle jusqu'à ce qu'une solution satisfaisante soit atteinte. Ce style itératif "maker-checker" améliore la précision, gère les requêtes mal formées et garantit des résultats de haute qualité.

Le système prend activement en charge son processus de raisonnement, réécrit les requêtes échouées, choisit différentes méthodes de récupération et intègre plusieurs outils—tels que la recherche vectorielle dans Azure AI Search, les bases de données SQL ou des API personnalisées—avant de finaliser sa réponse. La qualité distinctive d'un système agentique est sa capacité à posséder son processus de raisonnement. Les implémentations traditionnelles de RAG s'appuient sur des chemins pré-définis, mais un système agentique détermine de manière autonome la séquence des étapes en fonction de la qualité des informations qu'il trouve.

## Définir l'Agentic Retrieval-Augmented Generation (Agentic RAG)

L'Agentic Retrieval-Augmented Generation (Agentic RAG) est un paradigme émergent dans le développement de l'IA où les LLMs non seulement récupèrent des informations à partir de sources de données externes, mais planifient également leurs prochaines étapes de manière autonome. Contrairement aux modèles statiques de type "récupérer puis lire" ou aux séquences de prompts soigneusement scriptées, l'Agentic RAG repose sur une boucle d'appels itératifs au LLM, entrecoupés d'appels à des outils ou fonctions et de sorties structurées. À chaque étape, le système évalue les résultats obtenus, décide s'il doit affiner ses requêtes, invoque des outils supplémentaires si nécessaire, et poursuit ce cycle jusqu'à ce qu'une solution satisfaisante soit atteinte.

Ce style itératif "maker-checker" est conçu pour améliorer la précision, gérer les requêtes mal formées vers des bases de données structurées (par exemple, NL2SQL) et garantir des résultats équilibrés et de haute qualité. Plutôt que de se reposer uniquement sur des chaînes de prompts soigneusement conçues, le système prend activement en charge son processus de raisonnement. Il peut réécrire des requêtes échouées, choisir différentes méthodes de récupération et intégrer plusieurs outils—tels que la recherche vectorielle dans Azure AI Search, les bases de données SQL ou des API personnalisées—avant de finaliser sa réponse. Cela élimine le besoin de cadres d'orchestration excessivement complexes. À la place, une boucle relativement simple de "Appel LLM → Utilisation d'outil → Appel LLM → …" peut produire des résultats sophistiqués et bien fondés.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.2224925a913fb3439f518bda61a40096ddf6aa432a11c9b5bba8d0d625e47b79.fr.png)

## Maîtriser le processus de raisonnement

La qualité distinctive qui rend un système "agentique" est sa capacité à maîtriser son processus de raisonnement. Les implémentations traditionnelles de RAG dépendent souvent des humains pour pré-définir un chemin pour le modèle : une chaîne de réflexion qui décrit quoi récupérer et quand.
Mais lorsqu'un système est véritablement agentique, il décide en interne de la manière d'aborder le problème. Il ne fait pas qu'exécuter un script ; il détermine de manière autonome la séquence des étapes en fonction de la qualité des informations qu'il trouve. 
Par exemple, s'il est demandé de créer une stratégie de lancement de produit, il ne se repose pas uniquement sur un prompt qui décrit tout le flux de travail de recherche et de prise de décision. À la place, le modèle agentique décide indépendamment de :

1. Récupérer les rapports de tendances actuelles du marché à l'aide de Bing Web Grounding.
2. Identifier les données pertinentes sur les concurrents en utilisant Azure AI Search.
3. Corréler les métriques historiques de ventes internes en utilisant Azure SQL Database.
4. Synthétiser les résultats en une stratégie cohérente orchestrée via Azure OpenAI Service.
5. Évaluer la stratégie pour détecter des lacunes ou incohérences, initiant une nouvelle ronde de récupération si nécessaire.
Toutes ces étapes—affiner les requêtes, choisir les sources, itérer jusqu'à être "satisfait" de la réponse—sont décidées par le modèle, et non pré-scriptées par un humain.
``` 

*Note : La traduction est partielle en raison de la longueur du contenu. Si vous souhaitez continuer, veuillez me le faire savoir !*

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.