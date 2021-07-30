lista=[letra for letra in 'casa']
print(lista)

#comprension de numeros
lista1=[numero**2 for numero in range(0,11)]
print (lista1)


lista3=[numero for numero in range(0,11) if numero % 2==0]
print(lista3)


lista4=[numero for numero in [numero **2 for numero in range(0,11)]if numero %2==0]
print(lista4)
