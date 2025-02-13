```markdown
# AIエージェントにおけるメタ認知

## はじめに
AIエージェントにおけるメタ認知に関するレッスンへようこそ！この章は、AIエージェントがどのように自分自身の思考プロセスを考えることができるのかに興味を持つ初心者向けに設計されています。このレッスンの終わりには、重要な概念を理解し、AIエージェント設計においてメタ認知を応用するための実用的な例を学ぶことができます。

## 学習目標
このレッスンを完了すると、以下ができるようになります：
1. エージェント定義における推論ループの影響を理解する。
2. 計画および評価技術を使用して、自己修正型エージェントを支援する。
3. タスクを達成するためにコードを操作できるエージェントを作成する。

## メタ認知の導入
メタ認知とは、自分自身の思考について考えることを含む高次の認知プロセスを指します。AIエージェントにおいては、自己認識と過去の経験に基づいて行動を評価し調整する能力を意味します。

### メタ認知とは？
メタ認知、つまり「思考について考えること」は、自己認識と認知プロセスの自己調整を含む高次の認知プロセスです。AIの分野では、メタ認知はエージェントに戦略や行動を評価し適応させる力を与え、問題解決能力や意思決定能力の向上につながります。メタ認知を理解することで、より知的で適応性が高く効率的なAIエージェントを設計することができます。

### AIエージェントにおけるメタ認知の重要性
メタ認知は、AIエージェント設計において以下の理由で重要な役割を果たします：

![メタ認知の重要性](../../../09-metacognition/images/importance-of-metacognition.png)
- **自己反省**：エージェントは自分のパフォーマンスを評価し、改善が必要な領域を特定できます。
- **適応性**：エージェントは過去の経験や変化する環境に基づいて戦略を変更できます。
- **エラー修正**：エージェントはエラーを自律的に検出し修正することで、より正確な結果を得ることができます。
- **リソース管理**：エージェントは、時間や計算能力などのリソースを計画と評価によって最適化できます。

## AIエージェントの構成要素
メタ認知プロセスに入る前に、AIエージェントの基本的な構成要素を理解することが重要です。AIエージェントは通常、以下の要素で構成されます：

- **パーソナ**：エージェントの個性や特性であり、ユーザーとのインタラクションの方法を定義します。
- **ツール**：エージェントが実行できる機能や能力。
- **スキル**：エージェントが持つ知識や専門性。

これらの要素が組み合わさって、特定のタスクを実行できる「専門ユニット」を形成します。

**例**：旅行エージェントを考えてみましょう。このエージェントは旅行を計画するだけでなく、リアルタイムデータや過去の顧客の旅行経験に基づいてルートを調整することができます。

### 例：旅行エージェントサービスにおけるメタ認知
AIを活用した旅行エージェントサービスを設計していると想像してください。このエージェント「Travel Agent」は、ユーザーが休暇を計画するのを支援します。メタ認知を組み込むことで、Travel Agentは自己認識と過去の経験に基づいて行動を評価し調整できます。

#### 現在のタスク
現在のタスクは、ユーザーがパリへの旅行を計画するのを支援することです。

#### タスクを完了するためのステップ
1. **ユーザーの好みを収集する**：旅行日程、予算、興味（例：博物館、料理、ショッピング）、および特定の要件についてユーザーに尋ねます。
2. **情報を取得する**：ユーザーの好みに合ったフライトオプション、宿泊施設、観光地、レストランを検索します。
3. **提案を生成する**：フライトの詳細、ホテルの予約、おすすめのアクティビティを含むパーソナライズされた旅程を提供します。
4. **フィードバックに基づいて調整する**：提案についてユーザーからフィードバックを求め、必要に応じて調整を行います。

#### 必要なリソース
- フライトおよびホテル予約データベースへのアクセス。
- パリの観光地やレストランに関する情報。
- 過去のインタラクションからのユーザーフィードバックデータ。

#### 経験と自己反省
Travel Agentは、パフォーマンスを評価し、過去の経験から学ぶためにメタ認知を使用します。

1. **ユーザーフィードバックの分析**：Travel Agentはユーザーフィードバックを確認し、どの提案が好評で、どれがそうでなかったかを特定します。そして、将来の提案を調整します。
2. **適応性**：過去にユーザーが混雑した場所を嫌うと述べた場合、Travel Agentは今後、混雑する時間帯に人気の観光地を推奨しないようにします。
3. **エラー修正**：例えば、Travel Agentが以前に満室のホテルを推奨するエラーを犯した場合、今後は推奨する前に空室状況をより厳密に確認するよう学習します。

#### 実用的な開発者向け例
以下は、メタ認知を組み込んだTravel Agentのコードがどのように見えるかの簡略化された例です：

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
- **自己反省**：エージェントは自分のパフォーマンスを分析し、改善が必要な領域を特定できます。
- **適応性**：エージェントはフィードバックや変化する条件に基づいて戦略を変更できます。
- **エラー修正**：エージェントは自律的にエラーを検出し修正できます。
- **リソース管理**：エージェントは、時間や計算能力などのリソースを最適化できます。

メタ認知を組み込むことで、Travel Agentはよりパーソナライズされた正確な旅行提案を提供し、全体的なユーザー体験を向上させることができます。
```
```markdown
旅行代理店は、ユーザーのフィードバックに基づいて新しい検索クエリを作成します。  
- 例: ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```  
- **ツール**: 旅行代理店はアルゴリズムを使用して新しい検索結果をランク付けし、フィルタリングします。これにより、ユーザーのフィードバックに基づいた関連性を強調します。  
- 例: ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```  
- **評価**: 旅行代理店は、ユーザーのフィードバックを分析し、必要に応じて調整を行うことで、推奨事項の関連性と正確性を継続的に評価します。  
- 例: ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```  

#### 実践例  
以下は、旅行代理店におけるCorrective RAGアプローチを組み込んだ簡単なPythonコード例です:  
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

### 事前コンテキスト読み込み  
事前コンテキスト読み込みとは、クエリを処理する前に関連するコンテキストや背景情報をモデルに読み込むことを指します。これにより、モデルはプロセス中に追加のデータを取得する必要がなく、最初からこの情報にアクセスできるため、より情報に基づいた応答を生成できます。  

以下は、Pythonで旅行代理店アプリケーション向けの事前コンテキスト読み込みがどのように見えるかを示した簡単な例です:  
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

2. **Retrieving Information (`get_destination_info` method)**: When a user queries about a specific destination, the `get_destination_info` メソッド)**:  
   このメソッドは、事前にロードされたコンテキスト辞書から関連情報を取得します。コンテキストを事前に読み込むことで、旅行代理店アプリケーションは、リアルタイムで外部ソースから情報を取得することなく、ユーザーのクエリに迅速に応答できます。これにより、アプリケーションがより効率的で応答性の高いものになります。  

### 目標を設定して計画をブートストラップし、反復する前に  
目標を設定して計画をブートストラップするとは、明確な目標や目的を最初に定義し、それを指針として反復プロセス全体で活用することを指します。この方法により、各反復が目標達成に向けて効率的かつ集中して進むことができます。  

以下は、Pythonで旅行代理店向けに目標を設定して旅行計画をブートストラップする例です:  

### シナリオ  
旅行代理店がクライアントのためにカスタマイズされた休暇計画を立てたいと考えています。目標は、クライアントの満足度を最大化する旅行日程を作成することです。  

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
   このメソッドは、現在の計画に新しい目的地を含めた総コストを計算します。  

#### 使用例  
- **初期計画**: 旅行代理店は、観光を希望するクライアントの好みと2000ドルの予算に基づいて初期計画を作成します。  
- **洗練された計画**: 旅行代理店は計画を反復し、クライアントの好みと予算を最適化します。  

目標（例: クライアントの満足度を最大化すること）を明確に設定して計画をブートストラップし、それを反復して改善することで、旅行代理店はクライアントに合わせた最適化された旅行日程を作成できます。このアプローチにより、旅行計画がクライアントの好みと予算に初めから一致し、反復ごとに改善されます。  

### LLMを活用した再ランキングとスコアリング  
大規模言語モデル（LLM）は、取得した文書や生成された応答の関連性や品質を評価することで、再ランキングとスコアリングに使用できます。以下はその仕組みです:  

**取得**: 初期取得ステップでは、クエリに基づいて候補文書や応答のセットを取得します。  
**再ランキング**: LLMはこれらの候補を評価し、関連性と品質に基づいて再ランキングします。このステップにより、最も関連性が高く高品質な情報が最初に提示されます。  
**スコアリング**: LLMは各候補にスコアを割り当て、その関連性と品質を反映します。これにより、ユーザーに最適な応答や文書を選択するのに役立ちます。  

LLMを再ランキングとスコアリングに活用することで、システムはより正確で文脈に関連する情報を提供し、全体的なユーザー体験を向上させることができます。  

以下は、旅行代理店がクライアントの好みに基づいて旅行先を再ランキングおよびスコアリングするためにLLMを使用する例です:  

#### シナリオ - 好みに基づく旅行  
旅行代理店は、クライアントの好みに基づいて最適な旅行先を提案したいと考えています。LLMは、最も関連性の高いオプションを提示するために旅行先を再ランキングおよびスコアリングします。  

#### 手順:  
1. ユーザーの好みを収集します。  
2. 潜在的な旅行先のリストを取得します。  
3. LLMを使用して、ユーザーの好みに基づいて旅行先を再ランキングおよびスコアリングします。  

以下は、Azure OpenAI Servicesを使用して前述の例を更新する方法です:  

#### 要件  
1. Azureサブスクリプションが必要です。  
2. Azure OpenAIリソースを作成し、APIキーを取得します。  

#### Pythonコードの例  
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

LLMを再ランキングとスコアリングに活用することで、旅行代理店はクライアントによりパーソナライズされ、関連性の高い旅行提案を提供でき、全体的な体験を向上させることができます。  
```
```markdown
パリの最高の博物館?"). - **ナビゲーションの意図**: ユーザーは特定のウェブサイトやページに移動したいと考えています（例: 「ルーブル美術館公式ウェブサイト」）。 - **取引の意図**: ユーザーはフライトの予約や購入などの取引を行いたいと考えています（例: 「パリ行きのフライトを予約する」）。 2. **コンテキスト認識**: - ユーザーのクエリのコンテキストを分析することで、意図を正確に特定できます。これには、以前のやり取り、ユーザーの好み、現在のクエリの具体的な詳細を考慮することが含まれます。 3. **自然言語処理 (NLP)**: - NLP技術を使用して、ユーザーが提供する自然言語クエリを理解し解釈します。これには、エンティティ認識、感情分析、クエリ解析などのタスクが含まれます。 4. **パーソナライズ**: - ユーザーの履歴、好み、フィードバックに基づいて検索結果をパーソナライズすることで、取得した情報の関連性を高めます。 #### 実践例: 旅行エージェントでの意図を持った検索 旅行エージェントを例にとり、意図を持った検索がどのように実装されるかを見てみましょう。 1. **ユーザーの好みを収集する** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **ユーザーの意図を理解する** ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ``` 3. **コンテキスト認識** ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ``` 4. **検索と結果のパーソナライズ** ```python
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
   ``` 5. **使用例** ```python
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
   ``` --- ## 4. ツールとしてのコード生成 コード生成エージェントはAIモデルを使用してコードを作成および実行し、複雑な問題を解決したりタスクを自動化したりします。 ### コード生成エージェント コード生成エージェントは生成AIモデルを使用してコードを作成および実行します。これらのエージェントは、さまざまなプログラミング言語でコードを生成して実行することで、複雑な問題を解決し、タスクを自動化し、貴重な洞察を提供できます。 #### 実践的な応用例 1. **自動コード生成**: データ分析、ウェブスクレイピング、機械学習などの特定のタスクに対応するコードスニペットを生成します。 2. **RAGとしてのSQL**: データベースからデータを取得し操作するためにSQLクエリを使用します。 3. **問題解決**: 特定の問題を解決するためにコードを作成および実行します（例: アルゴリズムの最適化やデータ分析）。 #### 例: データ分析のためのコード生成エージェント データ分析を行うコード生成エージェントを設計すると仮定します。以下のように動作します: 1. **タスク**: データセットを分析してトレンドやパターンを特定します。 2. **手順**: - データセットをデータ分析ツールにロードします。 - データをフィルタリングおよび集計するためのSQLクエリを生成します。 - クエリを実行して結果を取得します。 - 結果を使用して視覚化や洞察を生成します。 3. **必要なリソース**: データセットへのアクセス、データ分析ツール、SQL機能。 4. **経験**: 過去の分析結果を活用して、将来の分析の精度と関連性を向上させます。 ### 例: 旅行エージェントのためのコード生成エージェント この例では、旅行エージェント用のコード生成エージェントを設計し、生成および実行するコードを通じてユーザーの旅行計画を支援します。このエージェントは、旅行オプションの取得、結果のフィルタリング、生成AIを使用した旅程の作成などのタスクを処理できます。 #### コード生成エージェントの概要 1. **ユーザーの好みを収集する**: 目的地、旅行日程、予算、興味などのユーザー入力を収集します。 2. **データを取得するコードを生成する**: フライト、ホテル、アトラクションに関するデータを取得するためのコードスニペットを生成します。 3. **生成されたコードを実行する**: 生成されたコードを実行してリアルタイム情報を取得します。 4. **旅程を生成する**: 取得したデータを個人に合わせた旅行プランにまとめます。 5. **フィードバックに基づいて調整する**: ユーザーのフィードバックを受け取り、必要に応じてコードを再生成して結果を改善します。 #### 実装のステップバイステップ 1. **ユーザーの好みを収集する** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **データを取得するコードを生成する** ```python
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
   ``` 3. **生成されたコードを実行する** ```python
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
   ``` 4. **旅程を生成する** ```python
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
   ``` 5. **フィードバックに基づいて調整する** ```python
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
   ``` ### 環境認識と推論の活用 テーブルのスキーマに基づいてクエリ生成プロセスを強化することで、環境認識と推論を活用することができます。以下はその方法の例です: 1. **スキーマの理解**: システムはテーブルのスキーマを理解し、この情報を基にクエリ生成を行います。 2. **フィードバックに基づいた調整**: システムはフィードバックに基づいてユーザーの好みを調整し、スキーマ内のどのフィールドを更新する必要があるかを推論します。 3. **クエリの生成と実行**: システムは新しい好みに基づいてクエリを生成および実行し、最新のフライトやホテルデータを取得します。 以下はこれらの概念を取り入れたPythonコードの更新例です: ```python
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
``` #### 説明 - フィードバックに基づく予約 1. **スキーマ認識**: `schema` dictionary defines how preferences should be adjusted based on feedback. It includes fields like `favorites` and `avoid`, with corresponding adjustments.
2. **Adjusting Preferences (`adjust_based_on_feedback` method)**: This method adjusts preferences based on user feedback and the schema.
3. **Environment-Based Adjustments (`adjust_based_on_environment` メソッド)**: このメソッドは、スキーマとフィードバックに基づいて調整をカスタマイズします。 4. **クエリの生成と実行**: システムは調整された好みに基づいてフライトやホテルデータを取得するコードを生成し、これらのクエリの実行をシミュレートします。 5. **旅程の生成**: システムは新しいフライト、ホテル、アトラクションデータに基づいて更新された旅程を作成します。 システムを環境認識させ、スキーマに基づいて推論することで、より正確で関連性の高いクエリを生成できるようになり、より良い旅行推奨と個別化されたユーザー体験を提供できます。 ### SQLをRAG技術として使用する SQL（構造化クエリ言語）はデータベースと対話するための強力なツールです。SQLをRetrieval-Augmented Generation（RAG）アプローチの一部として使用することで、データベースから関連データを取得し、AIエージェントの応答やアクションを生成する際に利用できます。旅行エージェントの文脈でSQLをRAG技術として使用する方法を見てみましょう。 #### 主要な概念 1. **データベースとの対話**: - SQLはデータベースをクエリし、関連情報を取得し、データを操作するために使用されます。 - 例: フライトの詳細、ホテル情報、アトラクションを旅行データベースから取得する。 2. **RAGとの統合**: - SQLクエリはユーザー入力と好みに基づいて生成されます。 - 取得したデータは個別化された推奨やアクションを生成するために使用されます。 3. **動的クエリ生成**: - AIエージェントはコンテキストやユーザーのニーズに基づいて動的にSQLクエリを生成します。 - 例: 予算、日程、興味に基づいて結果をフィルタリングするためのSQLクエリをカスタマイズする。 #### 応用例 - **自動コード生成**: 特定のタスクに対応するコードスニペットを生成する。 - **RAGとしてのSQL**: データ操作のためにSQLクエリを使用する。 - **問題解決**: 問題を解決するためにコードを作成および実行する。 **例**: データ分析エージェント: 1. **タスク**: データセットを分析してトレンドを見つける。 2. **手順**: - データセットをロードする。 - データをフィルタリングするためのSQLクエリを生成する。 - クエリを実行して結果を取得する。 - 視覚化と洞察を生成する。 3. **リソース**: データセットアクセス、SQL機能。 4. **経験**: 過去の結果を使用して将来の分析を改善する。 #### 実践例: 旅行エージェントでのSQLの使用 1. **ユーザーの好みを収集する** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **SQLクエリを生成する** ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ``` 3. **SQLクエリを実行する** ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ``` 4. **推奨を生成する** ```python
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
   ``` #### SQLクエリの例 1. **フライトクエリ** ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ``` 2. **ホテルクエリ** ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ``` 3. **アトラクションクエリ** ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ``` SQLをRetrieval-Augmented Generation（RAG）技術の一部として活用することで、旅行エージェントのようなAIエージェントは、関連性の高いデータを動的に取得し、正確で個別化された推奨を提供できます。 ### 結論 メタ認知はAIエージェントの能力を大幅に向上させる強力なツールです。メタ認知プロセスを組み込むことで、よりインテリジェントで適応性があり効率的なエージェントを設計できます。追加のリソースを活用して、AIエージェントにおけるメタ認知の魅力的な世界をさらに探求してください。
```

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で記載された原文を信頼できる情報源と見なしてください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用に起因する誤解や誤った解釈について、当社は一切の責任を負いかねます。