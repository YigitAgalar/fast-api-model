import logging

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()


fmt = '%(asctime)s| %(levelname)s  %(message)s'

formatter = logging.Formatter(fmt, datefmt='%d-%m-%Y %H:%M:%S')
handler.setFormatter(formatter)
file_handler = logging.FileHandler("logdeneme.log")
file_handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(file_handler)
