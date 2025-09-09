from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file


def call_function(function_call_part: types.FunctionCall, verbose: bool = False) -> types.Content:
    function_args = function_call_part.args
    function_name = function_call_part.name

    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    # Deliberately hardcoded working directory
    WORKING_DIR = './calculator'

    match function_name:
        case 'get_file_content':
            result = get_file_content(
                working_directory=WORKING_DIR, file_path=function_args.get('file_path'))
            return function_result_to_content(function_name=function_name, function_result=result)
        case 'get_files_info':
            result = get_files_info(
                working_directory=WORKING_DIR, directory=function_args.get('directory'))
            return function_result_to_content(function_name=function_name, function_result=result)
        case 'run_python_file':
            result = run_python_file(working_directory=WORKING_DIR, file_path=function_args.get(
                'file_path'), args=function_args.get('args', []))
            return function_result_to_content(function_name=function_name, function_result=result)
        case 'write_file':
            result = write_file(working_directory=WORKING_DIR, file_path=function_args.get(
                'file_path'), content=function_args.get('content'))
            return function_result_to_content(function_name=function_name, function_result=result)
        case function_name:
            return function_call_error(function_name=function_name)


def function_call_error(function_name: str) -> types.Content:
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
            )
        ],
    )


def function_result_to_content(function_name: str, function_result: any) -> types.Content:
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
