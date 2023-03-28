#Python Assignment No. 01 (Q3)

"""Write a python program to display Python program files
available in the current directory. Open the file from the
displayed list, reverse its content and print it."""

import os

def main():
    files = [f for f in os.listdir() if f.endswith('.py')]
    print("Python program files in current directory:")
    for i, f in enumerate(files): # enumerate() returns a tuple (index, value)
        print(f"{i+1}. {f}")
    choice = input("Enter the number of the file to reverse its content: ")
    if choice.isdigit() and int(choice) <= len(files):
        file = files[int(choice) - 1]
        with open(file, 'r') as f:
            content = f.read()[::-1]
            print(f"Reversed content of {file}:")
            print(content)
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()

