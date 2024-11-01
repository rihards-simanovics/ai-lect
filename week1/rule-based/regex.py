import re


class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if re.search(rule["condition"], text, re.IGNORECASE):
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."


rule_engine = RuleEngine()
rule_engine.add_rule(r"\bhello\b", "Hi there!")
rule_engine.add_rule(r"\bthank you\b", "Hi there!")
rule_engine.add_rule(r"\bgoodbye\b|\bbye\b", "Goodbye!")
rule_engine.add_rule(r"\bmy name is (.+?)\b", "Nice to meet you, {0}!")


# Add rules
rule_engine.add_rule("hello", "Hi there!")
rule_engine.add_rule("goodbye", "Goodbye!")

# Have conversation
while True:
    user_input = input("You: ")
    response = rule_engine.apply_rules(user_input)
    print(response)

    if user_input.lower() == "goodbye":
        break
