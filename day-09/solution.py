import sys
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

result = 0
for line in getLinesFromFile("day-09"):
    history = [[int(x) for x in line.replace('\n', '').split(' ')]]

    while any(history[len(history) - 1]):
        process = []
        items = history[len(history) - 1]
        for index in range(0, len(items) - 1, 1):
            process.append(int(items[index + 1]) - int(items[index]))
        history.append(process)

    value = 0
    for items in reversed(history):
        value += items[len(items) - 1]
    result += value

print(result)

# Answer: 1987402313
