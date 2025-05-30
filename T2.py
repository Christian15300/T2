import random
def generar_coordenadas(cantidad):
    coordenadas = []
    for i in range(cantidad):
        x = random.randint(-81, 81)
        y = random.randint(-81, 81)
        coordenadas.append([x, y])
    return coordenadas
def calcular_distancia(x, y):
    return (x * x + y * y) ** 0.5
def encontrar_mas_alejada(lista):
    if len(lista) == 0:
        return None
    if len(lista) == 1:
        x, y = lista[0]
        if x > 0 and y < 0:
            return lista[0]
        else:
            return None

    mitad = len(lista) // 2
    lado_izquierdo = encontrar_mas_alejada(lista[:mitad])
    lado_derecho = encontrar_mas_alejada(lista[mitad:])

    if lado_izquierdo is None:
        return lado_derecho
    if lado_derecho is None:
        return lado_izquierdo

    distancia_izq = calcular_distancia(lado_izquierdo[0], lado_izquierdo[1])
    distancia_der = calcular_distancia(lado_derecho[0], lado_derecho[1])

    if distancia_izq > distancia_der:
        return lado_izquierdo
    else:
        return lado_derecho
def main():
    cantidad = int(input("¿Cuántas coordenadas deseas generar?: "))
    matriz = generar_coordenadas(cantidad)

    print("\nCoordenadas generadas:")
    for par in matriz:
        print(par)

    resultado = encontrar_mas_alejada(matriz)

    if resultado:
        distancia = calcular_distancia(resultado[0], resultado[1])
        print("\nCoordenada más alejada con X > 0 e Y < 0:", resultado)
        print("Distancia al origen: {:.2f}".format(distancia))
    else:
        print("\nNo se encontró ninguna coordenada con X > 0 e Y < 0.")

main()