# getValidSumFunction(string)
# Checks for which adjacent digits match and gets the sum of the digits
# The next digit to the last digit is the first digit

def getValidSumFunction(inp: str) -> int:
    sumOfDigits: int = 0

    for i in range(0, len(inp)):
        if i < len(inp) - 1:
            if inp[i] == inp[i + 1]:
                sumOfDigits += int(inp[i])
        else:
            if inp[0] == inp[len(inp) - 1]:
                sumOfDigits += int(inp[0])
    
    return sumOfDigits

# getValidSumFunction_NextTwo(string)
# Checks for the digit halfway later (length of string / 2) and checks whether it matches

def getValidSumFunction_NextTwo(inp: str) -> int:
    sumOfDigits: int = 0

    for i in range(0, len(inp)):
        if i + len(inp) / 2.0 < len(inp):
            if inp[i] == inp[i + int(len(inp) / 2.0)]:
                sumOfDigits += int(inp[i])
        else:
            if inp[i] == inp[int((i + len(inp) / 2.0) % len(inp))]:
                sumOfDigits += int(inp[i])
    
    return sumOfDigits

# open file and use the function on the file contents
with open(r"Day1\\input.txt") as file:
    inputNum: str = [line for line in file][0]

    print(f"The CAPTCHA answer (PART 1): {getValidSumFunction(inputNum)}")
    print(f"The CAPTCHA answer (PART 2): {getValidSumFunction_NextTwo(inputNum)}")