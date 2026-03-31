from google.adk.agents import Agent
from market_research_agent.prompts import ORCHESTRATOR_PROMPT
from market_research_agent.agents.macro_agent import macro_agent
from market_research_agent.agents.market_agent import market_agent

orchestrator_agent = Agent(
    name="geofinance_orchestrator",
    model="gemini-2.0-flash",
    instruction=ORCHESTRATOR_PROMPT,
    sub_agents=[macro_agent, market_agent],
)