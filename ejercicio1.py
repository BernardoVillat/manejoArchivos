try:
    # Abre el archivo en modo lectura
    with open("archivo.txt", "r") as archivo:
        # Lee y muestra cada línea del archivo
        for linea in archivo:
            print(linea.strip())  # strip() elimina los caracteres de nueva línea y espacios en blanco extra al final de la línea
except FileNotFoundError:
    print("El archivo 'archivo.txt' no se encontró.")