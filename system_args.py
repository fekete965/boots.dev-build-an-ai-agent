from sys import argv, exit


class SystemArgs():
    def __init__(self):

        # Check if the user defined arguments
        if (len(argv) < 2):
            print("Usage: python main.py <user_prompt>")
            exit(1)

        # Get the user prompt
        self.user_prompt = argv[1]
        if self.user_prompt is None:
            print("Usage: python main.py <user_prompt>")
            exit(1)

        # Check for verbose flag
        self.has_verbose_flag = False
        for arg in argv[2:]:
            if arg == "--verbose":
                self.has_verbose_flag = True
