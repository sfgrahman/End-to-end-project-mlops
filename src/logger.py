import os
import sys
import logging
from datetime import datetime

FORMAT ="%m_%d_%Y_%H_%M_%S"
# filename
LOG_FILE = f"{datetime.now().strftime(FORMAT)}.log"

# join and create log file directory
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(log_path, exist_ok=True)

# Full directory path
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    
)

# if __name__=="__main__":
#     logging.info("Logging started")
    