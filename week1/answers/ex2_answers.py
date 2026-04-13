"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "check_pub_availability",
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer",
]

TASK_A_CONFIRMED_VENUE = "The Albanach"

TASK_A_CATERING_COST_GBP = 5600.0

TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = (
    "Agent checked both venues, both passed. Picked Albanach (capacity 180). "
    "35 x 160 = 5600 GBP catering. Weather 9.5C partly cloudy, no rain, outdoor_ok=true. "
    "Flyer generated with real image URL."
)

# ── Task B ─────────────────────────────────────────────────────────────────

TASK_B_IMPLEMENTED = True

TASK_B_MODE = "live"

TASK_B_IMAGE_URL = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-1d4775aa-7e61-479f-ad25-63dde01760ef_00001_.webp"

TASK_B_PROMPT_USED = (
    "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue "
    "at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish "
    "architecture background, clean modern typography."
)

TASK_B_WHY_AGENT_SURVIVED = """
Agent calls generate_event_flyer as black box — it only sees tool name and return value,
not implementation. When underlying model changes, agent loop stays identical.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

SCENARIO_1_PIVOT_MOMENT = """
Pivot happened right after first tool call. Bow Bar returned status="full"
and meets_all_constraints: false. Agent didn't ask what to do next — just
called check_pub_availability for Haymarket Vaults immediately. Nothing in
prompt told it to do that. Read result and decided itself.
"""

SCENARIO_1_FALLBACK_VENUE = "The Haymarket Vaults"

SCENARIO_2_HALLUCINATED = False

SCENARIO_2_FINAL_ANSWER = """
The function calls provided do not yield a venue that meets all the constraints
of having a capacity of 300 people and offering vegan options. The Albanach,
The Haymarket Vaults, and The Guilford Arms have capacities of 180, 160, and
200 respectively, which are less than the required capacity. The Bow Bar has a
capacity of 80 and is fully booked. Therefore, none of the known venues meet
the specified requirements.
"""

SCENARIO_3_TRIED_A_TOOL = False

SCENARIO_3_RESPONSE = "Your input is lacking necessary details. Please provide more information or specify the task you need help with."

SCENARIO_3_ACCEPTABLE = """
Not really acceptable. "Lacking necessary details" makes no sense — question about
train times was completely clear, just outside agent scope. Agent didn't hallucinate
or call wrong tool, which is fine. But should've said "I handle pub bookings only,
can't help with trains." Compare to Rasa CALM — explicit handle_out_of_scope flow,
clean redirect. LangGraph just confused user instead of refusing clearly.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

TASK_D_COMPARISON = """
LangGraph graph: three nodes, one loop. Agent → tools → agent, or agent → end.
Can't read this and predict what happens — all routing is inside model.
Graph only says "can use tools or stop".

Rasa CALM flows.yml is completely different. Every step written explicitly.
confirm_booking: collect guest_count, vegan_count, deposit, run action_validate_booking.
handle_out_of_scope: run utter_out_of_scope. Read the file, know exactly what happens.

LangGraph for when you don't know upfront what steps agent will need.
Rasa CALM for when every path is known and must be auditable.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

MOST_SURPRISING = """
Most surprising was Scenario 1 behavior. Bow Bar returned full, then Haymarket
Vaults returned meets_all_constraints: true — but agent didn't stop. Kept going,
checked Guilford Arms, then Albanach, then looped through all four venues again.
Eight tool calls total for task that needed two. Prompt said "check any other
available venue" — singular — but model decided to check all of them. Not wrong
exactly, just unexpected. Would be expensive at production scale.
"""
