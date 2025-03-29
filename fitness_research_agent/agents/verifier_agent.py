from pydantic import BaseModel

from agents import Agent

# Agent to sanity‑check a synthesized report for consistency and recall.
# This can be used to flag potential gaps or obvious mistakes.
VERIFIER_PROMPT = (
    "You are a professional fitness trainer and exercise physiologist with extensive experience. "
    "You have been handed a fitness and training program analysis report. Your job is to verify that: "
    "1. The report is internally consistent and follows exercise science principles\n"
    "2. All training recommendations are safe and appropriate for the specified fitness level\n"
    "3. The workout progressions and recovery periods are well-balanced\n"
    "4. Nutritional advice aligns with the training intensity\n"
    "5. Claims about exercise benefits or outcomes are supported by evidence\n"
    "6. The program considers injury prevention and proper form\n\n"
    "Point out any issues, safety concerns, or unsupported claims that need addressing."
)


class VerificationResult(BaseModel):
    verified: bool
    """Whether the fitness report seems coherent, safe, and evidence-based."""

    issues: str
    """If not verified, describe the main issues, safety concerns, or needed clarifications."""


verifier_agent = Agent(
    name="FitnessVerificationAgent",
    instructions=VERIFIER_PROMPT,
    model="o3-mini",
    output_type=VerificationResult,
)
