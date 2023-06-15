
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import sqlite3

from sqlite3 import Error

#_________________________________________

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

# ___________define el  grid layout ____________
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# __________crear treeview __________________
tree = ttk.Treeview(root)
tree.heading('#0', text='Gestión de tesis', anchor='w')
imagen1 = tk.PhotoImage(file="4ccc.png")
#imagen2 = tk.PhotoImage(file="aa.png")
# adiciona opciones 
tree.insert('', tk.END, text='Profesores', iid=0, open=False)
tree.insert('', tk.END, text='Alumnos', iid=1, open=False)
tree.insert('', tk.END, text='Tesis', iid=2, open=False)
tree.insert('', tk.END, text='Comites', iid=3, open=False)
tree.insert('', tk.END, text='', iid=4, open=False)
# adiciona hijos al primer nodo
tree.insert('', tk.END, text='Nro de tesis Guias',image=imagen1, iid=5, open=False)
tree.insert('', tk.END, text='Insertar Profesores', iid=6, open=False)
tree.insert('', tk.END, text='Existentes', iid=7, open=False)

tree.move(5, 0, 0)
tree.move(6, 0, 1)
tree.move(7, 0, 2)
#tree.move(8, 0, 3)
#tree.move(2, 1, 1)
#tree.move(3, 1, 2)
#tree.move(4, 1, 3)


# __________Item escogido ___________________________
def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        valor = item['values']
        nombreOpcion = item['text']
        imagen = item['image']
        abierto = item['open']
    
        if nombreOpcion=='Tesis'  :
                resDato=sql_fetch(con,"SELECT nombre,rut FROM Tesis INNER JOIN Alumnos on Tesis.idAlumno = Alumnos.idAlumno")
                showinfo(title='Selección', message="Nodo : "+str(item))

        if nombreOpcion=='Profesores'  :
                resDato=sql_fetch(con,"SELECT nombre, rut FROM Alumnos")
                showinfo(title='Selección', message="Nodo : "+str(item))

        if nombreOpcion=='Alumnos'  :
                resDato=sql_fetch(con,"SELECT nombre,rut FROM profesores")
                showinfo(title='Selección', message="Nodo : "+str(item))

# ____________control de la opcion escogida____________________
tree.bind('<<TreeviewSelect>>', item_selected)

# _______ubica el arbol en la raiz__________________ 
tree.grid(row=0, column=0, sticky='nsew')
root.mainloop()
