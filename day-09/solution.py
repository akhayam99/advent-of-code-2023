import sys
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

for line in getLinesFromFile("inputs"):
    items = [int(x) for x in line.replace('\n', '').split(' ')]

    while any(items):
        result += items[len(items) - 1]
        process = []
        for index in range(0, len(items) - 1, 1):
            process.append(int(items[index + 1]) - int(items[index]))
        items = process

print(result)

# Answer: 1987402313
