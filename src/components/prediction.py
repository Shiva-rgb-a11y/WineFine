import os
import sys
import numpy as np
import pandas as pd
import joblib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.logger import get_logger
from src import utils

logger = get_logger(__name__)

class PredictionPipeline:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model", "model.joblib")
        self.scaler_path = os.path.join("artifacts", "transformed", "scaler.joblib")  # optional if using
        self.model = None
        self.scaler = None

    def load_model(self):
        logger.info("🔍 Loading trained model...")
        self.model = joblib.load(self.model_path)
        logger.info(f"✅ Model loaded from: {self.model_path}")

    def predict(self, input_data: pd.DataFrame):
        if self.model is None:
            self.load_model()

        logger.info("📊 Performing prediction...")
        predictions = self.model.predict(input_data)
        logger.info("✅ Prediction complete.")
        return predictions
