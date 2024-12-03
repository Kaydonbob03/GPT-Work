import openai
import os
import time
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("OPENAI_ASSISTANT_ID", "asst_xUGkzWCAmNNpeicMvwf9sA4b")

# Generate dynamic log file name
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
log_file = f"assistant_log_{timestamp}.txt"

# Cool print statements
print(Fore.CYAN + "Logged in as:" + Style.RESET_ALL, Fore.YELLOW + f"{openai.api_key[:10]}... (API Key)")
print(Fore.CYAN + "Assistant logged in as:" + Style.RESET_ALL, Fore.GREEN + f"{assistant_id}")

# Ensure API key and assistant ID are set
if not openai.api_key or not assistant_id:
    raise ValueError(Fore.RED + "API Key or Assistant ID is missing. Please set them as environment variables.")

# Create a new thread
print(Fore.CYAN + "Creating new thread...")
thread = openai.beta.threads.create()
thread_id = thread.id
print(Fore.GREEN + "Thread active:" + Style.RESET_ALL, Fore.MAGENTA + f"{thread_id}")

# Open log file in append mode with UTF-8 encoding
with open(log_file, "a", encoding="utf-8") as log:
    log.write(f"Conversation Start ({timestamp})\n")
    log.write("="*40 + "\n\n")
print(Fore.LIGHTBLACK_EX + f"Log file created/updated: {log_file}")

# Track last processed message ID
last_message_id = None

# Continuous conversation loop
while True:
    # Get user input
    user_message = input(Fore.CYAN + "You: " + Style.RESET_ALL)
    
    # Exit condition
    if user_message.lower() in ['exit', 'quit']:
        print(Fore.YELLOW + "Exiting conversation. Goodbye!")
        with open(log_file, "a", encoding="utf-8") as log:
            log.write("\nConversation End\n" + "="*40 + "\n\n")
        print(Fore.LIGHTBLACK_EX + f"Log file updated: {log_file}")
        break

    # Log the user's message
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"You: {user_message}\n")
    print(Fore.LIGHTBLACK_EX + f"Log file updated: {log_file}")
    
    # Send user message to the thread
    openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_message
    )
    print(Fore.GREEN + "Message sent successfully.")
    
    # Run the assistant on the thread
    print(Fore.CYAN + "Running assistant on the thread...")
    run = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    
    # Wait for the run to complete
    while run.status in ["queued", "in_progress"]:
        print(Fore.YELLOW + f"Run status: {run.status}. Waiting...")
        time.sleep(1)
        run = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
    
    if run.status == "completed":
        print(Fore.GREEN + "Assistant has processed the thread.")
    else:
        print(Fore.RED + f"Run failed with status: {run.status}")
        exit()
    
    # Retrieve and display the assistant's response
    print(Fore.CYAN + "Retrieving assistant response...")
    messages = openai.beta.threads.messages.list(thread_id=thread_id)
    
    # Find the latest assistant message not previously processed
    for message in messages.data:
        if message.role == "assistant" and message.id != last_message_id:
            assistant_reply = message.content[0].text.value
            last_message_id = message.id
            print(Fore.GREEN + f"Assistant: {assistant_reply}")
            
            # Log the assistant's reply
            with open(log_file, "a", encoding="utf-8") as log:
                log.write(f"Assistant: {assistant_reply}\n\n")
            print(Fore.LIGHTBLACK_EX + f"Log file updated: {log_file}")
            break
