# SE-3, 20, Suraj Jagtap

#Python Experiment No. 07

"""Write a program to build packages and modules for queue data structures."""

from DataStructure.queue import *

def main():
    while True:
        print("\nQueue Menu:")
        print("\t1.Enqueue\n\t2.Dequeue\n\t3.Peek\n\t4.Display\n\t5.Show Size\n\t6.Exit")
        choice = input("Enter the choice: ")

        if choice == "1":
            element = int(input("Enter the element to enqueue: "))
            enqueue(element)
            print("Element has been enqueued")
        elif choice == "2":
            element = dequeue()
            if element != -1:
                print("Dequeued Element: ", element)
            else:
                print("Queue is empty")
        elif choice == "3":
            element = peek()
            if element != -1:
                print("Front Element: ", element)
            else:
                print("Queue is empty")
        elif choice == "4":
            tempQueue = display()
            if tempQueue != -1:
                print("Queue Elements: ", tempQueue)
            else:
                print("Queue is empty")
        elif choice == "5":
            print("Current Queue Size: ", queueSize())
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()
