print("===============")

##### HOMEWORK #####
# check if two vectors are the same length
# check if words are anagrams
######################

wordA = "ward"
wordB = "draw"

if set(wordA) == set(wordB):
    print(f"Words {wordA} and {wordB} are anagrams") # code executed in condition must be nested
else:
    print(f"Words {wordA} and {wordB} are not anagrams")

a = 5
b = 6

if a > b:
    print(f"{a} is bigger than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else: # all happens if all predecessing conditions are false
    print(f"{a} is smaller than {b}")

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # executes nested code for every value in iterable (iterables are things that you can iterate over)
    print(number)

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")

sum = 0
for number in numbers:
    sum += number

print(f"Sum of {numbers} is {sum}") 

for i in range(10): # zero to nine
    print(i)

for i in range(5, 10):
    print(i)

for i in range(10, 20, 2):
    print(i)

for i in range (10, 0, -1):
    print(i)

word = "Hello"

for letter in word:
    print(letter)

for index in range(len(word)):
    print(word[index])

for index in range(len(word)):
    print(word[-1 - index])

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



print("===============")