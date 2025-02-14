```markdown
# Erforsche KI-Agenten-Frameworks

KI-Agenten-Frameworks sind Softwareplattformen, die die Erstellung, Bereitstellung und Verwaltung von KI-Agenten vereinfachen sollen. Diese Frameworks bieten Entwicklern vorgefertigte Komponenten, Abstraktionen und Werkzeuge, die die Entwicklung komplexer KI-Systeme beschleunigen.

Diese Frameworks helfen Entwicklern, sich auf die einzigartigen Aspekte ihrer Anwendungen zu konzentrieren, indem sie standardisierte Ansätze für häufige Herausforderungen in der KI-Agenten-Entwicklung bereitstellen. Sie verbessern die Skalierbarkeit, Zugänglichkeit und Effizienz beim Aufbau von KI-Systemen.

## Einführung

Diese Lektion behandelt:

- Was sind KI-Agenten-Frameworks und was ermöglichen sie Entwicklern?
- Wie können Teams diese Frameworks nutzen, um schnell Prototypen zu erstellen, zu iterieren und die Fähigkeiten meiner Agenten zu verbessern?
- Welche Unterschiede gibt es zwischen den von Microsoft entwickelten Frameworks und Tools ([Autogen](https://aka.ms/ai-agents/autogen) / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel) / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service))?
- Kann ich meine bestehenden Azure-Ökosystem-Tools direkt integrieren, oder benötige ich eigenständige Lösungen?
- Was ist der Azure AI Agent Service und wie unterstützt er mich?

## Lernziele

Die Ziele dieser Lektion sind:

- Die Rolle von KI-Agenten-Frameworks in der KI-Entwicklung zu verstehen.
- Wie man KI-Agenten-Frameworks einsetzt, um intelligente Agenten zu entwickeln.
- Die wichtigsten Funktionen, die durch KI-Agenten-Frameworks ermöglicht werden.
- Die Unterschiede zwischen Autogen, Semantic Kernel und Azure AI Agent Service.

## Was sind KI-Agenten-Frameworks und was ermöglichen sie Entwicklern?

Traditionelle KI-Frameworks können dabei helfen, KI in Apps zu integrieren und diese Apps auf folgende Weise zu verbessern:

- **Personalisierung**: KI kann das Nutzerverhalten und die Vorlieben analysieren, um personalisierte Empfehlungen, Inhalte und Erlebnisse zu bieten.
Beispiel: Streaming-Dienste wie Netflix nutzen KI, um Filme und Serien basierend auf der Seh-Historie vorzuschlagen, was die Nutzerbindung und Zufriedenheit erhöht.
- **Automatisierung und Effizienz**: KI kann repetitive Aufgaben automatisieren, Arbeitsabläufe optimieren und die betriebliche Effizienz steigern.
Beispiel: Kundenservice-Apps nutzen KI-gestützte Chatbots, um häufige Anfragen zu bearbeiten, wodurch Antwortzeiten verkürzt und menschliche Mitarbeiter für komplexere Probleme freigestellt werden.
- **Verbesserte Nutzererfahrung**: KI kann die allgemeine Nutzererfahrung verbessern, indem sie intelligente Funktionen wie Spracherkennung, natürliche Sprachverarbeitung und prädiktiven Text bereitstellt.
Beispiel: Virtuelle Assistenten wie Siri und Google Assistant nutzen KI, um Sprachbefehle zu verstehen und darauf zu reagieren, was die Interaktion der Nutzer mit ihren Geräten erleichtert.

### Klingt großartig, oder? Warum brauchen wir dann KI-Agenten-Frameworks?

KI-Agenten-Frameworks gehen über herkömmliche KI-Frameworks hinaus. Sie sind darauf ausgelegt, die Erstellung intelligenter Agenten zu ermöglichen, die mit Nutzern, anderen Agenten und der Umgebung interagieren können, um spezifische Ziele zu erreichen. Diese Agenten können autonomes Verhalten zeigen, Entscheidungen treffen und sich an veränderte Bedingungen anpassen. Werfen wir einen Blick auf einige der wichtigsten Funktionen, die durch KI-Agenten-Frameworks ermöglicht werden:

- **Zusammenarbeit und Koordination von Agenten**: Ermöglicht die Erstellung mehrerer KI-Agenten, die zusammenarbeiten, kommunizieren und koordiniert komplexe Aufgaben lösen können.
- **Automatisierung und Verwaltung von Aufgaben**: Bietet Mechanismen zur Automatisierung mehrstufiger Arbeitsabläufe, zur Aufgabenverteilung und zum dynamischen Aufgabenmanagement zwischen Agenten.
- **Kontextuelles Verständnis und Anpassung**: Rüstet Agenten mit der Fähigkeit aus, Kontext zu verstehen, sich an sich verändernde Umgebungen anzupassen und Entscheidungen auf Basis von Echtzeitinformationen zu treffen.

Zusammenfassend lässt sich sagen, dass Agenten es ermöglichen, mehr zu leisten, Automatisierung auf die nächste Stufe zu heben und intelligentere Systeme zu schaffen, die sich an ihre Umgebung anpassen und aus ihr lernen können.

## Wie kann man die Fähigkeiten eines Agenten schnell prototypisieren, iterieren und verbessern?

Dies ist ein schnelllebiges Feld, aber es gibt einige Gemeinsamkeiten, die die meisten KI-Agenten-Frameworks bieten, um Prototypen schnell zu erstellen und zu iterieren. Dazu gehören modulare Komponenten, kollaborative Werkzeuge und Echtzeitlernen. Schauen wir uns diese genauer an:

- **Modulare Komponenten nutzen**: KI-Frameworks bieten vorgefertigte Komponenten wie Prompts, Parser und Speichermanagement.
- **Kollaborative Werkzeuge einsetzen**: Agenten mit spezifischen Rollen und Aufgaben entwerfen, um kollaborative Arbeitsabläufe zu testen und zu verfeinern.
- **In Echtzeit lernen**: Feedback-Schleifen implementieren, bei denen Agenten aus Interaktionen lernen und ihr Verhalten dynamisch anpassen.

### Modulare Komponenten nutzen

Frameworks wie LangChain und Microsoft Semantic Kernel bieten vorgefertigte Komponenten wie Prompts, Parser und Speichermanagement.

**Wie Teams diese nutzen können**: Teams können diese Komponenten schnell zusammenfügen, um einen funktionalen Prototyp zu erstellen, ohne von Grund auf neu beginnen zu müssen. Dies ermöglicht schnelles Experimentieren und Iterieren.

**Wie es in der Praxis funktioniert**: Sie können einen vorgefertigten Parser verwenden, um Informationen aus Benutzereingaben zu extrahieren, ein Speichermodul zum Speichern und Abrufen von Daten und einen Prompt-Generator, um mit Benutzern zu interagieren – alles ohne diese Komponenten selbst entwickeln zu müssen.

**Beispielcode**. Schauen wir uns ein Beispiel an, wie ein vorgefertigter Parser verwendet werden kann, um Informationen aus Benutzereingaben zu extrahieren:

```python
from langchain import Parser

parser = Parser()
user_input = "Book a flight from New York to London on July 15th"

parsed_data = parser.parse(user_input)

print(parsed_data)
# Output: {'origin': 'New York', 'destination': 'London', 'date': 'July 15th'}
```

In diesem Beispiel sehen Sie, wie ein vorgefertigter Parser verwendet werden kann, um Schlüsselinformationen aus Benutzereingaben zu extrahieren, wie z. B. den Ursprung, das Ziel und das Datum einer Flugbuchungsanfrage. Dieser modulare Ansatz ermöglicht es, sich auf die übergeordnete Logik zu konzentrieren.

### Kollaborative Werkzeuge einsetzen

Frameworks wie CrewAI und Microsoft Autogen erleichtern die Erstellung mehrerer Agenten, die zusammenarbeiten können.

**Wie Teams diese nutzen können**: Teams können Agenten mit spezifischen Rollen und Aufgaben entwerfen, um kollaborative Arbeitsabläufe zu testen und zu verfeinern und die Gesamteffizienz des Systems zu verbessern.

**Wie es in der Praxis funktioniert**: Sie können ein Team von Agenten erstellen, bei dem jeder Agent eine spezialisierte Funktion hat, wie z. B. Datenabruf, Analyse oder Entscheidungsfindung. Diese Agenten können kommunizieren und Informationen austauschen, um ein gemeinsames Ziel zu erreichen, wie z. B. eine Benutzeranfrage zu beantworten oder eine Aufgabe abzuschließen.

**Beispielcode (Autogen)**:

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

In diesem Code sehen Sie, wie eine Aufgabe erstellt wird, die mehrere Agenten einbezieht, die zusammenarbeiten, um Daten zu analysieren. Jeder Agent erfüllt eine spezifische Funktion, und die Aufgabe wird durch die Koordination der Agenten ausgeführt, um das gewünschte Ergebnis zu erzielen. Durch die Erstellung dedizierter Agenten mit spezialisierten Rollen können Sie die Effizienz und Leistung von Aufgaben verbessern.

### In Echtzeit lernen

Fortschrittliche Frameworks bieten Funktionen für kontextuelles Echtzeitverstehen und Anpassung.

**Wie Teams diese nutzen können**: Teams können Feedback-Schleifen implementieren, bei denen Agenten aus Interaktionen lernen und ihr Verhalten dynamisch anpassen, was zu einer kontinuierlichen Verbesserung und Verfeinerung der Fähigkeiten führt.

**Wie es in der Praxis funktioniert**: Agenten können Benutzerfeedback, Umweltdaten und Aufgabenergebnisse analysieren, um ihre Wissensbasis zu aktualisieren, Entscheidungsalgorithmen anzupassen und ihre Leistung im Laufe der Zeit zu verbessern. Dieser iterative Lernprozess ermöglicht es Agenten, sich an sich ändernde Bedingungen und Benutzerpräferenzen anzupassen, wodurch die Gesamteffektivität des Systems gesteigert wird.

## Was sind die Unterschiede zwischen den Frameworks Autogen, Semantic Kernel und Azure AI Agent Service?

Es gibt viele Möglichkeiten, diese Frameworks zu vergleichen, aber lassen Sie uns einige der wichtigsten Unterschiede in Bezug auf Design, Fähigkeiten und Zielanwendungen betrachten:

## Autogen

Ein Open-Source-Framework, entwickelt vom AI Frontiers Lab von Microsoft Research. Es konzentriert sich auf ereignisgesteuerte, verteilte *agentische* Anwendungen und ermöglicht mehrere LLMs, SLMs, Tools und fortgeschrittene Multi-Agent-Designmuster.

Autogen basiert auf dem Kernkonzept der Agenten, die autonome Einheiten sind, die ihre Umgebung wahrnehmen, Entscheidungen treffen und Aktionen ausführen können, um bestimmte Ziele zu erreichen. Agenten kommunizieren über asynchrone Nachrichten, was ihnen ermöglicht, unabhängig und parallel zu arbeiten, wodurch die Skalierbarkeit und Reaktionsfähigkeit des Systems verbessert wird.

Agenten basieren auf dem [Aktor-Modell](https://en.wikipedia.org/wiki/Actor_model). Laut Wikipedia ist ein Aktor _die grundlegende Baueinheit für parallele Berechnungen. Als Antwort auf eine empfangene Nachricht kann ein Aktor lokale Entscheidungen treffen, weitere Aktoren erstellen, weitere Nachrichten senden und bestimmen, wie auf die nächste empfangene Nachricht reagiert wird_.

**Anwendungsfälle**: Automatisierung von Code-Generierung, Datenanalyseaufgaben und Entwicklung maßgeschneiderter Agenten für Planungs- und Forschungsfunktionen.

Hier sind einige wichtige Kernkonzepte von Autogen:

- **Agenten**: Ein Agent ist eine Softwareeinheit, die:
  - **Über Nachrichten kommuniziert**, synchron oder asynchron.
  - **Einen eigenen Zustand aufrechterhält**, der durch eingehende Nachrichten geändert werden kann.
  - **Aktionen ausführt** als Reaktion auf empfangene Nachrichten oder Änderungen ihres Zustands.

  Hier ein kurzer Codeausschnitt, wie ein eigener Agent mit Chat-Fähigkeiten erstellt wird:

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
    
    In obigem Code ist `MyAssistant` has been created and inherits from `RoutedAgent`. It has a message handler that prints the content of the message and then sends a response using the `AssistantAgent` delegate. Especially note how we assign to `self._delegate` an instance of `AssistantAgent` ein vorgefertigter Agent, der Chat-Abschlüsse bearbeiten kann.

    Lassen Sie uns Autogen über diesen Agententyp informieren und das Programm starten:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Oben wird der Agent mit der Laufzeit registriert und dann eine Nachricht an den Agenten gesendet, was zu folgendem Ergebnis führt:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-Agenten**: Autogen unterstützt die Erstellung mehrerer Agenten, die zusammenarbeiten können, um komplexe Aufgaben zu lösen. Sie können unterschiedliche Typen von Agenten mit spezialisierten Funktionen und Rollen definieren, z. B. Datenabruf, Analyse, Entscheidungsfindung und Benutzerinteraktion. Sehen wir uns an, wie eine solche Erstellung aussieht:

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

    Oben wird ein `GroupChatManager` mit der Laufzeit registriert. Dieser Manager ist für die Koordination der Interaktionen zwischen verschiedenen Agententypen wie Autoren, Illustratoren, Redakteuren und Nutzern verantwortlich.

- **Agenten-Laufzeit**: Das Framework bietet eine Laufzeitumgebung, die die Kommunikation zwischen Agenten ermöglicht, ihre Identitäten und Lebenszyklen verwaltet und Sicherheits- sowie Datenschutzgrenzen durchsetzt. Dies bedeutet, dass Sie Ihre Agenten in einer sicheren und kontrollierten Umgebung ausführen können, was eine sichere und effiziente Interaktion gewährleistet. Es gibt zwei interessante Laufzeiten:
  - **Standalone-Laufzeit**: Eine gute Wahl für Einzelprozessanwendungen, bei denen alle Agenten in derselben Programmiersprache implementiert und im selben Prozess ausgeführt werden. Hier ist eine Illustration, wie es funktioniert:
  
  ![Standalone-Laufzeit](https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg)   
  *Agenten kommunizieren über Nachrichten durch die Laufzeit, und die Laufzeit verwaltet den Lebenszyklus der Agenten.*

  - **Verteilte Agenten-Laufzeit**: Geeignet für Multi-Prozess-Anwendungen, bei denen Agenten in verschiedenen Programmiersprachen implementiert und auf verschiedenen Maschinen ausgeführt werden können. Hier ist eine Illustration, wie es funktioniert:
  
  ![Verteilte Laufzeit](https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg)
```

basierend auf Projektzielen. Ideal für das Verständnis natürlicher Sprache und die Generierung von Inhalten. - **Azure AI Agent Service**: Flexible Modelle, unternehmenssichere Mechanismen, Daten-Speichermethoden. Ideal für die sichere, skalierbare und flexible Bereitstellung von KI-Agenten in Unternehmensanwendungen. ## Kann ich meine bestehenden Azure-Ökosystem-Tools direkt integrieren, oder benötige ich eigenständige Lösungen? Die Antwort ist ja, Sie können Ihre bestehenden Azure-Ökosystem-Tools direkt mit dem Azure AI Agent Service integrieren, insbesondere, da dieser nahtlos mit anderen Azure-Diensten zusammenarbeitet. Sie könnten beispielsweise Bing, Azure AI Search und Azure Functions integrieren. Es gibt auch eine tiefe Integration mit Azure AI Foundry. Für Autogen und Semantic Kernel können Sie ebenfalls mit Azure-Diensten integrieren, allerdings kann es erforderlich sein, die Azure-Dienste aus Ihrem Code aufzurufen. Eine weitere Möglichkeit zur Integration besteht darin, die Azure SDKs zu verwenden, um von Ihren Agenten aus mit Azure-Diensten zu interagieren. Außerdem, wie bereits erwähnt, können Sie den Azure AI Agent Service als Orchestrator für Ihre in Autogen oder Semantic Kernel erstellten Agenten verwenden, was einen einfachen Zugang zum Azure-Ökosystem ermöglicht. ## Referenzen - [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357) - [2] - [Semantic Kernel and Autogen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/) - [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp) - [4] - [Azure AI Agent service](https://learn.microsoft.com/azure/ai-services/agents/overview) - [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121)

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.