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

def multigreet_with_greeting(*names, **greetings):
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



###########################
###### DOCUMENTATION ######
###########################

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