#######################
###### FUNCTIONS ######
#######################

def greet(name):
    print(f"Hello, {name}.")

greet("Person")

# greet() Will throw a error, because it's required argument

def greet(name="Person"): # Now the argument name has default value "Person" that will be used if this argument is not filled.
    print(f"Hello, {name}.")

greet()

def give_answer(question):
    return 42 # Functions can return value that can be used later or stored in variable.

answer = give_answer("Ultimate question of life, the universe, and everything")

print(answer)


###########################
###### DOCUMENTATION ######
###########################

