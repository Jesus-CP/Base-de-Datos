
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
tree.insert('', tk.END, text='Nro de tesis por Profesor', iid=5, open=False)
tree.insert('', tk.END, text='Detalle Profesor-Tesis', iid=7, open=False)
tree.insert('', tk.END, text='Promedio Notas Profesor Tesis', iid=15, open=False)

tree.move(5, 0, 1)
tree.move(6, 0, 0)
tree.move(7, 0, 2)
tree.move(15, 0, 3)

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
tree.insert('', tk.END, text='Tesis Notas', iid=11, open=False)
tree.insert('', tk.END, text='Tesis Mejores Resultados', iid=12, open=False)

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

# Profesores
        if nombreOpcion == 'Ver Profesores':
            # Obtener los datos de los profesores
            profesores_query = "SELECT idProfesor, rut, nombre FROM Profesores"
            profesores_data = sql_fetch(con, profesores_query)

            # Mostrar los resultados en la tabla
            columnas = ('ID Profesor', 'RUT Profesor', 'Nombre Profesor')
            resDato = []

            for profesor_row in profesores_data:
                resDato.append(profesor_row)

            # Mostrar los resultados en la tabla
            crear_tabla(resDato, columnas, 'PROFESORES')

        if nombreOpcion == 'Nro de tesis por Profesor':
            # Obtener los datos de los profesores y la cantidad de tesis
            tesis_query = "SELECT Profesores.nombre, COUNT(Tesis.idTesis) AS Cantidad_Tesis " \
                          "FROM Profesores " \
                          "LEFT JOIN Miembros_Comite ON Profesores.idProfesor = Miembros_Comite.idProfesor " \
                          "JOIN Comite ON Miembros_Comite.idComite = Comite.idComite " \
                          "JOIN Tesis ON Comite.idTesis = Tesis.idTesis " \
                          "GROUP BY Profesores.idProfesor"
            tesis_data = sql_fetch(con, tesis_query)

            # Mostrar los resultados en la tabla
            columnas = ('Nombre Profesor', 'Cantidad de Tesis')
            resDato = []

            for tesis_row in tesis_data:
                resDato.append(tesis_row)

            # Mostrar los resultados en la tabla
            crear_tabla(resDato, columnas, 'Nro de tesis por Profesor')

        if nombreOpcion == 'Detalle Profesor-Tesis':
            # Obtener los datos de los profesores y sus tesis asociadas
            profesores_query = "SELECT Profesores.nombre, AreasEstudio.Descripción_Area " \
                               "FROM Profesores " \
                               "LEFT JOIN Miembros_Comite ON Profesores.idProfesor = Miembros_Comite.idProfesor " \
                               "JOIN Comite ON Miembros_Comite.idComite = Comite.idComite " \
                               "JOIN Tesis ON Comite.idTesis = Tesis.idTesis " \
                               "JOIN AreasEstudio ON Tesis.idArea = AreasEstudio.IdTema"
            profesores_data = sql_fetch(con, profesores_query)

            # Mostrar los resultados en la tabla
            columnas = ('Nombre Profesor', 'Descripción del Área')
            resDato = []

            for profesor_row in profesores_data:
                resDato.append(profesor_row)

            # Mostrar los resultados en la tabla
            crear_tabla(resDato, columnas, 'Detalle Profesor-Tesis')
        
        if nombreOpcion == 'Promedio Notas Profesor Tesis':
            # Obtener los datos de los profesores y su promedio de notas
            promedio_query = "SELECT Profesores.nombre, AVG(Miembros_Comite.notaDocumento) AS Promedio_Nota " \
                            "FROM Profesores " \
                            "JOIN Miembros_Comite ON Profesores.idProfesor = Miembros_Comite.idProfesor " \
                            "GROUP BY Profesores.idProfesor"
            promedio_data = sql_fetch(con, promedio_query)

            # Mostrar los resultados en la tabla
            columnas = ('Nombre Profesor', 'Promedio de Notas')
            resDato = []

            for promedio_row in promedio_data:
                resDato.append(promedio_row)

            # Mostrar los resultados en la tabla
            crear_tabla(resDato, columnas, 'Promedio Notas Profesor Tesis')
# Alumnos
        if nombreOpcion=='Ver Alumnos'  :
                resDato=sql_fetch(con,"SELECT idAlumno,rut,nombre, descripción FROM alumnos, carreras WHERE alumnos.idCarrera = carreras.idCarrera")
                #showinfo(title='Selección', message="Nodo : "+str(item))
                columnas = ('ID', 'RUT', 'Nombre','CARRERA')
                crear_tabla(resDato, columnas, 'ALUMNOS')
# Tesis
        if nombreOpcion=='Ver Tesis'  :
                resDato=sql_fetch(con,"SELECT tesis.IdTesis, alumnos.nombre, alumnos.rut, areasestudio.descripción_area, estadostesis.descripción_estado FROM Tesis JOIN alumnos ON tesis.IdAlumno = alumnos.IdAlumno JOIN estadostesis ON tesis.IdSituación = estadostesis.IdSituación  JOIN areasestudio ON tesis.idArea = areasestudio.IdTema;")
                #showinfo(title='Selección', message="Nodo : "+str(item))
                columnas=('ID', 'Nombre Alumno', 'Rut Alumno','Área', 'Estado Tesis')
                crear_tabla(resDato, columnas, 'TESIS')

        if nombreOpcion == 'Tesis Notas':
            # Obtener los datos de las tesis y sus notas
            tesis_query = "SELECT Tesis.IdTesis, AreasEstudio.Descripción_Area, Miembros_Comite.notaDocumento, Miembros_Comite.notaDefensa " \
                        "FROM Tesis " \
                        "JOIN Comite ON Tesis.IdTesis = Comite.idTesis " \
                        "JOIN Miembros_Comite ON Comite.idComite = Miembros_Comite.idComite " \
                        "JOIN AreasEstudio ON Tesis.idArea = AreasEstudio.IdTema"
            tesis_data = sql_fetch(con, tesis_query)

            # Mostrar los resultados en la tabla
            columnas = ('ID Tesis', 'Descripción del Área', 'Nota Documento', 'Nota Defensa')
            resDato = []

            for tesis_row in tesis_data:
                resDato.append(tesis_row)

            # Mostrar los resultados en la tabla
            crear_tabla(resDato, columnas, 'TESIS Y NOTAS')

        if nombreOpcion == 'Tesis Mejores Resultados':
            # Obtener los datos de las tesis con mejores resultados
            resultados_query = "SELECT Tesis.IdTesis, Alumnos.nombre, AreasEstudio.Descripción_Area, Profesores.nombre, Miembros_Comite.notaDocumento, Miembros_Comite.notaDefensa " \
                            "FROM Tesis " \
                            "JOIN Alumnos ON Tesis.idAlumno = Alumnos.idAlumno " \
                            "JOIN Comite ON Tesis.idTesis = Comite.idTesis " \
                            "JOIN Miembros_Comite ON Comite.idComite = Miembros_Comite.idComite " \
                            "JOIN Profesores ON Miembros_Comite.idProfesor = Profesores.idProfesor " \
                            "JOIN AreasEstudio ON Tesis.idArea = AreasEstudio.IdTema " \
                            "ORDER BY (Miembros_Comite.notaDocumento + Miembros_Comite.notaDefensa) DESC " \
                            "LIMIT 2"
            resultados_data = sql_fetch(con, resultados_query)

            # Mostrar los resultados en la tabla
            columnas = ('Título de la Tesis', 'Nombre del Alumno', 'Descripción del Área', 'Profesor Asociado', 'Nota Documento', 'Nota Defensa')
            resDato = []

            for resultado_row in resultados_data:
                resDato.append(resultado_row)

            # Mostrar los resultados en la tabla
            crear_tabla(resDato, columnas, 'TESIS MEJORES RESULTADOS')

# ____________control de la opcion escogida____________________
tree.bind('<<TreeviewSelect>>', item_selected)

# _______ubica el arbol en la raiz__________________ 
tree.grid(row=0, column=0, sticky='nsew')
root.mainloop()
