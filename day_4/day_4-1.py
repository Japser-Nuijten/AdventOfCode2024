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


def mcheck(x, y):
    directions = []
    if get(x - 1, y - 1) == "M":
        directions.append(1)
    if get(x, y - 1) == "M":
        directions.append(2)
    if get(x + 1, y - 1) == "M":
        directions.append(3)
    if get(x - 1, y) == "M":
        directions.append(4)
    if get(x + 1, y) == "M":
        directions.append(5)
    if get(x - 1, y + 1) == "M":
        directions.append(6)
    if get(x, y + 1) == "M":
        directions.append(7)
    if get(x + 1, y + 1) == "M":
        directions.append(8)
    return directions


for y in range(ysize):
    for x in range(xsize):
        if get(x, y) == "X":
            directions = mcheck(x, y)
            for direction in directions:
                if direction == 1 and get(x - 2, y - 2) == "A" and get(x - 3, y - 3) == "S":
                    xmasamount += 1
                elif direction == 2 and get(x, y - 2) == "A" and get(x, y - 3) == "S":
                    xmasamount += 1
                elif direction == 3 and get(x + 2, y - 2) == "A" and get(x + 3, y - 3) == "S":
                    xmasamount += 1
                elif direction == 4 and get(x - 2, y) == "A" and get(x - 3, y) == "S":
                    xmasamount += 1
                elif direction == 5 and get(x + 2, y) == "A" and get(x + 3, y) == "S":
                    xmasamount += 1
                elif direction == 6 and get(x - 2, y + 2) == "A" and get(x - 3, y + 3) == "S":
                    xmasamount += 1
                elif direction == 7 and get(x, y + 2) == "A" and get(x, y + 3) == "S":
                    xmasamount += 1
                elif direction == 8 and get(x + 2, y + 2) == "A" and get(x + 3, y + 3) == "S":
                    xmasamount += 1

print(xmasamount)
