# Agentic RAG

Diese Lektion bietet einen umfassenden Überblick über Agentic Retrieval-Augmented Generation (Agentic RAG), ein aufstrebendes KI-Paradigma, bei dem große Sprachmodelle (LMs) eigenständig ihre nächsten Schritte planen, während sie Informationen aus externen Quellen abrufen. Im Gegensatz zu statischen Mustern des Abrufens und Lesens umfasst Agentic RAG iterative Aufrufe an das LLM, unterbrochen durch Werkzeug- oder Funktionsaufrufe und strukturierte Ausgaben. Das System bewertet Ergebnisse, verfeinert Abfragen, ruft bei Bedarf zusätzliche Werkzeuge auf und setzt diesen Zyklus fort, bis eine zufriedenstellende Lösung erreicht ist.

## Einführung

Diese Lektion umfasst:

- **Agentic RAG verstehen:** Einblick in das aufkommende Paradigma in der KI, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen und Informationen aus externen Datenquellen abrufen.
- **Iterativer Maker-Checker-Ansatz:** Verständnis des iterativen Zyklus von LLM-Aufrufen, unterbrochen durch Werkzeug- oder Funktionsaufrufe und strukturierte Ausgaben, um die Korrektheit zu verbessern und fehlerhafte Abfragen zu behandeln.
- **Praktische Anwendungen erkunden:** Identifikation von Szenarien, in denen Agentic RAG besonders effektiv ist, wie z. B. in korrektheitsorientierten Umgebungen, bei komplexen Datenbankinteraktionen und in erweiterten Workflows.

## Lernziele

Nach Abschluss dieser Lektion wirst du wissen/verstehen, wie man:

- **Agentic RAG versteht:** Einblick in das aufkommende Paradigma in der KI, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen und Informationen aus externen Datenquellen abrufen.
- **Iterativer Maker-Checker-Ansatz:** Verstehen des Konzepts eines iterativen Zyklus von LLM-Aufrufen, unterbrochen durch Werkzeug- oder Funktionsaufrufe und strukturierte Ausgaben, um die Korrektheit zu verbessern und fehlerhafte Abfragen zu behandeln.
- **Den Denkprozess übernehmen:** Das System versteht, wie es seinen Denkprozess eigenständig steuert und Entscheidungen darüber trifft, wie es Probleme angeht, ohne auf vordefinierte Pfade angewiesen zu sein.
- **Workflow:** Verstehen, wie ein agentisches Modell eigenständig Markttrendberichte abruft, Wettbewerbsdaten identifiziert, interne Verkaufsmetriken korreliert, Erkenntnisse synthetisiert und die Strategie evaluiert.
- **Iterative Schleifen, Werkzeugintegration und Gedächtnis:** Lernen, wie das System auf einem iterativen Interaktionsmuster basiert, den Zustand und das Gedächtnis über die Schritte hinweg beibehält, um wiederholte Schleifen zu vermeiden und fundierte Entscheidungen zu treffen.
- **Umgang mit Fehlern und Selbstkorrektur:** Erforschung der robusten Selbstkorrekturmechanismen des Systems, einschließlich Iteration und erneuter Abfrage, Nutzung von Diagnosetools und Rückgriff auf menschliche Aufsicht.
- **Grenzen der Eigenständigkeit:** Verständnis der Einschränkungen von Agentic RAG mit Schwerpunkt auf domänenspezifischer Autonomie, Abhängigkeit von Infrastruktur und Einhaltung von Richtlinien.
- **Praktische Anwendungsfälle und Nutzen:** Identifikation von Szenarien, in denen Agentic RAG besonders effektiv ist, wie z. B. in korrektheitsorientierten Umgebungen, bei komplexen Datenbankinteraktionen und in erweiterten Workflows.
- **Governance, Transparenz und Vertrauen:** Lernen, wie wichtig Governance und Transparenz sind, einschließlich erklärbarer Argumentation, Kontrolle von Verzerrungen und menschlicher Aufsicht.

## Was ist Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) ist ein aufstrebendes KI-Paradigma, bei dem große Sprachmodelle (LLMs) eigenständig ihre nächsten Schritte planen, während sie Informationen aus externen Quellen abrufen. Im Gegensatz zu statischen Mustern des Abrufens und Lesens umfasst Agentic RAG iterative Aufrufe an das LLM, unterbrochen durch Werkzeug- oder Funktionsaufrufe und strukturierte Ausgaben. Das System bewertet Ergebnisse, verfeinert Abfragen, ruft bei Bedarf zusätzliche Werkzeuge auf und setzt diesen Zyklus fort, bis eine zufriedenstellende Lösung erreicht ist. Dieser iterative "Maker-Checker"-Ansatz verbessert die Korrektheit, behandelt fehlerhafte Abfragen und sorgt für qualitativ hochwertige Ergebnisse.

Das System übernimmt aktiv seinen Denkprozess, indem es fehlgeschlagene Abfragen neu schreibt, verschiedene Abrufmethoden wählt und mehrere Werkzeuge integriert—wie etwa Vektorsuche in Azure AI Search, SQL-Datenbanken oder benutzerdefinierte APIs—bevor es seine Antwort finalisiert. Das unterscheidende Merkmal eines agentischen Systems ist seine Fähigkeit, seinen Denkprozess eigenständig zu steuern. Traditionelle RAG-Implementierungen verlassen sich auf vordefinierte Pfade, während ein agentisches System die Abfolge der Schritte autonom auf Basis der Qualität der gefundenen Informationen bestimmt.

## Definition von Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) ist ein aufstrebendes Paradigma in der KI-Entwicklung, bei dem LLMs nicht nur Informationen aus externen Datenquellen abrufen, sondern auch eigenständig ihre nächsten Schritte planen. Im Gegensatz zu statischen Abruf-Lese-Mustern oder sorgfältig geskripteten Prompt-Sequenzen umfasst Agentic RAG einen iterativen Zyklus von LLM-Aufrufen, unterbrochen durch Werkzeug- oder Funktionsaufrufe und strukturierte Ausgaben. Das System bewertet bei jedem Schritt die erzielten Ergebnisse, entscheidet, ob es seine Abfragen verfeinern muss, ruft bei Bedarf zusätzliche Werkzeuge auf und setzt diesen Zyklus fort, bis es eine zufriedenstellende Lösung erreicht.

Dieser iterative "Maker-Checker"-Ansatz ist darauf ausgelegt, die Korrektheit zu verbessern, fehlerhafte Abfragen an strukturierte Datenbanken (z. B. NL2SQL) zu behandeln und ausgewogene, qualitativ hochwertige Ergebnisse sicherzustellen. Anstatt sich ausschließlich auf sorgfältig entwickelte Prompt-Ketten zu verlassen, übernimmt das System aktiv seinen Denkprozess. Es kann fehlgeschlagene Abfragen neu schreiben, verschiedene Abrufmethoden wählen und mehrere Werkzeuge integrieren—wie etwa Vektorsuche in Azure AI Search, SQL-Datenbanken oder benutzerdefinierte APIs—bevor es seine Antwort finalisiert. Dies macht komplexe Orchestrierungsrahmen überflüssig. Stattdessen kann eine relativ einfache Schleife aus „LLM-Aufruf → Werkzeugnutzung → LLM-Aufruf → …“ zu ausgefeilten und fundierten Ergebnissen führen.

![Agentic RAG Core Loop](../../../05-agentic-rag/images/agentic-rag-core-loop.png)

## Den Denkprozess übernehmen

Das unterscheidende Merkmal, das ein System "agentisch" macht, ist seine Fähigkeit, seinen Denkprozess eigenständig zu steuern. Traditionelle RAG-Implementierungen hängen oft davon ab, dass Menschen einen Pfad für das Modell vordefinieren: eine Denkweise, die festlegt, was wann abgerufen werden soll. Ein wirklich agentisches System hingegen entscheidet intern, wie es das Problem angeht. Es führt nicht einfach ein Skript aus, sondern bestimmt autonom die Abfolge der Schritte auf Basis der Qualität der gefundenen Informationen.

Zum Beispiel: Wenn das System aufgefordert wird, eine Produktstartstrategie zu erstellen, verlässt es sich nicht nur auf einen Prompt, der den gesamten Forschungs- und Entscheidungsworkflow vorgibt. Stattdessen entscheidet das agentische Modell eigenständig:

1. Aktuelle Markttrendberichte mit Bing Web Grounding abzurufen.
2. Relevante Wettbewerbsdaten mit Azure AI Search zu identifizieren.
3. Historische interne Verkaufsmetriken mit Azure SQL Database zu korrelieren.
4. Die Erkenntnisse zu einer kohärenten Strategie zu synthetisieren, orchestriert über Azure OpenAI Service.
5. Die Strategie auf Lücken oder Inkonsistenzen zu überprüfen und gegebenenfalls eine weitere Abrufrunde einzuleiten.

All diese Schritte—Abfragen verfeinern, Quellen auswählen, iterieren, bis eine zufriedenstellende Antwort erreicht ist—werden vom Modell entschieden, nicht von einem Menschen vorgegeben.

## Iterative Schleifen, Werkzeugintegration und Gedächtnis

![Tool Integration Architecture](../../../05-agentic-rag/images/tool-integration.png)

Ein agentisches System basiert auf einem iterativen Interaktionsmuster:

- **Erster Aufruf:** Das Ziel des Nutzers (auch User Prompt genannt) wird dem LLM präsentiert.
- **Werkzeugaufruf:** Wenn das Modell feststellt, dass Informationen fehlen oder Anweisungen unklar sind, wählt es ein Werkzeug oder eine Abrufmethode—wie eine Abfrage an eine Vektordatenbank (z. B. Azure AI Search Hybrid Search über private Daten) oder einen strukturierten SQL-Aufruf—um mehr Kontext zu sammeln.
- **Bewertung & Verfeinerung:** Nach Überprüfung der zurückgegebenen Daten entscheidet das Modell, ob die Informationen ausreichen. Falls nicht, verfeinert es die Abfrage, versucht ein anderes Werkzeug oder passt seinen Ansatz an.
- **Wiederholen, bis zufriedenstellend:** Dieser Zyklus wird fortgesetzt, bis das Modell feststellt, dass es genügend Klarheit und Beweise hat, um eine fundierte Antwort zu liefern.
- **Gedächtnis & Zustand:** Da das System den Zustand und das Gedächtnis über die Schritte hinweg beibehält, kann es sich an vorherige Versuche und deren Ergebnisse erinnern, wiederholte Schleifen vermeiden und fundiertere Entscheidungen treffen, während es voranschreitet.

Im Laufe der Zeit entsteht so ein Gefühl des fortschreitenden Verständnisses, das es dem Modell ermöglicht, komplexe, mehrstufige Aufgaben zu bewältigen, ohne dass ein Mensch ständig eingreifen oder den Prompt umformen muss.

## Umgang mit Fehlern und Selbstkorrektur

Die Eigenständigkeit von Agentic RAG umfasst auch robuste Selbstkorrekturmechanismen. Wenn das System auf Sackgassen stößt—wie das Abrufen irrelevanter Dokumente oder das Auftreten fehlerhafter Abfragen—kann es:

- **Iterieren und erneut abfragen:** Anstatt minderwertige Antworten zurückzugeben, versucht das Modell neue Suchstrategien, schreibt Datenbankabfragen um oder prüft alternative Datensätze.
- **Diagnosetools nutzen:** Das System kann zusätzliche Funktionen aufrufen, die ihm helfen, seine Denkschritte zu debuggen oder die Korrektheit der abgerufenen Daten zu bestätigen. Tools wie Azure AI Tracing sind entscheidend, um eine robuste Beobachtbarkeit und Überwachung zu ermöglichen.
- **Auf menschliche Aufsicht zurückgreifen:** In hochkritischen oder wiederholt scheiternden Szenarien könnte das Modell Unsicherheit signalisieren und menschliche Anleitung anfordern. Sobald der Mensch korrigierendes Feedback gibt, kann das Modell diese Lektion für die Zukunft übernehmen.

Dieser iterative und dynamische Ansatz ermöglicht es dem Modell, sich kontinuierlich zu verbessern und sicherzustellen, dass es nicht nur ein Einweg-System ist, sondern eines, das aus seinen Fehlern innerhalb einer Sitzung lernt.

![Self Correction Mechanism](../../../05-agentic-rag/images/self-correction.png)

## Grenzen der Eigenständigkeit

Trotz seiner Eigenständigkeit innerhalb einer Aufgabe ist Agentic RAG nicht mit einer allgemeinen künstlichen Intelligenz (Artificial General Intelligence) gleichzusetzen. Seine "agentischen" Fähigkeiten sind auf die von menschlichen Entwicklern bereitgestellten Werkzeuge, Datenquellen und Richtlinien beschränkt. Es kann keine eigenen Werkzeuge erfinden oder über die gesetzten Domänengrenzen hinausgehen. Stattdessen glänzt es darin, die vorhandenen Ressourcen dynamisch zu orchestrieren.

Wichtige Unterschiede zu fortgeschritteneren KI-Formen umfassen:

1. **Domänenspezifische Autonomie:** Agentic RAG-Systeme konzentrieren sich darauf, benutzerdefinierte Ziele innerhalb einer bekannten Domäne zu erreichen, indem sie Strategien wie Abfrageumformung oder Werkzeugauswahl anwenden, um Ergebnisse zu verbessern.
2. **Infrastrukturabhängigkeit:** Die Fähigkeiten des Systems hängen von den von Entwicklern integrierten Werkzeugen und Daten ab. Es kann diese Grenzen ohne menschliches Eingreifen nicht überschreiten.
3. **Einhaltung von Richtlinien:** Ethische Richtlinien, Compliance-Regeln und Geschäftspolitiken bleiben von großer Bedeutung. Die Freiheit des Agenten ist immer durch Sicherheitsmaßnahmen und Überwachungsmechanismen eingeschränkt (hoffentlich?).

## Praktische Anwendungsfälle und Nutzen

Agentic RAG glänzt in Szenarien, die iterative Verfeinerung und Präzision erfordern:

1. **Korrektheitsorientierte Umgebungen:** In Bereichen wie Compliance-Prüfungen, regulatorischer Analyse oder juristischer Recherche kann das agentische Modell Fakten wiederholt überprüfen, mehrere Quellen konsultieren und Abfragen umschreiben, bis es eine gründlich geprüfte Antwort liefert.
2. **Komplexe Datenbankinteraktionen:** Bei der Arbeit mit strukturierten Daten, bei denen Abfragen häufig scheitern oder angepasst werden müssen, kann das System eigenständig seine Abfragen mithilfe von Azure SQL oder Microsoft Fabric OneLake verfeinern, um sicherzustellen, dass die endgültige Abfrage mit der Benutzerabsicht übereinstimmt.
3. **Erweiterte Workflows:** Länger laufende Sitzungen können sich weiterentwickeln, wenn neue Informationen auftauchen. Agentic RAG kann kontinuierlich neue Daten integrieren und Strategien anpassen, während es mehr über den Problemraum lernt.

## Governance, Transparenz und Vertrauen

Da diese Systeme eigenständiger in ihrer Argumentation werden, sind Governance und Transparenz von entscheidender Bedeutung:

- **Erklärbare Argumentation:** Das Modell kann eine Prüfspur der getätigten Abfragen, der konsultierten Quellen und der Argumentationsschritte bereitstellen, die zu seiner Schlussfolgerung geführt haben. Tools wie Azure AI Content Safety und Azure AI Tracing / GenAIOps können helfen, Transparenz zu gewährleisten und Risiken zu minimieren.
- **Kontrolle von Verzerrungen und ausgewogene Abrufe:** Entwickler können Abrufstrategien anpassen, um sicherzustellen, dass ausgewogene, repräsentative Datenquellen berücksichtigt werden, und regelmäßig Ausgaben überprüfen, um Verzerrungen oder unausgewogene Muster zu erkennen, unter Verwendung benutzerdefinierter Modelle für fortgeschrittene Datenwissenschaftsorganisationen mit Azure Machine Learning.
- **Menschliche Aufsicht und Compliance:** Für sensible Aufgaben bleibt die menschliche Überprüfung unerlässlich. Agentic RAG ersetzt nicht das menschliche Urteilsvermögen bei kritischen Entscheidungen—es ergänzt es, indem es gründlicher geprüfte Optionen liefert.

Werkzeuge, die einen klaren Aktionsverlauf aufzeichnen, sind unerlässlich. Ohne sie kann das Debuggen eines mehrstufigen Prozesses sehr schwierig sein. Siehe folgendes Beispiel von Literal AI (Unternehmen hinter Chainlit) für einen Agent-Lauf:

![AgentRunExample](../../../05-agentic-rag/images/AgentRunExample.png)

![AgentRunExample2](../../../05-agentic-rag/images/AgentRunExample2.png)

## Fazit

Agentic RAG stellt eine natürliche Weiterentwicklung in der Art und Weise dar, wie KI-Systeme komplexe, datenintensive Aufgaben bewältigen. Durch die Einführung eines iterativen Interaktionsmusters, die autonome Auswahl von Werkzeugen und die Verfeinerung von Abfragen, bis ein qualitativ hochwertiges Ergebnis erzielt wird, geht das System über statisches Prompt-Following hinaus und wird zu einem anpassungsfähigen, kontextbewussten Entscheidungsträger. Obwohl es weiterhin durch menschlich definierte Infrastrukturen und ethische Richtlinien begrenzt ist, ermöglichen diese agentischen Fähigkeiten reichhaltigere, dynamischere und letztlich nützlichere KI-Interaktionen sowohl für Unternehmen als auch für Endbenutzer.

## Zusätzliche Ressourcen

- Implementierung von Retrieval Augmented Generation (RAG) mit Azure OpenAI Service: Erfahre, wie du deine eigenen Daten mit dem Azure OpenAI Service nutzen kannst. [Dieses Microsoft Learn-Modul bietet eine umfassende Anleitung zur Implementierung von RAG](https://learn.microsoft.com/training/modules/use-own-data-azure-openai)
- Evaluation generativer KI-Anwendungen mit Azure AI Foundry: Dieser Artikel behandelt die Bewertung und den Vergleich von Modellen anhand öffentlich verfügbarer Datensätze, einschließlich [Agentic AI-Anwendungen und RAG-Architekturen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [Was ist Agentic RAG | Weaviate](https://weaviate.io/blog/what-is-agentic-rag)
- [Agentic RAG: Ein vollständiger Leitfaden zu Agent-Based Retrieval Augmented Generation – News von Generation RAG](https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/)
- [Agentic RAG: Steigere dein RAG mit Abfrageumformung und Selbstabfrage! Hugging Face Open-Source AI Cookbook](https://huggingface.co/learn/cookbook/agent_rag)
- [Agentische Ebenen zu RAG hinzufügen](https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U)
- [Die Zukunft von Wissensassistenten: Jerry Liu](https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s)
- [Wie man Agentic RAG-Systeme baut](https://www.youtube.com/watch?v=AOSjiXP1jmQ)
- [Verwendung des Azure AI Foundry Agent Service zur Skalierung deiner KI-Agenten](https://ignite.microsoft.com/en-US/sessions/BRK102?source=sessions)

### Wissenschaftliche Arbeiten

- [2303.17651 Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- [2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- [2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)
```

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.