import csv
import os
import Telefonbuch_modul

def export_to_csv(filename="telefonbuch.csv"):
    """Exportiert den Datenstamm als CSV-Datei."""
    data = Telefonbuch_modul.read_data()
    if data:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Id", "Vorname", "Nachname", "Strasse", "Hausnummer", "Postleitzahl", "Stadt", "Land", "TelefonNr"])
            writer.writerows(data)
        print("Daten wurden erfolgreich als CSV exportiert.")
    else:
        print("Das Telefonbuch ist leer.")
    #input("Drücken Sie Enter, um fortzufahren...")

def import_from_csv(filename):
    """Importiert Daten aus einer CSV-Datei in den Datenstamm."""
    if not os.path.exists(filename):
        print("Die CSV-Datei existiert nicht.")
        return

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Überspringt die Header-Zeile
        data = [row for row in reader]
    if data:
        Telefonbuch_modul.insert_data(data)
        print("Daten wurden erfolgreich aus der CSV-Datei importiert.")
    else:
        print("Die CSV-Datei ist leer.")




