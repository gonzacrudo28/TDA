'''
⭐Para una inversión inmobiliaria un grupo inversor desea desarrollar un barrio privado paralelo a la una ruta. Con ese motivo realizaron una evaluación de los diferentes terrenos en un trayecto de la misma. Diferentes inversores participarán, pero a condición de comprar algún terreno en particular. El grupo inversor determinó para cada propiedad su evaluación de ganancia. El mismo surge como la suma de inversiones ofrecida por el terreno menos el costo de compra. Debemos recomendar que terrenos contiguos comprar para que maximicen sus ganancias.  Ejemplo: S = [-2, 3, -3, 4, -1, 2]. La mayor ganancia es de 5, comprando los terrenos de valor  [4, -1, 2]. Solucionar el problema mediante un algoritmo de programación dinámica.
'''

'''
Buscamos el maximo subarreglo terminado en i -> OPT[i]
Casos base:
Si tengo 0 elementos: OPT[0] = 0
Si tengo 1 elemento: OPT[i] = i -> si i > 0
Si tengo 2 elementos: 
    OPT[i] = MAX(OPT[i-1], 0)  (Si OPT [i] < 0)
    OPT[i] = MAX(OPT[i-1], 0) + Arr[i]
'''

def maximo_subarreglo(arreglo):
    n = len(arreglo)
    maximo = arreglo[0]
    suma_actual = arreglo[0]
    inicio_actual = 0
    inicio_mejor = 0
    fin_mejor = 0
    for i in range(1, n):
        if suma_actual + arreglo[i] < arreglo[i]:
            suma_actual = arreglo[i]
            inicio_actual = i
        else:
            suma_actual += arreglo[i]
        
        if suma_actual > maximo:
            maximo = suma_actual
            inicio_mejor = inicio_actual
            fin_mejor = i
    
    subarreglo = arreglo[inicio_mejor:fin_mejor + 1]
    return maximo, subarreglo

'''
⭐Dado un Grafo dirigido, acíclico G(V, E) con pesos en sus aristas y dos vértices “s” y “t”; queremos encontrar el camino de mayor peso que exista entre “s” y “t”. Resolver mediante programación dinámica.
'''
'''
OPT[w] = max(OPT[w], OPT[V]+peso(v,w)). W es adyacente a V.
'''

def camino_maximo_bf(grafo, origen):
    dist = {}
    padre = {}
    for v in grafo:
        dist[v] = -float('inf')
        padre[v] = None
    dist[origen] = 0

    aristas = grafo.obtener_aristas()

    for i in range(len(grafo)):
        for v, w, peso in aristas:
            if dist[v] + peso > dist[w]:
                padre[w] = v
                dist[w] = dist[v] + peso
                
    return padre, dist

'''

'''

'''
Casos base:
OPT[X] = MAX(SUM(DESC), R(X) + SUM(DESC(DESC(X))))
'''

def max_rating(arbol):
    dp = [0] * len(arbol)
    lista = ["Lista inversa con bfs al dueño"]
    invitados = set()
    for x in lista:
        if desc(x) == 0:
            dp[x] = r(x)
            continue
        invitado = r(x)
        no_invitado = 0
        for i in desc(x):
            no_invitado += r(i)
            for j in desc(i):
                invitado += r(j)
        
        if invitado > no_invitado:
            dp[x] = invitado
            invitados.add(x)
        
        else:
            dp[x] = no_invitado
    
    return dp[-1], invitados
def desc(x):
    return True
def r(x):
    return 0

'''
⭐La organización de una feria internacional tiene que programar diferentes eventos a realizar en su escenario principal. Para ello pueden elegir, en los diferentes días del evento, entre alguno de los siguientes rubros: un cantante, una compañía de danza, un show de variedades o un humorista.  Disponen de una oferta de cada tipo para cada día y la posible ganancia por venta de entradas. Existen ciertas restricciones que se aplican. No se pueden repetir 2 días seguidos el mismo rubro. Además por el tiempo de preparación un día después de un cantante solo puede presentarse un humorista. Plantear la resolución mediante programación dinámica.
'''

'''
Sea P elsiguiente compatible
OPT[i] = MAX(contratar algo + p, contratar al otro + p, ....)
OPT[i], limitado, cantante -> humorista. cantante, danza, show, humorista -> no pueden haber 2 seguidos
OPT[i] = MAX(elegir a ese tipo + el optimo de esas restricciones)
'''
def feria_maxima_ganancia(ganancias):  
    n = len(ganancias)       # cantidad de días
    R = 4                    # cantidad de rubros
    dp = [[-float('inf')] * R for _ in range(n)]
    
    # Día 0: simplemente pongo las ganancias de cada rubro
    for r in range(R):
        dp[0][r] = ganancias[0][r]
    
    for d in range(1, n):
        for r in range(R):  # rubro actual
            for r_ant in range(R):  # rubro anterior
                if r == r_ant:
                    continue  # no puede repetirse el mismo rubro
                if r_ant == 0 and r != 3:
                    continue  # después de cantante solo puede humorista
                dp[d][r] = max(dp[d][r], dp[d-1][r_ant] + ganancias[d][r]) #Maximo enter ponerme a mi o ponerme a mi mas el dia anterior?
    
    return max(dp[n-1])  # máxima ganancia en el último día

'''
⭐Contamos con una carretera de longitud M km que tiene distribuidos varios carteles publicitarios. Cada cartel ”i” está ubicado en un “ki” kilómetro determinado (pueden ubicarse en cualquier posición o fracción de kilómetro) y a quien lo utiliza le asegura una ganancia “gi”. Por una regulación no se puede contratar más de 1 cartel a 5km de otros. Queremos determinar qué carteles conviene contratar de tal forma de maximizar la ganancia a obtener.
'''
'''
Longitud M km
No puedo poner a menos de 5km

OPT[i] = MAX(OPT[i-1], G[i] + OPT[I']) Donde I' es el ultimo kilometro compatible con I
'''

def poner_carteles(carteles, ganancias, n):
    dp = [] * n
    dp[0] = ganancias[0]
    carteles.sort() #Ordenar por km creciente
    seleccionados = {}
    for i in range(1, n):
        if dp[i-1] > ganancias[i] + dp[i.ult_compatible()]:
            dp[i] = dp[i-1]
            seleccionados[i] = False
        else:
            dp[i] = ganancias[i] + dp[i.ult_compatible()]
            seleccionados[i] = True
    carteles = set()
    i = n
    while i > 0:
        if seleccionados[i] == True:
            carteles.add(i)
            i = i.ult_compatible()
        else:
            i -= 1

    return dp[n], carteles.reverse()


'''
⭐Un ramal ferroviaria pone en concesión los patios de comida en todas las estaciones. Son en total “n” estaciones. Por cada estación se cuenta con el promedio de facturación de los últimos 5 años. Por normativa antimonopólica existe como limitante que ninguna empresa puede explotar 3 o más estaciones contiguas. Pero, no existe una cantidad máxima de estaciones a explotar. Un oferente nos solicita que le digamos cuales son las estaciones que le conviene obtener para maximizar sus ganancias. Plantee la solución mediante programación dinámica.
'''

'''
Casos Base:
    Tengo una sola: OPT[i]
    Tengo 2: OPT[i] + OPT[i-1]
    Tengo 3:
       Primera opción: Evitar D, OPT[D] = OPT[C]
       Segunda opción: Evitar C, OPT[D] = OPT[B] + Gan[D]
       Tercera opción: Evitar B, OPT[D] = Gan[D] + Gan[C] + OPT[A]
obtengo a la estación i? 
Si la obtengo no puedo usar las contiguas:
OPT[i] = max(OPT[i-1], gan[i] + p[i])
'''

def obtener_estaciones(estaciones):
    n = len(estaciones)
    dp = [] * n
    dp[0] = estaciones[0].ganancia()
    dp[1] = dp[0] + estaciones[1].ganancia()
    dp[2] = max(estaciones[2].ganancia()+estaciones[1].ganancia(), estaciones[2].ganancia()+ estaciones[0].ganancia(), dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i-1],dp[i-2]+estaciones[i].ganancia(), estaciones[i-1].ganancia()+dp[i-3]+estaciones[i].ganancia())
    return dp[n]

'''
⭐En un grafo se conoce como conjunto independiente a un subconjunto de vértices del mismo tal que ninguno sea adyacente a otro. Es decir, es un conjunto X de vértices tal que para ningún par de ellos existe alguna arista que los conecte. No se conoce un algoritmo eficiente que resuelva el problema. Sin embargo, para algunos casos especiales de grafos si es posible. Considerar el siguiente caso: Un grafo es un camino si se pueden escribir sus nodos como una sucesión V1, V2, ..., Vn donde cada nodo Vi tiene un eje únicamente con Vi-1 y Vi+1. (Excepto en los extremos donde solo tienen un eje con el siguiente o el anterior). Considerar que cada nodo tiene un peso entero positivo. Construir un algoritmo utilizando programación dinámica que encuentre el set independiente de mayor peso.
'''
'''
Casos base:
1 elemento OPT[i] = i
2 elementos OPT[i] = max(i, opt[i-1])
3 elementos OPT[i] = max(i+OPT[i-2], OPT[i-1])
'''

def maximo_set_indep(lista):
    n = len(lista)
    dp = [] * n
    dp[0] = lista[0]
    dp[1] = max(lista[0], lista[1])
    for i in range (2, n):
        dp[i] = max(lista[i]+dp[i-2], dp[i-1])
    return dp[n]

'''
⭐Para un nuevo satélite a poner en órbita una empresa privada puede optar por incluir diversos sensores a bordo (por ejemplo: variación de temperatura, humedad en tierra, caudal de ríos, etc). Cada uno de ellos tiene un peso "pi" y una ganancia "gi" calculado por su uso durante la vida útil del satélite. Si bien les gustaría incluir todos, el satélite tiene una carga máxima P que puede llevar. Nos piden que generemos un algoritmo (utilizando programación dinámica) para resolver el problema. Indique si su solución es polinomial.
'''
'''
Casos base:
OPT[i, W] = 
OPT[i , 0] = 0 #Si no tengo espacio, el optimo es cero
OPT[0, W] = 0 #Si tengo espacio pero no elementos, el optimo es cero
OPT[i, W]: 
    Si wi > W, OPT[i, W] = OPT[i-1, W]
    Si wi <= W, OPT[i, W] = max(OPT[i-1, W], gi + OPT[i-1, W-wi]) #Si tengo espacio, el optimo es el valor de no agregarlo o agregarlo restando el peso y sumando el valor
'''

def knapsack(elementos, W):
    n = len(elementos)
    dp=[[0]*n+1]*W+1 #primera fila y columna todo en 0
    for i in range (1, n):
        for w in (1, W):
            if w < elementos[i].peso(): #no entra
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], elementos[i].ganancia() + dp[i-1][w-elementos[i].peso()])
    return reconstruir_camino(elementos, dp, n, W)

def reconstruir_camino(elementos, opt, n, W):
    resultado = []
    j = W
    for i in range(n, 0, -1):
        if opt[i][j] != opt[i - 1][j]:
            resultado.append(elementos[i - 1])
            j -= elementos[i - 1][1]
    resultado.reverse()
    return resultado
'''
⭐Se conoce como “Longest increasing subsequences” al problema de, dado un vector de numérico, encontrar la subsecuencia más larga de números (no necesariamente consecutivos) donde cada elemento sea mayor a los anteriores. Ejemplo: En la lista →  2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7. Podemos ver que la subsecuencia más larga es de longitud 6 y corresponde a la siguiente “1, 2, 3, 4, 6, 7”.  Resolver el problema mediante programación dinámica.
'''
'''
OPT[i] = Subsecuencia maxima que termina en el elemento i

OPT[i] = max(1, 
            max{0<=j<=1} donde A[j]< A[i] {dp[j] + 1})
[6, 7, 8, 9, 1]

[1, 2, 3, 4, 1]
prev = [-1, 0, 1, 2, -1]
'''

def lis(arr):
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    max_len = 0
    idx = -1

    for i in range(n):
        if dp[i] > max_len:
            max_len = dp[i]
            idx = i
    
    # Reconstruccion

    subseq = []
    while idx != -1:
        subseq.append(arr[idx])
        idx = prev[idx]
    
    return (max_len, subseq.reverse())

'''
⭐⭐Una variante del problema de la mochila corresponde a la posibilidad de incluir una cantidad ilimitada de cada uno de los elementos disponibles. En ese caso, tenemos una mochila de tamaño “k” y un conjunto de “n” elementos con stock ilimitado. Cada elemento tiene un peso y un costo. Queremos seleccionar el subconjunto de elementos que maximice la ganancia de la mochila sin superar su capacidad. Solucione el problema utilizando programación dinámica.
'''
'''
para cada i en W: MAX(OPT[i-1], MAX(otros) + OPT[i-1, W-wi])
'''


def mochila_infinita(elementos, W):
    n = len(elementos)
    dp = [0] * W + 1
    dp[0] = 0
    for i in range(1,W+1):
        for elemento in elementos:
            if elemento.peso() < i:
                dp[i] = max(dp[i], dp[i - elemento.peso()] + elemento.ganancia())
    return dp[n]

'''
⭐El dueño de una cosechadora está teniendo una demanda muy elevada en los próximos 7 meses. Desde “n” campos lo quieren contratar para que preste sus servicios. Lamentablemente no puede hacer todos los contratos puesto que varios de ellos se superponen en sus tiempos. Cuenta con un listado de los pedidos donde para cada uno de ellos se consigna: fecha de inicio, fecha de finalización, monto a ganar por realizarlo. Su idea es seleccionar la mayor cantidad de trabajos posibles. Mostrarle que esta solución puede no ser la óptima. Proponer una solución utilizando programación dinámica que nos otorgue el resultado óptimo (que trabajos elegir y cuanto se puede ganar). 
'''

'''
N ofertas
Cada oferta: Fecha de inicio / Fecha de finalizacion / monto a ganar
Tener la mayor ganancia posible
'''
'''
Caso Base:
Si tengo 0 contratos OPT[0] = 0
Si tengo 1 contrato OPT[i] = contrato.ganancia()
Si tengo 2 contratos:
    Si no se superponen OPT[i] = OPT[i-1] + contrato.ganancia()
    Si se superponen OPT[i] = max(OPT[i-1], contrato.ganancia())
Si tengo x contratos:
    OPT[x] = max(OPT[x-1], OPT[p(x)] + ganancia(x))
'''

def maxima_ganancia(contratos):
    contratos.sort() # Ordeno por fecha de finalizacion 
    n = len(contratos)
    dp = [0] * n+1
    dp [0] = 0
    for i in range(1, n+1):
        enOptimo = contratos[i].ganancia() + dp[contratos[i].ultimo_compatible()]
        noEnOptimo = dp[i-1]
        if enOptimo> noEnOptimo:
            dp[i] = enOptimo
        else:
            dp[i] = noEnOptimo
    
    solucion = []
    i = n
    while n > 0:
        if contratos[i].ganancia() + dp[contratos[i].ultimo_compatible()] > dp[i-1]:
            solucion.append(contratos[i])
            i = contratos[i].ultimo_compatible()
        else:
            i -= 1
    
    return dp[n], solucion

'''
⭐⭐Una empresa que realiza ciencia de datos debe realizar en las próximas “n” semanas procesos y cálculos intensivos. Para eso debe contratar tiempo de cómputo en la nube. Realizando una estimación conocen cuantas horas de cómputo necesitaran para cada una de las semanas. Por otro lado, luego de negociar con los principales proveedores tienen 2 opciones que puede combinar a gusto. Opción 1: Contratar a la empresa “Aragón” por semana. En esa semana se cobra proporcional al tiempo de cómputo según un parámetro “r”  (horas computo x r). Opción 2: Contratar a la empresa “Fuddle” por un lapso de 5 semanas contiguas. Durante el lapso contratado se paga una tarifa fija de “c”. Proponer una solución utilizando programación dinámica que nos indique la secuencia de elecciones a realizar para minimizar el costo total de cómputo. 
'''

'''
Tengo n semanas:
Aragon: Te cobro r por hora
Fuddle: Te cobro un monto c por las 5 semanas
Propuesta: 
opt[0] = 0
opt[1] = r * horas + opt[0]
opt[2] = r * horas + opt[1]
opt[3] = r * horas + opt[2]
opt[4] = r * horas + opt[3]
opt[i] = min(c + opt[i-5], opt[i-1] + r * horas)
'''

def mejor_contrato(c, r, n, horas):
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    reconstruccion = [] * n
    for i in range(1, 5):
        dp[i] = (r * horas[i]) + dp[i-1] 
    for i in range(5, n+1):
        dp[i] = min(c + dp[i - 5], dp[i-1] + r * horas[i])
        if c + dp[i-5] > dp[i-1] + r*horas[i]:
            reconstruccion[i]= ('A')
        else:
            reconstruccion[i] = 'F'
    i = n
    secuencia = [] * n
    while i > 0:
        if reconstruccion[i] == 'A':
            secuencia[i-1] = 'A'
            i -= 1
        else:
            secuencia[i-1] = 'F'
            i -= 5
    return dp[n]