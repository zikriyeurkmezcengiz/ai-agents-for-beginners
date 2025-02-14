```markdown
# Kurseinrichtung

## Einführung

In dieser Lektion wird erklärt, wie die Codebeispiele dieses Kurses ausgeführt werden können.

## Anforderungen

- Ein GitHub-Konto
- Python 3.12+

## Dieses Repository klonen oder forken

Um zu beginnen, klonen oder forken Sie bitte das GitHub-Repository. Dadurch erstellen Sie Ihre eigene Version des Kursmaterials, sodass Sie den Code ausführen, testen und anpassen können!

Dies können Sie tun, indem Sie auf den Link [fork the repo](https://github.com/microsoft/ai-agents-for-beginners/fork) klicken.

Sie sollten nun Ihre eigene geforkte Version dieses Kurses haben, wie unten gezeigt:

![Geforktes Repository](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.de.png)

## Abrufen Ihres GitHub Personal Access Token (PAT)

Dieser Kurs verwendet derzeit den GitHub Models Marketplace, um kostenlosen Zugriff auf Large Language Models (LLMs) bereitzustellen, die zur Erstellung von KI-Agenten verwendet werden.

Um auf diesen Service zuzugreifen, müssen Sie ein GitHub Personal Access Token erstellen.

Dies können Sie tun, indem Sie zu Ihren [Personal Access Tokens settings](https://github.com/settings/personal-access-tokens) in Ihrem GitHub-Konto gehen.

Wählen Sie die `Fine-grained tokens`-Optionen auf der linken Seite Ihres Bildschirms.

Wählen Sie anschließend `Generate new token`.

![Token generieren](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.de.png)

Kopieren Sie Ihren neu erstellten Token. Sie werden diesen nun in Ihre `.env`-Datei einfügen, die in diesem Kurs enthalten ist. 

## Hinzufügen zu Ihren Umgebungsvariablen

Um Ihre `.env`-Datei zu erstellen, führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
cp .env.example .env
```

Dieser Befehl kopiert die Beispieldatei und erstellt eine `.env`-Datei in Ihrem Verzeichnis.

Öffnen Sie diese Datei und fügen Sie den erstellten Token in das Feld `GITHUB_TOKEN=` der .env-Datei ein. 

## Erforderliche Pakete installieren

Um sicherzustellen, dass Sie alle erforderlichen Python-Pakete für die Ausführung des Codes haben, führen Sie den folgenden Befehl in Ihrem Terminal aus.

Wir empfehlen, eine Python-virtuelle Umgebung zu erstellen, um Konflikte und Probleme zu vermeiden.

```bash
pip install -r requirements.txt
```

Dies sollte die benötigten Python-Pakete installieren.

Sie sind nun bereit, den Code dieses Kurses auszuführen. Viel Spaß beim Erforschen der Welt der KI-Agenten!

Falls Sie Probleme bei der Einrichtung haben, treten Sie unserem [Azure AI Community Discord](https://discord.gg/kzRShWzttr) bei oder [erstellen Sie ein Issue](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst).
```

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.