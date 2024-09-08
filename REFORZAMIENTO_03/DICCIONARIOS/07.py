n = 4

diccionario = {}

for i in range(n):
    key = input("Ingrese un número: ")
    diccionario[key] = pow(int(key),3)

print(diccionario)