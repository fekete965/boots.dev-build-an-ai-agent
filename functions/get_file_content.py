from os import path

from google.genai import types

from config import MAX_CONTENT_CHUNK_SIZE


def get_file_content_unsafe(working_directory: str, file_path: str) -> str:
    working_dir_abs_path = path.abspath(working_directory)
    target_file_path_abs_path = path.abspath(
        path.join(working_directory, file_path))

    if not target_file_path_abs_path.startswith(working_dir_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not path.isfile(target_file_path_abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    result = None

    with open(target_file_path_abs_path, 'r') as file:
        result = file.read(MAX_CONTENT_CHUNK_SIZE)

    if len(result) == MAX_CONTENT_CHUNK_SIZE:
        result += f"\n[...File \"{file_path}\" truncated at {MAX_CONTENT_CHUNK_SIZE} characters]"

    return result


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        return get_file_content_unsafe(working_directory, file_path)
    except Exception as error:
        return f"Error getting file content: {error}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a file at the given path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to get the content of, relative to the working directory.",
            )
        }
    ),
)
