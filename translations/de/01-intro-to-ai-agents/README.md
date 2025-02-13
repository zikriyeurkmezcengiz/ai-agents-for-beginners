# Einführung in KI-Agenten und deren Anwendungsfälle

Willkommen zum Kurs "KI-Agenten für Anfänger"! Dieser Kurs vermittelt Ihnen grundlegendes Wissen und praktische Beispiele für die Arbeit mit KI-Agenten.

Treten Sie der [Azure AI Discord Community](https://discord.gg/kzRShWzttr) bei, um andere Lernende und Entwickler von KI-Agenten kennenzulernen und alle Fragen zu diesem Kurs zu stellen.

Zu Beginn des Kurses verschaffen wir uns zunächst ein besseres Verständnis darüber, was KI-Agenten sind und wie wir sie in den Anwendungen und Arbeitsabläufen, die wir entwickeln, einsetzen können.

## Einführung

Diese Lektion behandelt:

- Was sind KI-Agenten und welche Arten von Agenten gibt es?
- Für welche Anwendungsfälle eignen sich KI-Agenten besonders, und wie können sie uns helfen?
- Was sind die grundlegenden Bausteine beim Entwerfen agentenbasierter Lösungen?

## Lernziele
Nach Abschluss dieser Lektion sollten Sie in der Lage sein:

- Die Konzepte von KI-Agenten zu verstehen und zu erkennen, wie sie sich von anderen KI-Lösungen unterscheiden.
- KI-Agenten effizient einzusetzen.
- Agentenbasierte Lösungen produktiv für Benutzer und Kunden zu entwerfen.

## Definition von KI-Agenten und Typen von KI-Agenten

### Was sind KI-Agenten?

KI-Agenten sind **Systeme**, die es **Großen Sprachmodellen (LLMs)** ermöglichen, **Aktionen auszuführen**, indem sie deren Fähigkeiten erweitern und ihnen **Zugang zu Werkzeugen** und **Wissen** geben.

Lassen Sie uns diese Definition in kleinere Teile zerlegen:

- **System** – Es ist wichtig, Agenten nicht nur als eine einzelne Komponente zu betrachten, sondern als ein System aus vielen Komponenten. Auf der grundlegenden Ebene bestehen die Komponenten eines KI-Agenten aus:
  - **Umgebung** – Der definierte Raum, in dem der KI-Agent arbeitet. Zum Beispiel könnte die Umgebung eines Reisebuchungs-Agenten das Buchungssystem sein, das der Agent verwendet, um Aufgaben zu erledigen.
  - **Sensoren** – Umgebungen enthalten Informationen und geben Rückmeldungen. KI-Agenten nutzen Sensoren, um diese Informationen über den aktuellen Zustand der Umgebung zu sammeln und zu interpretieren. Im Beispiel des Reisebuchungs-Agenten könnte das Buchungssystem Informationen wie Hotelverfügbarkeit oder Flugpreise liefern.
  - **Aktuatoren** – Sobald der KI-Agent den aktuellen Zustand der Umgebung erhält, entscheidet er, welche Aktion für die jeweilige Aufgabe ausgeführt werden soll, um die Umgebung zu verändern. Im Fall des Reisebuchungs-Agenten könnte dies bedeuten, ein verfügbares Zimmer für den Benutzer zu buchen.

![Was sind KI-Agenten?](../../../translated_images/what-are-ai-agents.png?WT.7f2607783e984be0cfb6dd064ad20389d37cf6d1d28bc5d5a3c648ef353bde89.de.mc_id=academic-105485-koreyst)

**Große Sprachmodelle** – Das Konzept von Agenten existierte bereits vor der Entwicklung von LLMs. Der Vorteil beim Aufbau von KI-Agenten mit LLMs liegt in ihrer Fähigkeit, menschliche Sprache und Daten zu interpretieren. Diese Fähigkeit ermöglicht es LLMs, Umgebungsinformationen zu verstehen und einen Plan zur Veränderung der Umgebung zu definieren.

**Aktionen ausführen** – Außerhalb von KI-Agenten-Systemen sind LLMs darauf beschränkt, Inhalte oder Informationen basierend auf einer Benutzereingabe zu generieren. Innerhalb von KI-Agenten-Systemen können LLMs Aufgaben ausführen, indem sie die Anfrage des Benutzers interpretieren und die in ihrer Umgebung verfügbaren Werkzeuge nutzen.

**Zugang zu Werkzeugen** – Welche Werkzeuge dem LLM zur Verfügung stehen, wird durch 1) die Umgebung, in der es arbeitet, und 2) den Entwickler des KI-Agenten definiert. Im Beispiel des Reisebuchungs-Agenten sind die Werkzeuge des Agenten durch die im Buchungssystem verfügbaren Operationen begrenzt, oder der Entwickler kann den Zugriff des Agenten auf bestimmte Werkzeuge wie Flüge beschränken.

**Wissen** – Neben den Informationen, die von der Umgebung bereitgestellt werden, können KI-Agenten auch Wissen aus anderen Systemen, Diensten, Werkzeugen und sogar anderen Agenten abrufen. Im Beispiel des Reisebuchungs-Agenten könnte dieses Wissen Informationen über die Reisevorlieben des Benutzers aus einer Kundendatenbank umfassen.

### Die verschiedenen Arten von Agenten

Nachdem wir eine allgemeine Definition von KI-Agenten haben, betrachten wir nun einige spezifische Agententypen und wie sie auf einen Reisebuchungs-Agenten angewendet werden könnten.

| **Agententyp**                | **Beschreibung**                                                                                                                      | **Beispiel**                                                                                                                                                                                                                   |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Einfache Reflex-Agenten**   | Führen sofortige Aktionen basierend auf vordefinierten Regeln aus.                                                                     | Der Reiseagent interpretiert den Kontext einer E-Mail und leitet Beschwerden über Reisen an den Kundenservice weiter.                                                                                                          |
| **Modellbasierte Reflex-Agenten** | Führen Aktionen basierend auf einem Modell der Welt und dessen Veränderungen aus.                                                     | Der Reiseagent priorisiert Routen mit signifikanten Preisänderungen, basierend auf Zugriff auf historische Preisdaten.                                                                                                        |
| **Zielorientierte Agenten**   | Erstellen Pläne, um bestimmte Ziele zu erreichen, indem sie das Ziel interpretieren und Aktionen bestimmen, um es zu erreichen.         | Der Reiseagent bucht eine Reise, indem er die notwendigen Reisevorkehrungen (Auto, öffentliche Verkehrsmittel, Flüge) vom aktuellen Standort bis zum Zielort ermittelt.                                                        |
| **Nutzenbasierte Agenten**    | Berücksichtigen Präferenzen und wägen numerische Kompromisse ab, um Ziele zu erreichen.                                                | Der Reiseagent maximiert den Nutzen, indem er Bequemlichkeit gegenüber Kosten abwägt, wenn er Reisen bucht.                                                                                                                   |
| **Lernende Agenten**          | Verbessern sich im Laufe der Zeit, indem sie auf Feedback reagieren und ihre Aktionen entsprechend anpassen.                           | Der Reiseagent verbessert sich, indem er Kundenfeedback aus Nach-Reise-Umfragen nutzt, um zukünftige Buchungen anzupassen.                                                                                                    |
| **Hierarchische Agenten**     | Bestehen aus mehreren Agenten in einem gestuften System, wobei höherstufige Agenten Aufgaben in Unteraufgaben für niedrigerstufige Agenten aufteilen. | Der Reiseagent storniert eine Reise, indem er die Aufgabe in Unteraufgaben aufteilt (z. B. spezifische Buchungen stornieren) und niedrigere Agenten diese ausführen lässt, die wiederum an den höherstufigen Agenten berichten. |
| **Multi-Agenten-Systeme (MAS)** | Agenten erledigen Aufgaben unabhängig, entweder kooperativ oder im Wettbewerb.                                                         | Kooperativ: Mehrere Agenten buchen spezifische Reisedienstleistungen wie Hotels, Flüge und Unterhaltung. Wettbewerbsorientiert: Mehrere Agenten verwalten und konkurrieren um einen gemeinsamen Hotelbuchungskalender, um Kunden in das Hotel einzubuchen.             |

## Wann sollten KI-Agenten eingesetzt werden?

Im vorherigen Abschnitt haben wir das Beispiel eines Reisebuchungs-Agenten genutzt, um zu erklären, wie verschiedene Agententypen in unterschiedlichen Szenarien eingesetzt werden können. Dieses Anwendungsbeispiel wird im gesamten Kurs weiterverwendet.

Schauen wir uns die Arten von Anwendungsfällen an, für die sich KI-Agenten am besten eignen:

![Wann sollten KI-Agenten eingesetzt werden?](../../../translated_images/when-to-use-ai-agents.png?WT.1681e3f19611f820ee4331ab494b50ebc6f09b2fb4df3a5f4dac5458316263ad.de.mc_id=academic-105485-koreyst)

- **Offene Problemstellungen** – Ermöglicht dem LLM, die notwendigen Schritte zur Erledigung einer Aufgabe zu bestimmen, da diese nicht immer fest in einen Arbeitsablauf programmiert werden können.
- **Mehrstufige Prozesse** – Aufgaben, die ein gewisses Maß an Komplexität erfordern, bei denen der KI-Agent Werkzeuge oder Informationen über mehrere Schritte hinweg nutzen muss, anstatt sie in einem einzigen Schritt abzurufen.  
- **Verbesserung über Zeit** – Aufgaben, bei denen der Agent durch Feedback aus seiner Umgebung oder von Benutzern im Laufe der Zeit besser werden kann, um einen höheren Nutzen zu bieten.

Weitere Überlegungen zum Einsatz von KI-Agenten behandeln wir in der Lektion "Vertrauenswürdige KI-Agenten entwickeln".

## Grundlagen agentenbasierter Lösungen

### Entwicklung von Agenten

Der erste Schritt bei der Gestaltung eines KI-Agenten-Systems besteht darin, die Werkzeuge, Aktionen und Verhaltensweisen zu definieren. In diesem Kurs konzentrieren wir uns auf die Verwendung des **Azure AI Agent Service**, um unsere Agenten zu definieren. Dieser bietet Funktionen wie:

- Auswahl offener Modelle wie OpenAI, Mistral und Llama
- Nutzung lizenzierter Daten durch Anbieter wie Tripadvisor
- Verwendung standardisierter OpenAPI 3.0-Werkzeuge

### Agentenbasierte Muster

Die Kommunikation mit LLMs erfolgt über Prompts. Aufgrund der halbautonomen Natur von KI-Agenten ist es nicht immer möglich oder notwendig, das LLM manuell nach jeder Veränderung in der Umgebung erneut zu prompten. Wir verwenden **agentenbasierte Muster**, die es uns ermöglichen, das LLM über mehrere Schritte hinweg auf skalierbare Weise zu prompten.

Dieser Kurs ist in einige der derzeit populären agentenbasierten Muster unterteilt.

### Agentenbasierte Frameworks

Agentenbasierte Frameworks ermöglichen es Entwicklern, agentenbasierte Muster durch Code zu implementieren. Diese Frameworks bieten Vorlagen, Plugins und Werkzeuge für eine bessere Zusammenarbeit von KI-Agenten. Diese Vorteile ermöglichen eine bessere Beobachtbarkeit und Fehlerbehebung in KI-Agenten-Systemen.

In diesem Kurs werden wir das forschungsgetriebene AutoGen-Framework sowie das produktionsreife Agent-Framework von Semantic Kernel erkunden.

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.