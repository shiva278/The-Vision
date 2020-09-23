import headers as h
import braille as br
import json
import RPi.GPIO as gp
from shiftr_74HC595 import ShiftRegister
from time import sleep

e = '.txt'
flag = True
while(flag)
    h.vi(1)
    n=""
    for i in range(3):
        n=h.sp()
        if n=="error 1" or "error 2":
            n=""
            continue
        else:
            h.cnfm(n)
        dec=h.decision()
        if dec.lower()=='yes':
            h.cnfm_dlt(n)
            break
        elif dec.lower()=='no':
            h.cnfm_dlt(n)
            h.vi(2)
        else:
            n=""
            continue

    if n == "":
        h.vi(4)
        sys.exit()

    path = h.root + n + '/' + 'text' + '/'
    print(path)

# actual reading starts...
    path = os.path.join('Books', n)
    path = os.path.join(path, 'Texts')
    for root, dirs, files in os.walk(path):
        for filename in files:
            filename = os.path.join(path, filename)
            with open(fname, 'r') as rd:
                text = rd.read()        

# for controlling 1 braille unit (reading 1 character) at a time
    for ch in text :
        op = br.char_to_braille(ch)
        if op == "error":
            pass
        else :
            m = br.matr(op)
            br.drw(m)

            shr.setOutputs(op)
            shr.latch()
            sleep(2)


# for controlling 2 braille units (reading 2 characters) at a time
    ls_chars = []
    for ch in text :
        ls_chars.append(ch)

    start_pos = 0

    for i in range(start_pos, start_pos + 2) :
        tmp = []
        tmp.append(ls_chars[i])
    op = br.char_to_braille(ls_chars[i])
    if op == "error":
        pass
    else :
        m = br.matr(op)
        br.drw(m)

        shr.setOutputs(op)
        shr.latch()
        sleep(2)

# for controlling 4 braille units (reading 4 characters) at a time
    for ch in text :
        op = br.char_to_braille(ch)
        if op == "error":
            pass
        else :
            m = br.matr(op)
            br.drw(m)

            shr.setOutputs(op)          # setOutputs function in shiftr_74HC595 library takes a list
                                        # and define the data to be shifted out
                                        # through serial data input pin( pin 14) connected to the "dat" (pin of pi)
    
            shr.latch()                 # latch function shifts out the data
            sleep(2)
