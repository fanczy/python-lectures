print("===============")

# VSCode: CTRL + SHIFT + P 
# Select interpreter
# F2 + install refacrotring plugin
# F5 + install linter

print("hello world")
print("hello", "world")

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

###################
##### STRINGS #####
###################

message = "Hello world"
print(message)
print("I'm alive") # combination of single/double quotation marks allows use of quotes without string termination
print('He said: "I''m alive"') 
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

##############$######
# STRING FORMATTING #
###############$#####

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

print(f"{pi_approx:1.6f}") # floating number formatting - 1 number before decimal point, 6 nubmers after decimal point


print(len(message)) # returns string length
print(message.__len__()) # same as above

###################
###### LISTS ######
###################

numbers = "zero one two three four".split()
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

numbers = [2,1,3]
print(numbers)

numbers.sort() # sorting list of items
print(numbers)

numbers.reverse() # reversing list
print(numbers)

letters = ["c", "a", "b"] # sorting works on characters as well as numbers
letters.sort()
print(letters) 

# ! sort() function can't sort mixed type lists

print("===============")