# Registry
# Increment and decrement numbers based on instructions in registry

with open(r"Day8//input.txt") as file:
    # extract all the instructions
    instructions = [line.replace("\n", "") for line in file]

    # get all the variables
    allVariables = list(set([i.split(" ")[0] for i in instructions]))

    # turn each of the lines into conventional if statements
    # b inc 5 if a > 1 --> b += 5 if a > 1 else 0
    # ALSO
    # replace each variable with a dictionary representation and key
    # b inc 5 if a > 1 --> registry['b'] += 5 if registry['a'] > 1 else 0
    # first index (0) and fifth index (4) have the variables
    for i in range(0, len(instructions)):
        if "inc" in instructions[i]:
            instructions[i] = instructions[i].replace("inc", "+=")
        elif "dec" in instructions[i]:
            instructions[i] = instructions[i].replace("dec", "-=")
        
        instSplit = instructions[i].split(" ")
        instSplit[0] = f"registry['{instSplit[0]}']"
        instSplit[4] = f"registry['{instSplit[4]}']"

        instructions[i] = " ".join(instSplit) + " else 0"
    
# Create the registry
registry: dict = dict(zip(allVariables, [0 for i in range(0, len(allVariables))]))

# Compile and execute each command
allHighestValues = []
for inst in instructions:
    compiled = compile(inst, "filename", "exec")
    exec(compiled)

    # For Part 2
    allHighestValues.append(max(registry.values()))

print(f"PART 1: {max(registry.values())}")
print(f"PART 2: {max(allHighestValues)}")