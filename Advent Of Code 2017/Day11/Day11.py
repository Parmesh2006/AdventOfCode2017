i = []
with open(r"Day11\\input.txt") as file:
  i = file.read().split(",")

dmap = {
  "n": (0,1),
  "s": (0,-1),
  "ne": (.5,.5),
  "se": (.5,-.5),
  "nw": (-.5,.5),
  "sw": (-.5,-.5)
}

x, y = 0, 0 # x, y coordinates for tracking how far we've moved 
m = []

for d in i:
  x += dmap[d][0]
  y += dmap[d][1]

  m.append(abs(x) + abs(y))

print(f"Part 1: {abs(x) + abs(y)}") # Part 1
print(f"Part 2: {max(m)}") # Part 2