# Write your code here.

#1
def hello():
    return "Hello!"

#2
def greet(name):
    return f"Hello, {name}!"

#3
def calc(a, b, operation = "multiply"):
    try:
        if operation == "add":
            return a+b
        elif operation == "subtract":
            return a-b
        elif operation == "multiply":
            return a*b
        elif operation == "divide":
            return a/b
        elif operation == "modulo":
            return a%b
        elif operation == "int_divide":
            return a//b
        elif operation == "power":
            return a**b
        else:
            return "Unknown operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except Exception:
        return "You can't multiply those values!"
    

#4
def data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)
        elif type == "float":
            return float(value)
        elif type == "str":
            return str(value)
    except Exception:
        return f"You can't convert {value} into a {type}."
    

#5
def grade(*args):
    try:
        number_of_parametrs = len(args)
        total_of_parametrs = sum(args)
        average = total_of_parametrs / number_of_parametrs
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        elif average < 60:
            return "F"
    except Exception:
        return "Invalid data was provided."


#6
def repeat(string, count):
    result= ""
    for i in range(count):
        result += string
    return result


#7
def student_scores(mode, **kwargs):
    if mode == "mean":
        total= 0
        for i in kwargs.values():
           total += i
        average = total / len(kwargs)
        return average
    elif mode == "best":
        best_name = None
        best_score = 0
        for name, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_name = name
        return best_name


#8
def titleize(text):
    small_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()
    for index, w in enumerate(words):
        if index == 0:
            words[index] = w.capitalize()
        elif index == len(words) - 1:
            words[index] = w.capitalize()
        elif w in small_words:
            words[index] = w
        else:
            words[index] = w.capitalize()
    return " ".join(words)



#9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


#10
def pig_latin(text):
    vowel = ["a", "e", "i", "o", "u"]
    words = text.split()
    pig_latin_words = []

    for word in words:
        if word[0] in vowel:
            pig_latin_words.append(word + "ay")

        elif word.startswith("qu"):
            pig_latin_words.append(word[2:] + "qu" + "ay")
        
        elif word.startswith("squ"):
            pig_latin_words.append(word[3:] + "squ" + "ay")

        else:
            prefix = ""

            while word[0] not in vowel:
                prefix += word[0]
                word = word[1:]
            pig_latin_words.append(word + prefix + "ay")

    return " ".join(pig_latin_words)