from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the provider settings from the .env file
load_dotenv()

# Create an OpenAI-compatible client using the configured provider
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

# Display the assistant heading
print("=" * 40)
print("      My AI Assistant")
print("=" * 40)

# Keep chatting until the user enters "quit"
while True:

    # Read a prompt from the user
    user_input = input("\nYou : ")

    # Exit the conversation when requested
    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break

    # Send the prompt to the configured model as a user message
    response = client.responses.create(
            model=os.getenv("MODEL"),
            input=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

    # Print the model's text response
    print("\nAI :", response.output_text)
