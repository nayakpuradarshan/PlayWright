# Basics of for and while loops

# if else example

greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition matches")
else:
    print("Condition do NOT match")

print("if else condition code is completed")


# For loop exemple One

obj = [2, 3, 5, 7, 9]

for i in obj:
    print(i*2)

# Sum of first natural numbers (1+2+3+4+5 = 15)
summation = 0
for j in range(1, 6):           #range(i, j)  --> i to j-1
    summation = summation + j
print(summation)

# For seperation
print("******************")

# Skip number from list
for i in range(1, 11, 2):
    print(i)


print("******************* While Loop Started *****************")

# Learn WHILE LOOP

    # While loop is focusing on condition if condition is true then it will execute loop but if condition is not true then it will not executing loop

it = 10

while it>1:
    if it == 9:
        it = it - 1
        continue

    if it == 2:
        break
    print(it)

    it = it - 1

print("while loop execution is done")
