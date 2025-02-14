# Configuration du Cours

## Introduction

Cette leçon expliquera comment exécuter les exemples de code de ce cours.

## Prérequis

- Un compte GitHub
- Python 3.12+

## Cloner ou Forker ce Dépôt

Pour commencer, veuillez cloner ou forker le dépôt GitHub. Cela créera votre propre version du matériel de cours, vous permettant ainsi d'exécuter, de tester et de modifier le code !

Cela peut être fait en cliquant sur le lien pour [forker le dépôt](https://github.com/microsoft/ai-agents-for-beginners/fork).

Vous devriez maintenant avoir votre propre version forkée de ce cours, comme ci-dessous :

![Dépôt Forké](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.fr.png)

## Récupérer votre Token d'Accès Personnel (PAT) GitHub

Ce cours utilise actuellement le Marketplace des modèles GitHub pour offrir un accès gratuit aux Modèles de Langage de Grande Taille (LLMs) qui seront utilisés pour créer des Agents IA.

Pour accéder à ce service, vous devrez créer un Token d'Accès Personnel GitHub.

Cela peut être fait en allant dans vos [paramètres de Tokens d'Accès Personnel](https://github.com/settings/personal-access-tokens) sur votre compte GitHub.

Sélectionnez l'option `Fine-grained tokens` située à gauche de votre écran.

Puis sélectionnez `Generate new token`.

![Générer un Token](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.fr.png)

Copiez le nouveau token que vous venez de créer. Vous allez maintenant l'ajouter à votre fichier `.env` inclus dans ce cours.

## Ajouter ceci à vos Variables d'Environnement

Pour créer votre fichier `.env`, exécutez la commande suivante dans votre terminal :

```bash
cp .env.example .env
```

Cela copiera le fichier exemple et créera un fichier `.env` dans votre répertoire.

Ouvrez ce fichier et collez le token que vous avez créé dans le champ `GITHUB_TOKEN=` du fichier .env.

## Installer les Paquets Requis

Pour vous assurer d'avoir tous les paquets Python nécessaires à l'exécution du code, exécutez la commande suivante dans votre terminal.

Nous vous recommandons de créer un environnement virtuel Python pour éviter tout conflit ou problème.

```bash
pip install -r requirements.txt
```

Cela devrait installer les paquets Python requis.

Vous êtes maintenant prêt à exécuter le code de ce cours. Bon apprentissage dans le monde des Agents IA !

Si vous rencontrez des problèmes lors de cette configuration, rejoignez notre [Discord de la Communauté Azure AI](https://discord.gg/kzRShWzttr) ou [créez un ticket](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst).
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations cruciales, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.