# 設計の計画

## はじめに

このレッスンでは以下の内容を学びます：

* 明確な全体目標を定義し、複雑なタスクを扱いやすいタスクに分解する方法。
* 構造化された出力を活用して、信頼性が高く機械が読み取りやすい応答を得る方法。
* 動的なタスクや予期しない入力に対応するためのイベント駆動型アプローチを適用する方法。

## 学習目標

このレッスンを完了すると、次のことが理解できるようになります：

* AIエージェントの全体目標を特定し、設定することで、達成すべき内容を明確にする。
* 複雑なタスクを扱いやすいサブタスクに分解し、それらを論理的な順序で整理する。
* エージェントに適切なツール（例：検索ツールやデータ分析ツール）を装備させ、それらをいつ、どのように使用するかを決定し、予期しない状況に対応する。
* サブタスクの結果を評価し、パフォーマンスを測定し、最終的な出力を改善するためにアクションを繰り返す。

## 全体目標の定義とタスクの分解

![目標とタスクの定義](../../../translated_images/defining-goals-tasks.dcc1181bbdb194704ae0fb3363371562949e8b03fd2fadc256218aaadf84a9f4.ja.png)

多くの現実世界のタスクは、単一ステップで取り組むには複雑すぎます。AIエージェントには、計画と行動を導くための簡潔な目標が必要です。例えば、以下の目標を考えてみましょう：

    "3日間の旅行プランを作成する。"

この目標は一見シンプルですが、さらに具体化が必要です。目標が明確であればあるほど、エージェント（および人間の協力者）は、適切な結果を達成することに集中できます。例えば、フライトオプション、ホテルのおすすめ、アクティビティの提案を含む包括的な旅程を作成することが求められる場合です。

### タスクの分解

大規模または複雑なタスクは、小さく目標志向のサブタスクに分割することで扱いやすくなります。
旅行プランの例では、次のように目標を分解できます：

* フライト予約
* ホテル予約
* レンタカー手配
* パーソナライズ

各サブタスクは、専用のエージェントやプロセスによって処理されます。例えば、フライトの最適な料金を検索するエージェント、ホテル予約に特化したエージェントなどです。その後、調整役または「下流」のエージェントが、これらの結果をまとめてユーザーに一つの統合された旅程として提供します。

このモジュール式アプローチは、段階的な改善も可能にします。例えば、フードのおすすめや地元のアクティビティの提案に特化したエージェントを追加し、旅程をさらに洗練させることができます。

### 構造化された出力

大規模言語モデル（LLM）は、JSONのような構造化された出力を生成できます。これにより、下流のエージェントやサービスが解析・処理しやすくなります。これは特にマルチエージェント環境において有用で、計画出力を受け取った後にタスクを実行できます。この点については、[こちらのブログ記事](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/cookbook/structured-output-agent.html)をご参照ください。

以下は、計画エージェントが目標をサブタスクに分解し、構造化された計画を生成する簡単なPythonコードの例です：

### マルチエージェントオーケストレーションを活用した計画エージェント

この例では、Semantic Router Agentがユーザーのリクエスト（例："旅行のためのホテルプランが必要です。"）を受け取ります。

計画エージェントは以下の手順を実行します：

* **ホテルプランの受信**: エージェントはユーザーのメッセージを受け取り、システムプロンプト（利用可能なエージェントの詳細を含む）に基づいて構造化された旅行プランを生成します。
* **エージェントとそのツールの一覧化**: エージェントレジストリには、フライト、ホテル、レンタカー、アクティビティなどのエージェントリストと、それぞれが提供する機能やツールが含まれています。
* **プランの割り当て**: サブタスクの数に応じて、計画エージェントは専用エージェントに直接メッセージを送信する（単一タスクの場合）か、グループチャットマネージャーを介してマルチエージェントでのコラボレーションを調整します。
* **結果の要約**: 最後に、生成されたプランを要約して分かりやすくします。

以下はこれらのステップを示すPythonコードのサンプルです：

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

上記のコードから得られる出力例を以下に示します。この構造化された出力を使用して`assigned_agent`にルーティングし、旅行プランをエンドユーザーに要約して提供できます。

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

上記コードの例を含むノートブックは[こちら](../../../07-planning-design/code_samples/07-autogen.ipynb)から利用できます。

### 繰り返し計画

いくつかのタスクでは、結果に応じて計画を再調整する必要があります。例えば、エージェントがフライト予約中に予期しないデータ形式を発見した場合、戦略を適応させてからホテル予約に進む必要があるかもしれません。

さらに、ユーザーからのフィードバック（例：早い時間のフライトを希望する）によって、部分的な再計画が必要になる場合もあります。この動的で反復的なアプローチにより、最終的な解決策が現実の制約やユーザーの好みに適合することを確保します。

以下はその例を示すコードです：

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

より包括的な計画については、複雑なタスクを解決するためのMagnetic Oneに関する[ブログ記事](https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks)をご覧ください。

## まとめ

この記事では、利用可能なエージェントを動的に選択できるプランナーを作成する方法について説明しました。プランナーの出力はタスクを分解し、それぞれのエージェントに割り当てて実行されます。エージェントがタスクを実行するために必要な機能やツールにアクセスできることが前提です。さらに、リフレクションや要約、ラウンドロビンチャットなどのパターンを追加することで、さらにカスタマイズが可能です。

## 追加リソース

* o1推論モデルは、複雑なタスクの計画において非常に優れていることが証明されています - TODO: 例を共有予定？

* Autogen Magnetic One - 複雑なタスクを解決するための汎用マルチエージェントシステムであり、複数の難しいエージェントベンチマークで印象的な成果を上げています。参考：[autogen-magentic-one](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one)。この実装では、オーケストレーターがタスク固有の計画を作成し、これらのタスクを利用可能なエージェントに委任します。オーケストレーターは計画だけでなく、タスクの進行状況を監視し、必要に応じて再計画を行う追跡メカニズムも採用しています。

**免責事項**:  
本書類は、機械翻訳AIサービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳にはエラーや不正確さが含まれる可能性があることをご了承ください。原文（元の言語の文書）が公式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や解釈の誤りについて、当方は一切の責任を負いません。