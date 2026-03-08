# LLM Projects

A playground for experimenting with large language models and building interesting projects.

## Overview

This repo holds small, self-contained experiments and apps that use LLMs. Each project lives in its own folder so you can try different ideas without cluttering a single codebase.

## Structure

```
llm_projects/
├── dog-concierge/     # Example project (notebooks, scripts)
├── main.py            # Simple entry point
├── pyproject.toml     # Dependencies (managed with uv)
└── README.md
```

## Prerequisites

- **Python 3.12+**
- **[uv](https://docs.astral.sh/uv/)** (recommended) or pip for dependency management

## Setup

1. Clone the repo and enter the directory:
   ```bash
   cd llm_projects
   ```

2. Create a virtual environment and install dependencies with uv:
   ```bash
   uv sync
   ```

   Or with pip:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -e .
   ```

3. For Jupyter notebooks, the project already includes `ipykernel` and `jupyter`. Launch Jupyter with:
   ```bash
   uv run jupyter notebook
   ```
   or
   ```bash
   uv run jupyter lab
   ```

## Running

- **Entry point:** `uv run python main.py` (or `python main.py` with venv activated)
- **Notebooks:** Open any `.ipynb` from a project folder (e.g. `dog-concierge/concierge.ipynb`) in Jupyter.

## Projects

| Project           | Description                          |
|-------------------|--------------------------------------|
| **dog-concierge** | *(Starter — add your own idea here)* |

## Adding a New Project

1. Create a new folder under the repo root (e.g. `my-llm-app/`).
2. Add notebooks, scripts, or a small app as you like.
3. If you need extra dependencies, add them in `pyproject.toml` under `[project]` → `dependencies`, then run `uv sync`.
4. Optionally add a short row for the project in the **Projects** table above.

## Tips

- Keep API keys and secrets out of the repo (use env vars or a `.env` file and add it to `.gitignore`).
- Use `uv add <package>` to add new dependencies so the lockfile stays in sync.
