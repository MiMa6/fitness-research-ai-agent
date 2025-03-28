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
from fitness_research_agent.agents.planner_agent import (
    FitnessSearchPlan,
    FitnessSearchItem,
    planner_agent,
)
from fitness_research_agent.agents.search_agent import search_agent


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

        with trace("Fitness research trace", trace_id=trace_id):
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
            search_results = await self._perform_searches(search_plan)

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

    async def _perform_searches(self, search_plan: FitnessSearchPlan) -> Sequence[str]:
        with custom_span("Search the web"):
            self.printer.update_item("searching", "Searching...")
            tasks = [
                asyncio.create_task(self._search(item)) for item in search_plan.searches
            ]
            results: list[str] = []
            num_completed = 0
            for task in asyncio.as_completed(tasks):
                result = await task
                if result is not None:
                    results.append(result)
                num_completed += 1
                self.printer.update_item(
                    "searching", f"Searching... {num_completed}/{len(tasks)} completed"
                )
            self.printer.mark_item_done("searching")
            return results

    async def _search(self, item: FitnessSearchItem) -> str | None:
        input_data = f"Search term: {item.query}\nReason: {item.reason}"
        try:
            result = await Runner.run(search_agent, input_data)
            return str(result.final_output)
        except Exception:
            return None
