# def validatePassphrase(string)
# checks if there are duplicate words in the string

def validatePassphrase(passphrase: str) -> bool:
    return len(passphrase.replace("\n", "").split(" ")) == len(set(passphrase.replace("\n", "").split(" ")))

# Open file and retrieve information
with open(r"Day4\\input.txt") as file:
    data = [line for line in file]

    countOfValid = 0
    for line in data:
        if validatePassphrase(line):
            countOfValid += 1
    
    print(f"Valid Passwords: {countOfValid}")