import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import numpy as np
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
tree.insert('', tk.END, text='Distribución de Notas de los Profesores', iid=20, open=False)

tree.move(5, 0, 1)
tree.move(6, 0, 0)
tree.move(7, 0, 2)
tree.move(15, 0, 3)
tree.move(20, 0, 4)

# adicina hijos al segundo nodo SUBMENÚ ALUMNOS
tree.insert('', tk.END, text='Ver Alumnos', iid=8, open=False)

tree.move(8, 1, 2)
#tree.move(4, 1, 3)


# adicina hijos al segundo nodo SUBMENÚ TESIS
tree.insert('', tk.END, text='Ver Tesis', iid=13, open=False)
tree.insert('', tk.END, text='Tesis Notas del comite', iid=11, open=False)
tree.insert('', tk.END, text='Tesis Notas', iid=12, open=False)
tree.insert('', tk.END, text='Tesis Mejores Resultados', iid=16, open=False)
tree.insert('', tk.END, text='Distribución de Situaciones Tesis', iid=21, open=False)

tree.move(11, 2, 2)
tree.move(12, 2, 1)
tree.move(13, 2, 0)
tree.move(16, 2, 3)
tree.move(21, 2, 4)

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
            # Obtener los datos de las tesis y sus notas
            tesis_query = "SELECT Profesores.Nombre, AVG((Miembros_Comite.notaDocumento + Miembros_Comite.notaDefensa) / 2) AS Promedio " \
                        "FROM Tesis " \
                        "JOIN Comite ON Tesis.IdTesis = Comite.idTesis " \
                        "JOIN Miembros_Comite ON Comite.idComite = Miembros_Comite.idComite " \
                        "JOIN Profesores ON Miembros_Comite.idProfesor = Profesores.idProfesor " \
                        "GROUP BY Profesores.Nombre"
            tesis_data = sql_fetch(con, tesis_query)

            # Mostrar los resultados en la tabla
            columnas = ('Profesor', 'Promedio Notas')
            resDato = []

            for tesis_row in tesis_data:
                resDato.append(tesis_row)

            # Mostrar los resultados en la tabla
            crear_tabla(resDato, columnas, 'Promedio Notas Profesor Tesis')

        if nombreOpcion == 'Distribución de Notas de los Profesores':
            # Consulta para obtener las notas de los profesores
            notas_query = "SELECT notaDocumento, notaDefensa FROM Miembros_Comite"
            notas_data = sql_fetch(con, notas_query)

            # Obtener las notas de documento y defensa en listas separadas
            notas_documento = [row[0] for row in notas_data]
            notas_defensa = [row[1] for row in notas_data]

            # Calcular la nota final como promedio de las notas de documento y defensa
            notas_final = np.mean([notas_documento, notas_defensa], axis=0)

            # Calcular la distribución de notas utilizando histograma
            histograma, bins = np.histogram(notas_final, bins=[0, 4, 5, 6, 7])

            # Crear una tabla con la distribución de notas
            tabla_notas = []
            for i in range(len(histograma)):
                nota_inferior = bins[i]
                nota_superior = bins[i + 1]
                frecuencia = histograma[i]
                porcentaje = (frecuencia / len(notas_final)) * 100
                tabla_notas.append([f"Notas entre {nota_inferior} y {nota_superior}", porcentaje])

            # Mostrar la tabla
            columnas = ('Rango de Notas', 'Porcentaje')
            crear_tabla(tabla_notas, columnas, 'Distribución de Notas de los Profesores')

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

        if nombreOpcion == 'Tesis Notas del comite':
            # Obtener los datos de las tesis y sus notas
            tesis_query = "SELECT Tesis.IdTesis, AreasEstudio.Descripción_Area, Miembros_Comite.notaDocumento, " \
                        "Miembros_Comite.notaDefensa, Profesores.Nombre " \
                        "FROM Tesis " \
                        "JOIN Comite ON Tesis.IdTesis = Comite.idTesis " \
                        "JOIN Miembros_Comite ON Comite.idComite = Miembros_Comite.idComite " \
                        "JOIN AreasEstudio ON Tesis.idArea = AreasEstudio.IdTema " \
                        "JOIN Profesores ON Miembros_Comite.idProfesor = Profesores.idProfesor"
            tesis_data = sql_fetch(con, tesis_query)

            # Mostrar los resultados en la tabla
            columnas = ('ID Tesis', 'Descripción del Área', 'Nota Documento', 'Nota Defensa', 'Profesor')
            resDato = []

            for tesis_row in tesis_data:
                resDato.append(tesis_row)

            # Mostrar los resultados en la tabla
            crear_tabla(resDato, columnas, 'TESIS NOTAS DEL COMITE')
        
        if nombreOpcion == 'Tesis Notas':
            # Obtener el promedio de notas por título de tesis
            promedio_query = "SELECT Tesis.IdTesis, AreasEstudio.Descripción_Area, Alumnos.Nombre, " \
                            "AVG((Miembros_Comite.notaDocumento + Miembros_Comite.notaDefensa) / 2) AS Promedio " \
                            "FROM Tesis " \
                            "JOIN Comite ON Tesis.IdTesis = Comite.idTesis " \
                            "JOIN Miembros_Comite ON Comite.idComite = Miembros_Comite.idComite " \
                            "JOIN AreasEstudio ON Tesis.idArea = AreasEstudio.IdTema " \
                            "JOIN Alumnos ON Tesis.idAlumno = Alumnos.idAlumno " \
                            "GROUP BY Tesis.IdTesis"
            promedio_data = sql_fetch(con, promedio_query)

            # Mostrar los resultados en la tabla
            columnas = ('ID Tesis', 'Descripción del Área', 'Alumno', 'Promedio Notas')
            resDato = []

            for promedio_row in promedio_data:
                id_tesis = promedio_row[0]
                area_estudio = promedio_row[1]
                alumno = promedio_row[2]
                promedio = promedio_row[3]
                resDato.append((id_tesis, area_estudio, alumno, promedio))

            # Mostrar los resultados en la tabla
            crear_tabla(resDato, columnas, 'TESIS NOTAS')

        if nombreOpcion == 'Tesis Mejores Resultados':
            # Obtener el promedio de notas por título de tesis
            promedio_query = "SELECT Tesis.IdTesis, AreasEstudio.Descripción_Area, Alumnos.Nombre, " \
                            "AVG((Miembros_Comite.notaDocumento + Miembros_Comite.notaDefensa) / 2) AS Promedio " \
                            "FROM Tesis " \
                            "JOIN Comite ON Tesis.IdTesis = Comite.idTesis " \
                            "JOIN Miembros_Comite ON Comite.idComite = Miembros_Comite.idComite " \
                            "JOIN AreasEstudio ON Tesis.idArea = AreasEstudio.IdTema " \
                            "JOIN Alumnos ON Tesis.idAlumno = Alumnos.idAlumno " \
                            "GROUP BY Tesis.IdTesis"
            promedio_data = sql_fetch(con, promedio_query)

            # Mostrar los resultados en la tabla
            columnas = ('ID Tesis', 'Descripción del Área', 'Alumno', 'Promedio Notas')
            resDato = []

            for promedio_row in promedio_data:
                id_tesis = promedio_row[0]
                area_estudio = promedio_row[1]
                alumno = promedio_row[2]
                promedio = promedio_row[3]
                resDato.append((id_tesis, area_estudio, alumno, promedio))

            # Ordenar los resultados por el promedio de notas de forma descendente
            resDato.sort(key=lambda x: x[3], reverse=True)

            # Mostrar solo las dos primeras filas (las mejores notas)
            resDato = resDato[:2]

            # Mostrar los resultados en la tabla
            crear_tabla(resDato, columnas, 'TESIS MEJORES RESULTADOS')

        if nombreOpcion == 'Distribución de Situaciones Tesis':
            # Tabla EstadosTesis
            estados_tesis = np.array([
                [1, 'Presentación'],
                [2, 'Revisión'],
                [3, 'Graduado']
            ])

            # Tabla Tesis
            tesis = np.array([
                [1, 1, 1, 1],
                [2, 2, 2, 1],
                [3, 3, 3, 1]
            ])

            # Calcular el número total de tesis
            total_tesis = len(tesis)

            # Calcular el número de tesis en cada estado
            num_tesis_presentacion = np.sum(tesis[:, 3] == 1)
            num_tesis_revision = np.sum(tesis[:, 3] == 2)
            num_tesis_graduado = np.sum(tesis[:, 3] == 3)

            # Calcular el porcentaje de tesis en cada estado
            porcentaje_presentacion = (num_tesis_presentacion / total_tesis) * 100
            porcentaje_revision = (num_tesis_revision / total_tesis) * 100
            porcentaje_graduado = (num_tesis_graduado / total_tesis) * 100

            # Crear una tabla con la información
            tabla_situaciones = [
                ['Presentación', porcentaje_presentacion],
                ['Revisión', porcentaje_revision],
                ['Graduado', porcentaje_graduado]
            ]

            # Mostrar la tabla
            columnas = ('Situación', 'Porcentaje')
            crear_tabla(tabla_situaciones, columnas, 'Distribución de Situaciones Tesis')
# ____________control de la opcion escogida____________________
tree.bind('<<TreeviewSelect>>', item_selected)

# _______ubica el arbol en la raiz__________________ 
tree.grid(row=0, column=0, sticky='nsew')
root.mainloop()
