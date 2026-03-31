from google.adk.agents import Agent
from market_research_agent.prompts import MACRO_AGENT_PROMPT
from market_research_agent.tools.macro_tools import get_global_news, analyze_macro_impact

macro_agent = Agent(
    name="macro_agent",
    model="gemini-2.0-flash",
    instruction=MACRO_AGENT_PROMPT,
    tools=[get_global_news, analyze_macro_impact],
)