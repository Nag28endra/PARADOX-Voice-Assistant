import datetime
from speak import Say
import pywhatkit
import os
import requests
import webbrowser
import Listen
import pyjokes
from dotenv import load_dotenv


load_dotenv()
notepad_path = os.getenv('notepad_path')
ms_word = os.getenv('ms_word')
main_image=os.getenv('main-image')
title_image=os.getenv('title-image')
radiohalo_image=os.getenv('radiohalo-image')
motion_sphere_image=os.getenv('motion-sphere-image')
radar_image=os.getenv('radar-image')
t200w_image=os.getenv('200w-image')
reload_image=os.getenv('reload-image')
alien_image=os.getenv('alien-image')
initiating_image=os.getenv('initiating-image')
news_api=os.getenv('news_api')

def Time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    Say(time)

def Date():
    date = datetime.datetime().today()
    Say(date)

def NonInputExecution(query):
    query = str(query)

    if 'time' in query:
        Time()
    
    elif "date" in query:
        Date()

def InputExecution(tag,query):
    if "wikipedia" in tag:
        name = str(query).replace("", "")
        import wikipedia
        result = wikipedia.summary(name,1)
        Say(result)

    elif 'search' in tag:
        query = str(query).replace('search','')
        pywhatkit.search(query)
    elif 'notepad' in tag:
        os.startfile(notepad_path)
    elif 'cnotepad' in tag:
        os.system("taskkill /f /im notepad++.exe")

    elif 'commandprompt' in tag:
        os.system("start cmd")
    
    elif 'word' in tag:
        os.startfile(ms_word)

    elif 'powerpoint' in tag:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

    elif 'excel' in tag:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

    elif 'brave' in tag:
        os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

    elif 'cword' in tag:
        os.system("taskkill /f /im WINWORD.EXE")

    elif 'cpowerpoint' in tag:
        os.system("taskkill /f /im POWERPNT.EXE")

    elif 'cexcel' in tag:
        os.system("taskkill /f /im EXCEL.EXE")
    
    elif 'cbrave' in tag:
         os.system("taskkill /f /im brave.exe")

    elif 'news' in tag:
        Say('give me some time to fetch the top headlines..')
        news_url = news_api
        main_page = requests.get(news_url).json()
        articles = main_page["articles"]
        head = []
        day=["first","second","third","fourth","fifth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range(len(day)):
            Say(f'todays {day[i]} news is:{head[i]}')

    elif 'play' in tag:
        song = str(query).replace('play', '')
        Say(f"playing {song}")
        pywhatkit.playonyt(song)
    
    elif 'open youtube' in tag:
        Say('opening youtube')
        webbrowser.open('www.youtube.com')

    elif 'open google' in tag:
        Say('What should I Search?')
        search  = str(query).replace('', "")
        webbrowser.open(f'{search}')

    elif 'joke' in tag:
        Say(pyjokes.get_joke())