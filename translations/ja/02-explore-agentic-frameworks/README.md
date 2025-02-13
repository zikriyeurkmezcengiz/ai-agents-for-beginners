```markdown
# AIエージェントフレームワークを探る

AIエージェントフレームワークは、AIエージェントの作成、展開、管理を簡素化するために設計されたソフトウェアプラットフォームです。これらのフレームワークは、複雑なAIシステムの開発を効率化するための事前構築されたコンポーネント、抽象化、およびツールを開発者に提供します。

これらのフレームワークは、AIエージェント開発における共通の課題に対する標準化されたアプローチを提供することで、開発者がアプリケーションの独自の側面に集中できるようにします。それにより、AIシステムのスケーラビリティ、アクセシビリティ、効率性が向上します。

## はじめに

このレッスンでは以下を学びます：

- AIエージェントフレームワークとは何か、そしてそれが開発者に何を可能にするのか？
- チームはこれらをどのように使用して、エージェントの能力を迅速にプロトタイプ化、反復、改善できるのか？
- Microsoftが提供するフレームワークとツール（[Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)）の違いは何か？
- 既存のAzureエコシステムツールを直接統合できるのか、それとも独立したソリューションが必要なのか？
- Azure AI Agentsサービスとは何か、そしてそれがどのように役立つのか？

## 学習目標

このレッスンの目標は以下を理解することです：

- AIエージェントフレームワークがAI開発で果たす役割。
- AIエージェントフレームワークを活用してインテリジェントなエージェントを構築する方法。
- AIエージェントフレームワークによって可能になる主要な機能。
- Autogen、Semantic Kernel、Azure AI Agent Serviceの違い。

## AIエージェントフレームワークとは何か、そしてそれが開発者に何を可能にするのか？

従来のAIフレームワークは、AIをアプリに統合し、以下の方法でアプリを改善するのに役立ちます：

- **パーソナライズ**: AIはユーザーの行動や好みを分析し、個別化された推奨、コンテンツ、体験を提供できます。  
  例：Netflixのようなストリーミングサービスは、視聴履歴に基づいて映画や番組を提案し、ユーザーのエンゲージメントと満足度を向上させます。

- **自動化と効率化**: AIは反復的なタスクを自動化し、ワークフローを合理化し、運用効率を向上させます。  
  例：カスタマーサービスアプリは、AI搭載のチャットボットを使用して一般的な問い合わせを処理し、応答時間を短縮し、複雑な問題に対処するために人間のエージェントの時間を解放します。

- **ユーザー体験の向上**: AIは、音声認識、自然言語処理、予測テキストなどのインテリジェントな機能を提供することで、全体的なユーザー体験を向上させます。  
  例：SiriやGoogleアシスタントのようなバーチャルアシスタントは、AIを活用して音声コマンドを理解し応答し、ユーザーがデバイスと簡単にやり取りできるようにします。

### それは素晴らしいですが、なぜAIエージェントフレームワークが必要なのでしょうか？

AIエージェントフレームワークは、単なるAIフレームワーク以上のものを提供します。それは、ユーザー、他のエージェント、環境とやり取りし、特定の目標を達成するインテリジェントエージェントの作成を可能にするために設計されています。これらのエージェントは自律的な行動を示し、意思決定を行い、変化する条件に適応することができます。以下は、AIエージェントフレームワークが可能にする主な機能です：

- **エージェントの協調と連携**: 複数のAIエージェントを作成し、協力、通信、連携して複雑なタスクを解決することを可能にします。
- **タスクの自動化と管理**: マルチステップのワークフローの自動化、タスクの委任、エージェント間の動的タスク管理の仕組みを提供します。
- **コンテキストの理解と適応**: エージェントがコンテキストを理解し、変化する環境に適応し、リアルタイム情報に基づいて意思決定を行う能力を備えています。

要するに、エージェントはより多くのことを可能にし、自動化を次のレベルに引き上げ、環境から学び適応するよりインテリジェントなシステムを作成できるようにします。

## エージェントの能力を迅速にプロトタイプ化、反復、改善する方法

この分野は急速に進化していますが、ほとんどのAIエージェントフレームワークに共通するいくつかの要素があります。それらは、モジュールコンポーネント、コラボレーションツール、リアルタイム学習です。以下に詳しく見ていきましょう：

- **モジュールコンポーネントを活用する**: AIフレームワークは、プロンプト、パーサー、メモリ管理などの事前構築されたコンポーネントを提供します。
- **コラボレーションツールを活用する**: 特定の役割とタスクを持つエージェントを設計し、協力的なワークフローをテストして改善します。
- **リアルタイムで学習する**: エージェントが相互作用から学び、動的に行動を調整するフィードバックループを実装します。

### モジュールコンポーネントを活用する

LangChainやMicrosoft Semantic Kernelのようなフレームワークは、プロンプト、パーサー、メモリ管理などの事前構築されたコンポーネントを提供します。

**チームがこれらを活用する方法**: チームはこれらのコンポーネントを迅速に組み合わせて機能的なプロトタイプを作成し、ゼロから始めることなく迅速な実験と反復を可能にします。

**実際の使用例**: 事前構築されたパーサーを使用してユーザー入力から情報を抽出し、メモリモジュールを使用してデータを保存および取得し、プロンプトジェネレーターを使用してユーザーとやり取りすることができます。

**コード例**。以下は、事前構築されたパーサーを使用してユーザー入力から情報を抽出する方法の例です：

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

この例からわかるように、事前構築されたパーサーを活用して、フライト予約リクエストの出発地、目的地、日付などの重要な情報をユーザー入力から抽出する方法が示されています。このモジュール式のアプローチにより、高レベルのロジックに集中することができます。

### コラボレーションツールを活用する

CrewAIやMicrosoft Autogenのようなフレームワークは、複数のエージェントを作成することを容易にします。

**チームがこれらを活用する方法**: チームは特定の役割とタスクを持つエージェントを設計し、協力的なワークフローをテストして改善し、システム全体の効率を向上させます。

**実際の使用例**: 各エージェントがデータの取得、分析、意思決定などの特化した機能を持つチームを作成します。これらのエージェントは通信し、情報を共有して、ユーザーの質問に答えたり、タスクを完了したりする共通の目標を達成します。

**コード例（Autogen）**:

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

上記のコードでは、複数のエージェントが協力してデータを分析するタスクを作成する方法が示されています。それぞれのエージェントが特定の機能を果たし、協調してタスクを実行し、目的の結果を達成します。専用の役割を持つエージェントを作成することで、タスクの効率とパフォーマンスを向上させることができます。

### リアルタイムで学習する

高度なフレームワークは、リアルタイムのコンテキスト理解と適応の機能を提供します。

**チームがこれらを活用する方法**: チームは、エージェントが相互作用から学び、動的に行動を調整するフィードバックループを実装することで、能力の継続的な改善と洗練を実現します。

**実際の使用例**: エージェントは、ユーザーフィードバック、環境データ、タスクの結果を分析して知識ベースを更新し、意思決定アルゴリズムを調整し、時間とともにパフォーマンスを向上させます。この反復的な学習プロセスにより、エージェントは変化する条件やユーザーの好みに適応し、システム全体の有効性を向上させます。

## Autogen、Semantic Kernel、Azure AI Agent Serviceの違いは何ですか？

これらのフレームワークを比較する方法はいくつかありますが、設計、機能、対象とするユースケースに基づいて主な違いを見ていきましょう：

## Autogen

Microsoft ResearchのAI Frontiers Labによって開発されたオープンソースのフレームワークです。イベント駆動型で分散型の*エージェント的*アプリケーションに焦点を当て、複数のLLMやSLM、ツール、そして高度なマルチエージェントデザインパターンを可能にします。

Autogenは、環境を認識し、意思決定を行い、特定の目標を達成するために行動を起こす自律的なエンティティであるエージェントというコアコンセプトに基づいて構築されています。エージェントは非同期メッセージを通じて通信し、独立して並行して作業することで、システムのスケーラビリティと応答性を向上させます。

エージェントは[アクターモデル](https://en.wikipedia.org/wiki/Actor_model)に基づいています。Wikipediaによれば、アクターは_並行計算の基本構成要素であり、受信したメッセージに応じてローカルな意思決定を行い、新しいアクターを作成し、新しいメッセージを送信し、次に受信するメッセージへの応答方法を決定できる_とされています。

**ユースケース**: コード生成の自動化、データ分析タスク、計画および研究機能のためのカスタムエージェントの構築。

Autogenの重要なコアコンセプトの一部を以下に示します：

- **エージェント**. エージェントは以下を行うソフトウェアエンティティです：
  - **メッセージを介して通信する**。これらのメッセージは同期または非同期である可能性があります。
  - **独自の状態を維持する**。この状態は、受信したメッセージによって変更される可能性があります。
  - **アクションを実行する**。受信したメッセージや状態の変化に応じてアクションを実行します。このアクションは、エージェントの状態を変更し、メッセージログの更新、新しいメッセージの送信、コードの実行、またはAPI呼び出しなどの外部効果を生成する可能性があります。

  ここで、チャット機能を持つ独自のエージェントを作成する短いコードスニペットを示します：

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    上記のコードでは、`MyAssistant` has been created and inherits from `RoutedAgent`. It has a message handler that prints the content of the message and then sends a response using the `AssistantAgent` delegate. Especially note how we assign to `self._delegate` an instance of `AssistantAgent` という事前構築されたエージェントがチャット完了を処理します。

    次に、このエージェントタイプをAutogenに認識させ、プログラムを開始します：

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    上記では、エージェントがランタイムに登録され、エージェントにメッセージが送信されます。その結果、以下の出力が生成されます：

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **マルチエージェント**. Autogenは、複数のエージェントを作成し、協力して複雑なタスクを達成することをサポートします。エージェントは情報を共有し、問題を効率的に解決するためにアクションを調整できます。複数のエージェントを持つシステムを作成するには、データ取得、分析、意思決定、ユーザーとの対話などの特化した機能と役割を持つさまざまなタイプのエージェントを定義できます。以下はそのような作成方法の例です：

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    上記では、`GroupChatManager` がランタイムに登録されています。このマネージャーは、ライター、イラストレーター、エディター、ユーザーなど、さまざまなタイプのエージェント間のやり取りを調整する役割を果たします。

- **エージェントランタイム**. フレームワークは、エージェント間の通信を可能にし、エージェントの識別情報とライフサイクルを管理し、セキュリティとプライバシーの境界を強制するランタイム環境を提供します。これにより、エージェントを安全かつ制御された環境で実行し、効率的かつ安全に相互作用できるようにします。興味深いランタイムは2つあります：
  - **スタンドアロンランタイム**. 単一プロセスアプリケーションに適しており、すべてのエージェントが同じプログラミング言語で実装され、同じプロセスで実行されます。以下はその動作のイメージです：
  
  ![スタンドアロンランタイム](https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg)   
  アプリケーションスタック

    *エージェントはランタイムを介してメッセージで通信し、ランタイムはエージェントのライフサイクルを管理します*

  - **分散エージェントランタイム**. 異なるプログラミング言語で実装されたエージェントが異なるマシン上で実行されるマルチプロセスアプリケーションに適しています。以下はその動作のイメージです：
  
  ![分散ランタイム](https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg)

## Semantic Kernel + エージェントフレームワーク

Semantic Kernelは、Semantic KernelエージェントフレームワークとSemantic Kernelそのものの2つの要素で構成されています。

まずSemantic Kernelについて説明します。そのコアコンセプトは以下の通りです：

- **接続**: 外部のAIサービスやデータソースとのインターフェース。

    ```csharp
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    ここでは、カーネルを作成し、チャット補完サービスを追加するシンプルな例を示しています。Semantic Kernelは外部AIサービス、今回はAzure OpenAI Chat Completionへの接続を作成します。

- **プラグイン**: アプリケーションが使用できる関数をカプセル化します。既製のプラグインもあれば、自分で作成することも可能です。ここには「セマンティック関数」という概念があります。この関数がセマンティックと呼ばれるのは、Semantic Kernelがこの関数が
プロジェクト目標に基づく。自然言語理解やコンテンツ生成に最適。  
- **Azure AI Agent Service**: 柔軟なモデル、企業向けセキュリティメカニズム、データストレージ方法を提供。企業アプリケーションでの安全でスケーラブルかつ柔軟なAIエージェントの導入に最適。

## 既存のAzureエコシステムツールを直接統合できますか、それともスタンドアロンのソリューションが必要ですか？

答えは「はい」です。既存のAzureエコシステムツールをAzure AI Agent Serviceと直接統合できます。特に、このサービスは他のAzureサービスとシームレスに連携するように設計されています。たとえば、Bing、Azure AI Search、Azure Functionsと統合することができます。また、Azure AI Foundryとの深い統合もあります。

AutogenやSemantic Kernelの場合もAzureサービスと統合可能ですが、コードからAzureサービスを呼び出す必要がある場合があります。もう一つの統合方法として、Azure SDKを使用してエージェントからAzureサービスとやり取りする方法があります。

さらに、前述のように、AutogenやSemantic Kernelで構築したエージェントのオーケストレーターとしてAzure AI Agent Serviceを使用することで、Azureエコシステムへの簡単なアクセスが可能になります。

## 参考文献  
- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)  
- [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/)  
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp)  
- [4] - [Azure AI Agent service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)  
- [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)  

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。元の言語で書かれた原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用により生じた誤解や誤った解釈について、当方は責任を負いかねます。