```markdown
# Agents IA en Production 

## Introduction

Cette leçon couvrira :

- Comment planifier efficacement le déploiement de votre Agent IA en production.
- Les erreurs courantes et les problèmes que vous pourriez rencontrer lors du déploiement de votre Agent IA en production.
- Comment gérer les coûts tout en maintenant la performance de votre Agent IA.

## Objectifs d'apprentissage

Après avoir complété cette leçon, vous saurez/comment :

- Utiliser des techniques pour améliorer la performance, les coûts et l'efficacité d'un système d'Agent IA en production.
- Évaluer vos Agents IA et ce qu'il faut prendre en compte.
- Contrôler les coûts lors du déploiement d'Agents IA en production.

Il est essentiel de déployer des Agents IA fiables. Consultez également la leçon "Construire des Agents IA dignes de confiance".

## Évaluation des Agents IA

Avant, pendant et après le déploiement des Agents IA, il est crucial de mettre en place un système adéquat pour les évaluer. Cela garantit que votre système est aligné sur vos objectifs et ceux de vos utilisateurs.

Pour évaluer un Agent IA, il est important de pouvoir évaluer non seulement les réponses de l'agent, mais également l'ensemble du système dans lequel votre Agent IA opère. Cela inclut, mais ne se limite pas à :

- La demande initiale au modèle.
- La capacité de l'agent à identifier l'intention de l'utilisateur.
- La capacité de l'agent à choisir l'outil adéquat pour accomplir la tâche.
- La réponse de l'outil à la demande de l'agent.
- La capacité de l'agent à interpréter la réponse de l'outil.
- Les retours de l'utilisateur sur la réponse de l'agent.

Cela vous permet d'identifier les points d'amélioration de manière plus modulaire. Vous pouvez ensuite surveiller l'impact des changements sur les modèles, les invites, les outils et d'autres composants avec une meilleure efficacité.

## Problèmes Courants et Solutions Potentielles avec les Agents IA

| **Problème**                                   | **Solution Potentielle**                                                                                                                                                                                                   |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| L'Agent IA n'accomplit pas les tâches de manière cohérente | - Affinez l'invite donnée à l'Agent IA ; soyez clair sur les objectifs.<br>- Identifiez où diviser les tâches en sous-tâches et les confier à plusieurs agents peut être utile.                                               |
| L'Agent IA entre dans des boucles continues    | - Assurez-vous d'avoir des termes et conditions de fin clairs pour que l'Agent sache quand arrêter le processus.<br>- Pour les tâches complexes nécessitant raisonnement et planification, utilisez un modèle plus grand spécialisé dans ces tâches. |
| Les appels d'outils de l'Agent IA ne fonctionnent pas bien | - Testez et validez la sortie de l'outil en dehors du système de l'agent.<br>- Affinez les paramètres définis, les invites et les noms des outils.                                                                           |
| Le système multi-agents n'est pas cohérent     | - Affinez les invites données à chaque agent pour qu'elles soient spécifiques et distinctes les unes des autres.<br>- Construisez un système hiérarchique en utilisant un agent "routage" ou contrôleur pour déterminer quel agent est le plus adapté. |

## Gestion des Coûts

Voici quelques stratégies pour gérer les coûts lors du déploiement d'Agents IA en production :

- **Mise en cache des réponses** - Identifier les requêtes et tâches fréquentes et fournir les réponses avant qu'elles ne passent par votre système agentique est un bon moyen de réduire le volume de requêtes similaires. Vous pouvez même mettre en place un flux pour identifier à quel point une requête est similaire à celles mises en cache en utilisant des modèles IA plus basiques.

- **Utilisation de modèles plus petits** - Les Small Language Models (SLMs) peuvent bien fonctionner pour certains cas d'usage agentiques et réduire considérablement les coûts. Comme mentionné précédemment, construire un système d'évaluation pour déterminer et comparer la performance par rapport à des modèles plus grands est la meilleure manière de comprendre dans quelle mesure un SLM conviendra à votre cas d'usage.

- **Utilisation d'un modèle de routage** - Une stratégie similaire consiste à utiliser une diversité de modèles et de tailles. Vous pouvez utiliser un LLM/SLM ou une fonction sans serveur pour acheminer les requêtes en fonction de leur complexité vers les modèles les plus adaptés. Cela contribuera également à réduire les coûts tout en garantissant la performance sur les bonnes tâches.

## Félicitations  

Ceci est actuellement la dernière leçon de "Agents IA pour Débutants".

Nous prévoyons d'ajouter d'autres leçons en fonction des retours et des évolutions de cette industrie en pleine croissance, alors revenez bientôt.

Si vous souhaitez continuer à apprendre et à développer avec des Agents IA, rejoignez le [Azure AI Community Discord](https://discord.gg/kzRShWzttr).

Nous y organisons des ateliers, des tables rondes communautaires et des sessions "ask me anything".

Nous avons également une collection d'apprentissage avec des ressources supplémentaires pour vous aider à commencer à déployer des Agents IA en production.
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.