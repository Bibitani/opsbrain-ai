# OpsBrain AI — Project Context

## 1. What is OpsBrain AI?
OpsBrain AI is an agentic AI system designed to act like a digital operations analyst for logistics and supply-chain companies.

Instead of relying on static dashboards or manual analysis, OpsBrain:
- Reads structured business data from a database
- Identifies operational problems (e.g., delivery delays, cost overruns)
- Explains why they happened
- Suggests what actions should be taken next

The goal is not prediction-first ML, but reasoning-first operational intelligence.

---

## 2. Core Architecture (Mental Model)

- PostgreSQL → Source of truth (facts)
- SQL → Factual retrieval (no guessing)
- LLMs → Reasoning, explanation, planning
- Multi-agent design:
  - Planner Agent
  - Data / SQL Agent
  - Analyst Agent
  - Action Agent (automation later via n8n)

Important principle:
LLMs NEVER invent data — they only reason over SQL results.

---

## 3. Current Project State (As of Now)

### Completed:
- PostgreSQL database set up locally
- Real logistics dataset ingested (India, multi-partner)
- Raw ingestion table (`deliveries_raw`)
- Clean analytics table (`deliveries`)
- Professional GitHub repo structure created
- Collaboration workflow established

### Not Yet Built:
- AI agent workflows
- FastAPI backend
- Frontend
- Automation (n8n)
- Memory / RAG

---

## 4. “One Pain at a Time” Strategy

OpsBrain is modular.

Each operational problem is treated as a **Pain Module**, for example:
- Delivery delays
- Cost overruns
- Vendor performance
- Warehouse efficiency

Each pain module contains:
- Its own KPIs
- Its own SQL queries
- Its own reasoning logic
- Its own documentation

All pain modules share the same core architecture.

---

## 5. Work Split & Ownership

### Shared Core (DO NOT modify casually):
- Database schema
- Agent orchestration logic
- API layer
- Overall architecture

### Pain Module 1 — Delivery Delays (Owner: Bibiyan)
- Delay KPIs
- Delay analytics SQL
- Delay reasoning logic

### Pain Module 2 — <TO BE DECIDED> (Owner: Tanisha)
- Cost / Vendor / Other operational pain
- KPIs and SQL for that pain
- Reasoning prompts and insights

---

## 6. Non-Negotiable Rules
- Do NOT redesign core architecture without discussion
- Do NOT mix data ingestion with reasoning
- Use SQL for facts, LLMs for logic
- Keep modules independent and clean

This document is the authoritative context for OpsBrain AI.
