from os import getenv
from dotenv import load_dotenv


class EnvVariables:
    def __init__(self):
        # Load the environment variables
        load_dotenv()

        # Get the environment variables
        self.GEMINI_API_KEY = getenv("GEMINI_API_KEY")
        self.GEMINI_MODEL = getenv("GEMINI_MODEL")
