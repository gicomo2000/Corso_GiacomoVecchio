import math

class Punto:
    def __init__(self, x, y):
        self.x = x  
        self.y = y  

    def muovi(self, dx, dy):
    
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)


class Libro:
    def __init__(self, titolo,autore,pagine):
        self.titolo=titolo
        self.autore=autore
        self.pagine=pagine
    
    def descrizione(self):
        print("il libro è stato scritto da", self.autore, "si intitola", self.titolo, "ed ha", self.pagine, "pagine")

mio_libro=Libro("ciao","giacomo",23)
mio_libro.descrizione()