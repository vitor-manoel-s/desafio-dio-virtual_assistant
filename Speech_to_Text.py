#import section

import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import webbrowser
import pyaudio


#get mic audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")
        except sr.RequestError:
            speak("Sorry, the service is not available")
    return said.lower()

#speak converted audio to text
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

#function to respond to commands
def respond(text):
    print("Text from get_audio: " + text)
    if 'youtube' in text:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'email' in text:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
    elif 'exit' in text:
        speak("Goodbye, till next time")
        exit()


while True:
    print("I am listening...")
    text = get_audio()
    respond(text)