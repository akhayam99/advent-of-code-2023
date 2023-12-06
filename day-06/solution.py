import sys
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile,getNumbers
import math

lines = getLinesFromFile("day-06")

myMap = []
for i in range(len(getNumbers(lines[0]))):
    myMap.append(getNumbers(lines[0])[i] + "$" + getNumbers(lines[1])[i])

result = 1
for item in myMap:
    time, distance = item.split("$")
    min = (float(time) - math.sqrt(float(time) ** 2 - 4 * float(distance))) / 2
    max = (float(time) + math.sqrt(float(time) ** 2 - 4 * float(distance))) / 2

    result *= math.ceil(max) - math.floor(min) - 1

print(result)

# x1 = (T - sqrt(T^2-4D))/2
# x2 = (T + sqrt(T^2-4D))/2

# Answer: 2449062
