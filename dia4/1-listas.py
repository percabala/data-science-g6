dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]

#mostrar info de la lista
print(dias[0])

#agregar elementos a lista
dias.append("sábado")
dias.append("domingo")

#eliminar elementos de la lista
dias.pop(2)
del dias[0:2]

#actualizar un valor de la lista
dias[-1] = "Lunes"

#mostrar todos los valores de la lista
for dia in dias:
    print(dia)
