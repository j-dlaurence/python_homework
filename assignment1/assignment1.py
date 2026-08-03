# J-D Laurence

# Task 1
def hello():
    return "Hello!"

#print(hello())

# Task 2
def greet(name):
    return "Hello, " + name + "!"

#print(greet("Name"))

#Task 3
def calc(a, b, op="multiply"):
    try:
        match op:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    except Exception as e:
        return "An error has occured: " + str(e)


# print(calc(5, 0, "divide"))
# print(calc(5, 1, "modulo"))
# print(calc(1,2, "add"))
# print(calc("apple", "banana"))

# Task 4
def data_type_conversion(value, type_name):
    try:
        match type_name:
            case "int":
                return int(value)
            case "str":
                return str(value)
            case "float":
                return float(value)
            case _:
                return "Invalid type; choose int, float or string"

    except ValueError:
        return "You can't convert " + value + " into a " + type_name +"."

# print(data_type_conversion("5", "int"))
# print(data_type_conversion(5, "str"))
# print(data_type_conversion("3.14", "float"))
# print(data_type_conversion("5", "bool"))
# print(data_type_conversion("apple", "int"))

# Task 5
def grade(*args):
    try:
        total = sum(args)
        avg = total / len(args)

        match avg:
            case avg if avg  >= 90:
                return "A"
            case avg if avg >= 80:
                return "B"
            case avg if avg >= 70:
                return "C"
            case avg if avg >= 60:
                return "D"
            case avg if avg < 60:
                return "F" 
    except Exception:
        return "Invalid data was provided."
            
print(grade(90, 80, 70))
print(grade(100, "apple", 20))

