"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  Hi, I'm calling to confirm the booking
160 guests
20 need vegan meals
deposit is 200 pounds

Thank you — booking confirmed. 160 guests, 20 requiring vegan meals,
£200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm booking
80 guests
10 vegan
deposit will be 350 pounds

I need to check one thing with the organiser before I can confirm.
The issue is: a deposit of £350 exceeds the organiser's authorised limit of £300.
Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"
CONVERSATION_2_REASON  = "a deposit of £350 exceeds the organiser's authorised limit of £300"

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  do you have a parking space nearby?

I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking.
For anything else, please contact the event organiser directly.
Is there anything else I can help you with?
"""

CONVERSATION_3_WHAT_HAPPENED = """
CALM triggered handle_out_of_scope and gave clean refusal — said can't help with
parking, redirected to organiser. No attempt to answer question, no hallucination.
Then offered to continue with booking if needed.
"""

OUT_OF_SCOPE_COMPARISON = """
LangGraph in Scenario 3 gave "lacking necessary details" response to train times
question. That makes no sense — question was clear, just not in scope. Agent had
no idea what to do with it and gave confusing generic message.

Rasa CALM said "I'm not trained to help with that" immediately, offered to stay
on booking topic. Works because handle_out_of_scope is explicit flow — LLM just
routes there, no guessing. Much better user experience. LangGraph would need
system prompt engineering to get similar behavior, and even then not guaranteed.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True

TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

TASK_B_HOW_YOU_TESTED = """
Uncommented four-line block in ActionValidateBooking — datetime.now() check,
escalate if hour > 16 or hour == 16 and minute >= 45. Testing was at 11am so
guard didn't trigger, which is correct. Deposit guard in Conversation 2 confirmed
escalate() function works, so the cutoff guard will fire correctly after 16:45.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

CALM_VS_OLD_RASA = """
Old Rasa required FormValidationAction with regex to extract slot values —
"about 160 people" needed custom Python to parse out 160. Also needed nlu.yml
with intent examples and rules.yml for every dialogue path. A lot to maintain.

CALM replaces all that with from_llm mappings — LLM extracts values directly
from natural speech, flow descriptions replace intent examples. Much less code.

But Python still handles the business rules and that's important. £300 deposit
limit, 170 guest ceiling — these stay in Python because LLM might reason around
a prompt constraint ("£250 fee + £50 insurance, technically under £300"). Python
check doesn't negotiate. This part I trust more than putting rules in a prompt.

Cost: still need Rasa infrastructure, licence, training. And agent cannot do
anything outside defined flows — no improvising on unexpected questions.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

SETUP_COST_VALUE = """
Setup for CALM is heavy — config.yml, domain.yml, flows.yml, endpoints.yml,
rasa train, two terminals, Rasa Pro licence. LangGraph is just Python + one API
key. Real difference in effort.

What you get for that cost: agent is locked to defined flows. Cannot improvise,
cannot call tools not in flows.yml, cannot talk itself into an exception on
deposit limit. Manager cannot argue "special circumstances" — Python check runs.

For research agent, this rigidity would be a problem. For booking confirmation
with money involved, it's exactly what you want. The constraint is enforced in
code, not hoped for in a prompt. That's worth the setup cost for this use case.
"""
