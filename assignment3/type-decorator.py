# J-D Laurence

# Task 3

# Declare a decorator called type_converter. It has one argument called type_of_output,
# which would be a type, like str or int or float. 
# It should convert the return from func to the corresponding type.

def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # extra behaviour to decorate the original behaviour of func
            # use type_of_output here too
            result = func(*args, **kwargs)
            return type_of_output(result) # convert the type
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen

