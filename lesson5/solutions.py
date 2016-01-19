# Exercise 1:
i = 0
while i <= 10:
    print(i)
    i += 1

# Exercise 2:
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

# Exercise 3
for n in range(11):
    print(i)

# Exercise 4
for n in range(101):
    if i % 2 == 0:
        print(i)

# Exercise 5
for n in range(5):
    print('*') * n

# Exercise 6
n = 10
sum_of_n = 0
for i in range(n + 1):
    sum_of_n += i

# Exercise 7
word = 'Argentina'
for letter in word:
    print(letter)

# Exercise 8
for i in range(3):
    for j in range(4, 0, -1):
        print('*') * j

# Exercise 9
for i in range(11):
    for j in range(11):
        print(i * j)

# Exercise 10
# 10 factorial is 3628800
n = 10
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# Exercise 11
# The 12th Fibonacci number is 144
n = 12
fib = 0
num1 = 0
num2 = 1
for i in range(2, n + 1):
    fib = num1 + num2
    num1 = num2
    num2 = fib
