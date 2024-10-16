#Diccionarios ejercicio 3
print(" ")
print("Ordonez Martinez Valeria 3W 1203")
print(" ")
#Definir los elementos del diccionario
print("Frutas para comprar:")
frutas = {
    "manzana": "1.50",
    "pera": "2.00",
    "platano": "1.75",
    "uva": "1.00"
}
print(frutas) #Imprimir el diccionario
print(" ")

op = input("¿Qué fruta comprará? ").lower()  # Llamar funcion lower
if op in frutas: #Crear condicion si la opcion esta en las frtas
    kilos = float(input("¿Cuántos kilos se llevarán? ")) #Preguntar al usuario los kilos a llevar
    precio = kilos * float(frutas[op])  # Convertimos el precio a float
    print(f"El precio es: ${precio:.2f}")  # Formatear a dos decimales
else: #Codicion si la opcion no esta en el diccionario
    print("Esta fruta no está en el diccionario.")
