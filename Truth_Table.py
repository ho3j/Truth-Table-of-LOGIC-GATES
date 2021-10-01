"""
HOSSEIN JALILI
#HO3J
Truth Table of LOGIC GATES IN PYTHON (2 /3 /4 inputs)
Truth_Table.py
mehr 1400
ver 1.0
"""
################import###############
import os

################operation###############
clear=lambda : os.system("cls")

def AND2 (a, b):
    return (a & b)

def AND3 (a, b, c):
    return (a & b & c)
 
def AND4 (a, b, c, d):
    return (a & b & c & d)
 
 
def NAND2 (a, b):
    return not (a & b)

def NAND3 (a, b, c):
    return not (a & b & c)
 
def NAND4 (a, b, c, d):
    return not (a & b & c & d)
 

def OR2 (a, b):
    return (a | b)

def OR3 (a, b, c):
    return (a | b | c)
 
def OR4 (a, b, c, d):
    return (a | b | c| d)
 

def XOR2 (a, b):
    return (a ^ b)

def XOR3(a, b, c):
    return (a ^ b ^ c)

def XOR4(a, b, c, d):
    return (a ^ b ^ c ^ d)


def NOR2 (a, b):
    return not (a | b)

def NOR3 (a, b, c):
    return not (a | b | c)
 
def NOR4 (a, b, c, d):
    return not (a | b | c| d)
 

def XNOR2 (a, b):
    return not (a ^ b)

def XNOR3(a, b, c):
    return not (a ^ b ^ c)

def XNOR4(a, b, c, d):
    return not (a ^ b ^ c ^ d)

def NOT(a):
    return not a



###############Truth Table###############

def _not():
    clear()
    print("\n+----  NOT Truth Table------+")
    print("_________________")
    print("| a    |   NOT   | ")
    print("|______|_________|")
    print("|False | ",NOT(False),"  | ")
    print("|True  | ",NOT(True)," | ")
    print("|______|_________|")
    print("+-------------------------------------+\n")

    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()


def _and2():
    clear()
    print("\n+---- (2 input) AND Truth Table------+")
    print("_________________________")
    print("| a    | b     |   AND   | ")
    print("|______|_______|_________|")
    print("|False | False | ",AND2(False,False)," | ")
    print("|False | True  | ",AND2(False,True)," | ")
    print("|True  | False | ",AND2(True,False)," | ")
    print("|True  | True  | ",AND2(True,True),"  | ")
    print("|______|_______|_________|")
    print("+-------------------------------------+\n")

def _and3():
    print("\n+---- (3 input) AND Truth Table------+")
    print("_________________________________")
    print("| a    | b     | c     |   AND   | ")
    print("|______|_______|_______|_________|")
    print("|False | False | False | ",AND3(False,False,False)," | ")
    print("|False | False | True  | ",AND3(False,False,True)," | ")
    print("|False | True  | False | ",AND3(False,True,False)," | ")
    print("|False | True  | True  | ",AND3(False,True,True)," | ")
    print("|True  | False | False | ",AND3(True,False,False)," | ")
    print("|True  | False | True  | ",AND3(True,False,True)," | ")
    print("|True  | True  | False | ",AND3(True,True,False)," | ")
    print("|True  | True  | True  | ",AND3(True,True,True),"  | ")
    print("|______|_______|_______|_________|")
    print("+-------------------------------------+\n")

def _and4():
    print("\n+---- (4 input) AND Truth Table------+")
    print("_________________________________________")
    print("| a    | b     | c     | d     |   AND   |")
    print("|______|_______|_______|_______|_________|")
    print("|False | False | False | False | ",AND4(False,False,False,False)," | ")
    print("|False | False | False | True  | ",AND4(False,False,False,True)," | ")
    print("|False | False | True  | False | ",AND4(False,False,True,False)," | ")
    print("|False | False | True  | True  | ",AND4(False,False,True,True)," | ")
    print("|False | True  | False | False | ",AND4(False,True,False,False)," | ")
    print("|False | True  | False | True  | ",AND4(False,True,False,True)," | ")
    print("|False | True  | True  | False | ",AND4(False,True,True,False)," | ")
    print("|False | True  | True  | True  | ",AND4(False,True,True,True)," | ")
    print("|True  | False | False | False | ",AND4(True,False,False,False)," | ")
    print("|True  | False | False | True  | ",AND4(True,False,False,True)," | ")
    print("|True  | False | True  | False | ",AND4(True,False,True,False)," | ")
    print("|True  | False | True  | True  | ",AND4(True,False,True,True)," | ")
    print("|True  | True  | False | False | ",AND4(True,True,False,False)," | ")
    print("|True  | True  | False | True  | ",AND4(True,True,False,True)," | ")
    print("|True  | True  | True  | False | ",AND4(True,True,True,False)," | ")
    print("|True  | True  | True  | True  | ",AND4(True,True,True,True),"  | ")
    print("|______|_______|_______|_______|_________|")
    print("+-------------------------------------+\n")

    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()


def _nand2():
    clear()
    print("\n+---- (2 input) NAND Truth Table------+")
    print("_________________________")
    print("| a    | b     |   NAND  | ")
    print("|______|_______|_________|")
    print("|False | False | ",NAND2(False,False),"  | ")
    print("|False | True  | ",NAND2(False,True),"  | ")
    print("|True  | False | ",NAND2(True,False),"  | ")
    print("|True  | True  | ",NAND2(True,True)," | ")
    print("|______|_______|_________|")
    print("+-------------------------------------+\n")

def _nand3():
    print("\n+---- (3 input) NAND Truth Table------+")
    print("_________________________________")
    print("| a    | b     | c     |   NAND  | ")
    print("|______|_______|_______|_________|")
    print("|False | False | False | ",NAND3(False,False,False),"  | ")
    print("|False | False | True  | ",NAND3(False,False,True),"  | ")
    print("|False | True  | False | ",NAND3(False,True,False),"  | ")
    print("|False | True  | True  | ",NAND3(False,True,True),"  | ")
    print("|True  | False | False | ",NAND3(True,False,False),"  | ")
    print("|True  | False | True  | ",NAND3(True,False,True),"  | ")
    print("|True  | True  | False | ",NAND3(True,True,False),"  | ")
    print("|True  | True  | True  | ",NAND3(True,True,True)," | ")
    print("|______|_______|_______|_________|")
    print("+-------------------------------------+\n")

def _nand4():
    print("\n+---- (4 input) NAND Truth Table------+")
    print("_________________________________________")
    print("| a    | b     | c     | d     |   NAND  |")
    print("|______|_______|_______|_______|_________|")
    print("|False | False | False | False | ",NAND4(False,False,False,False),"  | ")
    print("|False | False | False | True  | ",NAND4(False,False,False,True),"  | ")
    print("|False | False | True  | False | ",NAND4(False,False,True,False),"  | ")
    print("|False | False | True  | True  | ",NAND4(False,False,True,True),"  | ")
    print("|False | True  | False | False | ",NAND4(False,True,False,False),"  | ")
    print("|False | True  | False | True  | ",NAND4(False,True,False,True),"  | ")
    print("|False | True  | True  | False | ",NAND4(False,True,True,False),"  | ")
    print("|False | True  | True  | True  | ",NAND4(False,True,True,True),"  | ")
    print("|True  | False | False | False | ",NAND4(True,False,False,False),"  | ")
    print("|True  | False | False | True  | ",NAND4(True,False,False,True),"  | ")
    print("|True  | False | True  | False | ",NAND4(True,False,True,False),"  | ")
    print("|True  | False | True  | True  | ",NAND4(True,False,True,True),"  | ")
    print("|True  | True  | False | False | ",NAND4(True,True,False,False),"  | ")
    print("|True  | True  | False | True  | ",NAND4(True,True,False,True),"  | ")
    print("|True  | True  | True  | False | ",NAND4(True,True,True,False),"  | ")
    print("|True  | True  | True  | True  | ",NAND4(True,True,True,True)," | ")
    print("|______|_______|_______|_______|_________|")
    print("+-------------------------------------+\n")

    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()


def _or2():
    clear()
    print("\n+---- (2 input) OR Truth Table------+")
    print("_________________________")
    print("| a    | b     |   OR    | ")
    print("|______|_______|_________|")
    print("|False | False | ",OR2(False,False)," | ")
    print("|False | True  | ",OR2(False,True),"  | ")
    print("|True  | False | ",OR2(True,False),"  | ")
    print("|True  | True  | ",OR2(True,True),"  | ")
    print("|______|_______|_________|")
    print("+-------------------------------------+\n")

def _or3():
    print("\n+---- (3 input) OR Truth Table------+")
    print("_________________________________")
    print("| a    | b     | c     |   OR    | ")
    print("|______|_______|_______|_________|")
    print("|False | False | False | ",OR3(False,False,False)," | ")
    print("|False | False | True  | ",OR3(False,False,True),"  | ")
    print("|False | True  | False | ",OR3(False,True,False),"  | ")
    print("|False | True  | True  | ",OR3(False,True,True),"  | ")
    print("|True  | False | False | ",OR3(True,False,False),"  | ")
    print("|True  | False | True  | ",OR3(True,False,True),"  | ")
    print("|True  | True  | False | ",OR3(True,True,False),"  | ")
    print("|True  | True  | True  | ",OR3(True,True,True),"  | ")
    print("|______|_______|_______|_________|")
    print("+-------------------------------------+\n")

def _or4():
    print("\n+---- (4 input) OR Truth Table------+")
    print("_________________________________________")
    print("| a    | b     | c     | d     |   OR    |")
    print("|______|_______|_______|_______|_________|")
    print("|False | False | False | False | ",OR4(False,False,False,False)," | ")
    print("|False | False | False | True  | ",OR4(False,False,False,True),"  | ")
    print("|False | False | True  | False | ",OR4(False,False,True,False),"  | ")
    print("|False | False | True  | True  | ",OR4(False,False,True,True),"  | ")
    print("|False | True  | False | False | ",OR4(False,True,False,False),"  | ")
    print("|False | True  | False | True  | ",OR4(False,True,False,True),"  | ")
    print("|False | True  | True  | False | ",OR4(False,True,True,False),"  | ")
    print("|False | True  | True  | True  | ",OR4(False,True,True,True),"  | ")
    print("|True  | False | False | False | ",OR4(True,False,False,False),"  | ")
    print("|True  | False | False | True  | ",OR4(True,False,False,True),"  | ")
    print("|True  | False | True  | False | ",OR4(True,False,True,False),"  | ")
    print("|True  | False | True  | True  | ",OR4(True,False,True,True),"  | ")
    print("|True  | True  | False | False | ",OR4(True,True,False,False),"  | ")
    print("|True  | True  | False | True  | ",OR4(True,True,False,True),"  | ")
    print("|True  | True  | True  | False | ",OR4(True,True,True,False),"  | ")
    print("|True  | True  | True  | True  | ",OR4(True,True,True,True),"  | ")
    print("|______|_______|_______|_______|_________|")
    print("+-------------------------------------+\n")

    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()


def _xor2():
    clear()
    print("\n+---- (2 input) XOR Truth Table------+")
    print("_________________________")
    print("| a    | b     |   XOR   | ")
    print("|______|_______|_________|")
    print("|False | False | ",XOR2(False,False)," | ")
    print("|False | True  | ",XOR2(False,True),"  | ")
    print("|True  | False | ",XOR2(True,False),"  | ")
    print("|True  | True  | ",XOR2(True,True)," | ")
    print("|______|_______|_________|")
    print("+-------------------------------------+\n")

def _xor3():
    print("\n+---- (3 input) XOR Truth Table------+")
    print("_________________________________")
    print("| a    | b     | c     |   XOR   | ")
    print("|______|_______|_______|_________|")
    print("|False | False | False | ",XOR3(False,False,False)," | ")
    print("|False | False | True  | ",XOR3(False,False,True),"  | ")
    print("|False | True  | False | ",XOR3(False,True,False),"  | ")
    print("|False | True  | True  | ",XOR3(False,True,True)," | ")
    print("|True  | False | False | ",XOR3(True,False,False),"  | ")
    print("|True  | False | True  | ",XOR3(True,False,True)," | ")
    print("|True  | True  | False | ",XOR3(True,True,False)," | ")
    print("|True  | True  | True  | ",XOR3(True,True,True),"  | ")
    print("|______|_______|_______|_________|")
    print("+-------------------------------------+\n")

def _xor4():
    print("\n+---- (4 input) XOR Truth Table------+")
    print("_________________________________________")
    print("| a    | b     | c     | d     |   XOR   |")
    print("|______|_______|_______|_______|_________|")
    print("|False | False | False | False | ",XOR4(False,False,False,False)," | ")
    print("|False | False | False | True  | ",XOR4(False,False,False,True),"  | ")
    print("|False | False | True  | False | ",XOR4(False,False,True,False),"  | ")
    print("|False | False | True  | True  | ",XOR4(False,False,True,True)," | ")
    print("|False | True  | False | False | ",XOR4(False,True,False,False),"  | ")
    print("|False | True  | False | True  | ",XOR4(False,True,False,True)," | ")
    print("|False | True  | True  | False | ",XOR4(False,True,True,False)," | ")
    print("|False | True  | True  | True  | ",XOR4(False,True,True,True),"  | ")
    print("|True  | False | False | False | ",XOR4(True,False,False,False),"  | ")
    print("|True  | False | False | True  | ",XOR4(True,False,False,True)," | ")
    print("|True  | False | True  | False | ",XOR4(True,False,True,False)," | ")
    print("|True  | False | True  | True  | ",XOR4(True,False,True,True),"  | ")
    print("|True  | True  | False | False | ",XOR4(True,True,False,False)," | ")
    print("|True  | True  | False | True  | ",XOR4(True,True,False,True),"  | ")
    print("|True  | True  | True  | False | ",XOR4(True,True,True,False),"  | ")
    print("|True  | True  | True  | True  | ",XOR4(True,True,True,True)," | ")
    print("|______|_______|_______|_______|_________|")
    print("+-------------------------------------+\n")

    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()


def _nor2():
    clear()
    print("\n+---- (2 input) NOR Truth Table------+")
    print("_________________________")
    print("| a    | b     |   NOR   | ")
    print("|______|_______|_________|")
    print("|False | False | ",NOR2(False,False),"  | ")
    print("|False | True  | ",NOR2(False,True)," | ")
    print("|True  | False | ",NOR2(True,False)," | ")
    print("|True  | True  | ",NOR2(True,True)," | ")
    print("|______|_______|_________|")
    print("+-------------------------------------+\n")

def _nor3():
    print("\n+---- (3 input) NOR Truth Table------+")
    print("_________________________________")
    print("| a    | b     | c     |   NOR   | ")
    print("|______|_______|_______|_________|")
    print("|False | False | False | ",NOR3(False,False,False),"  | ")
    print("|False | False | True  | ",NOR3(False,False,True)," | ")
    print("|False | True  | False | ",NOR3(False,True,False)," | ")
    print("|False | True  | True  | ",NOR3(False,True,True)," | ")
    print("|True  | False | False | ",NOR3(True,False,False)," | ")
    print("|True  | False | True  | ",NOR3(True,False,True)," | ")
    print("|True  | True  | False | ",NOR3(True,True,False)," | ")
    print("|True  | True  | True  | ",NOR3(True,True,True)," | ")
    print("|______|_______|_______|_________|")
    print("+-------------------------------------+\n")

def _nor4():
    print("\n+---- (4 input) NOR Truth Table------+")
    print("_________________________________________")
    print("| a    | b     | c     | d     |   NOR   |")
    print("|______|_______|_______|_______|_________|")
    print("|False | False | False | False | ",NOR4(False,False,False,False),"  | ")
    print("|False | False | False | True  | ",NOR4(False,False,False,True)," | ")
    print("|False | False | True  | False | ",NOR4(False,False,True,False)," | ")
    print("|False | False | True  | True  | ",NOR4(False,False,True,True)," | ")
    print("|False | True  | False | False | ",NOR4(False,True,False,False)," | ")
    print("|False | True  | False | True  | ",NOR4(False,True,False,True)," | ")
    print("|False | True  | True  | False | ",NOR4(False,True,True,False)," | ")
    print("|False | True  | True  | True  | ",NOR4(False,True,True,True)," | ")
    print("|True  | False | False | False | ",NOR4(True,False,False,False)," | ")
    print("|True  | False | False | True  | ",NOR4(True,False,False,True)," | ")
    print("|True  | False | True  | False | ",NOR4(True,False,True,False)," | ")
    print("|True  | False | True  | True  | ",NOR4(True,False,True,True)," | ")
    print("|True  | True  | False | False | ",NOR4(True,True,False,False)," | ")
    print("|True  | True  | False | True  | ",NOR4(True,True,False,True)," | ")
    print("|True  | True  | True  | False | ",NOR4(True,True,True,False)," | ")
    print("|True  | True  | True  | True  | ",NOR4(True,True,True,True)," | ")
    print("|______|_______|_______|_______|_________|")
    print("+-------------------------------------+\n")

    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()


def _xnor2():
    clear()
    print("\n+---- (2 input) XNOR Truth Table------+")
    print("_________________________")
    print("| a    | b     |   XNOR  | ")
    print("|______|_______|_________|")
    print("|False | False | ",XNOR2(False,False),"  | ")
    print("|False | True  | ",XNOR2(False,True)," | ")
    print("|True  | False | ",XNOR2(True,False)," | ")
    print("|True  | True  | ",XNOR2(True,True),"  | ")
    print("|______|_______|_________|")
    print("+-------------------------------------+\n")

def _xnor3():
    print("\n+---- (3 input) XNOR Truth Table------+")
    print("_________________________________")
    print("| a    | b     | c     |   XNOR  | ")
    print("|______|_______|_______|_________|")
    print("|False | False | False | ",XNOR3(False,False,False),"  | ")
    print("|False | False | True  | ",XNOR3(False,False,True)," | ")
    print("|False | True  | False | ",XNOR3(False,True,False)," | ")
    print("|False | True  | True  | ",XNOR3(False,True,True),"  | ")
    print("|True  | False | False | ",XNOR3(True,False,False)," | ")
    print("|True  | False | True  | ",XNOR3(True,False,True),"  | ")
    print("|True  | True  | False | ",XNOR3(True,True,False),"  | ")
    print("|True  | True  | True  | ",XNOR3(True,True,True)," | ")
    print("|______|_______|_______|_________|")
    print("+-------------------------------------+\n")

def _xnor4():
    print("\n+---- (4 input) XNOR Truth Table------+")
    print("_________________________________________")
    print("| a    | b     | c     | d     |   XNOR  |")
    print("|______|_______|_______|_______|_________|")
    print("|False | False | False | False | ",XNOR4(False,False,False,False),"  | ")
    print("|False | False | False | True  | ",XNOR4(False,False,False,True)," | ")
    print("|False | False | True  | False | ",XNOR4(False,False,True,False)," | ")
    print("|False | False | True  | True  | ",XNOR4(False,False,True,True),"  | ")
    print("|False | True  | False | False | ",XNOR4(False,True,False,False)," | ")
    print("|False | True  | False | True  | ",XNOR4(False,True,False,True),"  | ")
    print("|False | True  | True  | False | ",XNOR4(False,True,True,False),"  | ")
    print("|False | True  | True  | True  | ",XNOR4(False,True,True,True)," | ")
    print("|True  | False | False | False | ",XNOR4(True,False,False,False)," | ")
    print("|True  | False | False | True  | ",XNOR4(True,False,False,True),"  | ")
    print("|True  | False | True  | False | ",XNOR4(True,False,True,False),"  | ")
    print("|True  | False | True  | True  | ",XNOR4(True,False,True,True)," | ")
    print("|True  | True  | False | False | ",XNOR4(True,True,False,False),"  | ")
    print("|True  | True  | False | True  | ",XNOR4(True,True,False,True)," | ")
    print("|True  | True  | True  | False | ",XNOR4(True,True,True,False)," | ")
    print("|True  | True  | True  | True  | ",XNOR4(True,True,True,True),"  | ")
    print("|______|_______|_______|_______|_________|")
    print("+-------------------------------------+\n")

    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()




