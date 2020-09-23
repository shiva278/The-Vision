import os
import headers as v
import json
import sys
from playsound import playsound
import speech_recognition as sr
import firebase as fire

flag = True

def sp():
    # FUNCTION, "sp"(speech) IS USED TO RECOGNISE VOICE INPUT FROM USER AND RETURN STRING VALUE
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=1)
    st = ''
    st+= r.recognize_google(audio)
    if st!='':
        return st

while(flag):
    v.vi(1)
    n=""
    for i in range(3):
        n = sp()

        path = os.path.join('Books', n)
        path = os.path.join(path, 'Audio')
        for root, dirs, files in os.walk(path):         # if the audio files exist
            for filename in files:                      # take each audio file
                filename = os.path.join(path, filename)
                playsound(filename)                     # and PLAY IT

    v.vi(8)