import logging
import os
from datetime import datetime
log_file=f"{datetime.now().strftime("%m-%d-%Y,%H:%M:%S")}"
path=os.path.join(os.getcwd(),"log")
os.makedirs(path,exist_ok=True)
logging.basicConfig(filename=path,format="[%(asctime)s]%(lineno)d%(name)s %(levelname)s %(message)s")