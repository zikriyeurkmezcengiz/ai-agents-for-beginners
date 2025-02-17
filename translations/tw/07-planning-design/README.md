# 規劃設計

## 簡介

本課程將涵蓋以下內容：

* 定義明確的整體目標，並將複雜任務分解為可管理的小任務。
* 利用結構化輸出來實現更可靠且可機器讀取的回應。
* 採用事件驅動的方法來處理動態任務及應對意外輸入。

## 學習目標

完成本課程後，你將能夠：

* 確認並設定 AI 代理的整體目標，確保它明確知道需要完成的工作。
* 將複雜任務分解為可管理的子任務，並將它們組織成邏輯順序。
* 為代理配備適當的工具（例如搜尋工具或數據分析工具），決定何時及如何使用這些工具，並處理可能出現的意外情況。
* 評估子任務的結果、衡量性能，並通過反覆迭代改進最終輸出。

## 定義整體目標並分解任務

![定義目標與任務](../../../translated_images/defining-goals-tasks.dcc1181bbdb194704ae0fb3363371562949e8b03fd2fadc256218aaadf84a9f4.tw.png)

大多數現實世界的任務都過於複雜，無法一步完成。AI 代理需要一個簡潔的目標來指導其規劃和行動。例如，考慮以下目標：

    "生成一個三天的旅行行程。"

雖然這個目標表述簡單，但仍需進一步細化。目標越清晰，代理（以及任何人類協作者）就越能專注於實現正確的結果，例如創建一個包含航班選項、酒店推薦和活動建議的完整行程。

### 任務分解

大型或複雜的任務在被分解為更小的、目標導向的子任務後會更易管理。
以旅行行程為例，你可以將目標分解為：

* 航班預訂
* 酒店預訂
* 租車
* 個性化定制

每個子任務可以由專門的代理或流程處理。一個代理可能專注於搜尋最佳航班優惠，另一個代理則專注於酒店預訂，依此類推。一個協調或“下游”代理可以將這些結果整合成一個連貫的行程提供給最終用戶。

這種模組化方法還允許逐步改進。例如，你可以增加專門的代理來提供餐飲推薦或當地活動建議，並隨著時間推進不斷完善行程。

### 結構化輸出

大型語言模型（LLMs）可以生成結構化輸出（例如 JSON），這更方便下游代理或服務進行解析和處理。這在多代理上下文中特別有用，因為我們可以在規劃輸出完成後執行這些任務。請參考這篇 [blogpost](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/cookbook/structured-output-agent.html) 以快速了解。

以下是一段示範簡單規劃代理如何將目標分解為子任務並生成結構化計劃的 Python 程式碼片段：

### 使用多代理協作的規劃代理

在此範例中，一個語義路由代理接收到用戶請求（例如，“我需要一個旅行的酒店計劃。”）。

規劃器接下來會執行以下步驟：

* 接收酒店計劃：規劃器接收用戶的訊息，並根據系統提示（包括可用代理的詳細資訊）生成結構化的旅行計劃。
* 列出代理及其工具：代理註冊表保存了代理的清單（例如航班、酒店、租車和活動代理）以及它們提供的功能或工具。
* 將計劃路由至相應的代理：根據子任務數量，規劃器會將訊息直接發送給專門代理（適用於單一任務情境）或通過群組聊天管理器協調多代理合作。
* 總結結果：最後，規劃器為清晰起見總結生成的計劃。

以下是說明這些步驟的 Python 程式碼範例：

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

以下是上述程式碼的輸出，你可以使用這個結構化輸出路由到 `assigned_agent`，並向最終用戶總結旅行計劃。

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

包含上述程式碼範例的範例筆記本可在 [這裡](../../../07-planning-design/code_samples/07-autogen.ipynb) 獲取。

### 迭代規劃

某些任務需要反覆調整或重新規劃，其中一個子任務的結果可能會影響下一步。例如，如果代理在預訂航班時發現了意外的數據格式，它可能需要調整策略，然後再進行酒店預訂。

此外，用戶反饋（例如人類決定更喜歡早班航班）也可能觸發部分重新規劃。這種動態、迭代的方法確保最終解決方案能夠符合現實約束和不斷變化的用戶偏好。

例如程式碼：

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

如需更全面的規劃，請參考 Magnetic One [Blogpost](https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks)，以了解如何解決複雜任務。

## 總結

在本文中，我們探討了一個如何創建規劃器的範例，該規劃器可以動態選擇定義的可用代理。規劃器的輸出分解了任務並分配給代理進行執行。假設代理可以訪問執行任務所需的功能/工具。除了代理之外，你還可以包含其他模式，例如反思、摘要器、輪詢聊天，以進一步自定義。

## 其他資源

* 使用 o1 推理模型在規劃複雜任務中已證明相當先進——TODO: 分享範例？

* Autogen Magentic One - 一個通用型多代理系統，用於解決複雜任務，並在多個具有挑戰性的代理基準測試中取得了令人印象深刻的成果。參考資料：[autogen-magentic-one](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one)。在此實現中，協作器創建特定任務的計劃，並將這些任務委派給可用的代理。除了規劃之外，協作器還採用跟蹤機制來監控任務進度並在需要時重新規劃。

**免責聲明**：  
本文件是使用機器翻譯AI服務進行翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。