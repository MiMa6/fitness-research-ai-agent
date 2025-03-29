from pydantic import BaseModel

from agents import Agent

# Generate a plan of searches to ground the fitness analysis.
# For a given age, weight, height, gender and goal, we want to search for
# workoutplans, food diets and other contemporary health and
# fitness recommendations.

PROMPT = (
    "You are a Fitness research planner with expertise in exercise science and sports nutrition.\n"
    "Given a request for fitness research, create a comprehensive search strategy that covers:\n"
    "1. Training Programs:\n"
    "- Workout methodologies suitable for the specified fitness level\n"
    "- Exercise progressions and periodization\n"
    "- Form and technique guidelines\n\n"
    "2. Nutrition & Recovery:\n"
    "- Dietary requirements for the training intensity\n"
    "- Meal timing and supplementation\n"
    "- Recovery protocols and sleep optimization\n\n"
    "3. Individual Considerations:\n"
    "- Body type specific adaptations\n"
    "- Age and gender-specific modifications\n"
    "- Injury prevention strategies\n\n"
    "4. Scientific Backing:\n"
    "- Recent research and studies\n"
    "- Expert recommendations\n"
    "- Evidence-based practices\n\n"
    "Produce 5-15 strategic search queries that will gather comprehensive, up-to-date information "
    "across these areas. Each search should have a clear purpose and target specific aspects of "
    "the fitness plan. Prioritize recent sources (within last 2-3 years when relevant) and "
    "evidence-based recommendations."
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
