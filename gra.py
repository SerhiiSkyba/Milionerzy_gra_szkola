#importwoanie
from tkinter import *
from Milionerzy import listnum
from Milionerzy import listpyt
from Milionerzy import listodp
from Milionerzy import listodpA
from Milionerzy import listodpB
from Milionerzy import listodpC
from Milionerzy import listodpD
import random
from tkinter import messagebox
#ustawienia, wyglad itp
fnt = ("Times New Roman",13)
bgv= "lightgray"
windowgra = Tk()
windowgra.resizable(False,False)
windowgra.geometry("550x600")
windowgra.title("Gra Milionerzy")
windowgra.config(bg=bgv)
#pierwsze losowanie pytania
numer = random.choice(listnum)
pytanie = listpyt[numer-1]
OdpA = listodpA[numer-1]
OdpB = listodpB[numer-1]
OdpC = listodpC[numer-1]
OdpD = listodpD[numer-1]
OdpP = listodp[numer-1]
listnum.remove(numer)




#funkcja
def sprawdzenie(x):  #sprawdzenie wybranej odpowiedzi
    global PodpVar
    global Gowna
    aodp = 0
    bodp = 0
    codp = 0
    dodp = 0
    if PodpVar == 11:
        aodp = 1
    elif PodpVar == 12:
        bodp = 1
    elif PodpVar == 13:
        codp = 1
    elif PodpVar == 14:
        dodp = 1
        
    
    if x == 1:
        spr = aodp
    elif x == 2:
        spr = bodp
    elif x == 3:
        spr = codp
    elif x == 4:
        spr = dodp
        
    if Gowna.get() >= 2 and Gowna.get() < 7:
        kasagw.set(1000)
        kasaV.set("Otrzymujesz gwarantowane "+kasagw+"zł")
    elif Gowna.get() >= 7 and Gowna.get() < 13:
        kasagw.set(40000)
        kasaV.set("Otrzymujesz gwarantowane "+kasagw+"zł")
    elif Gowna.get() == 13:
        kasagw.set(1000000)
        kasaV.set("Otrzymujesz gwarantowane "+kasagw+"zł")
    
    if spr == 1:
        try:
            wynik.set("Poprawna odpowiedz")
            Gowna.set(Gowna.get()+1)
            numer = random.choice(listnum)
            pytanie = listpyt[numer-1]
            OdpA = listodpA[numer-1]
            OdpB = listodpB[numer-1]
            OdpC = listodpC[numer-1]
            OdpD = listodpD[numer-1]
            OdpP = listodp[numer-1]
            pytanieVar.set(pytanie)
            AodpVar.set(OdpA)
            BodpVar.set(OdpB)
            CodpVar.set(OdpC)
            DodpVar.set(OdpD)
            PodpVar = int(OdpP)
            listnum.remove(numer)
            c.set(str(Gowna.get())+"/12")
        except:
            messagebox.showinfo(title='Udało się', message='Wygrałeś')
            windowgra.destroy()
    else:
        wynik.set("Niepoprawna odpowiedz")
        numer = random.choice(listnum)
        pytanie = listpyt[numer-1]
        OdpA = listodpA[numer-1]
        OdpB = listodpB[numer-1]
        OdpC = listodpC[numer-1]
        OdpD = listodpD[numer-1]
        OdpP = listodp[numer-1]
        pytanieVar.set(pytanie)
        AodpVar.set(OdpA)
        BodpVar.set(OdpB)
        CodpVar.set(OdpC)
        DodpVar.set(OdpD)
        PodpVar = int(OdpP)
        listnum.remove(numer)
        mesasge = messagebox.showinfo(title="O nie", message="Przegrałeś")
        windowgra.destroy()
        
        
        
        

#zmienne
pytanieVar = StringVar()

PodpVar = IntVar()  #poprawna odpowiedz
PodpVar = int(OdpP)
#11 = A, 12 = B, 13 = C, 14 = D

AodpVar = StringVar()  #odpowiedz a
AodpVar.set(OdpA)

BodpVar = StringVar()  #odpowiedz b
BodpVar.set(OdpB)

CodpVar = StringVar()  #odpowiedz c
CodpVar.set(OdpC)

DodpVar = StringVar()  #odpowiedz d
DodpVar.set(OdpD)

wynik  = StringVar()  #wynik (poprawne/niepoprawne)
wynik.set("Tu wyswietli sie poprawnosc odpowiedzi")

Gowna = IntVar()  #punkty
c = StringVar()  #punkty na wyswietleniu
c.set(str(Gowna.get())+"/12")

kasagw = IntVar()
kasaV = StringVar()
kasaV.set("Otrzymujesz gwarantowane "+str(kasagw.get())+"zł")

#labele etc
pytanieL = Label(windowgra,textvariable=pytanieVar,font=fnt,width=60,height=5,bg=bgv)
pytanieVar.set(pytanie)
wynikL = Label(windowgra,textvariable=wynik,font=fnt,bg=bgv,width=60,height=5)
gownol = Label(windowgra, textvariable=c,font=fnt,bg=bgv)
kasa = Label(windowgra,textvariable=kasaV)

#odpowiedzi
AOdpbtn = Button(windowgra,textvariable=AodpVar,font=fnt,bg=bgv,command=lambda: sprawdzenie(1), width=30,height=3)
BOdpbtn = Button(windowgra,textvariable=BodpVar,font=fnt,bg=bgv,command=lambda: sprawdzenie(2),width=30,height=3)
COdpbtn = Button(windowgra,textvariable=CodpVar,font=fnt,bg=bgv,command=lambda: sprawdzenie(3),width=30,height=3)
DOdpbtn = Button(windowgra,textvariable=DodpVar,font=fnt,bg=bgv,command=lambda: sprawdzenie(4),width=30,height=3)

#gridy
pytanieL.grid(row=1,column=2,columnspan=3)
wynikL.grid(row=5,column=2,columnspan=3)
AOdpbtn.grid(row=2,column=1,columnspan=2)
BOdpbtn.grid(row=2,column=3,columnspan=2)
COdpbtn.grid(row=4,column=1,columnspan=2)
DOdpbtn.grid(row=4,column=3,columnspan=2)
gownol.grid(row=6,column=2,columnspan=3)
kasa.grid(row=7,column=2,columnspan=3)

windowgra.mainloop()