# Learn about the TUPLE datatype


# Tuple with values
val = (1, 2, "Darshan", 4.5)

# Print datatype of val
print(type(val))                # <class 'tuple'>

# Print val variable
print(val)                      # (1, 2, 'Darshan', 4.5)

# Tty to update index two from tuple
# val[2] = "Rahul"
print(val)                      # TypeError: 'tuple' object does not support item assignment




# Learn about the Dictionary datatype

dict = {"a" : 2, 4 : "abc", "c" : "Hello world"}

# Check datatype and then print dict variable
print(type(dict))           # <class 'dict'>
print(dict)                 # {'a': 2, 4: 'abc', 'c': 'Hello world'}

# Print values of key 4
print(dict[4])              # abc

# Print values of key c
print(dict["c"])            # Hello world



# How to add data in empty dictionary

dict = {}

dict["firstname"] = "Darshan"
dict["lastname"] = "Patel"
dict["gender"] = "male"

print(dict)







