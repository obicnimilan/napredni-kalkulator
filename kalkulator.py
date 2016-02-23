import math
import sys

operacije = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]

def sestevanje (x, y):
    return (x + y);
def odstevanje (x, y):
    return (x - y);
def mnozenje (x, y):
    return (x * y);
def deljenje (x, y):
    return (x / y)
def potenciranje (x, y):
    return (x ** y)
def korenjenje (x, y):
    return (x ** (1/y))
def sinus (x):
    return (math.sin(x))
def cosinus (x):
    return (math.cos(x))
def tangens (x):
    return (math.tan(x))
def asinus (x):
    return (math.asin(x))
def acosinus (x):
    return (math.acos(x))
def atangens (x):
    return (math.atan(x))
def sr (x):
    return ((x/360) *2*math.pi)
def rs (x):
    return ((x/(2*math.pi)) * 360)
def nl (x):
    return (math.log(x))
def dl (x):
    return (math.log10(x))

def vnos():
    while True:
        try:
            number = float(raw_input("Stevilo: "))
            break
        except ValueError:
            print("Error")
    return number


def operacija():
    while True:
        operacija = raw_input("Katero operacijo bi zeleli (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17)? ")
        if operacija in operacije:
            break
        else:
            print("Ta operacija ni na izbiro.")
    return operacija;

def ponovi():
    while True:
        again = raw_input("Znova? Da/Ne: ").lower()
        if again == "da":
            return True
        elif again == "ne":
            print ("____________________________________________________________________________________________________________________________________________")
            print ("____________________________________________________________________________________________________________________________________________")
            print ("Nasvidenje!")
            sys.exit(0)
        else:
            print("Error!")

while True:
    print ("Pozdravljeni v KALKULATORJU!")
    print ("____________________________________________________________________________________________________________________________________________")
    print ("____________________________________________________________________________________________________________________________________________")
    print ("____________________________________________________________________________________________________________________________________________")
    print ("____________________________________________________________________________________________________________________________________________")
    print ("Lahko izbirate med naslednjimi funkcijami: ")
    print ("1. Mnozenje")
    print ("2. Deljenje")
    print ("3. Sestevanje")
    print ("4. Odstevanje")
    print ("5. Potenciranje")
    print ("6. Korenjenje")
    print ("7. Kvadratna enacba")
    print ("Kotne funkcije:")
    print ("    8. Sinus")
    print ("    9. Cosinus")
    print ("    10. Tangens")
    print ("    Inverzne funkcije:")
    print ("        11. Sinus")
    print ("        12. Cosinus")
    print ("        13. Tangens")
    print ("Pretvorba:")
    print ("    14. Stopinj v Radiane")
    print ("    15. Radianov v Stopinje")
    print ("Logaritem:")
    print ("    16. Naravni")
    print ("    17. Desetiski")

    nacin = operacija()
    if nacin == "1":
        s1 = vnos()
        s2 = vnos()
        print (mnozenje(s1,s2))
    elif nacin == "3":
        s1 = vnos()
        s2 = vnos()
        print (sestevanje(s1,s2))
    elif nacin == "4":
        s1 = vnos()
        s2 = vnos()
        print (odstevanje(s1,s2))
    elif nacin == "2":
        s1 = vnos()
        s2 = vnos()
        print (deljenje(s1,s2))
    elif nacin == "5":
        s1 = vnos()
        s2 = vnos()
        print (potenciranje(s1, s2))
    elif nacin == "6":
        s1 = float(raw_input("Vnesite stevilo, ki ga bi radi korenili:"))
        s2 = float(raw_input("Vnesite stopnjo korena:"))
        print (korenjenje(s1,s2))
    elif nacin == "7":
        a = float(raw_input("Vnesi a koeficient:"))
        b = float(raw_input("Vnesi b koeficient:"))
        c = float(raw_input("Vnesi c koeficient:"))
        d = float(b**2-4*a*c)
        if d < 0:
            print ("Enacba nima realnih resitev")
        elif d == 0:
            x = (-b)/(2*a)
            print ("Enačba ima eno rešitev:")
            print (x)
        else:
            r1 = float((-b+math.sqrt(b**2-4*a*c))/(2*a))
            r2 = float((-b-math.sqrt(b**2-4*a*c))/(2*a))
            print ("Enacba ima dve resitvi:")
            print (r1)
            print (r2)
    elif nacin == "8":
        a = float(raw_input("Izberi kot:"))
        print (sinus(a))
    elif nacin == "9":
        a = float(raw_input("Izberi kot:"))
        print (cosinus(a))
    elif nacin == "10":
        a = float(raw_input("Izberi kot:"))
        print (tangens(a))
    elif nacin == "11":
        a = float(raw_input("Vnesi razmerje:"))
        print (asinus(a))
    elif nacin == "12":
        a = float(raw_input("Vnesi razmerje:"))
        print (acosinus(a))
    elif nacin == "13":
        a = float(raw_input("Vnesi razmerje:"))
        print (atangens(a))
    elif nacin == "14":
        a = float(raw_input("Vnesi stevilo stopinj:"))
        print ("Je toliko radianov:")
        print (sr(a))
    elif nacin == "15":
        a = float(raw_input("Vnesi stevilo radianov:"))
        print ("Je toliko stopinj:")
        print (sr(a))
    elif nacin == "16":
        a = vnos()
        print (nl(a))
    elif nacin == "17":
        a = vnos()
        print (dl(a))

    ponovi()

