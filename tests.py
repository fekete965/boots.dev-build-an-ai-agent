# Testing write_file.py
# from functions.run_python_file import run_python_file

# test_args = [
#     ("calculator", "main.py", None),
#     ("calculator", "main.py", ["3 + 5"]),
#     ("calculator", "tests.py" ,None),
#     ("calculator", "../main.py", None),
#     ("calculator", "nonexistent.py", None),
# ]

# for test_arg in test_args:
#     working_directory, file_path, args = test_arg
#     args = args if args is not None else []

#     result = run_python_file(working_directory, file_path, args)

#     print(f"Result for running {file_path}:")
#     print(result)
#     print("--------------------------------")

# Testing write_file.py
# from functions.write_file import write_file

# args = [
#     ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
#     ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
#     ("calculator", "/tmp/temp.txt", "this should not be allowed")
# ]

# for test_arg in test_args:
#     working_directory, file_path, content = test_arg
#     result = write_file(working_directory, file_path, content)

#     print(f"Result for writing to {file_path}:")
#     print(result)
#     print("--------------------------------")

# Testing get_file_content.py
# from functions.get_file_content import get_file_content

# args = [
#     ("calculator", "main.py"),
#     ("calculator", "pkg/calculator.py"),
#     ("calculator", "/bin/cat"),
#     ("calculator", "pkg/does_not_exist.py"),
#     ("calculator", "lorem.txt"),
# ]

# for test_arg in test_args:
#     working_directory, file_path = test_arg
#     result = get_file_content(working_directory, file_path)

#     print(f"Result for {file_path} file:")
#     print(result)
#     print("--------------------------------")

# Testing get_files_info.py
# from functions.get_files_info import get_files_info

# args = [
#     ("calculator", "."),
#     ("calculator", "pkg"),
#     ("calculator", "/bin"),
#     ("calculator", "../"),
# ]

# for test_arg in test_args:
#     working_directory, directory = test_arg
#     result = get_files_info(working_directory, directory)

#     dir_id = 'current' if directory == '.' else directory
#     print(f"Result for {dir_id} directory:")
#     print(result)
#     print("--------------------------------")
