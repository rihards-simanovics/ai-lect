class IncomeTaxRuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, tax_band):
        self.rules.append((condition, tax_band))

    def calculate_income_tax(self, income):
        for condition, tax_band in self.rules:
            if condition(income):
                return tax_band
        return "No applicable tax band"


# Create an instance of the IncomeTaxRuleEngine
rule_engine = IncomeTaxRuleEngine()

# Define rules for UK income tax bands
rule_engine.add_rule(lambda x: x <= 12570, "Personal Allowance")
rule_engine.add_rule(lambda x: 12571 <= x <= 50270, "Basic Rate")
rule_engine.add_rule(lambda x: 50271 <= x <= 125140, "Higher Rate")
rule_engine.add_rule(lambda x: x > 125140, "Additional Rate")

# Test the rule engine with a specific income
income = 30000
tax_band_result = rule_engine.calculate_income_tax(income)
print(f"For an income of £{income}, the tax band is: {tax_band_result}")
