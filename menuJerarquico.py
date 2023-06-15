
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import sqlite3

from sqlite3 import Error

# TABLA PARA VISUALIZAR DATOS
#_________________________________________

def crear_tabla(datos, columnas,title):
    ventana = tk.Tk()
    ventana.title("Tabla de datos")

    titulo = tk.Label(ventana, text=title)
    titulo.pack()

    tabla = ttk.Treeview(ventana)
    tabla['columns'] = columnas
    tabla.heading('#0', text='')
    tabla.column('#0', width=10)
    for c in columnas:
        tabla.heading(c, text=c, anchor='center')
        tabla.column(c, anchor='center')       

    for dato in datos:
        val = []
        for l in dato:
             val.append(l)
        tabla.insert(parent='', index='end', values=(val))

    tabla.pack()
    def cerrar_ventana():
         ventana.destroy()
         

    btn_cerrar = tk.Button(ventana, text='Cerrar', command=cerrar_ventana)
    btn_cerrar.pack()

    ventana.mainloop()

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

resDato=sql_fetch(con,'SELECT COUNT(*) FROM Alumnos')


root = tk.Tk()
root.title('Gestión de tesis')
root.geometry('400x400')

# ___________define el  grid layout ____________
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# __________crear treeview __________________
tree = ttk.Treeview(root)
tree.heading('#0', text='Gestión de tesis', anchor='w')
#imagen1 = tk.PhotoImage(file="4ccc.png")
#imagen2 = tk.PhotoImage(file="aa.png")
# adiciona opciones 
tree.insert('', tk.END, text='Profesores', iid=0, open=False)
tree.insert('', tk.END, text='Alumnos', iid=1, open=False)
tree.insert('', tk.END, text='Tesis', iid=2, open=False)
#tree.insert('', tk.END, text='Comites', iid=3, open=False)
#tree.insert('', tk.END, text='', iid=4, open=False)
# adiciona hijos al primer nodo SUBMENÚ PROFESORES
tree.insert('', tk.END, text='Ver Profesores', iid=6, open=False)
tree.insert('', tk.END, text='Nro de tesis Guias', iid=5, open=False)
tree.insert('', tk.END, text='Existentes', iid=7, open=False)

tree.move(5, 0, 1)
tree.move(6, 0, 0)
tree.move(7, 0, 2)

# adicina hijos al segundo nodo SUBMENÚ ALUMNOS
tree.insert('', tk.END, text='Ver Alumnos', iid=10, open=False)
tree.insert('', tk.END, text='Carrera', iid=8, open=False)
tree.insert('', tk.END, text='Insertar Alumno', iid=9, open=False)
tree.move(8, 1, 2)
tree.move(9, 1, 1)
tree.move(10, 1, 0)
#tree.move(4, 1, 3)


# adicina hijos al segundo nodo SUBMENÚ TESIS
tree.insert('', tk.END, text='Ver Tesis', iid=13, open=False)
tree.insert('', tk.END, text='ESTADO', iid=11, open=False)
tree.insert('', tk.END, text='Insertar TESIS', iid=12, open=False)

tree.move(11, 2, 2)
tree.move(12, 2, 1)
tree.move(13, 2, 0)

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
    
        if nombreOpcion=='Ver Tesis'  :
                resDato=sql_fetch(con,"SELECT tesis.IdTesis, alumnos.rut, alumnos.nombre, areasestudio.descripción_area, estadostesis.descripción_estado FROM Tesis JOIN alumnos ON tesis.IdAlumno = alumnos.IdAlumno JOIN estadostesis ON tesis.IdSituación = estadostesis.IdSituación  JOIN areasestudio ON tesis.idArea = areasestudio.IdTema;")
                #showinfo(title='Selección', message="Nodo : "+str(item))
                columnas=('ID', 'Nombre Alumno', 'Rut Alumno','Área', 'Estado Tesis')
                crear_tabla(resDato, columnas, 'TESIS')

        if nombreOpcion=='Ver Profesores'  :
                resDato=sql_fetch(con,"SELECT * FROM profesores")
                #showinfo(title='Selección', message="Se mostrarán todos los alumnos")
                columnas=('ID', 'Nombre', 'RUT')
                crear_tabla(resDato, columnas, 'PROFESORES')

        if nombreOpcion=='Ver Alumnos'  :
                resDato=sql_fetch(con,"SELECT idAlumno,rut,nombre, descripción FROM alumnos, carreras WHERE alumnos.idCarrera = carreras.idCarrera")
                #showinfo(title='Selección', message="Nodo : "+str(item))
                columnas = ('ID', 'RUT', 'Nombre','CARRERA')
                crear_tabla(resDato, columnas, 'ALUMNOS')

# ____________control de la opcion escogida____________________
tree.bind('<<TreeviewSelect>>', item_selected)

# _______ubica el arbol en la raiz__________________ 
tree.grid(row=0, column=0, sticky='nsew')
root.mainloop()
