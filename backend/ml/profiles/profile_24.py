
# ML Configuration Profile 24
# Used for tuning hyper-parameters in specific deployment scenarios

class MLProfile24:
    """
    Configuration profile for scenario 24.
    """
    def __init__(self):
        self.profile_id = "ML_PROF_24"
        self.active = True
        self.model_type = "IsolationForest" if 24 % 2 == 0 else "RandomForest"
        
        # Hyperparameters
        self.n_estimators = 100 + 24
        self.max_depth = 10 if 24 % 5 == 0 else 5
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
