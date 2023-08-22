import pyttsx3 as pt
import speech_recognition as sr
import wikipedia as wk
import webbrowser as wb


e = pt.init()
v = e.getProperty("voices")
e.setProperty("voice", v[1].id)  # 1 for female and 0


def speak(aa):
    e.say(aa)
    e.runAndWait()


def sp_pri(aa):
    print(aa)
    speak(aa)


def cmd():
    r = sr.Recognizer()

    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=1)
        print("Listening...")
        a2 = r.listen(mic)

    try:
        print("Recognizing...")
        tx = r.recognize_google(a2)
        speak(a2)

    except Exception:
        speak("Pardon... I didn't get that. Can you please repeat")
        return ""

    return tx


def voice():
    sp_pri("Would you prefer male voice or female voice?")

    tx2 = cmd().lower()

    if "female" in tx2:
        sp_pri("Changing voice to female")
        e.setProperty("voice", v[1].id)
        sp_pri("Hello, this is my new voice")

    elif "male" in tx2:
        sp_pri("Changing voice to male")
        e.setProperty("voice", v[0].id)
        sp_pri("Hello, this is my new voice")

    elif "mail" in tx2:
        sp_pri("Changing voice to male")
        e.setProperty("voice", v[0].id)
        sp_pri("Hello, this is my new voice")

    elif tx2 == "":
        voice()

    else:
        sp_pri(f"Sorry, I only hava a male and female voice. I do not have {tx2} voice")


sp_pri("Hii, I am a simple voice assistant")
sp_pri("I can do the following things for you :")
sp_pri("Search something on wikipedia")
sp_pri("Open Google and search something on it")
sp_pri("Open YouTube and search something on it")
sp_pri("Open Spotify")
sp_pri("Open Local drive C or D")
sp_pri("You can also change my voice")

sp_pri("How may I help you")


while 1:
    tx = cmd().lower()

    if "sleep" in tx:
        print("sleep")
        exit(0)

    elif "wikipedia" in tx:
        sp_pri("Searching Wikipedia ...")
        results = wk.summary(tx, sentences=4)
        sp_pri("According to wikipedia")
        sp_pri(results)

    elif "google" in tx:
        sp_pri("What do you want to google?")

        tx2 = cmd().lower()

        if "no" in tx2:
            sp_pri("Opening Google")
            wb.open("google.com")
        else:
            sp_pri(f"Searching {tx2} on Google")
            wb.open(f"google.com/search?q={tx2}")

    elif "youtube" in tx:
        sp_pri("Do you want to search something on youtube? Say no if not else just speak what you want to search")

        tx2 = cmd().lower()

        if "no" in tx2:
            sp_pri("Opening YouTube")
            wb.open("youtube.com")
        else:
            sp_pri(f"Searching {tx2} on YouTube")
            wb.open(f"youtube.com/results?search_query={tx2}")

    elif "spotify" in tx:
        sp_pri("Opening spotify")
        wb.open("spotify.com")

    elif "drive c" in tx:
        sp_pri("Opening Drive C")
        wb.open("C://")

    elif "drive d" in tx:
        sp_pri("Opening Drive D")
        wb.open("D://")

    elif "voice" in tx:
        voice()
