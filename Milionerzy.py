import tkinter as tk
import mysql.connector
import random

listpyt=[]
listodp=[]
listnum=[]
listodpA=[]
listodpB=[]
listodpC=[]
listodpD=[]

#Łączy bazę danych MySQL z projektem
MySQL = mysql.connector.connect(
            host = 'localhost',
            user = 'admin',
            passwd = 'Admin',
            database = 'pytania')
cursor = MySQL.cursor()
cursor.execute('select * from pytania_do_pracy')
records = cursor.fetchall()

#Konwertuje dane tabeli MySQL w listy
for row in records:
    listnum.append(row[0])
    listpyt.append(row[1])
    listodp.append(row[2])
    listodpA.append(row[3])
    listodpB.append(row[4])
    listodpC.append(row[5])
    listodpD.append(row[6])
print(listodp)  
print(listpyt)
print(listnum)
print(listodpA)  
print(listodpB)
print(listodpC)
print(listodpD)