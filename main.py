import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

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
    
    ai_response = client.models.generate_content(model=GEMINI_MODEL, contents=messages)
    print("Response")
    print(ai_response.text)
    
    if has_verbose_flag:
        print("--------------------------------")
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {ai_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {ai_response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
