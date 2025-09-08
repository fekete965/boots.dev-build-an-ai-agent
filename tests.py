from functions.get_files_info import get_files_info

args = [
  ("calculator", "."),
  ("calculator", "pkg"),
  ("calculator", "/bin"),
  ("calculator", "../"),
]

for arg in args:
  working_directory, directory = arg
  result = get_files_info(working_directory, directory)
  
  dir_id = 'current' if directory == '.' else directory
  print(f"Result for {dir_id} directory:")
  print(result)
  print("--------------------------------")
