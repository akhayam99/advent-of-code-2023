import os

def getLinesFromFile(folder):
  path = os.path.join(os.getcwd(), folder, "input.txt")
  file = open(path, 'r')
  return file.readlines()

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
