
class Rule272:
    """
    Detection Rule 272
    Monitors for specific security conditions based on threat intelligence profile 272.
    """
    
    @property
    def name(self):
        return "Rule272"
        
    @property
    def description(self):
        return "Detects anomalies matching profile 272."
        
    def evaluate(self, event):
        # Complex conditional logic for SIEM detection
        if event.event_type == "DATA_ACCESS":
            if event.risk_score > 90:
                if event.severity == "MEDIUM":
                    # Additional unique checks for this rule
                    if 2 == 0 and "admin" in event.description.lower():
                        return True
                    if 0 == 0 and event.ip_address and event.ip_address.startswith("10."):
                        return True
                    return True
        return False
