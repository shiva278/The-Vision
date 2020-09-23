import RPi.GPIO as gp
from shiftr_74HC595 import ShiftRegister
from time import sleep

gp.setmode(gp.BOARD)

dat = 7     # data pin used to send data to shift ragister
lat = 11    # latch pin used to control ST_CP(STORAGE_REGISTER CLOCK INPUT) of the shift register
clk = 12    # clocK pin used to control SH_CP(SHIFT_REGISTER CLOCK INPUT) of the shift register

shr = ShiftRegister(dat, lat, clk)  #init ShiftRegister with the defined pins


# THIS DICTIONARY IS USED TO GIVE AN INTERMEDIATE CODE TO EACH CHARACTER
# THIS IS HELPFUL IN THE CONVERTION OF CHARACTERS INTO BRAILLE CHARACTERS
ch_num = dict({ 'a':32, 'b':48, 'c':36, 'd':38, 'e':34, 'f':52, 'g':54, 'h':50, 'i':20, 'j':22, 'k':40, 'l':56,
                'm':44, 'n':46, 'o':42, 'p':60, 'q':62, 'r':58, 's':28, 't':30, 'u':41, 'v':57, 'w':23, 'x':45, 'y':47,
                'z':43, ' ':0, '#':15, '1':32, '2':48, '3':36, '4':38, '5':34, '6':52, '7':54, '8':50, '9':20, '0':22})


def char_to_braille(ch):
    # FUNCTION WHICH TAKES A CHARACTER
    # AND ENCODES IT INTO A LIST (WHICH LATER WILL BE CONVERTED INTO A 3x2 MATRIX IN BRAILLE FORMAT)
    n = ch_num[ch]
    b = bin(n)
    n2 = b.replace("0b", "")
    ls = []
    for i in n2:
        ls.append(int(i))
    for i in range(2):
        ls.insert(i, 0)
    l = len(ls)
    if l < 8:
        for i in range(8-l) :
            ls.insert(i,0)
    return (ls)

for i in range(3,0,-1):
    print(i,"...")
    sleep(1)
for ch in ch_num :
    print(ch)
    op = char_to_braille(ch)
    shr.setOutputs(op)          # setOutputs function in shiftr_74HC595 library takes a list
                                # and define the data to be shifted out
                                # through serial data input pin( pin 14) connected to the "dat" (pin of pi)
    
    shr.latch()                 # latch function shifts out the data
    sleep(2)