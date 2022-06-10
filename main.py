import logging

# START: python-json-logger
# from pythonjsonlogger import jsonlogger

# logger = logging.getLogger()

# logHandler = logging.StreamHandler()
# formatter = jsonlogger.JsonFormatter()
# logHandler.setFormatter(formatter)
# logger.addHandler(logHandler)
# END

# START
# from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
# import time

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
# handler = RotatingFileHandler("from_python_engineer/logging_tutorial/app.log",
#                               maxBytes=2000,
#                               backupCount=5)
# # s for seconds, m for minutes, h for hours, d for days, midnight, w0 = Monday
# # handler = TimedRotatingFileHandler('timed_test.log', when='s, interval=5, backupCount=5)

# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info("Hello, world!")
#     time.sleep(5)
# END

# START
# import traceback

# try:
#     a = [1,2,3]
#     val = a[4]
# except:
#     logging.error(f"the error is {traceback.format_exc()}")
# except IndexError as e:
#    logging.error(e, exc_info=True)
# END

# START
# import logging.config

# logging.config.fileConfig("from_python_engineer/logging_tutorial/logging.conf")
# # logging.config.dictConfig("from_python_engineer/logging_tutorial/logging.conf")

# logger = logging.getLogger("simpleExample")
# logger.debug("this is a debug message")
# END

### START
# logger = logging.getLogger(__name__)

# # create handler
# # stream is terminal
# # file is the file
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler("from_python_engineer/logging_tutorial/file.log")

# # level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# stream_f = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# file_f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# stream_h.setFormatter(stream_f)
# file_h.setFormatter(file_f)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning("this is a warning")
# logger.error("this is an error")
# END