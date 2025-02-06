# Tool Use Design Pattern  

## Introduction 
In this lesson, we're looking to answer the following questions:

- What is the tool use design pattern?
- What are the use cases it can be applied to?
- What are the elements/building blocks needed to implement the design pattern? 
- What are the special considerations for using the Tool Use Design Pattern to build trustworthy AI agents?

## Learning Goals 
After completing this lesson, you will be able to: 

- Define the Tool Use Design Pattern and its purpose.
- Identify use cases where the Tool Use Design Pattern is applicable.
- Understand the key elements needed to implement the design pattern.
- Recognize considerations for ensuring trustworthiness in AI agents using this design pattern.

## What is the Tool Use Design Pattern?

The **Tool Use Design Pattern** focuses on giving LLMs the ability to interact with external tools to achieve specific goals. Tools are code that can be executed by an agent to perform actions. A tool can be a simple function such as a calculator, or an API call to a third-party service such as stock price lookup or weather forecast. In the context of AI agents, tools are designed to be executed by agents in response to **model-generated function calls**.

## What are the use cases it can be applied to?

AI Agents can leverage tools to complete complex tasks, retrieve information, or make decisions. The tool use design pattern is often used in scenarios requiring dynamic interaction with external systems, such as databases, web services, or code interpreters. This ability is useful for a number of different use cases including:

- **Dynamic Information Retrieval:** Agents can query external APIs or databases to fetch up-to-date data (e.g., quering an SQLite database for data analysis, fetching stock prices or weather information).
- **Code Execution and Interpretation:** Agents can execute code or scripts to solve mathematical problems, generate reports, or perform simulations.
- **Workflow Automation:** Automating repetitive or multi-step workflows by integrating tools like task schedulers, email services, or data pipelines.
- **Customer Support:** Agents can interact with CRM systems, ticketing platforms, or knowledge bases to resolve user queries.
- **Content Generation and Editing:** Agents can leverage tools like grammar checkers, text summarizers, or content safety evaluators to assist with content creation tasks.

## What are the elements/building blocks needed to implement the tool use design pattern? 

### Function/Tool Calling 

Function calling is the primary way we enable Large Language Models (LLMs) to interact with tools. You will often see Function and Tool Calling used interchangeably because the 'functions' (blocks of reusable code) are the 'tools' used to carry out tasks. In order for a function's code to be run, an LLM must compare the user prompt against the functions description, and decide if the function will achieve the users desired result. The LLM will select the most appropriate function for the task and return its name and the arguments needed. 

At a high level to implement function calling for agents you will need:

1. **An LLM model that supports function calling:** Most LLM model providers including [AzureOpenAI](https://learn.microsoft.com/en-gb/azure/ai-services/openai/how-to/function-calling) support function calling. 

2. **Function Schema**: A structured format like JSON that contains the function name, description of what the function does, and the names and descriptions of the expected arguments.
   Here is an example of a 'get_current_time' function description in JSON, the users prompt to find the time in San Francisco and the API call to AzureOpenAI. 
   
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] # Single function call
  
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

    ```python
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```

    Whats important to note is that a function/tool call is what is returned, **not** the final answer to the question. As mentioned earlier, the LLM returns the name of the function it's selected for the     task, and the arguments that will the passed to it. 
  
3. **The function code required to carry out the task:** Now that the LLM has chosen which function needs to be run the code that carries out the task needs to be implemented and executed.
   In Python for the above example we could implement the function in this way.

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

      In order to execute the code you could then run the following logic to get the expected result. 

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
     ```python
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Function Calling is at the heart of most, if not all agent tool use design, however implementing it from scratch can sometimes be challenging. As we learned in [Lesson 3]() agentic frameworks provide us with pre-built building blocks to implement tool use. 
 
### Tool Use with Agentic Frameworks 

- **[Semantic Kernel](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)**

  Semantic Kernel is an open-source AI framework for .NET, Python, and Java developers working with Large Language Models (LLMs). It offers pre-built components such as prompts, parsers, and memory management. Along with this, Semantic Kernel also provides access to pre-built tools through the [Open AI Assistant Agent](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/assistant-agent?pivots=programming-language-python). One the tools that is particularly helpful for data-analysis tasks and more, is the [Code Interpreter](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/examples/example-assistant-code?pivots=programming-language-python).
  
  The Code Interpreter tool enables the LLM to generate Python code for tasks such as creating charts or performing complex data analyses based on user queries. It leverages natural language processing (NLP), sales data from an SQLite database, and user prompts to automate code generation. The LLM-generated Python code executes within a secure sandbox environment, utilizing a restricted subset of Python to ensure safe and controlled execution. Take a look at an example of how this is implemented in just a few lines of code [here](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/step9_assistant_tool_code_interpreter.py)
  
- **[Azure AI Agent Service](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)**
   
  When using function calling with AzureOpenAI we saw that it requires defining a function schema for the LLM. Azure AI Agent Service supports this approach and also offers a more flexible option. With the Azure AI Agent Service and its Python SDK, you can define the function schema directly within the Python function’s docstring. This approach keeps the definition and implementation together, simplifying maintenance and enhancing readability.
  
  For example, lets imagine you've written a function that executes LLM dynamically generated SQL queries against an SQLite database. The `fetch_sales_data_using_sqlite_query` function uses a docstring to specify its signature, inputs, and outputs. The SDK parses this docstring to generate the callable function for the LLM:
  
  ```python
  async def fetch_sales_data_using_sqlite_query(self: "SalesData", sqlite_query: str) -> str:
      """
      This function is used to answer user questions about Contoso sales data by executing SQLite queries against the database.
  
      :param sqlite_query: The input should be a well-formed SQLite query to extract information based on the user's question. The query result will be returned as a JSON object.
      :return: Return data in JSON serializable format.
      :rtype: str
      """
    ```

  When compared to developing with the LLM API's directly, Azure AI Agent Service provides some advantages, including:

  - Automatic tool calling – no need to parse a tool call, invoke the tool, and handle the response; all of this is now done server-side
  - Securely managed data – instead of managing your own conversation state, you can rely on threads to store all the information you need
  - Out-of-the-box tools – Tools that you can use to interact with your data sources, such as Bing, Azure AI Search, and Azure Functions.
 
    [add image here]

- **[Autogen](https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html)**
  TODO: Add more info here 


## What are the special considerations for using the Tool Use Design Pattern to build trustworthy AI agents?

A common concern with SQL dynamically generated by LLMs is security, particularly the risk of SQL injection or malicious actions, such as dropping or tampering with the database. While these concerns are valid, they can be effectively mitigated by properly configuring database access permissions.

For SQLite, this involves configuring the database as read-only. For database services like PostgreSQL or Azure SQL, the app should be assigned a read-only (SELECT) role. Running the app in a secure environment further enhances protection.

In enterprise scenarios, data is typically extracted and transformed from operational systems into a read-only database or data warehouse with a user-friendly schema. This approach ensures that the data is secure, optimized for performance and accessibility, and that the app has restricted, read-only access.


## Additional Resources 

- [Contoso Creative Writer Multi-Agent Workshop](https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop)
- [Azure AI Agents Service Workshop](https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/)





    
