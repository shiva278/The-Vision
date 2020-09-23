
# THIS DICTIONARY IS USED TO GIVE AN INTERMEDIATE CODE TO EACH CHARACTER
# THIS IS HELPFUL IN THE CONVERTION OF CHARACTERS INTO BRAILLE CHARACTERS
ch_num = dict({ 'a':32, 'b':48, 'c':36, 'd':38, 'e':34, 'f':52, 'g':54, 'h':50, 'i':20, 'j':22, 'k':40, 'l':56,
                'm':44, 'n':46, 'o':42, 'p':60, 'q':62, 'r':58, 's':28, 't':30, 'u':41, 'v':57, 'w':23, 'x':45, 'y':47,
                'z':43, ' ':0, '#':15, '1':32, '2':48, '3':36, '4':38, '5':34, '6':52, '7':54, '8':50, '9':20, '0':22})


def char_to_braille(ch):
    # FUNCTION WHICH TAKES A CHARACTER
    # AND ENCODES IT INTO A LIST (WHICH LATER WILL BE CONVERTED INTO A 3x2 MATRIX IN BRAILLE FORMAT)
    if ch in ch_num.keys():
        n   =   ch_num[ch]
        b   =   bin(n)
        n2  =   b.replace("0b", "")
        ls = []
        for i in n2:
            ls.append(int(i))
        if len(ls)<6:
            l = 6 - len(ls)
            for i in range(l):
                ls.insert(0, 0)
        return (ls)
    else :
        print("char not available!!!")
        return "error"

def matr(ls):
    # FUNCTION THAT TAKES THE LIST
    # AND CONVERTS IT INTO A 3x2 MATRIX OF 1's and 0's IN BRAILLE FORMAT WHICH REPRESENTS A BRAILLE CHARACTER
    ls1=[]
    ls2=[]
    res = []
    tmp = []
    for i in range(0,3):
        ls1.append(ls[i])
    for i in range(3,6):
        ls2.append(ls[i])
    for i in range(3):
        tmp=[]
        tmp.append(ls1[i])
        tmp.append(ls2[i])
        res.append(tmp)
    #print(res)
    return res

def drw(ls):
    # FUNCTION TO DRAW THE MATRIX
    for i in range(3):
        for j in range(2):
            print(ls[i][j], " ", end="")
        print()

while(True):
    text = input('enter text :')
    for ch in text:
        op = char_to_braille(ch)
        m = matr(op)
        print(m)
        drw(m)
