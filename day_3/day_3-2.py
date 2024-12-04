import re
memory = ""
instructions = []
formattedinstructions = []
total =0

with open('puzzleinput.txt') as puzzleinput:
    for line in puzzleinput:
        memory += line
memory.replace('\n', '')
firstbit = memory.split("don't()", maxsplit=1)[0]
firstbit = firstbit.split('do()', maxsplit=1)[0]
firstinstructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", firstbit)
print(firstbit)
print(len(firstinstructions))
for instruction in firstinstructions:
    instructions.append(instruction)

middlebit = re.findall(r"do\(\)(.*)don't\(\)", memory)
middlebit = ''.join(middlebit)
middleinstructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", middlebit)
for instruction in middleinstructions:
    instructions.append(instruction)

lastbit = memory.split("don't()")[-1]
lastbit = lastbit.split("do()")[-1]
lastinstructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", lastbit)
for instruction in lastinstructions:
    instructions.append(instruction)

print(instructions)
for instruction in instructions:
    instruction = instruction.lstrip("mul(")
    instruction = instruction.rstrip(")")
    formattedinstructions.append(instruction)

print(formattedinstructions)
print(len(formattedinstructions))
for instruction in formattedinstructions:
    factors = instruction.split(',')
    print(factors)
    total += int(factors[0]) * int(factors[1])

print(total)