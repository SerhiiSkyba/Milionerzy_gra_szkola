#importowanie
from tkinter import *
import customtkinter as ctk
from Baza_danych import listnum
from Baza_danych import listpyt
from Baza_danych import listodp
from Baza_danych import listodpA
from Baza_danych import listodpB
from Baza_danych import listodpC
from Baza_danych import listodpD
import random
from tkinter import messagebox

#ustawienia, wyglad itp
font_default = ("Inter",16,'normal')
font_pytanie = ("Inter",16,'bold')
bg= "#ffffff"
font_color='#121212'
width=25
height=1
windowgra = ctk.CTk(fg_color=bg)
windowgra.resizable(False,False)
windowgra.geometry("560x500")
windowgra.title("Gra Milionerzy")

#losowanie pierwszego pytania
numer = random.choice(listnum)
pytanie = listpyt[numer-1]
OdpA = listodpA[numer-1]
OdpB = listodpB[numer-1]
OdpC = listodpC[numer-1]
OdpD = listodpD[numer-1]
OdpP = listodp[numer-1]
listnum.remove(numer)




#funkcje
def sprawdzenie(x):  #sprawdzenie wybranej odpowiedzi
    global PodpVar
    global Gowna
    global kolav
    aodp = 0
    bodp = 0
    codp = 0
    dodp = 0
    if Gowna.get() == int(12):
        messagebox.showinfo(title='Udało się', message='Wygrałeś milion złotych!')
        windowgra.destroy()
    kolav.set("")
    AOdpbtn.configure(state=NORMAL)
    BOdpbtn.configure(state=NORMAL)
    COdpbtn.configure(state=NORMAL)
    DOdpbtn.configure(state=NORMAL)

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
        kasaV.set("Otrzymujesz gwarantowane "+str(kasagw.get())+"zł")
    elif Gowna.get() >= 7 and Gowna.get() < 13:
        kasagw.set(40000)
        kasaV.set("Otrzymujesz gwarantowane "+str(kasagw.get())+"zł")
    elif Gowna.get() == 13:
        kasagw.set(1000000)
        kasaV.set("Otrzymujesz gwarantowane "+str(kasagw.get())+"zł")
    
    if spr == 1:
        try:
            wynik.set("Poprawna odpowiedz")
            Gowna.set(Gowna.get()+1)
            numer = random.choice(listnum)
            pytanie = listpyt[numer-1]
            OdpA = "A: "+listodpA[numer-1]
            OdpB = "B: "+listodpB[numer-1]
            OdpC = "C: "+listodpC[numer-1]
            OdpD = "D: "+listodpD[numer-1]
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
            messagebox.showinfo(title='Udało się', message='Wygrałeś milion złotych!')
            windowgra.destroy()
    else:
        wynik.set("Niepoprawna odpowiedz")
        numer = random.choice(listnum)
        pytanie = listpyt[numer-1]
        OdpA = "A: "+listodpA[numer-1]
        OdpB = "B: "+listodpB[numer-1]
        OdpC = "C: "+listodpC[numer-1]
        OdpD = "D: "+listodpD[numer-1]
        OdpP = listodp[numer-1]
        pytanieVar.set(pytanie)
        AodpVar.set(OdpA)
        BodpVar.set(OdpB)
        CodpVar.set(OdpC)
        DodpVar.set(OdpD)
        PodpVar = int(OdpP)
        listnum.remove(numer)
        if kasagw.get() == 0:
               mesasge = messagebox.showinfo(title="O nie", message="Przegrałeś")
        else:
            mesasge = messagebox.showinfo(title="O nie", message="Przegrałeś, ale wracasz do domu z "+str(kasagw.get())+'zł')

        windowgra.destroy()

def kolo1():   #kolo ratunkowe 50/50
    fiftyfifty.configure(state=DISABLED)
    aodp = 0
    bodp = 0
    codp = 0
    dodp = 0
    
    if PodpVar == 11:
        aodp = 1
        BOdpbtn.configure(state=DISABLED)
        COdpbtn.configure(state=DISABLED)
    elif PodpVar == 12:
        bodp = 1
        AOdpbtn.configure(state=DISABLED)
        COdpbtn.configure(state=DISABLED)
    elif PodpVar == 13:
        codp = 1
        BOdpbtn.configure(state=DISABLED)
        DOdpbtn.configure(state=DISABLED)
    elif PodpVar == 14:
        dodp = 1
        AOdpbtn.configure(state=DISABLED)
        COdpbtn.configure(state=DISABLED)
        
def kolo2():   #kolo ratunkowe pytanie do publicznosci
    global PodpVar
    if PodpVar == 11:
        pyt = "A"
    elif PodpVar == 12:
        pyt = "B"
    elif PodpVar == 13:
        pyt ="C"
    elif PodpVar == 14:
        pyt = "D"

    pytdopub.configure(state=DISABLED)
    szanse = [1,2,3,4,5,6,7,8,9,10]
    a = random.choice(szanse)
    b = ["A","B","C","D"]
    if a >= 4:
        kolav.set("publiczność uważa, że to "+pyt)
    else:
        kolav.set("publiczność uważa, że to "+random.choice(b))

def kolo3():   #kolo ratunkowe telefon do przyjaciela
    global PodpVar
    if PodpVar == 11:
        pyt = "A"
    elif PodpVar == 12:
        pyt = "B"
    elif PodpVar == 13:
        pyt ="C"
    elif PodpVar == 14:
        pyt = "D"

    teldoprz.configure(state=DISABLED)
    szanse = [1,2,3,4,5,6,7,8,9,10]
    a = random.choice(szanse)
    b = ["A","B","C","D"]
    if a >= 4:
        kolav.set("przyjaciel uważa, że to "+pyt)
    if a == 1:
        kolav.set("przyjaciel nie odebrał telefonu")
    else:
        kolav.set("przyjaciel uważa, że to "+random.choice(b))

#zmienne
pytanieVar = ctk.StringVar()

PodpVar = ctk.IntVar()  #poprawna odpowiedz
PodpVar = int(OdpP)
#11 = A, 12 = B, 13 = C, 14 = D

AodpVar = ctk.StringVar()  #odpowiedz a
AodpVar.set("A: "+OdpA)

BodpVar = ctk.StringVar()  #odpowiedz b
BodpVar.set("B: "+OdpB)

CodpVar = ctk.StringVar()  #odpowiedz c
CodpVar.set("C: "+OdpC)

DodpVar = ctk.StringVar()  #odpowiedz d
DodpVar.set("D: "+OdpD)

wynik  = ctk.StringVar()  #wynik (poprawne/niepoprawne)
wynik.set("Tu wyswietli sie poprawnosc odpowiedzi")

Gowna = ctk.IntVar()  #punkty
Gowna.set(1)

c = ctk.StringVar()  #punkty na wyswietleniu
c.set("Pytanie "+str(Gowna.get())+"/12")

kasagw = ctk.IntVar()  #gwarantowane pieniadze mimo przegranej
kasaV = ctk.StringVar()
kasaV.set("Otrzymujesz gwarantowane "+str(kasagw.get())+"zł")

kolav = ctk.StringVar() #tekst wyswietlony po uzyciu kola ratunkowego (poza 50/50)

frame1 = ctk.CTkFrame(windowgra,fg_color=bg)
frame2 = ctk.CTkFrame(windowgra,fg_color=bg)
frame3 = ctk.CTkFrame(windowgra,fg_color=bg)
frame4 = ctk.CTkFrame(windowgra,fg_color=bg)

#labele etc
pytanieL = ctk.CTkLabel(windowgra,
                 textvariable=pytanieVar,
                 font=font_pytanie,
                 width=60,
                 text_color=font_color,
                 height=5,
                 wraplength=500,
                 fg_color=bg)

pytanieVar.set(pytanie)

wynikL = ctk.CTkLabel(frame3,
               textvariable=wynik,
               font=font_default,
               text_color=font_color,
               fg_color=bg)

gownol = ctk.CTkLabel(frame3,
               textvariable=c,
               font=font_default,
               text_color=font_color,
               fg_color=bg)

kasa = ctk.CTkLabel(frame3,
             textvariable=kasaV,
             text_color=font_color,font=font_default)

kola = ctk.CTkLabel(frame3, textvariable = kolav,font=font_default)

#--------------buttony----------------

#odpowiedzi
AOdpbtn = ctk.CTkButton(frame1,
                 textvariable=AodpVar,
                 font=font_default,
                 bg_color=bg,
                 command=lambda: sprawdzenie(1),
                 height=height)

BOdpbtn = ctk.CTkButton(frame1,
                 textvariable=BodpVar,
                 font=font_default,
                 bg_color=bg,
                 command=lambda: sprawdzenie(2),
                 height=height)

COdpbtn = ctk.CTkButton(frame2,
                 textvariable=CodpVar,
                 font=font_default,
                 bg_color=bg,
                 command=lambda: sprawdzenie(3),
                 height=height)

DOdpbtn = ctk.CTkButton(frame2,
                 textvariable=DodpVar,
                 font=font_default,
                 bg_color=bg,
                 command=lambda: sprawdzenie(4),
                 height=height,
                 corner_radius=0)

#kola ratunkowe
fiftyfifty = ctk.CTkButton(frame4,
                            text = '50/50',
                            command=lambda:kolo1(),
                            corner_radius=0)

pytdopub = ctk.CTkButton(frame4,
                         text = "pytanie do publicznosci",
                         command=lambda: kolo2(),
                         corner_radius=0)

teldoprz = ctk.CTkButton(frame4,
                         text='telefon do przyjaciela',
                         command=lambda: kolo3(),
                         corner_radius=0)


#ulozenie labeli, butonow etc
pytanieL.pack(side=TOP,padx=5,pady=5,expand = False, fill = BOTH)
AOdpbtn.pack(side=LEFT, padx=5,pady=5, expand = True, fill = BOTH)
BOdpbtn.pack(side=LEFT,padx=5,pady=5, expand = True, fill = BOTH)
COdpbtn.pack(side=LEFT,padx=5,pady=5, expand = True, fill = BOTH)
DOdpbtn.pack(side=LEFT,padx=5,pady=5, expand = True, fill = BOTH)
frame1.pack(expand = True, fill = BOTH)
frame2.pack(expand = True, fill = BOTH)
gownol.pack(side=TOP,padx=5,pady=20)
kasa.pack(side=TOP,padx=5,pady=5)
wynikL.pack(side=TOP,padx=5,pady=20)
fiftyfifty.pack(side=LEFT,padx=5,pady=20)
pytdopub.pack(side=LEFT,padx=5,pady=20)
teldoprz.pack(side=LEFT,padx=5,pady=20)
kola.pack(side = TOP,padx=5,pady=20)
frame3.pack(expand = True, fill = Y)
frame4.pack(expand = True, fill = Y)

windowgra.mainloop()