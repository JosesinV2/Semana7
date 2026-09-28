matriz = []
fila = 0
columnas = 0

def pedirTamaño(i, j):
    global filas, columnas
    filas = i
    columnas = j


def leerValor():
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