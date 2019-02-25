#######################
###### FUNCTIONS ######
#######################

def greet(name):
    print(f"Hello, {name}.")

greet("Person")

# greet() Will throw a error, because it's required argument

def greet_with_greeting(greeting, name="Person"): # Now the argument name has default value "Person" that will be used if this argument is not filled.
    print(f"{greeting}, {name}.")

greet_with_greeting("What's up")
greet_with_greeting("What's up", "man")


def give_answer(question):
    return 42 # Functions can return value that can be used later or stored in variable.
 
answer = give_answer("Ultimate question of life, the universe, and everything.")
print(answer)


def root(number, n):
    return number ** (1/n)

print(root(9,2)) 
print(root(-9,2)) # Python is so complex, yet so simple.

def multigreet(*names): # Puts all arguments into tuple.
    for name in names:
        greet(name)

multigreet("Hynek", "Vilem", "Jarmila")

def keyword_args(**kwargs): # Puts arguments with keywords into dictionary.
    print(kwargs)

# def multigreet_with_greeting(*names, **greetings):

    

##### excercises #####
# Write a function that determines if number is dividable by another number.
# Write a function that prints if number is dividable by another number as a sentencte example: print_dividable(4,2) prints "Number 4 is dividable by number 2."
######################




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