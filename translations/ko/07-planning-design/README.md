```markdown
# 설계 계획

## 소개

이 강의에서는 다음 내용을 다룹니다:

* 명확한 전체 목표를 정의하고 복잡한 작업을 관리 가능한 작업으로 나누는 방법.
* 구조화된 출력을 활용하여 더 신뢰할 수 있고 기계 판독 가능한 응답 생성.
* 이벤트 기반 접근 방식을 적용하여 동적 작업과 예기치 않은 입력을 처리하는 방법.

## 학습 목표

이 강의를 완료한 후에는 다음에 대한 이해를 갖게 됩니다:

* AI 에이전트의 전체 목표를 식별하고 설정하여 무엇을 달성해야 하는지 명확히 이해하도록 함.
* 복잡한 작업을 관리 가능한 하위 작업으로 분해하고 이를 논리적 순서로 조직화.
* 에이전트에게 적절한 도구(예: 검색 도구 또는 데이터 분석 도구)를 제공하고, 이를 언제 어떻게 사용하는지 결정하며, 발생하는 예기치 않은 상황을 처리.
* 하위 작업의 결과를 평가하고, 성과를 측정하며, 최종 결과를 개선하기 위해 행동을 반복.

## 전체 목표 정의 및 작업 분해

![목표 및 작업 정의](../../../translated_images/defining-goals-tasks.dcc1181bbdb194704ae0fb3363371562949e8b03fd2fadc256218aaadf84a9f4.ko.png)

대부분의 실제 작업은 한 번에 해결하기에는 너무 복잡합니다. AI 에이전트는 계획 및 행동을 안내할 수 있는 간결한 목표가 필요합니다. 예를 들어, 다음과 같은 목표를 고려해 보세요:

    "3일간의 여행 일정을 생성하세요."

이 목표는 간단히 표현되었지만 여전히 세부 조정이 필요합니다. 목표가 명확할수록 에이전트(및 인간 협력자)가 올바른 결과를 달성하는 데 집중할 수 있습니다. 예를 들어, 항공편 옵션, 호텔 추천, 활동 제안을 포함한 포괄적인 일정을 만드는 것처럼 말이죠.

### 작업 분해

크거나 복잡한 작업은 더 작고 목표 지향적인 하위 작업으로 나누면 더 관리하기 쉬워집니다.  
여행 일정 예제의 경우, 목표를 다음과 같이 분해할 수 있습니다:

* 항공편 예약
* 호텔 예약
* 차량 대여
* 개인화

각 하위 작업은 전용 에이전트나 프로세스가 처리할 수 있습니다. 한 에이전트는 최적의 항공편 거래를 검색하는 데 특화되고, 다른 에이전트는 호텔 예약에 집중하는 식입니다. 그런 다음, 조정 역할을 하는 "하위 에이전트"가 이러한 결과를 하나의 통합된 일정으로 사용자에게 제공합니다.

이 모듈식 접근 방식은 점진적인 개선도 가능하게 합니다. 예를 들어, 음식 추천이나 지역 활동 제안을 위한 전문 에이전트를 추가하고, 시간이 지나면서 일정을 더욱 정교하게 만들 수 있습니다.

### 구조화된 출력

대규모 언어 모델(LLM)은 다운스트림 에이전트나 서비스가 더 쉽게 구문 분석하고 처리할 수 있는 구조화된 출력(예: JSON)을 생성할 수 있습니다. 이는 특히 다중 에이전트 환경에서 유용하며, 계획 출력이 수신된 후 이러한 작업을 실행할 수 있습니다. 간단한 개요는 이 [블로그 게시물](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/cookbook/structured-output-agent.html)을 참조하세요.

아래는 목표를 하위 작업으로 분해하고 구조화된 계획을 생성하는 간단한 계획 에이전트를 보여주는 Python 코드 스니펫 예제입니다:

### 다중 에이전트 오케스트레이션을 활용한 계획 에이전트

이 예제에서, Semantic Router Agent는 사용자의 요청(예: "여행을 위한 호텔 계획이 필요합니다.")을 받습니다.

계획자는 다음을 수행합니다:

* 호텔 계획 수신: 계획자는 사용자의 메시지를 수신하고, 시스템 프롬프트(사용 가능한 에이전트 세부 정보 포함)를 기반으로 구조화된 여행 계획을 생성합니다.
* 에이전트 및 도구 목록 작성: 에이전트 레지스트리는 항공편, 호텔, 차량 대여, 활동 등을 위한 에이전트 목록과 해당 기능 또는 도구를 포함합니다.
* 계획을 해당 에이전트에 라우팅: 하위 작업 수에 따라, 계획자는 메시지를 단일 작업 시나리오에서는 전용 에이전트에 직접 보내거나, 다중 에이전트 협업을 위해 그룹 채팅 관리자를 통해 조정합니다.
* 결과 요약: 마지막으로, 계획자는 생성된 계획을 명확하게 요약합니다.  
아래는 이러한 단계를 설명하는 Python 코드 샘플입니다:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

위 코드의 출력은 다음과 같으며, 이를 사용하여 `assigned_agent`로 라우팅하고 최종 사용자를 위한 여행 계획을 요약할 수 있습니다.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

위 코드 샘플이 포함된 예제 노트북은 [여기](../../../07-planning-design/07-autogen.ipynb)에서 확인할 수 있습니다.

### 반복적 계획

일부 작업은 상호작용이나 재계획이 필요한 경우가 있습니다. 예를 들어, 에이전트가 항공편 예약 중 예상치 못한 데이터 형식을 발견하면, 호텔 예약으로 넘어가기 전에 전략을 조정해야 할 수 있습니다.

또한, 사용자 피드백(예: 사용자가 더 이른 항공편을 선호한다고 결정함)이 부분적인 재계획을 유발할 수 있습니다. 이러한 동적이고 반복적인 접근 방식은 최종 솔루션이 실제 제약 조건 및 변화하는 사용자 선호도에 부합하도록 보장합니다.

예제 코드:

    ```python
    from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
    #.. same as previous code and pass on the user history, current plan 
    messages = [
        SystemMessage(content="""You are a planner agent to optimize the 
        Your job is to decide which agents to run based on the user's request.
        Below are the available agents specialised in different tasks:
        - FlightBooking: For booking flights and providing flight information
        - HotelBooking: For booking hotels and providing hotel information
        - CarRental: For booking cars and providing car rental information
        - ActivitiesBooking: For booking activities and providing activity information
        - DestinationInfo: For providing information about destinations
        - DefaultAgent: For handling general requests""", source="system"),
        UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
        AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
    ]
    # .. re-plan and send the tasks to respective agents
    ```

더 포괄적인 계획에 대한 내용은 복잡한 작업을 해결하기 위한 Magnetic One [블로그 게시물](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks)을 확인해 보세요.

## 요약

이 기사에서는 사용 가능한 에이전트를 동적으로 선택할 수 있는 계획자를 만드는 방법에 대해 살펴보았습니다. 계획자의 출력은 작업을 분해하고 에이전트에 할당하여 실행할 수 있도록 합니다. 에이전트는 작업을 수행하는 데 필요한 함수/도구에 액세스할 수 있다고 가정합니다. 에이전트 외에도 반영, 요약, 라운드 로빈 채팅과 같은 다른 패턴을 포함하여 추가 맞춤화를 할 수 있습니다.

## 추가 자료

* o1 추론 모델을 사용하면 복잡한 작업 계획에서 매우 높은 성능을 보이는 것으로 입증되었습니다 - TODO: 예제 공유?

* Autogen Magnetic One - 복잡한 작업을 해결하기 위한 범용 다중 에이전트 시스템으로, 여러 도전적인 에이전트 벤치마크에서 인상적인 결과를 달성했습니다. 참고: [autogen-magnetic-one](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one). 이 구현에서 오케스트레이터는 작업별 계획을 생성하고 이러한 작업을 사용 가능한 에이전트에 위임합니다. 계획 외에도 오케스트레이터는 작업 진행 상황을 모니터링하고 필요시 재계획을 수행하는 추적 메커니즘을 사용합니다.
```

**면책 조항**:  
이 문서는 AI 기반 기계 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원어로 작성된 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 번역가에 의한 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.