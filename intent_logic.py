import datetime

def handle_command(command):
    if not command:
        return "I didn't catch that."
    if "time" in command:
        return datetime.datetime.now().strftime("It is %I:%M %p.")
    elif "joke" in command:
        return "Why did the chicken cross the road? To get to the other side!"
    elif "your name" in command:
        return "I am your voice assistant."
    else:
        return "Sorry, I can't help with that yet."
