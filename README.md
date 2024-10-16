# Practica_3_2do_Ordonez_Martinez_Valeria_1203_Direcciones_3W
Practica 3

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
![image](https://github.com/user-attachments/assets/d2de43dd-87ce-4c34-995b-17d597dcbb3c)
![image](https://github.com/user-attachments/assets/64b2b0f3-89c8-44dc-86d1-211d99caaeb0)

# Diccionarios ejercicio 2
print(" ")
print("Ordonez Martinez Valeria 3W 1203")
print(" ")
dic = dict() #Crear diccionario
print(dic) #Imprimir el diccionario
nombre = input("Introducir su nombre: ") #Solicitar que se introdusca el nombre
dic.setdefault("Nombre", nombre) #Asignar valor a la variable del nombre
print(" ")
edad = int(input("Ingrese su edad: ")) #Solicitar que se introdusca la edad
dic.setdefault("Edad", edad) #Asignar  valor a la variable de edad
print(" ")
direccion = input("Introducir su dirección: ") #Solicitar que se introdusca la direccion
dic.setdefault("Dirección", direccion) #Asignar valor a la direccion
print (" ")
telefono = input("Ingrese su número de teléfono: ") #Solicitar que se ingrese el numero de telefono
dic.setdefault("Teléfono", telefono) #Asignar valor a el telefono
print(" ")
#Imprimir el mensaje y usar f-string para mostrar la información del diccionario
print(f"{dic['Nombre']} tiene {dic['Edad']} años, vive en {dic['Dirección']} y su número de teléfono es {dic['Teléfono']}.")
print (" ")
![image](https://github.com/user-attachments/assets/51b16959-beff-418b-bdf7-2877b917403e)
![image](https://github.com/user-attachments/assets/6a6058fb-9863-416c-a290-ce7463390e78)

# Diccionarios ejercicio 3
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
![image](https://github.com/user-attachments/assets/2772b4e3-d87c-4840-bdd7-8f319300edbf)
![image](https://github.com/user-attachments/assets/625e770a-6f25-49ab-9482-95518380bec4)








