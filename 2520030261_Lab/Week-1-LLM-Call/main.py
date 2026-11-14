from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv(override=True)

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Generate content
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Display response
print("\nLLM Response:")
print(response.text)