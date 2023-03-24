# SE-3, 20, Suraj Jagtap

#Python Experiment No. 04

"""Write a menu driven python program to implement the following.
a) Find if two input lists are disjoint or not.
b) Count the frequency of each character in the given input string.
c) Accept a comma separated sequence of words as input and print the unique words in sorted form
(alphanumerically)."""

def disjoint(list1, list2):
    return set(list1).isdisjoint(list2)

def frequency(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1
    return freq

def unique_words(words):
    words = words.split(',')
    unique = set(words)
    return sorted(unique)

def main():
    choice = 0
    while choice != 4:
        print("\nChoose an option:")
        print("1. Check if two lists are disjoint")
        print("2. Count the frequency of characters in a string")
        print("3. Print unique words in a comma-separated list")
        print("4. Exit")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            list1 = list(map(int, input("Enter the first list (comma-separated): ").split(',')))
            list2 = list(map(int, input("Enter the second list (comma-separated): ").split(',')))
            if disjoint(list1, list2):
                print("The lists are disjoint")
            else:
                print("The lists are not disjoint")

        elif choice == 2:
            string = input("Enter a string: ")
            result = frequency(string)
            for key, value in result.items():
                print(f"{key}: {value}")

        elif choice == 3:
            words = input("Enter a comma-separated list of words: ")
            result = unique_words(words)
            print(", ".join(result))

        elif choice == 4:
            print("Exiting...")

        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
