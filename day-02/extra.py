import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

regGame = re.compile(r'Game \d+')
regReds = re.compile(r'\d+ red')
greensReg = re.compile(r'\d+ green')
bluesReg = re.compile(r'\d+ blue')

value = re.compile(r'\d+')

result = 0
for line in getLinesFromFile("day-02"):

    maxRed = 0
    maxGreen = 0
    maxBlue = 0

    for red in regReds.findall(line):
        new_value = int(value.findall(red)[0])
        if(new_value > maxRed):
            maxRed = new_value

    for green in greensReg.findall(line):
        new_value = int(value.findall(green)[0])
        if(new_value > maxGreen):
            maxGreen = new_value

    for blue in bluesReg.findall(line):
        new_value = int(value.findall(blue)[0])
        if(new_value > maxBlue):
            maxBlue = new_value

    result += (maxRed * maxGreen * maxBlue)

print(result)

# Answer: 67335
