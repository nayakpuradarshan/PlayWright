# 📚 Creating a Dictionary

"""
# Empty dictionary
empty_dict = {}

# Dictionary with data
student = {
    "name": "Alice",
    "age": 25,
    "courses": ["Math", "Science"]
}

# Using the dict() function
person = dict(name="Bob", age=30)
"""
from traceback import print_tb

# 🔍 Common Dictionary Operations

# Dictionary with data
student = {
    "name": "Alice",
    "age": 25,
    "courses": ["Math", "Science"]
}

# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("courses"))
# student["class"] = "B"
# print(dir(student))
# print(student)
#
# print("name" in student)
# del student['age']
# print(student)

for key, value in student.items():
    print(key, value)



