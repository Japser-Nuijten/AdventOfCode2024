from itertools import permutations

rules = []
updates = []
total = 0


def ordercheck(update, rules):
    for number in update:
        usedrules = []
        before = []
        after = []
        for rule in rules:
            if str(number) in rule:
                usedrules.append(rule)
        for rule in usedrules:
            if rule.index(str(number)) == 0:
                after.append(rule[-2:])
            else:
                before.append(rule[:2])
        before = [int(x) for x in before]
        after = [int(x) for x in after]
        numberposition = update.index(number)
        for i in update[:numberposition]:
            if i in before:
                continue
            else:
                return False
        for i in update[numberposition + 1:]:
            if i in after:
                continue
            else:
                return False
    return True

def fixorder(update, rules):
    allpossibles = list(permutations(update))
    for update in allpossibles:
        if ordercheck(update, rules):
            return update


with open('puzzleinput.txt')as puzzle_input:
    for line in puzzle_input:
        line = line.rstrip('\n')
        if len(line) == 5:
            rules.append(line)
        elif len(line) == 0:
            continue
        else:
            line = line.split(',')
            line = [int(x) for x in line]
            updates.append(line)

for update in updates:
    if not ordercheck(update, rules):
        update = fixorder(update, rules)
        middle = int((len(update)/2))
        total += update[middle]


print(total)
