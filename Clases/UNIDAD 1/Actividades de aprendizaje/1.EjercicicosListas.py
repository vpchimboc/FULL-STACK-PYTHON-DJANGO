###CURSO DE FUNDAMENTOS DE PYTHON
#1. Crear una lista de numeros del 1 al 5
lista_numeros = [1,2,3,4,5]
#2. Accede al elemto 3 de la lista:
print(lista_numeros[2])
#3. Modifica un elemento de la lista:
lista_numeros[3]=8
print(lista_numeros)
#4. Agrega el elemento 9 al final de la lista
lista_numeros.append(9)
#5. Eliminar el elemento 2 de la lista:
lista_numeros.remove(2)

#6. Recorrer una lista con un bucle for:
for e in lista_numeros:
    print(e)

#7. Ordenar una lista:
print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)

#8. Obtener la longitud de una lista:
print(len(lista_numeros))

#9. Comprobar si un elemento está en la lista:
print(5 in lista_numeros)

#10. presentar el numero minimo
print(min(lista_numeros))

#11. Presentar el numero maximo
print(max(lista_numeros))

#12. la suma de los elementos de la lista
print(sum(lista_numeros))