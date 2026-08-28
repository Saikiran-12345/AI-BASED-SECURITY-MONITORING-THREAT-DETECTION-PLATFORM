import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os
from apps.risk.models import UserBehavior

MODEL_DIR = os.path.join(os.path.dirname(__file__), '../saved_models')

class RiskPredictor:
    def __init__(self):
        self.model = LogisticRegression()
        
    def prepare_data(self):
        behaviors = UserBehavior.objects.all()
        if not behaviors:
            return None, None
            
        data = []
        for b in behaviors:
            # Predict if risk level is HIGH/CRITICAL (1) or LOW/MEDIUM (0)
            is_high_risk = 1 if b.risk_level in ['HIGH', 'CRITICAL'] else 0
            
            data.append({
                'login_freq': b.login_frequency,
                'failed_count': b.failed_login_count,
                'activity_freq': b.activity_frequency,
                'is_high_risk': is_high_risk
            })
            
        df = pd.DataFrame(data)
        X = df[['login_freq', 'failed_count', 'activity_freq']]
        y = df['is_high_risk']
        return X, y
        
    def train(self):
        X, y = self.prepare_data()
        if X is None or len(X) < 10:
            return False
            
        self.model.fit(X, y)
        joblib.dump(self.model, os.path.join(MODEL_DIR, 'risk_predictor.pkl'))
        return True
        
    def predict(self, login_freq, failed_count, activity_freq):
        try:
            self.model = joblib.load(os.path.join(MODEL_DIR, 'risk_predictor.pkl'))
        except:
            return 0
            
        pred = self.model.predict_proba([[login_freq, failed_count, activity_freq]])
        return pred[0][1] # Probability of being high risk
