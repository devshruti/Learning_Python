# 1. **Hello, World!**: Write a Python program that prints "Hello, World!" to the console.
#     - *Input*: None
#     - *Output*: "Hello, World!"

print("Hello, World!")


# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
#     - *Input*: None
#     - *Output*: "Type of variable1: <class 'int'>, value: 10..."



int = 13
float = 2.56
string = "Dev"
bool = True
list = [1, 2, 3]
tuple = (4, 5, 6)
dict = {'a': 7, 'b': 8}
set = {19, 10}

variables = [int, float, string, bool, list, tuple, dict, set]

for var in variables:
    print(f"Type of {var}: {type(var)}, value: {var}")


    # 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
    # - *Input*: None
    # - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."

  
num_list = list(range(1, 11))
print("Original list:", num_list)

num_list.append(20)
print("After adding 20:", num_list)

num_list.remove(3)
print("After removing 3:", num_list)

num_list.sort()
print("After sorting:", num_list)



# 4.  **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

list = [10, 20, 30, 40]
total = sum(list)
average = total / len(list)

print(f"Sum: {total}, Average: {average}")


# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

def reverse_string(string):
    return string[::-1]

str = "Python"
reversed_str = reverse_string(str)
print(reversed_str)


# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

def count_vowels(str):
    vowels = "AEIOUaeiou"
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count

str = "Hello"
count = count_vowels(str)
print(f"Number of vowels: {count}")

# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num = 13
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
result = factorial(num)
print(f"Factorial of {num} is {result}.")

# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

input_n = 5
fib_sequence = fibonacci(input_n)
print(f"Fibonacci sequence for {input_n} numbers: {fib_sequence}")



# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"

squares = [x ** 2 for x in range(1, 11)]
print(squares)

