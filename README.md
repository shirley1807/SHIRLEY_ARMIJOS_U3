# Algoritmos y Estructuras de Datos - Unidad 3
## Red de Ciudades - Esmeraldas

### Como ejecutar
python main.py

### Archivos
- main.py: Menu principal, grafo y comparacion R4
- utilidades.py: mostrar_grados, bfs, reconstruir_camino, dijkstra

### Grafo - 7 ciudades
Tonchigue, Atacames, Esmeraldas, Muisne, Quininde, Santo Domingo, Pedernales

### Requerimientos
- R1: Grafo ponderado con lista de adyacencia. Grado de cada ciudad.
- R2: BFS desde una ciudad. Muestra escalas, camino y conectividad.
- R3: Dijkstra desde una ciudad. Muestra km, camino, mas cercana y mas lejana.
- R4: Comparacion Tonchigue -> Quininde. BFS = 2 escalas (180 km). Dijkstra = 130 km (3 escalas).

### Complejidades
- R1 Mostrar grados: O(V + E)
- R2 BFS: O(V + E)
- R3 Dijkstra: O((V + E) log V)
- Reconstruir camino: O(V)
- R4 Comparacion: O((V + E) log V)

### R4 Explicacion
BFS minimiza escalas, Dijkstra minimiza km. Por eso no coinciden: el camino con menos escalas usa carreteras largas (Tonchigue-Muisne 60 + Muisne-Quininde 120 = 180 km), mientras el de menos km usa mas escalas pero carreteras cortas (20 + 30 + 80 = 130 km).
