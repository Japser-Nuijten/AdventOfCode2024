puzzle = []
with open('puzzleinput.txt') as puzzleinput:
    for line in puzzleinput:
        puzzle.append(line.rstrip('\n'))

xsize = len(puzzle[0])
ysize = len(puzzle)
xmasamount = 0


def get(x, y):
    if x < 0 or y < 0:
        return 0
    else:
        try:
            return puzzle[y][x]
        except IndexError:
            return 0


def mschecker(x, y):
    if get(x - 1, y - 1) == "M" and get(x + 1, y - 1) == "M" and get(x - 1, y + 1) == "S" and get(x + 1, y + 1) == "S":
        return True
    elif get(x - 1, y - 1) == "S" and get(x + 1, y - 1) == "M" and get(x - 1, y + 1) == "S" and get(x + 1, y + 1) == "M":
        return True
    elif get(x - 1, y - 1) == "S" and get(x + 1, y - 1) == "S" and get(x - 1, y + 1) == "M" and get(x + 1, y + 1) == "M":
        return True
    elif get(x - 1, y - 1) == "M" and get(x + 1, y - 1) == "S" and get(x - 1, y + 1) == "M" and get(x + 1, y + 1) == "S":
        return True
    else:
        return False


for y in range(ysize):
    for x in range(xsize):
        if get(x, y) == "A":
            if mschecker(x, y):
                xmasamount += 1

print(xmasamount)
