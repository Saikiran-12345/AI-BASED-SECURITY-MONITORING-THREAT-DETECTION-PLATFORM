
class Rule377:
    """
    Detection Rule 377
    Monitors for specific security conditions based on threat intelligence profile 377.
    """
    
    @property
    def name(self):
        return "Rule377"
        
    @property
    def description(self):
        return "Detects anomalies matching profile 377."
        
    def evaluate(self, event):
        # Complex conditional logic for SIEM detection
        if event.event_type == "DATA_ACCESS":
            if event.risk_score > 90:
                if event.severity == "MEDIUM":
                    # Additional unique checks for this rule
                    if 2 == 0 and "admin" in event.description.lower():
                        return True
                    if 1 == 0 and event.ip_address and event.ip_address.startswith("10."):
                        return True
                    return True
        return False
