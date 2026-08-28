import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

from apps.events.models import SecurityEvent
from apps.threats.models import ThreatCategory

MODEL_DIR = os.path.join(os.path.dirname(__file__), 'saved_models')

class MLClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        
    def prepare_data(self):
        # We need historical events that resulted in threats
        events = SecurityEvent.objects.all()
        if not events:
            return None, None
            
        data = []
        for e in events:
            # Did this event result in a threat?
            threat = e.threats.first()
            label = threat.category if threat else 'NORMAL'
            
            # Simple features
            sev_map = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3, 'CRITICAL': 4}
            data.append({
                'sev': sev_map.get(e.severity, 1),
                'risk': e.risk_score,
                'label': label
            })
            
        df = pd.DataFrame(data)
        X = df[['sev', 'risk']]
        y = df['label']
        return X, y
        
    def train(self):
        X, y = self.prepare_data()
        if X is None or len(X) < 20:
            return False
            
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model.fit(X_train, y_train)
        preds = self.model.predict(X_test)
        
        acc = accuracy_score(y_test, preds)
        print(f"Model trained with accuracy: {acc}")
        
        joblib.dump(self.model, os.path.join(MODEL_DIR, 'rf_classifier.pkl'))
        return True
        
    def predict(self, event):
        try:
            self.model = joblib.load(os.path.join(MODEL_DIR, 'rf_classifier.pkl'))
        except FileNotFoundError:
            return 'UNKNOWN'
            
        sev_map = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3, 'CRITICAL': 4}
        sev = sev_map.get(event.severity, 1)
        risk = event.risk_score
        
        pred = self.model.predict([[sev, risk]])
        return pred[0]
