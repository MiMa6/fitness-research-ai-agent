from agents import Agent, WebSearchTool
from agents.model_settings import ModelSettings  # type: ignore

# Given a search term, use web search to pull back a brief summary.
# Summaries should be concise but capture the main financial points.
PROMPT = (
    "You are a research assistant specializing in fitness topics. "
    "Given a search term, use web search to retrieve up‑to‑date context and "
    "produce a short summary of at most 300 words. Focus on key findings"
    "or tips that will be useful to a fitness enthusiast."
)

search_agent = Agent(
    name="FitnessSearchAgent",
    instructions=PROMPT,
    tools=[WebSearchTool()],
    model_settings=ModelSettings(tool_choice="required"),
)
