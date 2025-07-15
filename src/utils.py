import os
import json
import yaml
import joblib
from src.logger import get_logger

logger = get_logger(__name__)

# ✅ 1. Read YAML file
def read_yml(path_to_yaml: str) -> dict:
    try:
        with open(path_to_yaml, 'r') as file:
            data = yaml.safe_load(file)
            logger.info(f"YAML file loaded: {path_to_yaml}")
            return data
    except Exception as e:
        logger.error(f"Failed to read YAML file: {path_to_yaml} — {e}")
        raise

# ✅ 2. Create directories
def create_directories(path):
    try:
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)
        logger.info(f"Directory created or already exists: {dir_path}")
    except Exception as e:
        logger.error(f"Failed to create directories: {path} — {e}")
        raise e

# ✅ 3. Save JSON
def save_json(path: str, data: dict):
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
            logger.info(f"JSON saved: {path}")
    except Exception as e:
        logger.error(f"Failed to save JSON: {path} — {e}")
        raise

# ✅ 4. Load JSON
def load_json(path: str) -> dict:
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            logger.info(f"JSON loaded: {path}")
            return data
    except Exception as e:
        logger.error(f"Failed to load JSON: {path} — {e}")
        raise

# ✅ 5. Save binary using joblib
def save_bin(path: str, data):
    try:
        joblib.dump(data, path)
        logger.info(f"Binary data saved using joblib: {path}")
    except Exception as e:
        logger.error(f"Failed to save binary file: {path} — {e}")
        raise

# ✅ 6. Load binary using joblib
def load_bin(path: str):
    try:
        data = joblib.load(path)
        logger.info(f"Binary data loaded using joblib: {path}")
        return data
    except Exception as e:
        logger.error(f"Failed to load binary file: {path} — {e}")
        raise

# ✅ 7. Get file size in KB
def get_size(path: str) -> str:
    try:
        size = os.path.getsize(path) / 1024
        readable = f"{size:.2f} KB"
        logger.info(f"File size of {path}: {readable}")
        return readable
    except Exception as e:
        logger.error(f"Failed to get file size: {path} — {e}")
        raise
