import pyrebase
import os
import requests
from gtts import gTTS

config = {
    # firebase config settings
}

fire = pyrebase.initialize_app(config)

storage = fire.storage()

db = fire.database()

bookRef = db.child("Books").get()
pdfRef = db.child("PDFs").get()


def getName(name):
    return name.split('.')[0]

def getFile(url, cwd, fn) :
    # FUNCTION WHICH DOWNLOADS IMAGE/PDF FILES FROM FIREBASE
    r = requests.get(url, allow_redirects=True)
    cwd = os.path.join(cwd, 'Files')
    if not os.path.exists(cwd):
        os.mkdir(cwd)
    fn = os.path.join(cwd, fn)
    with open(fn, 'wb') as file:  # Use file to refer to the file object
        file.write(r.content)

def getAudio(text, cwd, fn):
    # FUNCTION WHICH GENERATES AUDIO FILES USING TEXT FILES
    cwd = os.path.join(cwd, 'Audio')
    if not os.path.exists(cwd):
        os.mkdir(cwd)
    tts = gTTS(text)
    fn = str(getName(fn)) + '.mp3'
    fn = os.path.join(cwd, fn)
    # if not os.path.exists(fn):
    #     os.mkdir(fn)
    tts.save(fn)

def getTxt(text, cwd, fn) :
    # FUNCTION WHICH GENERATES TEXT FILES USING TEXT DATA FROM FIREBASE
    # r = requests.get(url, allow_redirects=True)
    ttsDir = cwd
    txtfn = fn
    cwd = os.path.join(cwd, 'Texts')
    if not os.path.exists(cwd):
        os.mkdir(cwd)
    fn = os.path.join(cwd, fn)
    with open(fn, 'w') as file:  # Use file to refer to the file object
        file.write(text)
    getAudio(text, ttsDir, txtfn)


def getExt(type):
    return type.split('/')[1]

def fileName(pg, ext):
    return str(pg) + '.' + ext

def handleIt(path):
    # FUNCTION WHICH CREATES REQUIRED DIRECTORIES FOR STORING IMAGES, TEXT FILES & AUDIO FILES
    root = 'Books'
    if not os.path.exists(root):
        os.mkdir(root)

    cwd = os.path.join(root, path)
    if not os.path.exists(cwd):
        os.mkdir(cwd)
    imgDir = os.path.join(cwd, 'Files')
    if not os.path.exists(imgDir):
        os.mkdir(imgDir)
    txtDir = os.path.join(cwd, 'Texts')
    if not os.path.exists(txtDir):
        os.mkdir(txtDir)
    return cwd

def images(bn, books):
    # FUNCTION USED TO DOWNLOAD IMAGES AND GET THE RESPECTIVE TEXT DATA FROM FIREBASE
    data = []
    for dataKey in books.val():
        data.append(books.val()[dataKey])

    for i in data:
        ext = getExt(i['type'])
        pg = i['page']
        fn = fileName(pg, ext)

        url = i['image']
        detectedText = i['text']

        cwd = handleIt(bn)

        getFile(url, cwd, fn) # getFile function called to download image files

        txtfilename = str(pg) + '.txt'
        getTxt(detectedText, cwd, txtfilename) # DETECTED TEXT passed to getTxt function
    return True

def pdf(bn):
    # FUNCTION USED TO DOWNLOAD PDFs AND GET THE RESPECTIVE TEXT DATA FROM FIREBASE
    flag = False
    eBooks = []
    for books in pdfRef.each():
        eBooks.append(books)

    for books in eBooks:
        if bn.lower() == books.key():
            flag = True
            break
        else:
            flag = False
    if flag:
        data = []
        for dataKey in books.val():
            data.append(books.val()[dataKey])

        for i in data:
            fn = i['name']

            url = i['pdf']
            detectedText = i['detected-text']

            # detectedText = unicode(detectedText, "utf-8")
            detectedText.encode().decode('utf-8', 'ignore')
            # detectedText = make_unicode(detectedText)

            cwd = handleIt(bn)

            getFile(url, cwd, fn) # getFile function called to download PDF files

            txtfilename = str(getName(fn)) + '.txt'
            getTxt(detectedText, cwd, txtfilename) # DETECTED TEXT passed to getTxt function
            return True
    else:
        print('Book not found!!!')
        return False

def main(bn):
    # MAIN function takes bookname as input
    # it checks if image files exist for a given book
    # or if PDF files exist for a given book
    # accordingly called the image() or pdf() function to get all files and detected text
    # returns a variable, "result" which contains True if files exist and False if they don't
    # an appropriate message is given to the user depending on the value of result returned
    flag = False
    eBooks = []
    result = False
    for books in bookRef.each():
        eBooks.append(books)

    for books in eBooks:
        if bn.lower() == books.key():
            flag = True
            break
        else:
            flag = False
    if flag:
        if images(bn, books):
            result = True
            return result
    else:
        if pdf(bn):
            result = True
            return result
            
    return result
