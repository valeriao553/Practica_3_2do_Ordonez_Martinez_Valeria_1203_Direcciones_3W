# Diccionarios ejercicio 1
print(" ")
print("Ordonez Martinez Valeria 3W 1203")
print(" ")
#Declarar el diccionario
thisdict = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}
#imprimir el diccionario
print(thisdict)
print(" ")
#Solicitar al usuario que ingrese la divisa
op = str(input("Ingrese la divisa para mostrar el símbolo: "))
op = op.title() #Convertir la primera letra a mayuscula
print(" ")
#Agregar condiccion si la divisa se encuentra en el diccionario
if op in thisdict:
    print("Su simbolo es:",thisdict[op])
else: #Mensaje no se encuentra en el diccionario
    print("Esta divisa no está en el diccionario")
