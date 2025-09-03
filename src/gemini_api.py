import os
# import google.generativeai as genai
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def call_gemini(prompt):
    """
    Call Google Gemini API with a prompt.

    Args:
        prompt (str): The prompt to send to Gemini.

    Returns:
        str: The response from Gemini.
    """
    try:
        client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"