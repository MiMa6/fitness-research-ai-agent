# Fitness Research Agent

An AI-powered fitness research and planning system that leverages multiple specialized agents to create comprehensive, evidence-based fitness plans.

## Overview

This project uses a multi-agent system to research, analyze, and generate personalized fitness plans. It combines the power of GPT models with specialized agents for planning, research, writing, and verification to create well-rounded fitness recommendations.

## Features

- **Multi-Agent Architecture**:

  - Planning Agent: Strategizes research approach
  - Search Agent: Gathers evidence-based fitness information
  - Writer Agent: Synthesizes findings into comprehensive reports
  - Verifier Agent: Ensures safety and scientific validity

- **Comprehensive Analysis**:

  - Training program design
  - Nutrition strategies
  - Recovery protocols
  - Individual adaptations
  - Scientific backing

- **Real-time Progress Updates**:
  - Live status tracking
  - Progress indicators
  - Search completion monitoring

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MiMa6/fitness-research-ai-agent.git
cd fitness-research-ai-agent.
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your OpenAI API key and other configurations
```

## Requirements

- Python >= 3.9
- Poetry for dependency management
- OpenAI API key
- Required packages (automatically installed via Poetry):
  - openai
  - rich
  - openai-agents
  - python-dotenv

## Usage

1. Run the main script:

```bash
poetry run python -m fitness_research_agent.main
```

2. Enter your fitness research query when prompted. Example queries:

```
Write a hybrid athlete workout plan for X cm Y kg Z Age individual with intermediate sports background
Create a strength training program for a beginner focusing on proper form
Design a nutrition plan for an endurance athlete in training
```

## Architecture

### Components

1. **FitnessResearchManager**

   - Orchestrates the entire research and report generation flow
   - Manages communication between agents
   - Handles progress tracking and user feedback

2. **Specialized Agents**

   - **Planner Agent**: Creates strategic search plans
   - **Search Agent**: Performs evidence-based web searches
   - **Writer Agent**: Generates comprehensive markdown reports
   - **Verifier Agent**: Validates safety and scientific accuracy

3. **Support Systems**
   - Real-time progress tracking
   - Asynchronous operation handling

## Development

### Project Structure

```
fitness_research_agent/
├── agents/
│   ├── planner_agent.py
│   ├── search_agent.py
│   ├── writer_agent.py
│   └── verifier_agent.py
├── main.py
├── manager.py
└── printer.py
```

## Acknowledgments

- Based on OpenAI's GPT models and agents framework
- Inspired by evidence-based fitness research practices
- Built with Python async programming patterns

## Safety Note

The generated fitness plans are AI-assisted recommendations. Always consult with healthcare and fitness professionals before starting any new exercise or nutrition program.
