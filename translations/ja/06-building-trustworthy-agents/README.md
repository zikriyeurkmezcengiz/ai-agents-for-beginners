# 信頼できるAIエージェントの構築

## はじめに

このレッスンでは以下について学びます:

- 安全で効果的なAIエージェントの構築と展開方法
- AIエージェントを開発する際の重要なセキュリティ考慮事項
- AIエージェントを開発する際にデータとユーザーのプライバシーを維持する方法

## 学習目標

このレッスンを修了すると、次のことができるようになります:

- AIエージェントを作成する際のリスクを特定し、軽減する方法を理解する。
- データとアクセスが適切に管理されるようにセキュリティ対策を実装する。
- データのプライバシーを保護し、質の高いユーザー体験を提供するAIエージェントを作成する。

## 安全性

まず、安全なエージェントアプリケーションを構築する方法を見ていきましょう。安全性とは、AIエージェントが設計どおりに動作することを意味します。エージェントアプリケーションを構築する開発者として、安全性を最大化するための方法やツールがあります。

### メタプロンプトシステムの構築

大規模言語モデル（LLM）を使用してAIアプリケーションを構築した経験がある方は、堅牢なシステムプロンプトやシステムメッセージを設計することの重要性をご存じでしょう。これらのプロンプトは、LLMがユーザーやデータとどのようにやり取りするかの基本ルール、指示、ガイドラインを確立します。

AIエージェントの場合、システムプロンプトはさらに重要です。AIエージェントは設計されたタスクを完了するために、非常に具体的な指示を必要とするからです。

スケーラブルなシステムプロンプトを作成するために、アプリケーション内で1つ以上のエージェントを構築するためのメタプロンプトシステムを使用できます。

![メタプロンプトシステムの構築](../../../translated_images/building-a-metaprompting-system.aa7d6de2100b0ef48c3e1926dab6903026b22fc9d27fc4327162fbbb9caf960f.ja.png)

#### ステップ 1: メタまたはテンプレートプロンプトを作成する

メタプロンプトは、作成するエージェントのシステムプロンプトを生成するためにLLMによって使用されます。これをテンプレートとして設計することで、必要に応じて複数のエージェントを効率的に作成できます。

以下はLLMに与えるメタプロンプトの例です:

```plaintext
You are an expert at creating AI agent assitants. 
You will be provided a company name, role, responsibilites and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilites of the AI assistant. 
```

#### ステップ 2: 基本プロンプトを作成する

次に、AIエージェントを説明する基本プロンプトを作成します。エージェントの役割、完了するタスク、その他の責任を含める必要があります。

以下はその例です:

```plaintext
You are a travel agent for Contoso Travel with that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### ステップ 3: 基本プロンプトをLLMに提供する

次に、メタプロンプトをシステムプロンプトとして使用し、基本プロンプトを提供することで、このプロンプトを最適化します。

これにより、AIエージェントを導くためにより適切に設計されたプロンプトが生成されます:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### ステップ 4: 繰り返し改善する

このメタプロンプトシステムの価値は、複数のエージェントのプロンプトを簡単に作成できるだけでなく、時間とともにプロンプトを改善できる点にあります。最初から完全なユースケースに適したプロンプトが得られることは稀です。基本プロンプトを少し変更してシステムを通して実行することで、結果を比較評価し、改善を重ねることができます。

## 脅威の理解  

信頼できるAIエージェントを構築するためには、AIエージェントに対するリスクや脅威を理解し、それを軽減することが重要です。ここでは、AIエージェントに対するさまざまな脅威の一部と、それに対する計画と準備の方法を見ていきます。

![脅威の理解](../../../translated_images/understanding-threats.f8fbe6fe11e025b3085fc91e82d975937ad1d672260a2aeed40458aa41798d0e.ja.png)

### タスクと指示

**説明:** 攻撃者がプロンプトや入力を操作することで、AIエージェントの指示や目標を変更しようとする。

**軽減策:** 危険なプロンプトをAIエージェントが処理する前に検出するための検証チェックや入力フィルタを実行します。この種の攻撃は通常、エージェントとの頻繁なやり取りを必要とするため、会話のターン数を制限することも防止策の一つです。

### 重要なシステムへのアクセス

**説明:** AIエージェントが機密データを保存するシステムやサービスにアクセスできる場合、攻撃者はこれらのサービスとエージェント間の通信を侵害する可能性があります。これには直接的な攻撃や、エージェントを通じた間接的な情報収集が含まれます。

**軽減策:** AIエージェントは必要最小限のシステムにのみアクセスできるようにし、これらの攻撃を防ぎます。また、エージェントとシステム間の通信を安全に保つ必要があります。認証やアクセス制御を実装することも、この情報を保護する方法の一つです。

### リソースとサービスの過負荷

**説明:** AIエージェントはタスクを完了するためにさまざまなツールやサービスにアクセスします。攻撃者はこの能力を利用して、高頻度のリクエストをAIエージェント経由で送信し、システムの障害や高コストを引き起こす可能性があります。

**軽減策:** AIエージェントがサービスに送信できるリクエスト数を制限するポリシーを実装します。また、会話のターン数やエージェントへのリクエスト数を制限することも、この種の攻撃を防ぐ方法です。

### ナレッジベースの汚染

**説明:** この種の攻撃はAIエージェントそのものではなく、エージェントが使用するナレッジベースや他のサービスを標的とします。これには、エージェントがタスクを完了するために使用するデータや情報を改ざんし、ユーザーに偏ったまたは意図しない応答を返すことが含まれます。

**軽減策:** AIエージェントがワークフローで使用するデータを定期的に検証します。また、このデータへのアクセスを安全に保ち、信頼できる人物のみが変更できるようにします。

### エラーの連鎖

**説明:** AIエージェントはタスクを完了するためにさまざまなツールやサービスにアクセスします。攻撃者によるエラーが、エージェントが接続する他のシステムの障害を引き起こし、攻撃がより広範囲に広がり、トラブルシューティングが困難になる可能性があります。

**軽減策:** AIエージェントが直接システムを攻撃されないように、Dockerコンテナ内でタスクを実行するなどの制限された環境で動作させる方法があります。また、特定のシステムがエラーを返した場合にフォールバックメカニズムやリトライロジックを作成することも、大規模なシステム障害を防ぐ手段です。

## ヒューマンインザループ

信頼性の高いAIエージェントシステムを構築するもう一つの効果的な方法は、ヒューマンインザループを使用することです。これにより、ユーザーが実行中のプロセスに対してフィードバックを提供できるフローが作成されます。ユーザーはマルチエージェントシステム内のエージェントとして機能し、プロセスの承認または終了を行います。

![ヒューマンインザループ](../../../translated_images/human-in-the-loop.e9edbe8f6d42041b4213421410823250aa750fe8bdba5601d69ed46f3ff6489d.ja.png)

以下は、AutoGenを使用してこの概念を実装するコードスニペットです:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

**免責事項**:  
本書類は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳にはエラーや不正確さが含まれる可能性があることをご承知おきください。原文（原言語）が信頼できる正式な情報源として優先されるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。