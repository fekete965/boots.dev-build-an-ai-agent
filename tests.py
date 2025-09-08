# Testing write_file.py
from functions.write_file import write_file

args = [
  ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
  ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
  ("calculator", "/tmp/temp.txt", "this should not be allowed")
]

for arg in args:
  working_directory, file_path, content = arg
  result = write_file(working_directory, file_path, content)
  
  print(f"Result for writing to {file_path}:")
  print(result)
  print("--------------------------------")

# Testing get_file_content.py
# from functions.get_file_content import get_file_content

# args = [
#   ("calculator", "main.py"),
#   ("calculator", "pkg/calculator.py"),
#   ("calculator", "/bin/cat"),
#   ("calculator", "pkg/does_not_exist.py"),
#   ("calculator", "lorem.txt"),
# ]

# for arg in args:
#   working_directory, file_path = arg
#   result = get_file_content(working_directory, file_path)
  
#   print(f"Result for {file_path} file:")
#   print(result)
#   print("--------------------------------")

# Testing get_files_info.py
# from functions.get_files_info import get_files_info

# args = [
#   ("calculator", "."),
#   ("calculator", "pkg"),
#   ("calculator", "/bin"),
#   ("calculator", "../"),
# ]

# for arg in args:
#   working_directory, directory = arg
#   result = get_files_info(working_directory, directory)
  
#   dir_id = 'current' if directory == '.' else directory
#   print(f"Result for {dir_id} directory:")
#   print(result)
#   print("--------------------------------")
