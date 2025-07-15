import os
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.logger import get_logger
logger = get_logger(__name__)
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
if __name__ == "__main__":
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    validator = DataValidation(
        data_path=os.path.join('artifacts', 'data.csv'),
        schema_path=os.path.join('schema.yaml')
    )

    try:
        validator.validation_run()

        # ✅ Run these only if validation succeeds
        transformer = DataTransformation()
        x_train, x_test, y_train, y_test = transformer.transform_and_save()

        trainer = ModelTrainer()
        trainer.run()

        logger.info("✅ Pipeline completed successfully.")

    except Exception as e:
        logger.error(f"❌ Pipeline failed due to: {e}")
        raise e
