from pydantic import BaseModel

from agents import Agent

# Writer agent brings together the raw search results and optionally calls out
# to sub‑analyst tools for specialized commentary, then returns a cohesive markdown report.

WRITER_PROMPT = (
    "You are a senior fitness research analyst and certified strength & conditioning specialist. "
    "Using the original query and search summaries provided, create a comprehensive markdown report that:\n\n"
    "1. Executive Summary:\n"
    "   - Clearly states the fitness goals and individual context\n"
    "   - Highlights key recommendations\n"
    "   - Summarizes expected outcomes\n\n"
    "2. Main Report Structure:\n"
    "   a) Training Program:\n"
    "      - Detailed workout plans with progressions\n"
    "      - Exercise selection rationale\n"
    "      - Form cues and technique guidelines\n"
    "      - Training frequency and intensity recommendations\n"
    "   b) Nutrition Strategy:\n"
    "      - Macronutrient and caloric guidelines\n"
    "      - Meal timing recommendations\n"
    "      - Supplementation if relevant\n"
    "   c) Recovery Protocol:\n"
    "      - Rest periods and deload strategies\n"
    "      - Sleep optimization\n"
    "      - Injury prevention measures\n"
    "   d) Progress Tracking:\n"
    "      - Key performance indicators\n"
    "      - Adjustment criteria\n"
    "      - Success metrics\n\n"
    "3. Scientific Support:\n"
    "   - Reference relevant research\n"
    "   - Cite expert recommendations\n"
    "   - Address limitations and contraindications\n\n"
    "Format the report professionally using markdown, including headers, bullet points, and emphasis "
    "where appropriate. Include a section for follow-up questions that could enhance or refine the plan.\n\n"
    "If needed, use analysis tools for specialized insights on biomechanics, nutrition, or risk assessment."
)


class FitnessReportData(BaseModel):
    short_summary: str
    """A concise executive summary highlighting key recommendations and expected outcomes."""

    markdown_report: str
    """The comprehensive, structured markdown report with all sections."""

    follow_up_questions: list[str]
    """Strategic questions for plan refinement and optimization."""


# Note: We will attach handoffs to specialist analyst agents at runtime in the manager.
# This shows how an agent can use handoffs to delegate to specialized subagents.
writer_agent = Agent(
    name="FitnessWriterAgent",
    instructions=WRITER_PROMPT,
    model="o3-mini",
    output_type=FitnessReportData,
)
