
#PARCIAL 28 DE OCTUBRE DE 2024
'''
Greedy: El club de amigos de la república Antillense prepara un agape en sus instalaciones en la que desea invitar a la maxima cantidad de sus "n" socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito. Solo puede asistir si conoce a al menos otras 4 personas invitadas. Nos solicita seleccionar el mayor numero posible de invitados. Plantee una solucion algoritmica del problema.
'''

#El algoritmo propuesto itera por cada posible invitado. Si el mismo no conoce a 4 o mas personas se lo elimina de la lista, restando 1 a todos sus conocidos, los cuales seran evaluados para saber si siguen cumpliendo con la restriccion.
def seleccionar_invitados(personas, conocidos, q):
    for persona in personas:
        if conocidos[persona] < 4:
            q.encolar(persona)
    while not q.esta_vacia():
        persona = q.desencolar()
        for conocido in persona.conocidos:
            conocidos[conocido] -= 1
            if conocidos[conocido] < 4:
                q.encolar(conocido)
            personas.remove(persona)
    return personas

#Complejidad Temporal: O(n)
#Complejidad Espacial: O(n)
#Optimalidad: Si la funcion devolviese un resultado no optimo, signifca que al menos un elemento no conoce a 4 o mas personas, esto es imposible ya que esta programado para que siempre que un elemento no cumpla la condicion sea eliminado 

'''
Programación Dinámica: Un restaurante vende un plato llamado "menú ejecutivo" cuyo precio e ingredientes cambian cada día. Luego de "n" días los platos se vuelven a repetir con el mismo orden y mismos precios. En su carta se encuentra publicado el valor de cada uno de ellos. Un joven que recibe plata de sus padres quiere ir y comer la mayor cantidad de días posibles el menú ejecutivo. Sus padres le dijeron que cada vez que vaya le darán menos plata, que el valor del ultimo plato que selecciono, para pagar la cuenta. Ayudar mediante programacion dinamica al joven para que logre su cometido.
'''
#[10,10,9,8] -> 10. como maximo podes comprar el de 9
#[4, 3, 2, 1, 9]

#[1, 2, 3, 4, 1]
    

#OPT[i] = max subsecuencia decreciente que termina en el dia i
 #OPT[i] = max(1, max(dp[j] + 1)) donde 0<=j<=i y arr[j]>arr[i]

def mayor_cant_menu_ejec(arr):
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n

    for i in range(0,n):
        for j in range(0, i):
            if arr[j] > arr[i] and dp[j] + 1 > dp[i]:
                dp[i] =  dp[j] + 1
                prev[i] = j
    max_len = 0
    idx = 0
    #De todas las subsecuencias que tengo, busco la de mayor longitud y su indice en dp
    for i in range(0, n):
        if dp[i] > max_len:
            max_len = dp[i]
            idx = i
        
    subseq = []
    while idx != -1:
        subseq.append(arr[idx])
        idx = prev[idx]

    return max_len, subseq.reverse()

#Complejidad Temporal: O(n^2)
#Complejidad Espacial: O(n)
#Optimalidad: Es optimo ya que me encargo de de seleccionar de forma decreciente los dias a los que mayor cantidad de dias con precios menores vengan luego de él. Esto me permite maximizar la cantidad de dias de diferentes menus ejecutivos consumidos respetando el orden en que se ofrecen.

'''
Redes de Flujo: Una organizacion secreta tiene una red de mensajeros desde una base "A" a la base "B". CAda mensajero puede enviar un mensaje a un subconjunto de sus pares. Solo un subconjunto de mensajeros sabe llegar a "B". En "A" solo conocen a un subconjunto de mensajeros. "A" sospecha que la red ha sido comprometida y quieren informar a la base "B". Nos piden que indiquemos cual es el numero minimo de mensajeros que pueden perder (y quienes) antes de quedar incomunicados entre bases
'''

#Transformar a una red:
def transformacion(mensajeros):
    grafo = 0 #Creo un grafo con S y T, donde S es A y T es B
    for mensajero in mensajeros:
        nodo_in = f'{mensajero}_in'
        nodo_out = f'{mensajero}_out'
        grafo.add(nodo_in)
        grafo.add(nodo_out)
        grafo.crear_arista(nodo_in, nodo_out, 1)
        #Si es conocido de A o de B creo una arista que lo una
    #Agrego aristas desde out a in para cada conocido
#O(n + m)

def ff_ek(grafo, s, t):
    #inicialmente todo el flujo en 0
    #inicializo el grafo residual
    #mientras haya un camino de aumento entre s y t:
        #Sea P el camino de aumento
        #Sea W el cuello de botella
        #flujo += W
        #Actualizo grafo y grafo residual
    #retornar flujo, grafo residual
    return 0
#O(V*E^2)

def corte_minimo(grafo_residual, flujo):
    corte_minimo = set()
    #alcanzables = todos los nodos alcanzables desde S
    #no_alcanzables = complemento de alcanzables
    #Por cada arista en grafo_residual:
        #Si empieza en alcanzables y termina en no alcanzables
            #corte_minimo.agregar(arista)
    #retornar corte_minimo
#O(E)
def main(mensajeros, s, t):
    grafo = transformacion(mensajeros)
    flujo, gr = ff_ek(grafo, s, t)
    c_m = corte_minimo(gr, flujo)
    resultado = []
    for arista in c_m:
        resultado.append(arista.nodo_origen)
    return resultado
#O(V*E^2)

'''
Clases de Complejidad: Hay "n" personas que trabaja en bienes raice. Cada una con un portafolio de propiedades exclusivas a la venta y un area de cobertura. Algunas coberturas se superponen con otras. Para una App de bienes raices queremos seleccionar un subconjunto de personas que no se superpongan y maximicen el numero de propiedades ofrecidas entre ellos. Probar que el problema es NP-C (HINT!: Tal vez le resulte util conjunto independiente).
Problema de decisión (versión de tu problema)
Entrada: Un conjunto de personas, cada una con una lista de propiedades y una región de cobertura. Un entero k.
Pregunta: ¿Existe un subconjunto de personas cuyas coberturas no se superpongan y que en conjunto ofrezcan al menos k propiedades?
'''

def certificador_bienes_raices(personas, k, sol):
    props_ofrecidas = set()
    cubierto = 0
    for persona in sol:
        if persona not in personas:
            return False
        if persona.cobertura in cubierto:
            return False
        cubierto.append(persona.cobertura)
        props_ofrecidas.add(persona.propiedades)

    if props_ofrecidas < k:
        return False
    
    return True

#Tranformacion de Independent Set a este problema
    # Cada nodo es una persona que cubre 1 zona y en esa zona hay una propiedad
    # Cada arista entre u y v reflejan que la persona u y la persona v se superponen en las zonas de cobertura
    # el k = k
# Si existe un subconjunto de personas que no se superponeen con al menos k propiedades en total, entonces existe un subconjunto de al menos k nodos que no son adyacentes entre si

'''
Fuerza Bruta: Contamos con un contenedor que partirá en un barco desde el puerto de Buenos Aires. Este contenedor tiene una capacidad maxima de "k" kilos. Podemos elegir entre un conjunto de "n" lotes de productos a transportar, cada uno de ellos con un peso y una ganancia informada. Queremos seleccioanr aquel subconjuinto de productos que no superen la capacidad del contenedor y nos den la ganancia más grande. Tenga en cuenta que una regulacion de aduana indica que algunos productos son incompatibles con otros. Resolver mediante B&B.
'''
def funcion_costo_contenedor(elementos, capacidad_restante, ganancia_parcial):
    cota = 0
    i = elementos[0] #primer elemento que todavia no fue agarrado
    while capacidad_restante > 0:
        if elementos[i].es_compatible():
            if elementos.capacidad() < capacidad_restante:
                capacidad_restante -= elementos[i].capacidad()
                cota += elementos[i].ganancia()
        i += 1
    return cota + ganancia_parcial
def funcion_limite_contenedor(capacidad_restante, elemento):
    return capacidad_restante > elemento.capacidad() 

mejor_gagancia = 0
mejor_solucion = []
def max_ganancia_contenedor(productos, indice, seleccionados, capacidad_restante, ganancia_parcial):
    global mejor_ganancia, mejor_solucion
    if indice == len(productos):
        if ganancia_parcial > mejor_gagancia:
            mejor_gagancia = ganancia_parcial
            mejor_solucion = seleccionados.copy()
        return
    
    cota = funcion_costo_contenedor(productos, capacidad_restante, ganancia_parcial, seleccionados)

    if cota < mejor_gagancia:
        return
    
    producto = productos[indice]

    if producto.peso <= capacidad_restante: #and es_compatible(producto, seleccionados)
        seleccionados.append(producto)
        max_ganancia_contenedor(productos, indice+1, seleccionados, capacidad_restante - producto.pesp, ganancia_parcial + producto.ganancia)
        seleccionados.remove(producto)
    
    max_ganancia_contenedor(productos, indice+1, seleccionados, capacidad_restante, ganancia_parcial)



#PARCIAL 13 DE MAYO DE 2024

'''
Fuerza Bruta: El juego Sudoku corresponde a ubicar en una grilla de 9x9 numeros del 1 al 9 de forma tal que: (i) no hayan numeros repetidos en la misma fila. (ii) no hayan numeros repetidos en la misma columna. (iii) no hayan numeros repetidos en cada una de las 9 subgrillas 3x3 en las que se puede dividir la grilla. Una instancia es la grilla con un subconjunto de celdas con valor y el resto vacias. Se busca que el jugador relllene als celdas vacias para completar la grilla. Solucionar el problema mediante Backtracking.
'''
#Arbol de estados: En la raiz tengo la instancia que me dan, y como hijos tengo escribir un numero en la primer celda libre. Vamos a recorrerlo con DFS 
#Funcion limite: Que el numero escrito no este repetido en la misma fila, en la misma columna o en la subgrilla de 3x3

def funcion_limite(grilla, celda_actual, valor):
    #Verificar la columna O(n)
    #Verificar la fila O(n)
    #Verificar la subgrilla correspondiente O(n)    
    return True

def bt_sudoku(grilla, celda_actual):
    if grilla.esta_completa():
        return funcion_limite(grilla, celda_actual)
    for i in range(1, 10):
        if funcion_limite(grilla, celda_actual, i):
            celda_actual = i
            next = celda_actual.proxima()
            boolean = bt_sudoku(grilla, next)
            if boolean:
                return True
            celda_actual = 0
    return False, grilla
    
'''
Greedy: Contamos con una impresora 3D. Nos solicitan la impresión de “n” modelos. Cada una tiene un tiempo de impresión y una fecha de entrega. Incumplir con al menos 1 fecha determina un apercibimiento proporcional al retraso más largo ocurrido. La impresora requiere limpieza por lo que queremos lograr - si es posible - descanso entre los trabajos. Desean minimizar el apercibimiento. Presentar un algoritmo greedy para resolver el problema.
'''
def impresora_con_apercibimiento(modelos):
    modelos.sort() # Ordeno los modelos por fecha de deadline creciente
    mayor_delay = (0,0)
    tiempo_act = 0
    for modelo in modelos:
        prox_tiempo_act = tiempo_act + modelo.duracion
        if tiempo_act + modelo.duracion < modelo.deadline:
            limpieza = modelo.deadline - prox_tiempo_act
            tiempo_act += limpieza
        tiempo_act += modelo.duracion
        if tiempo_act < modelo.deadline:
            continue
        delay = tiempo_act - modelo.deadline
        if delay > mayor_delay[1]:
            mayor_delay = (modelo, delay)
    return mayor_delay

'''
Programacion dinamica: Una empresa vende "n" productos. CAda uno tiene un peso, un precio y un stock ilimitado. Deben enviar un contenedor que contenga al menos 1 unidad de cada producto. Desean despachar más productos asegurandose que al venderlos ganar lo maximo posible. La capacidad del contenedor es de "k" kilos. Queremos seleccionar el subconjunto de productos y su cantidad que maximice la posible ganancia.
'''
def mochila_infinita(elementos, k):
    # Paso 1: Incluir al menos una unidad de cada producto
    ganancia_base = 0
    for elemento in elementos:
        if elemento.peso > k:
            return "No es posible cumplir la condición de al menos una unidad de cada producto"
        k -= elemento.peso
        ganancia_base += elemento.ganancia

    # Paso 2: Mochila con repetición clásica sobre el peso restante
    dp = [0] * (k + 1)
    usados = [-1] * k+1
    for peso_actual in range(1, k + 1):
        for elemento in elementos:
            if elemento.peso <= peso_actual:
                if dp[peso_actual] < dp[peso_actual - elemento.peso] + elemento.ganancia:
                    dp[peso_actual] = dp[peso_actual - elemento.peso] + elemento.ganancia
                    usados[peso_actual] = elemento
    reconstruccion = []
    i = k
    while i > 0:
        reconstruccion.append(usados[i])
        i -= usados[i].peso
    reconstruccion += elementos
    return (ganancia_base + dp[k]), reconstruccion


'''
Redes de Flujo: Una red de comunicación fue publicada como de capacidad ilimitada. Está conformada por un conjunto de servidores y enlaces que conectan pares de estos. Cada enlace tiene una capacidad muy elevada de transmisión. No funciona como esperan. El procesamiento de derivación en cada servidor limita el flujo de datos. Brindarán su red de forma exclusiva para transferir desde un servidor en la red a otro un conjunto de datos. Contamos con la topología de la red y las capacidades de los enlaces y servidores. Determinar si es posible transmitir un volumen de datos X. De no ser posible recomendar justificando qué servidores analizará en primer lugar para aumentar su capacidad.
'''
def ff_ek(grafo):
    #Inicializo todo el flujo en 0
    #Creo el grafo residual
    #Mientras haya un camino de aumento entre s y t:
        #Sea p el camino de aumento
        #Sea w el cuello de botella
        #flujo += w
        #Actualizar el grafo y grafo residual
    #retornar flujo, grafo residual
    return f'Siempre azucar nunca edulcorante'
    

def servidores_saturados(red, servidores, x):
    s, t = 0, 0

    grafo = Grafo(s, t)
    for servidor in servidores:
        grafo.agregar_vertice("servidor_in")
        grafo.agregar_vertice("servidor_out")
        grafo.agregar_arista("servidor_in", "servidor_out", servidor.limite)
    
    for servidor in servidores:
        if len(servidor.anteriores) == 0:
            grafo.agregar_arista(s, "servidor_in", float("inf"))
        if len(servidor.siguientes) == 0:
            grafo.agregar_arista("servidor_out", t, float("inf"))
        for siguiente in servidor.siguientes:
            grafo.agregar_arista("servidor_out", "siguiente_in", float("inf"))

    flujo, grafo_residual = ff_ek(grafo, s, t)
    if flujo >= x:
        return " Completado"
    alcanzables = set() # Nodos alcanzables desde s en grafo residual
    no_alcanzables = set()
    servidores_a_mejorar = set()
 # Complemento de alcanzables
    servidores_a_mejorar = []
    for origen,destino,capacidad in grafo_residual.obtener_aristas():
        if origen in alcanzables and destino in no_alcanzables and capacidad == 0:
            servidores_a_mejorar.add(destino) 
    return servidores_a_mejorar
'''
Clases de Complejidad: Una base espacial tiene una capacidad de "k" kilos y puede albergar "p" personas. Se h recibido la peticion de "n" personas. Cada persona "i" requiere un total de "wi" kilos y ofrece "vi" de pago. ¿Es posible seleccionar al menos X personas y obtener una ganancia minima de Y? Demostrar que el problema es NP-C. (HINT: puede ayudarse con el problema de la mochila).
'''

def cert_base_espacial(k, p, personas, x, y, sol):
    if len(sol) < x:
        return False
    ganancia_total = 0
    peso_total = 0
    for persona in sol:
        if persona not in personas:
            return False
        ganancia_total += persona.ganancia
        peso_total += persona.peso
    
    if ganancia_total < y:tareas_restantes
        return False
    
    if peso_total > k:
        return False
    
    return Truetareas_restantes

# Transformacion
    # Cada elemento es una persona con su peso y ganancia
    # la capacidad k de la mochila es la misma que la base
    # el limite p de personas es la cantidad de elementos
    # la minima ganancia y es igual
    # la cantidad minima de personas x es 0

'''
Fuerza Bruta: Para un proyecto se definen tareas a realizar. Cada tarea tiene un conjunto de otras (o ninguna) que se deben realizar previamente para encararla. Solo se puede hacer de a una tarea por vez. Para cada tarea de acuerdo al orden en la que se realiza se conoce el costo a abonar. Queremos determinar el orden de todas las tareas para que se gaste lo menos posible y a su vez se cumplan las precedencias. Solucionar con branch and bound.
'''
# Mi arbol de estados arranca con ninguna tarea asignada a ningun momento, lo recorro como dfs donde cada ramificacion representa realizar una tarea compatible en el momento i.

def funcion_costo(tareas, costo_parcial, tarea):
    costo = 0
    for posicion in lugares_restantes:
        min_costo = float("inf")
        for tarea in tareas_restantes:
            if tarea[posicion] < min_costo:
                min_costo = tarea[posicion]
        costo += min_costo

    return min_costo + costo_parcial

mejor_solucion = None
mejor_costo = 0


def min_gasto_proyecto(momento_actual, tareas, sol_parcial, costo_parcial):
    if momento_actual == len(tareas):
        if costo_parcial < momento_actual.mejor_costo:
            mejor_costo = costo_parcial
            mejor_solucion = sol_parcial
        return 
        
    for tarea in tareas:
        if tarea not in sol_parcial and tarea.es_compatible(sol_parcial):
            cota = funcion_costo(tareas, costo_parcial, tarea)
            if cota > mejor_costo:
                continue
            sol_parcial.append(tarea)
            min_gasto_proyecto(momento_actual+1, tareas, sol_parcial, costo_parcial + tarea.costo)
            sol_parcial.remove(tarea)


'''
Programación dinámica: Un amigo está creando en un estudio de grabación su primer álbum. La sala tiene disponibilidad para los siguientes “n” días. Como cree en el tarot consultó a una adivina que le indicó día por día qué cantidad de avance pueden lograr si se presentan. Cada día que se juntan, el baterista y el bajista terminan la jornada en un bar compartiendo tragos hasta el amanecer. Esto impide que al día siguiente puedan volver a grabar. Ayude a maximizar el avance.
''' 


# OPT [0] = 0
# OPT[i] = max(OPT [i - 1], OPT[i - 2] + i.avance)

# Opt[i]: el mayor avance hasta el dia i

def estudio(dias):
    solucion = []
    OPT = [0] * (n + 1)
    OPT [1] = dias[1][0]
    for i in range (2, n+1):
        incluyo = OPT[i-2] + dias[i][0]
        no_incluyo = OPT[i-1]
        if incluyo > no_incluyo:
            OPT[i][0] = incluyo
            solucion.append(dias[i])
        else:
            OPT[i][0] = no_incluyo
            solucion.append(dias[i])
        
    return solucion, OPT[-1]

''' 
**Redes de Flujo:** Ante una emergencia una empresa debe movilizar “n” empleados a sus “c” centros estratégicos en la ciudad. Cada empleado ante el requerimiento transmite su ubicación geográfica a un servidor y este – conociendo la posición de todos los empleados y de los centros – le indica a qué centro debe presentarse. Por cuestiones operativas, los empleados se deben distribuir de forma balanceada en los centros y no deben tener que viajar más de k kilómetros para llegar al centro. Elaborar un algoritmo que resuelva el problema de asignación mediante redes de flujo.
'''

'''
Clase de Complejidad: Definimos el problema del Hitting Set como: dado un conjunto finito S de n elementos, una colección C de subconjuntos de S, y un número positivo K ≤ n, ¿existe un subconjunto S' ⊆ S tal que S' contiene al menos un elemento de cada subconjunto de C y |S'| ≤ K? Demostrar que este problema es NP-Completo (HNT) puede ayudarse con el problema vertex cover.
'''
def certificador(S, colecciones, solucion, k):
    if len(solucion) > k:
        return False
    colecciones_cubiertas = set()
    for numero in solucion:
        if numero not in S:
            return False
        # Agregar todas las colecciones al set donde aparezca numero.

    if colecciones_cubiertas != colecciones:
        return False
    
    return True

def pasar_a_VC(grafo, k):
    s = set()
    c = set()
    
    for v in grafo:
        s.add(v)
    
    for origen,destino in grafo.obtener_aristas():
        c.add(set(origen,destino))
    
    k_prima = k

    #hitting_set(s, k_prima, c)
