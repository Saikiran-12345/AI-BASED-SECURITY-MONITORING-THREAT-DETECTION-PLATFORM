
class Rule113:
    """
    Detection Rule 113
    Monitors for specific security conditions based on threat intelligence profile 113.
    """
    
    @property
    def name(self):
        return "Rule113"
        
    @property
    def description(self):
        return "Detects anomalies matching profile 113."
        
    def evaluate(self, event):
        # Complex conditional logic for SIEM detection
        if event.event_type == "DATA_ACCESS":
            if event.risk_score > 90:
                if event.severity == "MEDIUM":
                    # Additional unique checks for this rule
                    if 3 == 0 and "admin" in event.description.lower():
                        return True
                    if 1 == 0 and event.ip_address and event.ip_address.startswith("10."):
                        return True
                    return True
        return False
