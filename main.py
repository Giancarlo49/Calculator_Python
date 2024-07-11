import tkinter as tk

# Definiert eine Funktion, um Zahlen und Operatoren in das Eingabefeld einzufügen.
def click_button(value):
    current = display.get()  # Aktuellen Wert aus dem Display holen
    display.delete(0, tk.END)  # Aktuellen Inhalt des Displays löschen
    display.insert(0, current + value)  # Geklickten Wert zum bestehenden Wert hinzufügen

# Definiert eine Funktion zum Löschen des Inhalts im Display.
def clear():
    display.delete(0, tk.END)  # Löscht den gesamten Inhalt des Displays

# Definiert eine Funktion, um die im Display eingegebenen mathematischen Ausdrücke zu berechnen.
def calculate():
    try:
        result = str(eval(display.get()))  # Versucht, den Ausdruck auszuwerten und das Ergebnis in einen String umzuwandeln
        display.delete(0, tk.END)  # Löscht das Display
        display.insert(0, result)  # Zeigt das Ergebnis der Berechnung an
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")  # Zeigt "Error" an, wenn ein Fehler bei der Berechnung auftritt

# Erstellt das Hauptfenster für den Taschenrechner.
root = tk.Tk()
root.title("Einfacher Taschenrechner")

# Erstellt ein Eingabefeld, wo Zahlen und Ergebnisse angezeigt werden.
display = tk.Entry(root, width=40, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Platziert das Eingabefeld im Fenster

# Liste der Buttons für den Taschenrechner, jeweils mit dem anzuzeigenden Text und ihrer Position.
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 0), ('=', 4, 2)
]

# Erstellt Buttons im Fenster und weist ihnen Funktionen zu.
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=10, height=3, command=calculate).grid(row=row, column=col)  # Berechnungsbutton
    elif text == 'C':
        tk.Button(root, text=text, width=10, height=3, command=clear).grid(row=row, column=col)  # Löschen-Button
    else:
        # Erstellt einen Button für jede Zahl oder jeden Operator und bindet die click_button-Funktion
        tk.Button(root, text=text, width=10, height=3, command=lambda text=text: click_button(text)).grid(row=row, column=col)

# Startet die Tkinter-Event-Schleife, hält das Fenster offen.
root.mainloop()
