# Klasse für Laptops mit den Eigenschaften
#   - RAm Größe
#   - Marke
#   - Modell
#   -Bildschirmgröße

notebook_1_ram = 16
notebook_2_ram = 32

notebook_1_marke = "Apple"
notebook_2_marke = "Lenovo"

notebook_1_modell = "Macbook Air"
notebook_2_modell = "Thinkpad 14"

notebook_1_bildschirmgröße = 14.1
notebook_1_bildschirmgröße = 16

class Notebook: # class + Name -> legt neuen Bauplan an
    def __init__(self, ram, marke, modell, bildschirmgröße):
        self.ram = ram # Setze die Eigenschaft ram auf den Wert des Parammetes
        self.marke = marke
        self.marke = modell
        self.marke = bildschirmgröße
        print(f"Neues Noteook mit Marke: " + marke + " wurde erstellt")

nb_1 = Notebook(17, "Apple" , "Macbook Pro", 14.1)
        

    

    


