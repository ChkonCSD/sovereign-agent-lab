"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All three conditions correct but not same venue. PLAIN returned Haymarket Vaults,
XML and SANDWICH both returned Albanach. Both venues satisfy constraints — capacity
160+ and vegan available. Interesting that format change shifted which valid venue
model picked. XML tags and sandwich repeat seem to push attention toward Albanach
which appears earlier in list and has slightly higher capacity (180 vs 160).
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
Distractors did not change results at all, same answers as Part A. If anything
would cause error, it would be venue with capacity 159 and vegan=true — passes
every keyword check but fails on numeric constraint by one. Model would need to
actually compare numbers, not just look for matching attributes. This 70B model
handled it fine but smaller/weaker model could fail here.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C ran because A and B were all correct, so exercise tried 8B model to stress
test. Meta-Llama-3.1-8B also passed all three formats, always picking Haymarket
Vaults — unlike 70B which chose Albanach for XML and SANDWICH. So smaller model
gave correct answer but was less sensitive to formatting cues. Both models passed,
which matches what Rod said in office hours — modern models mostly solved lost-in-
middle problem for short clean contexts like this.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when model is weak, context is long, or data has
many near-miss distractors that look like correct answer on everything except one
detail. In this run all nine conditions passed — three formats, two model sizes,
with and without distractors. But even with all-correct results, formatting still
affected which valid venue was chosen: 70B model picked different venue under XML
vs PLAIN. So formatting influences attention even when it does not break accuracy.
The effect becomes critical when you push model harder — smaller model, longer
document, more confusing distractors, or answer buried deep in middle of context.
"""
