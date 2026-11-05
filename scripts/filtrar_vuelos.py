import csv
import sys

archivo = sys.argv[1]
contador = 0

with open(archivo, newline="", encoding="utf-8-sig") as f:
    for vuelo in csv.DictReader(f):
        if vuelo["Origin"] == "JFK":
            contador += 1

print("Vuelos con origen JFK:", contador)
