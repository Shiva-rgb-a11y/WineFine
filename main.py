import os
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.logging import get_logger
logger = get_logger(__name__)


if __name__ == "__main__":
    ingestion = DataIngestion()  # ✅ create object of class
    train_path, test_path = ingestion.initiate_data_ingestion()  # ✅ call the method

    validator = DataValidation(  # ✅ create object of class
        data_path=os.path.join('artifacts', 'data.csv'),
        schema_path=os.path.join('schema.yaml')
    )

    try:
        validator.validation_run()
    except Exception as e:
        print(f"❌ Validation failed: {e}")
