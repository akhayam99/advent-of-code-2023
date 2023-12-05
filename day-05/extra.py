import sys
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

result = 0
lines = getLinesFromFile("day-05")

for line in getLinesFromFile("day-05"):
    print(line)

print(result)
