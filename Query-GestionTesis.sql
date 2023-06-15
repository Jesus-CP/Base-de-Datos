SELECT nombre,rut FROM Tesis,Alumnos WHERE Tesis.idAlumno = Alumnos.idAlumno
SELECT nombre,rut FROM Tesis INNER JOIN Alumnos on Tesis.idAlumno = Alumnos.idAlumno
SELECT nombre,rut FROM Tesis INNER JOIN Alumnos on Tesis.idAlumno =Alumnos.idAlumno
SELECT rut from Miembros_Comite LEFT JOIN profesores on Miembros_Comite.idProfesor = Profesores.idProfesor
