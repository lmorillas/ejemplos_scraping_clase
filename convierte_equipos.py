import json
import csv

datos = json.load(open("equipos.json"))

#limpieza
datos = datos[0]
datos = datos["rows"]
datos = [d["values"] for d in datos]
claves = datos[0]

#crear csv
f = open("equipos.csv", "w")
fw = csv.writer(f)
fw.writerows(datos)
f.close()

# De csv a json
from csv import DictReader
dr = DictReader(open("equipos.csv"))
datosj = [x for x in dr]

# Convertir listas a json
datosj = [dict(zip(claves, d)) for d in datos[1:]]

json.dump(datosj, open("datos_equipos.json", "w"), ensure_ascii=False)
