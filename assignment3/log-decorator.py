# J-D Laurence

# Task 1

import logging
from pathlib import Path
LOGFILE = Path(__file__).resolve().parent / 'decorator.log'


logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO) # this means igmore anything less important, eg DEBUG
logger.addHandler(logging.FileHandler(LOGFILE,"a"))
# To write a log record:
# logger.log(logging.INFO, "this string would be logged")


#a function gets passed to the decorator and the following are logged in the log file:
# function: <the function name>
# positional parameters: <a list of the positional parameters (as a tuple or a list), or "none" if none are passed>
# keyword parameters: <a dict of the keyword parameters, or "none" if none are passed>
# return: <the return value>


# A decorator says: “Take this function or class, and pass it through another function to modify it.”

    # the first time this is run is when the program reaches the @ line, and all that happens is
    # that the function that is being decorated is passed into here and wrapper is returned instead of that function.
    # It is not until the function is actually called later with actual arguments that they are passed in and they are given 
    # to wrapper instead of to the original function, that's the whole point of decorating.
    # 
    # If we have a function that adds "world" like this:
    #   def func_decorator(func):
    #       def wrapper():      
    #           func()
    #           print("world")
    #       return wrapper

    # Then Writing
    #   @func_decorator
    #   def func1():
    #        print("Hello")
    # and then calling func1()
    # is the same as (but shorter) than writing
    #   def func1():
    #        print("Hello")
    # func1 = func_decorator(func1) where this line does the work of rebinding the function func1 to the a new version of the function
    # that wraps the original. This is what the @func_decorator is doing, simply a shorter version of rebinding.

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info( "logger decorator has been called")
        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {args or 'none'}") #more idiomatic and concise than {args if args else 'None'}
        logger.info(f"keyword parameters: {kwargs or 'none'}")
        val = func(*args, **kwargs) #call the actual function itself, that is now surrounded by logs
        logger.info(f"return: {val}")
        return val # this is needed in case the function we decorate has a return value        
    return wrapper # here we return this entire wrapper function because that is the one that will now be called when the original
                    # function is decorated and then called

@logger_decorator
def func1():
    print("Hello, World!")

@logger_decorator
def func2(*args): #this means it can take a variable number of positional arguments, and the function can access them via the args list
    return True

@logger_decorator
def func3(**kwargs):  # now the function accesses all the keywords and their values via a dict
    return logger_decorator #we return the memory address of the function itself, a bit like wrapper does

func1()
func2(1, 2, 3, 4)
func3(b=2, c=3) 