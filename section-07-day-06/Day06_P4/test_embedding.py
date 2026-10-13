from openai import OpenAI
from similarity import cosine_similarity
from dotenv import load_dotenv
import os

load_dotenv()

deployment_name = os.getenv("AZURE_EMBEDDING_DEPLOYMENT")
endpoint = os.getenv("AZURE_EMBEDDING_ENDPOINT")
api_key = os.getenv("AZURE_EMBEDDING_KEY")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key,
)

text1 = "Python is a programming language."
text2 = "Python is used for software development."

embedding1 = client.embeddings.create(
    model=deployment_name,
    input=text1,
).data[0].embedding

embedding2 = client.embeddings.create(
    model=deployment_name,
    input=text2,
).data[0].embedding

print(f"Embedding 1 dimensions: {len(embedding1)}")
print(f"Embedding 2 dimensions: {len(embedding2)}")

score = cosine_similarity(
    embedding1,
    embedding2
)

print(score)
