import datetime
import pywhatkit
import requests
from ai_helper import get_ai_response  # if you have AI chat feature

def handle_command(command):
    if not command:
        return "I didn't catch that."

    command = command.lower()

    if "time" in command:
        return datetime.datetime.now().strftime("It is %I:%M %p.")
    
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today}."
    
    elif "day" in command:
        today = datetime.datetime.now().strftime("%A")
        return f"Today is {today}."
    
    elif "weather" in command:
        return get_weather()
    
    elif "play" in command:
        song = command.replace("play", "").strip()
        pywhatkit.playonyt(song)
        return f"Playing {song} on YouTube."
    
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        pywhatkit.search(query)
        return f"Searching for {query} on Google."

    elif "fun fact" in command:
        return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3000 years old and still perfectly edible!"

    elif "your name" in command:
        return "I am your voice assistant."
    
    elif "ai mode" in command or "talk to you" in command:
        return get_ai_response("Let's chat. " + command)

    else:
        return "Sorry, I can't help with that yet."

def get_weather():
    # Fake weather response for now
    return "It's a beautiful day today!"

