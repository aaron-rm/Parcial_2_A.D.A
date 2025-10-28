
def leer_datos():

    return #dato

def menu():
    while True:
        print("Parcial 2 - Menú")
        print("  1) Rellenar datos")
        print("  2) ")
        print("  3) ")
        print("  4) ")
        print("  5) ")
        print("  6) Salir")
    
        try:
            opcion = int(input("\nSeleccione una opción (1-6): "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue  
        
        if opcion == 1:
            print("Ejecutando Algoritmo 1...")
        elif opcion == 2:
            print("Ejecutando Algoritmo 2...")
        elif opcion == 3:
            print("Ejecutando Algoritmo 3...")
        elif opcion == 4:
            print("Ejecutando Algoritmo 4...")
        elif opcion == 5:
            print("Ejecutando análisis empírico completo...")
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    
    
    input("\nPresione Enter para continuar...")
    
    
    
if __name__ == "__main__":
    menu()
    #funcion a ejecutar