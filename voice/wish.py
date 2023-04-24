
import datetime
import voice.speak as sp

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        sp.speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        sp.speak("Jai Shree Ram")

    else:
        sp.speak("Good Evening")