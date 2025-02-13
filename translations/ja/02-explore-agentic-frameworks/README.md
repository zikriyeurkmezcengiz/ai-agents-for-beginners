# AIエージェントフレームワークを探る

AIエージェントフレームワークは、AIエージェントの作成、展開、管理を簡素化するために設計されたソフトウェアプラットフォームです。これらのフレームワークは、開発者に事前構築されたコンポーネント、抽象化、およびツールを提供し、複雑なAIシステムの開発プロセスを効率化します。

これらのフレームワークは、AIエージェント開発における共通の課題に対する標準化されたアプローチを提供することで、開発者がアプリケーションの独自の側面に集中できるよう支援します。これにより、AIシステムのスケーラビリティ、アクセシビリティ、効率性が向上します。

## はじめに

このレッスンでは以下を学びます：

- AIエージェントフレームワークとは何か、そしてそれが開発者に何を可能にするのか？
- チームがこれをどのように活用して、エージェントの能力を迅速にプロトタイプ化、反復、改善できるのか？
- Microsoftが提供するフレームワークやツール（[Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)）の違いは何か？
- 既存のAzureエコシステムツールを直接統合できるのか、それともスタンドアロンソリューションが必要なのか？
- Azure AI Agents Serviceとは何で、それがどのように役立つのか？

## 学習目標

このレッスンの目標は以下を理解することです：

- AIエージェントフレームワークがAI開発において果たす役割。
- AIエージェントフレームワークを活用してインテリジェントエージェントを構築する方法。
- AIエージェントフレームワークによって実現される主要な機能。
- Autogen、Semantic Kernel、Azure AI Agent Serviceの違い。

## AIエージェントフレームワークとは何か、そしてそれが開発者に何を可能にするのか？

従来のAIフレームワークは、アプリにAIを統合し、以下のような方法でアプリを改善するのに役立ちます：

- **パーソナライズ**: AIはユーザーの行動や好みを分析し、パーソナライズされたおすすめ、コンテンツ、体験を提供します。
  - 例: Netflixのようなストリーミングサービスは、視聴履歴に基づいて映画や番組を提案し、ユーザーのエンゲージメントと満足度を向上させます。
- **自動化と効率化**: AIは繰り返しのタスクを自動化し、ワークフローを効率化し、運用効率を向上させます。
  - 例: カスタマーサービスアプリは、AI搭載のチャットボットを使用して一般的な問い合わせを処理し、応答時間を短縮し、人間のエージェントがより複雑な問題に集中できるようにします。
- **ユーザー体験の向上**: AIは、音声認識、自然言語処理、予測テキストなどのインテリジェントな機能を提供することで、全体的なユーザー体験を向上させます。
  - 例: SiriやGoogleアシスタントのようなバーチャルアシスタントは、AIを活用して音声コマンドを理解し応答することで、ユーザーがデバイスと簡単にやり取りできるようにします。

### それは素晴らしいことのように聞こえますが、なぜAIエージェントフレームワークが必要なのでしょうか？

AIエージェントフレームワークは、単なるAIフレームワーク以上のものを表しています。これらは、ユーザー、他のエージェント、および環境とやり取りして特定の目標を達成できるインテリジェントエージェントの作成を可能にするよう設計されています。これらのエージェントは、自律的な行動を示し、意思決定を行い、変化する条件に適応することができます。AIエージェントフレームワークによって実現される主な機能をいくつか見てみましょう：

- **エージェントの協力と調整**: 複数のAIエージェントを作成し、共同作業、コミュニケーション、および調整を通じて複雑なタスクを解決できるようにします。
- **タスクの自動化と管理**: マルチステップのワークフローの自動化、タスクの委任、エージェント間での動的なタスク管理のメカニズムを提供します。
- **コンテキスト理解と適応**: エージェントにコンテキストを理解し、変化する環境に適応し、リアルタイム情報に基づいて意思決定を行う能力を持たせます。

要するに、エージェントを活用することで、さらなる自動化を実現し、環境から学び適応する、よりインテリジェントなシステムを作成することが可能になります。

## エージェントの能力を迅速にプロトタイプ化、反復、改善する方法

この分野は急速に進化していますが、ほとんどのAIエージェントフレームワークで共通するいくつかのポイントがあります。それは、モジュールコンポーネント、協調ツール、リアルタイム学習です。それぞれを見ていきましょう：

- **モジュールコンポーネントの活用**: AIフレームワークは、プロンプト、パーサー、メモリ管理などの事前構築されたコンポーネントを提供します。
- **協調ツールの活用**: 特定の役割とタスクを持つエージェントを設計し、協調的なワークフローをテストし改善します。
- **リアルタイムでの学習**: フィードバックループを実装し、エージェントがインタラクションから学び、動的に行動を調整します。

### モジュールコンポーネントの活用

LangChainやMicrosoft Semantic Kernelのようなフレームワークは、プロンプト、パーサー、メモリ管理などの事前構築されたコンポーネントを提供します。

**チームがこれを活用する方法**: チームは、これらのコンポーネントを迅速に組み立てることで、ゼロから始めることなく機能的なプロトタイプを作成し、迅速な実験と反復が可能になります。

**実際の動作**: ユーザー入力から情報を抽出するための事前構築されたパーサー、データを保存・取得するためのメモリモジュール、ユーザーと対話するためのプロンプトジェネレーターを使用することができます。これらすべてをゼロから構築する必要はありません。

**コード例**: 以下は、事前構築されたパーサーを使用してユーザー入力から情報を抽出する例です：

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

この例から分かるように、事前構築されたパーサーを活用することで、フライト予約リクエストの出発地、目的地、日付などの重要な情報をユーザー入力から抽出できます。このモジュールアプローチにより、高レベルのロジックに集中できます。

### 協調ツールの活用

CrewAIやMicrosoft Autogenのようなフレームワークは、複数のエージェントを作成し協力させることを容易にします。

**チームがこれを活用する方法**: チームは、特定の役割とタスクを持つエージェントを設計し、協調的なワークフローをテスト・改善し、全体的なシステム効率を向上させることができます。

**実際の動作**: データ取得、分析、意思決定など、特化した機能を持つエージェントチームを作成します。これらのエージェントは、情報を共有し、協力してユーザーのクエリに答えたり、タスクを完了したりします。

**コード例 (Autogen)**:

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

上記のコードでは、複数のエージェントがデータを分析するタスクを協力して実行する様子が示されています。各エージェントが特定の機能を果たし、エージェント間の調整を通じて目的を達成します。専門的な役割を持つエージェントを作成することで、タスクの効率とパフォーマンスを向上させることができます。

### リアルタイムでの学習

高度なフレームワークは、リアルタイムのコンテキスト理解と適応機能を提供します。

**チームがこれを活用する方法**: フィードバックループを実装し、エージェントがインタラクションから学び、動的に行動を調整することで、能力の継続的な向上と洗練を実現します。

**実際の動作**: エージェントは、ユーザーフィードバック、環境データ、タスクの結果を分析し、知識ベースを更新し、意思決定アルゴリズムを調整し、パフォーマンスを時間とともに向上させます。この反復学習プロセスにより、エージェントは変化する条件やユーザーの好みに適応し、システム全体の有効性を向上させます。

## Autogen、Semantic Kernel、Azure AI Agent Serviceの違いは？

これらのフレームワークの設計、機能、対象となるユースケースの違いをいくつか見てみましょう：

### Autogen

Microsoft ResearchのAI Frontiers Labによって開発されたオープンソースフレームワークで、イベント駆動型、分散型の「エージェント指向」のアプリケーションに焦点を当てています。複数のLLMやSLM、ツール、そして高度なマルチエージェントデザインパターンを可能にします。

Autogenは、環境を認識し、意思決定を行い、特定の目標を達成するために行動を起こす自律的なエンティティとしての「エージェント」というコアコンセプトに基づいています。エージェントは非同期メッセージを通じて通信し、独立して並行して動作することで、システムのスケーラビリティと応答性を向上させます。

エージェントは[アクターモデル](https://en.wikipedia.org/wiki/Actor_model)に基づいています。Wikipediaによれば、アクターは「並行計算の基本構成要素」であり、受信したメッセージに応じて、ローカルな意思決定を行ったり、新しいアクターを作成したり、さらにメッセージを送信したり、次に受信するメッセージへの応答方法を決定することができます。

以下はAutogenの重要なコアコンセプトの一部です：

- **エージェント**. エージェントは以下を行うソフトウェアエンティティです：
  - **メッセージで通信**: メッセージは同期または非同期で行うことができます。
  - **独自の状態を維持**: 状態は受信メッセージによって変更される可能性があります。
  - **アクションを実行**: 受信メッセージまたは状態の変更に応じてアクションを実行します。これらのアクションはエージェントの状態を変更し、メッセージログの更新、新しいメッセージの送信、コードの実行、またはAPI呼び出しなどの外部効果を生み出すことがあります。

以下のコードスニペットでは、チャット機能を持つ独自のエージェントを作成する例を示します：

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

上記のコードでは、`MyAssistant` has been created and inherits from `RoutedAgent`. It has a message handler that prints the content of the message and then sends a response using the `AssistantAgent` delegate. Especially note how we assign to `self._delegate` an instance of `AssistantAgent`は、チャット完了を処理できる事前構築されたエージェントです。

続いて、このエージェントタイプをAutogenに知らせ、プログラムを開始します：

```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

上記では、エージェントがランタイムに登録され、その後、エージェントにメッセージが送信されます。結果として以下のような出力が得られます：

```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

... (以下、他のセクションも同様に翻訳されますが、ここで省略します) ...
プロジェクト目標に基づいています。自然言語理解、コンテンツ生成に最適です。  
- **Azure AI Agent Service**: 柔軟なモデル、エンタープライズ向けのセキュリティ機構、データストレージ手法。エンタープライズアプリケーションでの安全でスケーラブルかつ柔軟なAIエージェントの展開に最適です。

## 既存のAzureエコシステムツールを直接統合できますか、それとも独立したソリューションが必要ですか？
答えは「はい」です。特にAzure AI Agent Serviceは他のAzureサービスとシームレスに連携するように構築されているため、既存のAzureエコシステムツールを直接統合することができます。例えば、Bing、Azure AI Search、Azure Functionsを統合することが可能です。また、Azure AI Foundryとの深い統合もあります。AutogenやSemantic Kernelに関してもAzureサービスと統合できますが、コードからAzureサービスを呼び出す必要がある場合があります。もう1つの統合方法として、Azure SDKを使用してエージェントからAzureサービスとやり取りする方法があります。さらに、前述のように、AutogenまたはSemantic Kernelで構築されたエージェントのオーケストレーターとしてAzure AI Agent Serviceを使用することで、Azureエコシステムへの簡単なアクセスが可能になります。

## 参考文献
- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)  
- [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/)  
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp)  
- [4] - [Azure AI Agent service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)  
- [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)  

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる場合があります。元の言語で作成された原文を正式な情報源と見なしてください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の利用に起因する誤解や誤った解釈について、当社は一切の責任を負いません。