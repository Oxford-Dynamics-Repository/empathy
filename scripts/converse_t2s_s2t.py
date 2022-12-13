# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script translates speech to text and text to speech.
 
import speech_recognition as sr
import os
# import time

class VoiceClass:
    def __init__(self):
        self.recognizer = sr.Recognizer() # Initialize the recognizer.

    def text_to_speech(self, text):
        os.system("say " + text)

    def speech_to_text(self):
        # timeout = time.time() + 60 # hardcode 15s of wait time
        # Looping infinitely for user to speak.
        while(True):

            # if time.time() > timeout:
                # return 'Timeout'

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
    while(i < 2):
        output = VoiceObject.speech_to_text()
        print("Your text: " + output)
        VoiceObject.text_to_speech(output)

        i = i + 1


if __name__ == '__main__':
    main()
