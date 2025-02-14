# 工具使用設計模式  

## 介紹

在這節課中，我們將回答以下問題：

- 什麼是工具使用設計模式？
- 它可以應用於哪些使用案例？
- 實現這種設計模式需要哪些要素/組件？
- 使用工具使用設計模式來構建可信任的 AI 代理時需要注意哪些特別考量？

## 學習目標

完成本課程後，您將能夠：

- 定義工具使用設計模式及其目的。
- 辨識適用於工具使用設計模式的使用案例。
- 理解實現該設計模式所需的關鍵要素。
- 了解確保使用此設計模式的 AI 代理可信任的考量。

## 什麼是工具使用設計模式？

**工具使用設計模式**專注於賦予大型語言模型（LLMs）與外部工具互動的能力，以達成特定目標。工具是可由代理執行的程式碼，可以是簡單的函數（例如計算器），也可以是第三方服務的 API 呼叫（例如股票價格查詢或天氣預報）。在 AI 代理的上下文中，工具被設計為由代理根據**模型生成的函數呼叫**來執行。

## 它可以應用於哪些使用案例？

AI 代理可以利用工具完成複雜任務、檢索資訊或做出決策。工具使用設計模式通常用於需要與外部系統動態互動的場景，例如資料庫、網路服務或程式碼解釋器。這種能力適用於多種使用案例，包括但不限於：

- **動態資訊檢索：** 代理可以查詢外部 API 或資料庫以獲取最新數據（例如，查詢 SQLite 資料庫進行數據分析、獲取股票價格或天氣資訊）。
- **程式碼執行與解釋：** 代理可以執行程式碼或腳本來解決數學問題、生成報告或進行模擬。
- **工作流程自動化：** 通過整合任務排程器、電子郵件服務或數據管道等工具，自動化重複性或多步驟的工作流程。
- **客戶支持：** 代理可以與 CRM 系統、工單平台或知識庫互動，解決用戶問題。
- **內容生成與編輯：** 代理可以利用工具（如文法檢查器、文本摘要工具或內容安全評估器）協助完成內容創建任務。

## 實現工具使用設計模式需要哪些要素/組件？

### 函數/工具呼叫

函數呼叫是讓大型語言模型（LLMs）與工具互動的主要方式。您經常會看到「函數」和「工具」這兩個詞互換使用，因為「函數」（可重用的程式碼塊）就是代理用來執行任務的「工具」。為了讓函數的程式碼被調用，LLM 必須將用戶的請求與函數的描述進行比較。為此，需要向 LLM 傳送包含所有可用函數描述的架構（schema）。LLM 然後選擇最適合任務的函數，並返回其名稱和參數。選定的函數被調用，其響應會返回給 LLM，LLM 使用這些資訊來回應用戶的請求。

開發人員若要為代理實現函數呼叫，您需要：

1. 支援函數呼叫的 LLM 模型
2. 包含函數描述的架構
3. 每個描述函數的程式碼

讓我們用一個獲取城市當前時間的例子來說明：

- **初始化支援函數呼叫的 LLM：**

    並非所有模型都支援函數呼叫，因此檢查您使用的 LLM 是否支援此功能非常重要。[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) 支援函數呼叫。我們可以從初始化 Azure OpenAI 客戶端開始。

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

- **創建函數架構：**

    接下來，我們將定義一個包含函數名稱、函數用途描述以及函數參數名稱和描述的 JSON 架構。我們將此架構與用戶的請求一同傳遞給上述創建的客戶端，以查找舊金山的時間。需要注意的是，返回的是**工具呼叫**，而**不是**問題的最終答案。如前所述，LLM 返回的是它為任務選擇的函數名稱及其參數。

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
  
- **執行任務所需的函數程式碼：**

    現在，LLM 已選擇需要執行的函數，接下來需要實現並執行執行任務的程式碼。我們可以使用 Python 實現獲取當前時間的程式碼，還需要編寫程式碼來從 `response_message` 中提取名稱和參數以獲取最終結果。

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

函數呼叫是大多數（如果不是全部的話）代理工具使用設計的核心，然而從零開始實現它有時可能會具有挑戰性。如我們在 [第 2 課](../../../02-explore-agentic-frameworks) 中學到的，代理框架為我們提供了實現工具使用的預構建組件。

### 使用代理框架的工具使用範例

- ### **[Semantic Kernel](https://learn.microsoft.com/azure/ai-services/agents/overview)**

    Semantic Kernel 是一個為 .NET、Python 和 Java 開發者設計的開源 AI 框架，用於與大型語言模型（LLMs）協作。它通過一個稱為[序列化](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)的過程，自動向模型描述函數及其參數，簡化了函數呼叫的過程。它還處理模型與程式碼之間的交互。使用像 Semantic Kernel 這樣的代理框架的另一個優勢是，您可以訪問預構建的工具，例如 [File Search](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py) 和 [Code Interpreter](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)。

    下圖說明了使用 Semantic Kernel 進行函數呼叫的過程：

    ![函數呼叫](../../../translated_images/functioncalling-diagram.b5493ea5154ad8e3e4940d2e36a49101eec1398948e5d1039942203b4f5a4209.tw.png)

    在 Semantic Kernel 中，函數/工具被稱為 [Plugins](https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python)。我們可以將函數 `get_current_time` function we saw earlier into a plugin by turning it into a class with the function in it. We can also import the `kernel_function` 裝飾器，這需要提供函數的描述。當您使用 GetCurrentTimePlugin 創建一個 kernel 時，kernel 將自動序列化該函數及其參數，並在此過程中創建發送給 LLM 的架構。

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

    Azure AI Agent Service 是一個新型代理框架，旨在幫助開發者安全地構建、部署和擴展高質量且可擴展的 AI 代理，而無需管理底層的計算和存儲資源。它對於企業應用特別有用，因為它是一個具有企業級安全性的完全託管服務。

    與直接使用 LLM API 開發相比，Azure AI Agent Service 提供了一些優勢，包括：
  - 自動工具呼叫——無需解析工具呼叫、調用工具並處理響應；所有這些現在都在伺服器端完成。
  - 安全管理數據——您可以依靠線程存儲所需的所有資訊，而無需管理自己的對話狀態。
  - 現成的工具——您可以使用這些工具與數據源交互，例如 Bing、Azure AI Search 和 Azure Functions。

    Azure AI Agent Service 中的工具可以分為兩類：

    1. 知識工具：
        - [使用 Bing 搜索進行基礎設置](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview)
        - [文件搜索](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview)
        - [Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search)

    2. 行動工具：
        - [函數呼叫](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview)
        - [程式碼解釋器](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview)
        - [OpenAI 定義的工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview)
        - [Azure Functions](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview)

    Agent Service 允許我們將這些工具作為一個 `toolset`. It also utilizes `threads` which keep track of the history of messages from a particular conversation.

    Imagine you are a sales agent at a company called Contoso. You want to develop a conversational agent that can answer questions about your sales data.

    The image below illustrates how you could use Azure AI Agent Service to analyze your sales data:

    ![Agentic Service In Action](../../../translated_images/agent-service-in-action.jpg?WT.858cf9f67cc5c7f16ff3660d3df11c90e8cda37025bea4db5c4a59d2facce09a.tw.mc_id=academic-105485-koreyst)

    To use any of these tools with the service we can create a client and define a tool or toolset. To implement this practically we can use the Python code below. The LLM will be able to look at the toolset and decide whether to use the user created function, `fetch_sales_data_using_sqlite_query` 或者根據用戶請求使用預構建的程式碼解釋器。

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

## 使用工具使用設計模式構建可信任 AI 代理的特別考量是什麼？

LLM 動態生成的 SQL 一個常見的問題是安全性，尤其是 SQL 注入或惡意行為的風險，例如刪除或篡改資料庫。儘管這些擔憂是合理的，但可以通過適當配置資料庫訪問權限有效減輕。對於大多數資料庫，這涉及將資料庫配置為只讀模式。對於像 PostgreSQL 或 Azure SQL 這樣的資料庫服務，應為應用程式分配只讀（SELECT）角色。

在安全環境中運行應用進一步增強了保護。在企業場景中，數據通常從操作系統中提取並轉換為只讀資料庫或數據倉庫，並配有用戶友好的架構。這種方法確保了數據的安全性、性能優化和可訪問性，並且應用程式具有受限的只讀訪問權限。

## 其他資源

- [Azure AI Agents Service Workshop](https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/)
- [Contoso Creative Writer Multi-Agent Workshop](https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop)
- [Semantic Kernel Function Calling Tutorial](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)
- [Semantic Kernel Code Interpreter](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)
- [Autogen Tools](https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html)
```

**免責聲明**：  
本文件是使用基於機器的人工智能翻譯服務進行翻譯的。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議使用專業的人工作翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀不承擔責任。