# Trabajar con archivos csv

import csv
from pathlib import Path

FILE_PATH = Path("users.csv")

def read_csv():
    try:
        with open(FILE_PATH, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                print(row.get("first_name"), ' : ' , row.get("email"))
    except:
        print("No se encontro el archivo!")

def write_csv():
    try:
        with open(FILE_PATH, "a", newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=["first_name", "last_name", "email"], lineterminator="\n")
            csv_writer.writerows(
                [
                    {
                        "first_name": "Jaime",
                        "last_name": "Bayle",
                        "email": "kjaime@gmail.com"
                    },
                    {
                        "first_name": "Francisco",
                        "last_name": "Bolognesi",
                        "email": "fbolognesi@gmail.com"
                    }
                ]
            )
            print("Se escribio con exito")
    except:
        print("No se encontro el archivo")

if __name__ == "__main__":
    write_csv()
    read_csv()