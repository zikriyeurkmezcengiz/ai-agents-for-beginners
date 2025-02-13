```markdown
# Padrão de Design para Uso de Ferramentas  

## Introdução

Nesta lição, vamos buscar responder às seguintes perguntas:

- O que é o padrão de design para uso de ferramentas?
- Quais são os casos de uso em que ele pode ser aplicado?
- Quais são os elementos/blocos de construção necessários para implementar esse padrão de design?
- Quais são as considerações especiais ao usar o padrão de design para uso de ferramentas para criar agentes de IA confiáveis?

## Objetivos de Aprendizado

Após concluir esta lição, você será capaz de:

- Definir o Padrão de Design para Uso de Ferramentas e seu propósito.
- Identificar casos de uso onde o padrão de design para uso de ferramentas é aplicável.
- Compreender os principais elementos necessários para implementar o padrão de design.
- Reconhecer considerações para garantir a confiabilidade de agentes de IA que utilizam esse padrão de design.

## O que é o Padrão de Design para Uso de Ferramentas?

O **Padrão de Design para Uso de Ferramentas** se concentra em fornecer aos LLMs a capacidade de interagir com ferramentas externas para atingir objetivos específicos. Ferramentas são códigos que podem ser executados por um agente para realizar ações. Uma ferramenta pode ser uma função simples, como uma calculadora, ou uma chamada de API para um serviço de terceiros, como consulta de preços de ações ou previsão do tempo. No contexto de agentes de IA, as ferramentas são projetadas para serem executadas por agentes em resposta a **chamadas de função geradas pelo modelo**.

## Quais são os casos de uso em que ele pode ser aplicado?

Agentes de IA podem aproveitar ferramentas para concluir tarefas complexas, recuperar informações ou tomar decisões. O padrão de design para uso de ferramentas é frequentemente usado em cenários que exigem interação dinâmica com sistemas externos, como bancos de dados, serviços web ou interpretadores de código. Essa capacidade é útil para diversos casos de uso, incluindo:

- **Recuperação Dinâmica de Informações:** Agentes podem consultar APIs externas ou bancos de dados para buscar dados atualizados (por exemplo, consultar um banco de dados SQLite para análise de dados, buscar preços de ações ou informações meteorológicas).
- **Execução e Interpretação de Código:** Agentes podem executar códigos ou scripts para resolver problemas matemáticos, gerar relatórios ou realizar simulações.
- **Automação de Fluxos de Trabalho:** Automatizar fluxos de trabalho repetitivos ou de múltiplas etapas integrando ferramentas como agendadores de tarefas, serviços de e-mail ou pipelines de dados.
- **Suporte ao Cliente:** Agentes podem interagir com sistemas CRM, plataformas de tickets ou bases de conhecimento para resolver dúvidas dos usuários.
- **Geração e Edição de Conteúdo:** Agentes podem usar ferramentas como verificadores gramaticais, resumos de texto ou avaliadores de segurança de conteúdo para auxiliar em tarefas de criação de conteúdo.

## Quais são os elementos/blocos de construção necessários para implementar o padrão de design para uso de ferramentas?

### Chamada de Função/Ferramenta

A chamada de função é a principal forma de permitir que Modelos de Linguagem de Grande Escala (LLMs) interajam com ferramentas. Muitas vezes, você verá "Função" e "Ferramenta" sendo usados de forma intercambiável, pois "funções" (blocos de código reutilizáveis) são as "ferramentas" que os agentes usam para realizar tarefas. Para que o código de uma função seja invocado, um LLM deve comparar a solicitação do usuário com a descrição da função. Para isso, um esquema contendo as descrições de todas as funções disponíveis é enviado ao LLM. O LLM seleciona a função mais apropriada para a tarefa e retorna seu nome e argumentos. A função selecionada é invocada, sua resposta é enviada de volta ao LLM, que usa as informações para responder à solicitação do usuário.

Para que os desenvolvedores implementem a chamada de função para agentes, você precisará de:

1. Um modelo LLM que suporte chamadas de função
2. Um esquema contendo descrições das funções
3. O código para cada função descrita

Vamos usar o exemplo de obter a hora atual em uma cidade para ilustrar:

- **Inicializar um LLM que suporte chamadas de função:**

    Nem todos os modelos suportam chamadas de função, então é importante verificar se o LLM que você está usando suporta. [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) suporta chamadas de função. Podemos começar iniciando o cliente Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

- **Criar um Esquema de Função:**

    Em seguida, definiremos um esquema JSON que contém o nome da função, uma descrição do que a função faz, e os nomes e descrições dos parâmetros da função. Depois, passaremos esse esquema ao cliente criado acima, juntamente com a solicitação do usuário para encontrar a hora em São Francisco. O que é importante notar é que uma **chamada de ferramenta** é o que é retornado, **não** a resposta final à pergunta. Como mencionado anteriormente, o LLM retorna o nome da função que selecionou para a tarefa e os argumentos que serão passados a ela.

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
  
- **O código da função necessário para realizar a tarefa:**

    Agora que o LLM escolheu qual função precisa ser executada, o código que realiza a tarefa precisa ser implementado e executado. Podemos implementar o código para obter a hora atual em Python. Também precisaremos escrever o código para extrair o nome e os argumentos da `response_message` para obter o resultado final.

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

A chamada de função está no coração de grande parte, se não de toda, a concepção de uso de ferramentas por agentes. No entanto, implementá-la do zero pode ser desafiador. Como aprendemos na [Lição 2](../../../02-explore-agentic-frameworks), frameworks agentivos nos fornecem blocos de construção pré-configurados para implementar o uso de ferramentas.
 
### Exemplos de Uso de Ferramentas com Frameworks Agentivos

- ### **[Semantic Kernel](https://learn.microsoft.com/azure/ai-services/agents/overview)**

    O Semantic Kernel é um framework de IA de código aberto para desenvolvedores que trabalham com Modelos de Linguagem de Grande Escala (LLMs) em .NET, Python e Java. Ele simplifica o processo de uso de chamadas de função, descrevendo automaticamente suas funções e seus parâmetros para o modelo por meio de um processo chamado [serialização](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions). Ele também gerencia a comunicação entre o modelo e seu código. Outra vantagem de usar um framework agentivo como o Semantic Kernel é que ele permite acessar ferramentas pré-configuradas, como [Busca de Arquivos](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py) e [Interpretador de Código](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py).

    O diagrama a seguir ilustra o processo de chamadas de função com o Semantic Kernel:

    ![function calling](../../../translated_images/functioncalling-diagram.b5493ea5154ad8e3e4940d2e36a49101eec1398948e5d1039942203b4f5a4209.pt.png)

    No Semantic Kernel, funções/ferramentas são chamadas de [Plugins](https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python). Podemos converter o `get_current_time` function we saw earlier into a plugin by turning it into a class with the function in it. We can also import the `kernel_function` decorator, que recebe a descrição da função. Quando você cria um kernel com o GetCurrentTimePlugin, o kernel automaticamente serializa a função e seus parâmetros, criando o esquema a ser enviado ao LLM no processo.

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

    O Azure AI Agent Service é um framework agentivo mais recente, projetado para capacitar desenvolvedores a criar, implantar e escalar agentes de IA de alta qualidade e extensíveis de forma segura, sem a necessidade de gerenciar recursos de computação e armazenamento subjacentes. Ele é particularmente útil para aplicações empresariais, pois é um serviço totalmente gerenciado com segurança de nível corporativo.

    Quando comparado ao desenvolvimento diretamente com a API LLM, o Azure AI Agent Service oferece algumas vantagens, incluindo:
  - Chamadas de ferramenta automáticas – não é necessário analisar uma chamada de ferramenta, invocar a ferramenta e lidar com a resposta; tudo isso agora é feito no lado do servidor.
  - Gerenciamento seguro de dados – em vez de gerenciar seu próprio estado de conversação, você pode contar com threads para armazenar todas as informações necessárias.
  - Ferramentas prontas para uso – Ferramentas que você pode usar para interagir com suas fontes de dados, como Bing, Azure AI Search e Azure Functions.

    As ferramentas disponíveis no Azure AI Agent Service podem ser divididas em duas categorias:

    1. Ferramentas de Conhecimento:
        - [Grounding com Bing Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview)
        - [Busca de Arquivos](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview)
        - [Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search)

    2. Ferramentas de Ação:
        - [Chamada de Função](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview)
        - [Interpretador de Código](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview)
        - [Ferramentas definidas pelo OpenAI](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview)
        - [Azure Functions](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview)

    O Agent Service nos permite usar essas ferramentas juntas como um `toolset`. It also utilizes `threads` which keep track of the history of messages from a particular conversation.

    Imagine you are a sales agent at a company called Contoso. You want to develop a conversational agent that can answer questions about your sales data.

    The image below illustrates how you could use Azure AI Agent Service to analyze your sales data:

    ![Agentic Service In Action](../../../translated_images/agent-service-in-action.jpg?WT.858cf9f67cc5c7f16ff3660d3df11c90e8cda37025bea4db5c4a59d2facce09a.pt.mc_id=academic-105485-koreyst)

    To use any of these tools with the service we can create a client and define a tool or toolset. To implement this practically we can use the Python code below. The LLM will be able to look at the toolset and decide whether to use the user created function, `fetch_sales_data_using_sqlite_query`, ou o Interpretador de Código pré-configurado dependendo da solicitação do usuário.

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

## Quais são as considerações especiais ao usar o Padrão de Design para Uso de Ferramentas para criar agentes de IA confiáveis?

Uma preocupação comum com SQL gerado dinamicamente por LLMs é a segurança, particularmente o risco de injeção de SQL ou ações maliciosas, como excluir ou alterar o banco de dados. Embora essas preocupações sejam válidas, elas podem ser mitigadas de forma eficaz configurando corretamente as permissões de acesso ao banco de dados. Para a maioria dos bancos de dados, isso envolve configurá-los como somente leitura. Para serviços de banco de dados como PostgreSQL ou Azure SQL, o aplicativo deve receber uma função de somente leitura (SELECT).

Executar o aplicativo em um ambiente seguro aumenta ainda mais a proteção. Em cenários empresariais, os dados geralmente são extraídos e transformados de sistemas operacionais para um banco de dados somente leitura ou data warehouse com um esquema amigável ao usuário. Essa abordagem garante que os dados sejam seguros, otimizados para desempenho e acessibilidade, e que o aplicativo tenha acesso restrito e somente leitura.

## Recursos Adicionais

- [Workshop do Azure AI Agents Service](https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/)
- [Workshop Multi-Agente do Contoso Creative Writer](https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop)
- [Tutorial de Chamadas de Função do Semantic Kernel](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)
- [Interpretador de Código do Semantic Kernel](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)
- [Ferramentas Autogen](https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html)
```

**Aviso Legal**:  
Este documento foi traduzido usando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.