from typing import List
import re

import random

def leer_datos():
    while True:
        try:
            n = int(input("   Ingrese el numero total de puntos (incluyendo el deposito): "))
            cap = int(input("   Ingrese la capacidad maxima de paquetes por conductor: "))
            P = int(input("   Ingrese el total de paquetes a repartir: "))

            # convierte
            n   = int(n_txt)
            cap = int(cap_txt)
            P   = int(P_txt)

            # valida reglas del problema -> si falla, lanza excepcion a proposito
            if n <= 1:
                print("   El numero de puntos debe ser mayor que 1.")
                continue
            if cap <= 0:
                print("   La capacidad debe ser positiva.")
                continue
            if P <= 0:
                print("   El total de paquetes debe ser positivo.")
                continue
            break

        except ValueError:
            print("      Error: Debe ingresar solo numeros enteros validos. Intente de nuevo.\n")

    print(f"\n   Datos ingresados correctamente:")
    print(f"   → Numero de puntos: {n}")
    print(f"   → Capacidad por conductor: {cap}")
    print(f"   → Total de paquetes: {P}\n")

    return n, cap, P

def leer_matriz_distancias(n):
    print("   A continuacion, ingrese las distancias en kilometros entre los puntos (solo la mitad superior).")
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            while True:
                try:
                    distancia = float(input(f"      Distancia entre punto {i} y punto {j}: "))
                    if distancia < 0:
                        print("         Error: La distancia no puede ser negativa. Intente de nuevo.\n")
                    else:
                        matriz[i][j] = distancia
                        matriz[j][i] = distancia
                        break
                except ValueError:
                    print("         Error: Debe ingresar un numero válido.\n")
    return matriz

def generar_matriz_aleatoria(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            valor = random.randint(0, 100)
            matriz[i][j] = valor
            matriz[j][i] = valor
    return matriz

def mostrar_matriz(matriz):
    n = len(matriz)
    print("\n   De/A |", end="")
    for j in range(n):
        print(f"     {j:3}", end="")
    print("\n   " + "-" * (20 + 4 * n))
    for i in range(n):
        print(f"     {i:2} |", end="")
        for j in range(n):
            print(f"     {matriz[i][j]:3}", end="")
        print()

# K
