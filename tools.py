import logging
from functools import wraps
import datetime
def setup_logger(function, path="main.log"):
    logger = logging.getLogger(function.__name__)
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        for handler in logger.handlers:
            if isinstance(handler, logging.FileHandler):
                handler.close()
                logger.removeHandler(handler)
        file_handler = logging.FileHandler(path)
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        return logger
    else:
        file_handler = logging.FileHandler(path)
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)
    return logger

def logger(old_function):
    logger = setup_logger(old_function)
    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        logger.info(f"name function : {old_function.__name__}, datatime : {datetime.datetime.now()},"
                    f" *args : {args}, *kwargs : {kwargs}, return : {result} ")
        return result
    return new_function

def logger_params(path):
    def logger(old_function):
        logger = setup_logger(old_function, path=path)
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            logger.info(f"name function : {old_function.__name__}, datatime : {datetime.datetime.now()},"
                        f" *args : {args}, *kwargs : {kwargs}, return : {result} ")
            return result
        return new_function
    return logger
    
    