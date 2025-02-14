# ツール利用デザインパターン  

## はじめに

このレッスンでは、以下の質問に答えることを目指します：

- ツール利用デザインパターンとは何か？
- どのようなユースケースに適用できるのか？
- デザインパターンを実装するために必要な要素や構成要素は何か？
- 信頼性の高いAIエージェントを構築する際に、ツール利用デザインパターンを使用する際の特別な考慮事項は何か？

## 学習目標

このレッスンを完了すると、次のことができるようになります：

- ツール利用デザインパターンとその目的を定義する。
- ツール利用デザインパターンが適用可能なユースケースを特定する。
- デザインパターンを実装するために必要な主要要素を理解する。
- このデザインパターンを使用するAIエージェントの信頼性を確保するための考慮事項を認識する。

## ツール利用デザインパターンとは？

**ツール利用デザインパターン**は、LLM（大規模言語モデル）に外部ツールと連携する能力を与え、特定の目標を達成することを目的としています。ツールとは、エージェントがアクションを実行するために使用できるコードのことを指します。ツールは、電卓のような単純な関数や、株価検索や天気予報のようなサードパーティサービスへのAPI呼び出しなどがあります。AIエージェントの文脈では、ツールは**モデル生成の関数呼び出し**に応じてエージェントによって実行されるように設計されています。

## 適用できるユースケースは何か？

AIエージェントはツールを活用して、複雑なタスクを完了したり、情報を取得したり、意思決定を行うことができます。ツール利用デザインパターンは、データベースやウェブサービス、コードインタプリタなどの外部システムとの動的なやり取りを必要とするシナリオでよく使用されます。この能力は、以下のようなさまざまなユースケースで役立ちます：

- **動的な情報取得**：エージェントが外部APIやデータベースをクエリし、最新のデータを取得（例：SQLiteデータベースを使ったデータ分析、株価や天気情報の取得）。
- **コードの実行と解釈**：エージェントがコードやスクリプトを実行し、数学的問題を解いたり、レポートを生成したり、シミュレーションを行う。
- **ワークフローの自動化**：タスクスケジューラ、メールサービス、データパイプラインなどのツールを統合して反復的または多段階のワークフローを自動化。
- **カスタマーサポート**：CRMシステム、チケッティングプラットフォーム、ナレッジベースと連携してユーザーの問い合わせに対応。
- **コンテンツ生成と編集**：文法チェッカー、テキスト要約ツール、コンテンツの安全性評価ツールを活用してコンテンツ作成を支援。

## ツール利用デザインパターンを実装するために必要な要素/構成要素は何か？

### 関数/ツール呼び出し

関数呼び出しは、LLMがツールと連携する主要な方法です。「関数」と「ツール」はしばしば同義で使われます。なぜなら、「関数」（再利用可能なコードブロック）が、エージェントがタスクを実行するために使用する「ツール」だからです。関数のコードを呼び出すためには、LLMがユーザーのリクエストを関数の説明と比較する必要があります。そのため、利用可能なすべての関数の説明を含むスキーマをLLMに送信します。LLMはタスクに最も適した関数を選択し、その名前と引数を返します。選択された関数が呼び出され、その応答がLLMに送信され、LLMはその情報を使用してユーザーのリクエストに応答します。

エージェント用に関数呼び出しを実装するためには、以下が必要です：

1. 関数呼び出しをサポートするLLMモデル
2. 関数の説明を含むスキーマ
3. 説明された各関数のコード

以下の例では、特定の都市の現在時刻を取得するプロセスを説明します：

- **関数呼び出しをサポートするLLMの初期化**：

    すべてのモデルが関数呼び出しをサポートしているわけではないため、使用するLLMがサポートしていることを確認することが重要です。[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling)は関数呼び出しをサポートしています。Azure OpenAIクライアントを初期化するところから始めましょう。

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

- **関数スキーマの作成**：

    次に、関数名、関数の機能の説明、関数パラメータの名前と説明を含むJSONスキーマを定義します。このスキーマを上記で作成したクライアントに渡し、サンフランシスコの時刻を見つけるためのユーザーリクエストと一緒に送信します。重要な点は、返されるのは**ツール呼び出し**であり、**最終的な答え**ではないということです。先述したように、LLMはタスクに選択された関数の名前と、それに渡される引数を返します。

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
  
- **タスクを実行するために必要な関数コード**：

    LLMが実行すべき関数を選択した後、そのタスクを実行するコードを実装して実行する必要があります。
    Pythonで現在時刻を取得するコードを実装します。また、response_messageから関数名と引数を抽出して最終結果を得るコードも記述します。

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

関数呼び出しは、ほぼすべてのエージェントのツール利用設計の中心にありますが、ゼロから実装するのは時に困難です。
[レッスン2](../../../02-explore-agentic-frameworks)で学んだように、エージェントフレームワークはツール利用を実装するための事前構築された構成要素を提供してくれます。

### エージェントフレームワークを用いたツール利用の例

- ### **[Semantic Kernel](https://learn.microsoft.com/azure/ai-services/agents/overview)**

    Semantic Kernelは、LLMを利用する.NET、Python、Java開発者向けのオープンソースAIフレームワークです。このフレームワークは、関数呼び出しのプロセスを簡素化し、関数とそのパラメータをモデルに自動的に説明する[シリアライズ](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)というプロセスを通じて実現します。また、モデルとコード間のやり取りを処理する機能も備えています。さらに、Semantic Kernelのようなエージェントフレームワークを使用する利点として、[ファイル検索](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py)や[コードインタプリタ](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)などの事前構築されたツールにアクセスできる点があります。

    以下の図は、Semantic Kernelを使用した関数呼び出しのプロセスを示しています：

    ![function calling](../../../translated_images/functioncalling-diagram.b5493ea5154ad8e3e4940d2e36a49101eec1398948e5d1039942203b4f5a4209.ja.png)

    Semantic Kernelでは、関数/ツールは[プラグイン](https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python)と呼ばれます。`get_current_time` function we saw earlier into a plugin by turning it into a class with the function in it. We can also import the `kernel_function`デコレーターを使用して関数の説明を提供できます。このプラグインをKernelに追加すると、Kernelは関数とそのパラメータを自動的にシリアライズし、スキーマを作成してLLMに送信します。

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

    Azure AI Agent Serviceは、新しいエージェントフレームワークであり、開発者が高品質で拡張可能なAIエージェントを、安全に構築、デプロイ、スケーリングすることを可能にします。計算リソースやストレージリソースを管理する必要がないため、特にエンタープライズアプリケーションに適しています。

    LLM APIを直接使用する場合と比較して、Azure AI Agent Serviceは以下の利点を提供します：
  - 自動ツール呼び出し – ツール呼び出しの解析、ツールの呼び出し、応答の処理がすべてサーバーサイドで行われます。
  - セキュリティ管理されたデータ – 会話の状態を自分で管理する代わりに、スレッドを使用して必要な情報を保存できます。
  - 事前構築されたツール – Bing、Azure AI Search、Azure Functionsなどのデータソースとやり取りするためのツールを使用可能。

    Azure AI Agent Serviceで利用可能なツールは以下の2つのカテゴリに分けられます：

    1. 知識ツール:
        - [Bing Searchによる基盤情報](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview)
        - [ファイル検索](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview)
        - [Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search)

    2. アクションツール:
        - [関数呼び出し](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview)
        - [コードインタプリタ](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview)
        - [OpenAI定義ツール](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview)
        - [Azure Functions](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview)

    Agent Serviceを使用することで、これらのツールを`toolset`. It also utilizes `threads` which keep track of the history of messages from a particular conversation.

    Imagine you are a sales agent at a company called Contoso. You want to develop a conversational agent that can answer questions about your sales data.

    The image below illustrates how you could use Azure AI Agent Service to analyze your sales data:

    ![Agentic Service In Action](../../../translated_images/agent-service-in-action.jpg?WT.858cf9f67cc5c7f16ff3660d3df11c90e8cda37025bea4db5c4a59d2facce09a.ja.mc_id=academic-105485-koreyst)

    To use any of these tools with the service we can create a client and define a tool or toolset. To implement this practically we can use the Python code below. The LLM will be able to look at the toolset and decide whether to use the user created function, `fetch_sales_data_using_sqlite_query`や、ユーザーリクエストに応じた事前構築されたコードインタプリタと組み合わせて使用することができます。

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

## 信頼性の高いAIエージェントを構築する際に、ツール利用デザインパターンを使用する際の特別な考慮事項は何か？

LLMによって動的に生成されるSQLに関する一般的な懸念は、セキュリティ、特にSQLインジェクションやデータベースの削除や改ざんなどの悪意あるアクションのリスクです。これらの懸念は有効ですが、データベースアクセス権限を適切に設定することで効果的に軽減できます。ほとんどのデータベースでは、データベースを読み取り専用として設定することが推奨されます。PostgreSQLやAzure SQLなどのデータベースサービスでは、アプリに読み取り専用（SELECT）のロールを割り当てるべきです。

アプリを安全な環境で実行することは、さらに保護を強化します。エンタープライズシナリオでは、データは通常、運用システムから抽出され、変換され、読み取り専用のデータベースやデータウェアハウスに保存されます。このアプローチにより、データが安全で、パフォーマンスとアクセス性が最適化され、アプリが制限された読み取り専用アクセスを持つように確保されます。

## 追加リソース

- [Azure AI Agents Service Workshop](https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/)
- [Contoso Creative Writer Multi-Agent Workshop](https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop)
- [Semantic Kernel Function Calling Tutorial](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)
- [Semantic Kernel Code Interpreter](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)
- [Autogen Tools](https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html)
```

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。元の言語で記載された原文が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や解釈の誤りについて、当社は一切の責任を負いません。