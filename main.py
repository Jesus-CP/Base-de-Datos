
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('GestionTesisMR.db')

        return con

    except Error:

         print(Error)

# Muestra los registros
#_________________________________________

def sql_fetch(con,Comando_Sql):
     cursorObj = con.cursor()
     cursorObj.execute(Comando_Sql)
     rows = cursorObj.fetchall()
     for row in rows:
         print(row)
     con.commit()
     return rows

con = sql_connection()

resDato=sql_fetch(con,'SELECT COUNT(*) FROM Tesis')
print(resDato)

root = tk.Tk()
root.title('Vistas de Gestión de tesis')
root.geometry('400x200')
