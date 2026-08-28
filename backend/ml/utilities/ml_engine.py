import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from apps.events.models import SecurityEvent
import joblib
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), 'saved_models')
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

class MLEngine:
    def __init__(self):
        self.iso_forest = None
        self.classifier = None
        self.scaler = StandardScaler()
        
    def extract_features(self, events):
        # Very simple feature extraction for demonstration
        # In a real scenario, this would aggregate by user/session
        df = pd.DataFrame(list(events.values('id', 'user_id', 'event_type', 'severity', 'risk_score')))
        
        if df.empty:
            return df
            
        # Feature Engineering: 
        # map severity to int
        sev_map = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3, 'CRITICAL': 4}
        df['sev_num'] = df['severity'].map(sev_map).fillna(1)
        
        # map event type to dummy/frequency
        freq = df['event_type'].value_counts().to_dict()
        df['event_freq'] = df['event_type'].map(freq)
        
        features = df[['sev_num', 'risk_score', 'event_freq']]
        return features, df

    def train_anomaly_model(self):
        events = SecurityEvent.objects.all()
        features, df = self.extract_features(events)
        
        if features.empty or len(features) < 10:
            return False
            
        scaled = self.scaler.fit_transform(features)
        
        self.iso_forest = IsolationForest(contamination=0.05, random_state=42)
        self.iso_forest.fit(scaled)
        
        joblib.dump(self.iso_forest, os.path.join(MODEL_DIR, 'iso_forest.pkl'))
        joblib.dump(self.scaler, os.path.join(MODEL_DIR, 'scaler.pkl'))
        
        return True

    def detect_anomalies(self):
        try:
            self.iso_forest = joblib.load(os.path.join(MODEL_DIR, 'iso_forest.pkl'))
            self.scaler = joblib.load(os.path.join(MODEL_DIR, 'scaler.pkl'))
        except:
            if not self.train_anomaly_model():
                return []
                
        events = SecurityEvent.objects.all().order_by('-id')[:100] # Check latest 100
        if not events:
            return []
            
        features, df = self.extract_features(events)
        scaled = self.scaler.transform(features)
        
        preds = self.iso_forest.predict(scaled)
        # -1 is anomaly, 1 is normal
        df['is_anomaly'] = preds == -1
        
        anomalies = df[df['is_anomaly']]
        return anomalies['id'].tolist()
