# TODO: 
# Aufgabe 1:
"""Erstelle eine Klasse Buch mit folgenden Attributen:

- titel
- autor
- seiten
- gelesen (Boolean )

Erstelle zwei Bücher: Eines, das du gelesen hast (setze gelesen=True), 
und eines, das du noch nicht gelesen hast.
"""

# TODO: Aufgabe 2:
# Gib für jedes Buch eine Nachricht aus, die angibt, ob du das Buch gelesen hast oder nicht.

class Buch:
    def __init__(self, titel):
        self.titel = self.titel
        self.actor = self.actor
        self.seiten = self.seiten
        self.gelesen = self.gelesen
        print("Neues Buch wurde erstellt")
    
buch_1 = Buch(titel = "Harry Potter",actor = "Jacky Rolling", seiten = 300, gelesen = True)
buch_2 = Buch(titel = "Niebelungenlied",actor = "Horst Unteregger", seiten = 150, gelesen = False)
buch_3 = Buch("Die drei Fragezeichen", "Horst Unteregger", 100, True)

print(f"{buch_1.title} wurd gelesen:{buch_1.gelesen}")
print(f"{buch_2.title} wurd gelesen:{buch_2.gelesen}")
print(f"{buch_3.title} wurd gelesen:{buch_3.gelesen}")