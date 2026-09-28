matriz = []
fila = 0
columnas = 0

def pedirTamaño(i, j):
    global filas, columnas
    filas = i
    columnas = j


def leerValor(mensaje):
    while True:
        try:
            valor = int(input("Dime un valor númerico: "))
            return valor
        except ValueError:
            print("Error. Verifique que el valor sea entero")

def agregarElemento():
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(int(input(f"Valor ({i}, {j}): ")))

pedirTamaño(2, 2)
print(filas, columnas)
agregarElemento()

def menu():
    print("""
1. Asignar tamano
2. Agregar elemento
3. Salir
""")
    op = leerValor("Opcion:")
    return op
def main():
    while True:
        op = menu()
        if op == 1:
            pedirTamaño()
        elif op == 2:
            agregarElemento()
        elif op == 3:
            print("see yaa....")
            break
        
