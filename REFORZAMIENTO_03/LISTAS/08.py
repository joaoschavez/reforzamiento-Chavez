lista = []
n = 10


for i in range(1,n+1):
    dato_lista = int(input("Ingrese un número para la lista: "))
    lista.append(dato_lista)

print(sum(lista))

print(sum(lista)/len(lista))