import inspect
import logging


class BaseClass:

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # catches file name

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: <%(name)s> : %(message)s")

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # filehandler object into it

        logger.setLevel(logging.INFO)
        # logger.debug("a debug statement is executed")
        # logger.info("Information statement")  # not related to errors
        # logger.warning("Something is in warning mode")
        # logger.error("A major error has happened")
        # logger.critical("Critical issue")

        return logger
