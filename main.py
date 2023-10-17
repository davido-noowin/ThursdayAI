import os
import time
import pyaudio
import playsound
from gtts import gTTS
from pathlib import Path
import openai
import speech_recognition as sr

with open('gptkey.txt', 'r') as api_key:
    openai.api_key = api_key

LANG = 'en'

PATH = Path() / 'ThursdayAI' / 'playback'
print(PATH)


def main():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)

                if 'Thursday' in said:
                    if 'stop' in said:
                        text = 'goodbye'
                        speech = gTTS(text=text, lang=LANG, slow=False, tld="co.uk")
                        speech.save(PATH / "message.mp3")
                        playsound.playsound(PATH / "message.mp3")
                        os.remove(PATH / "message.mp3")
                        break
                    text = 'how can I be of assistance?'
                    speech = gTTS(text=text, lang=LANG, slow=False, tld="co.uk")
                    speech.save(PATH / "message.mp3")
                    playsound.playsound(PATH / "message.mp3")

            except Exception as e:
                print(e)


if __name__ == "__main__":
    main()