import random

def randomized_independent_set(pesos, adyacencia, iteraciones=1000):
    """
    pesos: lista de pesos w[i] para cada nodo i (aporte de cada inversor)
    adyacencia: lista de sets, donde adyacencia[i] contiene los vecinos (conflictos) del nodo i
    iteraciones: cuántas veces se prueba aleatoriamente
    """
    n = len(pesos)
    mejor_conjunto = set()
    mejor_total = 0

    for _ in range(iteraciones):
        nodos = list(range(n))
        random.shuffle(nodos)
        conjunto_actual = set()

        for nodo in nodos:
            if all(vecino not in conjunto_actual for vecino in adyacencia[nodo]):
                conjunto_actual.add(nodo)

        total = sum(pesos[i] for i in conjunto_actual)
        if total > mejor_total:
            mejor_total = total
            mejor_conjunto = conjunto_actual

    return mejor_conjunto, mejor_total
