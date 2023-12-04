import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getArrayOfNumbers

result = 0
lines = getLinesFromFile("day-04")

played = re.compile(r':\s(.*?)\s\|')
extracted = re.compile(r'\|\s(.*?)$')

for line in getLinesFromFile("day-04"):

    extractedNumbers = getArrayOfNumbers(extracted.findall(line)[0])
    points = 0

    for number in getArrayOfNumbers(played.findall(line)[0]):
        if number in extractedNumbers:
            points = 1 if points == 0 else points * 2

    result += points

print(result)

# Answer: 24733
