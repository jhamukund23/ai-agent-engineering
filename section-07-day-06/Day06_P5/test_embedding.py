import os
from dotenv import load_dotenv
from openai import OpenAI
from similarity import cosine_similarity

load_dotenv()

endpoint = os.getenv("AZURE_EMBEDDING_ENDPOINT")
api_key = os.getenv("AZURE_EMBEDDING_KEY")
deployment_name = os.getenv("AZURE_EMBEDDING_DEPLOYMENT")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key,
)

def create_embedding(content):
    embedding1 = client.embeddings.create(
    model=deployment_name,
    input=content
    ).data[0].embedding
    return embedding1





