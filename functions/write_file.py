from os import mkdir, path

from google.genai import types


def write_file_unsafe(working_directory: str, file_path: str, content: str) -> str:
    working_dir_abs_path = path.abspath(working_directory)
    target_file_path_abs_path = path.abspath(
        path.join(working_directory, file_path))

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


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        return write_file_unsafe(working_directory, file_path, content)
    except Exception as error:
        return f"Error writing file: {error}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the given content into a file at the given path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            )
        }
    )
)
