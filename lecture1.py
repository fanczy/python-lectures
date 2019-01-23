print("===============")

# install Python plugin from vsix
# VSCode: CTRL + SHIFT + P 
# Select interpreter
# F2 + install refactoring plugin
# F5 + install linter

# why python?

# fast learning curve
# large community


# easy to read
# print("Hello world")
#   vs. 
# public class HelloWorld {
#
#    public static void main(String[] args) {
#        System.out.println("Hello, World");
#    }
#}

# demanded on market
# modern
# dynamic typing (convenient but slow and hard to maintain)

print("hello world")
print("hello", "world")

# types: int, float, string, list, tup, set, dict, bool

###################
##### NUMBERS #####
###################
a = 5
b = 2


print(a + b)
print(a - b)
print(a * b)
print(a / b) # returns floating point number
print(a // b) # floor division
print(a % b) # modulo - division remainder
print(a ** b) # power

a = a + 1 # adding 1 to a
print(a)
a += 1
print(a) # adding 1 to a, shortened

print(4 * (2 + 3) ** 2) # parenthesis before power before multiplication/division before addition/substraction

##### excercises #####
# square root
# how to tell if number is even
######################

###################
##### STRINGS #####
###################

message = "Hello world"
print(message)
print("I'm alive") # combination of single/double quotation marks allows use of quotes without string termination
print('He said: "I\'m alive"')  # I can put backslash to "escape" the character so the quote mark doesn't terminate the string
print('Hello\nHello')
print(message[0]) # first character (strings are immutable - can't change character on index)
print(message[-1]) # first character from end (last character)

###################
# STRING SLICING  #
###################

#[start-index-included, stop-index-ecluded, step]

print(message[6:]) # slice from seventh character (index 6 included) to end
print(message[:4]) # slice from start to fourth character (index 4 excluded)
print(message[1:5]) # slice from second to fifth character
print(message[6::2]) # every second character from seventh character to end
print(message[::-1]) # reversed string (whole string from start to end, with -1 step)

#####################
# STRING FORMATTING #
#####################

greeting = message[:5]
name = "Person"

print(message.upper()) # one of basic string functions - converts string to upper case
print(greeting + name) # string joining
print(greeting + ", " + name + "." * 3) # string multiplication
print("{}, {}.".format(greeting, name)) # basic string format operations
print("{1}, {0}.".format(greeting, name))
print("{g} {n}!".format(g = greeting, n = name))
print("{g} {g}!".format(g = greeting, n = name))

print(f"{greeting}, {name}.") # string interpolation
print(f"{name}, {greeting.lower()}.")

pi_approx = 355 / 113

print(f"{pi_approx:1.6f}") # floating number formatting: one number before decimal point, six nubmers after decimal point


print(len(message)) # returns string length
print(message.__len__()) # same as above

##### excercises #####
# make "abaBABAbababa" into "aaaaaaaBBBBBB"
# make "abaBABAbababa" into BAba
######################

###################
###### LISTS ######
###################

numbers = "zero one two three four".split() # splits by space
print(numbers)
numbers = ", ".join(numbers) # joins with ", " between values
print(numbers)
numbers = numbers.split(", ") # splits by ", "
print(numbers)

numbers_extension = [5, "six"] # list creation, can combine different types
extended_numbers = numbers + numbers_extension # list concatenation
print(extended_numbers)

extended_numbers[5] = "five" # changing item in list
extended_numbers.append("seven") # appending to end of list
print(extended_numbers) 

extended_numbers.pop() # popping last item from list
print(extended_numbers)  

zero = extended_numbers.pop(0) # popping item at index zero from list, pop() function returns popped item
print(extended_numbers) 
print(zero) # popped item

extended_numbers.reverse() # reverses list
print(extended_numbers)

numbers = [2,1,3]
print(numbers)

numbers.sort() # sorting list of items
print(numbers)

print(numbers)

letters = ["c", "a", "b"] # sorting works on characters as well as numbers
letters.sort()
print(letters) 

# ! sort() function can't sort mixed type lists

##### excercises #####
# sequence [5, 8, 1, 0, 3, 7, 4, 2, 6, 9] 
# print in order from largest to smallest
# print odd numbers from smallest to largest
# get even numbers bigger than four from largest to smallest
# how to make all these excercises in least lines?
######################

####################
###### TUPLES ######
####################

vector = (1, 2, 1) # - immutable lists, if I need to be sure the data can't be changed
print(vector[0])


##### excercises #####
# vector addition
######################

##################
###### SETS ######
##################

fruits = {"apple", "pear"} # - every entry appears once, cant index in set
print(fruits)

fruits.add("orange")
print(fruits)

fruits.add("apple")
print(fruits)

repeated_values = [1, 2, 1, 3, 2, 1, 2, 2, 3]
print(set(repeated_values))

##### excercises #####
# which letters were used in string "Popokatepetl"
######################

##########################
###### DICTIONARIES ######
##########################

print("===============")

prices = {
    "apple": 1,
    "mango": 2
}
print(prices)
print(prices["apple"])

prices["apple"] = {
    "red": 1,
    "green": 0.9
}
print(prices["apple"]["green"])

print(prices.keys())
print(prices.values())
print(prices.items())

######################
###### BOOLEANS ######
######################

to_be = True # must have capital T
print(to_be)
print(type(True))
print(type("true"))

##################################
###### COMPARISON OPERATORS ######
##################################

print(2 == 2) # one = sign is value assignment therefore == is used for comparison
print(1 != 2)
print(1 > 2)
print(1 <= 2)
print(1 < 2 < 3)

print(2 == 2.0)
print(2 == "2")
print("hello" != "hi")
print("Hello" == "hello")
print(["a","b"] == ["a", "b"])
print(["a","b"] == ["b", "a"]) # same with tuples
print({"a","b"} == {"b","a"}) # order doesn't matter
print({"lock1":"key1", "lock2":"key2"} == {"lock2":"key2", "lock1":"key1"} )

###############################
###### LOGICAL OPERATORS ######
###############################

print(True and False)
print(True or False)
print(not True)
print(1 > 2 and 2 < 5)
print(to_be or not to_be)
print(False and True or True) # and precedes or
print(False and (True or True))


##### HOMEWORK #####
# check if two vectors are the same length
# check if words are anagrams
######################

#vector1 = (1, 2)
# vector2 = (2, 2)

# have_same_length = #homework
# print(have_same_length)

# word1 = "ward"
# word2 = "draw"

# are_anagrams = #homework
# print(are_anagrams)