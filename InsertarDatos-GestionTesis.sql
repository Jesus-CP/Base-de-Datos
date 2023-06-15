INSERT INTO alumnos (idAlumno, nombre,rut,idCarrera) VALUES(1,'Rodolfo','27019',1);
INSERT INTO alumnos (idAlumno, nombre,rut,idCarrera) VALUES(2,'Kizia','23232',1);
INSERT INTO alumnos (idAlumno, nombre,rut,idCarrera) VALUES(3,'Ofo','12123',2);
INSERT INTO alumnos (idAlumno, nombre,rut,idCarrera) VALUES(4,'Ofo','12123',3);
INSERT INTO Carreras(idCarrera, descripción ) VALUES(1,'Computaciòn e informatica');
INSERT INTO Carreras(idCarrera, descripción ) VALUES(2,'Contaduria');
INSERT INTO Carreras(idCarrera, descripción ) VALUES(3,'Indystrial');
INSERT INTO AreasEstudio(IdTema, descripcion ) VALUES(1,'Analitica de datos');
INSERT INTO AreasEstudio(idtema, descripcion ) VALUES(2,'Reconocimiento de objetos');
INSERT INTO AreasEstudio(idTema, descripcion ) VALUES(3,'Programaciòn de eventos');
INSERT INTO Situaciones(idSituacion, descripcion ) VALUES(1,'Presentaciòn');
INSERT INTO Situaciones(idSituacion, descripcion ) VALUES(2,'Revisiòn');
INSERT INTO Situaciones(idSituacion, descripcion ) VALUES(3,'Graduado');
INSERT INTO Profesores(idProfesor, rut,nombre) VALUES(1,'Rodolfo','123');
INSERT INTO Profesores(idProfesor, rut,nombre) VALUES(2,'Ana','234');
INSERT INTO Profesores(idProfesor, rut,nombre) VALUES(3,'Yudith','345');
INSERT INTO Roles(idRol, descripcion) VALUES(1,'Guia');
INSERT INTO Roles(idRol, descripcion) VALUES(2,'Informante 1');
INSERT INTO Roles(idRol, descripcion) VALUES(3,'Informante 2');
INSERT INTO Tesis(idTesis, idAlumno, idArea,IdSituacion) VALUES(1,1,1,1);
INSERT INTO Tesis(idTesis, idAlumno, idArea,IdSituacion) VALUES(2,2,2,1);
INSERT INTO Tesis(idTesis, idAlumno, idArea,IdSituacion) VALUES(3,3,2,1);
INSERT INTO Comite(idComite,idTesis) VALUES(1,1);
INSERT INTO Comite(idComite,idTesis) VALUES(2,2);
INSERT INTO Comite(idComite,idTesis) VALUES(3,3);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(1,1,1,0,0);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(1,2,2,0,0);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(1,3,3,0,0);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(2,3,1,0,0);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(2,2,2,0,0);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(2,1,3,0,0);