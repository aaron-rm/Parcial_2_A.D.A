"""
Algoritmo base: Asignación de Rutas – Parte 1
Autor: Eliber Oropeza
Descripción: Crea un algoritmo que asigne puntos de entrega a cada conductor, 
asegurando que ningún punto se repita.
"""

def asignar_rutas(puntos, conductores):
    """
    Asigna puntos de entrega a cada conductor.
    
    Parámetros:
    puntos (list): Lista de puntos o direcciones a entregar.
    conductores (list): Lista de nombres o identificadores de conductores.
    
    Retorna:
    dict: Diccionario con el conductor como clave y lista de puntos asignados como valor.
    """
    asignaciones = {conductor: [] for conductor in conductores}
    num_conductores = len(conductores)

    for i, punto in enumerate(puntos):
        conductor_asignado = conductores[i % num_conductores]
        asignaciones[conductor_asignado].append(punto)
    
    return asignaciones


# Ejemplo de uso (puede eliminarse al integrar con el proyecto principal)
if __name__ == "__main__":
    puntos = ["Punto A", "Punto B", "Punto C", "Punto D", "Punto E"]
    conductores = ["Conductor 1", "Conductor 2"]
    resultado = asignar_rutas(puntos, conductores)
    for conductor, entregas in resultado.items():
        print(f"{conductor}: {entregas}")
