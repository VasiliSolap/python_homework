#task 1
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"function: {func.__name__}")
        if args:
            logger.log(logging.INFO, f"positional parameters: {args}")
        else:
            logger.log(logging.INFO, f"positional parameters: none")

        if kwargs:
            logger.log(logging.INFO, f"keyword parameters: {kwargs}")
        else:
            logger.log(logging.INFO, f"keyword parameters: none") 

        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"return {result}")
        return result
    return wrapper


@logger_decorator
def no_params():
    print("Hello, World!")


@logger_decorator
def only_positional(*args):
    return True


@logger_decorator
def only_keywords(**kwargs):
    return logger_decorator


no_params()
only_positional(1, 2, 3)
only_keywords(x=10, y=20)