'''
⭐Un colaborador del laboratorio de “cálculo automatizado S.A” propone un nuevo método de multiplicación de matrices. Utiliza división y conquista partiendo la matrices en bloques de tamaño n/4 x n/4. Y el proceso de combinación de resultados llevara Θ(n2). Se muestra vago en indicar la cantidad de subproblemas que creará cada paso. Le indican que este dato es fundamental para decidir si proseguir con esa línea de investigación o no. Actualmente utilizan el algoritmo de Strassen con una complejidad de O(nlog2(7)). Siendo T (n) = aT (n/4) + Θ(n2), con a la información a determinar. ¿Cuál es la cantidad de subproblemas más grande que puede tomar la solución para que sea mejor que su algoritmo actual?
'''

'''
⭐Se cuenta con un vector de “n” posiciones en el que se encuentran algunos de los primeros ”m” números naturales ordenados en forma creciente (m >= n). En el vector no hay números repetidos. Se desea obtener el menor número no incluido. Ejemplo: [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]. Solución: 6. Proponer un algoritmo de tipo división y conquista que resuelva el problema en tiempo inferior a lineal. Expresar su relación de recurrencia y calcular su complejidad temporal.
'''
def obtener_numero_minimo(arreglo, inicio, fin):
    if inicio >= fin:
        return arreglo[inicio]
    medio = (inicio + fin)//2
    if arreglo[medio] != medio + 1:
        return obtener_numero_minimo(arreglo, inicio, medio)
    else:
        return obtener_numero_minimo(arreglo, medio+1, fin)
        
# L = [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]
# print(obtener_numero_minimo(L, 0, len(L) - 1))
    
'''
⭐Se realiza un torneo con n jugadores en el cual cada jugador juega con todos los otros n-1. El resultado del partido solo permite la victoria o la derrota. Se cuenta con los resultados almacenados en una matriz. Queremos ordenar los jugadores como P1, P2, …, Pn tal que P1 le gana a P2, P2 le gana a P3, …, Pn-1 le gana a Pn (La relación “le gana a” no es transitiva). Ejemplo: P1 le gana a P3, P2  le gana a P1 y P3 le gana a P2. Solución: [P1, P3, P2]. Resolver por división y conquista con una complejidad no mayor a O(n log n).
'''
def resultado_torneo(resultados, jugadores):
    if len(jugadores) == 1:
        return jugadores
    medio = len(jugadores)//2
    izq = resultado_torneo(resultados, jugadores[:medio])
    der = resultado_torneo(resultados, jugadores[medio::])
    return merge(izq, der)

def merge(L1, L2):
    merged = []
    while len(L1) != 0 and len(L2) != 0:
        if L1[0] > L2[0]: #Significa que L1[0] le gano a L2[0]
            merged.append(L1.remove(0))
        else:
            merged.append(L2.remove(0))
    if len(L1) != 0:
        merged.extend(L1)
    else:
        merged.extend(L2)
    return merged

'''
⭐Para determinar si un número es primo existen varios algoritmos propuestos. Entre ellos el test de Fermat. Este es un algoritmo randomizado que opera de la siguiente manera: Dado un número entero “n”, seleccionar de forma aleatoria un número entero “a” coprimo a n. Calcular an-1 módulo n. Si el resultado es diferente a 1, entonces el número “n” es compuesto. La parte central de esta operatoria es la potenciación. Podríamos algorítmicamente realizarla de la siguiente manera:

pot = 1
Desde i=1 a n-1
    pot = pot * a

En este caso se realizan o(n) multiplicaciones. Proponga un método usando división y conquista que resuelva la potenciación con menor complejidad temporal. 
'''
def potencia(a, n):
    if n == 1:
        return a
    if n % 2 == 0:
        return potencia(a, n/2) * potencia(a, n/2)
    else:
        return a * potencia(a, n-1)

'''
⭐A raíz de una nueva regulación industrial un fabricante debe rotular cada lote que produce según un valor numérico que lo caracteriza. Cada lote está conformado por “n” piezas. A cada una de ellas se le realiza una medición de volumen. La regulación considera que el lote es válido si más de la mitad de las piezas tienen el mismo volumen. En ese caso el rótulo deberá ser ese valor. De lo contrario el lote se descarta. Actualmente cuenta con el proceso “A” que consiste en para cada pieza del lote contar cuántas de las restantes tienen el mismo volumen. Si alguna de las piezas corresponde al “elemento mayoritario”, lo rotula. De lo contrario lo rechaza. Un consultor informático impulsa una solución (proceso “B”) que considera la más eficiente: ordenar las piezas por volumen y con ello luego reducir el tiempo de búsqueda del elemento mayoritario. Nos contratan para construir una solución mejor (proceso “C”). Se pide: 
Exprese mediante pseudocódigo el proceso “A”.
Explique si la sugerencia del consultor (proceso “B”) realmente puede mejorar el proceso. En caso afirmativo, arme el pseudocódigo que lo ilustre.
Proponga el proceso “C” como un algoritmo superador mediante división y conquista. Explíquelo detalladamente y brinde pseudocódigo.
'''
def lote_valido(arreglo, inicio, final):
    if inicio >= final:
        return arreglo[inicio]
    medio = (inicio + final) // 2
    izq = lote_valido(arreglo, inicio, medio)
    der = lote_valido(arreglo, medio + 1, final)
    if izq != None:
        cont_izq = 0
        for elemento in arreglo:
            if elemento == izq:
                cont_izq += 1
    if  der != None:
        cont_der = 0
        for elemento in arreglo:
            if elemento == der:
                cont_der += 1
    if cont_izq > len(arreglo) // 2:
        return izq
    elif cont_der > len(arreglo) // 2:
        return der
    return None

#Complejidad Temporal: O(n log n)

'''
⭐Una agencia gubernamental tiene un conjunto de "n" agentes dispersos por el país. Para una misión urgente requiere utilizar dos de ellos. Cada agente tiene una ubicación (x,y). Se dispone de un helicóptero para buscarlos. Generar una solución por división y conquista que indique cuáles son los 2 agentes más cercanos, cuál es su distancia y dónde debería ir el helicóptero a buscarlo.
'''

'''
⭐Dado “L” un listado ordenado de “n” elementos y un elemento “e” determinado. Deseamos conocer la cantidad total de veces que “e” se encuentra en “L”. Podemos hacerlo en tiempo O(n) por fuerza bruta. Presentar una solución utilizando división y conquista que mejore esta complejidad.
'''
def buscar_elemento(arreglo, inicio, fin, elemento):
    primera_aparicion = obtener_primera(arreglo, inicio, fin, elemento)
    ultima_aparicion = obtener_ultima(arreglo, inicio, fin, elemento)
    if primera_aparicion > ultima_aparicion:
        return 0  # No encontrado
    return ultima_aparicion - primera_aparicion + 1

def obtener_primera(arreglo, inicio, fin, elemento):
    if inicio > fin:
        return inicio
    medio = (inicio + fin) // 2
    if arreglo[medio] < elemento:
        return obtener_primera(arreglo, medio + 1, fin, elemento)
    else:
        return obtener_primera(arreglo, inicio, medio - 1, elemento)

def obtener_ultima(arreglo, inicio, fin, elemento):
    if inicio > fin:
        return fin
    medio = (inicio + fin) // 2
    if arreglo[medio] > elemento:
        return obtener_ultima(arreglo, inicio, medio - 1, elemento)
    else:
        return obtener_ultima(arreglo, medio + 1, fin, elemento)


'''
⭐Una encuesta de internet pidió a personas que ordenen un conjunto de “n” películas comenzando por las que más les gusta a las que menos. Con los resultados quieren encontrar quienes comparten gustos entre sí. Nos solicitan generar un algoritmo, que basándose en el concepto de inversión, compare entre pares de personas y determine qué tan compatibles o incompatibles son. Proponer un algoritmo utilizando división y conquista que lo resuelva.
'''
#contar inversiones de B respecto de A
def contar_inversiones(A, B):
    index_b = []
    for elemento in A:
        index_b.append(B.index(elemento))

    return merge_sort_inversiones(index_b, 0, len(index_b)-1)

def merge_sort_inversiones(arr):
    if len(arr) <= 1:
        return arr, 0
    medio = len(arr) // 2
    izq, inv_izq = merge_sort_inversiones(arr[:medio])
    der, inv_der = merge_sort_inversiones(arr[medio:])
    fusionado, inv_merge = merge(izq, der)
    return fusionado, inv_izq + inv_der + inv_merge

def merge(izq, der):
    i = j = inv = 0
    res = []
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            res.append(izq[i])
            i += 1
        else:
            res.append(der[j])
            inv += len(izq) - i  # Todas las que quedan en izquierda son mayores
            j += 1
    res.extend(izq[i:])
    res.extend(der[j:])
    return res, inv


'''
⭐⭐Dentro de un país existen dos colonias subacuáticas cada una de ellas con “n” habitantes. Cada habitante tiene su documento de identidad único identificado por un número. Para una tarea especial se decidió seleccionar a aquella persona que vive en alguna de las colonias cuyo número de documento corresponda a la mediana de todos los números de documento presentes en ellas. Por una cuestión de protocolo no nos quieren dar los listados completos de documentos. Solo nos responden de cada colonia ante la consulta “Cual es el documento en la posición X de todos los habitantes de la isla ordenados de mayor a menor”. Utilizando esto, proponer un algoritmo utilizando división y conquista que resuelva el problema con la menor cantidad posibles de consultas. Analizar complejidad espacial y temporal.
'''
# func mediana_colonias(n):
#     return encontrar_kesimo(0, 0, n)

# func encontrar_kesimo(i, j, k):
#     // Queremos encontrar el k-ésimo menor documento combinando ambas colonias
#     // i: inicio de búsqueda en colonia A
#     // j: inicio de búsqueda en colonia B

#     si i == n:
#         retornar consulta(2, j + k) // agotamos colonia 1
#     si j == n:
#         retornar consulta(1, i + k) // agotamos colonia 2

#     si k == 0:
#         return min(consulta(1, i), consulta(2, j))

#     mitad = (k - 1) // 2
#     i1 = min(i + mitad, n - 1)
#     j1 = min(j + mitad, n - 1)

#     a = consulta(1, i1)
#     b = consulta(2, j1)

#     si a > b:
#         // significa que descartamos j1 - j + 1 elementos de colonia 2
#         return encontrar_kesimo(i, j1 + 1, k - (j1 - j + 1))
#     sino:
#         // descartamos i1 - i + 1 elementos de colonia 1
#         return encontrar_kesimo(i1 + 1, j, k - (i1 - i + 1))

'''
⭐ Se cuenta con un vector V de “n” elementos. Este vector visto de forma circular está ordenado. Pero no necesariamente en la posición inicial se encuentra el elemento más pequeño. Deseamos conocer la cantidad total de rotaciones que presenta “V”. Ejemplo: V = [6, 7, 9, 2, 4, 5] se encuentra rotado en 3 posiciones. Podemos hacerlo en tiempo O(n) por fuerza bruta. Presentar una solución utilizando división y conquista que mejore esta complejidad.
'''
def busqueda_minimo(arreglo, inicio, fin):
    if inicio >= fin:
        return inicio
    medio = (inicio+fin) // 2
    if arreglo[medio] > arreglo[fin]:
        return busqueda_minimo(arreglo, medio+1, fin)
    else:
        return busqueda_minimo(arreglo, inicio, medio)


L = [6, 7, 9, 2, 4, 5]
print(busqueda_minimo(L,0,5))