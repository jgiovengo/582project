import datetime
import random

def recognize_command(command):
    """
    Matches the user's spoken command to predefined responses.
    """
    command = command.lower()

    if "time" in command:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."

    elif "tell me a joke" in command:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the computer go to therapy? Because it had too many bytes!",
            "I'm reading a book about anti-gravity. It's impossible to put down!"
        ]
        return random.choice(jokes)

    elif "your name" in command or "who are you" in command:
        return "My name is Aztec, your virtual assistant."

    else:
        return None  # Let intent_logic.py fall back to OpenAI or default
