# -*- coding: utf-8 -*-
# @Author: fredy
# @Date:   2020-04-10 19:41:52
# @Last Modified by:   fredy
# @Last Modified time: 2020-04-11 14:22:34

def phSpeak(text):
    import win32com.client
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def pySpeak(text):
    import pyttsx3
    # init function to get an engine instance for the speech synthesis
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # for voice in voices:
    #     print("Voice: %s" % voice.name)
    #     print(" - ID: %s" % voice.id)
    #     print(" - Languages: %s" % voice.languages)
    #     print(" - Gender: %s" % voice.gender)
    #     print(" - Age: %s" % voice.age)
    #     print("\n")
    #engine.setProperty('rate', 150)
    #engine.setProperty('gender','female')
    engine.setProperty("voice", voices[0].id)
    # say method on the engine that passing input text to be spoken
    engine.say('Hello sir, how may I help you, sir.')
    engine.say(text)
    # run and wait method, it processes the voice commands.
    engine.runAndWait()

if __name__ == "__main__":
    ask = "How crowded is the place?"
    response = "The crowded level, is medium."
    for i in range(10):
        if "crowd" in ask:
            #phSpeak(response)
            pySpeak(response)
