# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. 
# Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."

data = [("John", 25), ("Jane", 30)]

for name, age in data:
    print(f"{name} is {age} years old.")


# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. 
# Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

class AgeDict:
    def __init__(self):
        self.data = {}

    def addentry(self, name, age):
        self.data[name] = age
    
    def updateage(self, name, newAge):
        if name in self.data:
            self.data[name] = newAge

    def deleteentry(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return str(self.data)
    
# Create an instance of the AgeDict class

age_dict = AgeDict()

age_dict.addentry("John",25)

age_dict.updateage("John",26)

age_dict.deleteentry("John")

print(str(age_dict))


# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"

def two_sum(nums, target):
    numInd = {}

    for i, num in enumerate(nums):
        complement = target  - num
        if complement in numInd:
            return[numInd[complement], i]
        numInd[num] = i

    return None

nums = [2, 7, 11, 15]
target = 9
output = two_sum(nums, target)
print(output)


# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

def is_palindrome(word):
    word = word.lower()
    clean_word = ''.join(c for c in word if c.isalnum())
    reversed_word = clean_word[::-1]

    if clean_word == reversed_word:
        return True
    else:
        return False
    
input_word = "madam"
if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")


# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the elements

# Test the function
input_list = [64, 25, 12, 22, 11]
selection_sort(input_list)
print(input_list)


# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

import queue

class StackUsingQueue:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, value):
        self.q2.put(value)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1.empty():
            return self.q1.get()
        return None

# Test the implementation
stack = StackUsingQueue()

stack.push(1)
stack.push(2)
print(stack.pop())  
stack.push(3)
print(stack.pop())  
print(stack.pop())  


# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=", ")
    elif num % 3 == 0:
        print("Fizz", end=", ")
    elif num % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(num, end=", ")

# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

def write_count_to_file(count, output_filename):
    with open(output_filename, 'w') as file:
        file.write(f"Number of words: {count}")

input_filename = "input.txt"
output_filename = "output.txt"

word_count = count_words(input_filename)
write_count_to_file(word_count, output_filename)

print(f"Number of words: {word_count} (written to '{output_filename}')")


# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."

def safe_division(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Test the function
numerator = 5
denominator = 0

division_result = safe_division(numerator, denominator)

if isinstance(division_result, str):
    print(division_result)
else:
    print(f"Division result: {division_result}")
