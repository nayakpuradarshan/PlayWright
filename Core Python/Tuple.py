
"""

# Empty tuple
empty_tuple = ()

# Tuple with integers
numbers = (1, 2, 3, 3, 3, 3, 4)

# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)

# Single-element tuple (comma is necessary)
single_element_tuple = (42,)

# Nested tuple
nested_tuple = (1, (2, 3), 4)

# check type
print(type(numbers))

# Print what are the directory we have
print(dir(numbers))

# Print numbers tuple
print(numbers)

# Count the number 3 in tuple
print(numbers.count(3))

# search index
print(numbers.index(33))

"""

"""
📌 Problem 1: Tuple Manipulation
Write a function swap_elements(tup) that accepts a tuple of length 2 and returns a new tuple with the elements swapped.


def swap_elements(tup):
    # check if tuple lenght must be 2
    if len(tup) != 2:
        return ValueError("Value must be 2 given")

    else:
        return tup[1], tup[0]

try:
    result1 = swap_elements((10, 30))
    print(f"Input: (10, 30) -> Output: {result1}")

    result2 = swap_elements(("DP", 20))
    print(f"Input: ('DP', 20) -> Output: {result2}")

    result3 = swap_elements((100, 200))
    print(f"Input: (100, 200) -> Output: {result3}")

    result4 = swap_elements((200, 212, 232))
    print(f"Input: (200, 212, 232) -> Output: {result4}")

except ValueError as e:
    print(f"Error: {e}")
"""