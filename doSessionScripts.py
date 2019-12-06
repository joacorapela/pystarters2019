
################################################################################


def make_a_sound():
    print("quack")

make_a_sound()

################################################################################

def agree():
    return True

if agree():
    print("Splendid")
else:
    print("That was unexpected")

################################################################################

def echo(aString):
    return aString + " " + aString

print(echo("Pystarters"))

################################################################################

def greet(firstName, lastName, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", firstName + ' ' + lastName + ', ' + msg)

greet("Monica", "Garcia", "Good morning!")

################################################################################

# default argument in function definition

def greet(firstName, lastName, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", firstName + ' ' + lastName + ', ' + msg)

greet("Ann", "Robinson")
greet("Bruce", "Knight", "How do you do?")

################################################################################

# non-default arguments cannot follow default arguments

def greet(msg="Good morning!", firstName, lastName):
    """
    This function greets to
    the person with the
    provided message.

    If message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", firstName + ' ' + lastName + ', ' + msg)

################################################################################

# Problem with positional arguments: you need to remember the order of the
# arguments

def greet(firstName, lastName, msg):
    print("Hello", firstName + ' ' + lastName + ', ' + msg)

greet("How do you do?", "Bruce", "Knight")

################################################################################

# Solution: keyword arguments

# 3 keyword arguments (out of order)
greet(msg="How do you do?", lastName="Smith", firstName="Tom")

# 1 positional, 2 keyword argument
greet("Tom", lastName="Smith", msg="How do you do?")

# Error: positional arguments must preced keyword arguments
greet(firstName="Tom", "Smith", msg="How do you do?")

################################################################################

# Variable number of positional arguments

def greetMany(*names):
   """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello",name)

greetMany("Monica","Luke","Steve","John")

################################################################################

# Variable number of positional and keyword arguments

def cheeseshop(kind, *arguments, **keywords):
    # arguments is a tuple
    #  keywords is a dictionary
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", 
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

################################################################################

def multiplyMany(*numbers, scale=10):
    product = 1
    for number in numbers:
        product *= number
    return product*scale

multiplyMany(1, 2, 3)

