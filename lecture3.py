#######################
###### FUNCTIONS ######
#######################

def greet(name):
    print(f"Hello, {name}.")

greet("Person")

# greet() Will throw a error, because it's required argument

def greet_with_greeting(name, greeting="Hello"): # Now the argument greeting has default value "Hello" that will be used if this argument is not filled.
    print(f"{greeting}, {name}.")

greet_with_greeting("Person")
greet_with_greeting("man", "What's up")


def give_answer(question):
    return 42 # Functions can return value that can be used later or stored in variable.
 
answer = give_answer("Ultimate question of life, the universe, and everything.")
print(answer)


def root(number, n):
    return number ** (1/n)

print(root(9,2)) 
print(root(-9,2)) # Python is so complex, yet so simple.

##### excercises #####
# Write a function that determines if number is dividable by another number.
# Write a function that prints if number is dividable by another number as a sentencte example: print_dividable(4,2) prints "Number 4 is dividable by number 2."
######################

def multigreet(*names): # Puts all arguments into tuple.
    for name in names:
        greet(name)

multigreet("Hynek", "Vilem", "Jarmila")

def print_expensive_fruits(**priced_fruits): # Puts arguments with keywords into dictionary.
    for fruit in priced_fruits:
        if(priced_fruits[fruit] > 4):
            print(fruit)

print_expensive_fruits(apple = 1, melon = 5, pomelo = 7, orange = 2)

def multigreet_with_greeting(*names, **greetings): # You can combine 
    for name in names:
        if(name in greetings):
            greet_with_greeting(name, greetings[name])
        else:
            greet(name)

multigreet_with_greeting("Hynek", "Vilem", "Jarmila", Hynek="Hey", Jarmila="How are you")

##### excercise #####
# Write a function gather_fruits, that gets n strings as fruits, and then n keyword aguments of containers with list of fruits that goes into them
# the function will write which fruit goes to which container, if there is no container for the fruit, then it stays on floor
# EXAMPLE: gather_fruits("apple", "pear", "melon", "pomelo", basket=["apple", "pear"], crate=["melon"]) prints:
# apple goes to basket
# pear goes to basket
# melon goes to crate
# pomelo stays on ground
# ######################

number = 1

def scope_test():
    number = 2
    def enclosed_scope_test():
        number = 3 # If you use multiple variables with same name, the closest one will be used, first in the scope, then enclosing function and last in global space.
        print(number)
    enclosed_scope_test()

scope_test()

def scope_variable_change(number):
    number = 5 # If you change value of variable passed as argument, the original value will not be changed.
    print(number)

scope_variable_change(number)
print(number)

def global_variable_change():
    global number # AVOID overwrithing global variables, unless it's necesarry. It's generally bad practice and can lead to many mistakes.
    number = 7

global_variable_change()
print(number)


def greet_input_name():
    name = input("Enter name: ")
    greet(name)

# greet_input_name()

def start_super_program_9001():
    print("Welcome to Super Program 9001.\nEnter '?' for help.")
    command = None
    while(command != "exit"):
        command = input("Enter command: ")
        process_command(command)

def process_command(command):
    if(command == "?"):
        super_program_9001_help()
    elif(command == "greet"):
        greet_input_name()
    elif(command == "exit"):
        print("Good bye.")
    else:
        print(f"Error: unknown command '{command}'.")

def super_program_9001_help():
    print(f""" 
        AVAILABLE COMMANDS:
        ? - Prints help.
        greet - Greets you.
        exit - Closes Super Program 9001.
    """)

start_super_program_9001()


##########################
##### DOCUMENTATION ######
##########################

help(print)

def doc_test(echo):
    '''
    This text will appear in help(doc_test)\n
    INPUT:
        echo - value to be returned   
    OUTPUT:
        returns echo
    '''
    return echo

help(doc_test)

##### HOMEWORK #####
# Basic calculator
# Calculator will ask you to input first number until it's a valid number, 'exit', or 'clear' command.
# Then it will ask you to input valid operation ('+','-','*','/','exit','clear').
# Then it will ask you to input another valid number (or 'exit', 'clear' commands).
# Calculator will print the calculation with result.
# Then it will ask you to input another operation and the last result will be used as first number in operation.
# This will process will repeat until 'exit' is input (as a number or as a command).
# Inputting 'exit' as a number, or operation ends the calculator.
# Inputting 'clear' as a number, or operation will reset the calculator and let you input first number.
# This calculator will be really basic, so it will not work with parenthesis and operator precedence.
##### EXAMPLE #####
# Enter number: 1
# Choose operation: +
# Enter number: 4
# 1 + 4 = 5
# Enter operation: blabla
# Unknown operation
# Enter operation: *
# Enter number: qwejklhrkqjlh
# Invalid number
# Enter number: 4
# 5 * 4 = 20
# Enter operation: clear
# Enter number: -7
# Enter operation: -
# Enter number: -49
# -7 - -49 = 42
# Enter operation: /
# Enter number: exit
