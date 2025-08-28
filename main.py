import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsApi = "6276a8e5ccae44febbd47d35b87c0c7b"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def aiprocess(commad):
#     client = openAI(api_key="",)

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     message=[
#         {"role": "system","content": "you are a virtual assitance named jarvis skilled in general task like alexa and google cloud "},
#         {"role": "user", "content": command}
#     ]
#     )
#     return completion.choices[0].massage.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open whats up" in c.lower():
        webbrowser.open("https://web.whatsup.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=6276a8e5ccae44febbd47d35b87c0c7b")
        if r.status_code == 200:
            # parse  the json responce
            data = r.json()

            # Extract the artihcle
            articles = data.get('articles', [])

            # print the headline
            for article in articles:
                speak(article['title'])

    # else:
    #     # Let openAi handle this
    #     output = aiprocess(c)
    #     speak(output)


if __name__ == "__main__":
    speak("yes sir, how may i help you")
    while True:
        #listen for wake word "jarvis"
        #obtain audio from microphone
        r = sr.Recognizer()
            
        #recognize speech using google
        try:
            with sr.Microphone() as source:
                print("listening.....")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 3)
            command = r.recognize_google(audio)
            if "jarvis" in command.lower():
                speak("yes sir")
                print(command)
                #listen for command
                with sr.Microphone() as source:
                    print("jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print(" jarvis error, {0}".format(e))