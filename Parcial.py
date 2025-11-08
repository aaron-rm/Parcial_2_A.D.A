#Emily Bonilla 
# Entrada de Datos – Parte 1 (Interfaz y validaciones) 
# Diseñar la función principal leer_datos() que pida al usuario el número de puntos, la capacidad 
# y el total de paquetes. Validar que los datos sean correctos y convertirlos a enteros. 


#Jaziel Gonzalez 
# Entrada de Datos – Parte 2 (Carga de matriz) 
# Implementar la lectura o generación inicial de la matriz de distancias. 
# Validar que sea cuadrada (n×n) y con ceros en la diagonal. 


#Kenny Herrera 
# Verificador de Matriz de Distancias 
# Presentar la tabla a conductores y permite modificarla. 


#Walter Gonzalez 
# Distribución de Paquetes por Conductor 
# Crear una función asignar_paquetes() que divida los paquetes entre conductores según la capacidad máxima. 
# Si sobran paquetes, asignarlos al último conductor disponible. 


#Eliber Oropeza 
# Asignación de Rutas – Parte 1 (Diseño del recorrido)
# Crear el algoritmo base para asignar puntos de entrega a cada conductor. Asegurarse de no repetir puntos. 


#Aaron Remarchuk 
# Asignación de Rutas – Parte 2 (Optimización simple) 
# Mejorar el recorrido del punto 5 con una lógica más eficiente. Sin usar algoritmos de optimización externos. 


#Kahil Reyna 
# Cálculo de Métricas (distancia y tiempo) 
# Crear funciones para calcular la distancia total de cada ruta, 
# el tiempo total de recorrido y el promedio por conductor. Generar un resumen global. 


#Mijael Vallejos 
# Visualización de Resultados 
# Mostrar en pantalla las rutas con formato ordenado: 
# conductor, puntos recorridos, distancia total, paquetes transportados y tiempo estimado. 

import entrada_datos

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
    entrada_datos.leer_datos()
    menu()
    #funcion a ejecutar