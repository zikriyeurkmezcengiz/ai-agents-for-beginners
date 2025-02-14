# 코스 설정

## 소개

이 강의에서는 코스의 코드 샘플을 실행하는 방법에 대해 다룹니다.

## 요구 사항

- GitHub 계정
- Python 3.12+

## 이 저장소를 클론하거나 포크하기

시작하려면 GitHub 저장소를 클론하거나 포크하세요. 이렇게 하면 코스 자료의 자신의 버전을 만들어 코드를 실행하고, 테스트하고, 수정할 수 있습니다!

이 작업은 [fork the repo](https://github.com/microsoft/ai-agents-for-beginners/fork) 링크를 클릭하여 수행할 수 있습니다.

이제 아래와 같이 강의의 포크된 버전을 가지게 될 것입니다:

![Forked Repo](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.ko.png)

## GitHub Personal Access Token (PAT) 가져오기

현재 이 강의는 GitHub Models Marketplace를 사용하여 대형 언어 모델(LLMs)에 무료로 접근할 수 있는 서비스를 제공합니다. 이 모델들은 AI 에이전트를 생성하는 데 사용됩니다.

이 서비스를 사용하려면 GitHub Personal Access Token을 생성해야 합니다.

GitHub 계정에서 [Personal Access Tokens settings](https://github.com/settings/personal-access-tokens)으로 이동하여 생성할 수 있습니다.

화면 왼쪽에서 `Fine-grained tokens` 옵션을 선택하세요.

그런 다음 `Generate new token`를 선택하세요.

![Generate Token](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.ko.png)

방금 생성한 새 토큰을 복사하세요. 이 토큰을 이 강의에 포함된 `.env` 파일에 추가하게 됩니다.

## 환경 변수에 추가하기

`.env` 파일을 생성하려면 터미널에서 아래 명령을 실행하세요:

```bash
cp .env.example .env
```

이 명령은 예제 파일을 복사하여 디렉토리에 `.env` 파일을 생성합니다.

그 파일을 열고 생성한 토큰을 .env 파일의 `GITHUB_TOKEN=` 필드에 붙여넣으세요.

## 필요한 패키지 설치하기

코드를 실행하는 데 필요한 모든 Python 패키지를 설치하려면 터미널에 다음 명령을 실행하세요.

Python 가상 환경을 생성하여 충돌 및 문제를 방지하는 것을 권장합니다.

```bash
pip install -r requirements.txt
```

이 명령은 필요한 Python 패키지를 설치할 것입니다.

이제 코드를 실행할 준비가 되었습니다. AI 에이전트의 세계를 더 배워보세요!

설정 중 문제가 발생하면 [Azure AI Community Discord](https://discord.gg/kzRShWzttr)에서 도움을 요청하거나 [create an issue](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst)를 통해 문제를 보고하세요.
```

**면책 조항**:  
이 문서는 AI 기반 기계 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어로 작성된 문서)를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 번역가에 의한 번역을 권장합니다. 이 번역을 사용함으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.