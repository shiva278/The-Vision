import pytesseract
from PIL import Image 		        # adds image processing capabilities
from gtts import gTTS               # converts the text to speech
from playsound import playsound     # plays audio files
import speech_recognition as sr     # recognises voice input
import pyaudio                      # needed for working of playsound library
import os                           # takes care of searching/creating directories
import pathlib
from time import sleep
#from picamera import PiCamera
import json



fi="instr "
fr="read instr "
cnfm_n="confirm_"
err="error "
ext= ".mp3"
i_dir=""
i_dir+='C:/Users/sampleUser/Directory/subDirectory/load_instructions/'
read_dir=""
read_dir+='C:/Users/sampleUser/Directory/subDirectory/read_instructions/'
cnfm_dir=""
cnfm_dir+="C:/Users/sampleUser/Directory/subDirectory/confirmation/"
err_dir=""
err_dir+='C:/Users/sampleUser/Directory/subDirectory/errs/'
root='C:/Users/sampleUser/Directory/subDirectory/'

def ac(txt, path):
    tts = gTTS(txt)
    file = pathlib.Path(path + txt+ext)
    if file.exists ():
        print ("File exists")
    else:
        tts.save(path + txt + ext)

#def td(img):


def a_cnfm(book_name):
    tts = gTTS("You said " + book_name + ". Are you sure? Say yes to continue or no to say it again.")
    file = pathlib.Path(cnfm_dir + cnfm_n + book_name + ext)
    if file.exists():
        print("File exists")
    else:
        tts.save(cnfm_dir + cnfm_n + book_name + ext)


def vi(i):
    # FUNCTION TO PLAY ANY OF THE DEFINED INSTRUCTION AUDIO FILES
    file=fi+str(i)+ext
    playsound(i_dir+file)

def ve(i):
    # FUNCTION TO PLAY ANY OF THE DEFINED ERROR AUDIO FILES
    file=err+str(i)+ext
    playsound(err_dir+file)

def vc(i):
    # FUNCTION TO PLAY ANY OF THE DEFINED CONFIRMATION AUDIO FILES
    file=cnfm_n+str(i)+ext
    playsound(cnfm_dir+file)

def v_read(i):
    file=fr+str(i)+ext
    playsound(read_dir+file)

def bn(s):
    ls=list(s)
    c,f=0,1
    for i in range(len(ls)):
        if c==0:
            ls[i]=ls[i].upper()
            c=1
            continue
        if ls[i]==" ":
            f=0
            continue
        if f==0:
            ls[i]=ls[i].upper()
            f=1
    s2=""
    s2=s2.join(ls)
    return s2


def sp():
    r = sr.Recognizer()
    r.energy_threshold = 300
    with sr.Microphone() as source:
        audio = r.listen(source)
        book_name = ""
        book_name += r.recognize_google(audio)
        r.adjust_for_ambient_noise(source, duration=0.2)
        # return book_name
    try:
        print("You said ", end="")
        book_name = ""
        book_name += r.recognize_google(audio)
        if book_name!='':
            return book_name
    except sr.UnknownValueError:
        ve(1)
        return "error 1"
    except sr.RequestError as ext:
        ve(2)
        return "error 2"

#function, si() speak instruction is used to detect the main instructions the user gives
def si():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        instr = ""
        instr += r.recognize_google(audio)
        return instr
    except sr.UnknownValueError:
        #print("Could not understand audio")
        ve(1)
        return "error 1"
    except sr.RequestError as ext:
        #print("Could not request results; {0}".format(ext))
        ve(2)
        return "error 2"

def decision():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        # print("You said ", end="")
        decision = ""
        decision += r.recognize_google(audio)
        return decision
    except sr.UnknownValueError:
        # print("Could not understand audio")
        ve(1)
    except sr.RequestError as ext:
        # print("Could not request results; {0}".format(ext))
        ve(2)

def cnfm(book_name):
    a_cnfm(book_name)
    vc(book_name)

def cnfm_dlt(book_name):
    if os.path.exists(cnfm_dir + cnfm_n + book_name + ext):
        os.remove(cnfm_dir + cnfm_n + book_name + ext)

def create(book_name):
    if not os.path.exists(root):
        os.mkdir(root)
    dir = os.path.join(root, book_name)
    if not os.path.exists(dir):
        # creating directory for book
        os.mkdir(dir)

        #creating directory for pics
        pic_dir = os.path.join(dir, 'pics')
        os.mkdir(pic_dir)

        #creating directory for text files generated
        text_dir =  os.path.join(dir, 'text')
        os.mkdir(text_dir)

        # creating directory for audio files generated
        tts_dir =  os.path.join(dir, 'audio')
        os.mkdir(tts_dir)

        # creating log file
        first_log = {"last_added_page": 1, "bookmark": 1, "first_page": 1, "list_of_files": [1]}
        with open(dir + "log.json", "w") as fw:
            json.dump(first_log, fw)


def getImgName(path):
    with open(path + "log.json", "r") as fr:
        json_obj = json.load(fr)
    json_obj["last_added_page"] = json_obj["last_added_page"] + 1
    json_obj["list_of_files"].append(new_page)
    with open(path + "log.json", "w") as fw:
        json.dump(json_obj, fw)
    img_name = json_obj["last_added_page"]
    return img_name

# def capture(path):
    # camera = PiCamera()
    # camera.resolution = (2560, 1936)#3264, 2448
    # img_name = getImgName(path)
    # imgFilePath =  os.path.join(path, 'pics')
    # logFilePath = imgFilePath
    # logFilePath = os.path.join(logFilePath, log_image + '.json')
    # imgFilePath =  os.path.join(imgFilePath, img_name + '.jpg')
    # #taking pic and saves it as jpg
    # if camera.capture(imgFilePath):
    #     if os.path.exists(logFilePath):
    #         with open("logFilePath", "r") as fr:
    #             json_obj = json.load(fr)
    #         json_obj["last_added_page"] = json_obj["last_added_page"] + 1
    #         new_page = json_obj["last_added_page"]
    #         json_obj["list_of_files"].append(new_page)
    #         with open("logFilePath", "w") as fw:
    #             json.dump(json_obj, fw)
    #     else:
    #         # creating images log file
    #         first_log = {"last_added_page": 1, "bookmark": 1, "first_page": 1, "list_of_files": [1]}
    #         with open(logFilePath, "w") as fw:
    #             json.dump(first_log, fw)
    # return imgFilePath
    # return 'lol'

def getName(path):
    with open(path + "log.json", "r") as fr:
        json_obj = json.load(fr)
    txt_name = json_obj["last_added_page"]
    return txt_name

def ocr(path, img_path):
    #TODO tesseract
    # OCR operation using tesseract
    img = Image.open(img_path)
    text = pytesseract.image_to_string(img, lang='eng')

    # creating directory for generated text :
    txt_name = getName(path)
    txtFilePath =  os.path.join(path, 'text')
    logFilePath = txtFilePath
    logFilePath = os.path.join(logFilePath, log_text + '.json')
    txtFilePath =  os.path.join(txtFilePath, txt_name + '.txt')
    with open(txtFilePath, "w") as tf:
        if tf.write(text):
            if os.path.exists(logFilePath):
                with open("logFilePath", "r") as fr:
                    json_obj = json.load(fr)
                json_obj["last_added_page"] = json_obj["last_added_page"] + 1
                new_page = json_obj["last_added_page"]
                json_obj["list_of_files"].append(new_page)
                with open("logFilePath", "w") as fw:
                    json.dump(json_obj, fw)
            else:
                # creating images log file
                first_log = {"last_added_page": 1, "bookmark": 1, "first_page": 1, "list_of_files": [1]}
                with open(logFilePath, "w") as fw:
                    json.dump(first_log, fw)

    return txtFilePath

def audio(path, txt_path):
    # converting text-to-speech
    with open(txt_path) as f:       # we open the text file and...
        tts = gTTS(f.read(), "en")  # convert word by word to speech and save it in tts object

    # creating directory for generated speech :
    tts_name = getName(path)
    ttsFilePath = os.path.join(path, 'audio')
    logFilePath = ttsFilePath
    logFilePath = os.path.join(logFilePath, log_audio + '.json')
    ttsFilePath = os.path.join(ttsFilePath, tts_name + '.mp3')
    if tts.save(ttsFilePath):
        if os.path.exists(logFilePath):
            with open("logFilePath", "r") as fr:
                json_obj = json.load(fr)
            json_obj["last_added_page"] = json_obj["last_added_page"] + 1
            new_page = json_obj["last_added_page"]
            json_obj["list_of_files"].append(new_page)
            with open("logFilePath", "w") as fw:
                json.dump(json_obj, fw)
        else:
            # creating images log file
            first_log = {"last_added_page": 1, "bookmark": 1, "first_page": 1, "list_of_files": [1]}
            with open(logFilePath, "w") as fw:
                json.dump(first_log, fw)
    return ttsFilePath