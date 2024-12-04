leftlist = []
rightlist = []
similarityscore = 0

with open('puzzleinput.txt') as puzzleinput:
    for line in puzzleinput:
        line = line.rstrip('\n')
        splitline = line.split('   ')
        leftlist.append(splitline[0])
        rightlist.append(splitline[-1])

for i in leftlist:
    timesinrightlist = rightlist.count(i)
    similarityscore += (int(i)*timesinrightlist)

print(similarityscore)