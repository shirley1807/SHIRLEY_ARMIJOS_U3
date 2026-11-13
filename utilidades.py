# utilidades.py
# Solo estructuras nativas de Python: dict, list, tuple
from collections import deque
import heapq

def mostrar_grados(grafo):
    # R1 - Complejidad: O(V + E)
    # V = ciudades, E = carreteras
    print("\n--- R1: GRADO DE CADA CIUDAD ---")
    for ciudad, vecinos in grafo.items():
        # len(vecinos) es el grado
        nombres = [v[0] for v in vecinos]
        print(f"{ciudad}: grado {len(vecinos)} -> conecta con {nombres}")

def bfs(grafo, origen):
    # R2 - Recorrido BFS - Complejidad: O(V + E)
    # Devuelve: {ciudad: escalas desde origen} y {ciudad: ciudad anterior}
    visitado = {origen: 0}
    padre = {origen: None}
    cola = deque([origen])

    while cola:
        actual = cola.popleft()
        for vecina, _distancia in grafo[actual]:
            if vecina not in visitado:
                visitado[vecina] = visitado[actual] + 1
                padre[vecina] = actual
                cola.append(vecina)
    return visitado, padre

def reconstruir_camino(padre, destino):
    # Reconstruir ruta - Complejidad: O(V) en el peor caso
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = padre.get(actual)
    return list(reversed(camino))

def dijkstra(grafo, origen):
    # R3 - Código entregado por el docente al final del enunciado
    # Aquí solo se integra y se usa, no se programa desde cero
    # Complejidad: O((V + E) log V) por el uso de heap
    distancias = {ciudad: float('inf') for ciudad in grafo}
    distancias[origen] = 0
    padre = {origen: None}
    cola = [(0, origen)]  # (distancia acumulada, ciudad)

    while cola:
        dist_actual, actual = heapq.heappop(cola)
        if dist_actual > distancias[actual]:
            continue
        for vecina, peso in grafo[actual]:
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecina]:
                distancias[vecina] = nueva_dist
                padre[vecina] = actual
                heapq.heappush(cola, (nueva_dist, vecina))
    return distancias, padre