# J-D Laurence
# 6 October 2026

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
            
# print(grade(90, 80, 70))
# print(grade(100, "apple", 20))

#Task 6
def repeat(input_str, count):
    output_str = ""
    for i in range(count):
        output_str += input_str
    return output_str

# print(repeat("Hello", 5))

# Task 7
def student_scores(score_type,**kwargs):
    if score_type == "best":
        return max(kwargs, key=kwargs.get)
    elif score_type == "mean":
        total = sum(kwargs.values())
        mean = total / len(kwargs)
        return mean
    
# print(student_scores("best", Alice=90, Bob=85, Charlie=95))
# print(student_scores("mean", Alice=90, Bob=85, Charlie=95))

# Task 8
def titleize(input_str):
    excluded = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = input_str.split()
    first = words[0].capitalize()
    last = words[-1].capitalize()
    words.pop(0) #remove first
    words.pop() #remove last
    middle_words = words #remaining ones we check for excluded words
    #print(middle_words)
    for i, word in enumerate(middle_words):
        if word not in excluded:
            middle_words[i] = word.capitalize()

    if len(middle_words) == 0:        
        mid_word_str = ""
    else:
        mid_word_str = " ".join(middle_words) + " "
    output_str = first + " " + mid_word_str + last
    return output_str

# print(titleize("the quick brown fox jumps over the lazy dog"))
# print(titleize("a tale of two cities"))

# Task 9
def hangman(secret, guess):
    secret_list = list(secret.lower())
    guess_list = list(guess.lower())
    output_list = []
    for char_s in secret_list:
        if char_s in guess_list:
            output_list.append(char_s)
        else:
            output_list.append("_")

    return "".join(output_list)

#print(hangman("alphabet", "ab"))

# Task 10

def pig_latin(input_str):
    input_words = input_str.split()
    output_words = []
    for word in input_words:
        input_list = list(word)
        output_list = input_list.copy()

        vowels = ["a", "e", "i", "o", "u"]
    
        for i, char in enumerate(input_list):
            if char in vowels:
                break
            else:
                if (char =="q" and input_list[i+1] == "u"):
                    output_list.append(char) # add consonant to the end
                    output_list.append("u")
                    del output_list[:2] # get rid of consonant at the beginning
                else:
                    output_list.append(char) # add consonant to the end
                    del output_list[0] # get rid of consonant at the beginning
    
        output_list.append("ay")
        output_word = "".join(output_list)
        output_words.append(output_word)
    return " ".join(output_words)

#print(pig_latin("square brown fox"))

