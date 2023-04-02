# SE-3, 20, Suraj Jagtap

#Python Experiment No. 11

"""Write a program to perform following operations using numpy.
a) Create a 6x6 matrix and fill it with a checkerboard pattern

[[0 1 0 1 0 1]
..........
[0 1 0 1 0 1]
[1 0 1 0 1 0]]

b)Create the following pattern without hardcoding. Use only numpy functions and the below input array

Input: a = np.array([1,2,3])

Desired Output:
array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

C)Add, subtract, multiply and divide two matrices."""

import numpy as np

# function to create a checkerboard matrix
def create_checkerboard_matrix():
    matrix = np.zeros((6, 6))

    matrix[::2, 1::2] = 1
    matrix[1::2, ::2] = 1

    print("Checkerboard Matrix:\n", matrix)

# function to create a pattern from an input array
def create_pattern_from_array():
    a = np.array([1,2,3])

    output = np.concatenate((np.repeat(a, 4), np.tile(a, 3)))

    print("Pattern:\n", output)

# function to perform arithmetic operations on matrices
def perform_arithmetic_operations():
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])

    addition = matrix1 + matrix2

    subtraction = matrix1 - matrix2

    multiplication = matrix1 * matrix2

    np.set_printoptions(precision=2)

    division = matrix1 / matrix2

    print("Addition:\n", addition)
    print("Subtraction:\n", subtraction)
    print("Multiplication:\n", multiplication)
    print("Division:\n", division)

# menu function
def menu():
    while True:
        print("\nChoose an operation to perform:")
        print("1. Create Checkerboard Matrix")
        print("2. Create Pattern from Input Array")
        print("3. Perform Arithmetic Operations on Matrices")
        print("4. Exit Program")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            create_checkerboard_matrix()
        elif choice == 2:
            create_pattern_from_array()
        elif choice == 3:
            perform_arithmetic_operations()
        elif choice == 4:
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please enter a valid choice (1-4).")

if __name__ == "__main__":
    menu()