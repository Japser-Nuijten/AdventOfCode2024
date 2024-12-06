map = []

with open('puzzleinput.txt') as puzzleinput:
    for line in puzzleinput:
        line = line.rstrip('\n')
        line = list(line)
        map.append(line)


def rendermap(map):
    for row in map:
        print(row)


class Character:
    def __init__(self):
        self.direction = "^"
        self.xposition, self.yposition = self.updateposition()

    def updateposition(self):
        y = 0
        for row in map:
            if self.direction in row:
                self.xposition = row.index(self.direction)
                self.yposition = y
                return row.index(self.direction), y
            y += 1

    def moveup(self):
        x, y = self.xposition, self.yposition
        map[y][x] = "."
        map[y - 1][x] = "^"
        self.updateposition()

    def movedown(self):
        x, y = self.xposition, self.yposition
        map[y][x] = "."
        map[y + 1][x] = "v"
        self.updateposition()

    def moveleft(self):
        x, y = self.xposition, self.yposition
        map[y][x] = "."
        map[y][x - 1] = "<"
        self.updateposition()

    def moveright(self):
        x, y = self.xposition, self.yposition
        map[y][x] = "."
        map[y][x + 1] = ">"
        self.updateposition()

    def moveforward(self):
        if self.direction == "^":
            self.moveup()
        elif self.direction == ">":
            self.moveright()
        elif self.direction == "v":
            self.movedown()
        elif self.direction == "<":
            self.moveleft()
        self.markposition()

    def turnright(self):
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"

    def obstacle(self):
        if self.direction == "^":
            if map[self.yposition - 1][self.xposition] == "#":
                return True
            else:
                return False
        elif self.direction == ">":
            if map[self.yposition][self.xposition + 1] == "#":
                return True
            else:
                return False
        elif self.direction == "v":
            if map[self.yposition + 1][self.xposition] == "#":
                return True
            else:
                return False
        elif self.direction == "<":
            if map[self.yposition][self.xposition - 1] == "#":
                return True
            else:
                return False

    def markposition(self):
        history[self.yposition][self.xposition] = "X"

    def __str__(self):
        return f"{self.xposition} {self.yposition} {self.direction} {self.obstacle()}"


guard = Character()
history = []
for i in map:
    history.append(i.copy())

while True:
    try:
        if not guard.obstacle():
            guard.moveforward()
            print(guard)
        elif guard.obstacle():
            guard.turnright()
            print(guard)
    except IndexError:
        break

totalspots = 0
for i in history:
    print(i)
    for j in i:
        if j == "X":
            totalspots += 1
print(totalspots + 1)
