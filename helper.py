import logging

logger = logging.getLogger(__name__)
# logger.propagate = False
logger.info("this is a info message from helper")

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Set level
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
formatter = logging.Formatter(
    '%(asctime)s-%(name)s-%(levelname)s-%(message)s', datefmt='%m/%d/%Y %H:%M:%S')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning(" this is a warning")
logger.error(" this is a error")