import random

# Beispiellisten von Ländern, Vornamen und Nachnamen
beispiel_laender = ["Deutschland", "Frankreich", "Italien", "Spanien", "USA", "Kanada", "Japan", "China", "Indien", "Brasilien", "Russland", "Schweiz", "Österreich", "Niederlande", "Belgien", "Portugal", "Australien", "Neuseeland", "Südafrika", "Ägypten", "Griechenland", "Türkei", "Mexiko", "Argentinien", "Kolumbien", "Chile", "Peru", "Thailand", "Vietnam", "Südkorea"]
beispiel_vornamen = ["Max", "Anna", "Paul", "Maria", "Felix", "Sophie", "Tim", "Lena", "Moritz", "Laura", "Julian", "Emma", "Jonas", "Lisa", "Leon", "Sarah", "Luca", "Hannah", "Finn", "Lea", "Elias", "Mia", "Nico", "Jana", "Jan", "Clara", "David", "Lara", "Lukas", "Elena"]
beispiel_nachnamen = ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann", "Schäfer", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schröder", "Neumann", "Schwarz", "Zimmermann", "Braun", "Krüger", "Hofmann", "Hartmann", "Lange", "Schmitt", "Werner", "Schmitz", "Krause", "Meier"]

def generate_random_data():
    """Generiert einen neuen Beispieldatensatz."""
    land = random.choice(beispiel_laender)
    vorname = random.choice(beispiel_vornamen)
    nachname = random.choice(beispiel_nachnamen)
    telefonnr = str(random.randint(1000000000, 9999999999))
    return [land, vorname, nachname, telefonnr]

print(generate_random_data())