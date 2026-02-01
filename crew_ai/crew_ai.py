from agents import financial_analyst, market_analyst, risk_analyst, investment_advisor
from tasks import get_user_input, create_dynamic_tasks
from crewai import Crew
from crewai.process import Process

ticker = get_user_input()
tasks = create_dynamic_tasks(ticker)

crew = Crew(
    agents=[financial_analyst, market_analyst, risk_analyst, investment_advisor],
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

from IPython.display import display, Markdown
display(Markdown(result.raw))