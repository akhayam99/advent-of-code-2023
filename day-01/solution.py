import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile


# Strips the newline character
pattern = re.compile(r'\d')
result = 0
for line in getLinesFromFile("day-01"):
    matches = pattern.findall(line)
    result += int(matches[0] + "" + matches[len(matches) - 1])

print(result)

# Answer: 55447
