import sys
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile,getNumbers
import math

lines = getLinesFromFile("day-06")

time, distance = ''.join(getNumbers(lines[0])), ''.join(getNumbers(lines[1]))
min = (float(time) - math.sqrt(float(time) ** 2 - 4 * float(distance))) / 2
max = (float(time) + math.sqrt(float(time) ** 2 - 4 * float(distance))) / 2

print(math.ceil(max) - math.floor(min) - 1)

# Answer: 33149631
