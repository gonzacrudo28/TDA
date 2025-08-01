from graph import Graph
import copy
import random

def crear_grafo_inversores(inversores, incompatibilidades):
    """
    Crea un grafo donde los nodos son inversores y las aristas representan
    incompatibilidades entre ellos.

    Parámetros:
    - inversores: lista de nombres de inversores
    - incompatibilidades: diccionario donde las claves son nombres de inversores
        y los valores son listas de nombres de inversores incompatibles con la clave.
        La relacion es bidireccional.
    Devuelve:
    - grafo: instancia de Graph con los nodos y aristas correspondientes.
    """
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
    
    # Ordenar los vertices por grado descendente
    vertices.sort(key=lambda v: aportes[v]/(grado(grafo_copia, v) + 1), reverse=True)
    seleccionados = []
    total_dinero = 0

    # Por cada vertice lo agrego a seleccionados y borro los adyacentes
    for v in vertices:
        if v in grafo_copia.dict_graph:
            seleccionados.append(v)
            total_dinero += aportes[v]
            # Eliminar adyacentes
            for w in list(grafo_copia.dict_graph[v]):
                if w in grafo_copia.dict_graph:
                    grafo_copia.delete_vertex(w)
    return seleccionados, total_dinero


# A partir de la solucion greedy, planteo esta heuristica

def maximizar_dinero_inversores_heuristica(
    grafo,
    aportes: dict,
    ganancia_actual: int,
    solucion_actual: set,
    no_seleccionados: set
):
    """
    Mejora la solución actual por Hill Climbing: intenta intercambiar un inversor
    seleccionado por uno no seleccionado si el nuevo aporta más y no genera conflictos.

    Parámetros:
    - grafo: instancia de Graph con método are_united(v, w)  
    - aportes: dict {nodo: aporte_monetario}  
    - ganancia_actual: suma de aportes de solucion_actual  
    - solucion_actual: set de nodos seleccionados  
    - no_seleccionados: set de nodos no seleccionados  

    Devuelve:
    - ganancia_actual: nueva ganancia tras mejoras  
    - solucion_actual: set actualizado de nodos seleccionados  
    - no_seleccionados: set actualizado de nodos no seleccionados
    """
    mejoró = True
    while mejoró:
        mejoró = False
        # Recorremos cada par (s ∈ solucion_actual, t ∈ no_seleccionados)
        for s in list(solucion_actual):
            for t in list(no_seleccionados):
                # 1) t debe ser compatible con todos en solucion_actual \ {s}
                parcial = solucion_actual - {s}
                if any(grafo.are_united(t, u) for u in parcial):
                    continue
                # 2) calcular ganancia si hacemos swap
                nueva_ganancia = ganancia_actual - aportes[s] + aportes[t]
                if nueva_ganancia > ganancia_actual:
                    # aplicamos el intercambio
                    solucion_actual = parcial | {t}
                    no_seleccionados = (no_seleccionados - {t}) | {s}
                    ganancia_actual = nueva_ganancia
                    mejoró = True
                    break  # reiniciamos búsqueda desde la nueva solución
            if mejoró:
                break
    return ganancia_actual, solucion_actual

def maximizar_dinero_inversores_randomizado_grafo(grafo, aportes, iteraciones=1000):
    """
    Algoritmo randomizado para seleccionar un conjunto independiente de nodos (inversores)
    maximizando el aporte total, usando la estructura de grafo.

    Parámetros:
    - grafo: instancia de Graph (no dirigido), con método get_vertex() y dict_graph
    - aportes: dict {nodo: aporte_monetario}
    - iteraciones: cantidad de iteraciones aleatorias

    Devuelve:
    - mejor_conjunto: set de nodos seleccionados
    - mejor_total: suma de aportes de los seleccionados
    """
    vertices = grafo.get_vertex()
    mejor_conjunto = set()
    mejor_total = 0

    for _ in range(iteraciones):
        nodos = list(vertices)
        random.shuffle(nodos)
        conjunto_actual = set()

        for nodo in nodos:
            if all(vecino not in conjunto_actual for vecino in grafo.dict_graph[nodo]):
                conjunto_actual.add(nodo)

        total = sum(aportes[i] for i in conjunto_actual)
        if total > mejor_total:
            mejor_total = total
            mejor_conjunto = conjunto_actual

    return list(mejor_conjunto), mejor_total


def maximizar_dinero_inversores(inversores, incompatibilidades, aportes):
    """
    Maximiza el dinero de los inversores aplicando un algoritmo greedy seguido
    de una mejora heurística.

    Parámetros:
    - inversores: lista de nombres de inversores
    - incompatibilidades: diccionario de incompatibilidades entre inversores
    - aportes: diccionario {inversor: aporte_monetario}

    Devuelve:
    - seleccionados: lista de inversores seleccionados
    - total_dinero: suma total de aportes de los inversores seleccionados
    """
    grafo = crear_grafo_inversores(inversores, incompatibilidades)

    # Solución con algortimo randomizado
    seleccionados, total_dinero = maximizar_dinero_inversores_randomizado_grafo(grafo, aportes, iteraciones=1000)

    print("Solución aleatoria:", seleccionados, "Total dinero:", total_dinero)
    
    # Aplicar algoritmo greedy
    seleccionados, total_dinero = maximizar_dinero_inversores_greedy(grafo, aportes)
    print("Solución inicial (Greedy):", seleccionados, "Total dinero:", total_dinero)
    
    # Preparar sets para la heurística
    solucion_actual = set(seleccionados)
    no_seleccionados = set(grafo.get_vertex()) - solucion_actual
    
    # Aplicar heurística para mejorar la solución
    total_dinero, solucion_actual = maximizar_dinero_inversores_heuristica(
        grafo, aportes, total_dinero, solucion_actual, no_seleccionados
    )
    
    return list(solucion_actual), total_dinero

# ejemplo de uso
if __name__ == "__main__":
    """Supongamos tres inversores:
    A, con un aporte de 8.
    B, con un aporte de 5.
    C, con un aporte de 5.
    Las incompatibilidades son: A es incompatible tanto con B como con C (pero B y C son compatibles entre sí).
    """
    inversores = ['A', 'B', 'C', 'D', 'E']
    aportes = {'A': 100, 'B': 80, 'C': 70, 'D': 60, 'E': 50}
    incompatibilidades = {
        'A': ['C'],
        'B': ['A', 'D'],
        'C': ['B'],
        'D': ['E'],
        'E': []
    }
    
    seleccionados, total_dinero = maximizar_dinero_inversores(inversores, incompatibilidades, aportes)
    print("Inversores seleccionados:", seleccionados)
    print("Total dinero:", total_dinero)
    

    

    