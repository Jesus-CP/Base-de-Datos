INSERT INTO Carreras(idCarrera, descripción ) VALUES(1,'Computaciòn e informatica');
INSERT INTO Carreras(idCarrera, descripción ) VALUES(2,'Contaduria');
INSERT INTO Carreras(idCarrera, descripción ) VALUES(3,'Industrial');
INSERT INTO alumnos (idAlumno, nombre,rut,idCarrera) VALUES(1,'Jesus','27019',1);
INSERT INTO alumnos (idAlumno, nombre,rut,idCarrera) VALUES(2,'Millaray','23232',1);
INSERT INTO alumnos (idAlumno, nombre,rut,idCarrera) VALUES(3,'Vicente','12123',2);
INSERT INTO alumnos (idAlumno, nombre,rut,idCarrera) VALUES(4,'Vicente','12123',3);

INSERT INTO AreasEstudio(IdTema, Descripción_Area ) VALUES(1,'Analitica de datos');
INSERT INTO AreasEstudio(idtema, Descripción_Area ) VALUES(2,'Reconocimiento de objetos');
INSERT INTO AreasEstudio(idTema, Descripción_Area ) VALUES(3,'Programaciòn de eventos');

INSERT INTO EstadosTesis(idSituación, descripción_estado ) VALUES(1,'Presentaciòn');
INSERT INTO EstadosTesis(idSituación, descripción_estado ) VALUES(2,'Revisiòn');
INSERT INTO EstadosTesis(idSituación, descripción_estado ) VALUES(3,'Graduado');

INSERT INTO Profesores(idProfesor, rut,nombre) VALUES(1,'123','Rodolofo');
INSERT INTO Profesores(idProfesor, rut,nombre) VALUES(2,'234','Ana');
INSERT INTO Profesores(idProfesor, rut,nombre) VALUES(3,'345','Yudith');

INSERT INTO Role VALUES(1,'Guia');
INSERT INTO Role VALUES(2,'Informante 1');
INSERT INTO Role VALUES(3,'Informante 2');

INSERT INTO Tesis(idTesis, idAlumno, idArea,IdSituación) VALUES(1,1,1,1);
INSERT INTO Tesis(idTesis, idAlumno, idArea,IdSituación) VALUES(2,2,2,1);
INSERT INTO Tesis(idTesis, idAlumno, idArea,IdSituación) VALUES(3,3,3,1);

INSERT INTO Comite(idComite,idTesis) VALUES(1,1);
INSERT INTO Comite(idComite,idTesis) VALUES(2,2);
INSERT INTO Comite(idComite,idTesis) VALUES(3,3);

INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(1,1,1,7,7);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(2,2,2,5,4);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(3,3,3,3,3);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(1,3,1,5,6);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(2,2,2,6,6);
INSERT INTO Miembros_Comite(idComite,idProfesor,idRol,notaDocumento,notaDefensa) VALUES(3,1,3,4,5);