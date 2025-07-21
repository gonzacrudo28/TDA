heapq = 0
def dijkstra(grafo, origen):
    dist = {}
    padre = {}
    for v in grafo:
        dist[v] = float("inf")
    dist[origen] = 0
    padre[origen] = None
    q = heapq.crear() 
    q.encolar(origen, 0)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.ady(v):
            if dist[v] + grafo.peso_union(v,w) < dist[w]:
                dist[w] = dist[v] + grafo.peso_union(v,w)
                padre[w] = v
                q.encolar(w, dist[w])
    return padre, dist
#O((V+E) log V)