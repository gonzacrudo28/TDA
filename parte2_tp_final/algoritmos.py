from graph import Graph
import copy
import random

def crear_grafo_inversores(inversores, incompatibilidades):
    grafo = Graph(directed=False)
    for inversor in inversores:
        grafo.add_vertex(inversor)
    
    for inversor, incompatibles in incompatibilidades.items():
        for incompatible in incompatibles:
            if incompatible in grafo.dict_graph:
                if not grafo.are_united(inversor, incompatible):  
                    grafo.add_edge(inversor, incompatible)
    
    return grafo
    

def grado(grafo, v):
    if v not in grafo.get_vertex():
        return 0
    return len(grafo.dict_graph[v])

def maximizar_dinero_inversores_greedy(grafo, aportes):
    grafo_copia = copy.deepcopy(grafo)
    vertices = grafo_copia.get_vertex()
    
    # Ordeno los vertices por grado descendente
    vertices.sort(key=lambda v: aportes[v]/(grado(grafo_copia, v) + 1), reverse=True)
    seleccionados = []
    total_dinero = 0

    # Por cada vertice lo agrego a seleccionados y borro los adyacentes
    for v in vertices:
        if v in grafo_copia.dict_graph:
            seleccionados.append(v)
            total_dinero += aportes[v]
            for w in list(grafo_copia.dict_graph[v]):
                if w in grafo_copia.dict_graph:
                    grafo_copia.delete_vertex(w)
    return seleccionados, total_dinero


# A partir de la solucion greedy, planteamos esta heuristica

def maximizar_dinero_inversores_heuristica(
    grafo,
    aportes: dict,
    ganancia_actual: int,
    solucion_actual: set,
    no_seleccionados: set
):

    mejoro = True
    while mejoro:
        mejoro = False
        # Recorremos cada par (s ∈ solucion_actual, t ∈ no_seleccionados)
        for s in list(solucion_actual):
            for t in list(no_seleccionados):
                # 1) t debe ser compatible con todos en solucion_actual \ {s}
                parcial = solucion_actual - {s}
                if any(grafo.are_united(t, u) for u in parcial):
                    continue
                # 2) calculamos ganancia si hacemos swap
                nueva_ganancia = ganancia_actual - aportes[s] + aportes[t]
                if nueva_ganancia > ganancia_actual:
                    # Aplicamos el intercambio
                    solucion_actual = parcial | {t}
                    no_seleccionados = (no_seleccionados - {t}) | {s}
                    ganancia_actual = nueva_ganancia
                    mejoro = True
                    break  # Reiniciamos búsqueda desde la nueva solución
            if mejoro:
                break
    return ganancia_actual, list(solucion_actual)

def maximizar_dinero_inversores_randomizado_grafo(grafo, aportes, iteraciones=1000):
    vertices = grafo.get_vertex()
    mejor_conjunto = set()
    mejor_total = 0

    for _ in range(iteraciones):
        nodos = list(vertices)
        # Mezclamos aleatoriamente el orden de los nodos
        random.shuffle(nodos)  
        conjunto_actual = set()

        # Intentamos agregar cada nodo si es compatible con los ya seleccionados
        for nodo in nodos:
            if all(vecino not in conjunto_actual for vecino in grafo.dict_graph[nodo]):
                conjunto_actual.add(nodo)

        total = sum(aportes[i] for i in conjunto_actual)
        # Si el conjunto actual es mejor, lo guardamos
        if total > mejor_total:
            mejor_total = total
            mejor_conjunto = conjunto_actual

    return list(mejor_conjunto), mejor_total




# Ejemplos de uso
if __name__ == "__main__":
    # ejemplo con 5 inversores

    print("Ejemplo de maximización de dinero de 5 inversores:")
    inversores = ['A', 'B', 'C', 'D', 'E']
    aportes = {'A': 100, 'B': 80, 'C': 70, 'D': 60, 'E': 50}
    incompatibilidades = {
        'A': ['C'],
        'B': ['A', 'D'],
        'C': ['B'],
        'D': ['E'],
        'E': []
    }
    # Creamos el grafo de inversores
    grafo = crear_grafo_inversores(inversores, incompatibilidades)

    # Solución con algortimo randomizado
    seleccionados, total_dinero = maximizar_dinero_inversores_randomizado_grafo(grafo, aportes, iteraciones=1000)
    print("Solución aleatoria:", seleccionados, "Total dinero:", total_dinero)

    # Aplicamos algoritmo greedy
    seleccionados, total_dinero = maximizar_dinero_inversores_greedy(grafo, aportes)
    print("Solución inicial (Greedy):", seleccionados, "Total dinero:", total_dinero)
    
    # Preparamos sets para la heurística
    solucion_actual = set(seleccionados)
    no_seleccionados = set(grafo.get_vertex()) - solucion_actual

    ganancia_actual = total_dinero
    ganancia_actual, solucion_final = maximizar_dinero_inversores_heuristica(
        grafo, aportes, ganancia_actual, solucion_actual, no_seleccionados
    )
    print("Solución final (Heurística):", solucion_final, "Total dinero:", ganancia_actual)


    print("\n")

    # 
    print("Ejemplo de maximización de dinero de 3 inversores donde solo el randomizado lllega al óptimo:")
    inversores = ['A', 'B', 'C']
    aportes = {'A': 8, 'B': 5, 'C': 5}
    incompatibilidades = {
        'A': ['B', 'C'],
        'B': [],
        'C': []
    }

    # Creamos el grafo de inversores
    grafo = crear_grafo_inversores(inversores, incompatibilidades)

    # Solución con algortimo randomizado
    seleccionados, total_dinero = maximizar_dinero_inversores_randomizado_grafo(grafo, aportes, iteraciones=1000)
    print("Solución aleatoria:", seleccionados, "Total dinero:", total_dinero)

    # Aplicamos algoritmo greedy
    seleccionados, total_dinero = maximizar_dinero_inversores_greedy(grafo, aportes)
    print("Solución inicial (Greedy):", seleccionados, "Total dinero:", total_dinero)

    # Preparamos sets para la heurística
    solucion_actual = set(seleccionados)
    no_seleccionados = set(grafo.get_vertex()) - solucion_actual

    ganancia_actual = total_dinero
    ganancia_actual, solucion_final = maximizar_dinero_inversores_heuristica(
        grafo, aportes, ganancia_actual, solucion_actual, no_seleccionados
    )

    print("Solución final (Heurística):", solucion_final, "Total dinero:", ganancia_actual)


    print("\n")

    # Ejemplo donde en cada instancia se seleccionan distintos inversores peero siempre se llega al óptimo
    print("Ejemplo de maximización de dinero de 4 inversores donde solo el greedy + heurística lllega al óptimo:")
    inversores = ['A', 'B', 'C', 'D']
    aportes = {'A': 10, 'B': 10, 'C': 10, 'D': 10}
    incompatibilidades = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B', 'D'],
        'D': ['C']
    }

    # Creamos el grafo de inversores
    grafo = crear_grafo_inversores(inversores, incompatibilidades)
    
    # Solución con algortimo randomizado
    seleccionados, total_dinero = maximizar_dinero_inversores_randomizado_grafo(grafo, aportes, iteraciones=1000)
    print("Solución aleatoria:", seleccionados, "Total dinero:", total_dinero)

    # Aplicamos algoritmo greedy
    seleccionados, total_dinero = maximizar_dinero_inversores_greedy(grafo, aportes)
    print("Solución inicial (Greedy):", seleccionados, "Total dinero:", total_dinero)

    # Preparamos sets para la heurística
    solucion_actual = set(seleccionados)
    no_seleccionados = set(grafo.get_vertex()) - solucion_actual
    
    ganancia_actual = total_dinero
    ganancia_actual, solucion_final = maximizar_dinero_inversores_heuristica(
        grafo, aportes, ganancia_actual, solucion_actual, no_seleccionados
    )
    print("Solución final (Heurística):", solucion_final, "Total dinero:", ganancia_actual)

    print("\n")


    # Ejemplo donde solo se hace una iteración y el randomizado puede no llegar al óptimo
    print("Ejemplo donde solo se hace una iteración y el randomizado puede no llegar al óptimo:")
    inversores = ['A', 'B', 'C']
    aportes = {'A': 8, 'B': 5, 'C': 5}
    incompatibilidades = {
        'A': ['B', 'C'],
        'B': [],
        'C': []
    }

    # Creamos el grafo de inversores
    grafo = crear_grafo_inversores(inversores, incompatibilidades)

    # Solución con algortimo randomizado
    seleccionados, total_dinero = maximizar_dinero_inversores_randomizado_grafo(grafo, aportes, iteraciones=1) # Solo una iteración
    print("Solución aleatoria:", seleccionados, "Total dinero:", total_dinero)

    # Aplicamos algoritmo greedy
    seleccionados, total_dinero = maximizar_dinero_inversores_greedy(grafo, aportes)
    print("Solución inicial (Greedy):", seleccionados, "Total dinero:", total_dinero)

    # Preparamos sets para la heurística
    solucion_actual = set(seleccionados)
    no_seleccionados = set(grafo.get_vertex()) - solucion_actual

    ganancia_actual = total_dinero
    ganancia_actual, solucion_final = maximizar_dinero_inversores_heuristica(
        grafo, aportes, ganancia_actual, solucion_actual, no_seleccionados
    )

    print("Solución final (Heurística):", solucion_final, "Total dinero:", ganancia_actual)
    





    

    

    