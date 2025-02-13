# 課程設定

## 簡介

呢堂會教你點樣運行呢個課程嘅代碼示例。

## 必備條件

- 一個 GitHub 帳戶
- Python 3.12 或以上版本

## 複製或分叉呢個 Repo

首先，請複製（clone）或者分叉（fork）GitHub 嘅 Repository。咁樣你就可以擁有課程材料嘅自己版本，方便運行、測試同埋調整代碼！

可以點擊呢個連結 [fork the repo](https://github.com/microsoft/ai-agents-for-beginners/fork) 去操作。

完成後，你應該會有一個好似以下圖示嘅分叉版本：

![Forked Repo](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.hk.png)

## 獲取你嘅 GitHub Personal Access Token (PAT)

目前呢個課程使用 GitHub Models Marketplace 提供免費嘅大型語言模型（LLMs）服務，用嚟創建 AI Agents。

要使用呢個服務，你需要創建一個 GitHub 嘅 Personal Access Token。

你可以去你嘅 GitHub 帳戶嘅 [Personal Access Tokens settings](https://github.com/settings/personal-access-tokens) 頁面創建。

揀選屏幕左邊嘅 `Fine-grained tokens` 選項。

然後揀選 `Generate new token`。

![Generate Token](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.hk.png)

複製你啱啱創建嘅新 Token。之後，你需要將呢個 Token 加到課程中提供嘅 `.env` 文件內。

## 將 Token 加到環境變數

要創建你嘅 `.env` 文件，可以喺終端運行以下命令：

```bash
cp .env.example .env
```

呢條命令會複製示例文件，並喺你嘅目錄內創建一個 `.env` 文件。

打開呢個文件，然後將你創建嘅 Token 貼到 `.env` 文件中 `GITHUB_TOKEN=` 呢一行。

## 安裝所需嘅套件

為咗確保你有齊所有運行代碼所需嘅 Python 套件，請喺終端運行以下命令。

我哋建議你創建一個 Python 虛擬環境，避免發生衝突同埋問題。

```bash
pip install -r requirements.txt
```

呢條命令應該會安裝所有所需嘅 Python 套件。

而家你已經準備好運行課程嘅代碼，祝你學習 AI Agents 嘅世界愉快！

如果喺設定過程中遇到任何問題，可以加入我哋嘅 [Azure AI Community Discord](https://discord.gg/kzRShWzttr) 或者 [create an issue](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

**免責聲明**:  
本文件經由機器翻譯人工智能服務進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文作為權威來源。如涉及重要資訊，建議尋求專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或錯誤解釋概不負責。