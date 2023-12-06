import sys, re
import numpy as np

sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getNumbers

lines = getLinesFromFile("day-05", False)

dictionary, seeds = [], getNumbers(lines[0])

for index, line in enumerate(lines):
    if line.find("map") == -1:
        continue
    dictionary.append({ "fromToMap": []})
    j = index + 1
    while j < len(lines) and re.compile(r'\d+').match(lines[j]):
        dictionary[len(dictionary) - 1]["fromToMap"].append(getNumbers(lines[j]))
        j += 1

number_array = []
for i in range (0, len(seeds), 2):
    number_array.append([int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])])

founded = -1
initial = 219500000

print("START")

while(founded == -1):
    location = initial
    for item in reversed(list(dictionary)):
        for subitem in item["fromToMap"]:
            destination, source, span = map(int, subitem)
            if destination <= location <= (destination + span - 1):
                location = source + (location - destination)
                break
    for arr in number_array:
        if arr[0] <= location <= arr[1]:
            founded = location
            print(initial)
            break

    if(initial % 100000 == 0):
        print("log", initial)
    initial += 1

print(founded)

# 81 + 48 - 50 = 79
# 81 = 79 + 50 - 48
