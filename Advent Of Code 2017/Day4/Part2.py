# def validateNoAnagrams(string)
# checks if at least one word is not an anagram of the other
from collections import Counter

# Checks if two words are anagrams
def isAnagram(word1: str, word2: str) -> bool:
    return Counter(word1) == Counter(word2)

# Checks if there are any anagrams in passphrase
def validateNoAnagrams(passphrase: str) -> bool:
    x = ["".join(sorted(i)) for i in passphrase.split()]

    return len(x) == len(set(x))

# Open file and retrieve information
with open(r"Day4\\input.txt") as file:
    data = [line for line in file]

    countOfValid = 0
    for line in data:
        if validateNoAnagrams(line):
            countOfValid += 1
    
    print(f"Valid Passwords: {countOfValid}")