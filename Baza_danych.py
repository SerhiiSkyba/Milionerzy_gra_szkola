import tkinter as tk
import mysql.connector
import random
gracz1 = 0
gracz2 = 0
gracz3 = 0
gracz4 = 0

listpyt=[]
listodp=[]
listnum=[]
listodpA=[]
listodpB=[]
listodpC=[]
listodpD=[]
MySQL = mysql.connector.connect(
            host = 'localhost',
            user = 'Admin',
            passwd = 'admin',
            database = 'pytania')
cursor = MySQL.cursor()
cursor.execute('select * from pytania')
records = cursor.fetchall()
print("Total number of rows in table: ", cursor.rowcount)
print("\nPrinting each row")
for row in records:
    listnum.append(row[0])
    listpyt.append(row[1])
    listodp.append(row[2])
    listodpA.append(row[3])
    listodpB.append(row[4])
    listodpC.append(row[5])
    listodpD.append(row[6])
