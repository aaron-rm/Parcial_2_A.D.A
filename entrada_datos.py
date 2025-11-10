def leer_datos():
    while True:
        try:
            n_txt  = input("Ingrese el numero total de puntos (incluyendo el deposito): ").strip()
            cap_txt = input("Ingrese la capacidad maxima de paquetes por conductor: ").strip()
            P_txt   = input("Ingrese el total de paquetes a repartir: ").strip()

            # convierte
            n   = int(n_txt)
            cap = int(cap_txt)
            P   = int(P_txt)

            # valida reglas del problema -> si falla, lanza excepcion a proposito
            if n <= 1:
                raise ValueError("El numero de puntos debe ser mayor que 1.")
            if cap <= 0:
                raise ValueError("La capacidad debe ser positiva.")
            if P <= 0:
                raise ValueError("El total de paquetes debe ser positivo.")

            # si todo OK, rompe el while
            break

        except ValueError as e:
            # aqui llegan tanto errores de conversion como reglas violadas
            print(f"Error: {e} Intente de nuevo.\n")
            continue

    print("\nDatos ingresados correctamente:")
    print(f"→ Numero de puntos: {n}")
    print(f"→ Capacidad por conductor: {cap}")
    print(f"→ Total de paquetes: {P}\n")
    return n, cap, P

