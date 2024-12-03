# A SERIES OF TUBES
# Given a series of tubes as input, follow the tubes from the beginning until the end
# Keep track of the characters, in order, that you pass and submit that result for part 1

inputdata=open(r"Day19//input.txt").read()

lines = inputdata.splitlines()

x = 0
y = 0
while lines[y][x] == " ":
  x += 1

d = 0
out = ""
count = 0
while True:
  if lines[y][x] == " ":
    break
  
  count += 1

  if lines[y][x] == "+":
    if d in [0, 2]:
      if x > 0 and lines[y][x-1] != " ":
        d = 3
      elif x < len(lines[y])-1 and lines[y][x+1] != " ":
        d = 1
    else:
      if y > 0 and lines[y-1][x] != " ":
        d = 2
      elif y < len(lines)-1 and lines[y+1][x] != " ":
        d = 0
  elif lines[y][x] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    out += lines[y][x]

  if d == 0:
    y += 1
  elif d == 1:
    x += 1
  elif d == 2:
    y -= 1
  elif d == 3:
    x -= 1

# ANSWERS
print(f"PART 1: {out}")
print(f"PART 2: {count}")