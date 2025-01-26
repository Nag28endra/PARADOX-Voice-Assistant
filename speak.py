import pyttsx3

def Say(text):
    engine = pyttsx3.init('sapi5') # getting the api from microsoft
    voices = engine.getProperty('voices') # loading voices into the variable
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate',170)
    print(" ")
    print(f"paradox: {text}")
    engine.say(text=text)
    engine.runAndWait()
    print(" ")

# Say("hello nagendra")


