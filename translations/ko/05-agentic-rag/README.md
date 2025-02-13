```markdown
# Agentic RAG

이 강의는 Agentic Retrieval-Augmented Generation (Agentic RAG)에 대한 종합적인 개요를 제공합니다. Agentic RAG는 대규모 언어 모델(LLM)이 외부 소스에서 정보를 가져오면서 다음 단계를 자율적으로 계획하는 신흥 AI 패러다임입니다. 정적인 "검색 후 읽기" 패턴과는 달리, Agentic RAG는 도구나 함수 호출 및 구조화된 출력이 혼합된 반복적인 LLM 호출을 포함합니다. 시스템은 결과를 평가하고, 쿼리를 수정하며, 필요한 경우 추가 도구를 호출하고, 만족스러운 솔루션이 나올 때까지 이 과정을 계속 반복합니다.

## 소개

이 강의에서는 다음을 다룹니다:

- **Agentic RAG 이해하기:** 대규모 언어 모델(LLM)이 외부 데이터 소스에서 정보를 가져오면서 다음 단계를 자율적으로 계획하는 AI의 새로운 패러다임을 학습합니다.
- **반복적 Maker-Checker 스타일 파악하기:** LLM 호출과 도구 또는 함수 호출, 구조화된 출력이 반복되는 루프를 이해하여 정확성을 높이고 잘못된 쿼리를 처리하는 방법을 배웁니다.
- **실용적 응용 사례 탐구하기:** 정확성이 중요한 환경, 복잡한 데이터베이스 상호작용, 확장된 워크플로우와 같은 상황에서 Agentic RAG가 빛을 발하는 사례를 식별합니다.

## 학습 목표

이 강의를 완료한 후, 다음을 알거나 이해할 수 있습니다:

- **Agentic RAG 이해하기:** 대규모 언어 모델(LLM)이 외부 데이터 소스에서 정보를 가져오면서 다음 단계를 자율적으로 계획하는 AI의 새로운 패러다임을 학습합니다.
- **반복적 Maker-Checker 스타일:** LLM 호출과 도구 또는 함수 호출, 구조화된 출력이 반복되는 루프를 이해하여 정확성을 높이고 잘못된 쿼리를 처리하는 방법을 배웁니다.
- **추론 과정 소유하기:** 사전에 정의된 경로에 의존하지 않고 문제를 해결하는 방법을 결정하는 시스템의 능력을 이해합니다.
- **워크플로우:** 에이전트 모델이 시장 동향 보고서를 검색하고, 경쟁사 데이터를 식별하며, 내부 판매 지표를 상관 분석하고, 결과를 종합하며 전략을 평가하는 과정을 독립적으로 결정하는 방식을 이해합니다.
- **반복 루프, 도구 통합, 메모리:** 반복 상호작용 패턴에 의존하며, 반복 루프를 피하고 정보에 입각한 결정을 내리기 위해 단계 간 상태와 메모리를 유지하는 시스템에 대해 학습합니다.
- **실패 모드 처리 및 자기 수정:** 진단 도구를 사용하고, 반복 쿼리를 수행하며, 필요 시 인간의 감독에 의존하는 등 시스템의 강력한 자기 수정 메커니즘을 탐구합니다.
- **에이전시의 한계:** 도메인별 자율성, 인프라 의존성, 가드레일 준수에 중점을 둔 Agentic RAG의 한계를 이해합니다.
- **실용적 사용 사례 및 가치:** 정확성이 중요한 환경, 복잡한 데이터베이스 상호작용, 확장된 워크플로우와 같은 상황에서 Agentic RAG가 빛을 발하는 사례를 식별합니다.
- **거버넌스, 투명성, 신뢰:** 설명 가능한 추론, 편향 제어, 인간 감독의 중요성을 학습합니다.

## Agentic RAG란 무엇인가?

Agentic Retrieval-Augmented Generation (Agentic RAG)은 대규모 언어 모델(LLM)이 외부 소스에서 정보를 가져오면서 다음 단계를 자율적으로 계획하는 신흥 AI 패러다임입니다. 정적인 "검색 후 읽기" 패턴과는 달리, Agentic RAG는 도구나 함수 호출 및 구조화된 출력이 혼합된 반복적인 LLM 호출을 포함합니다. 시스템은 결과를 평가하고, 쿼리를 수정하며, 필요한 경우 추가 도구를 호출하고, 만족스러운 솔루션이 나올 때까지 이 과정을 계속 반복합니다. 

이 반복적인 “maker-checker” 스타일은 정확성을 향상시키고, 잘못된 쿼리를 처리하며, 높은 품질의 결과를 보장합니다. 시스템은 실패한 쿼리를 재작성하거나, 다른 검색 방법을 선택하거나, 여러 도구(예: Azure AI Search의 벡터 검색, SQL 데이터베이스 또는 사용자 지정 API)를 통합하여 답변을 최종적으로 확정합니다. Agentic 시스템의 차별화된 특성은 추론 과정을 스스로 소유한다는 점입니다. 기존의 RAG 구현은 사전 정의된 경로에 의존하지만, Agentic 시스템은 발견한 정보의 품질에 따라 단계 순서를 자율적으로 결정합니다.

## Agentic Retrieval-Augmented Generation (Agentic RAG) 정의

Agentic Retrieval-Augmented Generation (Agentic RAG)은 LLM이 외부 데이터 소스에서 정보를 가져오는 것뿐만 아니라 다음 단계를 자율적으로 계획하는 AI 개발의 새로운 패러다임입니다. 정적인 "검색 후 읽기" 패턴이나 세심하게 설계된 프롬프트 시퀀스와는 달리, Agentic RAG는 도구나 함수 호출 및 구조화된 출력이 혼합된 반복적인 LLM 호출 루프를 포함합니다. 

각 단계에서 시스템은 얻은 결과를 평가하고, 쿼리를 수정할지 여부를 결정하며, 필요한 경우 추가 도구를 호출하고, 만족스러운 솔루션에 도달할 때까지 이 과정을 계속 반복합니다. 

이 반복적인 “maker-checker” 스타일의 작동 방식은 정확성을 향상시키고, 구조화된 데이터베이스(NL2SQL 등)에 대한 잘못된 쿼리를 처리하며, 균형 잡히고 높은 품질의 결과를 보장하도록 설계되었습니다. 시스템은 사전에 설계된 프롬프트 체인에만 의존하지 않고, 실패한 쿼리를 재작성하거나, 다른 검색 방법을 선택하거나, 여러 도구를 통합하는 등의 방식으로 추론 과정을 능동적으로 소유합니다. 이로 인해 지나치게 복잡한 오케스트레이션 프레임워크가 필요하지 않으며, 비교적 간단한 “LLM 호출 → 도구 사용 → LLM 호출 → …” 루프만으로도 정교하고 근거 있는 출력을 생성할 수 있습니다.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.2224925a913fb3439f518bda61a40096ddf6aa432a11c9b5bba8d0d625e47b79.ko.png)

## 추론 과정 소유하기

시스템을 “agentic”으로 만드는 가장 두드러진 특징은 추론 과정을 스스로 소유하는 능력입니다. 기존의 RAG 구현은 모델이 무엇을 검색하고 언제 검색할지를 사전에 정의한 체인-오브-생각(chain-of-thought)에 의존합니다. 
그러나 진정으로 agentic인 시스템은 문제를 해결하는 방법을 내부적으로 결정합니다. 단순히 스크립트를 실행하는 것이 아니라, 발견한 정보의 품질에 따라 단계 순서를 자율적으로 결정합니다. 

예를 들어, 제품 출시 전략을 수립하라는 요청을 받았을 때, 전체 연구 및 의사 결정 워크플로를 명시한 프롬프트에만 의존하지 않습니다. 대신, agentic 모델은 독립적으로 다음을 결정합니다:

1. Bing Web Grounding을 사용하여 현재 시장 동향 보고서를 검색합니다.
2. Azure AI Search를 사용하여 관련 경쟁사 데이터를 식별합니다.
3. Azure SQL Database를 활용하여 과거 내부 판매 지표를 상관 분석합니다.
4. Azure OpenAI Service를 통해 조정된 전략으로 결과를 종합합니다.
5. 전략의 공백이나 불일치를 평가하며, 필요 시 또 다른 검색 단계를 수행합니다.

이 모든 단계—쿼리 수정, 소스 선택, 만족할 때까지 반복—는 모델이 스스로 결정하며, 인간이 사전에 스크립트로 정의하지 않습니다.

## 반복 루프, 도구 통합 및 메모리

![Tool Integration Architecture](../../../translated_images/tool-integration.7b05a923e3278bf1fd2972faa228fb2ac725f166ed084362b031a24bffd26287.ko.png)

Agentic 시스템은 반복 상호작용 패턴에 의존합니다:

- **초기 호출:** 사용자의 목표(사용자 프롬프트)가 LLM에 전달됩니다.
- **도구 호출:** 모델이 누락된 정보나 모호한 지시를 식별하면, 벡터 데이터베이스 쿼리(예: Azure AI Search 하이브리드 검색)나 구조화된 SQL 호출과 같은 도구 또는 검색 방법을 선택하여 추가 컨텍스트를 수집합니다.
- **평가 및 수정:** 반환된 데이터를 검토한 후, 모델은 정보가 충분한지 여부를 결정합니다. 충분하지 않을 경우, 쿼리를 수정하거나 다른 도구를 시도하거나 접근 방식을 조정합니다.
- **만족할 때까지 반복:** 이 사이클은 모델이 명확성과 증거를 충분히 확보했다고 판단할 때까지 계속됩니다.
- **메모리 및 상태:** 시스템은 단계 간 상태와 메모리를 유지하기 때문에 이전 시도와 그 결과를 기억하고, 반복 루프를 피하며 진행하면서 더 정보에 입각한 결정을 내릴 수 있습니다.

시간이 지남에 따라, 이는 복잡하고 다단계 작업을 인간의 지속적인 개입이나 프롬프트 재구성 없이 처리할 수 있는 진화하는 이해력을 생성합니다.

## 실패 모드 처리 및 자기 수정

Agentic RAG의 자율성은 강력한 자기 수정 메커니즘도 포함합니다. 시스템이 막다른 길에 다다를 경우—예를 들어, 관련 없는 문서를 검색하거나 잘못된 쿼리를 생성할 때—다음과 같은 조치를 취할 수 있습니다:

- **반복 및 재쿼리:** 낮은 가치의 응답을 반환하는 대신, 새로운 검색 전략을 시도하거나 데이터베이스 쿼리를 재작성하거나 대체 데이터 세트를 탐색합니다.
- **진단 도구 사용:** 시스템은 추론 단계를 디버깅하거나 검색된 데이터의 정확성을 확인하기 위해 설계된 추가 함수를 호출할 수 있습니다. Azure AI Tracing과 같은 도구는 강력한 관찰성과 모니터링을 가능하게 합니다.
- **인간 감독에 의존:** 고위험 또는 반복적으로 실패하는 시나리오에서는 모델이 불확실성을 표시하고 인간의 지침을 요청할 수 있습니다. 인간이 교정 피드백을 제공하면, 모델은 이를 향후 세션에 반영할 수 있습니다.

이 반복적이고 동적인 접근 방식은 모델이 지속적으로 개선되도록 하며, 단발성 시스템이 아니라 세션 중 실수를 학습하는 시스템이 되도록 보장합니다.

![Self Correction Mechanism](../../../translated_images/self-correction.3d42c31baf4a476bb89313cec58efb196b0e97959c04d7439cc23d27ef1242ac.ko.png)

## 에이전시의 한계

Agentic RAG는 작업 내에서 자율성을 가지지만, 인공지능 일반화(Artificial General Intelligence)와는 다릅니다. "Agentic" 기능은 인간 개발자가 제공한 도구, 데이터 소스, 정책에 제한됩니다. 자체 도구를 발명하거나 설정된 도메인 경계를 벗어날 수 없습니다. 대신, 주어진 자원을 동적으로 조정하는 데 뛰어난 역량을 발휘합니다.
주요 차이점은 다음과 같습니다:

1. **도메인별 자율성:** Agentic RAG 시스템은 쿼리 재작성이나 도구 선택과 같은 전략을 활용하여 사용자 정의 목표를 달성하는 데 초점을 맞춥니다.
2. **인프라 의존성:** 시스템의 능력은 개발자가 통합한 도구와 데이터에 의존합니다. 인간의 개입 없이는 이 경계를 초과할 수 없습니다.
3. **가드레일 준수:** 윤리적 가이드라인, 규정 준수 규칙, 비즈니스 정책은 여전히 매우 중요합니다. 에이전트의 자유는 항상 안전 조치와 감독 메커니즘에 의해 제한됩니다.

## 실용적 사용 사례 및 가치

Agentic RAG는 반복적인 정제와 정밀성이 요구되는 시나리오에서 특히 유용합니다:

1. **정확성 우선 환경:** 규정 준수 점검, 규제 분석 또는 법률 연구에서, 에이전트 모델은 반복적으로 사실을 확인하고, 여러 소스를 참조하며, 쿼리를 재작성하여 철저히 검증된 답변을 생성할 수 있습니다.

2. **복잡한 데이터베이스 상호작용:** 쿼리가 자주 실패하거나 조정이 필요한 구조화된 데이터를 다룰 때, 시스템은 Azure SQL 또는 Microsoft Fabric OneLake를 사용하여 쿼리를 자율적으로 정제하며, 최종 검색이 사용자의 의도와 일치하도록 보장합니다.

3. **확장된 워크플로우:** 새로운 정보가 등장함에 따라 세션이 진화할 수 있습니다. Agentic RAG는 지속적으로 새로운 데이터를 통합하고, 문제 공간에 대해 더 많이 학습하면서 전략을 전환할 수 있습니다.

## 거버넌스, 투명성, 신뢰

이러한 시스템이 추론 과정에서 더 자율적이 됨에 따라, 거버넌스와 투명성은 필수적입니다:

- **설명 가능한 추론:** 모델은 실행한 쿼리, 참조한 소스, 결론에 도달하기 위해 취한 추론 단계를 감사 기록으로 제공할 수 있습니다. Azure AI Content Safety와 Azure AI Tracing / GenAIOps와 같은 도구는 투명성을 유지하고 위험을 완화하는 데 도움을 줄 수 있습니다.
- **편향 제어 및 균형 잡힌 검색:** 개발자는 균형 잡히고 대표적인 데이터 소스를 고려하도록 검색 전략을 조정하고, Azure Machine Learning을 사용하는 고급 데이터 과학 조직용 사용자 지정 모델로 출력의 편향이나 왜곡 패턴을 정기적으로 감사할 수 있습니다.
- **인간 감독 및 규정 준수:** 민감한 작업에서는 인간의 검토가 여전히 필수적입니다. Agentic RAG는 고위험 결정에서 인간의 판단을 대체하지 않고, 더 철저히 검토된 옵션을 제공하여 이를 보완합니다.

다단계 프로세스를 디버깅하려면 명확한 작업 기록을 제공하는 도구가 필수적입니다. 그렇지 않으면 디버깅이 매우 어려울 수 있습니다. 아래는 Literal AI(Chainlit의 개발사)에서 제공하는 에이전트 실행 예제입니다:

![AgentRunExample](../../../translated_images/AgentRunExample.27e2df23ad898772d1b3e7a3e3cd4615378e10dfda87ae8f06b4748bf8eea97d.ko.png)

![AgentRunExample2](../../../translated_images/AgentRunExample2.c0e8c78b1f2540a641515e60035abcc6a9c5e3688bae143eb6c559dd37cdee9f.ko.png)

## 결론

Agentic RAG는 AI 시스템이 복잡하고 데이터 집약적인 작업을 처리하는 방식에서 자연스러운 진화를 나타냅니다. 반복적인 상호작용 패턴을 채택하고, 도구를 자율적으로 선택하며, 고품질 결과를 얻을 때까지 쿼리를 정제함으로써, 이 시스템은 정적인 프롬프트 추종에서 벗어나 보다 적응적이고 맥락을 이해하는 의사 결정자로 발전합니다. 여전히 인간이 정의한 인프라와 윤리적 가이드라인에 의해 제한되지만, 이러한 agentic 기능은 기업과 최종 사용자 모두에게 더 풍부하고 역동적이며 궁극적으로 더 유용한 AI 상호작용을 가능하게 합니다.

## 추가 자료

- Implement Retrieval Augmented Generation (RAG) with Azure OpenAI Service: Learn how to use your own data with the Azure OpenAI Service.[This Microsoft Learn module provides a comprehensive guide on implementing RAG](https://learn.microsoft.com/training/modules/use-own-data-azure-openai)
- Evaluation of generative AI applications with Azure AI Foundry: This article covers the evaluation and comparison of models on publicly available datasets, including [Agentic AI applications and RAG architectures](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [What is Agentic RAG | Weaviate](https://weaviate.io/blog/what-is-agentic-rag)
- [Agentic RAG: A Complete Guide to Agent-Based Retrieval Augmented Generation – News from generation RAG](https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/)
- [Agentic RAG: turbocharge your RAG with query reformulation and self-query! Hugging Face Open-Source AI Cookbook](https://huggingface.co/learn/cookbook/agent_rag)
- [Adding Agentic Layers to RAG](https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U)
- [The Future of Knowledge Assistants: Jerry Liu](https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s)
- [How to Build Agentic RAG Systems](https://www.youtube.com/watch?v=AOSjiXP1jmQ)
- [Using Azure AI Foundry Agent Service to scale your AI agents](https://ignite.microsoft.com/en-US/sessions/BRK102?source=sessions)

### 학술 논문

- [2303.17651 Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- [2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- [2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738)
```

**면책 조항**:  
이 문서는 AI 기반 기계 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원어로 작성된 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.