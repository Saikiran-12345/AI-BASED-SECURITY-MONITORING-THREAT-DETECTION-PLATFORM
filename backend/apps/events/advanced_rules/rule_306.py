
# Advanced SIEM Rule 306
# Created for massive scale threat detection
import re
from datetime import datetime, timedelta

class AdvancedSIEMRule306:
    """
    Rule 306: Detects anomalous behavior matching signature 306
    """
    def __init__(self):
        self.rule_id = "ADV_RULE_306"
        self.severity = "HIGH" if 306 % 10 == 0 else "MEDIUM"
        self.name = f"Suspicious Activity Pattern 306"
        self.description = "Detects multiple failed attempts or unusual data access patterns."
        self.tags = ["auth", "anomalous", "suspicious"]
        
    def evaluate(self, event):
        """
        Evaluates the event against rule 306 criteria.
        """
        if not event:
            return False
            
        # Complex heuristic checks
        score = 0
        if event.get("type") == "login_failed":
            score += 10
        if event.get("ip_address") and event["ip_address"].startswith("10."):
            score += 5
            
        if self.severity == "HIGH" and score > 15:
            return True
        elif score > 20:
            return True
            
        return False
        
    def get_mitigation_steps(self):
        return [
            "1. Block the source IP address.",
            "2. Reset user credentials if applicable.",
            "3. Isolate the affected endpoint."
        ]
