n1=int(input("inserisci il primo numero: "))
n2=int(input("inserisci il secondo numero: "))
operatore=input("seleziona l'operazione da effettuare: 1)addizione 2)sottrazione 3)moltiplicazione 4)divisione": )

if operatore==1:
    print(n1+n2)
elif operatore==2:
    print(n1-n2)
elif operatore==3:
    print(n1*n2)
elif operatore==4:
    if n2==0:
        print("non è possibile dividere per 0")
    else:
        print(n1/n2)
else:
    print("operazione non consentita")