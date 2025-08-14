import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# --- Configuration Section ---
# Set the model name and the prompt template. The template is crucial
# for instructing the model to provide both reasoning and a final answer.
MODEL_NAME = "openai/gpt-oss-20b"
REASONING_PROMPT_TEMPLATE = """
Question: {user_prompt}

Think step-by-step and provide your reasoning here:

{final_answer_key}
"""
# This key is used to split the output string. It must match
# the phrase you use in the prompt template exactly.
FINAL_ANSWER_KEY = "Final Answer:"
# -----------------------------

# Load environment variables from .env file
try:
    load_dotenv()
except Exception as e:
    print(f"Error loading .env file: {e}")
    exit()

hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    print("Error: HF_TOKEN not found in environment variables. Please check your .env file.")
    exit()

# Initialize the InferenceClient with the chosen model and your token
try:
    client = InferenceClient(model=MODEL_NAME, token=hf_token)
except Exception as e:
    print(f"Error initializing InferenceClient: {e}")
    exit()

print("Hugging Face Chat Bot Initialized! Type 'exit' to quit.")
print("-" * 50)

messages = [] # Initialize an empty list to store chat history

while True:
    user_prompt = input("You: ")
    if user_prompt.lower() == 'exit':
        break

    # Format the user's input into our specific reasoning prompt template
    formatted_prompt = REASONING_PROMPT_TEMPLATE.format(user_prompt=user_prompt, final_answer_key=FINAL_ANSWER_KEY)
    messages.append({"role": "user", "content": formatted_prompt})

    try:
        # Request a completion from the model
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            max_tokens=2000, # Increased tokens to allow for detailed reasoning and longer answers
            temperature=0.7,
            stream=True
        )

        full_content = ""
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                full_content += chunk.choices[0].delta.content
                print(chunk.choices[0].delta.content, end="", flush=True)

        print("\n") # Add a newline after the streamed output

        # This is the core logic for separating the content.
        # It looks for the specific key and splits the string at that point.
        if FINAL_ANSWER_KEY in full_content:
            thought_process, final_answer = full_content.split(FINAL_ANSWER_KEY, 1)
            thought_process = thought_process.strip().replace('**', '')
            final_answer = final_answer.strip().replace('**', '')
        else:
            # If the model doesn't follow the prompt, assume the whole
            # response is a direct answer and note that no reasoning was found.
            thought_process = "No clear reasoning provided by the model."
            final_answer = full_content.strip().replace('**', '')

        # Print the results in two separate, formatted sections
        print("\n--- Reasoning ---")
        print(thought_process)
        print(f"\n--- {FINAL_ANSWER_KEY} ---")
        print(final_answer)
        print("-" * 50)

        messages.append({"role": "assistant", "content": full_content})

    except Exception as e:
        print(f"An error occurred during the API call: {e}")