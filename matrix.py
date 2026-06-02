import numpy as np

# take input row from user
rows = int(input("Enter number of rows: "))

# take input column from user
cols = int(input("Enter number of columns: "))

# creating matrix 1
m1 = []

print("Enter Matrix 1 elements:")

# matrix 1 input
for i in range(rows):
    row = []    #create empty row

    for j in range(cols):
        x = int(input())
        row.append(x)

    m1.append(row)

# empty list for matrix 2
m2 = []

print("Enter Matrix 2 elements:")

# matrix 2 input
for i in range(rows):
    row = []

    for j in range(cols):
        x = int(input())
        row.append(x)

    m2.append(row)

# convert list into matrix
m1 = np.array(m1)
m2 = np.array(m2)

# show menu
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Inverse")

# take choice from user
choice = int(input("Enter your choice: "))

# addition
if choice == 1:
    print("Result:")
    print(m1 + m2)

# subtraction
elif choice == 2:
    print("Result:")
    print(m1 - m2)

# multiplication
elif choice == 3:
    print("Result:")
    print(np.dot(m1, m2))

# division
elif choice == 4:
    print("Result:")
    print(m1 / m2)

# inverse
elif choice == 5:

    # check matrix is square or not
    if rows == cols:
        print("Inverse of Matrix 1:")
        print(np.linalg.inv(m1))
    else:
        print("Inverse not possible")

# wrong choice
else:
    print("Invalid Choice")