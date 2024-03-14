import tkinter as tk
from tkinter import filedialog
import Telefonbuch_modul
import Telefonbuch_modul3


def initialData():
    listOfContacts=Telefonbuch_modul.read_data()
    return listOfContacts

def getListCollection(event):
    listEntry=listbox_all.curselection()
    if listEntry:
        index=listEntry[0]
        value=listbox_all.get(index)
        entry_name.insert(0, value.split(",")[0])
        entry_surname.insert(0, value.split(",")[1])
        entry_street.insert(0, (value.split(",")[3]).split(" ")[1])
        entry_house_number.insert(0, (value.split(",")[3]).split(" ")[2])
        entry_postal_code.insert(0, (value.split(",")[2]).split(" ")[1])
        entry_city.insert(0, (value.split(",")[2]).split(" ")[2])
        entry_country.insert(0, value.split(",")[4])
        entry_phone.insert(0, value.split(",")[5])

def browse_datei_clicked():
    filepath=filedialog.askopenfilename(title="CSV Datei auswählen", 
                                        initialdir="D:\\Projekte\\Softwareprojekte\\Python\\Projekt Kontaktbuch\\Version2\\Telefonbuch 1",
                                        filetypes=(("csv files", "*.csv"),("text files", "*.txt")))
    entry_datei.insert(0, filepath)

def push_datei_clicked():
    Telefonbuch_modul3.import_from_csv(entry_datei.get())
    initialList=initialData()
    for contact in initialList:
        listbox_all.insert("end", " "+contact[1]+", "+contact[2]+", "+contact[5]+" "+contact[6]
                       +", "+contact[3]+" "+contact[4]+", "+contact[7]+", "+contact[8]+", "+str(contact[0]))
    entry_datei.delete(0, tk.END)


def add_contact_clicked():
    contact=[(entry_name.get(), entry_surname.get(), entry_street.get(), entry_house_number.get(),
               entry_postal_code.get(), entry_city.get(), entry_country.get(), entry_phone.get())]
    Telefonbuch_modul.insert_data(contact)


def search_clicked():
    listbox_all.delete(0, tk.END)
    exprText=""
    filterText="Id" if selected_filter.get()=="---" else selected_filter.get()
    sortDirText="asc"
    if selected_sort.get() == "Absteigend":
        sortDirText="desc"
    filteredList=Telefonbuch_modul.read_data(entry_search.get(),filterText, sortDir=sortDirText)
    for contact in filteredList:
        listbox_all.insert("end", " "+contact[1]+", "+contact[2]+", "+contact[5]+" "+contact[6]
                        +", "+contact[3]+" "+contact[4]+", "+contact[7]+", "+contact[8]+", "+str(contact[0]))
    print(entry_search.get())
    

""" def filter_selected():
    pass

def sort_selected():
    pass
 """
def edit_contact_clicked():
    listEntry=listbox_all.curselection()    
    if listEntry:
        index=listEntry[0]
        value=listbox_all.get(index)
        recordList=[value.split(",")[0],value.split(",")[1],(value.split(",")[3]).split(" ")[1],
                                (value.split(",")[3]).split(" ")[2],(value.split(",")[2]).split(" ")[1],
                                (value.split(",")[2]).split(" ")[2],value.split(",")[4],value.split(",")[5],
                                int(value.split(",")[-1])]
    Telefonbuch_modul.update_record(recordList)
    listbox_all.delete(0, tk.END)
    initialList=initialData()
    for contact in initialList:
        listbox_all.insert("end", " "+contact[1]+", "+contact[2]+", "+contact[5]+" "+contact[6]
                       +", "+contact[3]+" "+contact[4]+", "+contact[7]+", "+contact[8]+", "+str(contact[0]))
    entry_name.delete(0, tk.END)
    entry_surname.delete(0, tk.END)
    entry_street.delete(0, tk.END)
    entry_house_number.delete(0, tk.END)
    entry_postal_code.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_country.delete(0, tk.END)
    entry_phone.delete(0, tk.END)


def delete_contact_clicked():
    listEntry=listbox_all.curselection()
    recordID=int()
    if listEntry:
        index=listEntry[0]
        value=listbox_all.get(index)
        recordID=int(value.split(",")[-1])          #  int(value[-1])
        print(int(value[-1]))
    Telefonbuch_modul.delete_record(recordID)
    listbox_all.delete(0, tk.END)
    initialList=initialData()
    for contact in initialList:
        listbox_all.insert("end", " "+contact[1]+", "+contact[2]+", "+contact[5]+" "+contact[6]
                       +", "+contact[3]+" "+contact[4]+", "+contact[7]+", "+contact[8]+", "+str(contact[0]))
    entry_name.delete(0, tk.END)
    entry_surname.delete(0, tk.END)
    entry_street.delete(0, tk.END)
    entry_house_number.delete(0, tk.END)
    entry_postal_code.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_country.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def save_contact_clicked():    
    Telefonbuch_modul3.export_to_csv(filedialog.asksaveasfilename(title="CSV Datei auswählen", 
                                        initialdir="D:\\Projekte\\Softwareprojekte\\Python\\Projekt Kontaktbuch\\Version2\\Telefonbuch 1",
                                        filetypes=(("csv files", "*.csv"),("text files", "*.txt"))))



# GUI-Einrichtung
root = tk.Tk()
root.title("Kontaktdatenbank")
root.configure(bg="gray15")


# Adjust column width
root.columnconfigure(1, minsize=200)


#Überschrift Datei öffnen
datei_label = tk.Label(root, text="Datenbank aus Datei erstellen", bg="gray23", fg="gray76", font=("Helvetica", 12, "bold"))
datei_label.grid(row=0, column=0, columnspan=5, padx=10, pady=5, sticky="ew")

# Label, Eingabe und Button zum Upload
label_datei = tk.Label(root, text="Dateiname:", bg="gray15", fg="gray76")
label_datei.grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_datei = tk.Entry(root, bg="lavender", fg="gray13", width=50)
entry_datei.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="e")

browse_button = tk.Button(root, text="CSV- Datei suchen", bg="gray22", fg="gray76", activebackground="LightBlue3", width=20, command=browse_datei_clicked)
browse_button.grid(row=1, column=3, padx=10, pady=5, sticky="e")
push_button = tk.Button(root, text="In Datenbank speichern", bg="gray22", fg="gray76", activebackground="LightBlue3", width=20, command=push_datei_clicked)
push_button.grid(row=2, column=3, padx=10, pady=5, sticky="e")

# Leere Zeile als Platzhalter##################################################################################################
empty_label = tk.Label(root, text="", bg="gray15")
empty_label.grid(row=2, column=0)
###############################################################################################################################


#Überschrift Kontakte hinzufügen
kontakte_label = tk.Label(root, text="Kontaktdetail", bg="gray23", fg="gray76", font=("Helvetica", 12, "bold"))
kontakte_label.grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="ew") 

# Labels und Eingabefelder zum Hinzufügen von Kontakten erstellen


label_name = tk.Label(root, text="Vorname:", bg="gray15", fg="gray76")
label_name.grid(row=4, column=0, sticky="e", padx=10, pady=5) 
entry_name = tk.Entry(root, bg="lavender", fg="gray13", width=50, )
entry_name.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="e") 



label_surname = tk.Label(root, text="Nachname:", bg="gray15", fg="gray76")
label_surname.grid(row=5, column=0, sticky="e", padx=10, pady=5) 
entry_surname = tk.Entry(root, bg="lavender", fg="gray13", width=50)
entry_surname.grid(row=5, column=1, columnspan=2, padx=10, pady=5, sticky="e") 

label_street = tk.Label(root, text="Straße:", bg="gray15", fg="gray76")
label_street.grid(row=6, column=0, sticky="e", padx=10, pady=5) 
entry_street = tk.Entry(root, bg="lavender", fg="gray13", width=50)
entry_street.grid(row=6, column=1, columnspan=2, padx=10, pady=5, sticky="e") 

label_house_number = tk.Label(root, text="Hausnummer:", bg="gray15", fg="gray76")
label_house_number.grid(row=7, column=0, sticky="e", padx=10, pady=5) 
entry_house_number = tk.Entry(root, bg="lavender", fg="gray13", width=50)
entry_house_number.grid(row=7, column=1, columnspan=2, padx=10, pady=5, sticky="e") 

label_postal_code = tk.Label(root, text="Postleitzahl:", bg="gray15", fg="gray76")
label_postal_code.grid(row=8, column=0, sticky="e", padx=10, pady=5) 
entry_postal_code = tk.Entry(root, bg="lavender", fg="gray13", width=50)
entry_postal_code.grid(row=8, column=1, columnspan=2, padx=10, pady=5, sticky="e") 

label_city = tk.Label(root, text="Stadt:", bg="gray15", fg="gray76")
label_city.grid(row=9, column=0, sticky="e", padx=10, pady=5) 
entry_city = tk.Entry(root, bg="lavender", fg="gray13", width=50)
entry_city.grid(row=9, column=1, columnspan=2, padx=10, pady=5, sticky="e") 

label_country = tk.Label(root, text="Land:", bg="gray15", fg="gray76")
label_country.grid(row=10, column=0, sticky="e", padx=10, pady=5) 
entry_country = tk.Entry(root, bg="lavender", fg="gray13", width=50)
entry_country.grid(row=10, column=1, columnspan=2, padx=10, pady=5, sticky="e") 

label_phone = tk.Label(root, text="Telefonnummer:", bg="gray15", fg="gray76")
label_phone.grid(row=11, column=0, sticky="e", padx=10, pady=5) 
entry_phone = tk.Entry(root, bg="lavender", fg="gray13", width=50)
entry_phone.grid(row=11, column=1, columnspan=2, padx=10, pady=5, sticky="e") 

add_button = tk.Button(root, text="Kontakt hinzufügen", bg="gray22", fg="gray76", activebackground="LightBlue3",width=20, command=add_contact_clicked)
add_button.grid(row=4, column=3, padx=10, pady=5, sticky="e") 

# Button zum Bearbeiten des ausgewählten Kontakts
edit_contact_button = tk.Button(root, text="Kontakt bearbeiten", bg="gray22", fg="gray76", activebackground="LightBlue3", width=20,command=edit_contact_clicked)
edit_contact_button.grid(row=5, column=3, sticky="ew", padx=10, pady=5)

# Button zum Löschen des ausgewählten Kontakts
delete_button = tk.Button(root, text="Kontakt löschen", bg="gray22", fg="gray76", activebackground="indian red", width=20, command=delete_contact_clicked)
delete_button.grid(row=6, column=3, sticky="ew", padx=10, pady=5)

# Leere Zeile als Platzhalter##################################################################################################
empty_label = tk.Label(root, text="", bg="gray15")
empty_label.grid(row=12, column=0)
###############################################################################################################################

#Überschrift Kontaktbuch anzeigen
kontakte_label = tk.Label(root, text="Meine Kontakte", bg="gray23", fg="gray76", font=("Helvetica", 12, "bold"))
kontakte_label.grid(row=13, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

# Labels, Eingabefeld und Button zum Suchen 
label_search = tk.Label(root, text="Suche:", bg="gray15", fg="gray76")
label_search.grid(row=14, column=0, sticky="e", padx=10, pady=5)
entry_search = tk.Entry(root, bg="lavender", fg="gray13", width=50)
entry_search.grid(row=14, column=1, columnspan=2, padx=10, pady=5, sticky="e")

search_button = tk.Button(root, text="LOS!", bg="gray22", fg="gray76", activebackground="LightBlue3", width=20, command=search_clicked)
search_button.grid(row=14, column=3, padx=10, pady=5, sticky="e")


# Label für das Dropdown-Menü
filter_label = tk.Label(root, text="Filtern nach:", bg="gray15", fg="gray76")
filter_label.grid(row=15, column=0, sticky="e", padx=10, pady=5)

# Liste der Filteroptionen erstellen
filter_options = ["---", "Vorname", "Nachname", "Strasse", "Stadt", "TelefonNr"]

# StringVar zum Speichern des ausgewählten Filters erstellen
selected_filter = tk.StringVar(root)
selected_filter.set(filter_options[0])  # Standardfilteroption setzen
selected_filter.get()

# Dropdown-Menü erstellen
filter_menu = tk.OptionMenu(root, selected_filter, *filter_options, ) #command=filter_selected
filter_menu.config(bg="gray22", fg="gray76", bd=0, highlightthickness=1, highlightbackground="grey", activebackground="LightBlue3", width=20 )
filter_menu.grid(row=15, column=1, padx=10, pady=5, sticky="w")

# Liste der Filteroptionen "Sortieren" erstellen
sort_options = ["Aufsteigend", "Absteigend"]

# StringVar zum Speichern des ausgewählten Filters erstellen
selected_sort = tk.StringVar(root)
selected_sort.set(sort_options[0])  # Standardfilteroption setzen


# Dropdown-Menü erstellen Sortieren
sort_menu = tk.OptionMenu(root, selected_sort, *sort_options, ) #command=sort_selected
sort_menu.config(bg="gray22", fg="gray76", bd=0, highlightthickness=1, highlightbackground="grey", activebackground="LightBlue3", width=11)
sort_menu.grid(row=15, column=2, padx=0, pady=5, sticky="w")


# Widget zum Anzeigen aller Kontakte
listbox_all = tk.Listbox(root, background="lavender", foreground="gray13", font=('Helvetica 15') )
listbox_all.grid(row=17, column=0, columnspan=4, rowspan=4, padx=10, pady=10, sticky="nsew")
initialList=initialData()
for contact in initialList:
    listbox_all.insert("end", " "+contact[1]+", "+contact[2]+", "+contact[5]+" "+contact[6]
                       +", "+contact[3]+" "+contact[4]+", "+contact[7]+", "+contact[8]+", "+str(contact[0]))
listbox_all.bind('<<ListboxSelect>>', getListCollection)



# Button zum Speichern des ausgewählten Kontakts
save_button = tk.Button(root, text="Kontaktliste speichern", bg="gray22", fg="gray76", activebackground="LightBlue3", command=save_contact_clicked)
save_button.grid(row=21, column=3, sticky="e", padx=10, pady=5)

root.mainloop()
