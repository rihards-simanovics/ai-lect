class WeatherExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, conditions, result):
        self.rules.append((conditions, result))

    def infer(self):
        for conditions, result in self.rules:
            if all(condition in self.facts for condition in conditions):
                return result
        return "Default"


expert_system = WeatherExpertSystem()

n_facts = int(input("How many facts would you like to enter?: "))

for count in range(n_facts):
    user_fact = input("Enter fact: ")
    expert_system.add_fact(user_fact)

expert_system.add_rule(["high temperature", "low humidity"], "Comfortable")
expert_system.add_rule(["high temperature", "high wind"], "Uncomfortable")

print(
    expert_system.infer()
)  # Output: Comfortable Challenge 2: Expert System with Forward Chaining


class TechSupportExpertSystem:
    def __init__(self):
        self.user_reports = {}
        self.rules = []

    def report_issue(self, category, description):
        self.user_reports[category] = description

    def add_rule(self, conditions, solution):
        self.rules.append({"conditions": conditions, "solution": solution})

    def troubleshoot(self):
        for rule in self.rules:
            conditions_met = all(
                self.user_reports[condition] for condition in rule["conditions"]
            )

            if conditions_met:
                return f"Suggested solution: {rule['solution']}"

        return "No specific solution found for the reported issue."


# Example Usage:
tech_support_system = TechSupportExpertSystem()

# User reports an issue with slow performance
tech_support_system.report_issue("Performance", "The device is running slow.")

# User reports an issue with connectivity
tech_support_system.report_issue("Connectivity", "Unable to connect to the internet.")

# Define rules for troubleshooting
tech_support_system.add_rule(
    ["Performance"], "Clear temporary files and optimize settings."
)
tech_support_system.add_rule(
    ["Connectivity"], "Check network cables and restart the router."
)

# Run troubleshooting
print(tech_support_system.troubleshoot())
