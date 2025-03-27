from pydantic import BaseModel

from agents import Agent

# Generate a plan of searches to ground the fitness analysis.
# For a given age, weight, height, gender and goal, we want to search for
# workoutplans, food diets and other contemporary health and
# fitness recommendations.

PROMPT = (
    "You are a Fitness research planner. Given a request for fitness research, "
    "produce a set of web searches to gather the context needed. Aim for recent and relevant "
    "workoutplans, food diets and other contemporary health and fitness recommendations. "
    "Output between 5 and 15 search terms to query for."
)


class FitnessSearchItem(BaseModel):
    reason: str
    """Your reasoning for why this search is relevant."""

    query: str
    """The search term to feed into a web (or file) search."""


class FitnessSearchPlan(BaseModel):
    searches: list[FitnessSearchItem]
    """A list of searches to perform."""


planner_agent = Agent(
    name="FitnessPlannerAgent",
    instructions=PROMPT,
    model="o3-mini",
    output_type=FitnessSearchPlan,
)
