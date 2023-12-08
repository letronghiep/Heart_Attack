class Rule:
    def __init__(self, conditions, diagnosis):
        self.conditions = conditions
        self.diagnosis = diagnosis

    def evaluate(self, facts):
        if self.condition(facts):
            self.action(facts)
class Fact:
    def __init__(self, name, value):
        self.name = name
        self.value = value
class RuleBasedDiagnosisSystem:
    def __init__(self):
        self.rules = []
    def add_rule(self, rule):
        self.rules.append(rule)
    def diagnose(self, patient):
        for rule in self.rules:
            conditions_met = True
            for condition, value in rule.conditions.items():
                if patient.get(condition) != value:
                    conditions_met = False
                    break
            if conditions_met:
                return rule.diagnosis
        return "Cannot diagnose"
