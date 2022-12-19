# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script translates speech to text and text to speech.
 
import speech_recognition as sr
import playsound
import os
import time
from gtts import gTTS


class VoiceClass:
    def __init__(self):
        self.recognizer = sr.Recognizer() # Initialize the recognizer.

    def text_to_speech(self, text):
        tts = gTTS(text = text, lang = 'fr', tld = 'fr')

        filename = 'AI_voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)

        os.remove(filename)

    def speech_to_text(self):
        timeout = time.time() + 15 # 15 seconds time to ask a question

        # Looping infinitely for user to speak.
        while(True):
            if time.time() > timeout: 
                print("Break called.")
                break

            try: # Exception handling to handle exceptions at the runtime.
                print("Try-block called.")

                with sr.Microphone() as source:
                    print("Feel free to speak.")

                    # Wait for a second to let the recognizer adjust the energy threshold 
                    # based on the surrounding noise level.
                    self.recognizer.adjust_for_ambient_noise(source, duration=1)

                    # Listening for the user input.
                    audio = self.recognizer.listen(source)
                    
                    # Using Google to recognize audio.
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    return text
                    
            except:
                print("Pass-block called.")
                pass

def main():
    VoiceObject = VoiceClass()

    i = 0
    while(i < 1):
        output = VoiceObject.speech_to_text()
        print("Your text: " + output)
        VoiceObject.text_to_speech(output)

        i = i + 1


if __name__ == '__main__':
    main()