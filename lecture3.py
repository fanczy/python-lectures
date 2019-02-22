#######################
###### FUNCTIONS ######
#######################

def greet(name):
    print(f"Hello, {name}.")

greet("Person")

# greet() Will throw a error, because it's required argument

def greet(name="Person"): # now the argument name has default value "Person" that will be used if this argument is not filled.
    print(f"Hello, {name}.")

greet()

###########################
###### DOCUMENTATION ######
###########################

