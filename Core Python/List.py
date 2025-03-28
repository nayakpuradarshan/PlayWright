"""
# List basic practice

tea_verities = ["Black", "Green", "lemon", "Herbal"]

print(dir(tea_verities))
# Output:
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', 
'__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
'__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 
'remove', 'reverse', 'sort']
print("tea_verities are:",tea_verities)

# Append
tea_verities.append("With Milk")
print("tea_verities are:",tea_verities)

# copy
New_tea_verities = tea_verities.copy()
print("NEW_tea_verities are:",New_tea_verities)

# count
print(tea_verities.count("Herbal"))

# Insert
tea_verities.insert(1, "TeaName")
print(tea_verities)

# Remaining objects can be practice by your own

# tea_verities.extend(["DP Tea", 5, 2, 3])

tea_verities += ["DP Tea", 5, 2, 3]
print(tea_verities)

"""

# Practice questions for list


"""
# 📌 Problem 1: Sum of Elements
# Write a Python function sum_of_list(numbers) that takes a list of integers and returns the sum of all elements.

# 📌 Solution 1:

numbers = [1, 2, 3, 4, 5, 6, 7]

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

all_sum = sum_of_list(numbers)
print("Sum of all numbers is:", all_sum)
"""


"""
# 📌 Problem 2: Find Maximum and Minimum
# Write a Python program to find the maximum and minimum elements in a given list without using built-in functions
# like max() and min().

numbers1 = [897, 22, 55, 64, 35, 89, 100, 345345, 5534, 56456, 324324]

# write a function which will return max and min values
def find_max_min(numbers1):

    current_max = numbers1[0]
    current_min = numbers1[0]

    for num in numbers1:
        if num > current_max:
            current_max = num
        if num < current_min:
            current_min = num
    return current_min, current_max

min_val, max_val = find_max_min(numbers1)
print("maximum value is:", max_val)
print("minimum value is:", min_val)
"""















