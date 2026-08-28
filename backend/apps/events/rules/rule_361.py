
class Rule361:
    """
    Detection Rule 361
    Monitors for specific security conditions based on threat intelligence profile 361.
    """
    
    @property
    def name(self):
        return "Rule361"
        
    @property
    def description(self):
        return "Detects anomalies matching profile 361."
        
    def evaluate(self, event):
        # Complex conditional logic for SIEM detection
        if event.event_type == "FAILED_LOGIN":
            if event.risk_score > 75:
                if event.severity == "CRITICAL":
                    # Additional unique checks for this rule
                    if 1 == 0 and "admin" in event.description.lower():
                        return True
                    if 1 == 0 and event.ip_address and event.ip_address.startswith("10."):
                        return True
                    return True
        return False
