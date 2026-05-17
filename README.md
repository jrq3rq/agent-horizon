# Agent Horizon

**The living calendar and knowledge graph for long-running AI agents.**

A persistent, adaptive, full-year planning system purpose-built for AI agents and guided human programs — starting with the **Builder Program: Foundations of Self-Reliance**.

---

## ✨ What is Agent Horizon?

Agent Horizon is not just another calendar. It is a **self-evolving knowledge graph** that tracks, plans, and adapts over months or years.

It turns static curricula into dynamic, evidence-based learning journeys with built-in safety, neurodivergent support, and automatic replanning.

**Current Focus**: A patient AI tutor that guides homeschool families (ages 8–14) through a complete 36-week self-reliance and life skills curriculum.

---

## Key Features

- Infinite-horizon living graph with dependencies and auto-replanning
- Evidence-grounded progress (photos, journals, outputs required)
- Natural language control (“Move Week 5 forward by 3 days”)
- Neurodivergent-friendly design with regulation breaks and tiered difficulty
- Multi-agent system (Tutor + Safety Guardian + Progress Analyst)
- Local-first & privacy focused — your data stays on your machine
- Full-year trajectory visualization and forecasting
- Beautiful exports (weekly plans, portfolios, capstone reports)

---

## Project Structure

```markdwon
agent-horizon/
├── horizon.json                  # ← With basic schema + full Builder Program structure
├── .env.example
├── README.md                     # ← The full professional README I wrote earlier
├── LICENSE                       # (AGPL-3.0 or MIT)
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── curriculum/                   # Full original curriculum files
│   └── builder-program-foundations/   # (all PDFs, MD files, weekly plans)
├── config/
│   ├── difficulty-tiers.json
│   ├── safety-rules.json
│   ├── family-settings.json.example
│   └── schemas/
├── src/                          # Core Python files (even if minimal)
│   ├── core/
│   │   ├── __init__.py
│   │   ├── state.py
│   │   ├── graph.py
│   │   └── replanner.py
│   ├── agents/
│   │   ├── __init__.py
│   │   └── tutor_agent.py
│   └── tools/
│       ├── __init__.py
├── interface/
│   └── web/
│       └── app.py                # Basic Streamlit app (even if just "Hello World" for now)
├── docs/
│   └── architecture.md
├── scripts/
│   └── seed_example_data.py
├── tracks/                       # Empty folders with .gitkeep
├── calendar/
├── journal/
├── memory/
├── security/
├── logs/
├── backups/
├── tests/
├── exports/
└── assets/
```

---

## Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/yourusername/agent-horizon.git
cd agent-horizon

pip install -e .
cp .env.example .env
```

### 2. Seed the Curriculum

```bash
python scripts/seed_example_data.py
```

### 3. Run the Tutor

```bash
streamlit run interface/web/app.py
```

---

## How to Use

1. Onboard your family in **Week 0**
2. Chat naturally with the AI tutor
3. Submit evidence (photos/journal) to complete tasks
4. Parent reviews weekly progress
5. Export beautiful reports and portfolios anytime

---

## Safety First

- Dedicated **Safety Guardian** agent
- “Ask an adult first” enforced on all hands-on activities
- Local-first design (no data leaves your computer by default)
- Full audit logging and parental approval system

**This tool supports — never replaces — responsible adult supervision.**

---

## Tech Stack

- **Core**: LangGraph + Pydantic
- **Models**: Claude 4 / OpenAI / Grok
- **Storage**: JSON + SQLite
- **UI**: Streamlit (Phase 1), Tauri + React (future)
- **Visualization**: Planned infinite canvas

---

## Roadmap

- [x] Core LangGraph engine
- [x] Builder Program curriculum integration
- [ ] Beautiful infinite year canvas
- [ ] Tauri desktop app
- [ ] Multi-year support & open protocol
- [ ] Community curriculum sharing

---

## Who It's For

- Homeschooling families
- Self-reliance educators
- AI developers building long-horizon agents
- Anyone who wants true year-scale AI guidance

---

## License

AGPL-3.0 — See [LICENSE](LICENSE)

---

**Built to grow resilient minds and capable hands.**

---

<!-- **Minimal Guide – Get Agent Horizon Running**

### 1. Every Time You Work (Important)

```bash
cd agent-horizon
source venv/bin/activate
```

You should see `(venv)` at the start of your prompt.

### 2. Install Packages (Only Once)

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run interface/web/app.py
```

---

### Quick Commands Summary

- Start working → `source venv/bin/activate`
- Run app → `streamlit run interface/web/app.py`
- Stop app → Press `Ctrl + C` in terminal

---

**Do this now:**

1. Run `source venv/bin/activate`
2. Run `pip install -r requirements.txt`
3. Run `streamlit run interface/web/app.py`
4. Run `deactivate` -->
