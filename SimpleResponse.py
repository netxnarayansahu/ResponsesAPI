import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

project_endpoint = os.getenv("PROJECT_ENDPOINT")
if not project_endpoint:
    raise ValueError(
        "PROJECT_ENDPOINT is not set. Add it to your .env file or environment variables."
    )

credential = DefaultAzureCredential()
project_client = AIProjectClient(endpoint=project_endpoint, credential=credential)
openai_client = project_client.get_openai_client()

# Generate a response using the OpenAI-compatible client.
response = openai_client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="Write a creative story about AI.",
    temperature=0.8,  # Higher temperature for more creativity,Controls randomness (0.0-2.0). Higher values make output more creative and varied
    # top_p: Alternative to temperature for controlling randomness
    max_output_tokens=200,  # Limit response length.Limits the maximum number of tokens in the response
    # Using a Foundry direct model
    model="microsoft-phi-4",  # Example Foundry direct model
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="What are the benefits of small language models?",
)

# Display the response
print(f"Response: {response.output_text}")
print(f"Response ID: {response.id}")
print(f"Tokens used: {response.usage.total_tokens}")
print(f"Status: {response.status}")

# Using a Foundry direct model
response = openai_client.responses.create(
    model="microsoft-phi-4",  # Example Foundry direct model
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="What are the benefits of small language models?",
)
# Display the response
print(f"Response: {response.output_text}")
print(f"Response ID: {response.id}")
print(f"Tokens used: {response.usage.total_tokens}")
print(f"Status: {response.status}")
