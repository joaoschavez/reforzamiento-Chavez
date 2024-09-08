
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

lista_alumnos = []

for i in range(cantidad_alumnos):
    alumno = input("Ingrese el nombre del alumno: ")
    lista_alumnos.append(alumno)

print("Los cantidad de alumnos es de {}".format(len(lista_alumnos)))
print("La lista de alumnos es la siguiente: {}".format(lista_alumnos))