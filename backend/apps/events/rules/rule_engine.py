
class RuleEngine:
    def __init__(self):
        self.rules = []
        
    def register_rule(self, rule):
        self.rules.append(rule)
        
    def evaluate(self, event):
        triggered = []
        for rule in self.rules:
            if rule.evaluate(event):
                triggered.append(rule)
        return triggered
