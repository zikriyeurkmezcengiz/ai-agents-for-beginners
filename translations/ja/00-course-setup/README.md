# コースセットアップ

## はじめに

このレッスンでは、このコースのコードサンプルを実行する方法について説明します。

## 必要条件

- GitHub アカウント
- Python 3.12+

## このリポジトリをクローンまたはフォークする

まず、GitHub リポジトリをクローンまたはフォークしてください。これにより、コース教材の自分専用のバージョンが作成され、コードを実行したり、テストしたり、調整したりすることができます！

[リポジトリをフォークする](https://github.com/microsoft/ai-agents-for-beginners/fork)リンクをクリックすることでこれを実行できます。

以下のように、このコースのフォーク済みバージョンが作成されているはずです:

![フォークされたリポジトリ](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.ja.png)

## GitHub Personal Access Token (PAT) を取得する

現在、このコースでは GitHub Models Marketplace を利用して、AIエージェントを作成するために使用する大規模言語モデル (LLMs) への無料アクセスを提供しています。

このサービスにアクセスするには、GitHub Personal Access Token を作成する必要があります。

これは、GitHub アカウントの [Personal Access Tokens 設定](https://github.com/settings/personal-access-tokens) にアクセスすることで行えます。

画面左側の `Fine-grained tokens` オプションを選択してください。

次に `Generate new token` を選択します。

![トークンを生成](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.ja.png)

新しく作成したトークンをコピーしてください。このトークンを、このコースに含まれる `.env` ファイルに追加します。

## 環境変数に追加する

`.env` ファイルを作成するには、ターミナルで以下のコマンドを実行してください:

```bash
cp .env.example .env
```

これにより、例となるファイルがコピーされ、ディレクトリ内に `.env` が作成されます。

そのファイルを開き、作成したトークンを .env ファイルの `GITHUB_TOKEN=` フィールドに貼り付けてください。

## 必要なパッケージをインストールする

コードを実行するために必要な Python パッケージをすべて揃えるには、以下のコマンドをターミナルで実行してください。

Python 仮想環境を作成することをお勧めします。これにより、競合や問題を避けることができます。

```bash
pip install -r requirements.txt
```

これにより、必要な Python パッケージがインストールされます。

これでコードを実行する準備が整いました！AIエージェントの世界について楽しく学んでください！

セットアップの実行中に問題が発生した場合は、[Azure AI Community Discord](https://discord.gg/kzRShWzttr) に参加するか、[issue を作成する](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst) ことでサポートを受けることができます。

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な表現が含まれる場合があります。元の言語で記載された原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や解釈の誤りについて、当社は一切の責任を負いません。