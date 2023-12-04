import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getNumbers

result = 0

for line in getLinesFromFile("day-04"):
    points = 0
    played, extracted = map(getNumbers, line.split(':')[1].split('|'))

    for number in played:
        if number in extracted:
            points = 1 if points == 0 else points * 2

    result += points

print(result)

# Answer: 24733
