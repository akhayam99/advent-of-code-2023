import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getNumbers

lines = getLinesFromFile("day-05")

dictionary, seeds = [], map(int, getNumbers(lines[0]))

for index, line in enumerate(lines):
    if line.find("map") == -1:
        continue
    dictionary.append({"fromToMap": []})
    j = index + 1
    while j < len(lines) and re.compile(r'\d+').match(lines[j]):
        dictionary[len(dictionary) - 1]["fromToMap"].append(getNumbers(lines[j]))
        j += 1

min = -1
for seed in seeds:
    for item in dictionary:
        for subitem in item["fromToMap"]:
            destination, source, span = int(subitem[0]), int(subitem[1]), int(subitem[2])
            if seed >= source and seed <= (source + span - 1):
                seed = destination + (seed - source)
                break
    if min == -1 or seed < min:
        min = seed

print(min)

# Answer: 403695602
