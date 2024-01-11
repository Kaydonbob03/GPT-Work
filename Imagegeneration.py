from openai import OpenAI
import requests
import os

# Retrieve your OpenAI API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is set
if not api_key:
    raise ValueError("The OpenAI API key is not set in the environment variables.")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Prompt for generating the image
prompt = input("Enter a prompt to generate an image: ")

try:
    # Generate an image using DALL-E 3
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    # Extract the image URL from the response
    image_url = response.data[0].url
    print(image_url)

    # Specify the save path
    save_path = r'C:\Specify\Path\Here'

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Fetch the image from the URL
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        # Save the image to the specified path
        with open(save_path, "wb") as image_file:
            image_file.write(image_response.content)
        print(f"Image generated and saved at {save_path}")
    else:
        print(f"Failed to fetch the image: {image_response.status_code}")
except Exception as ex:
    print(f"An error occurred: {ex}")
