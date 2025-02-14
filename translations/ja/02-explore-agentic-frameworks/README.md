# AIエージェントフレームワークを探る

AIエージェントフレームワークは、AIエージェントの作成、展開、管理を簡素化するために設計されたソフトウェアプラットフォームです。これらのフレームワークは、開発者にあらかじめ構築されたコンポーネント、抽象化、およびツールを提供し、複雑なAIシステムの開発を効率化します。

これらのフレームワークは、AIエージェント開発における共通の課題に対して標準化されたアプローチを提供することで、開発者がアプリケーションの独自の側面に集中できるようにします。また、AIシステムのスケーラビリティ、アクセシビリティ、効率性を向上させます。

## はじめに

このレッスンでは以下について学びます：

- AIエージェントフレームワークとは何か、そしてそれによって開発者が何を実現できるのか？
- チームがこれらをどのように活用して、エージェントの能力を迅速にプロトタイプ化、反復、改善できるのか？
- Microsoftが提供するフレームワークとツール（[Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service)）の違いは何か？
- 既存のAzureエコシステムツールを直接統合できるのか、それともスタンドアロンのソリューションが必要なのか？
- Azure AI Agentsサービスとは何で、それがどのように役立つのか？

## 学習目標

このレッスンの目標は以下を理解することです：

- AI開発におけるAIエージェントフレームワークの役割。
- AIエージェントフレームワークを活用してインテリジェントエージェントを構築する方法。
- AIエージェントフレームワークによって可能になる主要な機能。
- Autogen、Semantic Kernel、Azure AI Agent Serviceの違い。

## AIエージェントフレームワークとは何か、そしてそれによって開発者が何を実現できるのか？

従来のAIフレームワークは、AIをアプリに統合し、それらのアプリを以下の方法で改善するのに役立ちます：

- **パーソナライズ**: AIはユーザーの行動や好みを分析し、パーソナライズされた推奨、コンテンツ、体験を提供します。  
例: Netflixのようなストリーミングサービスは、視聴履歴に基づいて映画や番組を提案し、ユーザーのエンゲージメントと満足度を向上させます。
- **自動化と効率化**: AIは反復的なタスクを自動化し、ワークフローを合理化し、運用効率を向上させます。  
例: カスタマーサービスアプリは、AI搭載のチャットボットを使用して一般的な問い合わせを処理し、応答時間を短縮し、人間のエージェントがより複雑な問題に集中できるようにします。
- **ユーザーエクスペリエンスの向上**: AIは音声認識、自然言語処理、予測テキストなどのインテリジェント機能を提供することで、全体的なユーザー体験を向上させます。  
例: SiriやGoogleアシスタントのようなバーチャルアシスタントは、AIを使用して音声コマンドを理解し応答し、ユーザーがデバイスと簡単にやり取りできるようにします。

### それは素晴らしいことのように聞こえますが、なぜAIエージェントフレームワークが必要なのでしょうか？

AIエージェントフレームワークは、単なるAIフレームワーク以上のものを表しています。それは、特定の目標を達成するために、ユーザー、他のエージェント、環境とやり取りできるインテリジェントエージェントの作成を可能にするように設計されています。これらのエージェントは、自律的な行動を示し、意思決定を行い、変化する条件に適応することができます。AIエージェントフレームワークによって可能になる主要な機能をいくつか見てみましょう：

- **エージェントの協調と調整**: 複数のAIエージェントを作成し、それらが協力し、通信し、調整して複雑なタスクを解決することを可能にします。
- **タスクの自動化と管理**: 複数ステップのワークフローの自動化、タスクの委任、エージェント間の動的タスク管理の仕組みを提供します。
- **コンテキストの理解と適応**: エージェントがコンテキストを理解し、変化する環境に適応し、リアルタイムの情報に基づいて意思決定を行う能力を備えています。

要するに、エージェントを活用することで、より多くのことを行い、自動化を次のレベルに引き上げ、環境から学び適応できるよりインテリジェントなシステムを作成できるのです。

## エージェントの能力を迅速にプロトタイプ化、反復、改善するには？

この分野は急速に進化していますが、ほとんどのAIエージェントフレームワークに共通する点がいくつかあります。それは、モジュール型コンポーネント、協調ツール、リアルタイム学習です。以下にそれらを詳しく見ていきましょう：

- **モジュール型コンポーネントの利用**: AIフレームワークは、プロンプト、パーサー、メモリ管理などのあらかじめ構築されたコンポーネントを提供します。
- **協調ツールの活用**: 特定の役割やタスクを持つエージェントを設計し、協調的なワークフローをテストして改善します。
- **リアルタイムで学ぶ**: フィードバックループを実装し、エージェントがインタラクションから学び、動的に行動を調整します。

### モジュール型コンポーネントの利用

LangChainやMicrosoft Semantic Kernelのようなフレームワークは、プロンプト、パーサー、メモリ管理などのあらかじめ構築されたコンポーネントを提供します。

**チームがこれらを活用する方法**: チームはこれらのコンポーネントを迅速に組み立てて、ゼロから始めることなく機能的なプロトタイプを作成し、迅速な実験と反復を可能にします。

**実際の動作方法**: あらかじめ構築されたパーサーを使用してユーザー入力から情報を抽出し、メモリモジュールを使用してデータを保存および取得し、プロンプトジェネレーターを使用してユーザーと対話することができます。これらすべてをゼロから構築する必要はありません。

**コード例**: 以下は、あらかじめ構築されたパーサーを使用してユーザー入力から情報を抽出する方法の例です：

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

この例からわかるように、あらかじめ構築されたパーサーを活用して、フライト予約リクエストの出発地、目的地、日付などの重要な情報をユーザー入力から抽出できます。このモジュール型アプローチにより、高レベルのロジックに集中することができます。

### 協調ツールの活用

CrewAIやMicrosoft Autogenのようなフレームワークは、複数のエージェントを作成して連携させることを容易にします。

**チームがこれらを活用する方法**: チームは特定の役割やタスクを持つエージェントを設計し、協調的なワークフローをテストして洗練し、システム全体の効率を向上させることができます。

**実際の動作方法**: データ取得、分析、意思決定などの特定の機能を持つエージェントチームを作成できます。これらのエージェントは通信し、情報を共有して、ユーザーの質問に答えたり、タスクを完了したりする共通の目標を達成します。

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

上記のコードでは、複数のエージェントがデータを分析するタスクを協調して実行する例を示しています。それぞれのエージェントが特定の機能を果たし、エージェントを調整して目標を達成します。専用の役割を持つエージェントを作成することで、タスクの効率とパフォーマンスを向上させることができます。

### リアルタイムで学ぶ

高度なフレームワークは、リアルタイムでのコンテキスト理解と適応機能を提供します。

**チームがこれらを活用する方法**: チームはフィードバックループを実装し、エージェントがインタラクションから学び、動的に行動を調整することで、能力の継続的な向上と洗練を実現します。

**実際の動作方法**: エージェントはユーザーのフィードバック、環境データ、タスクの結果を分析して知識ベースを更新し、意思決定アルゴリズムを調整し、時間とともにパフォーマンスを向上させます。この反復学習プロセスにより、エージェントは変化する条件やユーザーの好みに適応し、システム全体の効果を向上させます。

## Autogen、Semantic Kernel、Azure AI Agent Serviceの違いとは？

これらのフレームワークを比較する方法はいくつかありますが、その設計、機能、対象ユースケースに基づいて主な違いを見てみましょう。

### Autogen

Microsoft ResearchのAI Frontiers Labによって開発されたオープンソースフレームワークです。イベント駆動型の分散型エージェンティックアプリケーションに焦点を当てており、複数のLLMやSLM、ツール、高度なマルチエージェント設計パターンをサポートします。

Autogenは、エージェントというコアコンセプトに基づいて構築されています。エージェントとは、環境を認識し、意思決定を行い、特定の目標を達成するために行動を起こす自律的なエンティティです。エージェントは非同期メッセージを通じて通信し、独立して並列に動作することで、システムのスケーラビリティと応答性を向上させます。

エージェントは[アクターモデル](https://en.wikipedia.org/wiki/Actor_model)に基づいています。Wikipediaによると、アクターとは_メッセージを受信した際にローカルな意思決定を行い、新しいアクターを作成し、さらなるメッセージを送信し、次に受信するメッセージへの応答方法を決定できる並行計算の基本構成要素_です。

**ユースケース**: コード生成、データ分析タスクの自動化、計画および研究機能のためのカスタムエージェントの構築。

Autogenの重要なコアコンセプトについて以下に示します：

- **エージェント**
  - エージェントは、メッセージ通信、自身の状態の保持、受信メッセージや状態変化に応じた行動を行います。
  - 例: チャットエージェントの作成

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

    ここでは、`MyAssistant`というエージェントが作成されています。

    エージェントタイプをAutogenに登録してプログラムを開始します：

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    上記では、エージェントが登録され、メッセージを送信することで応答を得ています。

- **マルチエージェント**
  - Autogenは複数のエージェントを作成し、それらが連携して複雑なタスクを効率的に解決する仕組みを提供します。

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

    上記の例では、`GroupChatManager`がエージェント間のやり取りを調整しています。

- **エージェントランタイム**
  - エージェント間の通信、アイデンティティとライフサイクルの管理、セキュリティ境界の強制を行います。

    - **スタンドアロンランタイム**  
      単一プロセスアプリケーション向け。

      ![スタンドアロンランタイム](https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg)

    - **分散エージェントランタイム**  
      マルチプロセスアプリケーション向け。

      ![分散ランタイム](https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg)

### Semantic Kernel + エージェントフレームワーク

Semantic Kernelには以下のコアコンセプトがあります：

- **接続**: 外部AIサービスやデータソースとのインターフェース。

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

    上記はAzure OpenAI Chat Completionサービスへの接続例です。

- **プラグイン**: アプリケーションで使用可能な関数をカプセル化。

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // Register the function
    kernel.CreateSemanticFunction(
        promptTemplate: skPrompt,
        functionName: "SummarizeText",
        pluginName: "SemanticFunctions"
    );
    ```

    Semantic Kernelは、提供されたセマンティック情報に基づいて適切な関数を呼び出します。

- **ネイティブ関数**: フレームワークが直接呼び出せる関数。

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";
    
    var nativeFunctions = new NativeFunctions();
    kernel.ImportFunctions(nativeFunctions, plugInName);
    ```

- **プランナー**: ユーザー入力に基づいて実行計画を策定。

    ```csharp
    string planDefinition = "Read content from a local file and summarize the content.";
    SequentialPlanner sequentialPlanner = new SequentialPlanner(kernel);
    
    string assetsFolder = @"../../assets";
    string fileName = Path.Combine(assetsFolder,"docs","06_SemanticKernel", "aci_documentation.txt");
    
    ContextVariables contextVariables = new ContextVariables();
    contextVariables.Add("fileName", fileName);
    
    var customPlan = await sequentialPlanner.CreatePlanAsync(planDefinition);
    
    // Execute the plan
    KernelResult kernelResult = await kernel.RunAsync(contextVariables, customPlan);
    Console.WriteLine($"Summarization: {kernelResult.GetValue<string>()}");
    ```

- **メモリ**: AIアプリケーションのコンテキスト管理を抽象化。

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/en-us/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/en-us/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    メモリコレクションに情報を保存して活用します。

### Azure AI Agent Service

Azure AI Agent Serviceは、Microsoft Ignite 2024で導入された新しいサービスで、オープンソースLLM（例: Llama 3、Mistral、Cohere）の直接呼び出しをサポートします。

- **エージェント**: "スマート"マイクロサービスとして動作。

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

- **スレッドとメッセージ**: 会話やインタラクションを管理。

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

- **他のAIフレームワークとの統合**: AutogenやSemantic Kernelと連携可能。

**ユースケース**: エンタープライズ向けのセキュアでスケーラブルなAIエージェント展開に最適。

## これらのフレームワークの違いとは？

以下の表で主な違いをまとめました：

| フレームワーク       | フォーカス                              | コアコンセプト                        | ユースケース                      |
|----------------------|-----------------------------------------|--------------------------------------|----------------------------------|
| Autogen             | イベント駆動型、分散型エージェンティックアプリケーション | エージェント、ペルソナ、関数、データ | コード生成、データ分析タスク     |
| Semantic Kernel     | 人間のようなテキスト生成と理解           | エージェント、モジュール型コンポーネント、協調 | 自然言語理解、コンテンツ生成    |
| Azure AI Agent Service | 柔軟なモデル、エンタープライズセキュリティ、ツール呼び出し | モジュール性、協調、プロセスオーケストレーション | セキュアでスケーラブルなAI展開 |

### どのフレームワークを選ぶべき？

> **Q**: コード生成やデータ分析タスクを自動化するプロジェクトに取り組んでいます。どのフレームワークを使用すべきですか？  
> **A**: Autogenが適しています。イベント駆動型で分散型エージェンティックアプリケーションに特化しており、高度なマルチエージェント設計パターンをサポートしています。

> **Q**: エンタープライズ
プロジェクト目標に基づいています。自然言語理解、コンテンツ生成に最適です。  
- **Azure AI Agent Service**: 柔軟なモデル、エンタープライズ向けのセキュリティメカニズム、データストレージ方法。エンタープライズアプリケーションにおける安全でスケーラブルかつ柔軟なAIエージェントの展開に最適です。

## 既存のAzureエコシステムツールを直接統合できますか、それともスタンドアロンのソリューションが必要ですか？
答えは「はい」です。既存のAzureエコシステムツールをAzure AI Agent Serviceと直接統合できます。特に、このサービスは他のAzureサービスとシームレスに動作するように設計されています。たとえば、Bing、Azure AI Search、Azure Functionsと統合することができます。また、Azure AI Foundryとの深い統合もあります。

AutogenやSemantic Kernelについても、Azureサービスと統合できますが、コードからAzureサービスを呼び出す必要がある場合があります。別の統合方法としては、Azure SDKを使用してエージェントからAzureサービスとやり取りすることも可能です。さらに、前述のように、Azure AI Agent ServiceをAutogenやSemantic Kernelで構築されたエージェントのオーケストレーターとして使用することで、Azureエコシステムへの簡単なアクセスを実現できます。

## 参考文献
- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)  
- [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/)  
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp)  
- [4] - [Azure AI Agent service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)  
- [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)  

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳にはエラーや不正確な部分が含まれる可能性があります。元の言語で記載された原文を正式な情報源と見なしてください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。