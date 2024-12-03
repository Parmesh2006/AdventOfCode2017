# Generator A starts with 783
#   Multiply by factor of 16807 and then keep the remainder of that product divided by 2147483647
#   REPEATED
# Generator B starts with 325
#   Multiply by factor of 48271 and then keep the remainder of that product divided by 2147483647
#   REPEATED

# Returns ending 16 digits if binary is longer than 16 digits
# Returns zeros attached at beginning if binary is shorter than 16 digits
def zeros_str(binary: str) -> str:
    if len(binary) > 16:
        return binary[len(binary) - 16:len(binary)]
    else:
        return "".join(["0" for i in range(0, 16 - len(binary))]) + binary

genA: int = 783
factorA: int = 16807

genB: int = 325
factorB: int = 48271

mod: int = 2147483647

# First 40,000,000 pairs of A and B
countOfBitsEqual: int = 0

for i in range(0, 40000000):
    genA: int = (genA * factorA) % mod
    genB: int = (genB * factorB) % mod

    # makes it 16 digits long if it is short and accounts for long binary strings too
    newBinA: str = zeros_str(bin(genA).replace("0b", ""))
    newBinB: str = zeros_str(bin(genB).replace("0b", ""))

    # Increase count if newBinA and newBinB are equal
    if newBinA == newBinB:
        countOfBitsEqual += 1

# Part 1
print(f"Count of Bits Equal: {countOfBitsEqual}")