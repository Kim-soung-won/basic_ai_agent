from crewai import Agent, LLM
from crewai_tools   import SerperDevTool
from stock_analysis import comprehensive_stock_analysis
from datetime import datetime

# LLM을 사용하면 Key 설정이 필수, 필요가 없더라도
import os 
os.environ['OPENAI_API_KEY'] = "NA"

# 현재 시간 가져오기
current_time = datetime.now()
search_tool = SerperDevTool()


llm = LLM(model = "ollama/llama3.1:8b", base_url = "http://localhost:11434", max_tokens=3000)
invest_llm = LLM(model = "ollama/llama3.1:8b", base_url = "http://localhost:11434", max_tokens=3000)
# 재무 분석가
financial_analyst = Agent(
    role="Financial Analyst",
    goal="회사의 재무 상태 및 성과 분석",
    backstory="당신은 재무 제표와 비율을 해석하는 데 전문성을 갖춘 노련한 재무 분석가입니다.날짜: {current_time:%Y년 %m월 %d일}",
    tools=[comprehensive_stock_analysis],
    llm=llm,
    max_iter=3, # 최대 3회 반복 실행
    allow_delegation=False,
    verbose=True
)

# 시장 분석가
market_analyst = Agent(
    role="Market Analyst",
    goal="회사의 시장 지위 및 업계 동향 분석",
    backstory="당신은 기업/산업 현황 및 경쟁 환경을 전문적으로 분석할 수 있는 숙련된 시장 분석가입니다.날짜: {current_time:%Y년 %m월 %d일}",
    tools=[search_tool],
    llm=llm,
    max_iter=3, # 최대 3회 
    allow_delegation=False,
    verbose=True
)

# 위험 분석가
risk_analyst = Agent(
    role="Risk Analyst",
    goal="주식과 관련된 잠재적 위험 식별 및 평가",
    backstory="당신은 투자에서 명백한 위험과 숨겨진 위험을 모두 식별하는 예리한 안목을 갖춘 신중한 위험 분석가입니다.날짜: {current_time:%Y년 %m월 %d일}",
    tools=[comprehensive_stock_analysis],
    llm=llm,
    allow_delegation=False,
    verbose=True
)

# 투자 전문가
# 앞선 결과를 기반으로 하기 때문에 Tool은 필요하지 않음
investment_advisor = Agent(
    role="Investment Advisor",
    goal="전체 분석을 기반으로 한 투자 추천 제공",
    backstory="다양한 분석을 종합하여 전략적 투자 조언을 제공하는 신뢰할 수 있는 투자 자문가입니다.날짜: {current_time:%Y년 %m월 %d일}",
    llm=invest_llm,
    allow_delegation=False,
    verbose=True
)