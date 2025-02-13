```markdown
# Configuration du cours

## Introduction

Cette leçon couvrira comment exécuter les exemples de code de ce cours.

## Prérequis

- Un compte GitHub
- Python 3.12+

## Cloner ou Forker ce dépôt

Pour commencer, veuillez cloner ou forker le dépôt GitHub. Cela vous permettra de créer votre propre version du matériel du cours afin de pouvoir exécuter, tester et ajuster le code !

Vous pouvez le faire en cliquant sur le lien pour [forker le dépôt](https://github.com/microsoft/ai-agents-for-beginners/fork).

Vous devriez maintenant avoir votre propre version forkée de ce cours, comme illustré ci-dessous :

![Dépôt forké](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.fr.png)

## Récupérer votre jeton d'accès personnel GitHub (PAT)

Actuellement, ce cours utilise le Marketplace des modèles GitHub pour offrir un accès gratuit à des modèles de langage étendus (LLMs) qui seront utilisés pour créer des agents IA.

Pour accéder à ce service, vous devrez créer un jeton d'accès personnel GitHub.

Cela peut être fait en accédant à vos [paramètres des jetons d'accès personnel](https://github.com/settings/personal-access-tokens) dans votre compte GitHub.

Sélectionnez les options `Fine-grained tokens` sur le côté gauche de votre écran.

Ensuite, sélectionnez `Generate new token`.

![Générer un jeton](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.fr.png)

Copiez votre nouveau jeton que vous venez de créer. Vous allez maintenant l’ajouter à votre fichier `.env` inclus dans ce cours.

## Ajouter ceci à vos variables d'environnement

Pour créer votre fichier `.env`, exécutez la commande ci-dessous dans votre terminal :

```bash
cp .env.example .env
```

Cela copiera le fichier d'exemple et créera un fichier `.env` dans votre répertoire.

Ouvrez ce fichier et collez le jeton que vous avez créé dans le champ `GITHUB_TOKEN=` du fichier .env.

## Installer les packages requis

Pour vous assurer que vous disposez de tous les packages Python nécessaires pour exécuter le code, exécutez la commande suivante dans votre terminal.

Nous recommandons de créer un environnement virtuel Python pour éviter tout conflit ou problème.

```bash
pip install -r requirements.txt
```

Cela devrait installer les packages Python requis.

Vous êtes maintenant prêt à exécuter le code de ce cours. Bonne découverte du monde des agents IA !

Si vous rencontrez un problème lors de cette configuration, rejoignez notre [Discord de la communauté Azure AI](https://discord.gg/kzRShWzttr) ou [créez une issue](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst).
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.