import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

pattern = re.compile(r'\d+')
symbols = re.compile(r'[^.\d]')

result = 0

lines = getLinesFromFile("day-03")

for index, line in enumerate(lines):
    previousIndex = 0
    for match in pattern.findall(line):
        current = line.find(match, previousIndex)
        previousIndex = current + len(match) + 1

        start = current - 1
        end = current + len(match) + 1

        if(start < 0):
            start = 0

        if(end > len(line) - 1):
            end = len(line) - 1

        isValidBefore= False
        isValidAfter= False
        isValidSide = False

        if(index > 0):
            isValidBefore = symbols.search(lines[index - 1][start:end]) != None
            print(lines[index - 1][start:end], symbols.findall(lines[index - 1][start:end]), isValidBefore)

        isValidSide = symbols.search(line[start:end]) != None
        print(line[start:end], symbols.findall(line[start:end]), isValidSide)

        if (index < len(lines) - 1):
            isValidAfter = symbols.search(lines[index + 1][start:end]) != None
            print(lines[index + 1][start:end], symbols.findall(lines[index + 1][start:end]), isValidAfter)

        print("-----")

        if(isValidBefore or isValidSide or isValidAfter):
            result += int(match)

print(result)

# Answer: 539755
