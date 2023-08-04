### Problem **1: Print the following pattern**
# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 5 

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


### Problem **2: Display numbers from a list using loop**
# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions
# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

# **Given**:
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
# **Expected output:**
# 75
# 150
# 145


numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number > 500:
        break  # Stop the loop if number is greater than 500
    if number > 150:
        continue  # Skip numbers greater than 150
    if number % 5 == 0:
        print(number)


### Problem **3: Append new string in the middle of a given string**
# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:
# ```
# s1 = "Ault"
# s2 = "Kelly"
# ```

# **Expected Output**:
# ```
# AuKellylt
# ```

s1 = "Ault"
s2 = "Kelly"

middle_index = len(s1) // 2  

s3 = s1[:middle_index] + s2 + s1[middle_index:]  
print(s3)


### Problem **4: Arrange string characters such that lowercase letters should come first**
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:
# ```
# str1 = PyNaTive
# ```

# **Expected Output**:
# ```
# yaivePNT
# ```

str1 = "PyNaTive"

lowercase = ""
uppercase = ""

for char in str1:
    if char.islower():
        lowercase += char
    else:
        uppercase += char

arranged_str = lowercase + uppercase
print(arranged_str)


### Problem **5: Concatenate two lists index-wise**
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# **Given**:
# ```
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# ```

# **Expected output:**
# ```
# ['My', 'name', 'is', 'Kelly']
# ```

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result_list = [item1 + item2 for item1, item2 in zip(list1, list2)]
print(result_list)


### Problem **6: Concatenate two lists in the following order**

# ```
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ```

# **Expected output:**
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result_list = [word1 + word2 for word1 in list1 for word2 in list2]
print(result_list)

