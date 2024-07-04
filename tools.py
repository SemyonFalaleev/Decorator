import logging
from functools import wraps
import datetime
def setup_logger(path="main.log"):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(path)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    
    return logger

def logger(old_function):
    logger = setup_logger()
    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        logger.info(f"name function : {new_function.__name__}, datatime : {datetime.datetime.now()},"
                    f" *args : {args}, *kwargs : {kwargs}, return : {result} ")
        return result
    return new_function

def logger_params(path):
    def logger(old_function):
        logger = setup_logger(path)
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            logger.info(f"name function : {new_function.__name__}, datatime : {datetime.datetime.now()},"
                        f" *args : {args}, *kwargs : {kwargs}, return : {result} ")
            return result
        return new_function
    return logger
    
    