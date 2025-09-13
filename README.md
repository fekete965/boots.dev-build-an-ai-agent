# AI Coding Agent

A secure, sandboxed AI coding agent built with Google's Gemini API that can safely interact with your codebase through controlled function calls. The agent operates within a restricted working directory and can help you with various coding tasks while maintaining security boundaries.

## Features

The AI agent provides a secure environment for code interaction with these capabilities:

- **Safe File Operations**: Read file contents and list directories within the sandbox
- **Controlled Code Execution**: Run Python files with arguments in an isolated environment
- **Secure File Writing**: Create or modify files within the permitted working directory
- **Directory Exploration**: Safely navigate and analyze project structure
- **Security-First Design**: All operations are constrained to prevent unauthorized access

## Prerequisites

- Python 3.10 or higher
- Google Gemini API key

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd boots.dev-build-an-ai-agent
```

2. Install dependencies using uv (recommended) or pip:

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install google-genai python-dotenv
```

3. Create a `.env` file in the project root with your Gemini API credentials:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-flash
```

## Usage

Run the AI agent with a prompt describing what you want it to do:

```bash
python main.py "Your request here"
```

### Examples

```bash
# Analyze code structure
python main.py "Read and analyze the main.py file to understand the project structure"

# Execute Python code safely
python main.py "Run the main.py file with arguments 'hello world'"

# Create new files
python main.py "Create a new Python file called hello.py that prints 'Hello, World!'"

# Explore project structure
python main.py "Show me all the files in the current directory and their sizes"

# Debug and fix code
python main.py "Read the test file, run it, and fix any errors you find"
```

### Verbose Mode

Add the `--verbose` flag to see detailed information about function calls and token usage:

```bash
python main.py --verbose "Your request here"
```

## Project Structure

```
├── main.py                 # Main entry point
├── run_agent.py           # Core agent logic
├── config.py              # Configuration settings
├── env_variables.py       # Environment variable handling
├── system_args.py         # Command line argument parsing
├── functions/             # Available function implementations
│   ├── call_function.py   # Function call dispatcher
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
└── calculator/            # Test project (dummy project for testing the agent)
```

## How It Works

1. **Secure Initialization**: The agent starts with a restricted working directory and validates all operations
2. **Function Planning**: Receives your prompt and creates a plan using available secure functions
3. **Sequential Execution**: Makes multiple function calls in sequence to accomplish complex tasks
4. **Security Validation**: Every file operation is validated to ensure it stays within the sandbox
5. **Timeout Protection**: Has built-in limits to prevent infinite loops and resource exhaustion
6. **Natural Responses**: Returns results as human-readable natural language responses

## Configuration

Key configuration options in `config.py`:

- `AGENT_TIMEOUT_COUNT`: Maximum number of function call loops (default: 20)
- `MAX_CONTENT_CHUNK_SIZE`: Maximum content size for file operations (default: 10000 characters)
- `TIMEOUT`: Timeout for individual operations (default: 30 seconds)

## Security Features

- **Sandboxed Environment**: All operations are constrained to a specific working directory
- **Path Validation**: Every file path is validated to prevent directory traversal attacks
- **Content Limits**: File reading is limited to prevent memory exhaustion (10,000 characters max)
- **Execution Timeouts**: Python file execution has a 30-second timeout limit
- **Loop Protection**: Maximum of 20 function call iterations to prevent infinite loops
- **Transparent Logging**: All function calls are logged when using verbose mode

## Development

This project demonstrates how to build secure AI agents with function calling capabilities. It showcases:

- **Secure Function Calling**: How to safely expose file system operations to AI agents
- **Sandboxing Techniques**: Path validation and working directory restrictions
- **Error Handling**: Robust error handling for all function operations
- **Token Management**: Tracking and logging of API usage for cost monitoring

The calculator directory is included as a minimal test project to demonstrate the agent's capabilities in a controlled environment.

## License

This project is for educational purposes.
