# 設計の計画

## はじめに

このレッスンでは以下の内容を学びます：

* 明確な全体目標を定義し、複雑なタスクを管理可能なタスクに分解する方法。
* 構造化された出力を活用して、より信頼性が高く機械可読な応答を得る方法。
* イベント駆動型アプローチを適用し、動的なタスクや予期しない入力に対応する方法。

## 学習目標

このレッスンを修了すると、次のことが理解できるようになります：

* AIエージェントの全体目標を設定し、何を達成すべきかを明確に認識させる。
* 複雑なタスクを管理可能なサブタスクに分解し、それらを論理的な順序で整理する。
* 適切なツール（例: 検索ツールやデータ分析ツール）をエージェントに装備させ、いつどのようにそれらを使用するかを判断し、発生する予期しない状況に対処する。
* サブタスクの成果を評価し、パフォーマンスを測定し、最終的な成果を改善するためにアクションを繰り返す。

## 全体目標の定義とタスクの分解

![目標とタスクの定義](../../../translated_images/defining-goals-tasks.dcc1181bbdb194704ae0fb3363371562949e8b03fd2fadc256218aaadf84a9f4.ja.png)

現実世界のほとんどのタスクは、一度にすべてを解決するには複雑すぎます。AIエージェントには、計画と行動を導くための簡潔な目標が必要です。例えば、次のような目標を考えてみましょう：

    "3日間の旅行プランを作成する。"

この目標はシンプルに見えますが、まだ洗練が必要です。目標が明確であればあるほど、エージェント（および人間の協力者）は適切な成果を達成することに集中できます。例えば、フライトオプション、ホテルの推奨、アクティビティの提案を含む包括的な旅程を作成することです。

### タスクの分解

大規模または複雑なタスクは、より小さく目標指向のサブタスクに分割することで、管理が容易になります。
旅行プランの例では、目標を次のように分解できます：

* フライト予約
* ホテル予約
* レンタカー
* パーソナライズ

それぞれのサブタスクは、専用のエージェントやプロセスによって処理されます。例えば、あるエージェントは最適なフライトの検索に特化し、別のエージェントはホテル予約を担当する、という具合です。そして、調整役や「下流の」エージェントがこれらの結果を統合し、最終的な旅程としてユーザーに提供します。

このモジュール型アプローチにより、段階的な改善も可能になります。例えば、食事の提案や現地アクティビティの提案に特化したエージェントを追加して、旅程をさらに洗練させることができます。

### 構造化された出力

大規模言語モデル（LLM）は、構造化された出力（例: JSON）を生成できます。これは、下流のエージェントやサービスが解析・処理しやすくするために特に有用です。マルチエージェント環境では、計画出力を受け取った後にこれらのタスクを実行することができます。この点については、[このブログ記事](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/cookbook/structured-output-agent.html)を参照してください。

以下は、目標をサブタスクに分解し、構造化された計画を生成するシンプルなプランニングエージェントを示すPythonコードの例です：

### マルチエージェントオーケストレーションを用いたプランニングエージェント

この例では、Semantic Router Agentがユーザーリクエスト（例: "旅行のホテルプランが必要です。"）を受け取ります。

プランナーは次のステップを実行します：

* ホテルプランの受信：プランナーはユーザーのメッセージを受け取り、システムプロンプト（利用可能なエージェントの詳細を含む）に基づいて構造化された旅行プランを生成します。
* エージェントとそのツールのリスト化：エージェントレジストリには、フライト、ホテル、レンタカー、アクティビティなどのエージェントと、それらが提供する機能やツールのリストが含まれています。
* プランの適切なエージェントへのルーティング：サブタスクの数に応じて、プランナーはメッセージを専用のエージェント（単一タスクの場合）に直接送信するか、マルチエージェントコラボレーションのためにグループチャットマネージャーを介して調整します。
* 結果の要約：最後に、プランナーは生成されたプランを明確に要約します。

以下は、これらのステップを示すPythonコードサンプルです：

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

上記のコードからの出力例を以下に示します。この構造化された出力を使用して`assigned_agent`にルーティングし、最終的な旅行プランをユーザーに要約することができます。

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

上記のコードサンプルを含むサンプルノートブックは[こちら](../../../07-planning-design/07-autogen.ipynb)で利用可能です。

### 繰り返し型の計画

一部のタスクでは、結果に応じた再計画ややり取りが必要です。例えば、フライト予約中に予期しないデータ形式が見つかった場合、次のステップに進む前に戦略を適応させる必要があるかもしれません。

また、ユーザーからのフィードバック（例: 「もっと早い時間のフライトが良い」という人間の判断）が部分的な再計画を引き起こすこともあります。この動的で反復的なアプローチにより、最終的なソリューションが現実的な制約や進化するユーザーの好みに一致することを保証します。

例：サンプルコード

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

より包括的な計画については、複雑なタスクを解決するためのMagnetic Oneに関する[ブログ記事](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks)をご覧ください。

## まとめ

この記事では、利用可能なエージェントを動的に選択できるプランナーの作成方法について例を示しました。プランナーの出力はタスクを分解し、エージェントに割り当てて実行するようにします。エージェントは、タスクを実行するために必要な関数やツールにアクセスできることが前提です。さらに、エージェントに加えて、リフレクション、要約、ラウンドロビンチャットなどのパターンを含めることで、さらにカスタマイズすることができます。

## 追加リソース

* o1推論モデルを使用することで、複雑なタスクの計画が非常に高度化しています - TODO: サンプルを共有する？

* Autogen Magnetic One - 複雑なタスクを解決するための汎用的なマルチエージェントシステムであり、複数の難しいエージェントベンチマークで印象的な結果を達成しています。参照：[autogen-magentic-one](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one)。この実装では、オーケストレーターがタスク固有の計画を作成し、それらのタスクを利用可能なエージェントに委任します。計画に加えて、オーケストレーターはタスクの進捗を追跡し、必要に応じて再計画を行う仕組みも採用しています。

**免責事項**:  
本書類は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。原文（原言語の文書）が公式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や誤認について、当社は一切の責任を負いません。