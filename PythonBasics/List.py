# Learn about the LIST datatypes


# List with name values
values = [1, 2, "rahul", 4, 5]

# Print index 0 from the list
print(values[0])

# Print index 4 from the list
print(values[4])

# Print index from end
print(values[-2])

# print index from till to
print(values[1:3])

# Insert value in list
values.insert(3, "patel")
print(values)

# Insert/add values in the end
values.append("DP")
print(values)

# Update value from list
values[2] = "Darshan"
print(values)               # [1, 2, 'Darshan', 'patel', 4, 5, 'DP']

# Delete value from list
del values[0]
print(values)               # [2, 'Darshan', 'patel', 4, 5, 'DP']

