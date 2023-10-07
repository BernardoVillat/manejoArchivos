nombres = []

while True:
    nombre = input("Por favor ingrese un nombre (o 'q' para salir) ")
    if nombre.lower() == 'q':
        break
    nombres.append(nombre)

with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")
print("Los nombres se han guardado correctamente en el archivo 'nombres.txt'")

with open("nombres.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
