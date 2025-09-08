from os import mkdir, path

def write_file_unsafe(working_directory, file_path, content):
  working_dir_abs_path = path.abspath(working_directory)
  target_file_path_abs_path = path.abspath(path.join(working_directory, file_path))
  
  if not target_file_path_abs_path.startswith(working_dir_abs_path):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
  
  # Create the directory if doesn't exist
  file_dir_name = path.dirname(target_file_path_abs_path)
  is_path_exists = path.exists(file_dir_name)
  if not is_path_exists:
    mkdir(file_dir_name)
  
  # Write the content of a file
  with open(target_file_path_abs_path, 'w') as file:
    file.write(content)

  return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  
def write_file(working_directory, file_path, content):
  try: 
    return write_file_unsafe(working_directory, file_path, content)
  except Exception as error:
    return f"Error writing file: {error}"
