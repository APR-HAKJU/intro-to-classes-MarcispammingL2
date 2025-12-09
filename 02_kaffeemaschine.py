"""
Übung 2: Kaffeemaschine mit Parametern

Aufgabe:
Erstelle eine Klasse `Kaffeemaschine` mit:
- Konstruktor mit Parameter: wasserstand (in ml, z.B. 1000)
- Methode kaffee_machen(menge) mit Parameter:
  - Prüft, ob genug Wasser da ist
  - Wenn ja: Reduziert Wasserstand und gibt aus "☕ Kaffee gemacht! X ml"
  - Wenn nein: Gibt aus "❌ Nicht genug Wasser! Bitte nachfüllen."
- Methode wasser_nachfuellen(menge) mit Parameter: Erhöht den Wasserstand
- Methode zeige_status() ohne Parameter: Zeigt aktuellen Wasserstand

Erstelle eine Kaffeemaschine mit 500ml Wasser, mache 2x Kaffee (je 200ml),
versuche es nochmal (es sollte dieses Mal fehlschlagen), fülle Wasser nach und mache nochmal Kaffee.

💡 Tipps:
- Verwende if self.wasserstand >= menge: um zu prüfen
- self.wasserstand -= menge verringert den Wasserstand
- self.wasserstand += menge erhöht den Wasserstand

Erwartetes Ergebnis:
Wasserstand: 500 ml
☕ Kaffee gemacht! 200 ml
☕ Kaffee gemacht! 200 ml
❌ Nicht genug Wasser! Bitte nachfüllen.
💧 500 ml Wasser nachgefüllt
☕ Kaffee gemacht! 200 ml
Wasserstand: 400 ml
"""

# TODO: Erstelle hier die Klasse Kaffeemaschine
class Kaffeemaschine:
    def __init__(self, wasserstand):
        self.wasserstand = wasserstand
        print("Neue Kaffeemaschine wurde erstellt")
        
    def kaffee_machen(self, menge):
        if menge > self.wasserstand:
            print("Nicht genug Wasser!>:(")
        else:
            print("Kaffee wird gemacht:)")
            self.wasserstand = self.wasserstand - menge
            print(f"Neuer Wasserstand: {self.wasserstand}")

    def zeie_info(self):
        print(f"Aktueller Wasserstand: {self.wasserstand}")

    def wasser_nachfüllen(self, menge):
        self.wasserstand += menge



# TODO: Erstelle eine Kaffeemaschine mit 500ml Wasser
Kaffeemaschine1 = Kaffeemaschine(wasserstand = 500)
Kaffeemaschine1.kaffee_machen(menge= 100)

# TODO: Zeige den Status
Kaffeemaschine1.wasser_nachfüllen(500)
Kaffeemaschine1.kaffee_machen(200)
Kaffeemaschine1.kaffee_machen(50)
Kaffeemaschine1.kaffee_machen(1000)

Kaffeemaschine2 = Kaffeemaschine(10000)
Kaffeemaschine1.kaffee_machen(1000)


# TODO: Mache 2x Kaffee mit je 200ml
Kaffeemaschine1 = Kaffeemaschine(wasserstand = 200)

Kaffeemaschine1 = Kaffeemaschine(wasserstand = 200)


# TODO: Versuche nochmal Kaffee zu machen (sollte fehlschlagen)


# TODO: Fülle 500ml Wasser nach


# TODO: Mache nochmal Kaffee mit 200ml


# TODO: Zeige den Status erneut