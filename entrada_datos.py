def leer_datos():
    while True:
        try:
            n = int(input("Ingrese el numero total de puntos (incluyendo el deposito): "))
            cap = int(input("Ingrese la capacidad maxima de paquetes por conductor: "))
            P = int(input("Ingrese el total de paquetes a repartir: "))

            if n <= 1:
                print("El numero de puntos debe ser mayor que 1.")
                continue
            if cap <= 0:
                print("La capacidad debe ser positiva.")
                continue
            if P <= 0:
                print("El total de paquetes debe ser positivo.")
                continue

            break

        except ValueError:
            print("Error: Debe ingresar solo numeros enteros validos. Intente de nuevo.\n")

    print(f"\nDatos ingresados correctamente:")
    print(f"→ Numero de puntos: {n}")
    print(f"→ Capacidad por conductor: {cap}")
    print(f"→ Total de paquetes: {P}\n")

    return n, cap, P
