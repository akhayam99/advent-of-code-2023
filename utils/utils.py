import os
import re

symbols = re.compile(r'[^.\d]')

# This function returns an array of lines from the given file
def getLinesFromFile(folder):
  path = os.path.join(os.getcwd(), folder, "_input.txt")
  file = open(path, 'r')
  return file.readlines()

# This function returns the literal value of the given number
def getLiteralValue(value):
  match value:
    case "one": return "1"
    case "two": return "2"
    case "three": return "3"
    case "four": return "4"
    case "five": return "5"
    case "six": return "6"
    case "seven": return "7"
    case "eight": return "8"
    case "nine": return "9"
  return value

# This function checks if there are any symbols around the given index
def hasSymbolsAround(lines, index, start, end):
  if(index > 0):
      if(symbols.search(lines[index - 1][start:end]) != None):
          return True

  if(index < len(lines) - 1):
      if(symbols.search(lines[index + 1][start:end]) != None):
          return True

  return symbols.search(lines[index][start:end]) != None

# This function returns an array of numbers that are in the given line
def getArrayOfNumbers(line):
    return re.compile(r'\d+').findall(line)


# This function returns the number that is in the same row as the given row
def extractNumbersFromRow(lines, i, start, end):
    number = lines[i][start:end]
    if(re.compile(r'\d').search(lines[i][start]) != None):
        topIndex = start - 1
        while(re.compile(r'\d').search(lines[i][topIndex]) != None):
            number = lines[i][topIndex] + number
            topIndex -= 1

    if(re.compile(r'\d').search(lines[i][end - 1]) != None):
        after = end
        while(re.compile(r'\d').search(lines[i][after]) != None):
            number = number + lines[i][after]
            after += 1

    return number


def getNewMaxValue(line, reg, max):
    for match in reg.findall(line):
        new_value = int(getArrayOfNumbers(reg.findall(match)[0])[0])
        if(new_value > max):
            max = new_value

    return max
