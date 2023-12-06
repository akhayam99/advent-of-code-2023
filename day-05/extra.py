import sys, re
import numpy as np

sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getNumbers

lines = getLinesFromFile("day-05")

dictionary, seeds = [], getNumbers(lines[0])

for index, line in enumerate(lines):
    if line.find("map") == -1:
        continue
    dictionary.append({
        "fromToMap": [],
        "cache": [],
        })
    j = index + 1
    while j < len(lines) and re.compile(r'\d+').match(lines[j]):
        dictionary[len(dictionary) - 1]["fromToMap"].append(getNumbers(lines[j]))
        j += 1

index = 0
min = -1
while index < len(seeds):
    start = int(seeds[index])
    end = start + int(seeds[index + 1])
    for seed in range(start, end):
        for item in dictionary:
            if(seed in item["cache"]):
                print("BREAK", seed)
                break
            for index, subitem in enumerate(item["fromToMap"]):
                destination, source, span = map(int, subitem)
                if source <= seed <= (source + span - 1):
                    item["cache"].append(seed)
                    seed = destination + (seed - source)
                    break
                if index == len(item["fromToMap"]) - 1:
                    item["cache"].append(seed)

        if min == -1 or int(seed) < min:
            min = int(seed)
            print("MIN", min)
    index += 2

print(min)

# number_array = []
# for i in range (0, len(seeds), 2):
#     number_array.append(np.arange(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])))
#     print(i)

# min = -1
# for index, seed in enumerate(unique):
#     for item in dictionary:
#         for subitem in item["fromToMap"]:
#             destination, source, span = map(int, subitem)
#             if source <= seed <= (source + span - 1):
#                 seed = destination + (seed - source)
#                 break

#     if min == -1 or seed < min:
#         min = seed

#     print(index, "/", uniqueLen)

# print(min)

# print(len(number_array))
# unique_array = list(set(number_array))
# print(len(unique_array))

# i = 0
# while i < len(seeds):
#     start = int(seeds[i])
#     end = start + int(seeds[i + 1])
#     for seed in range(start, end):
#         print(seed)
#         for item in dictionary:
#             for subitem in item["fromToMap"]:
#                 destination, source, span = map(int, subitem)
#                 if source <= seed <= (source + span - 1):
#                     seed = destination + (seed - source)
#                     break
#             break
#     if min == -1 or seed < min:
#         min = seed

#     i += 2

# print(min)

# Answer: 403695602 (wrong) too high

# 420738748

# 3509911225

# 420738748

# 1142967655

# 284352702 --> 1966060902 108698829

# 1547295753

# 368124453

# 3789179727

# 403695602

# 660525000
