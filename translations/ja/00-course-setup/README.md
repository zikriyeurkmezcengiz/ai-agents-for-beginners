# コースセットアップ

## はじめに

このレッスンでは、このコースのコードサンプルを実行する方法を説明します。

## 必要条件

- GitHubアカウント
- Python 3.12以上

## このリポジトリをクローンまたはフォークする

まず最初に、GitHubリポジトリをクローンまたはフォークしてください。これにより、コース教材の自分専用のバージョンが作成され、コードを実行、テスト、調整できるようになります。

以下のリンクをクリックして[リポジトリをフォークする](https://github.com/microsoft/ai-agents-for-beginners/fork)ことができます。

これで、以下のように自分専用のフォークされたコースバージョンが作成されます:

![フォークされたリポジトリ](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.ja.png)

## GitHubパーソナルアクセストークン（PAT）の取得

現在、このコースではGitHub Models Marketplaceを利用して、AIエージェントを作成するための大規模言語モデル（LLMs）への無料アクセスを提供しています。

このサービスにアクセスするには、GitHubのパーソナルアクセストークンを作成する必要があります。

トークンを作成するには、GitHubアカウントの[Personal Access Tokens設定](https://github.com/settings/personal-access-tokens)にアクセスしてください。

画面左側の `Fine-grained tokens` オプションを選択します。

次に `Generate new token` を選択してください。

![トークンの生成](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.ja.png)

作成した新しいトークンをコピーしてください。このトークンを、このコースに含まれる `.env` ファイルに追加します。

## 環境変数に追加する

`.env` ファイルを作成するには、以下のコマンドをターミナルで実行してください:

```bash
cp .env.example .env
```

これにより、サンプルファイルがコピーされ、ディレクトリ内に `.env` が作成されます。

そのファイルを開き、作成したトークンを `.env` ファイルの `GITHUB_TOKEN=` フィールドに貼り付けてください。

## 必要なパッケージのインストール

コードを実行するために必要なPythonパッケージをすべてインストールするには、以下のコマンドをターミナルに入力してください。

Python仮想環境を作成することをお勧めします。これにより、競合や問題を回避できます。

```bash
pip install -r requirements.txt
```

これで必要なPythonパッケージがインストールされます。

これでコードを実行する準備が整いました。AIエージェントの世界について学ぶことを楽しんでください！

セットアップの実行中に問題が発生した場合は、[Azure AI Community Discord](https://discord.gg/kzRShWzttr)に参加するか、[Issueを作成](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst)してください。
```

**免責事項**:  
この文書は、AIによる機械翻訳サービスを使用して翻訳されています。正確さを期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文（元の言語で記載された文書）が正式な情報源として優先されるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の利用により生じた誤解や解釈の相違について、当方は一切の責任を負いません。