matriz = []
filas = 0
columnas = 0

def Size():
    global filas, columnas
    filas = int(input("Tamaño de filas: "))
    columnas = int(input("Tamaño de Columnas: "))

def ReadValue(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error. Verifique que el valor sea entero")

def AddElement():
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            dato = ReadValue(f"Valor ({i+1}, {j+1}): ")
            matriz[i].append(dato)


def menu():
    print("""
1. Asignar Tamaño
2. Agregar Elemento
3. Salir
""")
    op = ReadValue("Opcion: ")
    return op

def main():
    while True:
        op = menu()
        if op == 1:
            Size()
        elif op == 2:
            AddElement()
        elif op == 3:
            print("adios")
        break

main()