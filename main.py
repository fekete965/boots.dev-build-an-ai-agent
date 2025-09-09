from sys import exit
from google import genai

from env_variables import EnvVariables
from run_agent import run_agent
from system_args import SystemArgs


def main():
    # Initialize the environment variables
    env_variables = EnvVariables()

    # Initialize the system arguments
    sys_args = SystemArgs()
    has_verbose_flag = sys_args.has_verbose_flag
    user_prompt = sys_args.user_prompt

    # Initialize the client
    client = genai.Client(api_key=env_variables.GEMINI_API_KEY)

    try:
        response = run_agent(
            client=client,
            env_variables=env_variables,
            has_verbose_flag=has_verbose_flag,
            user_prompt=user_prompt,
        )
    except Exception as error:
        print("\nSomething went wrong during the execution of the agent:\n")
        print(f"Error: {error}")
        exit(1)

    print(f"Final response: {response}")


if __name__ == "__main__":
    main()
