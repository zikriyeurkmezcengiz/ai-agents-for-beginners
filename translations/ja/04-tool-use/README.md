```markdown
# ツール使用デザインパターン  

## はじめに

このレッスンでは、以下の質問に答えることを目指します：

- ツール使用デザインパターンとは何か？
- このパターンを適用できるユースケースは何か？
- デザインパターンを実装するために必要な要素や構成要素は何か？
- 信頼性の高いAIエージェントを構築するためにツール使用デザインパターンを使用する際の特別な考慮事項は何か？

## 学習目標

このレッスンを終えると、以下のことができるようになります：

- ツール使用デザインパターンとその目的を定義する。
- ツール使用デザインパターンが適用可能なユースケースを特定する。
- デザインパターンを実装するために必要な主要な要素を理解する。
- このデザインパターンを使用するAIエージェントの信頼性を確保するための考慮事項を認識する。

## ツール使用デザインパターンとは？

**ツール使用デザインパターン**は、LLM（大規模言語モデル）に外部ツールと連携する能力を与え、特定の目標を達成するために使用されます。ツールとは、エージェントがアクションを実行するために実行可能なコードのことを指します。ツールは、電卓のようなシンプルな関数から、株価の取得や天気予報といったサードパーティサービスへのAPI呼び出しまで多岐にわたります。AIエージェントの文脈では、ツールは**モデル生成関数呼び出し**に応じてエージェントが実行するよう設計されています。

## 適用できるユースケースは何か？

AIエージェントは、ツールを活用して複雑なタスクを完了したり、情報を取得したり、意思決定を行ったりすることができます。ツール使用デザインパターンは、データベース、ウェブサービス、コードインタープリタなど外部システムとの動的な連携が必要なシナリオでよく利用されます。この能力は以下のようなさまざまなユースケースに役立ちます：

- **動的な情報取得**: エージェントは外部APIやデータベースにクエリを送信して最新のデータを取得できます（例：SQLiteデータベースへのクエリによるデータ分析、株価や天気情報の取得）。
- **コード実行と解釈**: エージェントはコードやスクリプトを実行して数学的な問題を解決したり、レポートを生成したり、シミュレーションを実行したりします。
- **ワークフローの自動化**: タスクスケジューラ、メールサービス、データパイプラインなどのツールを統合して繰り返し作業や複数ステップのワークフローを自動化します。
- **カスタマーサポート**: CRMシステム、チケットプラットフォーム、ナレッジベースと連携してユーザーの問い合わせに対応します。
- **コンテンツ生成と編集**: 文法チェッカー、要約ツール、コンテンツの安全性評価ツールを活用してコンテンツ作成を支援します。

## ツール使用デザインパターンを実装するために必要な要素/構成要素は何か？

### 関数/ツール呼び出し

関数呼び出しは、LLMがツールと連携するための主要な手段です。「関数」と「ツール」という用語はしばしば同じ意味で使われます。なぜなら、「関数」（再利用可能なコードのブロック）がエージェントがタスクを実行するための「ツール」となるからです。関数のコードを実行するには、LLMがユーザーのリクエストを関数の説明と照らし合わせて比較する必要があります。このため、利用可能な関数の説明を含むスキーマがLLMに送信されます。LLMはタスクに最も適した関数を選択し、その名前と引数を返します。その後、選択された関数が実行され、その応答がLLMに戻され、ユーザーのリクエストに応じた回答が生成されます。

エージェントの関数呼び出しを実装するために、開発者が必要とするものは以下の通りです：

1. 関数呼び出しをサポートするLLMモデル
2. 関数の説明を含むスキーマ
3. 説明された各関数のコード

以下に、都市の現在時刻を取得する例を用いて説明します：

- **関数呼び出しをサポートするLLMを初期化する:**

    すべてのモデルが関数呼び出しをサポートしているわけではないため、使用するLLMがサポートしているか確認することが重要です。[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling)は関数呼び出しをサポートしています。まず、Azure OpenAIクライアントを初期化することから始めます。

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

- **関数スキーマを作成する:**

    次に、関数名、関数が実行する内容の説明、関数パラメータの名前と説明を含むJSONスキーマを定義します。このスキーマを先ほど作成したクライアントに渡し、サンフランシスコの時刻を取得するためのユーザーリクエストとともに送信します。重要な点は、**ツール呼び出し**が返されるのであって、質問に対する最終的な答えではないということです。前述の通り、LLMはタスクに選択した関数の名前と引数を返します。

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
- **タスクを実行するために必要な関数コード:**

    LLMが実行すべき関数を選択した後、そのタスクを実行するコードを実装し、実行する必要があります。
    Pythonで現在時刻を取得するコードを実装できます。また、response_messageから名前と引数を抽出して最終結果を取得するコードも記述する必要があります。

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

関数呼び出しは、ほぼすべてのエージェントツール使用デザインの中心にありますが、ゼロから実装するのは時に困難です。
[レッスン2](../../../02-explore-agentic-frameworks)で学んだように、エージェントフレームワークはツール使用を実装するための事前構築された構成要素を提供してくれます。
 
### エージェントフレームワークを使用したツール使用の例

- ### **[Semantic Kernel](https://learn.microsoft.com/azure/ai-services/agents/overview)**

    Semantic Kernelは、.NET、Python、Javaの開発者向けのオープンソースAIフレームワークで、大規模言語モデル（LLMs）を活用するために設計されています。関数呼び出しのプロセスを簡素化し、関数とそのパラメータをモデルに自動的に説明する[シリアライズ](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)というプロセスを通じて実現します。また、モデルとコード間のやり取りも処理します。Semantic Kernelのようなエージェントフレームワークを使用するもう一つの利点は、[ファイル検索](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py)や[コードインタープリタ](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)のような事前構築されたツールにアクセスできることです。

    以下の図は、Semantic Kernelを使用した関数呼び出しのプロセスを示しています：

    ![function calling](../../../translated_images/functioncalling-diagram.b5493ea5154ad8e3e4940d2e36a49101eec1398948e5d1039942203b4f5a4209.ja.png)

    Semantic Kernelでは、関数/ツールは[プラグイン](https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python)と呼ばれます。`get_current_time` function we saw earlier into a plugin by turning it into a class with the function in it. We can also import the `kernel_function`デコレータを使用して、関数の説明を指定することができます。その後、GetCurrentTimePluginを使用してカーネルを作成すると、カーネルは関数とそのパラメータを自動的にシリアライズし、LLMに送信するスキーマを生成します。

    ```python
    from semantic_kernel.functions import kernel_function

    class GetCurrentTimePlugin:
        async def __init__(self, location):
            self.location = location

        @kernel_function(
            description="Get the current time for a given location"
        )
        def get_current_time(location: str = ""):
            ...

    ```

    ```python 
    from semantic_kernel import Kernel

    # Create the kernel
    kernel = Kernel()

    # Create the plugin
    get_current_time_plugin = GetCurrentTimePlugin(location)

    # Add the plugin to the kernel
    kernel.add_plugin(get_current_time_plugin)
    ```
  
- ### **[Azure AI Agent Service](https://learn.microsoft.com/azure/ai-services/agents/overview)**

    Azure AI Agent Serviceは、開発者が高品質で拡張可能なAIエージェントを安全に構築、展開、スケーリングできるように設計された新しいエージェントフレームワークです。基盤となるコンピューティングやストレージリソースを管理する必要がないため、特にエンタープライズアプリケーションにおいて有用です。

    LLM APIを直接使用する場合と比較して、Azure AI Agent Serviceにはいくつかの利点があります：
  - ツール呼び出しの自動化 – ツール呼び出しの解析、ツールの実行、応答の処理がすべてサーバー側で行われます。
  - データの安全な管理 – 会話の状態を管理する代わりに、スレッドを使用して必要な情報を保存できます。
  - 標準搭載のツール – BingやAzure AI Search、Azure Functionsなどのデータソースと連携するためのツールを使用できます。

    Azure AI Agent Serviceで利用可能なツールは、以下の2つのカテゴリに分けられます：

    1. 知識ツール:
        - [Bing検索による情報取得](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview)
        - [ファイル検索](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview)
        - [Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search)

    2. アクションツール:
        - [関数呼び出し](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview)
        - [コードインタープリタ](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview)
        - [OpenAI定義ツール](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview)
        - [Azure Functions](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview)

    Agent Serviceを使用すると、これらのツールを`toolset`. It also utilizes `threads` which keep track of the history of messages from a particular conversation.

    Imagine you are a sales agent at a company called Contoso. You want to develop a conversational agent that can answer questions about your sales data.

    The image below illustrates how you could use Azure AI Agent Service to analyze your sales data:

    ![Agentic Service In Action](../../../translated_images/agent-service-in-action.jpg?WT.858cf9f67cc5c7f16ff3660d3df11c90e8cda37025bea4db5c4a59d2facce09a.ja.mc_id=academic-105485-koreyst)

    To use any of these tools with the service we can create a client and define a tool or toolset. To implement this practically we can use the Python code below. The LLM will be able to look at the toolset and decide whether to use the user created function, `fetch_sales_data_using_sqlite_query`のように組み合わせたり、ユーザーリクエストに応じて事前構築されたコードインタープリタを使用することができます。

    ```python 
    import os
    from azure.ai.projects import AIProjectClient
    from azure.identity import DefaultAzureCredential
    from fecth_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fecth_sales_data_functions.py file.
    from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

    project_client = AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str=os.environ["PROJECT_CONNECTION_STRING"],
    )

    # Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
    fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
    toolset = ToolSet()
    toolset.add(fetch_data_function)

    # Initialize Code Interpreter tool and adding it to the toolset. 
    code_interpreter = code_interpreter = CodeInterpreterTool()
    toolset = ToolSet()
    toolset.add(code_interpreter)

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
        toolset=toolset
    )
    ```

## 信頼性の高いAIエージェントを構築するためにツール使用デザインパターンを使用する際の特別な考慮事項は何か？

LLMが動的に生成するSQLに関連する一般的な懸念は、セキュリティ、特にSQLインジェクションやデータベースの削除や改ざんといった悪意ある行動のリスクです。これらの懸念は確かに有効ですが、データベースアクセス権限を適切に構成することで効果的に軽減できます。ほとんどのデータベースでは、データベースを読み取り専用に構成することでこれを実現できます。PostgreSQLやAzure SQLのようなデータベースサービスでは、アプリに読み取り専用（SELECT）のロールを割り当てるべきです。

アプリを安全な環境で実行することで、さらに保護が強化されます。エンタープライズ環境では、データは通常、操作システムから抽出および変換され、読み取り専用のデータベースまたはデータウェアハウスに格納され、ユーザーフレンドリーなスキーマが提供されます。このアプローチにより、データは安全で、パフォーマンスとアクセシビリティが最適化され、アプリには制限された読み取り専用のアクセス権が与えられます。

## 追加リソース

- [Azure AI Agents Service ワークショップ](https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/)
- [Contoso Creative Writer Multi-Agent ワークショップ](https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop)
- [Semantic Kernel 関数呼び出しチュートリアル](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)
- [Semantic Kernel コードインタープリタ](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)
- [Autogen Tools](https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html)
```

**免責事項**:  
本書類は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文（元の言語の文書）を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や解釈の誤りについて、当方は一切の責任を負いません。