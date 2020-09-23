import headers as v
import sys
import firebase as fire
import speech_recognition as sr
import pyaudio
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
        result = fire.main(n)   # WHEN BOOKNAME, n IS PASSED TO MAIN(),
                                # THE FIREBASE.PY TAKES CARE OF DOWNLOADING ALL THE NECCESSARY FILES FROM FIREBASE
        if result:
            v.vi()
        print(result)
        print(n)