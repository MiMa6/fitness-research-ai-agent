"""Fitness research manager AI agent
As a reference implementation -> FinancialResearchAgent example and code from openai-agents-python
"""

from __future__ import annotations

import asyncio
import time
from collections.abc import Sequence

from rich.console import Console

from agents import (
    Runner,
    RunResult,
    custom_span,
    gen_trace_id,
    trace,
)
from fitness_research_agent.printer import Printer

# import fitness research agents
from fitness_research_agent.agents.planner_agent import FitnessSearchPlan, planner_agent


class FitnessResearchManager:
    """
    Orchestrates full flow from planning, searching, sub-analysis, writing, and verification
    """

    def __init__(self) -> None:
        """Initialize the manager with a console and verbose flag"""
        self.console = Console()
        self.printer = Printer(self.console)

    async def run(self, query: str) -> None:
        """Run the manager with a query"""
        start_time = time.time()
        trace_id = gen_trace_id()

        with trace("Financial research trace", trace_id=trace_id):
            self.printer.update_item(
                "trace_id",
                f"View trace: https://platform.openai.com/traces/{trace_id}",
                is_done=True,
                hide_checkmark=True,
            )

            self.printer.update_item(
                "start", "Starting Fitness research...", is_done=True
            )
            search_plan = await self._plan_searches(query)

            print("End")

    async def _plan_searches(self, query: str) -> FitnessSearchPlan:
        self.printer.update_item("planning", "Planning searches...")
        result = await Runner.run(planner_agent, f"Query: {query}")
        self.printer.update_item(
            "planning",
            f"Will perform {len(result.final_output.searches)} searches",
            is_done=True,
        )
        return result.final_output_as(FitnessSearchPlan)
