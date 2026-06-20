def imprimir_laberinto(matriz):
    for fila in matriz:
        print("\t".join(str(celda) for celda in fila))
    print("-" * 55)

def resolver_laberinto(matriz, x, y, vidas):
    filas = len(matriz)
    columnas = len(matriz[0])

    if x < 0 or x >= filas or y < 0 or y >= columnas:
        return False
    valor_celda = matriz[x][y]
    if valor_celda == 0 or valor_celda == '*':
        return False
    vidas_actuales = vidas
    if valor_celda == -1:
        vidas_actuales -= 1
    elif valor_celda == -2:
        vidas_actuales -= 2
    if vidas_actuales <= 0:
        return False
    if valor_celda == 'F':
        matriz[x][y] = 'F' 
        return True
    temp = matriz[x][y] 
    if temp != 'I':
        matriz[x][y] = '*' 
    print(f"Avanzando a posición ({x}, {y}) | Vidas restantes: {vidas_actuales}")
    imprimir_laberinto(matriz)
    input("presione Enter para ver el siguiente movimiento...") 
    movimientos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for mov_x, mov_y in movimientos:
        if resolver_laberinto(matriz, x + mov_x, y + mov_y, vidas_actuales):
            return True
    print(f"Retrocediendo desde ({x}, {y})...")
    matriz[x][y] = temp
    return False
laberinto_original = [
    ['F',  1,  1,  1,  0,  1,  1,  1,  1],
    [ -2,  0,  0, -1,  0,  1,  0,  1,  0],
    [  1,  1,  0,  1,  1,  1,  0,  1,  0],
    [  0,  1,  0, -1,  0,  0,  0, -1,  0],
    [  1,  1,  1,  1,  1,  1,  1,  1,  0],
    [ -1,  0,  0,  0,  0,  0,  0,  1,  1],
    [  1,  1,  1,  1, -1,  1,  1,  1,  0],
    [  1,  0,  0,  1,  0,  1,  0,  1,  0],
    ['I',  1, -1,  1,  1,  1,  0,  1,  1]
]
print("Laberinto Original:")
imprimir_laberinto(laberinto_original)
laberinto_resolviendo = []
for fila in laberinto_original:
    laberinto_resolviendo.append(fila[:])
print("Iniciando búsqueda...\n")
logro_salir = resolver_laberinto(laberinto_resolviendo, 8, 0, 3)
if logro_salir:
    print("\nResultado el ratón ha logrado salir del laberinto")
    print("Matriz final indicando el camino de salida marcado con '*':")
    imprimir_laberinto(laberinto_resolviendo)
