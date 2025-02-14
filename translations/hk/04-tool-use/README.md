# 工具使用設計模式  

## 簡介

喺呢堂課，我哋會解答以下問題：

- 咩係工具使用設計模式？
- 呢個模式適用於咩場景？
- 實現呢個設計模式需要嘅元素/組成部分係咩？
- 喺建立可信賴嘅AI代理時，使用工具使用設計模式需要注意啲咩特別事項？

## 學習目標

完成呢堂課之後，你將能夠：

- 定義工具使用設計模式及其目的。
- 識別適用工具使用設計模式嘅場景。
- 理解實現呢個設計模式所需嘅關鍵元素。
- 認識使用呢個設計模式時，確保AI代理可信賴嘅考量。

## 咩係工具使用設計模式？

**工具使用設計模式**重點喺俾大型語言模型（LLMs）能夠與外部工具互動，以達到特定目標。工具係由代理執行嘅代碼，佢可以係一個簡單嘅函數，例如計算機，亦可以係第三方服務嘅API調用，例如股票價格查詢或者天氣預報。喺AI代理嘅背景下，工具係設計俾代理響應**模型生成嘅函數調用**而執行。

## 呢個模式適用於咩場景？

AI代理可以利用工具完成複雜任務、檢索信息或者做決策。工具使用設計模式通常應用喺需要動態與外部系統交互嘅場景，例如數據庫、網絡服務或者代碼解釋器。呢種能力對多種場景都好有用，包括：

- **動態信息檢索：** 代理可以查詢外部API或者數據庫，獲取最新數據（例如查詢SQLite數據庫進行數據分析、獲取股票價格或者天氣信息）。
- **代碼執行與解釋：** 代理可以執行代碼或者腳本，解決數學問題、生成報告或者進行模擬。
- **工作流自動化：** 通過集成工具（例如任務調度器、電子郵件服務或者數據管道），自動化重複或者多步驟工作流。
- **客戶支持：** 代理可以與CRM系統、工單平台或者知識庫互動，解答用戶問題。
- **內容生成與編輯：** 代理可以利用工具，例如語法檢查器、文本摘要生成器或者內容安全評估工具，協助完成內容創建任務。

## 實現工具使用設計模式需要嘅元素/組成部分係咩？

### 函數/工具調用

函數調用係俾大型語言模型（LLMs）與工具互動嘅主要方式。你可能會見到「函數」同「工具」互換使用，因為「函數」（可重用嘅代碼塊）就係代理用嚟執行任務嘅「工具」。為咗讓函數嘅代碼可以被調用，LLM需要將用戶請求同函數嘅描述進行比較。為咗做到呢點，一個包含所有可用函數描述嘅結構（schema）會被發送俾LLM。然後，LLM會選擇最適合嘅函數，返回佢嘅名稱同參數。被選中嘅函數會被執行，佢嘅回應會再返俾LLM，然後LLM利用呢啲信息回應用戶請求。

開發者想為代理實現函數調用，需要：

1. 一個支持函數調用嘅LLM模型
2. 一個包含函數描述嘅結構（schema）
3. 每個描述中提到嘅函數代碼

用一個查詢城市當前時間嘅例子嚟說明：

- **初始化支持函數調用嘅LLM：**

    唔係所有模型都支持函數調用，所以確認你用嘅LLM支持呢個功能好重要。[Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling)支持函數調用。我哋可以由初始化Azure OpenAI客戶端開始。

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

- **創建函數結構（Schema）：**

    接住，我哋會定義一個JSON結構，包含函數名稱、函數用途嘅描述，以及函數參數嘅名稱同描述。
    然後，我哋會將呢個結構同用戶請求一齊傳俾之前創建嘅客戶端，請求查詢三藩市嘅時間。需要注意嘅係，返回嘅係**工具調用**，而唔係問題嘅最終答案。如之前提到，LLM返回咗佢為任務選擇嘅函數名稱同將會傳遞俾函數嘅參數。

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
  
- **執行任務所需嘅函數代碼：**

    而家LLM已經選擇咗需要運行嘅函數，接住就需要實現並執行完成任務嘅代碼。
    我哋可以用Python實現查詢當前時間嘅代碼。同時，我哋亦需要編寫代碼，從response_message中提取名稱同參數以獲取最終結果。

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

函數調用係大部分（如果唔係全部）代理工具使用設計嘅核心，但從零開始實現有時會有挑戰。
正如我哋喺[第二課](../../../02-explore-agentic-frameworks)學到，代理框架為我哋提供咗預構建嘅組件，方便實現工具使用。

### 使用代理框架嘅工具使用例子

- ### **[Semantic Kernel](https://learn.microsoft.com/azure/ai-services/agents/overview)**

    Semantic Kernel係一個開源嘅AI框架，適合用.NET、Python同Java開發大型語言模型（LLMs）嘅開發者。佢透過一個叫做[序列化](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)嘅過程，自動將你嘅函數同參數描述傳遞俾模型，簡化咗使用函數調用嘅過程。佢仲處理模型同你代碼之間嘅雙向通信。使用代理框架例如Semantic Kernel嘅另一個好處係，你可以訪問預構建嘅工具，例如[文件搜索](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py)同[代碼解釋器](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)。

    以下圖解展示咗使用Semantic Kernel進行函數調用嘅過程：

    ![函數調用](../../../translated_images/functioncalling-diagram.b5493ea5154ad8e3e4940d2e36a49101eec1398948e5d1039942203b4f5a4209.hk.png)

    喺Semantic Kernel中，函數/工具被稱為[插件](https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python)。我哋可以將`get_current_time` function we saw earlier into a plugin by turning it into a class with the function in it. We can also import the `kernel_function`裝飾器，加入函數描述。當你用GetCurrentTimePlugin創建內核時，內核會自動序列化函數同佢嘅參數，喺呢個過程中創建結構發送俾LLM。

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

    Azure AI Agent Service係一個較新嘅代理框架，旨喺幫助開發者安全地構建、部署同擴展高質量同可擴展嘅AI代理，而唔需要管理底層嘅計算同存儲資源。呢個框架對企業應用特別有用，因為佢係一個完全託管嘅服務，並提供企業級別嘅安全性。

    同直接用LLM API開發相比，Azure AI Agent Service提供咗以下優勢：
  - 自動工具調用——唔需要解析工具調用、調用工具同處理回應；呢啲全部都喺服務端完成
  - 安全管理數據——唔需要自行管理會話狀態，可以依賴threads存儲所需嘅所有信息
  - 預構建工具——可以用嚟與數據源交互嘅工具，例如Bing、Azure AI Search同Azure Functions。

    Azure AI Agent Service提供嘅工具可以分為兩類：

    1. 知識工具：
        - [使用Bing Search進行信息補充](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview)
        - [文件搜索](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview)
        - [Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search)

    2. 行動工具：
        - [函數調用](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview)
        - [代碼解釋器](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview)
        - [OpenAI定義嘅工具](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview)
        - [Azure Functions](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview)

    Agent Service允許我哋將呢啲工具作為一個`toolset`. It also utilizes `threads` which keep track of the history of messages from a particular conversation.

    Imagine you are a sales agent at a company called Contoso. You want to develop a conversational agent that can answer questions about your sales data.

    The image below illustrates how you could use Azure AI Agent Service to analyze your sales data:

    ![Agentic Service In Action](../../../translated_images/agent-service-in-action.8c2d8aa8e9d91feeb29549b3fde529f8332b243875154d03907616a69198afbc.hk.jpg?WT.mc_id=academic-105485-koreyst)

    To use any of these tools with the service we can create a client and define a tool or toolset. To implement this practically we can use the Python code below. The LLM will be able to look at the toolset and decide whether to use the user created function, `fetch_sales_data_using_sqlite_query`，或者根據用戶請求使用預構建嘅代碼解釋器。

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

## 使用工具使用設計模式構建可信AI代理需要注意啲咩特別事項？

使用LLM動態生成嘅SQL通常會引起安全問題，特別係SQL注入或者惡意操作（例如刪除或者篡改數據庫）嘅風險。雖然呢啲擔憂係合理嘅，但可以通過正確配置數據庫訪問權限有效減輕呢啲風險。對於大多數數據庫，呢個過程包括將數據庫設置為只讀模式。對於例如PostgreSQL或者Azure SQL嘅數據庫服務，應該為應用程序分配只讀（SELECT）角色。

喺安全環境中運行應用程序可以進一步增強保護。喺企業場景中，數據通常會從運營系統中提取並轉換到只讀數據庫或者數據倉庫，並具有用戶友好嘅結構。呢個方法可以確保數據安全，並優化性能同可訪問性，同時限制應用程序只有只讀訪問權限。

## 其他資源

- [Azure AI Agents Service Workshop](https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/)
- [Contoso Creative Writer Multi-Agent Workshop](https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop)
- [Semantic Kernel Function Calling Tutorial](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)
- [Semantic Kernel Code Interpreter](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)
- [Autogen Tools](https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html)
```

**免責聲明**:  
本文件是使用機器翻譯人工智能服務進行翻譯的。我們雖然努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或錯誤解讀概不負責。