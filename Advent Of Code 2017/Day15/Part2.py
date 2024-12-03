# Generator A starts with 783
#   Multiply by factor of 16807 and then keep the remainder of that product divided by 2147483647
#   REPEATED
#   ONLY HANDED TO JUDGE IF THE RESULTING VALUE IS A MULTIPLE OF 4
# Generator B starts with 325
#   Multiply by factor of 48271 and then keep the remainder of that product divided by 2147483647
#   REPEATED
#   ONLY HANDED TO JUDGE IF THE RESULTING VALUE IS A MULTIPLE OF 8
# EACH GENERATOR IS DOING THIS PROCESS INDEPENDENTLY

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

# First 5,000,000 pairs of A and B
A_gen: list = []

while len(A_gen) <= 5000000:
    genA: int = (genA * factorA) % mod

    if genA % 4 == 0:
        newBinA: str = zeros_str(bin(genA).replace("0b", ""))
        A_gen.append(newBinA)

B_gen: list = []

while len(B_gen) <= 5000000:
    genB: int = (genB * factorB) % mod

    if genB % 8 == 0:
        newBinB: str = zeros_str(bin(genB).replace("0b", ""))
        B_gen.append(newBinB)

# VALIDATION
countOfBitsEqual: int = 0

for i in range(0, 5000000):
    if A_gen[i] == B_gen[i]:
        countOfBitsEqual += 1

# Part 2
print(f"Count of Bits Equal: {countOfBitsEqual}")