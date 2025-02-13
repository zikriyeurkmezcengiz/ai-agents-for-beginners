```markdown
# Entwurfsmuster für die Nutzung von Tools  

## Einführung

In dieser Lektion wollen wir folgende Fragen beantworten:

- Was ist das Entwurfsmuster für die Nutzung von Tools?
- Für welche Anwendungsfälle kann es eingesetzt werden?
- Welche Elemente/Bausteine sind notwendig, um das Entwurfsmuster umzusetzen?
- Welche besonderen Überlegungen sind bei der Nutzung des Entwurfsmusters für die Entwicklung vertrauenswürdiger KI-Agenten zu beachten?

## Lernziele

Nach Abschluss dieser Lektion wirst du in der Lage sein:

- Das Entwurfsmuster für die Nutzung von Tools und dessen Zweck zu definieren.
- Anwendungsfälle zu identifizieren, in denen das Entwurfsmuster anwendbar ist.
- Die wichtigsten Elemente zu verstehen, die für die Implementierung des Entwurfsmusters erforderlich sind.
- Überlegungen zur Sicherstellung der Vertrauenswürdigkeit von KI-Agenten, die dieses Entwurfsmuster verwenden, zu erkennen.

## Was ist das Entwurfsmuster für die Nutzung von Tools?

Das **Entwurfsmuster für die Nutzung von Tools** konzentriert sich darauf, LLMs die Fähigkeit zu geben, mit externen Tools zu interagieren, um bestimmte Ziele zu erreichen. Tools sind Code, der von einem Agenten ausgeführt werden kann, um Aktionen durchzuführen. Ein Tool kann eine einfache Funktion wie ein Taschenrechner oder ein API-Aufruf zu einem Drittanbieterdienst wie eine Aktienkursabfrage oder eine Wettervorhersage sein. Im Kontext von KI-Agenten sind Tools so konzipiert, dass sie von Agenten als Antwort auf **modellgenerierte Funktionsaufrufe** ausgeführt werden.

## Für welche Anwendungsfälle kann es eingesetzt werden?

KI-Agenten können Tools nutzen, um komplexe Aufgaben zu erledigen, Informationen abzurufen oder Entscheidungen zu treffen. Das Entwurfsmuster für die Nutzung von Tools wird oft in Szenarien eingesetzt, die eine dynamische Interaktion mit externen Systemen wie Datenbanken, Webdiensten oder Code-Interpretern erfordern. Diese Fähigkeit ist für eine Vielzahl von Anwendungsfällen nützlich, darunter:

- **Dynamische Informationsbeschaffung:** Agenten können externe APIs oder Datenbanken abfragen, um aktuelle Daten abzurufen (z. B. Abfragen einer SQLite-Datenbank für Datenanalysen, Abrufen von Aktienkursen oder Wetterinformationen).
- **Codeausführung und -interpretation:** Agenten können Code oder Skripte ausführen, um mathematische Probleme zu lösen, Berichte zu erstellen oder Simulationen durchzuführen.
- **Workflow-Automatisierung:** Automatisierung von sich wiederholenden oder mehrstufigen Workflows durch die Integration von Tools wie Aufgabenplanern, E-Mail-Diensten oder Datenpipelines.
- **Kundensupport:** Agenten können mit CRM-Systemen, Ticketplattformen oder Wissensdatenbanken interagieren, um Benutzeranfragen zu lösen.
- **Inhaltsgenerierung und -bearbeitung:** Agenten können Tools wie Grammatikprüfer, Textzusammenfasser oder Inhaltsbewertungstools nutzen, um bei der Erstellung von Inhalten zu helfen.

## Welche Elemente/Bausteine sind notwendig, um das Entwurfsmuster für die Nutzung von Tools umzusetzen?

### Funktions-/Toolaufrufe

Der Funktionsaufruf ist der primäre Mechanismus, mit dem wir großen Sprachmodellen (LLMs) die Interaktion mit Tools ermöglichen. Häufig werden die Begriffe „Funktion“ und „Tool“ synonym verwendet, da „Funktionen“ (wiederverwendbare Codeblöcke) die „Tools“ sind, die Agenten verwenden, um Aufgaben auszuführen. Damit der Code einer Funktion aufgerufen werden kann, muss ein LLM die Benutzeranfrage mit der Beschreibung der Funktion vergleichen. Dazu wird ein Schema mit den Beschreibungen aller verfügbaren Funktionen an das LLM gesendet. Das LLM wählt dann die passendste Funktion für die Aufgabe aus und gibt deren Namen und Argumente zurück. Die ausgewählte Funktion wird aufgerufen, ihre Antwort wird an das LLM zurückgesendet, das die Informationen verwendet, um auf die Benutzeranfrage zu antworten.

Um Funktionsaufrufe für Agenten zu implementieren, benötigen Entwickler:

1. Ein LLM-Modell, das Funktionsaufrufe unterstützt
2. Ein Schema, das Funktionsbeschreibungen enthält
3. Den Code für jede beschriebene Funktion

Lass uns das Beispiel der Abfrage der aktuellen Uhrzeit in einer Stadt verwenden, um dies zu veranschaulichen:

- **Initialisierung eines LLMs, das Funktionsaufrufe unterstützt:**

    Nicht alle Modelle unterstützen Funktionsaufrufe, daher ist es wichtig zu überprüfen, ob das von dir verwendete LLM dies tut. [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling) unterstützt Funktionsaufrufe. Wir können damit beginnen, den Azure OpenAI-Client zu initialisieren.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

- **Erstellen eines Funktionsschemas:**

    Als Nächstes definieren wir ein JSON-Schema, das den Funktionsnamen, eine Beschreibung der Funktion sowie die Namen und Beschreibungen der Funktionsparameter enthält.
    Dieses Schema übergeben wir dann zusammen mit der Benutzeranfrage an den oben erstellten Client, um die Uhrzeit in San Francisco zu finden. Wichtig ist, dass ein **Toolaufruf** zurückgegeben wird, **nicht** die endgültige Antwort auf die Frage. Wie bereits erwähnt, gibt das LLM den Namen der Funktion zurück, die es für die Aufgabe ausgewählt hat, sowie die Argumente, die an sie übergeben werden.

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
  
- **Der Funktionscode, der zur Durchführung der Aufgabe erforderlich ist:**

    Nachdem das LLM entschieden hat, welche Funktion ausgeführt werden soll, muss der Code, der die Aufgabe ausführt, implementiert und ausgeführt werden.
    Wir können den Code implementieren, um die aktuelle Uhrzeit in Python abzurufen. Außerdem müssen wir den Code schreiben, um den Namen und die Argumente aus der response_message zu extrahieren, um das endgültige Ergebnis zu erhalten.

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

Der Funktionsaufruf steht im Mittelpunkt der meisten, wenn nicht aller Designs für die Tool-Nutzung von Agenten. Die Implementierung von Grund auf kann jedoch manchmal eine Herausforderung sein.
Wie wir in [Lektion 2](../../../02-explore-agentic-frameworks) gelernt haben, bieten agentische Frameworks uns vorgefertigte Bausteine zur Implementierung der Tool-Nutzung.

### Beispiele für die Nutzung von Tools mit agentischen Frameworks

- ### **[Semantic Kernel](https://learn.microsoft.com/azure/ai-services/agents/overview)**

    Semantic Kernel ist ein Open-Source-KI-Framework für .NET-, Python- und Java-Entwickler, die mit großen Sprachmodellen (LLMs) arbeiten. Es vereinfacht die Nutzung von Funktionsaufrufen, indem es deine Funktionen und deren Parameter automatisch durch einen Prozess namens [Serialisierung](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions) beschreibt. Außerdem übernimmt es die Kommunikation zwischen dem Modell und deinem Code. Ein weiterer Vorteil eines agentischen Frameworks wie Semantic Kernel ist, dass es den Zugriff auf vorgefertigte Tools wie [File Search](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py) und [Code Interpreter](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py) ermöglicht.

    Das folgende Diagramm zeigt den Prozess des Funktionsaufrufs mit Semantic Kernel:

    ![Funktionsaufruf](../../../translated_images/functioncalling-diagram.b5493ea5154ad8e3e4940d2e36a49101eec1398948e5d1039942203b4f5a4209.de.png)

    In Semantic Kernel werden Funktionen/Tools als [Plugins](https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python) bezeichnet. Wir können die `get_current_time` function we saw earlier into a plugin by turning it into a class with the function in it. We can also import the `kernel_function`-Dekorator verwenden, der die Beschreibung der Funktion enthält. Wenn du dann einen Kernel mit dem GetCurrentTimePlugin erstellst, serialisiert der Kernel die Funktion und ihre Parameter automatisch und erstellt dabei das Schema, das an das LLM gesendet wird.

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

    Der Azure AI Agent Service ist ein neues agentisches Framework, das Entwicklern dabei helfen soll, hochwertige, erweiterbare KI-Agenten sicher zu erstellen, bereitzustellen und zu skalieren, ohne die zugrunde liegenden Rechen- und Speicherressourcen verwalten zu müssen. Es ist besonders nützlich für Unternehmensanwendungen, da es ein vollständig verwalteter Dienst mit Sicherheit auf Unternehmensniveau ist.

    Im Vergleich zur direkten Entwicklung mit der LLM-API bietet der Azure AI Agent Service einige Vorteile, darunter:
  - Automatische Toolaufrufe – kein Parsen eines Toolaufrufs, Ausführen des Tools und Verarbeiten der Antwort erforderlich; all dies erfolgt nun serverseitig
  - Sicher verwaltete Daten – anstelle der Verwaltung des eigenen Gesprächsstatus kann man sich auf Threads verlassen, um alle benötigten Informationen zu speichern
  - Tools out-of-the-box – Tools, die zur Interaktion mit Datenquellen verwendet werden können, wie Bing, Azure AI Search und Azure Functions.

    Die im Azure AI Agent Service verfügbaren Tools lassen sich in zwei Kategorien unterteilen:

    1. Wissenstools:
        - [Grounding mit Bing Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview)
        - [File Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview)
        - [Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search)

    2. Aktionstools:
        - [Funktionsaufrufe](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview)
        - [Code Interpreter](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview)
        - [Von OpenAI definierte Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview)
        - [Azure Functions](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview)

    Der Agent Service ermöglicht die Nutzung dieser Tools zusammen als `toolset`. It also utilizes `threads` which keep track of the history of messages from a particular conversation.

    Imagine you are a sales agent at a company called Contoso. You want to develop a conversational agent that can answer questions about your sales data.

    The image below illustrates how you could use Azure AI Agent Service to analyze your sales data:

    ![Agentic Service In Action](../../../translated_images/agent-service-in-action.jpg?WT.858cf9f67cc5c7f16ff3660d3df11c90e8cda37025bea4db5c4a59d2facce09a.de.mc_id=academic-105485-koreyst)

    To use any of these tools with the service we can create a client and define a tool or toolset. To implement this practically we can use the Python code below. The LLM will be able to look at the toolset and decide whether to use the user created function, `fetch_sales_data_using_sqlite_query` oder des vorgefertigten Code Interpreters, abhängig von der Benutzeranfrage.

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

## Welche besonderen Überlegungen sind bei der Nutzung des Entwurfsmusters für die Entwicklung vertrauenswürdiger KI-Agenten zu beachten?

Ein häufiges Anliegen bei SQL, das dynamisch von LLMs generiert wird, ist die Sicherheit, insbesondere das Risiko von SQL-Injection oder bösartigen Aktionen, wie das Löschen oder Manipulieren der Datenbank. Obwohl diese Bedenken berechtigt sind, können sie effektiv durch die richtige Konfiguration der Datenbankzugriffsrechte gemindert werden. Bei den meisten Datenbanken bedeutet dies, die Datenbank als schreibgeschützt zu konfigurieren. Für Datenbankdienste wie PostgreSQL oder Azure SQL sollte der App eine schreibgeschützte (SELECT) Rolle zugewiesen werden.

Das Ausführen der App in einer sicheren Umgebung erhöht den Schutz weiter. In Unternehmensszenarien werden Daten typischerweise aus operativen Systemen in eine schreibgeschützte Datenbank oder ein Data Warehouse mit einer benutzerfreundlichen Schema extrahiert und transformiert. Dieser Ansatz stellt sicher, dass die Daten sicher sind, für Leistung und Zugänglichkeit optimiert und dass die App eingeschränkten, schreibgeschützten Zugriff hat.

## Zusätzliche Ressourcen

- [Azure AI Agents Service Workshop](https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/)
- [Contoso Creative Writer Multi-Agent Workshop](https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop)
- [Semantic Kernel Function Calling Tutorial](https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions)
- [Semantic Kernel Code Interpreter](https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py)
- [Autogen Tools](https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html)
```

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.