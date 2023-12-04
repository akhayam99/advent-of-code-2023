import os

def getLinesFromFile(folder):
  current_folder = os.getcwd()
  # parent_folder = os.path.abspath(os.path.join(current_folder, ".."))
  # folder_path = os.path.join(parent_folder, folder)
  print(os.path.join(current_folder, folder, "input.txt"))
  filePath = os.path.join(current_folder, folder, "input.txt")

  file = open(filePath, 'r')

  return file.readlines()
