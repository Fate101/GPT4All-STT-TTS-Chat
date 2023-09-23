import speech_recognition as sr
from gpt4all import GPT4All
import keyboard
from gtts import gTTS
import pygame
import time
from os import system,name
model = None
response = None

# Uses default input for communication to send Speech to Google to Resolve it to text      
def speech_to_text():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening for speech...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Could not understand")
            return None
        except sr.RequestError as e:
            print(f"Error: {e}")
            return None

# Takes the text and puts it through Googles Text to Speech. Might be worth replacing?
def speak_response(response_text):
    tts = gTTS(response_text)
    #Saves in the location the script is ran
    tts.save("response.mp3")
    #Give it enough time to download and save the response
    time.sleep(3)
    pygame.mixer.init(devicename="DEVICENAMEHERE") #Replace Wave Link etc with the name of your Audio Output. i.e "Headphones (Realtek...)" or clear () to make it use default device
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    #Wait till audio has finished playing
    while pygame.mixer.music.get_busy() == True:
        continue
    pygame.mixer.quit()
                    
def main():
    global model
    global response
    if model == None:
        # Windows Default Location for models predownloaded C:\Users\{USERNAMEHERE}\.cache\gpt4all
        model = GPT4All(model_name='MODELNAMEHERE.bin')
    
    #This is where you give the AI personality or context
    sysprompt = "Respond like xyz."
    with model.chat_session(system_prompt=sysprompt):
        print("Press HOME key to start listening or Q to quit.")
        while True:
            # Loops here to ensure it remember previous responses
            key_pressed = keyboard.read_event().name
            if key_pressed == "q":
                break

            if key_pressed == "home":
                text = speech_to_text()
                if text:
                    print(f"You Said: {text}")
                    response = model.generate(prompt=text, temp=0)
                    print ("")
                    if response:
                        print(f"GPT4All: {response}")
                        speak_response(response)
                        print("Press HOME key to start listening or Q to quit.")


if __name__ == "__main__":
    main()
