import logging
import os


class MyLogger:
    @staticmethod
    def getLogger():
        """

        """
        logger = logging.getLogger("my_logger")
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_path = os.path.join(os.path.abspath(os.curdir),'logs','test_log.log')
        file_handler = logging.FileHandler(file_path)

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger