# SPINLOCK
# Spinlock algorithm to fix computer
# Part 1: What is the value after 2017 after the spinlock manuever?
# Part 2: What is the value after 0 the moment 50000000 is inserted?

step = 345 # my input

# part 1
i = 0
buf = [0]
for t in range(1,2018):
	i = (i + step) % len(buf) + 1
	buf[i:i] = [t] # equivalent to insert
	
print(f"PART 1: {buf[i - 5:i + 5]}")

# part 2
i = 0
for t in range(1,50000001):
	i = (i + step) % t + 1
	if i == 1:
		val_after_0 = t
print(f"PART 2: {val_after_0}")