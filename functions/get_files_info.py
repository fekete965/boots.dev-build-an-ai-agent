from os import listdir, path

def unsafe_get_files_info(working_directory, directory="."):
  working_dir_abs_path = path.abspath(working_directory)
  target_dir_abs_path = path.abspath(path.join(working_directory, directory))
  
  if not target_dir_abs_path.startswith(working_dir_abs_path):
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
  
  if not path.isdir(target_dir_abs_path):
    raise f'Error: "{directory}" is not a directory'
  
  dir_list = listdir(target_dir_abs_path)
  
  result = []
  
  for item in dir_list:
    item_path = path.join(target_dir_abs_path, item)
    file_size = path.getsize(item_path)
    is_dir = path.isdir(item_path)
    
    result.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")

  return "\n".join(result)

def get_files_info(working_directory, directory="."):
  try:
    return unsafe_get_files_info(working_directory, directory)
  except Exception as error:
    return f"Error listing files: {error}"
