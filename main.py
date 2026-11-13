# main.py
# Programa principal - se ejecuta con: python main.py
# R1 - Grafo ponderado: O(V + E) al mostrar grados
from utilidades import mostrar_grados, bfs, reconstruir_camino, dijkstra

# R1 - Grafo ponderado propio, 7 ciudades
# Lista de adyacencia: clave = ciudad, valor = lista de tuplas (vecina, distancia_en_km)
grafo = {
    "Tonchigue": [("Atacames", 20), ("Muisne", 60)],
    "Atacames": [("Tonchigue", 20), ("Esmeraldas", 30)],
    "Esmeraldas": [("Atacames", 30), ("Quininde", 80), ("Muisne", 100)],
    "Muisne": [("Tonchigue", 60), ("Esmeraldas", 100), ("Quininde", 120), ("Pedernales", 70)],
    "Quininde": [("Esmeraldas", 80), ("Muisne", 120), ("Santo Domingo", 90)],
    "Santo Domingo": [("Quininde", 90), ("Pedernales", 110)],
    "Pedernales": [("Muisne", 70), ("Santo Domingo", 110)],
}

def main():
    while True:
        print("\n=== RED DE CIUDADES - ESMERALDAS ===")
        print("1. R1 - Ver grafo y grados")
        print("2. R2 - BFS desde una ciudad")
        print("3. R3 - Dijkstra desde una ciudad")
        print("4. R4 - Comparar BFS vs Dijkstra (Tonchigue -> Quininde)")
        print("5. Salir")
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            # R1 - Mostrar grafo y grados: O(V + E)
            print("\nGrafo:", grafo)
            mostrar_grados(grafo)

        elif opcion == "2":
            # R2 - BFS: O(V + E)
            origen = input("Ciudad origen (ej: Tonchigue): ")
            if origen not in grafo:
                print("Esa ciudad no existe en el grafo")
                continue
            visitado, padre = bfs(grafo, origen)
            print(f"\n--- R2: BFS desde {origen} ---")
            for ciudad, escalas in visitado.items():
                # Reconstruir camino: O(V) en el peor caso
                camino = " -> ".join(reconstruir_camino(padre, ciudad))
                print(f"{ciudad}: {escalas} escalas | Camino: {camino}")
            if len(visitado) == len(grafo):
                print("La red esta COMPLETAMENTE CONECTADA")
            else:
                aisladas = set(grafo) - set(visitado)
                print(f"Hay ciudades aisladas: {aisladas}")

        elif opcion == "3":
            # R3 - Dijkstra: O((V + E) log V)
            origen = input("Ciudad origen (ej: Tonchigue): ")
            if origen not in grafo:
                print("Esa ciudad no existe en el grafo")
                continue
            distancias, padre = dijkstra(grafo, origen)
            print(f"\n--- R3: Dijkstra desde {origen} ---")
            for ciudad, km in distancias.items():
                # Reconstruir camino: O(V) en el peor caso
                camino = " -> ".join(reconstruir_camino(padre, ciudad))
                print(f"{ciudad}: {km} km | Camino: {camino}")
            sin_origen = {c: d for c, d in distancias.items() if c != origen}
            cercana = min(sin_origen, key=sin_origen.get)
            lejana = max(sin_origen, key=sin_origen.get)
            print(f"\nMas cercana a {origen}: {cercana} ({sin_origen[cercana]} km)")
            print(f"Mas lejana a {origen}: {lejana} ({sin_origen[lejana]} km)")

        elif opcion == "4":
            # R4 - Comparacion: O(V + E) + O((V + E) log V) = O((V + E) log V)
            print("\n--- R4: COMPARACION Tonchigue -> Quininde ---")
            visitado, padre_bfs = bfs(grafo, "Tonchigue")
            camino_bfs = reconstruir_camino(padre_bfs, "Quininde")
            print(f"BFS (menos escalas): {' -> '.join(camino_bfs)} = {visitado['Quininde']} escalas")
            distancias, padre_dijk = dijkstra(grafo, "Tonchigue")
            camino_dijk = reconstruir_camino(padre_dijk, "Quininde")
            print(f"Dijkstra (menos km): {' -> '.join(camino_dijk)} = {distancias['Quininde']} km")
            print("\nEXPLICACION: No coinciden porque BFS minimiza el numero de saltos,")
            print("sin importar los km. Dijkstra minimiza la suma total de km,")
            print("aunque tenga mas escalas.")

        elif opcion == "5":
            print("Chao Vale!")
            break
        else:
            print("Opcion invalida, intenta de nuevo")

if __name__ == "__main__":
    main()