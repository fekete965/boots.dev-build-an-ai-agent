from os import path
import subprocess

from config import TIMEOUT

def run_python_file_unsafe(working_directory, file_path, args=[]):
  working_dir_abs_path = path.abspath(working_directory)
  target_file_abs_path = path.abspath(path.join(working_directory, file_path))
  target_file_dir_abs_path = path.dirname(target_file_abs_path)
  
  if not target_file_abs_path.startswith(working_dir_abs_path):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  
  if not path.exists(target_file_abs_path):
    return f'Error: File "{file_path}" not found.'
  
  if not target_file_abs_path.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file.'
  
  process_args = ["python", file_path] + args
  completed_process = subprocess.run(args=process_args, cwd=target_file_dir_abs_path, timeout=TIMEOUT, capture_output=True)
  
  result = [
    f"STDOUT: \n {completed_process.stdout.decode('utf-8')}",
    f"STDERR:: \n {completed_process.stderr}",
  ]
  
  return_code = completed_process.returncode
  if return_code != 0:
    result.append(f"Process exited with code {return_code}")
    
  is_empty_output = completed_process.stdout == 0
  if is_empty_output:
    result.append("No output produced.")
    
  return "\n".join(result)
  
def run_python_file(working_directory, file_path, args=[]):
  try:
    return run_python_file_unsafe(working_directory, file_path, args)
  except Exception as error:
    return f"Error: executing Python file: {error}"
    