from gtts import gTTS
import speech_recognition as sr
from time import ctime
from gtts import gTTS
import os
import pickle
import PyQt5.QtCore as coremodule
import PyQt5.QtMultimedia as multimedia
import sys


class Backend:

    def __init__(self):
        self.app = coremodule.QCoreApplication(sys.argv)

    def playSound(self, audioPath):
        url = coremodule.QUrl.fromLocalFile(audioPath)
        content = multimedia.QMediaContent(url)
        player = multimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        player.stateChanged.connect(self.app.quit)
        self.app.exec()

    def speak(self, audioString):
        tts = gTTS(text=audioString, lang='tr')
        tts.save("audio.mp3")
        # os.system("audio.mp3")
        self.playSound("audio.mp3")

    def recordAudio(self):
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
            print("Ne dediğini anlamadım")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return data