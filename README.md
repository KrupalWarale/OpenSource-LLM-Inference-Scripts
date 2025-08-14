# Large Language Model Inference Scripts

This repository contains Python scripts designed for interacting with various large language models (LLMs) via the Hugging Face Inference API. Each script is tailored to a specific model or a particular interaction style, offering flexibility for different use cases.

## Scripts Overview

### `meta-llama-3.1-8b.py`
This script provides a straightforward interface for the `meta-llama/Llama-3.1-8B-Instruct` model. It supports both single-query interactions and a continuous conversational mode.

**Use Cases:**
*   **Quick Queries:** Get a direct response to a single question provided as a command-line argument.
*   **Interactive Chat:** Engage in a back-and-forth conversation with the Llama 3.1 8B model, ideal for exploratory discussions or iterative prompt refinement.

### `gpt-oss-120b.py`
This script is designed for interacting with the `openai/gpt-oss-120b` model. A key feature of this script is its structured prompting, which encourages the model to provide a "thought process" (reasoning) before a "final answer."

**Use Cases:**
*   **Reasoning Exploration:** Ideal for tasks where understanding the model's intermediate steps or logical flow is as important as the final output.
*   **Complex Problem Solving:** Useful for breaking down intricate problems, as the script explicitly asks the model for step-by-step reasoning.
*   **Debugging or Analysis:** Helps in analyzing how the model arrives at a particular conclusion.

### `gpt-oss-20b.py`
Similar to `gpt-oss-120b.py`, this script interacts with the `openai/gpt-oss-20b` model and also utilizes a structured reasoning prompt template. The functionality and use cases are largely the same as `gpt-oss-120b.py`, but it targets a different model variant.

**Use Cases:**
*   **Reasoning Exploration (Smaller Model):** Provides similar reasoning capabilities as `gpt-oss-120b.py` but with the `openai/gpt-oss-20b` model, which might be suitable for environments with fewer computational resources or when a smaller model's performance is sufficient.
*   **Comparative Analysis:** Can be used to compare the reasoning styles and answer quality between the `gpt-oss-120b` and `gpt-oss-20b` models for similar prompts.

## Features

*   **Command-line Prompting:** Send a single prompt directly from the command line for quick responses.
*   **Interactive REPL:** Engage in continuous chat sessions with models.
*   **Hugging Face Inference API Integration:** All scripts utilize the `huggingface_hub` library for seamless interaction with models hosted on Hugging Face.
*   **Environment Variable Support:** Securely load your Hugging Face API token (`HF_TOKEN` or `HUGGINGFACEHUB_API_TOKEN`) from a `.env` file or system environment variables.
*   **Structured Reasoning (for `gpt-oss-*b.py` scripts):** Explicitly prompts models to show their thought process before delivering a final answer.

## Requirements

*   Python 3.x
*   A Hugging Face API token (can be obtained from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens))
*   `huggingface_hub` library
*   `python-dotenv` library

## Installation

1.  **Clone the repository (if applicable) or create the project files.**
    ```bash
    # If you have a git repository
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    If you don't have a `requirements.txt` file, create one with the following content:
    ```
    huggingface_hub
    python-dotenv
    ```
    Then run:
    ```bash
    pip install huggingface_hub python-dotenv
    ```

5.  **Set up your Hugging Face API Token:**
    Create a file named `.env` in the root directory of your project and add your Hugging Face API token to it:
    ```
    HF_TOKEN="YOUR_HUGGING_FACE_TOKEN"
    ```
    Alternatively, you can set the `HF_TOKEN` or `HUGGINGFACEHUB_API_TOKEN` environment variable directly in your system.

## Usage

### `meta-llama-3.1-8b.py`

#### Single Prompt (Command-line)

To send a single prompt and get a response, pass your prompt as command-line arguments:

```bash
python meta-llama-3.1-8b.py "What is the capital of France?"
```

#### Interactive REPL

To enter an interactive chat session, run the script without any command-line arguments:

```bash
python meta-llama-3.1-8b.py
```

You will see a `>` prompt. Type your message and press Enter. To exit the REPL, type `exit`, `quit`, or press `Ctrl+C` (or `Ctrl+D` on Linux/macOS).

**Example Session:**

```
$ python meta-llama-3.1-8b.py
> Hello, how are you?
I am a large language model, trained by Google. I am functioning correctly. How can I assist you today?
> Tell me a fun fact.
Did you know that a group of owls is called a parliament?
> exit
```

### `gpt-oss-120b.py` and `gpt-oss-20b.py`

These scripts share a similar usage pattern, focusing on extracting reasoning and a final answer from the model.

#### Interactive REPL

To start an interactive session with reasoning extraction, run the respective script:

```bash
python gpt-oss-120b.py
# or
python gpt-oss-20b.py
```

You will be prompted to enter your questions. The script will display the model's thought process and then its final answer separately. Type `exit` to quit.

