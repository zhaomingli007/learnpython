import logging
from logging import handlers
import logging.config
import traceback
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
import time
logging.config.fileConfig('logging.conf')

# logger = logging.getLogger('main')
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s-%(name)s-%(levelname)s-%(message)s', datefmt='%m/%d/%Y %H:%M:%S')

# import helper

# logger.info("hello")

logger = logging.getLogger('simpleExample')
logger.debug("this is a debug msg")

try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    # logger.error(e, exc_info=True)
    logger.error('the error is %s', traceback.format_exc())


# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
#s, m, h, d, midnight,w0
# Python json formatter
handler = TimedRotatingFileHandler('times_app.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('hello word')
    time.sleep(5)

