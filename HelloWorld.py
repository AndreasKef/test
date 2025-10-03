print("Hello, World")
print("______________________________________")

# variables.py
name = "Andreas"
age = 26
print("My name is",name,"and I am",age,"years old")
print("______________________________________")

# math_basics.py
a = 10
b = 3
print("a = ",a,"& b = ",b)
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)   # division
print("a // b =", a // b) # integer division
print("a % b =", a % b)   # remainder
print("a ** b =", a ** b) # power
print("______________________________________")

# user_input.py
name = input("What is your name? ")
print("Hello,", name, "!")
print("______________________________________")

# if_else.py
number = int(input("Enter a number: "))

if number > 0:
    print("That's a positive number!")
elif number < 0:
    print("That's a negative number!")
else:
    print("That's zero!")
print("______________________________________")

# loops.py
for i in range(5):
    print("Loop number:", i)

print("Now let's do a while loop:")

count = 0
while count < 5:
    print("Count is", count)
    count += 1
print("______________________________________")
