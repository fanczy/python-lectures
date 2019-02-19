print("===============")
# ADDITION TO LAST LESSON: dictionary.get("nonexistent key", "defaultValue")

######################
##### CONDITIONS #####
######################

if True: # if condition in statement is true then nested code is executed
    print("It's true") # code executed in condition must be nested

condition = False

if condition:
    print("It's true")
else: # else nested code is executed if the condition is false
    print("It's false")



a = 5
b = 6

if a > b:
    print(f"{a} is bigger than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else: # happens if all predecessing conditions are false
    print(f"{a} is smaller than {b}")


word = "hello"

containment_phrase = "contains"

if "b" not in word:
    containment_phrase = "does not contain"

print(f"Word '{word}' {containment_phrase} letter 'b'" )

##### excercises #####
# two variables: a, b write a code that will put bigger value to a and lower to b
######################

#####################
##### FOR LOOPS #####
#####################

numbers = [0, 1, 2, 3, 4, 5]

for number in numbers: # executes nested code for every value in iterable (iterables are things that you can iterate over)
    print(number)

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")

for number in numbers:
    if number > 2:
        break # breaks execution of this for loop
    print(number)

for number in numbers:
    if number == 2:
        continue # skips the rest of nested code and continues on another value
    print(number)


sum = 0
for number in numbers:
    sum += number

print(f"Sum of {numbers} is {sum}") 

##### excercises #####
# find min and max in list of values | float("inf") | float("-inf") <- biggest and lowest float
# in list of strings print first word that contains letter "a"
######################

word = "Hello"

for letter in word:
    print(letter)

# vectors = [[1,2], [3,4], [5,6]]
vectors = [(1,2), (3,4), (5,6)]
for vector in vectors:
    print(vector)

for a, b in vectors:
    print(f"Vector ({a}, {b})")

store_prices = {
    "apple": 1, 
    "pineaple": 2, 
    "pizza": 4.20
}

for item in store_prices: # by default for iterates over dictionary keys, iterating over dictionary is not in order
    print(item)

for price in store_prices.values():
    print(price)

for item in store_prices.items():
    print(item)

for item, price in store_prices.items():
    print(f"{item} costs {price}")


for i in range(10): # zero to nine
    print(i)

for i in range(5, 10):
    print(i)

for i in range(10, 20, 2):
    print(i)

for i in range (10, 0, -1):
    print(i)

for index in range(len(word)):
    print(word[index])

for index in range(len(word)):
    print(word[-1 - index])

print(range(5))
print(list(range(5)))

for index, letter in enumerate(word): # enumerates items with index
    print(index, letter)

##### excercises #####
# print 7!
######################

counter = 0

while counter < 10: # executes nested code while initial condition is still True
    print(counter)
    counter += 1

while counter > 0:
    print(counter)
    counter -= 1
else:
    print(f"Counter stopped at {counter}.")


##### excercises #####
# print random numbers from 0 to 10 until it's 7, then print how many tries did it take to hit 7 | from random import randint <- imports random number generator | randint(0,10)
######################

##############################
##### LIST COMPREHENSION #####
##############################

numbers = [ num for num in range(0,10) ]
print(numbers)

numbers = [ num ** 2 for num in [2, 4, 6, 8]]
print(numbers)

odd_numbers = [ num for num in range(0,10) if num % 2 != 0 ]
print(odd_numbers)

numbers = [ num if num % 2 == 0 else "odd" for num in range(0,10) ] # UNREADABLE, avoid using this.
print(numbers)

numbers = [num * multiplicator for num in [1, 2, 3] for multiplicator in [1, 10, 100]] # UNREADABLE
print(numbers)

##### HOMEWORK #####
######### 1 ########
#
# menu = {
#     "soups": {
#         "tomato soup": 25,
#         "chicken soup": 20
#     },
#     "main courses": {
#         "spaghetti bolognese": 80,
#         "pineapple pizza": 420
#     },
#     "deserts": {
#         "ice cream": 30,
#         "brownies": 30 
#     },
#     "drinks": {
#         "beer": 5,
#         "water": 100
#     }
# } 
#
#
# print in human readable form:
# ===== soups =====
# tomato soup .... 25 BTC
# chicken soup ..... 20 BTC
# ===== main courses =====
# spaghetti bolognese ..... 80 BTC
# .
# .
# .
#
######### 2 ########
# Generate 100 sequences of random numbers (0 - 10) ending with 7.
# print shortest sequence
# print longest sequence
# print sequence with the longest same number combo
# print which number was the combo
# print combo length
# print begining index of the combo in generated sequence
# print in which generation the longest combo appeared
# print which number appeared the most and how many times throughout all generations
# ######################

print("===============")