#Python Assignment No. 02 (Q3)

"""Write a NumPy program to perform following operations:
a) Find the union of two arrays
b) Find common values between two arrays.
c) Find the difference of two arrays.
d) Find the set exclusive-or of two arrays"""

import numpy as np

def main():

    arr1 = input("Enter first array separated by commas: ")
    arr1 = np.array([int(x.strip()) for x in arr1.split(",")])

    arr2 = input("Enter second array separated by commas: ")
    arr2 = np.array([int(x.strip()) for x in arr2.split(",")])

    while True:
        print("\nMenu:")
        print("1. Array Union")
        print("2. Array Common")
        print("3. Array Difference")
        print("4. Array Set Exclusive-Or")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            result = np.union1d(arr1, arr2)
        elif choice == 2:
            result = np.intersect1d(arr1, arr2)
        elif choice == 3:
            result = np.setdiff1d(arr1, arr2)
        elif choice == 4:
            result = np.setxor1d(arr1, arr2)
        elif choice == 5:
            print("Program Terminated")
            break
        else:
            print("Invalid choice")

        print("Result: ", result)

if __name__ == "__main__":
    main()
