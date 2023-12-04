import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getNumbers

lines = getLinesFromFile("day-04")
instances = [0] * len(lines)

for i, line in enumerate(lines):
    instances[i] += 1

    played, extracted = map(getNumbers, line.split(':')[1].split('|'))

    for j in range(1, sum(1 for number in played if number in extracted) + 1):
        instances[i + j] += instances[i]

print(sum(instances))

# Answer: 5422730
