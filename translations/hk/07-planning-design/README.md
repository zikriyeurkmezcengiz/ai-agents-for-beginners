# 設計規劃

## 簡介

呢堂課會講解以下內容：

* 點樣清晰咁定義一個整體目標，並將複雜嘅任務拆解成可管理嘅細項。
* 善用結構化輸出，提供更可靠同機器可讀嘅回應。
* 採用事件驅動嘅方法，應對動態任務同突發輸入。

## 學習目標

完成呢堂課後，你將會了解：

* 點樣為 AI agent 設定清晰嘅整體目標，確保佢知道需要達成咩。
* 將複雜嘅任務分解成可管理嘅子任務，並用邏輯次序組織好。
* 為 agents 配備合適嘅工具（例如搜尋工具或數據分析工具），決定幾時同點樣使用，並處理出現嘅突發情況。
* 評估子任務嘅結果，衡量表現，並對行動進行迭代改進，以提升最終輸出。

## 定義整體目標同拆解任務

![定義目標同任務](../../../translated_images/defining-goals-tasks.dcc1181bbdb194704ae0fb3363371562949e8b03fd2fadc256218aaadf84a9f4.hk.png)

大部分現實世界嘅任務都太過複雜，唔可以一步完成。AI agent 需要一個簡明嘅目標嚟指導佢嘅規劃同行動。例如，考慮以下目標：

    "生成一個 3 日嘅旅遊行程表。"

雖然目標簡單易明，但仍然需要進一步細化。目標越清晰，agent（同人類協作者）越能專注於實現正確嘅結果，例如創建一個全面嘅行程表，包括航班選擇、酒店推薦同活動建議。

### 任務分解

大或者複雜嘅任務可以拆分成細小、針對目標嘅子任務，咁樣會更加易處理。
以旅遊行程表為例，你可以將目標分解成以下部分：

* 機票預訂
* 酒店預訂
* 汽車租賃
* 個人化設定

每個子任務可以交畀專門嘅 agents 或流程處理。例如，一個 agent 可以專注於搜尋最佳機票優惠，另一個則負責酒店預訂，等等。之後，一個協調或者“下游”agent 可以將呢啲結果整合成一個完整嘅行程表提供畀用戶。

呢種模組化嘅方法仲方便逐步改進。例如，你可以加入專門處理美食推薦或者當地活動建議嘅 agents，隨時間優化行程表。

### 結構化輸出

大型語言模型（LLMs）可以生成結構化輸出（例如 JSON），更容易畀下游嘅 agents 或服務進一步解析同處理。呢個特別適合多 agent 嘅場景，當規劃結果生成後，可以即刻執行呢啲任務。參考呢篇 [blogpost](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/cookbook/structured-output-agent.html) 可以快速了解。

以下係一段 Python 範例代碼，展示咗一個簡單嘅規劃 agent 點樣將目標分解成子任務並生成結構化嘅計劃：

### 多 Agent 協調嘅規劃 Agent

呢個例子中，一個 Semantic Router Agent 接收用戶請求（例如，“我需要一個針對我旅行嘅酒店計劃。”）。

規劃器會：

* 接收酒店計劃：規劃器根據用戶嘅信息，結合系統提示（包括可用 agent 嘅詳情），生成一個結構化嘅旅遊計劃。
* 列出 Agents 同佢哋嘅工具：agent 註冊表會保存一個 agents 嘅列表（例如航班、酒店、汽車租賃同活動），以及佢哋提供嘅功能或工具。
* 將計劃分配畀相關嘅 Agents：根據子任務數量，規劃器會直接將信息發送畀專屬 agent（單一任務情況），或者透過群組聊天管理器協調多 agent 嘅合作。
* 總結結果：最後，規劃器會將生成嘅計劃進行總結，方便理解。

以下係示例代碼展示咗呢啲步驟：

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

以上代碼嘅輸出如下，之後你可以用呢個結構化輸出分配畀 `assigned_agent`，並將旅遊計劃總結畀用戶。

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

你可以喺呢度搵到包含上述代碼示例嘅 notebook：[07-autogen.ipynb](../../../07-planning-design/code_samples/07-autogen.ipynb)。

### 迭代規劃

有啲任務需要反覆修改或者重新規劃，因為某個子任務嘅結果可能會影響下一步。例如，當 agent 發現預訂航班時數據格式出乎意料，可能需要調整策略，然後再處理酒店預訂。

另外，用戶嘅反饋（例如用戶決定佢更想搭早啲嘅航班）亦可能觸發部分重新規劃。呢種動態、迭代嘅方法可以確保最終解決方案符合現實世界嘅限制同用戶不斷變化嘅需求。

例如以下代碼：

    ```python
    from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
    #.. same as previous code and pass on the user history, current plan 
    messages = [
        SystemMessage(content="""You are a planner agent to optimize the 
        Your job is to decide which agents to run based on the user's request.
        Below are the available agents specialised in different tasks:
        - FlightBooking: For booking flights and providing flight information
        - HotelBooking: For booking hotels and providing hotel information
        - CarRental: For booking cars and providing car rental information
        - ActivitiesBooking: For booking activities and providing activity information
        - DestinationInfo: For providing information about destinations
        - DefaultAgent: For handling general requests""", source="system"),
        UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
        AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
    ]
    # .. re-plan and send the tasks to respective agents
    ```

如果想更全面了解規劃，可以參考 Magnetic One [Blogpost](https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks)，解釋點樣處理複雜任務。

## 總結

喺呢篇文章中，我哋睇咗一個例子，點樣創建一個規劃器，動態選擇可用嘅 agents。規劃器嘅輸出會分解任務並分配畀 agents 執行。假設 agents 已經有執行任務所需嘅功能/工具。除此之外，你仲可以加入其他模式，例如反思、總結、輪流聊天，進一步自訂化。

## 其他資源

* 使用 o1 推理模型喺規劃複雜任務方面表現相當先進 - TODO: 分享示例？

* Autogen Magnetic One - 一個通用型多 agent 系統，用嚟解決複雜任務，喺多個挑戰性 agent 基準測試中取得咗令人印象深刻嘅結果。參考：[autogen-magentic-one](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one)。喺呢個實現中，協調器會創建針對任務嘅計劃，並將呢啲任務分配畀可用嘅 agents。除咗規劃之外，協調器仲會用一個追蹤機制監控任務進度，並喺需要時重新規劃。

**免責聲明**:  
本文件是使用機器翻譯服務進行翻譯的。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業的人工作翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。