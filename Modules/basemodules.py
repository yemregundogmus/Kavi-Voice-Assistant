from gtts import gTTS
import speech_recognition as sr
from time import ctime
from gtts import gTTS
import os
import pickle

class Main:

    def speak(audioString):
        tts = gTTS(text=audioString, lang='tr')
        tts.save("audio.mp3")
        os.system("audio.mp3")

    def recordAudio():
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
    
        # Speech recognition using Google Speech Recognition
        data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio, language='tr-tr')
            data = data.lower()
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Ne Dediğini Anlamadım")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            
        return data