"""Speech capture and recognition helpers for the PARADOX assistant."""

import speech_recognition as sr

from speak import Say


def Listen():
    """Capture microphone audio and convert it to lowercase text."""
    recognizer = sr.Recognizer()

    # Activate the microphone and wait for speech input.
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 2
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print('Recognizing...')
        query = recognizer.recognize_google(audio, language='en-in')
        print(f'You said: {query}')
    except Exception:
        # If speech recognition fails, ask the user to repeat the command.
        Say('say that again please..')
        return " "

    return str(query).lower()