```markdown
# AIエージェントにおけるメタ認知

## はじめに

AIエージェントにおけるメタ認知についてのレッスンへようこそ！この章は、AIエージェントが自身の思考プロセスについてどのように考えることができるのかに興味を持つ初心者向けに設計されています。このレッスンの終わりには、重要な概念を理解し、AIエージェントの設計にメタ認知を適用するための実践的な例を学べるようになります。

## 学習目標

このレッスンを修了すると、以下のことができるようになります：

1. エージェント定義における推論ループの影響を理解する。
2. 計画および評価技術を使用して、自己修正可能なエージェントを支援する。
3. タスクを達成するためにコードを操作できるエージェントを作成する。

## メタ認知の紹介

メタ認知とは、自身の思考について考える高次の認知プロセスを指します。AIエージェントにとって、これは自己認識や過去の経験に基づいて行動を評価し調整する能力を意味します。

### メタ認知とは？

メタ認知、つまり「思考について考えること」は、自己認識と認知プロセスの自己調整を含む高次の認知プロセスです。AIの分野では、メタ認知はエージェントが戦略や行動を評価し適応させる能力を与え、問題解決能力や意思決定能力の向上につながります。メタ認知を理解することで、より知的で適応力があり効率的なAIエージェントを設計できます。

### AIエージェントにおけるメタ認知の重要性

メタ認知は、AIエージェント設計において以下の理由で重要な役割を果たします：

![メタ認知の重要性](../../../translated_images/importance-of-metacognition.e351a5983bb745d60a1a60185391a39a6751d033c8c1948ceb6ad04eff7dbeac.ja.png)

- **自己反省**：エージェントは自身のパフォーマンスを評価し、改善点を特定できます。
- **適応性**：過去の経験や変化する環境に基づいて戦略を修正できます。
- **エラー修正**：エージェントはエラーを自律的に検出し修正することで、より正確な結果を得られます。
- **リソース管理**：エージェントは時間や計算能力などのリソースを計画・評価することで最適化できます。

## AIエージェントの構成要素

メタ認知プロセスに入る前に、AIエージェントの基本的な構成要素を理解することが重要です。AIエージェントは通常、以下の要素で構成されています：

- **パーソナ**：エージェントの性格や特性で、ユーザーとのやり取り方法を定義します。
- **ツール**：エージェントが実行できる機能や能力。
- **スキル**：エージェントが持つ知識や専門性。

これらの要素が連携して、特定のタスクを実行できる「専門性ユニット」を形成します。

**例**：旅行代理店エージェントを考えてみましょう。このエージェントは、旅行計画を立てるだけでなく、リアルタイムデータや過去の顧客経験に基づいて経路を調整します。

### 例：旅行代理店サービスにおけるメタ認知

AIを活用した旅行代理店サービスを設計していると想像してください。このエージェント「Travel Agent」は、ユーザーの休暇計画を支援します。メタ認知を組み込むには、Travel Agentが自己認識や過去の経験に基づいて行動を評価し調整する必要があります。

#### 現在のタスク

現在のタスクは、ユーザーがパリ旅行を計画するのを支援することです。

#### タスクを完了するための手順

1. **ユーザーの好みを収集**：旅行日程、予算、興味（例：博物館、料理、ショッピング）、特定の要件を尋ねます。
2. **情報を取得**：ユーザーの好みに合ったフライトオプション、宿泊施設、観光地、レストランを検索します。
3. **推奨事項を生成**：フライトの詳細、ホテルの予約、提案されたアクティビティを含む個別の旅程を提供します。
4. **フィードバックに基づいて調整**：推奨事項に対するユーザーのフィードバックを求め、必要に応じて調整を行います。

#### 必要なリソース

- フライトおよびホテル予約データベースへのアクセス。
- パリの観光地やレストランに関する情報。
- 過去のインタラクションからのユーザーフィードバックデータ。

#### 経験と自己反省

Travel Agentは、パフォーマンスを評価し過去の経験から学ぶためにメタ認知を使用します。

1. **ユーザーフィードバックの分析**：Travel Agentは、どの推奨事項が好評だったか、どれがそうでなかったかを確認し、将来の提案を調整します。
2. **適応性**：以前に混雑した場所が嫌いだと述べたユーザーの場合、Travel Agentは今後ピーク時に人気の観光地を避けるようにします。
3. **エラー修正**：以前に満室のホテルを提案するなどのエラーをした場合、提案前に空室状況をより厳密に確認することを学びます。

#### 実践的な開発者向け例

以下は、Travel Agentがメタ認知を組み込む際のコードの簡略化された例です：

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### メタ認知が重要な理由

- **自己反省**：エージェントはパフォーマンスを分析し、改善点を特定できます。
- **適応性**：フィードバックや変化する条件に基づいて戦略を修正できます。
- **エラー修正**：エージェントは自律的にミスを検出し修正できます。
- **リソース管理**：エージェントは時間や計算能力などのリソースを最適化できます。

メタ認知を組み込むことで、Travel Agentはより個別化された正確な旅行推奨を提供し、全体的なユーザー体験を向上させます。

---
```
```markdown
旅行代理店は、ユーザーのフィードバックに基づいて新しい検索クエリを作成します。  
- 例: ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```  
- **ツール**: 旅行代理店はアルゴリズムを使用して新しい検索結果をランク付けおよびフィルタリングし、ユーザーのフィードバックに基づいて関連性を強調します。  
- 例: ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```  
- **評価**: 旅行代理店は、ユーザーのフィードバックを分析し、必要な調整を行うことで、推奨事項の関連性と正確性を継続的に評価します。  
- 例: ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```  

#### 実用例  
以下は、旅行代理店で修正型RAGアプローチを取り入れたシンプルなPythonコード例です:  
```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```  

### 予防的コンテキストロード  
予防的コンテキストロードとは、クエリを処理する前に関連するコンテキストや背景情報をモデルにロードすることを指します。これにより、モデルはプロセス中に追加データを取得する必要なく、情報に基づいた応答を生成することが可能になります。  

以下は、旅行代理店アプリケーションで予防的コンテキストロードを実装した場合のシンプルな例です:  
```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```  

#### 説明  
1. **初期化 (`__init__` method)**: The `TravelAgent` class pre-loads a dictionary containing information about popular destinations such as Paris, Tokyo, New York, and Sydney. This dictionary includes details like the country, currency, language, and major attractions for each destination.

2. **Retrieving Information (`get_destination_info` method)**: When a user queries about a specific destination, the `get_destination_info` メソッドは、事前ロードされたコンテキスト辞書から関連情報を取得します)。**  
   コンテキストを事前にロードすることで、旅行代理店アプリケーションは、リアルタイムで外部ソースから情報を取得する必要なく、ユーザーのクエリに迅速に応答できます。これにより、アプリケーションはより効率的で応答性が向上します。  

### 目標を設定して計画をブートストラップし、反復する  
計画をブートストラップする際に目標を設定することは、明確な目的または目標結果を念頭に置いて開始することを意味します。この目標を事前に定義することで、モデルは反復プロセス全体でこれを指針として使用できます。これにより、各反復が望ましい結果の達成に向けて進むことを確実にし、プロセスが効率的で集中したものになります。  

以下は、旅行代理店が目標を設定して計画をブートストラップし、その後反復する方法の例です:  

### シナリオ  
旅行代理店がクライアントのためにカスタマイズされた休暇を計画したいと考えています。その目標は、クライアントの好みと予算に基づいて満足度を最大化する旅行日程を作成することです。  

### 手順  
1. クライアントの好みと予算を定義します。  
2. これらの好みに基づいて初期計画をブートストラップします。  
3. クライアントの満足度を最適化するために計画を反復します。  

#### Pythonコード  
```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Example usage
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```  

#### コードの説明  
1. **初期化 (`__init__` method)**: The `TravelAgent` class is initialized with a list of potential destinations, each having attributes like name, cost, and activity type.

2. **Bootstrapping the Plan (`bootstrap_plan` method)**: This method creates an initial travel plan based on the client's preferences and budget. It iterates through the list of destinations and adds them to the plan if they match the client's preferences and fit within the budget.

3. **Matching Preferences (`match_preferences` method)**: This method checks if a destination matches the client's preferences.

4. **Iterating the Plan (`iterate_plan` method)**: This method refines the initial plan by trying to replace each destination in the plan with a better match, considering the client's preferences and budget constraints.

5. **Calculating Cost (`calculate_cost` メソッド)**:  
   このメソッドは、現在の計画の総コストを計算します（新しい目的地を含む場合）。  

#### 使用例  
- **初期計画**: 旅行代理店は、観光を好み、予算が2000ドルのクライアントの好みに基づいて初期計画を作成します。  
- **改良された計画**: 旅行代理店は計画を反復し、クライアントの好みと予算を最適化します。  

目標（例: クライアントの満足度を最大化する）を明確に設定して計画をブートストラップし、計画を改良することで、旅行代理店はクライアントにカスタマイズされた最適な旅行日程を作成できます。このアプローチにより、旅行計画が開始時からクライアントの好みと予算に一致し、各反復で改善されることが保証されます。  

### LLMを活用した再ランク付けとスコアリング  
大規模言語モデル（LLM）は、取得した文書や生成された応答の関連性と品質を評価することで、再ランク付けとスコアリングに使用できます。以下はその仕組みです:  

**取得**: 初期取得ステップでは、クエリに基づいて候補文書や応答のセットを取得します。  
**再ランク付け**: LLMはこれらの候補を評価し、関連性と品質に基づいて再ランク付けします。このステップにより、最も関連性が高く質の高い情報が最初に提示されます。  
**スコアリング**: LLMは各候補にスコアを割り当て、関連性と品質を反映します。これにより、ユーザーに最適な応答や文書を選択するのに役立ちます。  

LLMを再ランク付けとスコアリングに活用することで、システムはより正確で文脈的に関連性の高い情報を提供でき、全体的なユーザー体験が向上します。  

以下は、旅行代理店がユーザーの好みに基づいて旅行先を再ランク付けし、スコアリングするためにLLMを使用する例です:  

#### シナリオ - ユーザーの好みに基づく旅行  
旅行代理店は、クライアントの好みに基づいて最適な旅行先を推奨したいと考えています。LLMは旅行先を再ランク付けし、スコアリングすることで、最も関連性の高いオプションを提示します。  

#### 手順  
1. ユーザーの好みを収集します。  
2. 潜在的な旅行先のリストを取得します。  
3. ユーザーの好みに基づいてLLMを使用して旅行先を再ランク付けし、スコアリングします。  

Azure OpenAI Servicesを使用するように前の例を更新する方法は次のとおりです:  

#### 必要条件  
1. Azureサブスクリプションが必要です。  
2. Azure OpenAIリソースを作成し、APIキーを取得します。  

#### Pythonコード例  
```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Example usage
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```  

#### コードの説明 - Preference Booker  
1. **初期化**: `TravelAgent` class is initialized with a list of potential travel destinations, each having attributes like name and description.

2. **Getting Recommendations (`get_recommendations` method)**: This method generates a prompt for the Azure OpenAI service based on the user's preferences and makes an HTTP POST request to the Azure OpenAI API to get re-ranked and scored destinations.

3. **Generating Prompt (`generate_prompt` method)**: This method constructs a prompt for the Azure OpenAI, including the user's preferences and the list of destinations. The prompt guides the model to re-rank and score the destinations based on the provided preferences.

4. **API Call**: The `requests` library is used to make an HTTP POST request to the Azure OpenAI API endpoint. The response contains the re-ranked and scored destinations.

5. **Example Usage**: The travel agent collects user preferences (e.g., interest in sightseeing and diverse culture) and uses the Azure OpenAI service to get re-ranked and scored recommendations for travel destinations.

Make sure to replace `your_azure_openai_api_key` with your actual Azure OpenAI API key and `https://your-endpoint.com/...` をAzure OpenAIデプロイメントの実際のエンドポイントURLに置き換えます。  

LLMを再ランク付けとスコアリングに活用することで、旅行代理店はクライアントにより個別化され、関連性の高い旅行推奨を提供し、全体的な体験を向上させることができます。  

### RAG: プロンプト技法 vs ツール  
Retrieval-Augmented Generation（RAG）は、AIエージェントの開発においてプロンプト技法とツールの両方として機能します。この2つの違いを理解することで、プロジェクトでRAGをより効果的に活用できます。  

#### RAG as a Prompting Technique  
**それは何か?**  
- プロンプト技法としてのRAGは、大規模なコーパスやデータベースから関連情報を取得するための特定のクエリやプロンプトを作成することを指します。この情報は、応答やアクションを生成するために使用されます。  

**仕組み:**  
1. **プロンプトの作成**: タスクやユーザーの入力に基づいて、構造化されたプロンプトやクエリを作成します。  
2. **情報の取得**: プロンプトを使用して、事前に存在する知識ベースやデータセットから関連データを検索します。  
3. **応答の生成**: 取得した情報と生成AIモデルを組み合わせて、包括的で一貫性のある応答を生成します。  

**旅行代理店での例**:  
- ユーザー入力: 「パリの博物館を訪れたいです。」  
- プロンプト: 「パリのトップ博物館を見つける。」  
- 取得情報: ルーブル美術館、オルセー美術館などの詳細。  
- 生成応答: 「パリのトップ博物館はこちらです: ルーブル美術館、オルセー美術館、ポンピドゥーセンター。」  

#### RAG as a Tool  
**それは何か?**  
- ツールとしてのRAGは、取得と生成プロセスを自動化し、各クエリのために手動でプロンプトを作成する必要なく、複雑なAI機能を開発者が簡単に実装できる統合システムです。  

**仕組み:**  
1. **統合**: RAGをAIエージェントのアーキテクチャに埋め込み、取得と生成タスクを自動的に処理できるようにします。  
2. **自動化**: ツールは、ユーザー入力を受け取るところから最終応答を生成するまで、すべてのプロセスを管理します。  
3. **効率化**: 取得と生成プロセスを合理化し、より迅速で正確な応答を可能にします。  

**旅行代理店での例**:  
- ユーザー入力: 「パリの博物館を訪れたいです。」  
- RAGツール: 自動的に博物館に関する情報を取得し、応答を生成します。  
- 生成応答: 「パリのトップ博物館はこちらです: ルーブル美術館、オルセー美術館、ポンピドゥーセンター。」  

### 比較  

| 項目                     | プロンプト技法                                             | ツール                                             |  
|------------------------|-------------------------------------------------------------|-------------------------------------------------------|  
| **手動 vs 自動**       | 各クエリに対してプロンプトを手動で作成する。                 | 取得と生成のプロセスを自動化する。                     |  
| **制御**               | 取得プロセスをより細かく制御できる。                         | 取得と生成を合理化して自動化する。                     |  
| **柔軟性**             | 特定のニーズに基づいてカスタマイズされたプロンプトを作成可能。 | 大規模な実装において効率的。                         |  
| **複雑性**             | プロンプトの作成と調整が必要。                               | AIエージェントのアーキテクチャに簡単に統合できる。     |  

### 実用例  
**プロンプト技法の例:**  
```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```  

**ツールの例:**  
```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```  
```
```markdown
パリの最高の美術館は?")。  
- **ナビゲーションの意図**: ユーザーは特定のウェブサイトやページに移動したい（例:「ルーブル美術館公式ウェブサイト」）。  
- **取引の意図**: ユーザーはフライトの予約や購入などの取引を行いたい（例:「パリ行きのフライトを予約する」）。  

2. **コンテキスト認識**:  
   - ユーザーのクエリのコンテキストを分析することで、その意図を正確に特定するのに役立つ。これには、以前のやり取り、ユーザーの好み、現在のクエリの具体的な詳細を考慮することが含まれる。  

3. **自然言語処理 (NLP)**:  
   - NLP技術を使用して、ユーザーが提供する自然言語クエリを理解し解釈する。これには、エンティティ認識、感情分析、クエリ解析などのタスクが含まれる。  

4. **パーソナライズ**:  
   - ユーザーの履歴、好み、フィードバックに基づいて検索結果をパーソナライズすることで、取得された情報の関連性を向上させる。  

#### 実用例: 旅行代理店での意図に基づく検索  
旅行代理店を例に取り、意図に基づく検索がどのように実装されるかを見てみましょう。  

1. **ユーザーの好みを収集する**  
   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```  

2. **ユーザーの意図を理解する**  
   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```  

3. **コンテキスト認識**  
   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```  

4. **検索結果をパーソナライズする**  
   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```  

5. **使用例**  
   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```  

---

## 4. ツールとしてのコード生成  
コード生成エージェントは、AIモデルを使用してコードを書き、実行し、複雑な問題を解決し、タスクを自動化する。  

### コード生成エージェント  
コード生成エージェントは、生成AIモデルを使用してコードを書き、実行する。これらのエージェントは、さまざまなプログラミング言語でコードを生成および実行することで、複雑な問題を解決し、タスクを自動化し、貴重な洞察を提供することができる。  

#### 実用的な応用例  
1. **自動コード生成**: データ分析、ウェブスクレイピング、機械学習などの特定のタスクに対するコードスニペットを生成する。  
2. **RAGとしてのSQL**: データベースからデータを取得および操作するためのSQLクエリを使用する。  
3. **問題解決**: アルゴリズムの最適化やデータの分析など、特定の問題を解決するためのコードを作成および実行する。  

#### 例: データ分析のためのコード生成エージェント  
データ分析のためのコード生成エージェントを設計する場合、以下のように動作します。  

1. **タスク**: データセットを分析してトレンドやパターンを特定する。  
2. **手順**:  
   - データセットをデータ分析ツールにロードする。  
   - データをフィルタリングおよび集計するSQLクエリを生成する。  
   - クエリを実行して結果を取得する。  
   - 結果を使用して可視化や洞察を生成する。  
3. **必要なリソース**: データセットへのアクセス、データ分析ツール、およびSQL機能。  
4. **経験**: 過去の分析結果を使用して、将来の分析の精度と関連性を向上させる。  

### 例: 旅行代理店のためのコード生成エージェント  
この例では、旅行代理店のコード生成エージェントを設計し、生成されたコードを実行して旅行の計画を支援します。このエージェントは、旅行オプションの取得、結果のフィルタリング、生成AIを使用した旅程の作成などのタスクを処理できます。  

#### コード生成エージェントの概要  
1. **ユーザーの好みを収集する**: 目的地、旅行日程、予算、興味などのユーザー入力を収集する。  
2. **データを取得するコードを生成する**: フライト、ホテル、観光スポットに関するデータを取得するためのコードスニペットを生成する。  
3. **生成されたコードを実行する**: 実際の情報を取得するために生成されたコードを実行する。  
4. **旅程を生成する**: 取得したデータを個別化された旅行計画にまとめる。  
5. **フィードバックに基づいて調整する**: ユーザーのフィードバックを受け取り、必要に応じてコードを再生成して結果を改善する。  

#### 実装のステップバイステップ  
1. **ユーザーの好みを収集する**  
   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```  

2. **データを取得するコードを生成する**  
   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```  

3. **生成されたコードを実行する**  
   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```  

4. **旅程を生成する**  
   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```  

5. **フィードバックに基づいて調整する**  
   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```  

### 環境認識と推論を活用する  
テーブルのスキーマに基づいてクエリ生成プロセスを強化するために、環境認識と推論を活用できます。以下はその方法の例です。  

1. **スキーマを理解する**: システムはテーブルのスキーマを理解し、この情報を使用してクエリ生成を行う。  
2. **フィードバックに基づいて調整する**: システムはフィードバックに基づいてユーザーの好みを調整し、スキーマ内のどのフィールドを更新する必要があるかを推論する。  
3. **クエリを生成および実行する**: システムは新しい好みに基づいてクエリを生成および実行し、更新されたフライトやホテルのデータを取得する。  

以下はこれらの概念を組み込んだPythonコードの更新例です。  
```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```  

#### 説明 - フィードバックに基づく予約  
1. **スキーマ認識**: `schema` dictionary defines how preferences should be adjusted based on feedback. It includes fields like `favorites` and `avoid`, with corresponding adjustments.
2. **Adjusting Preferences (`adjust_based_on_feedback` method)**: This method adjusts preferences based on user feedback and the schema.
3. **Environment-Based Adjustments (`adjust_based_on_environment` メソッド)**: このメソッドは、スキーマとフィードバックに基づいて調整をカスタマイズします。  
4. **クエリを生成および実行する**: システムは調整された好みに基づいてフライトおよびホテルデータを取得するコードを生成し、これらのクエリの実行をシミュレートします。  
5. **旅程を生成する**: システムは新しいフライト、ホテル、および観光データに基づいて更新された旅程を作成します。  

システムを環境認識型にし、スキーマに基づいて推論することで、より正確で関連性の高いクエリを生成でき、より良い旅行の提案とパーソナライズされたユーザー体験が可能になります。  

### RAG（検索強化生成）技術としてのSQLの使用  
SQL（構造化問い合わせ言語）は、データベースとやり取りするための強力なツールです。RAG（検索強化生成）アプローチの一環として使用される場合、SQLはデータベースから関連データを取得し、AIエージェントの応答やアクションを生成するための情報を提供します。  

#### 主要な概念  
1. **データベースとのやり取り**:  
   - SQLは、データベースをクエリし、関連情報を取得し、データを操作するために使用されます。  
   - 例: フライトの詳細、ホテル情報、観光スポットを旅行データベースから取得する。  

2. **RAGとの統合**:  
   - SQLクエリは、ユーザーの入力と好みに基づいて生成されます。  
   - 取得したデータは、個別化された推奨やアクションを生成するために使用されます。  

3. **動的クエリ生成**:  
   - AIエージェントは、コンテキストとユーザーのニーズに基づいて動的なSQLクエリを生成します。  
   - 例: 予算、日程、興味に基づいて結果をフィルタリングするSQLクエリをカスタマイズする。  

#### 応用例  
- **自動コード生成**: 特定のタスクのためのコードスニペットを生成する。  
- **RAGとしてのSQL**: SQLクエリを使用してデータを操作する。  
- **問題解決**: 問題を解決するためのコードを作成および実行する。  

**例**: データ分析エージェント:  
1. **タスク**: データセットを分析してトレンドを見つける。  
2. **手順**:  
   - データセットをロードする。  
   - データをフィルタリングするSQLクエリを生成する。  
   - クエリを実行して結果を取得する。  
   - 可視化と洞察を生成する。  
3. **リソース**: データセットへのアクセス、SQL機能。  
4. **経験**: 過去の結果を使用して将来の分析を改善する。  

#### 実用例: 旅行代理店でのSQLの使用  
1. **ユーザーの好みを収集する**  
   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```  

2. **SQLクエリを生成する**  
   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```  

3. **SQLクエリを実行する**  
   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```  

4. **推奨を生成する**  
   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```  

#### SQLクエリの例  
1. **フライトクエリ**  
   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```  

2. **ホテルクエリ**  
   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```  

3. **観光地クエリ**  
   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```  

SQLをRAG技術の一部として活用することで、Travel AgentのようなAIエージェントは、関連データを動的に取得し、正確で個別化された推奨を提供することができます。  

### 結論  
メタ認知は、AIエージェントの能力を大幅に向上させる強力なツールです。メタ認知プロセスを組み込むことで、よりインテリジェントで適応性が高く効率的なエージェントを設計できます。追加のリソースを使用して、AIエージェントにおけるメタ認知の魅力的な世界をさらに探求してください。
```

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。原文（元の言語の文書）が公式な情報源として優先されるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の利用により生じた誤解や誤解釈について、当方は一切の責任を負いかねます。