def area_triangolo(base,altezza):
    area=(base*altezza)/2
    return area
def area_quadrato(lato):
    area=lato*lato
    return area
def area_rettangolo(base, altezza):
    area=base*altezza
    return area
i=0
while i==0:
    forma=int(input("Di quale forma vuoi calcolare l'area: 1)triangolo 2)quadrato 3)rettangolo 4)esci ->"))
    if forma==1:
       base=int(input("Inserisci la base: "))
       altezza=int(input("Inserisci l'altezza: "))
       print(area_triangolo(base,altezza))
    elif forma==2:
        lato=int(input("Inserisci la lunghezza del lato: "))
        print(area_quadrato(lato))
    elif forma==3:
        base=int(input("Inserisci la base: "))
        altezza=int(input("Inserisci l'altezza: "))
        print(area_rettangolo(base,altezza))
    else:
        break
    continuare=input("Vuoi continuare? ")
    if continuare=="si":
        continue
    else:
        break