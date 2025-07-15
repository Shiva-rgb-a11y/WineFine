import os
import sys
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from src.logger import get_logger
logger = get_logger(__name__)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.logger import get_logger
from src import utils




class DataTransformationConfig:
    def __init__(self):
        self.train_path = os.path.join("artifacts", "train.csv")
        self.test_path = os.path.join("artifacts", "test.csv")
        self.transformed_dir = os.path.join("artifacts", "transformed")

class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()
        utils.create_directories(os.path.join(self.config.transformed_dir, "dummy.txt"))

    def load_data(self):
        train_df = pd.read_csv(self.config.train_path)
        test_df = pd.read_csv(self.config.test_path)
        return train_df, test_df

    def split_X_y(self, df):
        X = df.drop("quality", axis=1)
        y = df["quality"]
        return X, y

    def transform_and_save(self):
        logger.info("🔄 Starting data transformation...")

        train_df, test_df = self.load_data()
        X_train, y_train = self.split_X_y(train_df)
        X_test, y_test = self.split_X_y(test_df)

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        np.save(os.path.join(self.config.transformed_dir, "X_train.npy"), X_train_scaled)
        np.save(os.path.join(self.config.transformed_dir, "X_test.npy"), X_test_scaled)
        np.save(os.path.join(self.config.transformed_dir, "y_train.npy"), y_train)
        np.save(os.path.join(self.config.transformed_dir, "y_test.npy"), y_test)

        logger.info("✅ Data transformation completed and files saved.")

        return X_train_scaled, X_test_scaled, y_train, y_test

