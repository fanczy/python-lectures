print("===============")

a = 5
b = 2

print("addition", a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)

message = "Hello world"
print(message)
print("I'm alive")
print('He said: "I''m alive"')
print(message[0]) #strings are immutable
print(message[-1])
print(message[6:])
print(message[:4]) # stop index excluded
print(message[1:5])
print(message[6::2])
print(message[::-1])

hello = message[:5]
name = "Person"

print(message.upper())
print(hello + name)
print(hello + ", " + name + "." * 3)
print("{}, {}.".format(hello, name))
print("{1}, {0}.".format(hello, name))
print("{g} {n}".format(g = hello, n = name))
print("{g} {g}".format(g = hello, n = name))

print(f"{hello}, {name}.")
print(f"{name}, {hello.lower()}")

pi_approx = 355 / 113

print(f"{pi_approx:1.6f}")


print(len(message))
print(message.__len__())

numbers = "zero one two three four".split()
print(numbers)
numbers_extension = [5, "six"]
extended_numbers = numbers + numbers_extension
print(extended_numbers)
extended_numbers = extended_numbers + ["seven", "eight"]
print(extended_numbers) 
extended_numbers += ["nine", "ten"]
extended_numbers[5] = "five"
extended_numbers.append("eleven")
print(extended_numbers) 
extended_numbers.pop()
print(extended_numbers)  
zero = extended_numbers.pop(0)
print(extended_numbers) 
print(zero)
numbers = [2,1,3]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
letters = ["c", "a", "b"]
letters.sort()
print(letters) # can't sort mixed list



print("===============")