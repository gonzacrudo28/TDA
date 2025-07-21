def camino_minimo_bf(grafo, origen):
    dist = {}
    padre = {}
    for v in grafo:
        dist[v] = float("inf")
        padre[v] = None
    dist[origen] = 0
    aristas = grafo.obtener_aristas()
    for _ in range(len(grafo) - 1):
        for u, v, peso in aristas:
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                padre[v] = u
    for u, v, peso in aristas:
        if dist[u] + peso < dist[v]:
            return None  # Hay un ciclo negativo

    return padre, dist
