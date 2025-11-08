def leer_datos():
    while True:
        try:
            n = int(input("   Ingrese el numero total de puntos (incluyendo el deposito): "))
            cap = int(input("   Ingrese la capacidad maxima de paquetes por conductor: "))
            P = int(input("   Ingrese el total de paquetes a repartir: "))

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
    print("   A continuacion, ingrese las distancias en kilometros entre los puntos.")
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                print(f"      Distancia del punto {i} a si mismo = 0")
                fila.append(0)
            else:
                while True:
                    try:
                        distancia = int(input(f"      Ingrese la distancia entre el punto {i} y el punto {j} (en kilometros): "))
                        if(distancia<0):
                            print("         Error: La distancia no puede ser negativa. Intente de nuevo.\n")
                        else:
                            fila.append(distancia)
                            break
                    except ValueError:
                        print("         Error: Debe ingresar solo numeros enteros validos. Intente de nuevo.\n")
        matriz.append(fila)
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
    


