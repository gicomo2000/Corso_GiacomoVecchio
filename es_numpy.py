import numpy as np
arr=np.arange(10,50)
print(arr)
print(arr.dtype)
arr=np.array(arr,dtype="float64")
print(arr.dtype)
print(arr.shape)


arr1d=np.random.randint(10,50,20)
print(arr1d)
print(arr1d[:10])
print(arr1d[-5:])
print(arr1d[5:15])
print(arr1d[2::3])
arr1d[5:10]=99
print(arr1d)


arr2=np.linspace(0,1,12)
print(arr2)
re_arr2=arr2.reshape(3,4)
print(re_arr2)
casuali=np.random.rand(3,4)
print(casuali)

somma=re_arr2+casuali
print(somma)



arr3=np.linspace(0,10,50)
print(arr3)
arr4=np.random.random(50)
print(arr4)
somma=arr3+arr4
print(somma)
print("la somma è:", np.sum(somma))
somma=np.array(somma[somma>5])
print("la somma è:", np.sum(somma))



#ESERCIZIO FINALE 1
x=True

while x:
    dim=int(input("inserisci righe: "))
    dim2=int(input("inserisci colonne: "))
    arr5=np.random.randint(0,10,(dim,dim2))
    menu=int(input("cosa vuoi fare? 1)sottomatrice 2)trasposto 3)somma elementi 4)esci ->"))
    if menu==1:
        sotto_matrice = arr5[1:dim-1, 1:dim2-1]
        print(sotto_matrice)
        break
    elif menu==2:
        print(arr5.T)
        break
    elif menu==3:
        print("La somma degli elementi nella matrice è: ",np.sum(arr5))
        break
    else:
        print("Ciao!")
        break
