def print_verbose_data(user_prompt: str, prompt_token_count: int, candidates_token_count: int):
    print("--------------------------------")
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {candidates_token_count}")
