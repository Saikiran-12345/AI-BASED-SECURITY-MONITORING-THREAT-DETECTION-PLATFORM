
# ML Configuration Profile 12
# Used for tuning hyper-parameters in specific deployment scenarios

class MLProfile12:
    """
    Configuration profile for scenario 12.
    """
    def __init__(self):
        self.profile_id = "ML_PROF_12"
        self.active = True
        self.model_type = "IsolationForest" if 12 % 2 == 0 else "RandomForest"
        
        # Hyperparameters
        self.n_estimators = 100 + 12
        self.max_depth = 10 if 12 % 5 == 0 else 5
        self.random_state = 42
        
        # Feature selection
        self.features = [
            "login_failures",
            "data_exfiltration_bytes",
            "unusual_hours_access",
            "privilege_escalation_attempts"
        ]
        
    def get_config_dict(self):
        return {
            "n_estimators": self.n_estimators,
            "max_depth": self.max_depth,
            "random_state": self.random_state
        }
        
    def is_compatible(self, model_version):
        return model_version >= 2.0
