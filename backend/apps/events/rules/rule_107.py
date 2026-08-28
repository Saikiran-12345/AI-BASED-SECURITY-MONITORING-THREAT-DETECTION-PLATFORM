
class Rule107:
    """
    Detection Rule 107
    Monitors for specific security conditions based on threat intelligence profile 107.
    """
    
    @property
    def name(self):
        return "Rule107"
        
    @property
    def description(self):
        return "Detects anomalies matching profile 107."
        
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
