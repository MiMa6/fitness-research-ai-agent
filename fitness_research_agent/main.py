import asyncio

from fitness_research_agent.manager import FitnessResearchManager


# Entrypoint for the FitnessResearchAgent

# Fitness research query, for example:
# "Write a hybrid athlete workout plan for
# x cm y kg individual with sports background""


async def main() -> None:
    query = input("Enter a Fitness research query: ")
    mgr = FitnessResearchManager()
    await mgr.run(query)


if __name__ == "__main__":
    asyncio.run(main())
