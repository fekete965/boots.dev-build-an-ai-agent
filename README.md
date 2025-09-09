# AI Coding Agent

An intelligent AI coding agent built with Google's Gemini API that can interact with your codebase through function calls. The agent can read files, execute Python code, write files, and navigate directories to help you with coding tasks.

## Features

The AI agent has access to the following capabilities:

- **File Operations**: Read file contents and get directory listings
- **Code Execution**: Run Python files with optional arguments
- **File Writing**: Create or overwrite files with new content
- **Directory Navigation**: Explore project structure and file information

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
# Analyze a Python file
python main.py "Read and analyze the main.py file in the calculator directory"

# Execute code
python main.py "Run the calculator with the expression '2 + 3 * 4'"

# Create a new file
python main.py "Create a new Python file called hello.py that prints 'Hello, World!'"

# Get project structure
python main.py "Show me all the files in the project"
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

1. The agent receives your prompt and creates a plan using available functions
2. It can make multiple function calls in sequence to accomplish complex tasks
3. All operations are scoped to a specific working directory for security
4. The agent has a timeout limit to prevent infinite loops
5. Results are returned as natural language responses

## Configuration

Key configuration options in `config.py`:

- `AGENT_TIMEOUT_COUNT`: Maximum number of function call loops (default: 20)
- `MAX_CONTENT_CHUNK_SIZE`: Maximum content size for file operations (default: 10000 characters)
- `TIMEOUT`: Timeout for individual operations (default: 30 seconds)

## Security

- The agent operates within a restricted working directory
- File paths are validated and sanitized
- Function calls are logged for transparency

## Development

This project is built as a learning exercise for creating AI agents with function calling capabilities. The calculator directory contains a simple test project that the agent can interact with to demonstrate its capabilities.

## License

This project is for educational purposes.
