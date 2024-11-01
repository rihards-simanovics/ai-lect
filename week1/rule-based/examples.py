#  .	 Matches any single character except a newline.
#  ^	 Anchors the regex at the start of a line.
#  $	 Anchors the regex at the end of a line.
#  *	 Matches 0 or more occurrences of the preceding character or group.
#  +	 Matches 1 or more occurrences of the preceding character or group.
#  ?	 Matches 0 or 1 occurrence of the preceding character or group (optional).
#  \	 Escapes a metacharacter, allowing it to be treated as a literal character.
#  []	 Defines a character class, matching any one of the characters inside the brackets.
#  |	 Acts as an OR operator, allowing alternatives.
#  ()	 Creates a capturing group, allowing you to extract or apply quantifiers to a specific part of the regex.
#  {}	 Specifies a specific number of occurrences or a range of occurrences of the preceding character or group.
#  \b	 Matches a word boundary.
#  \d	 Matches any digit (0-9).
#  \w	 Matches any word character (alphanumeric plus underscore).
#  \s	 Matches any whitespace character (spaces, tabs, newlines).
#  [^]	 Negated Character Class: Matches any character not in the specified character class.
#  (?i)	 Case-Insensitive Flag: Makes the regex case-insensitive.
#  (?m)	 Multiline Flag: Allows ^ and $ to match the start/end of each line within a multiline string.
#  \.	 Literal Dot: Matches a literal dot character.


def basic_rule_based_system(input_value):
    if input_value < 10:
        return "Low"
    else:
        return "High"


result = basic_rule_based_system(7)
print(result)  # Output: Low


def multiple_condition_rule_system(input_value):
    if input_value < 5:
        return "Very Low"
    elif 5 <= input_value < 10:
        return "Low"
    elif 10 <= input_value < 20:
        return "Medium"
    else:
        return "High"


result = multiple_condition_rule_system(15)
print(result)  # Output: Medium


def rule_1(input_value):
    return input_value < 5


def rule_2(input_value):
    return 5 <= input_value < 10


def rule_3(input_value):
    return 10 <= input_value < 20


def rule_based_system(input_value):
    if rule_1(input_value):
        return "Very Low"
    elif rule_2(input_value):
        return "Low"
    elif rule_3(input_value):
        return "Medium"
    else:
        return "High"


result = rule_based_system(15)
print(result)  # Output: Medium


class RuleEngine1:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rules(self, input_value):
        for condition, result in self.rules:
            if condition(input_value):
                return result
        return "Default"


engine = RuleEngine1()
engine.add_rule(lambda x: x < 5, "Very Low")
engine.add_rule(lambda x: 5 <= x < 10, "Low")
engine.add_rule(lambda x: 10 <= x < 20, "Medium")

result = engine.apply_rules(15)
print(result)  # Output: Medium


class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if rule["condition"] in text.lower():
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."


# Example usage
rule_engine = RuleEngine()

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
