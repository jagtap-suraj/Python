#Python Assignment No. 01 (Q1)

"""Write a menu driven program to implement the
following:
a. Accept two strings from the user.
b. Display common letters in two input strings.
c. Display letters which are in the first string but not in
the second string.
d. Display set of all letters of both the strings.
e. Display letters which are in the two strings but not in
both."""

def main():
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    result = ""
    while True:
        print("\nMenu:")
        print("1. Display common letters in two strings")
        print("2. Display letters which are in the first string but not in the second string")
        print("3. Display set of all letters of both the strings")
        print("4. Display letters which are in the two strings but not in both")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            result = set(string1) & set(string2)
        elif choice == 2:
            result = set(string1) - set(string2)
        elif choice == 3:
            result = set(string1) | set(string2)
        elif choice == 4:
            result = set(string1) ^ set(string2)
        elif choice == 5:
            print("Program Terminated")
            break
        else:
            print("Invalid choice")
            
        for letter in result:
            print(letter, end=" ")

if __name__ == '__main__':
    main()
