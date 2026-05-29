import random
def contar_multiplos_fila(fila):
    if len(fila) == 0:
        return 0
    if len(fila) == 1:
        return 1 if fila[0] % 5 == 0 or fila[0] % 7 == 0 else 0
    mitad = len(fila) // 2
    return contar_multiplos_fila(fila[:mitad]) + contar_multiplos_fila(fila[mitad:])
def contar_multiplos_matriz(matriz):
    if len(matriz) == 0:
        return 0
    if len(matriz) == 1:
        return contar_multiplos_fila(matriz[0])
    mitad = len(matriz) // 2
    return contar_multiplos_matriz(matriz[:mitad]) + contar_multiplos_matriz(matriz[mitad:])
try:
    n = int(input("ingrese el tamaño n para la matriz cuadrada (n x n): "))
except ValueError:
    print("ingrese un numero entero valido")
    n = 0
if n > 0:
    matriz = [[random.randint(99, 999) for _ in range(n)] for _ in range(n)]
    print(f"\nmatriz generada ({n}x{n}):")
    for fila in matriz:
        print(" ".join(str(num) for num in fila))
    total = contar_multiplos_matriz(matriz)
    print(f"\ncantidad de multiplos de 5 o 7: {total}")