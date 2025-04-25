import datetime
from ai_helper import get_ai_response  # Make sure this file is in your folder

def handle_command(command):
    if not command:
        return "I didn't catch that."

    if "time" in command:
        return datetime.datetime.now().strftime("It is %I:%M %p.")
    elif "joke" in command:
        return "Why did the chicken cross the road? To get to the other side!"
    elif "your name" in command:
        return "I am your voice assistant."
    
    # AI Mode condition 
    elif "ai mode" in command or "talk to you" in command:
        return get_ai_response("Let's chat. " + command)
        
    #Fallback
    else:
        return "Sorry, I can't help with that yet."
