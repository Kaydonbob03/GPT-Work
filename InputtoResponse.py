import os
from openai import OpenAI

# Retrieve your OpenAI API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is set
if not api_key:
    raise ValueError("The OpenAI API key is not set in the environment variables.")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# -------------------------------------------------------------------


def generate_response(prompt, model_name="gpt-4-turbo"):
    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        if model_name == "gpt-4-turbo":
            print("Failed to access GPT-4 Turbo, falling back to GPT-3.5 Turbo.")
            return generate_response(prompt, "gpt-3.5-turbo")
        else:
            raise e

while True:
    # Get user input
    input_text = input("Enter your input text (or type 'exit' to quit): ")

    if input_text.lower() == "exit":
        print("Goodbye!")
        break

    # Generate a response
    generated_response = generate_response(input_text)

    # Print the generated response
    print("Generated Response:")
    print(generated_response)


    
    
    # -------------------------------------------------------------------------
    
    # Talk With Fixed Prompt Block


# # Fixed prompt that will be added to the beginning of each input
# fixed_prompt = "You are acting as a Canadian fratboy. Please phrase your response as such using 'Bro' and 'eh' frequently.:\n"

# def generate_response(prompt, model_name="gpt-4-turbo"):
#     try:
#         completion = client.chat.completions.create(
#             model=model_name,
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         return completion.choices[0].message.content.strip()
#     except Exception as e:
#         if model_name == "gpt-4-turbo":
#             print("Failed to access GPT-4 Turbo, falling back to GPT-3.5 Turbo.")
#             return generate_response(prompt, "gpt-3.5-turbo")
#         else:
#             raise e

# while True:
#     # Get user input
#     input_text = input("Enter your input text (or type 'exit' to quit): ")

#     if input_text.lower() == "exit":
#         print("Goodbye!")
#         break

#     # Generate a response
#     generated_response = generate_response(input_text)

#     # Print the generated response
#     print("Generated Response:")
#     print(generated_response)

