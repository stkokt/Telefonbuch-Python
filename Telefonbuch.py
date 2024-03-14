import os
import Telefonbuch_modul
import Telefonbuch_modul2
import Telefonbuch_modul3

def display_menu():
    """Menü anzeigen."""
    print("Telefonbuch-Menü:")
    print("1. Daten aus SQLite abrufen und anzeigen")
    print("2. Neuen Datensatz hinzufügen")
    print("3. Datensatz löschen")
    print("4. Datensatz ändern und aktualisieren")
    print("5. Neuen Beispieldatensatz erstellen und hinzufügen")
    print("6. Datenstamm als CSV exportieren")
    print("7. Datenstamm aus CSV importieren und anhängen")
    print("8. Beenden")

def show_data():
    """Daten aus SQLite abrufen und anzeigen."""
    data = Telefonbuch_modul.read_data()
    if data:
        print("Telefonbuch-Daten:")
        for record in data:
            print(record)
    else:
        print("Das Telefonbuch ist leer.")
    input("Drücken Sie Enter, um fortzufahren...")

def add_record():
    """Neuen Datensatz hinzufügen."""
    record = [
        input("Vorname: "),
        input("Nachname: "),
        input("Strasse:"),
        input("Hausnummer:"),
        input("Postleitzahl:"),
        input("Stadt:"),
        input("Land:"),
        input("Telefonnummer: ")
    ]
    Telefonbuch_modul.insert_data([record])
    print("Neuer Datensatz hinzugefügt.")
    input("Drücken Sie Enter, um fortzufahren...")

def delete_record():
    """Datensatz löschen."""
    show_data()
    record_id = input("Geben Sie die ID des zu löschenden Datensatzes ein: ")
    if record_id.strip():  # Überprüfen, ob die Eingabe nicht leer ist
        record_id = int(record_id)
        Telefonbuch_modul.delete_record(record_id)
        print("Datensatz gelöscht.")
    else:
        print("Ungültige Eingabe für ID.")
    input("Drücken Sie Enter, um fortzufahren...")

def update_record():
    """Datensatz ändern und aktualisieren."""
    show_data()
    record_id = input("Geben Sie die ID des zu aktualisierenden Datensatzes ein: ")
    if record_id.strip():  # Überprüfen, ob die Eingabe nicht leer ist
        record_id = int(record_id)
        record = [
            record_id,
            input("Neuer Vorname: "),
            input("Neuer Nachname: "),
            input("Neue Strasse:"),
            input("Neue Hausnummer:"),
            input("Neue Postleitzahl:"),
            input("Neue Stadt:"),
            input("Neues Land:"),
            input("Neue Telefonnummer: ")
        ]
        Telefonbuch_modul.update_record(record)
        print("Datensatz aktualisiert.")
    else:
        print("Ungültige Eingabe für ID.")
    input("Drücken Sie Enter, um fortzufahren...")

def add_example_record():
    """Einen neuen Beispieldatensatz erstellen und hinzufügen."""
    record = Telefonbuch_modul2.generate_random_data()
    Telefonbuch_modul.insert_data([record])
    print("Neuer Beispieldatensatz hinzugefügt.")
    input("Drücken Sie Enter, um fortzufahren...")

'''
def export_to_csv():
    """Datenstamm als CSV exportieren."""
    data = Telefonbuch_modul.read_data()
    if data:
        with open("telefonbuch.csv", "w") as file:
            file.write("Id,Land,Vorname,Nachname,TelefonNr\n")
            for record in data:
                file.write(",".join(map(str, record)) + "\n")
        print("Daten wurden erfolgreich als CSV exportiert.")
    else:
        print("Das Telefonbuch ist leer.")
    input("Drücken Sie Enter, um fortzufahren...")


def export_to_csv(filename="telefonbuch.csv"):
    """Exportiert den Datenstamm als CSV-Datei."""
    data = Telefonbuch_modul.read_data()
    if data:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Id", "Land", "Vorname", "Nachname", "TelefonNr"])
            writer.writerows(data)
        print("Daten wurden erfolgreich als CSV exportiert.")
    else:
        print("Das Telefonbuch ist leer.")
    input("Drücken Sie Enter, um fortzufahren...")
'''


# Hauptprogramm
if __name__ == "__main__":
    Telefonbuch_modul.create_table()  # Tabelle erstellen, falls sie nicht existiert
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Konsole leeren
        display_menu()
        choice = input("Bitte wählen Sie eine Option: ")
        if choice == "1":
            show_data()
        elif choice == "2":
            add_record()
        elif choice == "3":
            delete_record()
        elif choice == "4":
            update_record()
        elif choice == "5":
            add_example_record()
        elif choice == "6":
            Telefonbuch_modul3.export_to_csv("telefonbuch.csv")
        elif choice == "7":
            Telefonbuch_modul3.import_from_csv("telefonbuch.csv")
        elif choice == "8":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie erneut.")
