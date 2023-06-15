CREATE TABLE IF NOT EXISTS Carreras("idCarrera" int NOT NULL, "descripción" "char" NOT NULL, PRIMARY KEY ("idCarrera"));
CREATE TABLE IF NOT EXISTS Alumnos("idAlumno" bigint NOT NULL,rut "char" NOT NULL,nombre name NOT NULL,"idCarrera" bigint NOT NULL,PRIMARY KEY ("idAlumno"));
CREATE TABLE IF NOT EXISTS Profesores("idProfesor" bigint NOT NULL, rut "char" NOT NULL,nombre name NOT NULL,PRIMARY KEY ("idProfesor"));
CREATE TABLE IF NOT EXISTS EstadosTesis("idSituación" bigint NOT NULL,"descripción_estado" "char" NOT NULL,PRIMARY KEY ("idSituación"));
CREATE TABLE IF NOT EXISTS Tesis("idTesis" bigint NOT NULL,"idAlumno" bigint NOT NULL,"idArea" bigint NOT NULL,"idSituación" bigint NOT NULL,
    PRIMARY KEY ("idTesis"));
CREATE TABLE IF NOT EXISTS AreasEstudio("IdTema" int NOT NULL,"Descripción_Area" "char",PRIMARY KEY ("IdTema"));
CREATE TABLE IF NOT EXISTS Comite("idComite" bigint NOT NULL,"idTesis" bigint NOT NULL,PRIMARY KEY ("idComite"));
CREATE TABLE IF NOT EXISTS Role("idRol" bigint NOT NULL,"Descripción " "char" NOT NULL,PRIMARY KEY ("idRol"));
CREATE TABLE IF NOT EXISTS  Miembros_Comite("idComite" int NOT NULL,"idProfesor" bigint NOT NULL,"idRol" bigint NOT NULL,
    "notaDocumento" real NOT NULL,
    "notaDefensa" real NOT NULL
);
