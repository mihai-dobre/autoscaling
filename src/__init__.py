import logging

__version__ = "1.0"

logger = logging.getLogger()
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
log_file_handler = logging.FileHandler("pds.log")
fmt = logging.Formatter("%(asctime)s : %(message)s")
log_file_handler.setFormatter(fmt)
logger.addHandler(log_file_handler)
