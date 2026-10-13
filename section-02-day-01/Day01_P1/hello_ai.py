from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration from the .env file
load_dotenv()

# Create a client that communicates with the configured AI provider
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

# Send a question to the AI model using the newer Responses API
response = client.responses.create(
    model=os.getenv("MODEL"),
    input=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence?"
        }
    ]
)

# Display the response
print(response.output_text)
