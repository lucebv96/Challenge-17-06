#Listas de claves y valores
claves = ['nombre', 'edad', 'ciudad', 'profesion']
valores = [] #Los valores seran ingresados por el usuario

# Ingreso de los valores dados por el usuario
for clave in claves:
    valor = input(f"Ingrese '{clave}': ")
    valores.append(valor)

#Inicialización de un diccionario vacío
diccionario = {}

#Verificación de que las listas tengan la misma longitud
if len(claves) == len(valores):
    # Iteración sobre el índice de las listas
    for i in range(len(claves)):
        # Asignación de cada par clave-valor al diccionario
        diccionario[claves[i]] = valores[i]
    # Mostrar el diccionario resultante
    print("El diccionario creado es:")
    print(diccionario)
else:
    # Mensaje de error si las listas no tienen la misma longitud
    print("Error: Las listas de claves y valores deben tener la misma longitud.")