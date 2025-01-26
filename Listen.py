import speech_recognition as sr
from speak import Say
def Listen():
    recog = sr.Recognizer() # this object recognizes the audio from the user
    with sr.Microphone() as source:  # this will activate the microphone
        print('Listening...')
        recog.pause_threshold=2
        audio = recog.listen(source,timeout=5,phrase_time_limit=5)
    
    try:
        print('Recognizing...')
        query = recog.recognize_google(audio,language='en-in')
        print(f'You said: {query}')
    except Exception as e:
        Say('say that again please..')
        return " "
    
    query = str(query)
    return query.lower()

# Listen()