CREATE TABLE IF NOT EXISTS fst_table(
    cod_localidad INT,
    id_provincia INT,
    id_departamento INT,
    categoría TEXT,
    provincia TEXT,
    localidad TEXT,
    nombre TEXT,
    domicilio TEXT,
    "código postal" TEXT,
    "número de teléfono" TEXT,
    mail TEXT,
    web TEXT,
    "fecha de carga" TEXT
);


CREATE TABLE IF NOT EXISTS snd_table(
    categoría TEXT,
    "total por categoría" INT,
    fuente TEXT,
    "total por fuente" INT,
    provincia TEXT,
    "total por provincia y categoría" INT,
    "fecha de carga" TEXT
);


CREATE TABLE IF NOT EXISTS trd_table(
    Provincia TEXT,
    "Cantidad de pantallas" INT,
    "Cantidad de butacas" INT,
    "Cantidad de espacios INCAA" INT
);

