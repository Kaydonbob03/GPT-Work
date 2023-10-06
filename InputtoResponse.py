import openai

# -------------------------------------------------------------------

# Just Talk Block


# Set your OpenAI API key here
api_key = "YOUR_OPENAI_API_KEY"

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Set to gpt-3.5-turbo for GPT3.5 or set to gpt-4 for GPT4
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,   # Change the temperature from 0 to 1 for more or less creative responses. 0 is more probable, 1 is more creative. Default is 0.2
        max_tokens=150     # Specify the maximum number of tokens in the response
    )
    return response.choices[0].message["content"].strip()


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

# # Set your OpenAI API key here
# api_key = "YOUR_OPENAI_API_KEY"

# # Initialize the OpenAI API client
# openai.api_key = api_key

# # Fixed prompt that will be added to the beginning of each input
# fixed_prompt = "You are acting as a Canadian fratboy. Please phrase your response as such using 'Bro' and 'eh' frequently.\n"

# def generate_response(prompt):
#     full_prompt = fixed_prompt + prompt
#     response = openai.ChatCompletion.create(
#         model="gpt-4",  # Set to gpt-3.5-turbo for GPT3.5 or set to gpt-4 for GPT4
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": full_prompt}
#         ],
#         temperature=0.2,   # Change the temperature from 0 to 1 for more or less creative responses. 0 is more probable, 1 is more creative. Default is 0.2
#         max_tokens=150     # Specify the maximum number of tokens in the response
#     )
#     return response.choices[0].message["content"].strip()





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
