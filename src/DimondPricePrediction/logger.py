import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs")

os.makedirs(os.path.dirname(log_path),exist_ok=True)

Log_file_path=os.path.join(log_path,LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    filename=Log_file_path,
                    format="[%(asctime)s] %(lineno)d %(name)s- %(levelname)s- %(message)s" 

                              )
if __name__ =='__main__':
    logging.info("This is a test message")