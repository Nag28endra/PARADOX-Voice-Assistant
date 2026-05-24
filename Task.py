"""Task handlers for PARADOX commands that trigger actions or external apps."""

import datetime
import os

import pyjokes
import pywhatkit
import requests
import webbrowser
from dotenv import load_dotenv

from speak import Say


load_dotenv()

# Paths and API settings are loaded from the environment so they can be changed
# without editing the source code.
notepad_path = os.getenv('notepad_path')
ms_word = os.getenv('ms_word')
news_api = os.getenv('news_api')


def Time():
    """Read the current system time aloud."""
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    Say(current_time)


def Date():
    """Read the current date aloud."""
    current_date = datetime.date.today().strftime('%B %d, %Y')
    Say(current_date)


def NonInputExecution(query):
    """Handle commands that do not require additional user input."""
    query = str(query)

    if 'time' in query:
        Time()
    elif 'date' in query:
        Date()


def InputExecution(tag, query):
    """Handle user commands that trigger application actions or external services."""
    if 'wikipedia' in tag:
        import wikipedia

        name = str(query).replace('', '')
        result = wikipedia.summary(name, 1)
        Say(result)

    elif 'search' in tag:
        query = str(query).replace('search', '')
        pywhatkit.search(query)

    elif 'notepad' in tag:
        os.startfile(notepad_path)

    elif 'cnotepad' in tag:
        os.system('taskkill /f /im notepad++.exe')

    elif 'commandprompt' in tag:
        os.system('start cmd')

    elif 'word' in tag:
        os.startfile(ms_word)

    elif 'powerpoint' in tag:
        os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE')

    elif 'excel' in tag:
        os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE')

    elif 'brave' in tag:
        os.startfile('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe')

    elif 'cword' in tag:
        os.system('taskkill /f /im WINWORD.EXE')

    elif 'cpowerpoint' in tag:
        os.system('taskkill /f /im POWERPNT.EXE')

    elif 'cexcel' in tag:
        os.system('taskkill /f /im EXCEL.EXE')

    elif 'cbrave' in tag:
        os.system('taskkill /f /im brave.exe')

    elif 'news' in tag:
        Say('give me some time to fetch the top headlines..')
        main_page = requests.get(news_api).json()
        articles = main_page['articles']
        headlines = [article['title'] for article in articles]

        # Read the top five headlines aloud.
        day = ['first', 'second', 'third', 'fourth', 'fifth']
        for index, label in enumerate(day[:len(headlines)]):
            Say(f'todays {label} news is:{headlines[index]}')

    elif 'play' in tag:
        song = str(query).replace('play', '')
        Say(f'playing {song}')
        pywhatkit.playonyt(song)

    elif 'open youtube' in tag:
        Say('opening youtube')
        webbrowser.open('www.youtube.com')

    elif 'open google' in tag:
        Say('What should I Search?')
        search = str(query).replace('', '')
        webbrowser.open(f'{search}')

    elif 'joke' in tag:
        Say(pyjokes.get_joke())
