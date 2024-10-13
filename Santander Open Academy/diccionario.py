
User={"persona:" "Emmanuel", "edad:" "21", "ciudad:" "CDMX", "hobby:" "futbol", "carrera:" "ingenieria" }
#keys(): devuelve una vista de todas las claves del diccionario.
#values(): devuelve una vista de todos los valores del diccionario.
#items(): devuelve una vista de todos los pares clave-valor del diccionario.
#update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario


print(User.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(User.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(User.items())