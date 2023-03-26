# SE-3, 20, Suraj Jagtap

#Python Experiment No. 07

"""Write a program to build packages and modules for stack data structures."""

from DataStructure.stack import *

def main():
    while True:
        print("\nStack Menu:")
        print("\t1.Push\n\t2.Pop\n\t3.Peek\n\t4.Display\n\t5.Show Size\n\t6.Exit")
        choice = input("Enter the choice: ")

        if choice == "1":
            element = int(input("Enter the element to push: "))
            push(element)
            print("Element has been pushed")
        elif choice == "2":
            element = pop()
            if element != -1:
                print("Popped Element: ", element)
            else:
                print("Stack is empty")
        elif choice == "3":
            element = peek()
            if element != -1:
                print("Stack-top Element: ", element)
            else:
                print("Stack is empty")
        elif choice == "4":
            tempStack = display()
            if tempStack != -1:
                print("Stack Elements: ", tempStack)
            else:
                print("Stack is empty")
        elif choice == "5":
            print("Current Stack Size: ", stackSize())
        elif choice == "6":
            print("Program Exited")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()
