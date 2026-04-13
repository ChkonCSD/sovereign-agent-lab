"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No venues match — search_venues returned matches=[], count=0 for 300 guests with vegan options. Agent correctly reported no matching venues exist."

# ── The experiment ─────────────────────────────────────────────────────────

EX4_EXPERIMENT_DONE = True

EX4_EXPERIMENT_RESULT = """
Changed Albanach status to 'full' in mcp_venue_server.py, re-ran ex4.
Query 1 returned 1 match instead of 2 — Albanach disappeared, agent
picked Haymarket Vaults (1 Dalry Road) instead.

Only file touched: mcp_venue_server.py. Agent code, LangGraph loop, LLM calls —
all unchanged. Agent adapted automatically. That's the point of MCP: update
data in one place, every client sees it next run without any code change.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 0   # exercise2 imports from sovereign_agent, no tool code in exercise file
LINES_OF_TOOL_CODE_EX4 = 0   # exercise4 discovers tools dynamically, no definitions needed

MCP_VALUE_PROPOSITION = """
Main thing MCP buys: dynamic discovery. Exercise 2 has hardcoded TOOLS list in
research_agent.py — add new tool, go update that import. Exercise 4 calls
discover_tools() at runtime and gets whatever server exposes right now. Add
@mcp.tool() to mcp_venue_server.py, every client picks it up automatically.

Also MCP is standard protocol — same server works with Rasa action server,
different LangGraph agent, Claude Desktop, anything MCP-compatible. One place
for venue data and logic, any number of clients consume it. Not just "separate
file" — separate service with defined interface.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────

WEEK_5_ARCHITECTURE = """
- MCP venue server is shared data layer — all agents talk to it, so when venue
  data changes only one file needs updating, not every agent separately.
- LangGraph research agent handles open-ended part — find venues, check weather,
  estimate costs, generate flyer — because you can't write those steps in advance,
  model needs to decide order and what to call.
- Rasa CALM confirmation agent handles manager call — deposit limits and capacity
  rules enforced in Python, not hoped for in a prompt.
- Memory layer stores past runs so research agent doesn't re-check venues it
  already knows are full, recalls decisions from previous sessions.
- LangSmith observability tracks every tool call and token cost so you can audit
  what happened without reproducing the run when something breaks.
"""

# ── The guiding question ───────────────────────────────────────────────────

GUIDING_QUESTION_ANSWER = """
LangGraph for research, Rasa CALM for manager call. Swapping feels wrong because
each agent strength maps directly to one task.

Exercise 2 Task A: agent checked two venues, picked Albanach, did catering math,
checked weather, generated flyer — all in one run, in order it decided itself.
Nobody told it to check weather after venues. That autonomy is what makes it
useful. Can't put that in flows.yml because you don't know in advance what
steps will be needed.

Exercise 3: Rasa confirmed 160 guests / £200 deposit and rejected £350 with
exact reason from Python code. Rejection is guaranteed. If LangGraph handled
manager call, £300 limit would live in prompt — model could argue around it
("250 fee plus 60 insurance is technically under 300"). Also saw Scenario 3
where LangGraph responded "lacking necessary details" to simple train question
— completely confused. Rasa CALM routed to handle_out_of_scope cleanly because
that flow is explicitly defined.

Rasa for research fails because it only knows two flows. LangGraph for confirmation
fails because you can't enforce business rules through a prompt.
"""
