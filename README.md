# GPT4All STT TTS Chat in Python
## Description
This script allows you to use your Microphone to "talk" with the selected GPT4All model on Python. 
100% Local and Free!
This is very basic and not completely user friendly currently but does work.

This is commonly used to do similar things that DougDoug does for his AI Videos.

I made this because I wanted to use this for my streams and haven't made anything in Python for years.
Did it live and took me 2 and a half hours to understand/remember how Python Structuring works... smh

Feel free to take this whole thing and make it better to your needs. No need to credit me as it's super basic.
I do plan to improve it where I can but I'm ultimately happy where it is.
# Requirements

 - Python 3.11.4+ [Tested on Python 3.11.4 - Windows 11]

## Modules
You'll need to install all these modules via pip -m [If you can't use pip -m for whatever reason, please google it]
 - SpeechRecognition
 - gpt4all
 - keyboard
 - gtts
 - pygame

# Models

To speed up the process to get straight to talking. It's advised you pre-download a model from https://gpt4all.io/index.html
and install it before hand.
Windows Location - `C:\Users\USERNAMEHERE\.cache\gpt4all`

If you haven't downloaded beforehand, It will download the selected model automatically. These are about 3GB - 8GB depending on the model.

# Config

## Audio Output
You can set the default audio output here -

    pygame.mixer.init(devicename="DEVICENAME")
Example - 

    pygame.mixer.init(devicename="Wave Link Aux 2 (Elgato Wave:3)")

If you just want to use your default audio output you can do this -

    pygame.mixer.init()

To get your audio device name on Windows. You can find it your Sound Settings
![enter image description here](https://i.imgur.com/zG0XZrN.png)
## Model
You can change the model to any specified on [https://gpt4all.io/index.html](https://gpt4all.io/index.html) here [Yes include .bin] - 

    model  =  GPT4All(model_name='MODELNAMEHERE.bin')
Example - 

    model  =  GPT4All(model_name='orca-mini-13b.ggmlv3.q4_0.bin')

## Personality/Context Prompt
You can change the prompt which applies the personality/context to the conversation here -

    sysprompt  =  "Respond like xyz"
Example -

    sysprompt  =  "Respond like you're an trivia gameshow host that specializes in Video Games. Keep it short. Only give me the next question when I ask for it."

## Other
Some things can be replaced very easily like what services the recognizer uses, key press etc.

# GPT4All Quirks
One thing I want to note. It has been observed that sometimes you'll need to sometimes remind it what context/personality it needs to know set when you ran the script.
