# getChecksumComponent(list) -> PART 1
# Gets the difference between the largest and smallest of the list

def getCheckSumComponent(numberList: list) -> int:
    return max(numberList) - min(numberList)

# whichEvenlyDividesEachOther(list) -> PART 2
# Gets the only two numbers in the list that divide each other equally, returns the quotient

def whichEvenlyDividesEachOther(numberList: list) -> float:
    for i in numberList:
        for j in numberList:
            if i != j:
                if j % i == 0:
                    return j / i
                elif i % j == 0:
                    return i / j
    
    return 0

# Open file and process each line
with open(r"Day2\\input.txt") as file:
    lines = [line for line in file]

    checksum: int = 0
    quotientSum: int = 0
    for line in lines:
        numbers = line.split("\t")
        numbers[-1] = numbers[-1].replace("\n", "")

        newNumbers = [int(i) for i in numbers]

        checksum += getCheckSumComponent(newNumbers)
        quotientSum += whichEvenlyDividesEachOther(newNumbers)
    
    print(f"Checksum (PART 1): {checksum}")
    print(f"Checksum (PART 2): {quotientSum}")