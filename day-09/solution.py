import sys
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

result = 0
lines = getLinesFromFile("day-09")

histories = []
for line in lines:
    histories.append([int(x) for x in line.replace('\n', '').split(' ')])

for history in histories:
    process = [history]

    while any(process[len(process) - 1]):
        toAppend = []
        items = process[len(process) - 1]
        for index in range(0, len(items) - 1, 1):
            toAppend.append(int(items[index + 1]) - int(items[index]))
        process.append(toAppend)

    for items in reversed(process):
        result += items[len(items) - 1]

print(result)

# Answer: 1987402313
