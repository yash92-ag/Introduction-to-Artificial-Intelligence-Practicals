"""
Practical 10: Mini AI Project - Rule-Based Customer Support Chatbot

Aim:
    To independently build, test and document a complete end-to-end AI
    application, integrating the rule systems, pattern matching and inference
    logic practiced across earlier practicals.

How to run:
    python practicals/practical_10_mini_ai_project.py
"""

# ---------------------------------------------------------------
# STEP 1: Knowledge representation
# Each "intent" (what the user wants) has a list of trigger phrases.
# ---------------------------------------------------------------
intents = {
    "greeting": ["hello", "hi", "hey there", "good morning"],
    "order_status": ["where is my order", "track my order", "order status", "shipment"],
    "return_policy": ["how do i return an item", "return policy", "refund process", "refund"],
    "store_hours": ["what are your store hours", "when are you open", "closing time"]
}

# ---------------------------------------------------------------
# STEP 2: Standard answer for every intent
# ---------------------------------------------------------------
responses = {
    "greeting": "Hello! Welcome to Support. How can I help you today?",
    "order_status": "You can track your order using the tracking link sent to your registered email.",
    "return_policy": "Items can be returned within 30 days with the original receipt and packaging.",
    "store_hours": "Our retail stores are open from 10:00 AM to 9:00 PM, Monday through Sunday."
}

print(f"Initialized Chatbot with {len(intents)} intents and corresponding domain knowledge templates.")


# ---------------------------------------------------------------
# STEP 3: Find the reply using substring pattern matching
# If any trigger phrase appears inside the user's message, return its answer.
# If nothing matches, return a polite fallback reply.
# ---------------------------------------------------------------
def get_response(user_input):
    user_input_clean = user_input.lower().strip()
    for intent, phrases in intents.items():
        for phrase in phrases:
            if phrase in user_input_clean:
                return responses[intent]
    return "I'm sorry, I didn't understand that. Could you please rephrase your request?"


# ---------------------------------------------------------------
# STEP 4: Test the chatbot (in-domain and out-of-domain queries)
# ---------------------------------------------------------------
test_inputs = [
    "hi there",
    "where is my order",
    "what's your return policy",
    "when are you open on sunday",
    "do you sell gaming laptops"    # Out-of-domain query
]

for inp in test_inputs:
    print(f"User Query : {inp}")
    print(f"Bot Output : {get_response(inp)}\n")

# ---------------------------------------------------------------
# STEP 5: Project documentation (summary)
# ---------------------------------------------------------------
# 1. Problem Statement : Automate tier-1 customer support replies about
#                        orders, returns and store hours.
# 2. Approach          : Rule-based substring matching (fast, predictable,
#                        and it never "makes up" answers).
# 3. Knowledge Base    : Two dictionaries - intents (triggers) and responses.
# 4. Test Analysis     : In-domain queries answered correctly; out-of-scope
#                        queries get the fallback reply.
# 5. Limitations       : Typos (e.g. 'ordr statu'), sentences with several
#                        intents, and heavy paraphrasing are not understood.
# 6. Future Work       : Use the TF-IDF + Naive Bayes classifier from
#                        Practical 9, plus fuzzy matching (Levenshtein distance).
