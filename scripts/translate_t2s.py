# Johann Diep (johann@oxdynamics.com) - Oxford Dynamics - November 2022
#
# This script translates speech to text and text to speech.
 
import speech_recognition as sr
import pyttsx3
 

# Initialize the recognizer.
recognizer = sr.Recognizer()
 
# Function to convert text to speech.
def SpeakText(command):
    engine = pyttsx3.init() # Initialize the engine.
    engine.say(command)
    engine.runAndWait()
     
     
# Loop infinitely for user to speak 
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
 
            print("Text: " + text)

            # print("Did you say: ", text)
            # SpeakText(text)
             
    except sr.RequestError as e:
        print("Could not request results: {0}".format(e))
         
    except sr.UnknownValueError:
        print("Unknown error occurred.")