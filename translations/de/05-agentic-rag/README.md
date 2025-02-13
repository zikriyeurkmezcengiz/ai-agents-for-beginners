```markdown
# Agentic RAG

Diese Lektion bietet einen umfassenden Überblick über Agentic Retrieval-Augmented Generation (Agentic RAG), ein aufkommendes KI-Paradigma, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen, während sie Informationen aus externen Quellen abrufen. Im Gegensatz zu statischen Mustern des Abrufens und Lesens umfasst Agentic RAG iterative Aufrufe des LLM, die durch Tool- oder Funktionsaufrufe und strukturierte Ausgaben unterbrochen werden. Das System bewertet die Ergebnisse, verfeinert Anfragen, ruft bei Bedarf zusätzliche Tools auf und setzt diesen Zyklus fort, bis eine zufriedenstellende Lösung erreicht ist.

## Einführung

Diese Lektion behandelt:

- **Verständnis von Agentic RAG:** Erfahren Sie mehr über das aufkommende Paradigma in der KI, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen, während sie Informationen aus externen Datenquellen abrufen.
- **Iterativer Maker-Checker-Stil:** Verstehen Sie die Schleife iterativer Aufrufe des LLM, die durch Tool- oder Funktionsaufrufe und strukturierte Ausgaben ergänzt werden, um die Korrektheit zu verbessern und fehlerhafte Anfragen zu behandeln.
- **Praktische Anwendungen erkunden:** Identifizieren Sie Szenarien, in denen Agentic RAG besonders effektiv ist, wie z. B. in Umgebungen mit Fokus auf Korrektheit, bei komplexen Datenbankinteraktionen und in erweiterten Workflows.

## Lernziele

Nach Abschluss dieser Lektion werden Sie in der Lage sein:

- **Agentic RAG verstehen:** Lernen Sie das aufkommende Paradigma in der KI kennen, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen und Informationen aus externen Datenquellen abrufen.
- **Iterativer Maker-Checker-Stil:** Verstehen Sie das Konzept einer Schleife aus iterativen Aufrufen des LLM, ergänzt durch Tool- oder Funktionsaufrufe und strukturierte Ausgaben, die darauf abzielen, die Korrektheit zu verbessern und fehlerhafte Anfragen zu behandeln.
- **Den Denkprozess übernehmen:** Verstehen Sie, wie das System seinen Denkprozess selbstständig steuert und Entscheidungen darüber trifft, wie Probleme angegangen werden sollen, ohne auf vorab definierte Pfade angewiesen zu sein.
- **Workflow:** Erfahren Sie, wie ein agentisches Modell eigenständig Markttrendberichte abruft, Wettbewerbsdaten identifiziert, interne Verkaufsmetriken korreliert, Erkenntnisse synthetisiert und die Strategie bewertet.
- **Iterative Schleifen, Tool-Integration und Speicher:** Lernen Sie, wie das System auf einem Schleifeninteraktionsmuster basiert, den Zustand und Speicher über die Schritte hinweg beibehält, um Wiederholungen zu vermeiden und fundierte Entscheidungen zu treffen.
- **Umgang mit Fehlern und Selbstkorrektur:** Erkunden Sie die robusten Selbstkorrekturmechanismen des Systems, einschließlich Iteration und erneuter Abfragen, der Verwendung von Diagnosetools und der Rückfalloption auf menschliche Aufsicht.
- **Grenzen der Eigenständigkeit:** Verstehen Sie die Einschränkungen von Agentic RAG, mit einem Fokus auf domänenspezifische Autonomie, Abhängigkeit von Infrastruktur und Einhaltung von Sicherheitsvorkehrungen.
- **Praktische Anwendungsfälle und Nutzen:** Identifizieren Sie Szenarien, in denen Agentic RAG besonders effektiv ist, wie z. B. in Umgebungen mit Fokus auf Korrektheit, bei komplexen Datenbankinteraktionen und in erweiterten Workflows.
- **Governance, Transparenz und Vertrauen:** Lernen Sie die Bedeutung von Governance und Transparenz kennen, einschließlich nachvollziehbarer Argumentationen, Kontrolle von Vorurteilen und menschlicher Aufsicht.

## Was ist Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) ist ein aufkommendes KI-Paradigma, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen, während sie Informationen aus externen Quellen abrufen. Im Gegensatz zu statischen Mustern des Abrufens und Lesens umfasst Agentic RAG iterative Aufrufe des LLM, die durch Tool- oder Funktionsaufrufe und strukturierte Ausgaben unterbrochen werden. Das System bewertet die Ergebnisse, verfeinert Anfragen, ruft bei Bedarf zusätzliche Tools auf und setzt diesen Zyklus fort, bis eine zufriedenstellende Lösung erreicht ist. Dieser iterative „Maker-Checker“-Stil verbessert die Korrektheit, behandelt fehlerhafte Anfragen und gewährleistet qualitativ hochwertige Ergebnisse.

Das System übernimmt aktiv die Verantwortung für seinen Denkprozess, indem es fehlgeschlagene Anfragen umschreibt, unterschiedliche Abrufmethoden auswählt und mehrere Tools integriert – wie z. B. Vektorsuche in Azure AI Search, SQL-Datenbanken oder benutzerdefinierte APIs – bevor es seine Antwort abschließt. Die herausragende Eigenschaft eines agentischen Systems ist seine Fähigkeit, seinen Denkprozess eigenständig zu steuern. Traditionelle RAG-Implementierungen verlassen sich auf vorab definierte Pfade, während ein agentisches System die Abfolge der Schritte basierend auf der Qualität der gefundenen Informationen eigenständig bestimmt.

## Definition von Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) ist ein aufkommendes Paradigma in der KI-Entwicklung, bei dem LLMs nicht nur Informationen aus externen Datenquellen abrufen, sondern auch eigenständig ihre nächsten Schritte planen. Im Gegensatz zu statischen Mustern des Abrufens und Lesens oder sorgfältig geskripteten Prompt-Sequenzen umfasst Agentic RAG eine Schleife aus iterativen Aufrufen des LLM, ergänzt durch Tool- oder Funktionsaufrufe und strukturierte Ausgaben. In jeder Phase bewertet das System die erzielten Ergebnisse, entscheidet, ob es seine Anfragen verfeinern soll, ruft bei Bedarf zusätzliche Tools auf und setzt diesen Zyklus fort, bis es eine zufriedenstellende Lösung erreicht hat.

Dieser iterative „Maker-Checker“-Stil zielt darauf ab, die Korrektheit zu verbessern, fehlerhafte Anfragen an strukturierte Datenbanken (z. B. NL2SQL) zu behandeln und ausgewogene, qualitativ hochwertige Ergebnisse zu gewährleisten. Anstatt sich ausschließlich auf sorgfältig gestaltete Prompt-Ketten zu verlassen, übernimmt das System aktiv die Verantwortung für seinen Denkprozess. Es kann fehlerhafte Anfragen umschreiben, unterschiedliche Abrufmethoden auswählen und mehrere Tools integrieren – wie z. B. Vektorsuche in Azure AI Search, SQL-Datenbanken oder benutzerdefinierte APIs – bevor es seine Antwort abschließt. Dies reduziert die Notwendigkeit für übermäßig komplexe Orchestrierungsframeworks. Stattdessen kann eine relativ einfache Schleife aus „LLM-Aufruf → Tool-Nutzung → LLM-Aufruf → …“ zu ausgefeilten und fundierten Ergebnissen führen.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.2224925a913fb3439f518bda61a40096ddf6aa432a11c9b5bba8d0d625e47b79.de.png)

## Verantwortung für den Denkprozess übernehmen

Die herausragende Eigenschaft, die ein System „agentisch“ macht, ist seine Fähigkeit, die Verantwortung für seinen Denkprozess zu übernehmen. Traditionelle RAG-Implementierungen hängen oft davon ab, dass Menschen einen Pfad für das Modell vorab definieren: eine Gedankenkette, die beschreibt, was abgerufen werden soll und wann. Ein wirklich agentisches System entscheidet jedoch intern, wie es das Problem angehen möchte. Es führt nicht einfach ein Skript aus, sondern bestimmt eigenständig die Abfolge der Schritte basierend auf der Qualität der gefundenen Informationen.

Zum Beispiel: Wenn es darum gebeten wird, eine Produktstartstrategie zu erstellen, verlässt es sich nicht ausschließlich auf einen Prompt, der den gesamten Recherche- und Entscheidungsworkflow vorgibt. Stattdessen entscheidet das agentische Modell eigenständig:

1. Aktuelle Markttrendberichte mithilfe von Bing Web Grounding abzurufen.
2. Relevante Wettbewerbsdaten mit Azure AI Search zu identifizieren.
3. Historische interne Verkaufsmetriken mit Azure SQL Database zu korrelieren.
4. Die Ergebnisse zu einer kohärenten Strategie zusammenzuführen, orchestriert über den Azure OpenAI Service.
5. Die Strategie auf Lücken oder Inkonsistenzen zu prüfen, was möglicherweise eine weitere Runde von Abrufen auslöst.

All diese Schritte – Anfragen verfeinern, Quellen auswählen, iterieren, bis die Antwort „passt“ – werden vom Modell entschieden, nicht von einem Menschen vorgegeben.

## Iterative Schleifen, Tool-Integration und Speicher

![Tool Intergration Architecture](../../../translated_images/tool-integration.7b05a923e3278bf1fd2972faa228fb2ac725f166ed084362b031a24bffd26287.de.png)

Ein agentisches System basiert auf einem Schleifeninteraktionsmuster:

- **Erster Aufruf:** Das Ziel des Nutzers (d. h. der Nutzer-Prompt) wird dem LLM präsentiert.
- **Tool-Aufruf:** Wenn das Modell fehlende Informationen oder unklare Anweisungen erkennt, wählt es ein Tool oder eine Abrufmethode aus – wie eine Abfrage in einer Vektordatenbank (z. B. Azure AI Search Hybrid Search über private Daten) oder einen strukturierten SQL-Aufruf –, um mehr Kontext zu sammeln.
- **Bewertung & Verfeinerung:** Nach der Überprüfung der zurückgegebenen Daten entscheidet das Modell, ob die Informationen ausreichen. Falls nicht, verfeinert es die Anfrage, versucht ein anderes Tool oder passt seinen Ansatz an.
- **Wiederholen, bis zufrieden:** Dieser Zyklus wird fortgesetzt, bis das Modell entscheidet, dass es genügend Klarheit und Beweise hat, um eine abschließende, gut begründete Antwort zu liefern.
- **Speicher & Zustand:** Da das System Zustand und Speicher über die Schritte hinweg beibehält, kann es sich an frühere Versuche und deren Ergebnisse erinnern, Wiederholungen vermeiden und fundiertere Entscheidungen treffen, während es fortschreitet.

Mit der Zeit entsteht so ein Gefühl des fortschreitenden Verständnisses, das es dem Modell ermöglicht, komplexe, mehrstufige Aufgaben zu bewältigen, ohne dass ein Mensch ständig eingreifen oder den Prompt anpassen muss.

## Umgang mit Fehlern und Selbstkorrektur

Die Eigenständigkeit von Agentic RAG umfasst auch robuste Selbstkorrekturmechanismen. Wenn das System auf Sackgassen stößt – wie das Abrufen irrelevanter Dokumente oder das Auftreten fehlerhafter Anfragen –, kann es:

- **Iterieren und erneut abfragen:** Anstatt minderwertige Antworten zurückzugeben, versucht das Modell neue Suchstrategien, schreibt Datenbankabfragen um oder betrachtet alternative Datensätze.
- **Diagnosetools verwenden:** Das System kann zusätzliche Funktionen aufrufen, die ihm helfen, seine Denkschritte zu debuggen oder die Korrektheit der abgerufenen Daten zu bestätigen. Tools wie Azure AI Tracing sind wichtig, um robuste Beobachtbarkeit und Überwachung zu ermöglichen.
- **Auf menschliche Aufsicht zurückgreifen:** In risikoreichen oder wiederholt scheiternden Szenarien könnte das Modell Unsicherheiten kennzeichnen und um menschliche Anleitung bitten. Sobald der Mensch korrigierendes Feedback gibt, kann das Modell diese Lektion in Zukunft nutzen.

Dieser iterative und dynamische Ansatz ermöglicht es dem Modell, sich kontinuierlich zu verbessern und sicherzustellen, dass es nicht nur ein einmaliges System ist, sondern eines, das aus seinen Fehltritten während einer Sitzung lernt.

![Self Correction Mechanism](../../../translated_images/self-correction.3d42c31baf4a476bb89313cec58efb196b0e97959c04d7439cc23d27ef1242ac.de.png)

## Grenzen der Eigenständigkeit

Trotz seiner Autonomie innerhalb einer Aufgabe ist Agentic RAG nicht mit einer allgemeinen künstlichen Intelligenz gleichzusetzen. Seine „agentischen“ Fähigkeiten sind auf die von menschlichen Entwicklern bereitgestellten Tools, Datenquellen und Richtlinien beschränkt. Es kann keine eigenen Tools erfinden oder die gesetzten Domänengrenzen überschreiten. Stattdessen zeichnet es sich durch die dynamische Orchestrierung der verfügbaren Ressourcen aus.

Wichtige Unterschiede zu fortschrittlicheren KI-Formen sind:

1. **Domänenspezifische Autonomie:** Agentic RAG-Systeme konzentrieren sich darauf, benutzerdefinierte Ziele innerhalb eines bekannten Bereichs zu erreichen, indem sie Strategien wie das Umschreiben von Abfragen oder die Auswahl von Tools anwenden, um die Ergebnisse zu verbessern.
2. **Infrastrukturabhängig:** Die Fähigkeiten des Systems hängen von den von Entwicklern integrierten Tools und Daten ab. Es kann diese Grenzen ohne menschliches Eingreifen nicht überschreiten.
3. **Einhaltung von Sicherheitsvorkehrungen:** Ethische Richtlinien, Compliance-Regeln und Geschäftspolitiken bleiben von großer Bedeutung. Die Freiheit des Agenten ist immer durch Sicherheitsmaßnahmen und Überwachungsmechanismen eingeschränkt (hoffentlich?).

## Praktische Anwendungsfälle und Nutzen

Agentic RAG zeigt seine Stärken in Szenarien, die iterative Verfeinerung und Präzision erfordern:

1. **Umgebungen mit Fokus auf Korrektheit:** In Compliance-Prüfungen, regulatorischen Analysen oder juristischen Recherchen kann das agentische Modell wiederholt Fakten überprüfen, mehrere Quellen konsultieren und Anfragen umschreiben, bis es eine gründlich geprüfte Antwort liefert.

2. **Komplexe Datenbankinteraktionen:** Bei der Arbeit mit strukturierten Daten, bei denen Abfragen oft fehlschlagen oder angepasst werden müssen, kann das System eigenständig seine Abfragen mit Azure SQL oder Microsoft Fabric OneLake verfeinern und sicherstellen, dass die endgültigen Abrufe der Absicht des Nutzers entsprechen.

3. **Erweiterte Workflows:** Länger laufende Sitzungen können sich entwickeln, wenn neue Informationen verfügbar werden. Agentic RAG kann kontinuierlich neue Daten einbeziehen und Strategien anpassen, während es mehr über den Problemraum lernt.

## Governance, Transparenz und Vertrauen

Da diese Systeme in ihrem Denkprozess immer eigenständiger werden, sind Governance und Transparenz entscheidend:

- **Nachvollziehbare Argumentation:** Das Modell kann eine Prüfspur der von ihm durchgeführten Abfragen, der konsultierten Quellen und der Schritte, die es zu seinen Schlussfolgerungen geführt haben, bereitstellen. Tools wie Azure AI Content Safety und Azure AI Tracing / GenAIOps können helfen, Transparenz zu gewährleisten und Risiken zu mindern.
- **Kontrolle von Vorurteilen und ausgewogener Abruf:** Entwickler können Abrufstrategien anpassen, um sicherzustellen, dass ausgewogene, repräsentative Datenquellen berücksichtigt werden, und regelmäßig Ausgaben überprüfen, um Vorurteile oder verzerrte Muster zu erkennen, beispielsweise mit benutzerdefinierten Modellen für fortgeschrittene Datenwissenschaftsorganisationen, die Azure Machine Learning verwenden.
- **Menschliche Aufsicht und Compliance:** Für sensible Aufgaben bleibt die menschliche Überprüfung unerlässlich. Agentic RAG ersetzt nicht das menschliche Urteilsvermögen bei Entscheidungen mit hohen Einsätzen – es ergänzt es, indem es gründlicher geprüfte Optionen liefert.

Tools, die eine klare Aufzeichnung der Aktionen bereitstellen, sind unerlässlich. Ohne sie kann das Debuggen eines mehrstufigen Prozesses sehr schwierig sein. Siehe unten ein Beispiel von Literal AI (Unternehmen hinter Chainlit) für einen Agentenlauf:

![AgentRunExample](../../../translated_images/AgentRunExample.27e2df23ad898772d1b3e7a3e3cd4615378e10dfda87ae8f06b4748bf8eea97d.de.png)

![AgentRunExample2](../../../translated_images/AgentRunExample2.c0e8c78b1f2540a641515e60035abcc6a9c5e3688bae143eb6c559dd37cdee9f.de.png)

## Fazit

Agentic RAG stellt eine natürliche Weiterentwicklung dar, wie KI-Systeme komplexe, datenintensive Aufgaben bewältigen. Durch die Übernahme eines Schleifeninteraktionsmusters, die eigenständige Auswahl von Tools und die Verfeinerung von Anfragen bis zur Erzielung eines qualitativ hochwertigen Ergebnisses geht das System über statisches Prompt-Following hinaus und wird zu einem anpassungsfähigeren, kontextbewussteren Entscheidungsträger. Obwohl es weiterhin durch von Menschen definierte Infrastrukturen und ethische Richtlinien begrenzt ist, ermöglichen diese agentischen Fähigkeiten reichhaltigere, dynamischere und letztendlich nützlichere KI-Interaktionen für Unternehmen und Endnutzer.

## Zusätzliche Ressourcen

- Implementierung von Retrieval Augmented Generation (RAG) mit Azure OpenAI Service: Lernen Sie, wie Sie Ihre eigenen Daten mit dem Azure OpenAI Service nutzen können. [Dieses Microsoft Learn-Modul bietet eine umfassende Anleitung zur Implementierung von RAG](https://learn.microsoft.com/training/modules/use-own-data-azure-openai)
- Bewertung generativer KI-Anwendungen mit Azure AI Foundry: Dieser Artikel behandelt die Bewertung und den Vergleich von Modellen auf öffentlich verfügbaren Datensätzen, einschließlich [Agentic AI-Anwendungen und RAG-Architekturen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [Was ist Agentic RAG | Weaviate](https://weaviate.io/blog/what-is-agentic-rag)
- [Agentic RAG: Ein vollständiger Leitfaden zu agentenbasierter Retrieval Augmented Generation – News von generation RAG](https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/)
- [Agentic RAG: turbocharge your RAG with query reformulation and self-query! Hugging Face Open-Source AI Cookbook](https://huggingface.co/learn/cookbook/agent_rag)
- [Adding Agentic Layers to RAG](https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U)
- [The Future of Knowledge Assistants: Jerry Liu](https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s)
- [How to Build Agentic RAG Systems](https://www.youtube.com/watch?v=AOSjiXP1jmQ)
- [Using Azure AI Foundry Agent Service to scale your AI agents](https://ignite.microsoft.com/en-US/sessions/BRK102?source=sessions)

### Akademische Artikel

- [2303.17651 Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- [2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- [2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)
```

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.