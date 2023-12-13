import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

lines = getLinesFromFile("day-10")

pattern = re.compile(r'[\w\W]')

matrix = []

startIndex = ""
for index, line in enumerate(lines):
    matrix.append(pattern.findall(line.replace("\n", "")))
    if(matrix[index].count("S") > 0):
        startIndex = [index, matrix[index].index("S")]

validDirections = [
    {
        "L": ["down-right", "left-up"]
    },
    {
        "F": ["up-right", "left-down"]
    },
    {
        "7": ["up-left", "right-down"]
    },
    {
        "J": ["down-left", "right-up"]
    },
    {
        "|": ["down-down", "up-up"]
    },
    {
        "-": ["left-left", "right-right"]
    }
]

sequences = ["up", "right", "down", "left"]

for sequence in sequences:
    char = "*"
    direction = sequence
    distance = 1
    path = [startIndex[0], startIndex[1]]

    while(char != "S"):

        if char == "*":
            if direction == "up" and path[0] - 1 >= 0:
                path[0] -= 1
            if direction == "right" and path[1] + 1 < len(matrix[path[0]]):
                path[1] += 1
            if direction == "down" and path[0] + 1 < len(matrix):
                path[0] += 1
            if direction == "left" and path[1] - 1 >= 0:
                path[1] -= 1
            char = matrix[path[0]][path[1]]

        if((directions := next((arr[char] for arr in validDirections if char in arr), None)) == None):
            break

        temp_direction = None
        for value in directions:
            from_direction, to_direction = value.split("-")
            if from_direction == direction:
                temp_direction = to_direction
                if temp_direction == "up":
                    path[0] -= 1
                if temp_direction == "right":
                    path[1] += 1
                if temp_direction == "down":
                    path[0] += 1
                if temp_direction == "left":
                    path[1] -= 1

        if temp_direction == None:
            break

        char = matrix[path[0]][path[1]]
        direction = temp_direction
        distance += 1

    if char == "S":
        break

print(distance // 2)

# Answer: 7063
