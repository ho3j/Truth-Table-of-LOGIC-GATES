"""
HOSSEIN JALILI
#HO3J
Truth Table of LOGIC GATES IN PYTHON (2 /3 /4 inputs)
main.py
mehr 1400
ver 1.0
"""
################import###############
import Truth_Table as tt
import os

################lambda###############
clear=lambda : os.system("cls")

################main###############
clear()
while True:
    try:
        print("""
        Truth Table of LOGIC GATES
        |*************************|
        |   1 : \t AND      |
        |   2 : \t NAND     |
        |   3 : \t OR       |
        |   4 : \t NOR      |
        |   5 : \t XOR      |
        |   6 : \t XNOR     |
        |   7 : \t NOT      |
        |   8 : \t quit     |
        ***************************
        """)
        i=int(input("Enter number of LOGIC GATES :\t"))
        if i ==1:
            tt._and2()
            tt._and3()
            tt._and4()
        elif i==2:
            tt._nand2()
            tt._nand3()
            tt._nand4()
        elif i==3:
            tt._or2()
            tt._or3()
            tt._or4()
        elif i==4:
            tt._nor2()
            tt._nor3()
            tt._nor4() 
        elif i==5:
            tt._xor2()
            tt._xor3()
            tt._xor4() 
        elif i==6:
            tt._xnor2()
            tt._xnor3()
            tt._xnor4() 
        elif i==7 :
            tt._not()
        elif i==8:
            break
        else :
            clear()
            print("wrong  number !!! " ,end="\n \n")
            print( end=" ")
            qq = input("Enter 'Q' to quit app \n or 'Enter' to continue : \t ").lower()
            if qq =="q" :
                break
            else :
                clear()
                continue
    except:
        clear()
        print("Enter number !")

