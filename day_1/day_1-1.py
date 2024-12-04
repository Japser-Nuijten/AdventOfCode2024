leftlist = []
rightlist = []
totaldifference = 0

with open('puzzleinput.txt') as puzzleinput:
    for line in puzzleinput:
        line = line.rstrip('\n')
        splitline = line.split('   ')
        leftlist.append(splitline[0])
        rightlist.append(splitline[-1])

leftlist.sort()
rightlist.sort()

for i in range(len(leftlist)):
    difference = int(leftlist[i]) - int(rightlist[i])
    if difference < 0:
        difference = difference * -1
    totaldifference += difference
print(totaldifference)
