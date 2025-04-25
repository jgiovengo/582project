import openai
import os
from dotenv import load_dotenv

# Load the .env file that contains your API key
load_dotenv()

# Assign the API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(prompt):
    try:
        # Send prompt to OpenAI's GPT-3.5 Turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Return the assistant's reply
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Error while getting AI response:", e)
        return "I'm having trouble thinking right now."
