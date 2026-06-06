import numpy as np

# This function only takes matrix input
def create_matrix(rows, cols, name):
    matrix = []

    print(f"\nEnter {name} elements:")

    for i in range(rows):
        row = []
    

        for j in range(cols):
            row.append(int(input()))

        matrix.append(row)

    return np.array(matrix)


#This function only performs operations
def perform_operation(choice, m1, m2):

    if choice == 1:                 #Addition
        print("Result:")
        print(m1 + m2)

    elif choice == 2:                #Subtraction
        print("Result:")
        print(m1 - m2)

    elif choice == 3:                #Multiplication
        print("Result:")
        print(np.dot(m1, m2))

    elif choice == 4:                 #Division
        print("Result:")
        print(m1 / m2)

    elif choice == 5:                 #Inverse
        print("Inverse of Matrix 1:")
        print(np.linalg.inv(m1))

    else:
        print("Invalid Choice")


try:
    # Take matrix size
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # Create matrices
    m1 = create_matrix(rows, cols, "Matrix 1")
    m2 = create_matrix(rows, cols, "Matrix 2")

    # Menu
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Inverse")

    choice = int(input("Enter your choice: "))

    # New operations can be added later
    perform_operation(choice, m1, m2)

except ValueError:
    print("Please enter valid numbers.")

except np.linalg.LinAlgError:
    print("Inverse not possible for this matrix.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")