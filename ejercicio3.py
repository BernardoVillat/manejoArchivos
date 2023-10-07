try:
    with open("archivo_inexistente.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())
except FileNotFoundError:
    print("El archivo 'archivo_inexistente.txt' no fue encontrado.")
    