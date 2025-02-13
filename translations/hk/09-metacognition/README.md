```markdown
# 元認知於人工智能代理中的應用

## 簡介

歡迎來到關於人工智能代理元認知的課程！本章節專為對人工智能代理如何思考其自身思維過程感興趣的初學者設計。在本課程結束時，您將理解關鍵概念，並能運用實際例子設計具備元認知能力的人工智能代理。

## 學習目標

完成本課程後，您將能夠：
1. 理解代理定義中推理循環的影響。
2. 使用規劃與評估技術幫助代理自我糾正。
3. 創建能夠操控代碼以完成任務的代理。

## 元認知簡介

元認知指的是涉及對自身思維過程進行思考的高階認知過程。對於人工智能代理來說，這意味著能夠基於自我意識和過去經驗評估並調整其行為。

### 什麼是元認知？

元認知，或稱“思考的思考”，是一種高階認知過程，涉及對自身認知過程的自我意識和自我調節。在人工智能領域，元認知使代理能夠評估並適應其策略和行動，從而提升問題解決和決策能力。通過理解元認知，您可以設計出更智能、更具適應性和效率的人工智能代理。

### 元認知在人工智能代理中的重要性

元認知在人工智能代理設計中具有以下幾點重要意義：

![元認知的重要性](../../../09-metacognition/images/importance-of-metacognition.png)

- **自我反思**：代理能夠評估自身表現並找出改進的領域。
- **適應性**：代理能夠根據過去經驗和變化的環境調整其策略。
- **錯誤糾正**：代理能夠自主檢測並糾正錯誤，從而獲得更準確的結果。
- **資源管理**：代理能夠通過規劃和評估行動來優化資源（如時間和計算能力）的使用。

## 人工智能代理的組成

在深入探討元認知過程之前，先了解人工智能代理的基本組成是很重要的。一個人工智能代理通常由以下部分組成：

- **人格**：代理的個性和特徵，定義了它如何與用戶互動。
- **工具**：代理能執行的功能和能力。
- **技能**：代理擁有的知識和專業能力。

這些組成部分共同構建了一個“專業單元”，能夠執行特定任務。

**例子**：考慮一個旅行代理，它不僅計劃您的假期，還能基於實時數據和過往客戶旅程經驗調整路徑。

### 例子：旅行代理服務中的元認知

假設您正在設計一個由人工智能驅動的旅行代理服務。該代理“旅行代理”幫助用戶規劃假期。為了融入元認知，旅行代理需要基於自我意識和過往經驗評估並調整其行動。以下是元認知可能發揮作用的方式：

#### 當前任務

幫助用戶規劃一次巴黎之旅。

#### 完成任務的步驟

1. **收集用戶偏好**：詢問用戶旅行日期、預算、興趣（如博物館、美食、購物）以及任何具體需求。
2. **檢索信息**：搜尋符合用戶偏好的航班選項、住宿、景點和餐廳。
3. **生成推薦**：提供包含航班詳情、酒店預訂和建議活動的個性化行程。
4. **根據反饋調整**：詢問用戶對推薦的反饋並進行必要調整。

#### 所需資源

- 訪問航班和酒店預訂數據庫。
- 關於巴黎景點和餐廳的信息。
- 過往互動中的用戶反饋數據。

#### 經驗與自我反思

旅行代理利用元認知評估其表現並從過去經驗中學習。例如：

1. **分析用戶反饋**：旅行代理回顧用戶反饋，以確定哪些推薦受到歡迎，哪些不受歡迎，並相應地調整未來建議。
2. **適應性**：如果用戶之前提到不喜歡擁擠的地方，旅行代理將避免在高峰時段推薦熱門旅遊景點。
3. **錯誤糾正**：如果旅行代理在過去的預訂中出現錯誤，例如推薦已滿房的酒店，它將學習在推薦之前更嚴格地檢查可用性。

#### 實用開發者示例

以下是一個簡化的示例，展示旅行代理在代碼中如何融入元認知：

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

#### 為什麼元認知很重要

- **自我反思**：代理能分析其表現並找出改進的領域。
- **適應性**：代理能根據反饋和變化條件調整策略。
- **錯誤糾正**：代理能自主檢測並糾正錯誤。
- **資源管理**：代理能優化資源的使用，例如時間和計算能力。

通過融入元認知，旅行代理可以提供更個性化和準確的旅行推薦，提升整體用戶體驗。

---

## 2. 代理中的規劃

規劃是人工智能代理行為的一個關鍵組成部分。它涉及考慮當前狀態、資源和可能的障礙，制定實現目標所需的步驟。

### 規劃的要素

- **當前任務**：明確定義任務。
- **完成任務的步驟**：將任務分解為可管理的步驟。
- **所需資源**：確定必要的資源。
- **經驗**：利用過去經驗指導規劃。

**例子**：以下是旅行代理有效協助用戶規劃旅行所需採取的步驟：

### 旅行代理的步驟

1. **收集用戶偏好**
   - 詢問用戶有關旅行日期、預算、興趣以及任何具體需求的詳細信息。
   - 例子：“您計劃什麼時候旅行？”“您的預算範圍是多少？”“您在度假時喜歡哪些活動？”

2. **檢索信息**
   - 根據用戶偏好搜尋相關旅行選項。
   - **航班**：尋找符合用戶預算和偏好旅行日期的可用航班。
   - **住宿**：尋找符合用戶位置、價格和設施偏好的酒店或租賃物業。
   - **景點和餐廳**：確定符合用戶興趣的熱門景點、活動和餐飲選擇。

3. **生成推薦**
   - 將檢索到的信息編輯成個性化行程。
   - 提供航班選項、酒店預訂和建議活動的詳細信息，確保建議符合用戶偏好。

4. **向用戶展示行程**
   - 與用戶分享建議行程供其審閱。
   - 例子：“這是您巴黎之旅的建議行程，包括航班詳情、酒店預訂以及推薦活動和餐廳。請告訴我您的想法！”

5. **收集反饋**
   - 詢問用戶對建議行程的反饋。
   - 例子：“您喜歡這些航班選項嗎？”“這家酒店是否符合您的需求？”“是否有任何活動需要添加或刪除？”

6. **根據反饋調整**
   - 根據用戶反饋修改行程。
   - 將航班、住宿和活動推薦做必要更改以更好地符合用戶偏好。

7. **最終確認**
   - 向用戶展示更新後的行程供其最終確認。
   - 例子：“我已根據您的反饋進行了調整。這是更新後的行程。一切看起來是否合適？”

8. **預訂並確認**
   - 用戶批准行程後，進行航班、住宿及任何預先計劃活動的預訂。
   - 將確認詳情發送給用戶。

9. **提供持續支持**
   - 在旅行前和旅行期間，隨時為用戶提供幫助或額外需求。
   - 例子：“如果您在旅行期間需要進一步的幫助，隨時聯繫我！”

### 互動示例

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

# Example usage within a booing request
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

## 3. 糾正性 RAG 系統

首先，讓我們了解 RAG 工具與預先上下文加載的區別：

![RAG vs Context Loading](../../../09-metacognition/images/rag-vs-context.png)

### 檢索增強生成（RAG）

RAG 將檢索系統與生成模型結合。當查詢被提出時，檢索系統從外部來源獲取相關文檔或數據，並將檢索到的信息用於增強生成模型的輸入。這有助於模型生成更準確和上下文相關的響應。

在 RAG 系統中，代理從知識庫中檢索相關信息並用於生成適當的響應或行動。

### 糾正性 RAG 方法

糾正性 RAG 方法專注於使用 RAG 技術糾正錯誤並提高人工智能代理的準確性。這涉及：

1. **提示技術**：使用特定提示指導代理檢索相關信息。
2. **工具**：實施算法和機制，使代理能夠評估檢索信息的相關性並生成準確的響應。
3. **評估**：持續評估代理的表現並進行調整以提高其準確性和效率。

#### 例子：搜索代理中的糾正性 RAG

考慮一個從網絡檢索信息以回答用戶查詢的搜索代理。糾正性 RAG 方法可能涉及：

1. **提示技術**：根據用戶輸入制定搜索查詢。
2. **工具**：使用自然語言處理和機器學習算法對搜索結果進行排序和過濾。
3. **評估**：分析用戶反饋以識別和糾正檢索信息中的不準確之處。

### 糾正性 RAG 在旅行代理中的應用

糾正性 RAG（檢索增強生成）增強了人工智能在檢索和生成信息時糾正任何不準確的能力。讓我們看看旅行代理如何使用糾正性 RAG 方法提供更準確和相關的旅行建議。這涉及：

- **提示技術**：使用特定提示指導代理檢索相關信息。
- **工具**：實施算法和機制，使代理能夠評估檢索信息的相關性並生成準確的響應。
- **評估**：持續評估代理的表現並進行調整以提高其準確性和效率。

#### 實施糾正性 RAG 的步驟

1. **初次用戶互動**
   - 旅行代理收集用戶的初始偏好，例如目的地、旅行日期、預算和興趣。
   - 例子：```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **信息檢索**
   - 旅行代理根據用戶偏好檢索有關航班、住宿、景點和餐廳的信息。
   - 例子：```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **生成初始推薦**
   - 旅行代理使用檢索到的信息生成個性化行程。
   - 例子：```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **收集用戶反饋**
   - 旅行代理詢問用戶對初始推薦的反饋。
   - 例子：```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **糾正性 RAG 過程**
   - **提示技術**：請從左到右書寫輸出。
```
```markdown
旅遊代理根據用戶反饋制定新的搜索查詢。  
- 範例：```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```  
- **工具**：旅遊代理使用算法對新的搜索結果進行排名和篩選，強調基於用戶反饋的相關性。  
- 範例：```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```  
- **評估**：旅遊代理通過分析用戶反饋並進行必要調整，不斷評估其推薦的相關性和準確性。  
- 範例：```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```  

#### 實用範例  
以下是一個簡化的 Python 代碼範例，展示了如何在旅遊代理中應用 Corrective RAG 方法：  
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

### 預先加載上下文  
預先加載上下文是指在處理查詢之前，將相關的上下文或背景信息加載到模型中。這意味著模型從一開始就能夠訪問這些信息，從而在不需要在過程中檢索額外數據的情況下生成更有根據的回應。  

以下是一個展示如何為旅遊代理應用程序在 Python 中進行預先加載上下文的簡化範例：  
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

#### 解釋  
1. **初始化 (`__init__` method)**: The `TravelAgent` class pre-loads a dictionary containing information about popular destinations such as Paris, Tokyo, New York, and Sydney. This dictionary includes details like the country, currency, language, and major attractions for each destination.

2. **Retrieving Information (`get_destination_info` method)**: When a user queries about a specific destination, the `get_destination_info` 方法)**：該方法從預加載的上下文字典中獲取相關信息。通過預加載上下文，旅遊代理應用程序可以快速響應用戶查詢，而不需要實時從外部源檢索這些信息。這使應用程序更高效且更具響應性。  

### 在迭代前用目標啟動計劃  
在迭代前用目標啟動計劃是指以清晰的目標或預期結果為起點。通過提前定義這一目標，模型可以將其作為指導原則，貫穿整個迭代過程。這有助於確保每次迭代都朝著實現所需結果的方向邁進，使過程更加高效且聚焦。  

以下是一個展示如何在旅遊代理中用目標啟動旅行計劃的 Python 範例：  

### 場景  
一位旅遊代理希望為客戶制定一個定制化的假期計劃。目標是基於客戶的偏好和預算，創建一個最大化客戶滿意度的旅行行程。  

### 步驟  
1. 定義客戶的偏好和預算。  
2. 基於這些偏好啟動初始計劃。  
3. 迭代以完善計劃，優化客戶滿意度。  

#### Python 代碼  
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

#### 代碼解釋  
1. **初始化 (`__init__` method)**: The `TravelAgent` class is initialized with a list of potential destinations, each having attributes like name, cost, and activity type.

2. **Bootstrapping the Plan (`bootstrap_plan` method)**: This method creates an initial travel plan based on the client's preferences and budget. It iterates through the list of destinations and adds them to the plan if they match the client's preferences and fit within the budget.

3. **Matching Preferences (`match_preferences` method)**: This method checks if a destination matches the client's preferences.

4. **Iterating the Plan (`iterate_plan` method)**: This method refines the initial plan by trying to replace each destination in the plan with a better match, considering the client's preferences and budget constraints.

5. **Calculating Cost (`calculate_cost` 方法)**：該方法計算當前計劃的總成本，包括一個潛在的新目的地。  

#### 使用範例  
- **初始計劃**：旅遊代理基於客戶對觀光的偏好和 $2000 的預算創建初始計劃。  
- **優化計劃**：旅遊代理通過迭代完善計劃，優化客戶的偏好和預算。  

通過以清晰的目標（例如，最大化客戶滿意度）啟動計劃並進行迭代以完善計劃，旅遊代理可以為客戶創建一個定制化且優化的旅行行程。這種方法確保旅行計劃從一開始就符合客戶的偏好和預算，並在每次迭代中得到改進。  

### 利用 LLM 進行重新排序和評分  
大型語言模型（LLMs）可以通過評估檢索到的文檔或生成的回應的相關性和質量來進行重新排序和評分。以下是其工作原理：  

**檢索**：初始檢索步驟根據查詢獲取一組候選文檔或回應。  
**重新排序**：LLM 評估這些候選項，並根據其相關性和質量重新排序。此步驟確保最相關和高質量的信息優先呈現。  
**評分**：LLM 為每個候選項分配分數，反映其相關性和質量。這有助於選擇最適合用戶的回應或文檔。  

通過利用 LLM 進行重新排序和評分，系統可以提供更準確且具有上下文相關的信息，從而改善整體用戶體驗。  

以下是一個展示旅遊代理如何使用大型語言模型（LLM）根據用戶偏好對旅行目的地進行重新排序和評分的 Python 範例：  

#### 場景 - 基於偏好的旅行  
一位旅遊代理希望根據客戶的偏好推薦最佳旅行目的地。LLM 將幫助重新排序和評分目的地，確保呈現最相關的選項。  

#### 步驟：  
1. 收集用戶偏好。  
2. 檢索潛在旅行目的地的列表。  
3. 使用 LLM 根據用戶偏好重新排序和評分目的地。  

以下是如何使用 Azure OpenAI 服務更新上述範例：  

#### 要求  
1. 您需要擁有 Azure 訂閱。  
2. 創建 Azure OpenAI 資源並獲取您的 API 密鑰。  

#### Python 代碼範例  
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

#### 代碼解釋 - 偏好預訂器  
1. **初始化**：將 `TravelAgent` class is initialized with a list of potential travel destinations, each having attributes like name and description.

2. **Getting Recommendations (`get_recommendations` method)**: This method generates a prompt for the Azure OpenAI service based on the user's preferences and makes an HTTP POST request to the Azure OpenAI API to get re-ranked and scored destinations.

3. **Generating Prompt (`generate_prompt` method)**: This method constructs a prompt for the Azure OpenAI, including the user's preferences and the list of destinations. The prompt guides the model to re-rank and score the destinations based on the provided preferences.

4. **API Call**: The `requests` library is used to make an HTTP POST request to the Azure OpenAI API endpoint. The response contains the re-ranked and scored destinations.

5. **Example Usage**: The travel agent collects user preferences (e.g., interest in sightseeing and diverse culture) and uses the Azure OpenAI service to get re-ranked and scored recommendations for travel destinations.

Make sure to replace `your_azure_openai_api_key` with your actual Azure OpenAI API key and `https://your-endpoint.com/...` 替換為 Azure OpenAI 部署的實際端點 URL。  

通過利用 LLM 進行重新排序和評分，旅遊代理可以為客戶提供更個性化且相關性更高的旅行推薦，從而提升他們的整體體驗。  

### RAG：提示技術與工具  
檢索增強生成（RAG）既可以作為提示技術，也可以作為 AI 代理開發中的工具。理解兩者的區別有助於您更有效地在項目中利用 RAG。  

#### RAG 作為提示技術  
**什麼是 RAG？**  
- 作為提示技術，RAG 涉及制定特定查詢或提示，以引導從大型語料庫或數據庫中檢索相關信息。這些信息隨後被用於生成回應或採取行動。  

**如何運作：**  
1. **制定提示**：根據任務或用戶輸入創建結構良好的提示或查詢。  
2. **檢索信息**：使用提示從預先存在的知識庫或數據集中搜索相關數據。  
3. **生成回應**：將檢索到的信息與生成式 AI 模型結合，生成全面且連貫的回應。  

**旅遊代理範例**：  
- 用戶輸入：「我想參觀巴黎的博物館。」  
- 提示：「查找巴黎的頂級博物館。」  
- 檢索信息：關於盧浮宮、奧賽博物館等的詳細信息。  
- 生成回應：「以下是巴黎的一些頂級博物館：盧浮宮、奧賽博物館和蓬皮杜中心。」  

#### RAG 作為工具  
**什麼是 RAG？**  
- 作為工具，RAG 是一個集成系統，自動化檢索和生成過程，使開發者能夠更輕鬆地實現複雜的 AI 功能，而無需為每個查詢手動編寫提示。  

**如何運作：**  
1. **集成**：將 RAG 嵌入到 AI 代理的架構中，使其能夠自動處理檢索和生成任務。  
2. **自動化**：工具管理整個過程，從接收用戶輸入到生成最終回應，無需為每一步驟顯式提示。  
3. **效率**：通過簡化檢索和生成過程，提高代理的性能，實現更快且更準確的回應。  

**旅遊代理範例**：  
- 用戶輸入：「我想參觀巴黎的博物館。」  
- RAG 工具：自動檢索關於博物館的信息並生成回應。  
- 生成回應：「以下是巴黎的一些頂級博物館：盧浮宮、奧賽博物館和蓬皮杜中心。」  

### 比較  
| **方面**              | **提示技術**                                              | **工具**                                           |  
|------------------------|-------------------------------------------------------------|---------------------------------------------------|  
| **手動與自動**         | 每個查詢手動制定提示。                                      | 檢索和生成過程自動化。                             |  
| **控制**              | 提供對檢索過程的更多控制。                                  | 簡化並自動化檢索和生成過程。                       |  
| **靈活性**            | 允許基於特定需求定制提示。                                  | 對於大規模實現更高效。                             |  
| **複雜性**            | 需要編寫和調整提示。                                        | 更易於集成到 AI 代理的架構中。                     |  

### 實用範例  
**提示技術範例：**  
```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```  

**工具範例：**  
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

### 評估相關性  
評估相關性是 AI 代理性能的一個關鍵方面。它確保代理檢索和生成的信息對用戶是適當的、準確的且有用的。讓我們探討如何在 AI 代理中評估相關性，包括實用範例和技術。  

#### 評估相關性的關鍵概念  
1. **上下文意識**：  
   - 代理必須理解用戶查詢的上下文，以檢索和生成相關信息。  
   - 範例：如果用戶詢問「巴黎最好的餐廳」，代理應考慮用戶的偏好，例如菜系類型和預算。  
2. **準確性**：  
   - 代理提供的信息應該是事實正確且最新的。  
   - 範例：推薦目前營業且評價良好的餐廳，而不是過時或已關閉的選項。  
3. **用戶意圖**：  
   - 代理應推斷用戶查詢背後的意圖，以提供最相關的信息。  
   - 範例：如果用戶詢問「經濟型酒店」，代理應優先考慮價格實惠的選項。  
4. **反饋迴路**：  
   - 持續收集和分析用戶反饋，有助於代理完善其相關性評估過程。  
   - 範例：將用戶對先前推薦的評分和反饋納入，改進未來的回應。  

#### 評估相關性的實用技術  
1. **相關性評分**：  
   - 根據與用戶查詢和偏好的匹配程度，為每個檢索項分配相關性分數。  
   - 範例：```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```  
2. **篩選和排序**：  
   - 篩選掉不相關的項目，並根據相關性分數對剩餘項目進行排序。  
   - 範例：```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Return top 10 relevant items
     ```  
3. **自然語言處理（NLP）**：  
   - 使用 NLP 技術來理解用戶查詢並檢索相關信息。  
   - 範例：```python
     def process_query(query):
         # Use NLP to extract key information from the user's query
         processed_query = nlp(query)
         return processed_query
     ```  
4. **用戶反饋集成**：  
   - 收集用戶對推薦的反饋，並用於調整未來的相關性評估。  
   - 範例：```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```  

#### 範例：在旅遊代理中評估相關性  
以下是一個展示旅遊代理如何評估旅行推薦相關性的實用範例：  
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
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Return top 10 relevant items

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

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
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```  

### 帶有意圖的搜索  
帶有意圖的搜索是指理解和解釋用戶查詢背後的潛在目的或目標，以檢索和生成最相關且有用的信息。這種方法超越了簡單的關鍵詞匹配，專注於掌握用戶的實際需求和上下文。  

#### 帶有意圖的搜索的關鍵概念  
1. **理解用戶意圖**：  
   - 用戶意圖可以分為三種主要類型：資訊性、導航性和交易性。  
   - **資訊性意圖**：用戶尋求有關某個主題的信息（例如，「什麼是...」）。  
```
巴黎最好的博物館？"). - **導航意圖**：用戶希望導航到特定網站或頁面（例如，“盧浮宮官方網站”）。 - **交易意圖**：用戶旨在執行交易，例如預訂航班或進行購買（例如，“預訂飛往巴黎的航班”）。  

2. **上下文意識**：  
   - 分析用戶查詢的上下文有助於準確識別其意圖。這包括考慮之前的互動、用戶偏好以及當前查詢的具體細節。  

3. **自然語言處理 (NLP)**：  
   - 採用 NLP 技術來理解和解釋用戶提供的自然語言查詢。這包括實體識別、情感分析和查詢解析等任務。  

4. **個性化**：  
   - 根據用戶的歷史記錄、偏好和反饋來個性化搜索結果，提高檢索信息的相關性。  

#### 實用示例：在旅遊代理中基於意圖的搜索  
讓我們以旅遊代理為例，看看如何實現基於意圖的搜索。  

1. **收集用戶偏好**  
   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```  

2. **理解用戶意圖**  
   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```  

3. **上下文意識**  
   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```  

4. **搜索並個性化結果**  
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

5. **示例使用**  
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

## 4. 作為工具的代碼生成  
代碼生成代理使用 AI 模型編寫和執行代碼，解決複雜問題並自動化任務。  

### 代碼生成代理  
代碼生成代理利用生成式 AI 模型來編寫和執行代碼。這些代理可以通過生成和運行多種編程語言的代碼來解決複雜問題、自動化任務並提供有價值的見解。  

#### 實用應用  
1. **自動代碼生成**：為特定任務生成代碼片段，例如數據分析、網頁抓取或機器學習。  
2. **SQL 作為 RAG**：使用 SQL 查詢從數據庫檢索和操作數據。  
3. **問題解決**：創建並執行代碼以解決特定問題，例如優化算法或分析數據。  

#### 示例：數據分析的代碼生成代理  
假設您正在設計一個代碼生成代理。以下是其工作方式：  

1. **任務**：分析數據集以識別趨勢和模式。  
2. **步驟**：  
   - 將數據集加載到數據分析工具中。  
   - 生成 SQL 查詢以篩選和聚合數據。  
   - 執行查詢並檢索結果。  
   - 使用結果生成可視化和見解。  
3. **所需資源**：訪問數據集、數據分析工具和 SQL 功能。  
4. **經驗**：利用過去的分析結果來提高未來分析的準確性和相關性。  

### 示例：旅遊代理的代碼生成代理  
在此示例中，我們將設計一個代碼生成代理（旅遊代理），以通過生成和執行代碼來協助用戶規劃旅行。該代理可以處理例如獲取旅行選項、篩選結果和使用生成式 AI 編制行程的任務。  

#### 代碼生成代理概述  
1. **收集用戶偏好**：收集用戶輸入，如目的地、旅行日期、預算和興趣。  
2. **生成代碼以獲取數據**：生成代碼片段以檢索有關航班、酒店和景點的信息。  
3. **執行生成的代碼**：運行生成的代碼以獲取實時信息。  
4. **生成行程**：將檢索到的數據編制成個性化旅行計劃。  
5. **基於反饋進行調整**：接收用戶反饋，並在必要時重新生成代碼以優化結果。  

#### 分步實現  
1. **收集用戶偏好**  
   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```  

2. **生成代碼以獲取數據**  
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

3. **執行生成的代碼**  
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

4. **生成行程**  
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

5. **基於反饋進行調整**  
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

### 利用環境感知和推理  
基於表格的架構確實可以通過利用環境感知和推理來增強查詢生成過程。以下是如何實現的示例：  

1. **理解架構**：系統將理解表格的架構並利用此信息來支持查詢生成。  
2. **基於反饋進行調整**：系統將根據反饋調整用戶偏好，並推理需要在架構中更新的字段。  
3. **生成和執行查詢**：系統將生成並執行查詢以根據新偏好檢索更新的航班和酒店數據。  

以下是包含這些概念的更新 Python 代碼示例：  
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

#### 解釋 - 基於反饋進行預訂  
1. **架構感知**：  
   `schema` dictionary defines how preferences should be adjusted based on feedback. It includes fields like `favorites` and `avoid`, with corresponding adjustments.
2. **Adjusting Preferences (`adjust_based_on_feedback` method)**: This method adjusts preferences based on user feedback and the schema.
3. **Environment-Based Adjustments (`adjust_based_on_environment` 方法**：此方法根據架構和反饋定制調整。  
4. **生成和執行查詢**：系統生成代碼以根據調整後的偏好檢索更新的航班和酒店數據，並模擬執行這些查詢。  
5. **生成行程**：系統基於新的航班、酒店和景點數據創建更新的行程。  

通過使系統具備環境感知並基於架構進行推理，它可以生成更準確和相關的查詢，從而提供更好的旅行建議和更個性化的用戶體驗。  

### 使用 SQL 作為檢索增強生成 (RAG) 技術  
SQL（結構化查詢語言）是與數據庫交互的強大工具。作為檢索增強生成 (RAG) 方法的一部分，SQL 可以從數據庫檢索相關數據，以在 AI 代理中生成響應或執行操作。讓我們探索在旅遊代理上下文中如何使用 SQL 作為 RAG 技術。  

#### 關鍵概念  
1. **數據庫交互**：  
   - 使用 SQL 查詢數據庫，檢索相關信息並操作數據。  
   - 示例：從旅遊數據庫中檢索航班詳情、酒店信息和景點。  
2. **與 RAG 集成**：  
   - 根據用戶輸入和偏好生成 SQL 查詢。  
   - 然後使用檢索到的數據生成個性化建議或操作。  
3. **動態查詢生成**：  
   - AI 代理根據上下文和用戶需求生成動態 SQL 查詢。  
   - 示例：定制 SQL 查詢以根據預算、日期和興趣篩選結果。  

#### 應用  
- **自動代碼生成**：為特定任務生成代碼片段。  
- **SQL 作為 RAG**：使用 SQL 查詢操作數據。  
- **問題解決**：創建並執行代碼以解決問題。  

**示例**：數據分析代理：  
1. **任務**：分析數據集以發現趨勢。  
2. **步驟**：  
   - 加載數據集。  
   - 生成 SQL 查詢以篩選數據。  
   - 執行查詢並檢索結果。  
   - 生成可視化和見解。  
3. **資源**：數據集訪問權限、SQL 功能。  
4. **經驗**：利用過去的結果改進未來分析。  

#### 實用示例：在旅遊代理中使用 SQL  
1. **收集用戶偏好**  
   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```  

2. **生成 SQL 查詢**  
   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```  

3. **執行 SQL 查詢**  
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

4. **生成推薦**  
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

#### 示例 SQL 查詢  
1. **航班查詢**  
   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```  

2. **酒店查詢**  
   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```  

3. **景點查詢**  
   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```  

通過將 SQL 作為檢索增強生成 (RAG) 技術的一部分，像旅遊代理這樣的 AI 代理可以動態檢索並利用相關數據，提供準確且個性化的建議。  

### 結論  
元認知是一種強大的工具，可以顯著增強 AI 代理的能力。通過納入元認知過程，您可以設計出更智能、更適應性和更高效的代理。利用額外資源進一步探索 AI 代理中元認知的迷人世界。  

**免責聲明**:  
本文件使用基於機器的人工智能翻譯服務進行翻譯。我們雖然致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。