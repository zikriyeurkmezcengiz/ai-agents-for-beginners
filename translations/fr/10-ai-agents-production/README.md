# Agents d'IA en Production 

## Introduction

Cette leçon couvrira :

- Comment planifier efficacement le déploiement de votre agent d'IA en production.
- Les erreurs courantes et les problèmes que vous pourriez rencontrer lors du déploiement de votre agent d'IA en production.
- Comment gérer les coûts tout en maintenant les performances de votre agent d'IA.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez/comment :

- Utiliser des techniques pour améliorer les performances, les coûts et l'efficacité d'un système d'agent d'IA en production.
- Évaluer vos agents d'IA et ce qu'il faut examiner.
- Contrôler les coûts lors du déploiement des agents d'IA en production.

Il est essentiel de déployer des agents d'IA fiables. Consultez également la leçon "Construire des agents d'IA dignes de confiance".

## Évaluation des agents d'IA

Avant, pendant et après le déploiement des agents d'IA, il est crucial de mettre en place un système adéquat pour évaluer vos agents. Cela garantit que votre système est aligné sur vos objectifs et ceux de vos utilisateurs.

Pour évaluer un agent d'IA, il est important de pouvoir évaluer non seulement les résultats de l'agent, mais également l'ensemble du système dans lequel il opère. Cela inclut, sans s'y limiter :

- La requête initiale au modèle.
- La capacité de l'agent à identifier l'intention de l'utilisateur.
- La capacité de l'agent à choisir le bon outil pour accomplir la tâche.
- La réponse de l'outil à la requête de l'agent.
- La capacité de l'agent à interpréter la réponse de l'outil.
- Le retour d'information de l'utilisateur sur la réponse de l'agent.

Cela vous permet d'identifier les domaines à améliorer de manière plus modulaire. Vous pourrez ensuite surveiller l'effet des changements sur les modèles, les invites, les outils et d'autres composants avec une meilleure efficacité.

## Problèmes courants et solutions potentielles avec les agents d'IA

| **Problème**                                   | **Solution potentielle**                                                                                                                                                                                                      |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| L'agent d'IA n'exécute pas les tâches de manière cohérente | - Affinez l'invite donnée à l'agent d'IA ; soyez clair sur les objectifs.<br>- Identifiez si diviser les tâches en sous-tâches et les confier à plusieurs agents peut être utile.                                                 |
| L'agent d'IA entre dans des boucles continues  | - Assurez-vous d'avoir des termes et conditions de terminaison clairs pour que l'agent sache quand arrêter le processus.<br>- Pour les tâches complexes nécessitant du raisonnement et de la planification, utilisez un modèle plus grand spécialisé dans ces tâches. |
| Les appels aux outils par l'agent d'IA ne sont pas performants | - Testez et validez les résultats des outils en dehors du système de l'agent.<br>- Affinez les paramètres définis, les invites et les noms des outils.                                                                           |
| Le système multi-agents manque de cohérence    | - Affinez les invites données à chaque agent pour qu'elles soient spécifiques et distinctes les unes des autres.<br>- Construisez un système hiérarchique en utilisant un agent "routeur" ou contrôleur pour déterminer quel agent est le plus adapté.                  |

## Gestion des coûts

Voici quelques stratégies pour gérer les coûts du déploiement des agents d'IA en production :

- **Mise en cache des réponses** - Identifier les requêtes et tâches courantes et fournir les réponses avant qu'elles ne passent par votre système d'agents est une bonne façon de réduire le volume de requêtes similaires. Vous pouvez même implémenter un flux pour identifier à quel point une requête est similaire à vos requêtes mises en cache en utilisant des modèles d'IA plus basiques.

- **Utilisation de modèles plus petits** - Les Small Language Models (SLMs) peuvent être efficaces pour certains cas d'utilisation d'agents et réduiront considérablement les coûts. Comme mentionné précédemment, construire un système d'évaluation pour déterminer et comparer les performances par rapport à des modèles plus grands est la meilleure façon de comprendre dans quelle mesure un SLM peut convenir à votre cas d'utilisation.

- **Utilisation d'un modèle routeur** - Une stratégie similaire consiste à utiliser une diversité de modèles et de tailles. Vous pouvez utiliser un LLM/SLM ou une fonction sans serveur pour router les requêtes en fonction de leur complexité vers les modèles les plus adaptés. Cela aidera également à réduire les coûts tout en assurant de bonnes performances pour les tâches appropriées.

## Félicitations  

Ceci est actuellement la dernière leçon de "Agents d'IA pour Débutants".

Nous prévoyons d'ajouter des leçons en fonction des retours et des évolutions dans cette industrie en pleine croissance, alors revenez nous voir prochainement.

Si vous souhaitez continuer à apprendre et à développer avec des agents d'IA, rejoignez le [Azure AI Community Discord](https://discord.gg/kzRShWzttr).

Nous y organisons des ateliers, des tables rondes communautaires et des sessions "ask me anything".

Nous avons également une collection de ressources d'apprentissage supplémentaires qui peuvent vous aider à commencer à déployer des agents d'IA en production.
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.