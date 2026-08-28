
# ML Configuration Profile 196
# Used for tuning hyper-parameters in specific deployment scenarios

class MLProfile196:
    """
    Configuration profile for scenario 196.
    """
    def __init__(self):
        self.profile_id = "ML_PROF_196"
        self.active = True
        self.model_type = "IsolationForest" if 196 % 2 == 0 else "RandomForest"
        
        # Hyperparameters
        self.n_estimators = 100 + 196
        self.max_depth = 10 if 196 % 5 == 0 else 5
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
