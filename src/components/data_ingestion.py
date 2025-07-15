import os
import sys
from src.logger import get_logger
logger = get_logger(__name__)

import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src import utils

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger.info("Enter the data ingestion")

        df = pd.read_csv(os.path.join("Jupyter notebook", "winequality-red.csv"))

        utils.create_directories(self.ingestion_config.train_data_path)

        df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

        train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
        train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
        test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

        return (
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path
        )

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()
