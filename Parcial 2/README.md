# Parcial_2_A.D.A

## Descripción del problema 
Una empresa de mensajería necesita asignar rutas diarias a sus conductores para entregar paquetes en distintos puntos de la ciudad. Cada conductor tiene una capacidad máxima de paquetes y cada punto de entrega tiene un tiempo estimado de llegada. Se requiere desarrollar un algoritmo que asigne rutas de entrega válidas con base en la capacidad y distancia entre puntos, intentando minimizar el tiempo total de recorrido. Este problema se puede considerar una simplificación del problema de ruteo de vehículos (VRP), pero sin aplicar búsqueda exhaustiva ni algoritmos de optimización clásicos. 

### Requisitos funcionales 
 1. El usuario ingresa: 
- [x] Número de puntos de entrega (n) 
- [x] Distancia entre los puntos (matriz n×n) 
- [x] Capacidad máxima de paquetes por conductor 
- [x] Cantidad total de paquetes a distribuir 
 2. El programa debe: 
- [x] Asignar rutas válidas a cada conductor según su capacidad. 
- [x] Calcular el tiempo estimado total para todas las rutas. 
- [x] Mostrar las rutas y sus métricas (distancia total, paquetes transportados, tiempo). 