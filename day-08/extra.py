import sys, re, math
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

lines = getLinesFromFile("day-08")

myMap = []
myMatches = []
paths = [char for char in lines[0].replace('\n', '')]

pattern = re.compile(r'\w{3}')
for line in lines:
    if ' = ' not in line:
        continue
    values = pattern.findall(line)
    myMap.append({values[0]: values[1:len(values)]})
    if(values[0].endswith('A')):
        myMatches.append(values[0])

succeded = []
counter, index = 1, 0
while len(succeded) != len(myMatches):
    index = 0 if index >= len(paths) else index
    for i, match in enumerate(myMatches):
        combination = next((arr[match] for arr in myMap if match in arr), None)
        prevMatch = myMatches[i]
        myMatches[i] = combination[1] if paths[index] == "R" else combination[0]
        if(myMatches[i].endswith('Z')):
            succeded.append(counter)
    index += 1; counter += 1

print(print(math.lcm(*succeded)))

# Answer: 19185263738117
