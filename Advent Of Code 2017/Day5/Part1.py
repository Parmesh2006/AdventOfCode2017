# Positive jumps move to the right of the list
# Negative jumps move to the left of the list
# As soon as the jump occurs, the element you were originally on is incremented

with open(r"Day5\\input.txt") as file:
    lines: list = [int(num) for num in file]

index: int = 0
steps: int = 0

while index >= 0 and index < len(lines):
    tempIndex = index + lines[index]
    lines[index] = lines[index] + 1

    index = tempIndex
    steps += 1

print(f"Steps: {steps}")