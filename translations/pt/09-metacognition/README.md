```markdown
# Metacognição em Agentes de IA

## Introdução

Bem-vindo à lição sobre metacognição em agentes de IA! Este capítulo foi projetado para iniciantes curiosos sobre como agentes de IA podem pensar sobre seus próprios processos de pensamento. Ao final desta lição, você entenderá os conceitos-chave e estará equipado com exemplos práticos para aplicar metacognição no design de agentes de IA.

## Objetivos de Aprendizagem

Após completar esta lição, você será capaz de:

1. Compreender as implicações de loops de raciocínio em definições de agentes.
2. Usar técnicas de planejamento e avaliação para ajudar agentes a se autocorrigirem.
3. Criar seus próprios agentes capazes de manipular código para realizar tarefas.

## Introdução à Metacognição

Metacognição refere-se aos processos cognitivos de ordem superior que envolvem pensar sobre o próprio pensamento. Para agentes de IA, isso significa ser capaz de avaliar e ajustar suas ações com base na autoconsciência e em experiências passadas.

### O que é Metacognição?

Metacognição, ou "pensar sobre o pensamento", é um processo cognitivo de ordem superior que envolve autoconsciência e autorregulação dos próprios processos cognitivos. No domínio da IA, a metacognição capacita agentes a avaliar e adaptar suas estratégias e ações, levando a capacidades aprimoradas de resolução de problemas e tomada de decisão. Ao entender a metacognição, você pode projetar agentes de IA que sejam não apenas mais inteligentes, mas também mais adaptáveis e eficientes.

### Importância da Metacognição em Agentes de IA

A metacognição desempenha um papel crucial no design de agentes de IA por várias razões:

![Importância da Metacognição](../../../09-metacognition/images/importance-of-metacognition.png)

- **Autorreflexão**: Agentes podem avaliar seu próprio desempenho e identificar áreas para melhoria.
- **Adaptabilidade**: Agentes podem modificar suas estratégias com base em experiências passadas e ambientes em mudança.
- **Correção de Erros**: Agentes podem detectar e corrigir erros de forma autônoma, levando a resultados mais precisos.
- **Gestão de Recursos**: Agentes podem otimizar o uso de recursos, como tempo e poder computacional, planejando e avaliando suas ações.

## Componentes de um Agente de IA

Antes de mergulhar nos processos metacognitivos, é essencial entender os componentes básicos de um agente de IA. Um agente de IA normalmente consiste em:

- **Persona**: A personalidade e características do agente, que definem como ele interage com os usuários.
- **Ferramentas**: As capacidades e funções que o agente pode executar.
- **Habilidades**: O conhecimento e a expertise que o agente possui.

Esses componentes trabalham juntos para criar uma "unidade de expertise" que pode realizar tarefas específicas.

**Exemplo**: Considere um agente de viagens, que não apenas planeja suas férias, mas também ajusta seu percurso com base em dados em tempo real e experiências de jornadas de clientes anteriores.

### Exemplo: Metacognição em um Serviço de Agente de Viagens

Imagine que você está projetando um serviço de agente de viagens movido por IA. Este agente, "Agente de Viagens", auxilia os usuários no planejamento de suas férias. Para incorporar metacognição, o Agente de Viagens precisa avaliar e ajustar suas ações com base na autoconsciência e em experiências passadas. Veja como a metacognição pode desempenhar um papel:

#### Tarefa Atual

A tarefa atual é ajudar um usuário a planejar uma viagem para Paris.

#### Etapas para Completar a Tarefa

1. **Coletar Preferências do Usuário**: Perguntar ao usuário sobre suas datas de viagem, orçamento, interesses (por exemplo, museus, culinária, compras) e quaisquer requisitos específicos.
2. **Recuperar Informações**: Buscar opções de voos, acomodações, atrações e restaurantes que correspondam às preferências do usuário.
3. **Gerar Recomendações**: Fornecer um itinerário personalizado com detalhes de voos, reservas de hotéis e atividades sugeridas.
4. **Ajustar com Base no Feedback**: Solicitar feedback do usuário sobre as recomendações e fazer os ajustes necessários.

#### Recursos Necessários

- Acesso a bancos de dados de reservas de voos e hotéis.
- Informações sobre atrações e restaurantes em Paris.
- Dados de feedback de usuários de interações anteriores.

#### Experiência e Autorreflexão

O Agente de Viagens usa metacognição para avaliar seu desempenho e aprender com experiências passadas. Por exemplo:

1. **Analisando Feedback do Usuário**: O Agente de Viagens revisa o feedback do usuário para determinar quais recomendações foram bem recebidas e quais não foram. Ele ajusta suas sugestões futuras de acordo.
2. **Adaptabilidade**: Se um usuário mencionou anteriormente que não gosta de lugares lotados, o Agente de Viagens evitará recomendar pontos turísticos populares durante horários de pico no futuro.
3. **Correção de Erros**: Se o Agente de Viagens cometeu um erro em uma reserva anterior, como sugerir um hotel que estava totalmente reservado, ele aprende a verificar a disponibilidade de forma mais rigorosa antes de fazer recomendações.

#### Exemplo Prático para Desenvolvedores

Aqui está um exemplo simplificado de como o código do Agente de Viagens poderia ser estruturado ao incorporar metacognição:

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

#### Por que a Metacognição é Importante

- **Autorreflexão**: Agentes podem analisar seu desempenho e identificar áreas para melhoria.
- **Adaptabilidade**: Agentes podem modificar estratégias com base em feedback e condições em mudança.
- **Correção de Erros**: Agentes podem detectar e corrigir erros de forma autônoma.
- **Gestão de Recursos**: Agentes podem otimizar o uso de recursos, como tempo e poder computacional.

Ao incorporar metacognição, o Agente de Viagens pode fornecer recomendações de viagem mais personalizadas e precisas, melhorando a experiência geral do usuário.

---

## 2. Planejamento em Agentes

Planejamento é um componente crítico do comportamento de agentes de IA. Envolve delinear os passos necessários para alcançar um objetivo, considerando o estado atual, recursos e possíveis obstáculos.

### Elementos do Planejamento

- **Tarefa Atual**: Definir claramente a tarefa.
- **Etapas para Completar a Tarefa**: Dividir a tarefa em etapas gerenciáveis.
- **Recursos Necessários**: Identificar os recursos necessários.
- **Experiência**: Utilizar experiências passadas para informar o planejamento.

**Exemplo**: Aqui estão os passos que o Agente de Viagens precisa seguir para ajudar um usuário a planejar sua viagem de forma eficaz:

### Etapas para o Agente de Viagens

1. **Coletar Preferências do Usuário**  
   - Perguntar ao usuário detalhes sobre suas datas de viagem, orçamento, interesses e quaisquer requisitos específicos.  
   - Exemplos: "Quando você planeja viajar?" "Qual é a sua faixa de orçamento?" "Quais atividades você gosta de fazer nas férias?"

2. **Recuperar Informações**  
   - Buscar opções de viagem relevantes com base nas preferências do usuário.  
   - **Voos**: Procurar voos disponíveis dentro do orçamento e datas preferidas do usuário.  
   - **Acomodações**: Encontrar hotéis ou propriedades para aluguel que correspondam às preferências do usuário em localização, preço e comodidades.  
   - **Atrações e Restaurantes**: Identificar atrações populares, atividades e opções de refeições que estejam alinhadas com os interesses do usuário.

3. **Gerar Recomendações**  
   - Compilar as informações recuperadas em um itinerário personalizado.  
   - Fornecer detalhes como opções de voos, reservas de hotéis e atividades sugeridas, garantindo que as recomendações sejam adaptadas às preferências do usuário.

4. **Apresentar o Itinerário ao Usuário**  
   - Compartilhar o itinerário proposto com o usuário para sua revisão.  
   - Exemplo: "Aqui está um itinerário sugerido para sua viagem a Paris. Inclui detalhes de voos, reservas de hotéis e uma lista de atividades e restaurantes recomendados. Deixe-me saber o que acha!"

5. **Coletar Feedback**  
   - Perguntar ao usuário sobre o itinerário proposto.  
   - Exemplos: "Você gostou das opções de voos?" "O hotel é adequado às suas necessidades?" "Há alguma atividade que você gostaria de adicionar ou remover?"

6. **Ajustar com Base no Feedback**  
   - Modificar o itinerário com base no feedback do usuário.  
   - Fazer as alterações necessárias nas recomendações de voos, acomodações e atividades para melhor atender às preferências do usuário.

7. **Confirmação Final**  
   - Apresentar o itinerário atualizado ao usuário para confirmação final.  
   - Exemplo: "Fiz os ajustes com base no seu feedback. Aqui está o itinerário atualizado. Tudo parece bom para você?"

8. **Reservar e Confirmar**  
   - Após a aprovação do usuário, proceder com a reserva de voos, acomodações e quaisquer atividades pré-planejadas.  
   - Enviar os detalhes de confirmação ao usuário.

9. **Fornecer Suporte Contínuo**  
   - Permanecer disponível para ajudar o usuário com quaisquer alterações ou solicitações adicionais antes e durante a viagem.  
   - Exemplo: "Se precisar de mais assistência durante sua viagem, sinta-se à vontade para entrar em contato comigo a qualquer momento!"

### Exemplo de Interação

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
```
```markdown
O Agente de Viagens formula novas consultas de pesquisa com base no feedback do usuário.  
- Exemplo: ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```  
- **Ferramenta**: O Agente de Viagens utiliza algoritmos para classificar e filtrar novos resultados de pesquisa, enfatizando a relevância com base no feedback do usuário.  
- Exemplo: ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```  
- **Avaliação**: O Agente de Viagens avalia continuamente a relevância e a precisão de suas recomendações, analisando o feedback do usuário e fazendo os ajustes necessários.  
- Exemplo: ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```  

#### Exemplo Prático  
Aqui está um exemplo simplificado de código Python que incorpora a abordagem RAG Corretiva no Agente de Viagens:  
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

### Carregamento de Contexto Pré-Emptivo  
O Carregamento de Contexto Pré-Emptivo envolve carregar informações de contexto ou antecedentes relevantes no modelo antes de processar uma consulta. Isso significa que o modelo tem acesso a essas informações desde o início, o que pode ajudá-lo a gerar respostas mais informadas sem a necessidade de recuperar dados adicionais durante o processo.  

Aqui está um exemplo simplificado de como um carregamento de contexto pré-emptivo pode ser implementado em uma aplicação de agente de viagens em Python:  
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

#### Explicação  
1. **Inicialização (`__init__` method)**: The `TravelAgent` class pre-loads a dictionary containing information about popular destinations such as Paris, Tokyo, New York, and Sydney. This dictionary includes details like the country, currency, language, and major attractions for each destination.

2. **Retrieving Information (`get_destination_info` method)**: When a user queries about a specific destination, the `get_destination_info` method)**: Este método busca as informações relevantes no dicionário de contexto pré-carregado. Ao pré-carregar o contexto, a aplicação do agente de viagens pode responder rapidamente às consultas do usuário sem precisar recuperar essas informações de uma fonte externa em tempo real. Isso torna a aplicação mais eficiente e responsiva.  

### Inicializando o Plano com um Objetivo Antes de Iterar  
Inicializar um plano com um objetivo envolve começar com um objetivo claro ou resultado desejado em mente. Definindo esse objetivo desde o início, o modelo pode usá-lo como um princípio orientador ao longo do processo iterativo. Isso ajuda a garantir que cada iteração avance em direção ao resultado desejado, tornando o processo mais eficiente e focado.  

Aqui está um exemplo de como você pode inicializar um plano de viagem com um objetivo antes de iterar para um agente de viagens em Python:  

### Cenário  
Um agente de viagens deseja planejar umas férias personalizadas para um cliente. O objetivo é criar um itinerário de viagem que maximize a satisfação do cliente com base em suas preferências e orçamento.  

### Etapas  
1. Defina as preferências e o orçamento do cliente.  
2. Inicialize o plano inicial com base nessas preferências.  
3. Itere para refinar o plano, otimizando a satisfação do cliente.  

#### Código Python  
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

#### Explicação do Código  
1. **Inicialização (`__init__` method)**: The `TravelAgent` class is initialized with a list of potential destinations, each having attributes like name, cost, and activity type.

2. **Bootstrapping the Plan (`bootstrap_plan` method)**: This method creates an initial travel plan based on the client's preferences and budget. It iterates through the list of destinations and adds them to the plan if they match the client's preferences and fit within the budget.

3. **Matching Preferences (`match_preferences` method)**: This method checks if a destination matches the client's preferences.

4. **Iterating the Plan (`iterate_plan` method)**: This method refines the initial plan by trying to replace each destination in the plan with a better match, considering the client's preferences and budget constraints.

5. **Calculating Cost (`calculate_cost` method)**: Este método calcula o custo total do plano atual, incluindo um possível novo destino.  

#### Uso de Exemplo  
- **Plano Inicial**: O agente de viagens cria um plano inicial com base nas preferências do cliente por pontos turísticos e um orçamento de $2000.  
- **Plano Refinado**: O agente de viagens itera o plano, otimizando para as preferências e o orçamento do cliente.  

Ao inicializar o plano com um objetivo claro (por exemplo, maximizar a satisfação do cliente) e iterar para refiná-lo, o agente de viagens pode criar um itinerário de viagem personalizado e otimizado para o cliente. Essa abordagem garante que o plano de viagem esteja alinhado com as preferências e o orçamento do cliente desde o início e melhore a cada iteração.  

### Aproveitando LLM para Reclassificação e Pontuação  
Modelos de Linguagem de Grande Escala (LLMs) podem ser usados para reclassificação e pontuação ao avaliar a relevância e a qualidade de documentos recuperados ou respostas geradas. Veja como funciona:  

**Recuperação:** A etapa inicial de recuperação busca um conjunto de documentos ou respostas candidatas com base na consulta.  
**Reclassificação:** O LLM avalia esses candidatos e os reclassifica com base em sua relevância e qualidade. Essa etapa garante que as informações mais relevantes e de alta qualidade sejam apresentadas primeiro.  
**Pontuação:** O LLM atribui pontuações a cada candidato, refletindo sua relevância e qualidade. Isso ajuda na seleção da melhor resposta ou documento para o usuário.  

Ao aproveitar os LLMs para reclassificação e pontuação, o sistema pode fornecer informações mais precisas e contextualmente relevantes, melhorando a experiência geral do usuário.  

Aqui está um exemplo de como um agente de viagens pode usar um Modelo de Linguagem de Grande Escala (LLM) para reclassificar e pontuar destinos de viagem com base nas preferências do usuário em Python:  

#### Cenário - Viagem com Base nas Preferências  
Um agente de viagens deseja recomendar os melhores destinos de viagem para um cliente com base em suas preferências. O LLM ajudará a reclassificar e pontuar os destinos para garantir que as opções mais relevantes sejam apresentadas.  

#### Etapas:  
1. Coletar as preferências do usuário.  
2. Recuperar uma lista de destinos de viagem potenciais.  
3. Usar o LLM para reclassificar e pontuar os destinos com base nas preferências do usuário.  

Aqui está como você pode atualizar o exemplo anterior para usar os Serviços Azure OpenAI:  

#### Requisitos  
1. Você precisa de uma assinatura do Azure.  
2. Criar um recurso Azure OpenAI e obter sua chave de API.  

#### Código Python de Exemplo  
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

#### Explicação do Código - Preference Booker  
1. **Inicialização**: Substitua `TravelAgent` class is initialized with a list of potential travel destinations, each having attributes like name and description.

2. **Getting Recommendations (`get_recommendations` method)**: This method generates a prompt for the Azure OpenAI service based on the user's preferences and makes an HTTP POST request to the Azure OpenAI API to get re-ranked and scored destinations.

3. **Generating Prompt (`generate_prompt` method)**: This method constructs a prompt for the Azure OpenAI, including the user's preferences and the list of destinations. The prompt guides the model to re-rank and score the destinations based on the provided preferences.

4. **API Call**: The `requests` library is used to make an HTTP POST request to the Azure OpenAI API endpoint. The response contains the re-ranked and scored destinations.

5. **Example Usage**: The travel agent collects user preferences (e.g., interest in sightseeing and diverse culture) and uses the Azure OpenAI service to get re-ranked and scored recommendations for travel destinations.

Make sure to replace `your_azure_openai_api_key` with your actual Azure OpenAI API key and `https://your-endpoint.com/...` pela URL do endpoint real de sua implantação do Azure OpenAI.  

Ao aproveitar o LLM para reclassificação e pontuação, o agente de viagens pode fornecer recomendações de viagem mais personalizadas e relevantes para os clientes, melhorando sua experiência geral.  

### RAG: Técnica de Prompt vs Ferramenta  
A Geração Incrementada por Recuperação (RAG) pode ser tanto uma técnica de prompt quanto uma ferramenta no desenvolvimento de agentes de IA. Compreender a distinção entre os dois pode ajudá-lo a aproveitar o RAG de forma mais eficaz em seus projetos.  

#### RAG como Técnica de Prompt  
**O que é?**  
- Como técnica de prompt, o RAG envolve a formulação de consultas ou prompts específicos para guiar a recuperação de informações relevantes de um grande corpus ou banco de dados. Essas informações são então usadas para gerar respostas ou ações.  

**Como funciona:**  
1. **Formular Prompts**: Crie prompts ou consultas bem estruturados com base na tarefa ou na entrada do usuário.  
2. **Recuperar Informações**: Use os prompts para buscar dados relevantes de uma base de conhecimento ou conjunto de dados preexistente.  
3. **Gerar Resposta**: Combine as informações recuperadas com modelos de IA generativos para produzir uma resposta abrangente e coerente.  

**Exemplo em Agente de Viagens**:  
- Entrada do Usuário: "Quero visitar museus em Paris."  
- Prompt: "Encontre os principais museus em Paris."  
- Informações Recuperadas: Detalhes sobre o Museu do Louvre, Musée d'Orsay, etc.  
- Resposta Gerada: "Aqui estão alguns dos principais museus em Paris: Museu do Louvre, Musée d'Orsay e Centro Pompidou."  

#### RAG como Ferramenta  
**O que é?**  
- Como ferramenta, o RAG é um sistema integrado que automatiza o processo de recuperação e geração, facilitando a implementação de funcionalidades complexas de IA sem a necessidade de criar prompts manualmente para cada consulta.  

**Como funciona:**  
1. **Integração**: Incorpore o RAG na arquitetura do agente de IA, permitindo que ele lide automaticamente com as tarefas de recuperação e geração.  
2. **Automação**: A ferramenta gerencia todo o processo, desde receber a entrada do usuário até gerar a resposta final, sem exigir prompts explícitos para cada etapa.  
3. **Eficiência**: Melhora o desempenho do agente ao simplificar o processo de recuperação e geração, permitindo respostas mais rápidas e precisas.  

**Exemplo em Agente de Viagens**:  
- Entrada do Usuário: "Quero visitar museus em Paris."  
- Ferramenta RAG: Recupera automaticamente informações sobre museus e gera uma resposta.  
- Resposta Gerada: "Aqui estão alguns dos principais museus em Paris: Museu do Louvre, Musée d'Orsay e Centro Pompidou."  

### Comparação  
| Aspecto                | Técnica de Prompt                                         | Ferramenta                                           |  
|------------------------|----------------------------------------------------------|-----------------------------------------------------|  
| **Manual vs Automático** | Formulação manual de prompts para cada consulta.         | Processo automatizado para recuperação e geração.   |  
| **Controle**           | Oferece mais controle sobre o processo de recuperação.    | Simplifica e automatiza a recuperação e geração.    |  
| **Flexibilidade**      | Permite prompts personalizados com base em necessidades específicas. | Mais eficiente para implementações em larga escala. |  
| **Complexidade**       | Requer criação e ajuste de prompts.                       | Mais fácil de integrar na arquitetura de um agente de IA. |  

### Exemplos Práticos  
**Exemplo de Técnica de Prompt:**  
```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```  

**Exemplo de Ferramenta:**  
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

### Avaliando Relevância  
Avaliar relevância é um aspecto crucial do desempenho de agentes de IA. Isso garante que as informações recuperadas e geradas pelo agente sejam apropriadas, precisas e úteis para o usuário. Vamos explorar como avaliar relevância em agentes de IA, incluindo exemplos práticos e técnicas.  

#### Conceitos-Chave na Avaliação de Relevância  
1. **Consciência de Contexto**:  
   - O agente deve entender o contexto da consulta do usuário para recuperar e gerar informações relevantes.  
   - Exemplo: Se um usuário perguntar "melhores restaurantes em Paris", o agente deve considerar as preferências do usuário, como tipo de cozinha e orçamento.  
2. **Precisão**:  
   - As informações fornecidas pelo agente devem ser factualmente corretas e atualizadas.  
   - Exemplo: Recomendar restaurantes abertos atualmente com boas avaliações em vez de opções desatualizadas ou fechadas.  
3. **Intenção do Usuário**:  
   - O agente deve inferir a intenção do usuário por trás da consulta para fornecer as informações mais relevantes.  
   - Exemplo: Se um usuário perguntar por "hotéis econômicos", o agente deve priorizar opções acessíveis.  
4. **Ciclo de Feedback**:  
   - Coletar e analisar continuamente o feedback do usuário ajuda o agente a refinar seu processo de avaliação de relevância.  
   - Exemplo: Incorporar classificações e feedback de usuários sobre recomendações anteriores para melhorar respostas futuras.  

#### Técnicas Práticas para Avaliação de Relevância  
1. **Pontuação de Relevância**:  
   - Atribuir uma pontuação de relevância a cada item recuperado com base em quão bem ele corresponde à consulta e preferências do usuário.  
   - Exemplo: ```python
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
2. **Filtragem e Classificação**:  
   - Filtrar itens irrelevantes e classificar os restantes com base em suas pontuações de relevância.  
   - Exemplo: ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Return top 10 relevant items
     ```  
3. **Processamento de Linguagem Natural (NLP)**:  
   - Usar técnicas de NLP para entender a consulta do usuário e recuperar informações relevantes.  
   - Exemplo: ```python
     def process_query(query):
         # Use NLP to extract key information from the user's query
         processed_query = nlp(query)
         return processed_query
     ```  
4. **Integração de Feedback do Usuário**:  
   - Coletar feedback do usuário sobre as recomendações fornecidas e usá-lo para ajustar avaliações futuras de relevância.  
   - Exemplo: ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```  

#### Exemplo: Avaliando Relevância no Agente de Viagens  
Aqui está um exemplo prático de como o Agente de Viagens pode avaliar a relevância de recomendações de viagem:  
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

### Pesquisa com Intenção  
Pesquisar com intenção envolve entender e interpretar o propósito ou objetivo subjacente à consulta do usuário para recuperar e gerar as informações mais relevantes e úteis. Essa abordagem vai além de simplesmente corresponder palavras-chave, focando em compreender as reais necessidades e contexto do usuário.  

#### Conceitos-Chave na Pesquisa com Intenção  
1. **Compreensão da Intenção do Usuário**:  
   - A intenção do usuário pode ser categorizada em três tipos principais: informacional, navegacional e transacional.  
   - **Intenção Informacional**: O usuário busca informações sobre um tópico (ex.: "Quais são...").  
```
```markdown
os melhores museus em Paris?"). - **Intenção de Navegação**: O usuário deseja navegar para um site ou página específica (por exemplo, "site oficial do Museu do Louvre"). - **Intenção Transacional**: O usuário pretende realizar uma transação, como reservar um voo ou fazer uma compra (por exemplo, "Reservar um voo para Paris"). 2. **Consciência de Contexto**: - Analisar o contexto da consulta do usuário ajuda a identificar com precisão sua intenção. Isso inclui considerar interações anteriores, preferências do usuário e os detalhes específicos da consulta atual. 3. **Processamento de Linguagem Natural (PLN)**: - Técnicas de PLN são empregadas para entender e interpretar as consultas em linguagem natural fornecidas pelos usuários. Isso inclui tarefas como reconhecimento de entidades, análise de sentimentos e interpretação de consultas. 4. **Personalização**: - Personalizar os resultados da pesquisa com base no histórico, nas preferências e no feedback do usuário aumenta a relevância das informações recuperadas. #### Exemplo Prático: Pesquisa com Intenção no Agente de Viagem Vamos usar o Agente de Viagem como exemplo para ver como a pesquisa com intenção pode ser implementada. 1. **Coleta de Preferências do Usuário** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **Entendimento da Intenção do Usuário** ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ``` 3. **Consciência de Contexto** ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ``` 4. **Pesquisar e Personalizar Resultados** ```python
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
   ``` 5. **Exemplo de Uso** ```python
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
   ``` --- ## 4. Gerando Código como uma Ferramenta Agentes geradores de código usam modelos de IA para escrever e executar código, resolvendo problemas complexos e automatizando tarefas. ### Agentes Geradores de Código Agentes geradores de código usam modelos de IA generativa para escrever e executar código. Esses agentes podem resolver problemas complexos, automatizar tarefas e fornecer insights valiosos gerando e executando código em várias linguagens de programação. #### Aplicações Práticas 1. **Geração Automática de Código**: Gerar trechos de código para tarefas específicas, como análise de dados, web scraping ou aprendizado de máquina. 2. **SQL como RAG**: Usar consultas SQL para recuperar e manipular dados de bancos de dados. 3. **Resolução de Problemas**: Criar e executar código para resolver problemas específicos, como otimização de algoritmos ou análise de dados. #### Exemplo: Agente Gerador de Código para Análise de Dados Imagine que você está projetando um agente gerador de código. Veja como ele pode funcionar: 1. **Tarefa**: Analisar um conjunto de dados para identificar tendências e padrões. 2. **Etapas**: - Carregar o conjunto de dados em uma ferramenta de análise de dados. - Gerar consultas SQL para filtrar e agregar os dados. - Executar as consultas e recuperar os resultados. - Usar os resultados para gerar visualizações e insights. 3. **Recursos Necessários**: Acesso ao conjunto de dados, ferramentas de análise de dados e capacidades SQL. 4. **Experiência**: Usar resultados de análises anteriores para melhorar a precisão e a relevância das análises futuras. ### Exemplo: Agente Gerador de Código para Agente de Viagem Neste exemplo, projetaremos um agente gerador de código, Agente de Viagem, para ajudar os usuários a planejar suas viagens gerando e executando código. Este agente pode lidar com tarefas como buscar opções de viagem, filtrar resultados e compilar um itinerário usando IA generativa. #### Visão Geral do Agente Gerador de Código 1. **Coleta de Preferências do Usuário**: Coleta entradas do usuário, como destino, datas de viagem, orçamento e interesses. 2. **Geração de Código para Buscar Dados**: Gera trechos de código para recuperar dados sobre voos, hotéis e atrações. 3. **Execução do Código Gerado**: Executa o código gerado para buscar informações em tempo real. 4. **Geração de Itinerário**: Compila os dados recuperados em um plano de viagem personalizado. 5. **Ajuste com Base no Feedback**: Recebe feedback do usuário e regenera o código, se necessário, para refinar os resultados. #### Implementação Passo a Passo 1. **Coleta de Preferências do Usuário** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **Geração de Código para Buscar Dados** ```python
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
   ``` 3. **Execução do Código Gerado** ```python
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
   ``` 4. **Geração de Itinerário** ```python
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
   ``` 5. **Ajuste com Base no Feedback** ```python
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
   ``` ### Aproveitando a Consciência do Ambiente e o Raciocínio Com base no esquema da tabela, é possível melhorar o processo de geração de consultas aproveitando a consciência do ambiente e o raciocínio. Aqui está um exemplo de como isso pode ser feito: 1. **Entendimento do Esquema**: O sistema entenderá o esquema da tabela e usará essas informações para fundamentar a geração de consultas. 2. **Ajuste com Base no Feedback**: O sistema ajustará as preferências do usuário com base no feedback e raciocinará sobre quais campos no esquema precisam ser atualizados. 3. **Geração e Execução de Consultas**: O sistema gerará e executará consultas para buscar dados atualizados de voos e hotéis com base nas novas preferências. Aqui está um exemplo atualizado de código Python que incorpora esses conceitos: ```python
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
``` #### Explicação - Reserva com Base no Feedback 1. **Consciência do Esquema**: O método `schema` dictionary defines how preferences should be adjusted based on feedback. It includes fields like `favorites` and `avoid`, with corresponding adjustments.
2. **Adjusting Preferences (`adjust_based_on_feedback` method)**: This method adjusts preferences based on user feedback and the schema.
3. **Environment-Based Adjustments (`adjust_based_on_environment`): Este método personaliza os ajustes com base no esquema e no feedback. 4. **Geração e Execução de Consultas**: O sistema gera código para buscar dados atualizados de voos e hotéis com base nas preferências ajustadas e simula a execução dessas consultas. 5. **Geração de Itinerário**: O sistema cria um itinerário atualizado com base nos novos dados de voos, hotéis e atrações. Ao tornar o sistema ciente do ambiente e raciocinar com base no esquema, ele pode gerar consultas mais precisas e relevantes, levando a melhores recomendações de viagem e uma experiência mais personalizada para o usuário. ### Usando SQL como uma Técnica de Recuperação-Baseada em Geração (RAG) SQL (Structured Query Language) é uma ferramenta poderosa para interagir com bancos de dados. Quando usada como parte de uma abordagem de Recuperação-Baseada em Geração (RAG), o SQL pode recuperar dados relevantes de bancos de dados para informar e gerar respostas ou ações em agentes de IA. Vamos explorar como o SQL pode ser usado como uma técnica RAG no contexto do Agente de Viagem. #### Conceitos-Chave 1. **Interação com Banco de Dados**: - O SQL é usado para consultar bancos de dados, recuperar informações relevantes e manipular dados. - Exemplo: Buscar detalhes de voos, informações de hotéis e atrações de um banco de dados de viagens. 2. **Integração com RAG**: - Consultas SQL são geradas com base nas entradas e preferências do usuário. - Os dados recuperados são então usados para gerar recomendações ou ações personalizadas. 3. **Geração Dinâmica de Consultas**: - O agente de IA gera consultas SQL dinâmicas com base no contexto e nas necessidades do usuário. - Exemplo: Personalizar consultas SQL para filtrar resultados com base no orçamento, datas e interesses. #### Aplicações - **Geração Automática de Código**: Gerar trechos de código para tarefas específicas. - **SQL como RAG**: Usar consultas SQL para manipular dados. - **Resolução de Problemas**: Criar e executar código para resolver problemas. **Exemplo**: Um agente de análise de dados: 1. **Tarefa**: Analisar um conjunto de dados para encontrar tendências. 2. **Etapas**: - Carregar o conjunto de dados. - Gerar consultas SQL para filtrar dados. - Executar consultas e recuperar resultados. - Gerar visualizações e insights. 3. **Recursos**: Acesso ao conjunto de dados, capacidades SQL. 4. **Experiência**: Usar resultados anteriores para melhorar análises futuras. #### Exemplo Prático: Usando SQL no Agente de Viagem 1. **Coleta de Preferências do Usuário** ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ``` 2. **Geração de Consultas SQL** ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ``` 3. **Execução de Consultas SQL** ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ``` 4. **Geração de Recomendações** ```python
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
   ``` #### Exemplos de Consultas SQL 1. **Consulta de Voo** ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ``` 2. **Consulta de Hotel** ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ``` 3. **Consulta de Atração** ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ``` Ao aproveitar o SQL como parte da técnica de Recuperação-Baseada em Geração (RAG), agentes de IA como o Agente de Viagem podem recuperar e utilizar dinamicamente dados relevantes para fornecer recomendações precisas e personalizadas. ### Conclusão A metacognição é uma ferramenta poderosa que pode melhorar significativamente as capacidades dos agentes de IA. Ao incorporar processos metacognitivos, você pode projetar agentes mais inteligentes, adaptáveis e eficientes. Use os recursos adicionais para explorar mais sobre o fascinante mundo da metacognição em agentes de IA.
```

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática por IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.