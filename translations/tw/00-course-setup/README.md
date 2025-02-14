# 課程設置

## 簡介

本課程將介紹如何運行本課程中的程式範例。

## 需求

- 一個 GitHub 帳號
- Python 3.12+ 版本

## 複製或分叉這個倉庫

首先，請複製（clone）或分叉（fork）GitHub 倉庫。這樣可以建立您自己的課程資料副本，方便您運行、測試以及調整程式碼！

您可以透過點擊此連結 [fork the repo](https://github.com/microsoft/ai-agents-for-beginners/fork) 來完成操作。

完成後，您應該會有一個如下所示的分叉版本：

![Forked Repo](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.tw.png)

## 獲取您的 GitHub 個人訪問令牌（PAT）

目前，本課程使用 GitHub Models Marketplace 提供免費的大型語言模型（LLMs）存取權，這些模型將用於創建 AI Agents。

要使用此服務，您需要建立一個 GitHub 個人訪問令牌（Personal Access Token）。

您可以前往您的 GitHub 帳號中的 [Personal Access Tokens settings](https://github.com/settings/personal-access-tokens) 進行設定。

在螢幕左側選擇 `Fine-grained tokens` 選項。

接著選擇 `Generate new token`。

![Generate Token](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.tw.png)

複製您剛剛建立的新令牌。接下來，您需要將它添加到課程中提供的 `.env` 文件中。

## 將令牌添加到環境變數

要建立您的 `.env` 文件，請在終端機中運行以下指令：

```bash
cp .env.example .env
```

這將複製範例文件並在您的目錄中建立一個 `.env` 文件。

打開該文件，將您創建的令牌粘貼到 .env 文件的 `GITHUB_TOKEN=` 欄位中。

## 安裝必要的套件

為了確保您擁有運行程式所需的所有 Python 套件，請在終端機中運行以下指令。

我們建議建立一個 Python 虛擬環境，以避免任何衝突或問題。

```bash
pip install -r requirements.txt
```

這應該會安裝所有必要的 Python 套件。

現在，您已準備好運行程式碼，祝您學習 AI Agents 的世界愉快！

如果您在設置過程中遇到任何問題，請加入我們的 [Azure AI 社群 Discord](https://discord.gg/kzRShWzttr) 或 [建立問題單](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。
```

**免責聲明**：  
本文檔是使用機器翻譯的人工智慧翻譯服務完成的。我們雖然努力確保翻譯的準確性，但請注意，自動翻譯可能會包含錯誤或不精確之處。應以原文檔的原始語言版本作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。