import re
memory = ""
formattedinstructions = []
total = 0

with open('puzzleinput.txt') as puzzleinput:
    for line in puzzleinput:
        memory += line

instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)

for instruction in instructions:
    instruction = instruction.lstrip("mul(")
    instruction = instruction.rstrip(")")
    formattedinstructions.append(instruction)

print(formattedinstructions)

for instruction in formattedinstructions:
    factors = instruction.split(',')
    print(factors)
    total += int(factors[0]) * int(factors[1])

print(total)