
class Rule474:
    """
    Detection Rule 474
    Monitors for specific security conditions based on threat intelligence profile 474.
    """
    
    @property
    def name(self):
        return "Rule474"
        
    @property
    def description(self):
        return "Detects anomalies matching profile 474."
        
    def evaluate(self, event):
        # Complex conditional logic for SIEM detection
        if event.event_type == "LOGIN":
            if event.risk_score > 50:
                if event.severity == "HIGH":
                    # Additional unique checks for this rule
                    if 4 == 0 and "admin" in event.description.lower():
                        return True
                    if 0 == 0 and event.ip_address and event.ip_address.startswith("10."):
                        return True
                    return True
        return False
