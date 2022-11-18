# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script translates speech to text and text to speech.
 
import speech_recognition as sr
import pyttsx3
 

# Function to convert text to speech.
def text_to_speech(text):
    engine = pyttsx3.init() # Initialize the engine.
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    # Initialize the recognizer.
    recognizer = sr.Recognizer()
        
    # Looping infinitely for user to speak.
    while(True):   
        try: # Exception handling to handle exceptions at the runtime.
            with sr.Microphone() as source:
                # Wait for a second to let the recognizer adjust the energy threshold 
                # based on the surrounding noise level.
                recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Listening for the user input.
                audio = recognizer.listen(source)
                
                # Using Google to recognize audio.
                text = recognizer.recognize_google(audio)
                text = text.lower()

                return text
                
        except:
            pass

def main():
    output = speech_to_text()
    text_to_speech(output)
    

if __name__ == '__main__':
    main()