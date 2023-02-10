# SE-3, 20, Suraj Jagtap

#Python Experiment No. 02

"""Write a python program that takes any word and changes 
all occurrences of vowels to the next vowel (cyclically) using function:
a—> e, e —> i, i —> o, o —>u, u —> a"""

#Here we are using the index of the vowels to find the next vowel
def next_vowel(word):
    vowels = "aeiouAEIOU"
    next_vowels = "eiouaEIOUA"
    result = ""
    for char in word:
        if char in vowels:
            index = vowels.index(char)
            result += next_vowels[index]
        else:
            result += char
    return result

def main():
    print("")
    word = input("Enter a word: ")
    print("Next vowel word: " + next_vowel(word))
    print("")

main()