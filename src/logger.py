import logging
import os

def get_logger(name=__name__, log_file='logs/app.log'):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)  # ✅ same clean format

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        # ✅ Optional: disable propagation to root logger
        logger.propagate = False

    return logger
