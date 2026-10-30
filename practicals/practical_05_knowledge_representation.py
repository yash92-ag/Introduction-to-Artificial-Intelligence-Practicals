"""
Practical 5: Knowledge Representation using Prolog/Python

Aim:
    To represent facts and rules for an organizational hierarchy and perform
    forward- and backward-chaining logical inference.

How to run:
    python practicals/practical_05_knowledge_representation.py
"""

# ---------------------------------------------------------------
# STEP 1: Knowledge base of facts
# Each fact is (child, parent), meaning "child reports to parent".
# ---------------------------------------------------------------
facts = [
    ("Aarav", "Priya"),   # Aarav reports to Priya
    ("Priya", "Rohit"),   # Priya reports to Rohit
    ("Sneha", "Priya"),   # Sneha reports to Priya
    ("Rohit", "Kavya")    # Rohit reports to Kavya (CEO)
]


# ---------------------------------------------------------------
# STEP 2: Rules
# ---------------------------------------------------------------
def is_parent(child, parent):
    # Rule: a direct manager is a fact that exists in the knowledge base
    return (child, parent) in facts


def is_ancestor(person, ancestor, visited=None):
    # Rule: an ancestor is a direct manager, or a manager's manager, and so on
    if visited is None:
        visited = set()
    for child, parent in facts:
        if child == person and parent not in visited:
            if parent == ancestor:
                return True
            visited.add(parent)
            if is_ancestor(parent, ancestor, visited):
                return True
    return False


print("Is Priya direct manager of Aarav?", is_parent("Aarav", "Priya"))
print("Is Rohit direct manager of Aarav?", is_parent("Aarav", "Rohit"))
print("Is Rohit an ancestor of Aarav?", is_ancestor("Aarav", "Rohit"))
print("Is Kavya an ancestor of Aarav?", is_ancestor("Aarav", "Kavya"))


# ---------------------------------------------------------------
# STEP 3: Forward chaining
# Start from the known facts and keep deriving new facts until
# nothing new can be found.
# Rule used: if (a reports to b) and (b reports to d), then (a reports to d).
# ---------------------------------------------------------------
def forward_chain(facts):
    derived = set(facts)
    changed = True
    while changed:
        changed = False
        new_facts = set()
        for (a, b) in derived:
            for (c, d) in derived:
                if b == c and (a, d) not in derived and (a, d) not in new_facts:
                    new_facts.add((a, d))
        if new_facts:
            derived.update(new_facts)
            changed = True
    return derived


all_relationships = forward_chain(facts)
print("All direct + derived reporting relationships:")
for rel in sorted(all_relationships):
    print(f"  {rel[0]} reports up to {rel[1]}")


# ---------------------------------------------------------------
# STEP 4: Backward chaining
# Start from the goal (the question) and work backwards through the
# facts, keeping a trace of the reasoning steps.
# ---------------------------------------------------------------
def backward_chain(query_child, query_ancestor, facts, trace=None):
    if trace is None:
        trace = []
    for (child, parent) in facts:
        if child == query_child:
            trace.append(f"Checking: does {child} report directly to {parent}?")
            if parent == query_ancestor:
                trace.append(f"  Match found: {child} -> {parent}. Goal reached.")
                return True, trace
            else:
                trace.append(f"  Not a direct match. Recursing on {parent} -> {query_ancestor}")
                result, trace = backward_chain(parent, query_ancestor, facts, trace)
                if result:
                    return True, trace
    return False, trace


# STEP 5: Query the knowledge base
result, trace = backward_chain("Aarav", "Kavya", facts)
print(f"Query Result: Does Aarav report up to Kavya? {result}\n")
print("Reasoning steps (Trace):")
for step in trace:
    print(" ", step)
