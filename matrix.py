import numpy as np

print("To perform operations number of Rows and Columns of both matrix must be same..")

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

    if choice == 1:                  #Addition
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
        
        print("\n Inverse of matrix 2:")
        print(np.linalg.inv(m2))

    else:
        print("Invalid Choice")

while True:
    try:
        # Take matrix size
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows <= 0 or cols <= 0:                              
            print("Rows and columns must be greater than zero!")

        if rows != cols :
            print("Please enter same number of rows and columns")
            continue

        break

    except ValueError :
        print("Please Enter correct numbers")

if rows > 4 or cols > 4 :

    start = int(input("Enter minimum value: "))
    end = int(input("Enter maximum value: "))

    m1 = np.random.randint(start, end + 1, (rows, cols))
    m2 = np.random.randint(start, end + 1, (rows, cols))


    print("\nMatrix 1:")
    print(m1)

    print("\nMatrix 2:")
    print(m2)

else:
    m1 = create_matrix(rows, cols, "Matrix 1")
    m2 = create_matrix(rows, cols, "Matrix 2")

    print("Matrices created")


while True:
    try:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Inverse")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 6:                                             # Break code when exit is choosen
            print("Program is Exited")
            break

        # New operations can be added later
        perform_operation(choice, m1, m2)

    except ValueError:
        print("Please enter valid numbers.")

    except np.linalg.LinAlgError:
        print("Inverse not possible for this matrix.")

    except ZeroDivisionError:
        print("Division by zero is not allowed.")   