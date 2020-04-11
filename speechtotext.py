# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import speech_recognition as sr
import os
import sys

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command

def sofiaResponse(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

def assistant(command):
    "if statements for executing commands"
    if 'call an ambulance' in command:
            sofiaResponse('Call an ambulance from Prince of Wales hospital.')
        #time
    elif 'time' in command:
        import datetime
        now = datetime.datetime.now()
        sofiaResponse('Current time is %d hours %d minutes' % (now.hour, now.minute))

# sofiaResponse('Hi User, I am your personal voice assistant. What can i do for you?')
# #loop to continue executing multiple commands
# while True:
#     assistant(myCommand())
