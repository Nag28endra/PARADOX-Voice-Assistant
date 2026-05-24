"""Text-to-speech wrapper for PARADOX."""

import pyttsx3


def Say(text):
    """Speak the supplied text using the Windows speech engine."""
    # Create the Microsoft SAPI speech engine.
    engine = pyttsx3.init('sapi5')

    # Load and select the first available voice.
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)

    # Use a faster speaking rate so responses feel responsive.
    engine.setProperty('rate', 170)

    print(" ")
    print(f"paradox: {text}")
    engine.say(text=text)
    engine.runAndWait()
    print(" ")


