import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

from functions.get_files_info import schema_get_files_info

# Load the environment variables
load_dotenv()

if (len(sys.argv) < 2):
    print("Usage: python main.py <user_prompt>")
    sys.exit(1)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

user_prompt = sys.argv[1]
if user_prompt is None:
    print("Usage: python main.py <user_prompt>")
    sys.exit(1)

has_verbose_flag = False
for arg in sys.argv[2:]:
    if arg == "--verbose":
        has_verbose_flag = True

# Initialize the client
client = genai.Client(api_key=GEMINI_API_KEY)

def main():
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )
    
    ai_response = client.models.generate_content(
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
        ),
        contents=messages,
        model=GEMINI_MODEL, 
    )
    print("Response")
    if ai_response.function_calls is not None and len(ai_response.function_calls) > 0:
        for function_call_part in ai_response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(ai_response.text)
        
    
    if has_verbose_flag:
        print("--------------------------------")
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {ai_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {ai_response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
