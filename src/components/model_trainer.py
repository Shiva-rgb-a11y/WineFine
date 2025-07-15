import os
import sys
import numpy as np 
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score
import joblib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.logger import get_logger

logger = get_logger(__name__)

class ModelTrainerConfig:
    def __init__(self):
        self.model_dir = os.path.join('artifacts', 'model')
        self.model_path = os.path.join(self.model_dir, 'model.joblib')
        self.metrics_path = os.path.join(self.model_dir, "metrics.json")

class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()

        print("✅ Model directory path:", self.config.model_dir)

        try:
            if not os.path.exists(self.config.model_dir):
                os.makedirs(self.config.model_dir)
                print("📁 Model directory created.")
            else:
                print("📁 Model directory already exists.")
        except Exception as e:
            print("❌ Error while creating model directory:", e)

            
    def train(self, x_train, y_train):
        logger.info("🔧 Training ElasticNet model...")
        model = ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42)
        model.fit(x_train, y_train)
        return model
    
    def evaluate_and_save(self, model, x_test, y_test):
        logger.info("📊 Evaluating model performance...")
        y_pred = model.predict(x_test)
        r2 = r2_score(y_test, y_pred)
        logger.info(f"✅ R2 Score: {r2:.4f}")

        joblib.dump(model, self.config.model_path)
        logger.info(f"📦 Model saved at: {self.config.model_path}")

        with open(self.config.metrics_path, "w") as f:
            import json
            json.dump({"r2_score": r2}, f, indent=4)
        logger.info(f"📊 Metrics saved at: {self.config.metrics_path}")

        return r2
    
    def run(self):
        logger.info("🚀 Starting model training pipeline...")

        x_train = np.load(os.path.join("artifacts", "transformed", 'X_train.npy'))
        x_test = np.load(os.path.join("artifacts", "transformed", 'X_test.npy'))
        y_train = np.load(os.path.join("artifacts", "transformed", 'y_train.npy'))
        y_test = np.load(os.path.join("artifacts", "transformed", 'y_test.npy'))

        model = self.train(x_train, y_train)
        score = self.evaluate_and_save(model, x_test, y_test)

        logger.info("🏁 Model training pipeline finished.")
        return score
