# Positive jumps move to the right of the list
# Negative jumps move to the left of the list
# As soon as the jump occurs, the element you were originally on is incremented
# But if the offset (the element) is 3 or more, decrease it by one instead

with open(r"Day5\\input.txt") as file:
    lines: list = [int(num) for num in file]

steps = 0
place = 0
while place < len(lines) and place > -1:
    steps += 1
    old = place
    jump = lines[place]
    place += jump

    if jump > 2:
        lines[old] -= 1
    else:
        lines[old] += 1

print(f"Steps: {steps}")