reports = []
safereports = 0

def ascending(report):
    unsorted = report.copy()
    sorted = report.copy()
    sorted.sort()
    if unsorted == sorted:
        return True
    else:
        return False

def descending(report):
    unsorted = report.copy()
    sorted = report.copy()
    sorted.sort(reverse=True)
    if unsorted == sorted:
        return True
    else:
        return False

def alloweddifference(report):
    for i in range(len(report) - 1):
        difference = report[i + 1] - report[i]
        if difference > 3 or difference < -3 or difference == 0:
            return False
    return True

with open('puzzleinput.txt') as puzzleinput:
    for line in puzzleinput:
        line = line.rstrip('\n')
        splitline = line.split(' ')
        splitline = [int(x) for x in splitline]
        reports.append(splitline)

for report in reports:
    if (ascending(report) == True or descending(report) == True) and alloweddifference(report) == True:
        safereports += 1
        print(report)

print(safereports)
