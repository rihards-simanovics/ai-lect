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
expert_system.add_fact("high_temperature")  # Example: High temperature
expert_system.add_fact("low_humidity")  # Example: Low humidity
expert_system.add_rule(["high_temperature", "low_humidity"], "Comfortable")

result = expert_system.infer()
print(result)  # Output: Comfortable


class MedicalDiagnosisExpertSystem:
    def __init__(self):
        self.symptoms = {}
        self.rules = []

    def add_symptom(self, name, present):
        self.symptoms[name] = present

    def add_rule(self, conditions, diagnosis):
        self.rules.append({"conditions": conditions, "diagnosis": diagnosis})

    def diagnose(self):
        for rule in self.rules:
            conditions_met = all(
                self.symptoms[condition] for condition in rule["conditions"]
            )

            if conditions_met:
                return f"The patient is diagnosed with: {rule['diagnosis']}"

        return "No specific diagnosis based on the observed symptoms."


# Example Usage:
medical_system = MedicalDiagnosisExpertSystem()
medical_system.add_symptom("fever", True)
medical_system.add_symptom("cough", True)
medical_system.add_symptom("headache", True)

medical_system.add_rule(["fever", "cough", "headache"], "Common Cold")
medical_system.add_rule(["fever", "cough"], "Flu")
medical_system.add_rule(["headache"], "Migraine")

result = medical_system.diagnose()
print(result)


class DiscountEligibilitySystem:
    def __init__(self):
        self.purchase_history = {}
        self.rules = []

    def add_purchase(self, item, price):
        if item in self.purchase_history:
            self.purchase_history[item] += price
        else:
            self.purchase_history[item] = price

    def add_rule(self, goal, condition_amount):
        self.rules.append({"goal": goal, "conditions": condition_amount})

    def check_discount_eligibility(self, goal):
        total_purchase_amount = sum(self.purchase_history.values())

        if total_purchase_amount == 0:
            return "Customer has no purchase history for evaluation."

        for rule in self.rules:
            if rule["goal"] == goal and total_purchase_amount >= rule["conditions"]:
                return f"The customer is eligible for a {goal} discount. Conditions met: {rule['conditions']}"

        return f"The customer is not eligible for a {goal} discount based on their purchase history."


# Example Usage:
discount_system = DiscountEligibilitySystem()

# Add purchase history
discount_system.add_purchase("Electronics", 800)
discount_system.add_purchase("Clothing", 150)
discount_system.add_purchase("Books", 50)

# Define rules for discount eligibility based on overall purchase amount
discount_system.add_rule("10% Off Electronics", 500)
discount_system.add_rule("20% Off Clothing", 100)

# Check discount eligibility
result = discount_system.check_discount_eligibility("10% Off Electronics")
print(result)
