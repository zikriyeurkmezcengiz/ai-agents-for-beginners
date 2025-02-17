# 설계 계획

## 소개

이 강의에서는 다음 내용을 다룹니다:

* 명확한 전체 목표를 정의하고 복잡한 작업을 관리 가능한 작업으로 나누는 방법.
* 구조화된 출력을 활용하여 더 신뢰할 수 있고 기계가 읽을 수 있는 응답을 생성하는 방법.
* 이벤트 기반 접근 방식을 적용하여 동적 작업과 예기치 않은 입력을 처리하는 방법.

## 학습 목표

이 강의를 완료한 후에는 다음 내용을 이해할 수 있습니다:

* AI 에이전트의 전체 목표를 설정하고, 이를 통해 무엇을 달성해야 하는지 명확히 알 수 있도록 합니다.
* 복잡한 작업을 관리 가능한 하위 작업으로 나누고 이를 논리적인 순서로 조직합니다.
* 에이전트에게 적합한 도구(예: 검색 도구 또는 데이터 분석 도구)를 제공하고, 언제 어떻게 사용할지 결정하며 발생하는 예기치 않은 상황을 처리합니다.
* 하위 작업의 결과를 평가하고 성능을 측정하며, 최종 출력을 개선하기 위해 행동을 반복적으로 수정합니다.

## 전체 목표 정의 및 작업 세분화

![목표와 작업 정의](../../../translated_images/defining-goals-tasks.dcc1181bbdb194704ae0fb3363371562949e8b03fd2fadc256218aaadf84a9f4.ko.png)

대부분의 실제 작업은 한 번에 해결하기에는 너무 복잡합니다. AI 에이전트는 계획 및 행동을 안내할 간결한 목표가 필요합니다. 예를 들어, 다음과 같은 목표를 고려해 봅시다:

    "3일간의 여행 일정 생성하기."

이 목표는 간단히 표현되었지만, 여전히 구체화가 필요합니다. 목표가 명확할수록 에이전트(및 협력하는 사람들)가 올바른 결과를 달성하는 데 더 집중할 수 있습니다. 예를 들어, 항공편 옵션, 호텔 추천, 활동 제안을 포함하는 포괄적인 일정을 만드는 것이 그 예입니다.

### 작업 세분화

큰 작업이나 복잡한 작업은 더 작은 목표 지향적인 하위 작업으로 나누면 더 쉽게 관리할 수 있습니다. 
여행 일정 예제를 기준으로 하면, 목표를 다음과 같이 세분화할 수 있습니다:

* 항공편 예약
* 호텔 예약
* 렌터카 예약
* 개인화

각 하위 작업은 전담 에이전트나 프로세스에 의해 처리될 수 있습니다. 한 에이전트는 최적의 항공편을 검색하는 데 전문화되고, 다른 에이전트는 호텔 예약을 담당하는 식입니다. 이후 조정 또는 "다운스트림" 에이전트가 이러한 결과를 하나의 완성된 일정으로 통합하여 최종 사용자에게 제공합니다.

이 모듈식 접근 방식은 점진적인 개선도 가능하게 합니다. 예를 들어, 음식 추천이나 현지 활동 제안을 전문으로 하는 에이전트를 추가하여 일정의 품질을 점진적으로 개선할 수 있습니다.

### 구조화된 출력

대형 언어 모델(LLM)은 다운스트림 에이전트나 서비스가 더 쉽게 구문 분석하고 처리할 수 있는 구조화된 출력(예: JSON)을 생성할 수 있습니다. 이는 계획 출력이 수신된 후 작업을 실행하는 다중 에이전트 컨텍스트에서 특히 유용합니다. 자세한 내용은 [이 블로그 글](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/cookbook/structured-output-agent.html)을 참고하세요.

아래는 목표를 하위 작업으로 분해하고 구조화된 계획을 생성하는 간단한 계획 에이전트를 보여주는 Python 코드 예제입니다:

### 다중 에이전트 오케스트레이션을 활용한 계획 에이전트

이 예제에서, 시맨틱 라우터 에이전트는 사용자 요청(예: "여행을 위한 호텔 계획이 필요합니다.")을 받습니다.

플래너는 다음을 수행합니다:

* 호텔 계획 수신: 플래너는 사용자의 메시지를 받고, 시스템 프롬프트(사용 가능한 에이전트 세부 정보 포함)를 기반으로 구조화된 여행 계획을 생성합니다.
* 에이전트와 그 도구 나열: 에이전트 레지스트리는 항공편, 호텔, 렌터카, 활동 등을 위한 에이전트 목록과 그들이 제공하는 기능 또는 도구를 포함합니다.
* 계획을 해당 에이전트에 라우팅: 하위 작업의 수에 따라, 플래너는 메시지를 전용 에이전트(단일 작업 시나리오의 경우)에게 직접 보내거나, 다중 에이전트 협업을 위한 그룹 채팅 관리자를 통해 조정합니다.
* 결과 요약: 마지막으로, 플래너는 생성된 계획을 명확히 요약합니다.

아래는 이러한 단계를 보여주는 Python 코드 샘플입니다:

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

위 코드에서 생성된 출력은 `assigned_agent`로 라우팅하고 최종 사용자에게 여행 계획을 요약하는 데 사용할 수 있습니다.

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

위 코드 샘플이 포함된 예제 노트북은 [여기](../../../07-planning-design/code_samples/07-autogen.ipynb)에서 확인할 수 있습니다.

### 반복적 계획

일부 작업은 상호작용이나 재계획이 필요하며, 한 하위 작업의 결과가 다음 작업에 영향을 미칠 수 있습니다. 예를 들어, 에이전트가 항공편 예약 중 예기치 않은 데이터 형식을 발견하면, 호텔 예약으로 넘어가기 전에 전략을 조정해야 할 수 있습니다.

또한, 사용자 피드백(예: 사용자가 더 이른 항공편을 선호한다고 결정하는 경우)은 부분적인 재계획을 유발할 수 있습니다. 이러한 동적이고 반복적인 접근 방식은 최종 솔루션이 현실적인 제약 조건과 변화하는 사용자 선호도에 맞도록 보장합니다.

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

더 포괄적인 계획에 대해 알아보려면 복잡한 작업 해결을 위한 Magnetic One [블로그 글](https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks)을 확인하세요.

## 요약

이 글에서는 가용한 에이전트를 동적으로 선택할 수 있는 플래너를 생성하는 방법의 예를 살펴보았습니다. 플래너의 출력은 작업을 세분화하고 에이전트에게 할당하여 실행되도록 합니다. 에이전트가 작업을 수행하는 데 필요한 기능/도구에 액세스할 수 있다고 가정합니다. 에이전트 외에도 반영, 요약, 라운드 로빈 채팅과 같은 패턴을 추가하여 더욱 맞춤화할 수 있습니다.

## 추가 자료

* O1 추론 모델은 복잡한 작업 계획에서 매우 뛰어난 성능을 입증했습니다 - TODO: 예제 공유?

* Autogen Magnetic One - 복잡한 작업을 해결하기 위한 범용 다중 에이전트 시스템으로, 다양한 도전적인 에이전트 벤치마크에서 인상적인 결과를 달성했습니다. 참고: [autogen-magentic-one](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one). 이 구현에서는 오케스트레이터가 작업별 계획을 생성하고 이러한 작업을 사용 가능한 에이전트에 위임합니다. 계획 외에도 오케스트레이터는 작업 진행 상황을 모니터링하고 필요에 따라 재계획하는 추적 메커니즘도 활용합니다.
```

**면책 조항**:  
이 문서는 AI 기반 기계 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 번역가에 의한 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.