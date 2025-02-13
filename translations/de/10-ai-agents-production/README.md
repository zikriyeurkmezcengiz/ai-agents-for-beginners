```markdown
# KI-Agenten in der Produktion

## Einführung

Diese Lektion behandelt:

- Wie Sie die Bereitstellung Ihres KI-Agenten in der Produktion effektiv planen.
- Häufige Fehler und Probleme, die bei der Bereitstellung Ihres KI-Agenten in der Produktion auftreten können.
- Wie Sie die Kosten verwalten und gleichzeitig die Leistung Ihres KI-Agenten aufrechterhalten können.

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie Sie:

- Techniken anwenden können, um die Leistung, Kosten und Effektivität eines KI-Agentensystems in der Produktion zu verbessern.
- Ihre KI-Agenten bewerten können und verstehen, was dabei zu beachten ist.
- Kosten kontrollieren können, wenn Sie KI-Agenten in die Produktion bringen.

Es ist wichtig, vertrauenswürdige KI-Agenten bereitzustellen. Schauen Sie sich dazu auch die Lektion "Vertrauenswürdige KI-Agenten erstellen" an.

## Bewertung von KI-Agenten

Vor, während und nach der Bereitstellung von KI-Agenten ist es entscheidend, ein geeignetes System zur Bewertung Ihrer KI-Agenten zu haben. Dies stellt sicher, dass Ihr System mit Ihren und den Zielen Ihrer Nutzer übereinstimmt.

Um einen KI-Agenten zu bewerten, ist es wichtig, nicht nur die Ausgabe des Agenten zu analysieren, sondern das gesamte System, in dem Ihr KI-Agent arbeitet. Dies umfasst unter anderem:

- Die anfängliche Modellanfrage.
- Die Fähigkeit des Agenten, die Absicht des Nutzers zu erkennen.
- Die Fähigkeit des Agenten, das richtige Tool zur Aufgabenbewältigung auszuwählen.
- Die Antwort des Tools auf die Anfrage des Agenten.
- Die Fähigkeit des Agenten, die Antwort des Tools zu interpretieren.
- Das Feedback des Nutzers auf die Antwort des Agenten.

So können Sie Verbesserungsbereiche auf eine modulare Weise identifizieren. Anschließend können Sie die Auswirkungen von Änderungen an Modellen, Prompts, Tools und anderen Komponenten effizienter überwachen.

## Häufige Probleme und mögliche Lösungen bei KI-Agenten

| **Problem**                                   | **Mögliche Lösung**                                                                                                                                                                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| KI-Agent führt Aufgaben nicht konsistent aus  | - Verfeinern Sie den Prompt, der dem KI-Agenten gegeben wird; seien Sie klar in den Zielen.<br>- Überlegen Sie, ob das Aufteilen der Aufgaben in Teilaufgaben und deren Bearbeitung durch mehrere Agenten hilfreich sein könnte. |
| KI-Agent gerät in Endlosschleifen             | - Stellen Sie klare Abbruchbedingungen und -kriterien bereit, damit der Agent weiß, wann der Prozess beendet werden soll.<br>- Für komplexe Aufgaben, die logisches Denken und Planung erfordern, verwenden Sie ein größeres Modell, das auf solche Aufgaben spezialisiert ist. |
| Tool-Anfragen des KI-Agenten funktionieren nicht gut | - Testen und validieren Sie die Ausgabe des Tools außerhalb des Agentensystems.<br>- Verfeinern Sie die definierten Parameter, Prompts und die Benennung der Tools.                                                      |
| Multi-Agenten-System arbeitet nicht konsistent | - Verfeinern Sie die Prompts für jeden Agenten, um sicherzustellen, dass sie spezifisch und voneinander unterscheidbar sind.<br>- Erstellen Sie ein hierarchisches System mit einem "Routing-" oder Steuerungsagenten, der entscheidet, welcher Agent der richtige ist. |

## Kostenmanagement

Hier sind einige Strategien, um die Kosten für die Bereitstellung von KI-Agenten in der Produktion zu verwalten:

- **Antworten zwischenspeichern** - Häufige Anfragen und Aufgaben zu identifizieren und die Antworten bereitzustellen, bevor sie durch Ihr agentisches System laufen, ist eine gute Möglichkeit, das Volumen ähnlicher Anfragen zu reduzieren. Sie können sogar einen Ablauf implementieren, um zu bestimmen, wie ähnlich eine Anfrage den zwischengespeicherten Anfragen ist, indem Sie einfachere KI-Modelle verwenden.

- **Kleinere Modelle verwenden** - Kleine Sprachmodelle (SLMs) können bei bestimmten agentischen Anwendungsfällen gut abschneiden und die Kosten erheblich senken. Wie bereits erwähnt, ist der Aufbau eines Bewertungssystems, um Leistung und Kosten zwischen kleineren und größeren Modellen zu vergleichen, der beste Weg, um zu verstehen, wie gut ein SLM für Ihren Anwendungsfall geeignet ist.

- **Router-Modell verwenden** - Eine ähnliche Strategie besteht darin, eine Vielfalt von Modellen und Größen zu nutzen. Sie können ein LLM/SLM oder eine serverlose Funktion verwenden, um Anfragen basierend auf deren Komplexität an die am besten geeigneten Modelle weiterzuleiten. Dies hilft, Kosten zu senken und gleichzeitig sicherzustellen, dass die Leistung bei den richtigen Aufgaben erhalten bleibt.

## Herzlichen Glückwunsch  

Dies ist derzeit die letzte Lektion von "KI-Agenten für Anfänger".

Wir planen, basierend auf Feedback und Veränderungen in dieser stetig wachsenden Branche, weitere Lektionen hinzuzufügen. Schauen Sie also bald wieder vorbei.

Wenn Sie Ihr Lernen und Arbeiten mit KI-Agenten fortsetzen möchten, treten Sie dem [Azure AI Community Discord](https://discord.gg/kzRShWzttr) bei.

Dort veranstalten wir Workshops, Community-Roundtables und "Ask Me Anything"-Sitzungen.

Wir haben außerdem eine Learn-Sammlung mit weiteren Materialien, die Ihnen helfen können, KI-Agenten in der Produktion zu entwickeln.
```

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.