# 探索 AI Agent 框架

AI Agent 框架係一啲專門設計嘅軟件平台，目標係簡化 AI agent 嘅開發、部署同管理。呢啲框架為開發者提供預設嘅組件、抽象層同工具，令到開發複雜嘅 AI 系統變得更加簡單。

呢啲框架幫助開發者專注於應用程式嘅獨特部分，通過為 AI agent 開發中常見嘅挑戰提供標準化嘅解決方案。佢哋提升咗構建 AI 系統嘅可擴展性、可用性同效率。

## 簡介

呢堂課會涵蓋：

- 乜嘢係 AI Agent 框架？佢哋可以幫開發者做到啲乜？
- 團隊可以點樣利用呢啲框架快速原型設計、反覆改良同提升 agent 嘅能力？
- 微軟開發嘅框架同工具（[Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)）有乜唔同？
- 我可以直接整合現有嘅 Azure 生態系統工具，定係需要獨立嘅解決方案？
- 乜嘢係 Azure AI Agents Service？佢可以點樣幫到我？

## 學習目標

呢堂課嘅目標係幫你了解：

- AI Agent 框架喺 AI 開發中嘅角色。
- 點樣利用 AI Agent 框架構建智能 agent。
- AI Agent 框架提供嘅關鍵功能。
- Autogen、Semantic Kernel 同 Azure AI Agent Service 嘅分別。

## 乜嘢係 AI Agent 框架？佢哋可以幫開發者做到啲乜？

傳統嘅 AI 框架可以幫你將 AI 整合到應用程式入面，並令呢啲應用更好，方式如下：

- **個性化**：AI 可以分析用戶行為同喜好，提供個人化推薦、內容同體驗。  
例子：Netflix 呢類串流服務用 AI 根據用戶嘅觀看歷史推薦電影同節目，提升用戶參與度同滿意度。

- **自動化同效率**：AI 可以自動化重複性任務、簡化工作流程，提升運營效率。  
例子：客戶服務應用利用 AI 驅動嘅聊天機械人處理常見查詢，縮短回應時間，令人工客服可以專注於更複雜嘅問題。

- **提升用戶體驗**：AI 可以提供智能功能，例如語音識別、自然語言處理同預測文本，改善整體用戶體驗。  
例子：虛擬助手例如 Siri 同 Google Assistant 利用 AI 理解同回應語音指令，令用戶更容易操作設備。

### 咁聽起嚟好正，但點解仲需要 AI Agent 框架？

AI Agent 框架唔止係 AI 框架咁簡單。佢哋設計出嚟係為咗創建智能 agent，呢啲 agent 可以同用戶、其他 agent 同環境互動，達到特定目標。呢啲 agent 可以表現出自主行為、作決策，並適應不斷變化嘅條件。以下係 AI Agent 框架提供嘅幾個關鍵功能：

- **Agent 合作同協調**：支持創建多個 AI agent，佢哋可以合作、溝通同協調，解決複雜任務。
- **任務自動化同管理**：提供機制，自動化多步工作流程、任務分配同動態任務管理。
- **上下文理解同適應**：賦予 agent 理解上下文、適應環境變化嘅能力，並根據實時信息作出決策。

總結嚟講，agent 令你做到更多，可以將自動化提升到新層次，創建能夠適應同學習環境嘅更智能系統。

## 點樣快速原型設計、反覆改良同提升 agent 嘅能力？

呢個領域發展得好快，但大多數 AI Agent 框架都有啲共通點，可以幫你快速原型設計同反覆改良，包括模塊化組件、協作工具同實時學習。讓我哋逐一探討：

- **使用模塊化組件**：AI 框架提供預設嘅組件，例如 prompts、parsers 同記憶管理。
- **利用協作工具**：設計擁有特定角色同任務嘅 agent，測試同改良協作工作流程。
- **實時學習**：實現反饋循環，令 agent 從互動中學習，並動態調整行為。

### 使用模塊化組件

框架例如 LangChain 同 Microsoft Semantic Kernel 提供預設嘅組件，例如 prompts、parsers 同記憶管理。

**團隊點樣用呢啲**：團隊可以快速組裝呢啲組件，創建一個可用嘅原型，而唔需要從零開始，從而快速進行實驗同反覆改良。

**實際操作係點**：你可以使用預設嘅 parser 從用戶輸入中提取信息，用記憶模塊存取數據，並用 prompt 生成器同用戶互動，呢啲都唔需要你自己從頭開發。

**範例代碼**：以下係一個例子，展示點樣用預設嘅 parser 從用戶輸入中提取信息：

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

由呢個例子你可以睇到，點樣利用預設嘅 parser 提取用戶輸入嘅關鍵信息，例如航班預訂請求嘅出發地、目的地同日期。呢種模塊化方法可以令你專注於高層次邏輯。

### 利用協作工具

框架例如 CrewAI 同 Microsoft Autogen 幫助創建多個可以合作嘅 agent。

**團隊點樣用呢啲**：團隊可以設計擁有特定角色同任務嘅 agent，測試同改良協作工作流程，從而提升整體系統效率。

**實際操作係點**：你可以創建一組 agent，每個 agent 都有專門功能，例如數據檢索、分析或決策。呢啲 agent 可以溝通同分享信息，以完成共同目標，例如回答用戶查詢或完成任務。

**範例代碼 (Autogen)**：

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

上面嘅代碼展示咗點樣創建一個涉及多個 agent 協作分析數據嘅任務。每個 agent 執行特定功能，並通過協調佢哋嘅行動完成目標任務。創建專門角色嘅 agent 可以提升任務效率同性能。

### 實時學習

高級框架提供實時上下文理解同適應嘅能力。

**團隊點樣用呢啲**：團隊可以實現反饋循環，令 agent 從互動中學習，並動態調整行為，實現持續改良同能力提升。

**實際操作係點**：agent 可以分析用戶反饋、環境數據同任務結果，更新佢哋嘅知識庫，調整決策算法，並隨時間改進性能。呢種反覆學習過程令 agent 能夠適應變化嘅條件同用戶偏好，提升整體系統效能。

## Autogen、Semantic Kernel 同 Azure AI Agent Service 嘅分別係咩？

有好多方法可以比較呢啲框架，以下係從設計、功能同目標用例方面嘅主要區別：

### Autogen

一個由 Microsoft Research 嘅 AI Frontiers Lab 開發嘅開源框架，專注於事件驅動、分布式嘅 *agentic* 應用，支持多個 LLMs、SLMs、工具同高級多-agent 設計模式。

Autogen 嘅核心概念係基於 agent，呢啲係自主實體，可以感知環境、作決策同採取行動以達到特定目標。agent 通過非同步消息進行溝通，令佢哋可以獨立同並行工作，提升系統可擴展性同響應能力。

...（以下省略其餘部分，內容太長）...
根據項目目標。適用於自然語言理解、內容生成。  
- **Azure AI Agent Service**：靈活的模型、企業級安全機制、數據存儲方法。適用於企業應用中安全、可擴展且靈活的 AI 代理部署。  

## 我可以直接整合現有的 Azure 生態系統工具，還是需要獨立的解決方案？  
答案是肯定的，您可以直接將現有的 Azure 生態系統工具與 Azure AI Agent Service 整合，特別是因為它被設計為能與其他 Azure 服務無縫協作。例如，您可以整合 Bing、Azure AI Search 和 Azure Functions。還有與 Azure AI Foundry 的深度整合。對於 Autogen 和 Semantic Kernel，您也可以與 Azure 服務整合，但可能需要從您的代碼中調用 Azure 服務。另一種整合方式是使用 Azure SDK 從您的代理與 Azure 服務進行交互。此外，如前所述，您可以將 Azure AI Agent Service 作為 Autogen 或 Semantic Kernel 構建的代理的協調器，這將使您能輕鬆訪問 Azure 生態系統。  

## 參考資料  
- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)  
- [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/)  
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp)  
- [4] - [Azure AI Agent service](https://learn.microsoft.com/azure/ai-services/agents/overview)  
- [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)  

**免責聲明**：  
本文件是使用機器翻譯AI服務進行翻譯的。我們致力於追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或錯誤解釋概不負責。