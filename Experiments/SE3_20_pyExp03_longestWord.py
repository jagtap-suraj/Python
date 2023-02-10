# SE-3, 20, Suraj Jagtap

#Python Experiment No. 03

"""Write a python program to implement the following.
a) Find the longest word in a list of words
b) Reverse a list using recursion."""

# Finding the longest word in a list of words
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Reversing a list using recursion
def reverse_list(lst, start, end):
    if start < end:
        lst[start], lst[end] = lst[end], lst[start]
        reverse_list(lst, start + 1, end - 1)

def reverse_list_wrapper(lst):
    reverse_list(lst, 0, len(lst) - 1)
    return lst

def main():
    print("")
    words = []
    n = int(input("Enter the number of words: "))
    for i in range(n):
        words.append(input("Enter word " + str(i + 1) + ": "))
    print("\nLongest word: " + longest_word(words))
    print("\nReversed list: " + str(reverse_list_wrapper(words)))
    print("")

main()