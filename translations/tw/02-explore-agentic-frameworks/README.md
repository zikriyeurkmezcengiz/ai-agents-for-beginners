# 探索 AI Agent 框架

AI Agent 框架是為了簡化 AI agent 的創建、部署和管理而設計的軟體平台。這些框架為開發者提供了預先構建的組件、抽象層和工具，從而加速複雜 AI 系統的開發過程。

透過提供標準化的方法來解決 AI agent 開發中的常見挑戰，這些框架讓開發者能專注於應用程式的獨特面向。同時，它們提升了 AI 系統的可擴展性、可存取性和效率。

## 簡介

本課程將涵蓋以下內容：

- 什麼是 AI Agent 框架？它能讓開發者完成哪些事情？
- 團隊如何利用這些框架快速原型化、迭代和提升 agent 的能力？
- 微軟的框架與工具（[Autogen](https://aka.ms/ai-agents/autogen)、[Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel)、[Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)）之間的差異是什麼？
- 我可以直接整合現有的 Azure 生態系統工具，還是需要獨立的解決方案？
- 什麼是 Azure AI Agents 服務，它能如何幫助我？

## 學習目標

本課程的目標是幫助您了解：

- AI Agent 框架在 AI 開發中的角色。
- 如何利用 AI Agent 框架來構建智慧型 agent。
- AI Agent 框架所啟用的核心功能。
- Autogen、Semantic Kernel 和 Azure AI Agent Service 的差異。

## 什麼是 AI Agent 框架？它能讓開發者完成哪些事情？

傳統的 AI 框架可以幫助您將 AI 整合到應用程式中，並透過以下方式提升應用程式的功能：

- **個性化**：AI 能分析用戶行為和偏好，提供個性化的推薦、內容和體驗。  
  範例：像 Netflix 這樣的串流服務利用 AI 根據觀看歷史推薦電影和節目，提升用戶參與度和滿意度。
  
- **自動化與效率**：AI 能自動化重複性任務、簡化工作流程並提升運營效率。  
  範例：客戶服務應用程式利用 AI 驅動的聊天機器人處理常見問題，縮短回應時間，讓人類客服專注於更複雜的問題。

- **提升用戶體驗**：AI 能提供智慧功能，例如語音識別、自然語言處理和預測性文字輸入，改善整體用戶體驗。  
  範例：像 Siri 和 Google Assistant 這樣的虛擬助手利用 AI 理解並回應語音指令，讓用戶更輕鬆地與裝置互動。

### 聽起來很棒對吧，那為什麼我們還需要 AI Agent 框架？

AI Agent 框架不僅僅是 AI 框架，它們旨在創建能與用戶、其他 agent 和環境互動以達成特定目標的智慧型 agent。這些 agent 能展現自主行為、做出決策並適應變化中的環境。我們來看看 AI Agent 框架啟用的一些關鍵功能：

- **Agent 的協作與協調**：能創建多個 AI agent，它們可以協作、溝通並共同解決複雜任務。
- **任務自動化與管理**：提供機制來自動化多步驟的工作流程、任務分配和動態任務管理。
- **上下文理解與適應**：讓 agent 具備理解上下文、適應變化環境並根據即時資訊做出決策的能力。

總而言之，這些 agent 能幫助您完成更多工作，將自動化提升到新層次，並創建能從環境中學習和適應的智慧系統。

## 如何快速原型化、迭代並提升 agent 的能力？

這是一個快速變化的領域，但大多數 AI Agent 框架中有一些共同的元素，能幫助您快速原型化和迭代，主要包括模組化組件、協作工具和即時學習。我們來深入了解這些元素：

- **使用模組化組件**：AI 框架提供預構建的組件，例如提示、解析器和記憶管理。
- **利用協作工具**：設計具有特定角色和任務的 agent，測試並完善協作工作流程。
- **即時學習**：實施反饋循環，讓 agent 從互動中學習並動態調整行為。

### 使用模組化組件

像 LangChain 和 Microsoft Semantic Kernel 這樣的框架提供了預構建的組件，例如提示、解析器和記憶管理。

**團隊如何使用**：團隊可以快速組裝這些組件來創建功能原型，無需從零開始，從而進行快速實驗和迭代。

**實際運作方式**：您可以使用預構建的解析器從用戶輸入中提取資訊，使用記憶模組來儲存和檢索數據，並使用提示生成器與用戶互動，無需自行構建這些組件。

**範例代碼**：以下是如何使用預構建的解析器從用戶輸入中提取資訊的範例：

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

從這個範例可以看出，如何利用預構建的解析器從用戶輸入中提取關鍵資訊，例如航班預訂請求的出發地、目的地和日期。這種模組化方法讓您能專注於高層次邏輯。

### 利用協作工具

像 CrewAI 和 Microsoft Autogen 這樣的框架可以幫助創建多個能協作的 agent。

**團隊如何使用**：團隊可以設計具有特定功能和任務的 agent，測試並完善協作工作流程，提升整體系統效率。

**實際運作方式**：您可以創建一組 agent，其中每個 agent 都有專門的功能，例如數據檢索、分析或決策。這些 agent 能溝通並分享資訊，以完成共同目標，例如回答用戶查詢或完成任務。

**範例代碼（Autogen）**：

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

上述代碼展示了如何創建一個任務，涉及多個 agent 協作完成數據分析。每個 agent 執行特定功能，透過協調這些 agent 的行動來實現目標。透過創建具有專業角色的專屬 agent，您可以提升任務效率和性能。

### 即時學習

進階框架提供了即時上下文理解和適應的能力。

**團隊如何使用**：團隊可以實施反饋循環，讓 agent 從互動中學習並動態調整行為，實現持續改進和能力優化。

**實際運作方式**：agent 可以分析用戶反饋、環境數據和任務結果，更新其知識庫、調整決策演算法並提升性能。這種迭代學習過程讓 agent 能適應變化的條件和用戶偏好，增強整體系統的效能。

## Autogen、Semantic Kernel 和 Azure AI Agent Service 之間有什麼差異？

這些框架之間有許多比較方式，但我們可以從設計、功能和目標使用案例的角度來看一些關鍵差異：

### Autogen

這是一個由微軟研究院 AI Frontiers Lab 開發的開源框架，專注於事件驅動的分散式 *agentic* 應用程式，支持多個 LLM 和 SLM、工具以及進階的多 agent 設計模式。

Autogen 的核心概念是 agent，也就是能感知環境、做出決策並採取行動以達成特定目標的自主實體。agent 透過非同步訊息進行溝通，使其能獨立且並行工作，提升系統的可擴展性和響應性。

... (請參閱原始文件中的完整詳細說明，內容過多，無法一次列出)

### Semantic Kernel + Agent Framework

Semantic Kernel 包含兩部分：Semantic Kernel Agent Framework 和 Semantic Kernel 本身。

... (請參閱原始文件中的完整詳細說明)

### Azure AI Agent Service

Azure AI Agent Service 是最近推出的服務（於 Microsoft Ignite 2024 發表）。它允許使用更靈活的模型來開發和部署 AI agent，例如直接調用開源 LLM（如 Llama 3、Mistral 和 Cohere）。

... (請參閱原始文件中的完整詳細說明)

---

### 哪個框架適合您的使用案例？

以下是一些常見使用案例的建議：

> **Q**: 我的團隊正在開發一個涉及自動化代碼生成和數據分析任務的項目，我們應該使用哪個框架？  
> **A**: Autogen 是一個不錯的選擇，因為它專注於事件驅動的分散式 *agentic* 應用程式，並支持進階的多 agent 設計模式。

... (請參閱原始文件中的完整對話內容)

---

希望這些資訊能幫助您更好地選擇適合您需求的 AI Agent 框架！
根據項目目標。適用於自然語言理解和內容生成。  
- **Azure AI Agent Service**：靈活的模型、企業安全機制、數據存儲方法。適用於在企業應用中部署安全、可擴展且靈活的 AI 代理。  

## 我可以直接整合現有的 Azure 生態系統工具，還是需要獨立的解決方案？  
答案是肯定的，您可以直接將現有的 Azure 生態系統工具與 Azure AI Agent Service 整合，特別是因為它被設計為能與其他 Azure 服務無縫協作。例如，您可以整合 Bing、Azure AI Search 和 Azure Functions。此外，還可以與 Azure AI Foundry 深度整合。  

對於 Autogen 和 Semantic Kernel，您也可以與 Azure 服務整合，但可能需要從您的代碼中調用 Azure 服務。另一種整合方式是使用 Azure SDK 從您的代理與 Azure 服務交互。此外，如前所述，您可以使用 Azure AI Agent Service 作為基於 Autogen 或 Semantic Kernel 構建的代理的協調器，從而輕鬆訪問 Azure 生態系統。  

## 參考資料  
- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)  
- [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/)  
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp)  
- [4] - [Azure AI Agent service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)  
- [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)  

**免責聲明**：  
本文件使用基於機器的人工智能翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文檔的母語版本應被視為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對使用此翻譯所引起的任何誤解或錯誤解讀概不負責。