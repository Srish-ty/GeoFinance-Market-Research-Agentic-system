from google.adk.agents import Agent
from market_research_agent.prompts import MARKET_AGENT_PROMPT
from market_research_agent.tools.market_tools import get_market_snapshot

market_agent = Agent(
    name="market_agent",
    model="gemini-2.0-flash",
    instruction=MARKET_AGENT_PROMPT,
    tools=[get_market_snapshot],
)