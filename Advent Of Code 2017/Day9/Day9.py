# Use the brackets to identify the final score and garbage count

score = 0
level = 0
garbageCount = 0

with open(r'Day9\\input.txt') as file:
	data = file.read()

i = 0
while i < len(data):
	if data[i] == '{':
		level += 1
		score += level
	elif data[i] == '}':
		level -= 1
	elif data[i] == '<':
		i += 1
		while data[i] != '>':
			if data[i] == '!':
				i += 1
			else:
				garbageCount += 1
			i += 1
	i += 1

print(f"Final Score: {score}")
print(f"Garbage Count: {garbageCount}")