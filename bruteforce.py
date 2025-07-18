'''
⭐Resuelva el problema de las reinas en el tablero de ajedrez mediante backtracking planteado como permutaciones. Brinde el pseudocódigo y determine la cantidad máxima posible de subproblemas a explorar.
'''
#Funcion limite
def es_valido(ubicacion, tablero):
    #Para la ubicacion dada, verifica que no hay reinas colocadas en esa misma fila, diagonal o columna.
    return True
#Tenemos un arbol de estados que en la raiz tiene el tablero vacio y cada nodo corresponde a agregar una reina en una celda determinada.
#La forma de recorrerlo es DFS.

# [1, 3, 4, 2]

#VERSION CON PERMUTACIONES
def bt(tablero, fila_act, n):
    if fila_act == n + 1:
        return True
    for i in range(1, n+1):
        if es_valido(tablero, opcion_actual = i):
            tablero[fila_act] = i
            if bt(tablero, fila_act + 1, n):
                return True
            tablero[fila_act] = 0
    return False 

#VERSION SIN PERMUTACIONES
def bt(tablero, fila_act, n):
    if fila_act == n + 1 :
        return True
    for i in range(1, n+1):
        if es_valido(tablero, opcion_actual = i):
            tablero[fila_act][i] = 1
            if bt(tablero, fila_act + 1, n):
                return True
            tablero[fila_act][i] = 0
    return False        
            
#Cantidad de casos posibles: 
#   Para la version de permutaciones es n!
#   Para la version sin permutaciones es n^n
#Complejidad espacial:
#   Para la version de permutaciones: O(n)
#   Para la version sin permutaciones es O(n^2)

'''
⭐⭐En un tablero de ajedrez (una cuadrícula de 8x8) se ubica la pieza llamada “caballo” en la esquina superior izquierda. Un caballo tiene una manera peculiar de moverse por el tablero: Dos casillas en dirección horizontal o vertical y después una casilla más en ángulo recto (formando una forma similar a la letra “L”). El caballo se traslada de la casilla inicial a la final sin tocar las intermedias, dado que las “salta”. Se quiere determinar si es posible, mover esta pieza de forma sucesiva a través de todas las casillas del tablero, pasando una sola vez por cada una de ellas, y terminando en la casilla inicial. Plantear la solución mediante backtracking.
'''

# transformacion de problema del caballo a ciclo hamiltoniano:
    # cada casillero del tablero pasa a ser un nodo
    # dados dos nodos u y v que representan casilleros distintos,estos seran adyacentes
    # si con el movimiento de un caballo se puede ir de uno al otro
    # se pasa el casillero inicial como nodo de origen y se plantea encontrar un ciclo hamiltoniano

def bt_ciclo_hamiltoniano(origen, visitados, grafo, nodo_actual, camino):
    if len(visitados) == len(grafo):
        if origen in grafo.adyacentes(nodo_actual):  # puede volver al origen
            camino.append(nodo_actual)
            return True, camino
        return False, []
    
    for adyacente in grafo.adyacentes(nodo_actual):
        if adyacente not in visitados:
            visitados.add(adyacente)
            camino.append(nodo_actual)
            res, path = bt_ciclo_hamiltoniano(origen, visitados, grafo, adyacente, camino)
            if res:
                return True, path
            camino.pop()
            visitados.remove(adyacente)

    return False, []

#Complejidad espacial: O(n)

'''
⭐Se cuenta con “n” trabajos por realizar y la misma cantidad de contratistas para realizarlos. Ellos son capaces de realizar cualquiera de los trabajos aunque una vez que se comprometen a hacer uno, no podrán realizar el resto. Tenemos un presupuesto de cada trabajo por cada contratista. Queremos asignarlos de forma tal de minimizar el costo del trabajo total. Proponer un algoritmo por branch and bound que resuelva el problema de la asignación.
'''
#Arbol de Estados: cada nivel del arbol corresponde a un trabajo a asignar. Las ramas salen de asignar el trabajo a cada contratista libre
# Si vemos que un costo parcial es mayor al mejor costo, podamos.
# La funcion de costo es el costo parcial mas el costo minimo optimista de asignar los trabajos restantes a los contratistas libres.
# Si Bound > mejor costo, podar
# Si el costo actual es menor al mejor, actualizar la solucion
n = 0 # cant trabajos o contratistas
mejor_costo = float("inf")
mejor_sol = None
usados = set()
sol_act = [-1] * n 
nodos_visitados = 0

def buscar_asignacion(trabajo_act, costo_parcial, costos):
    nodos_visitados += 1
    if trabajo_act == n:
        if costo_parcial < mejor_costo:
            mejor_costo = costo_parcial
            mejor_sol = sol_act.cpoy()
        return
    
    cota = calcular_cota_inf(trabajo_act, costo_parcial, costos)
    if cota >= mejor_costo:
        return

    for c in range(0, n):
        if c not in usados:
            nuevo_costo = costo_parcial + costos[trabajo_act][c]

            if nuevo_costo > mejor_costo:
                continue
            
            usados.add(c)
            sol_act[trabajo_act] = c
            buscar_asignacion(trabajo_act + 1, nuevo_costo), costos
            usados.remove(c)
            sol_act[trabajo_act] = -1


def calcular_cota_inf(trabajo_act, costo_parcial, costos):
    cota = 0
    for j in range(trabajo_act, n):
        menor = float("inf")
        for c in range(0, n):
            if c not in usados and costos[j][c] < menor:
                menor = costos[j][c]
        cota += menor
    return costo_parcial + cota

def principal(costos):
    n = len(costos)
    buscar_asignacion(0, 0)
    return mejor_costo, mejor_sol, nodos_visitados

'''
⭐⭐Contamos con un conjunto de “n” actividades entre las que se puede optar por realizar. Cada actividad x tiene una fecha de inicio Ix, una fecha de finalización fx y un valor vx que obtenemos por realizarla. Queremos seleccionar el subconjunto de actividades compatibles entre sí que maximice la ganancia a obtener (suma de los valores del subconjunto). Proponer un algoritmo por branch and bound que resuelva el problema.
'''

'''
⭐⭐Se cuenta con “n” servidores especializados en renderización de videos para películas animadas en 3d. Los servidores son exactamente iguales. Además contamos con “m” escenas de películas que se desean procesar. Cada escena tiene una duración determinada. Queremos determinar la asignación de las escenas a los servidores de modo tal de minimizar el tiempo a esperar hasta que la última de las escenas termine de procesarse. Determinar dos metodologías con la que pueda resolver el problema y presente cómo realizar el proceso.
'''

'''
⭐⭐Contamos con una cuadrícula de n*n celdas. Cada celda puede pintarse de 2 colores: blanco o negro. Por cada fila (y cada columna) nos indican cuantas celdas hay que pintar de negro. Debemos obtener todas las coloraciones válidas que cumplan con las instrucciones.  Resolver mediante Backtracking.
'''
#Arbol de Estados: Cada nodo representa una celda pintada de un color (puede ser negro o blanco), luego cada hijo representa pintar la celda siguiente de un color.
#La funcion limite verifica si se excede el limite de celdas negras en la fila o en la columna
#Recorro el arbol usando DFS
soluciones = [] # Lista de tableros 

def funcion_limite_pintar_celdas(cuadricula, celda, cant_negras_f, cant_negras_c):
    #Valida que la fila y la columna no exceda la cantidad de celdas negras
    return True

#celda_actual = (fila, columna)
def bt(tablero, fila, col, negras_fila, negras_col, req_fila, req_col, n):
    if fila == n:
        if negras_fila == req_fila and negras_col == req_col:
            soluciones.append(tablero.copy())
        return  # no cortar: seguir buscando más soluciones

    fila_sig, col_sig = (fila, col + 1) if col + 1 < n else (fila + 1, 0)

    # Intentar pintar de NEGRO
    tablero[fila][col] = 'N'
    negras_fila[fila] += 1
    negras_col[col] += 1
    if es_valido(fila, col, negras_fila, negras_col, req_fila, req_col):
        bt(tablero, fila_sig, col_sig, negras_fila, negras_col, req_fila, req_col, n)
    negras_fila[fila] -= 1
    negras_col[col] -= 1

    # Intentar pintar de BLANCO
    tablero[fila][col] = 'B'
    bt(tablero, fila_sig, col_sig, negras_fila, negras_col, req_fila, req_col, n)