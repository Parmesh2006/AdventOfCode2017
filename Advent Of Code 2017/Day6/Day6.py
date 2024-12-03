# Bank Redistribution
# Take the maximum, and split it evenly among the rest
# Do this again and again until you reach a point you have reached before
# Keep track of the number of iterations
# Return the number of iterations
import itertools

with open(r"Day6\\input.txt") as file:
    # There is only one line
    line: list = [line for line in file][0]

# List of Banks
banks: list = [int(i.strip()) for i in line.split("\t")]

# Traverse through the map of banks and keep track of each one
count = 0
seen = {}

while tuple(banks) not in seen:
    seen[tuple(banks)] = count
    i, m = max(enumerate(banks), key=lambda k: (k[1], -k[0]))
    banks[i] = 0
    for j in itertools.islice(itertools.cycle(range(len(banks))), i + 1, i + m + 1):
        banks[j] += 1
    count += 1

# ANSWERS
print(f"PART 1: {count}")
print(f"PART 2: {count - seen[tuple(banks)]}")