
class Rule004:
    """
    Detection Rule 4
    Monitors for specific security conditions based on threat intelligence profile 4.
    """
    
    @property
    def name(self):
        return "Rule004"
        
    @property
    def description(self):
        return "Detects anomalies matching profile 4."
        
    def evaluate(self, event):
        # Complex conditional logic for SIEM detection
        if event.event_type == "FAILED_LOGIN":
            if event.risk_score > 75:
                if event.severity == "CRITICAL":
                    # Additional unique checks for this rule
                    if 4 == 0 and "admin" in event.description.lower():
                        return True
                    if 0 == 0 and event.ip_address and event.ip_address.startswith("10."):
                        return True
                    return True
        return False
