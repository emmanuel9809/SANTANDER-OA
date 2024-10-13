frutas = ["manzana", "banana", "naranja"]


frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]


fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"


frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

#append(elemento): agrega un elemento al final de la lista.
#insert(indice, elemento): inserta un elemento en una posición específica de la lista.
#remove(elemento): elimina la primera aparición de un elemento en la lista.
#pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
#sort(): ordena los elementos de la lista en orden ascendente.
#reverse(): invierte el orden de los elementos en la lista.