def kruskal(grafo):
    conjuntos = UnionFind(grafo.obtener_vertices())
    aristas = sort(obtener_aristas(grafo))
    arbol = grafo_crear(grafo.obtener_vertices())
    for a in aristas:
        v, w, peso = a
        if conjuntos.find(v) == conjuntos.find(w):
            continue #Ya estan en la misma comp conexa
        arbol.agregar_arista(v, w, peso)
        conjuntos.union(v,w)
    return arbol
#O(E LOG E)
