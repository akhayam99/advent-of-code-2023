import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile


# Strips the newline character
pattern = re.compile(r'\d')
sum = 0
for line in getLinesFromFile("day-01"):
    matches = pattern.findall(line)
    sum += int(matches[0] + "" + matches[len(matches) - 1])

print(sum)
