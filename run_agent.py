from google import genai
from google.genai import types

from config import AGENT_TIMEOUT_COUNT, SYSTEM_PROMPT
from env_variables import EnvVariables
from print_verbose_data import print_verbose_data
from functions.call_function import call_function
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file


def run_agent(
    client: genai.Client,
    env_variables: EnvVariables,
    has_verbose_flag: bool,
    user_prompt: str,
):
    # Initialize the final response and loop count
    final_response = None
    loop_count = 0

    # Initialize the initial message with the user prompt
    messages = [types.Content(
        role="user", parts=[types.Part(text=user_prompt)])]

    available_function = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    while final_response is None or loop_count <= AGENT_TIMEOUT_COUNT:
        # Communicate with the AI
        ai_response = client.models.generate_content(
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=[available_function],
            ),
            contents=messages,
            model=env_variables.GEMINI_MODEL,
        )

        # Update messages with the response
        for candidate in ai_response.candidates:
            if candidate.content is not None:
                messages.append(candidate.content)

        # Check if the AI response has function calls
        has_function_calls = ai_response.function_calls is not None and len(
            ai_response.function_calls) > 0
        if has_function_calls:
            for function_call_part in ai_response.function_calls:
                # Call the function
                result: types.Content = call_function(
                    function_call_part=function_call_part, verbose=has_verbose_flag)
                result_head = result.parts[0]

                # Check if the function call failed
                if result_head is None or result_head.function_response.response is None:
                    raise Exception(
                        f"Function call failed: {function_call_part.name}")
                else:
                    # Update messages with the function call result
                    messages.append(types.Content(
                        role="user",
                        parts=[types.Part(
                            text=result_head.function_response.response.get('result'))],
                    ))
        else:
            # Update the final response
            final_response = ai_response.text

        # Print verbose data if required
        if has_verbose_flag:
            print_verbose_data(
                user_prompt=user_prompt,
                prompt_token_count=ai_response.usage_metadata.prompt_token_count,
                candidates_token_count=ai_response.usage_metadata.candidates_token_count,
            )

        # Increment the loop count
        loop_count += 1

    return final_response
