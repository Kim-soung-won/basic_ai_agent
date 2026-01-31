from crewai import Agent, Task, Crew, LLM
import os
from crewai.process import Process
os.environ['OPENAI_API_KEY'] = "NA" # Ollama does not require an API key, but it might need to be set to something non-empty

#목차 설정 에이전트
outline_generator = Agent(
    role='목차 생성기',
    goal='주어진 주제에 대한 기사의 구조화된 목차를 생성합니다. 한국어로 답변하세요.',
    # 주제에 따라 max_tokens를 컨트롤하여 비용 절감
    llm = LLM(model = "ollama/llama3.1:8b", base_url = "http://localhost:11434", max_tokens=1000),
    # 보다 상세한 시스템 프롬프트 작성을 위해 문장 추가
    backstory='당신은 정보를 정리하고 다양한 주제에 대한 포괄적인 목차를 만드는 전문가입니다.'
)
#본문 작성 에이전트
writer = Agent(
    role='작가',
    goal='조사를 바탕으로 흥미로운 콘텐츠를 작성합니다. 한국어로 답변하세요.',
    llm = LLM(model = "ollama/llama3.1:8b", base_url = "http://localhost:11434", max_tokens=3000),
    backstory='당신은 복잡한 정보를 읽기 쉬운 콘텐츠로 변환할 수 있는 숙련된 작가입니다.'
)


# Task 정의
outline_task = Task(
    description='AI가 고용 시장에 미치는 영향에 대한 기사의 상세 목차를 작성하세요.',
    agent=outline_generator,
    expected_output="""AI가 고용에 미치는 영향의 주요 측면을 다루는 포괄적인 목차"""
)

writing_task = Task(
    description='연구 결과를 바탕으로 기사를 작성하세요.',
    agent=writer,
    expected_output='AI가 고용 시장에 미치는 영향을 논의하는 흥미로운 기사'
)

ai_impact_crew = Crew(
    agents=[outline_generator, writer],
    tasks=[outline_task, writing_task],
    verbose=True,
    Process=Process.sequential
)

# Crew 실행
result = ai_impact_crew.kickoff()

result