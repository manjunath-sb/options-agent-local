# Options Analysis Agent – Decision Support Prototype

## Project Purpose

This project explores how **agentic AI** can be used as a **decision-support layer** for options analysis, sitting on top of structured market data and deterministic analytics.

The goal is **not** to automate trading or generate signals, but to:

* Interpret multiple analytical dimensions together
* Explain the options environment clearly
* Highlight risks and uncertainty
* Support human decision-making

---

## What This Project Is (and Is Not)

### This project IS:

* An analytical assistant
* A reasoning and explanation layer
* A safe, offline prototype for learning agentic AI
* A demonstration of MCP + tools + agent architecture

### This project IS NOT:

* A trading bot
* A signal generator
* A prediction engine
* An execution system

---

## High-Level Architecture

```
Curated Market Data (CSV)
        ↓
Deterministic Evaluation Tools
        ↓
MCP Server (Tool Boundary)
        ↓
Agent (LLM-based Reasoning)
        ↓
Human-readable Explanation
```

**Key principle:**
Logic is deterministic, reasoning is probabilistic.

---

## Business Logic Breakdown

The system evaluates the options environment using four independent dimensions:

1. **Trend Context**

   * Direction (bullish / bearish / sideways)
   * Confidence level

2. **Volatility Context**

   * Volatility regime
   * Relative option pricing (cheap / fair / expensive)

3. **Risk Boundaries**

   * Presence of nearby support and resistance
   * Clarity of downside and upside risk

4. **Event Risk**

   * Proximity to earnings or major events
   * Near-term uncertainty

Each dimension is evaluated independently and later synthesised by the agent.

---

## Data Handling Approach

* Market data is treated as **already-ingested analytics**
* Data is curated manually from discovery platforms (via allowed export)
* A single-row CSV snapshot is used to represent the current state of a company
* The system is intentionally decoupled from live data ingestion

This mirrors real enterprise workflows, where ingestion and reasoning are separate.

---

## Role of the Agent

The agent:

* Does not compute indicators
* Does not access raw data directly
* Does not give trading advice

The agent:

* Reads structured tool outputs
* Synthesises multiple risk dimensions
* Explains trade-offs and uncertainty in plain language
* Maintains a cautious, analytical tone

The agent behaves like a **junior analyst explaining reasoning**, not a trader.

---

## Technical Components (Summary)

* **Language:** Python
* **Agent framework:** Strands Agents
* **Tool protocol:** Model Context Protocol (MCP)
* **LLM (local):** Ollama with LLaMA 3.2
* **Data format:** CSV (curated snapshot)
* **Execution:** Fully local, offline

---

## Current Status

* Core architecture implemented and working
* Deterministic tools implemented and exposed via MCP
* Agent successfully integrated and responding
* Observed limitations are **model-related**, not architectural

The project is currently paused at a stable checkpoint to focus on business understanding before further refinement.

---

## Known Limitations

* Smaller open-source LLM has weak autonomous tool orchestration
* Agent may over-focus on a single analytical dimension
* Occasional repetition in responses
* Strategy leakage requires tighter control or forced orchestration

These are expected limitations and can be addressed with:

* Stronger models, or
* Explicit tool orchestration logic

---

## Why This Project Matters

This prototype demonstrates:

* Safe use of agentic AI in finance-adjacent domains
* Clear separation of logic and reasoning
* Explainable and auditable system design
* A reusable architectural template for future products

The foundation is intentionally designed to scale with better models and richer data.

---

## Next Steps (When Resumed)

* Improve tool orchestration strategy
* Refine agent prompts and output structure
* Enhance explanation quality
* Explore integration with richer internal datasets
* Prepare manager- or client-facing demos

---

## Disclaimer

This project is for **learning and experimentation only**.
It does not provide financial advice and should not be used for live trading or investment decisions.

---

If you want, I can next:

* Compress this into a **1-page README**
* Convert it into a **portfolio / resume project description**
* Add a **“lessons learned” section**
* Or tailor it for a **manager-facing internal repo**

Tell me what you want to refine.
