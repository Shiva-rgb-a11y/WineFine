import os 
import sys
from src.logging import get_logger
logger = get_logger(__name__)
import pandas as pd 
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src import utils

class DataValidation:
    def __init__(self, data_path: str, schema_path: str):
        self.data_path = data_path
        self.schema_path = schema_path
        self.schema = utils.read_yml(self.schema_path)

    def validate_column_name(self, df: pd.DataFrame):
        expected_columns = list(self.schema['columns'].keys())
        if list(df.columns) != expected_columns:
            raise ValueError(f"❌ Column mismatch!\nExpected: {expected_columns}\nFound: {list(df.columns)}")
        logging.info("✅ Column names are valid.")

    def validate_column_types(self, df: pd.DataFrame):
        for col, expected_type in self.schema['columns'].items():
            if col not in df.columns:
                raise ValueError(f"❌ Missing column: {col}")
            if expected_type == "float" and not pd.api.types.is_float_dtype(df[col]):
                raise TypeError(f"❌ Column '{col}' expected to be float but found {df[col].dtype}")
            elif expected_type == "int" and not pd.api.types.is_integer_dtype(df[col]):
                raise TypeError(f"❌ Column '{col}' expected to be int but found {df[col].dtype}")
        logging.info("✅ Column data types are valid.")

    def validation_run(self):
        df = pd.read_csv(self.data_path)
        self.validate_column_name(df)
        self.validate_column_types(df)
        logging.info("✅ Data validation complete.")
        return True
