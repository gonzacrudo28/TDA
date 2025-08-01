
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
Clases de Complejidad: Hay "n" personas que trabaja en bienes raices. Cada una con un portafolio de propiedades exclusivas a la venta y un area de cobertura. Algunas coberturas se superponen con otras. Para una App de bienes raices queremos seleccionar un subconjunto de personas que no se superpongan y maximicen el numero de propiedades ofrecidas entre ellos. Probar que el problema es NP-C (HINT!: Tal vez le resulte util conjunto independiente).
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
    
    if ganancia_total < y:
        return False
    
    if peso_total > k:
        return False
    
    return True

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
    n = len(dias)
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

'''
Fuerza Bruta: El problema de coloreo de grafos intenta asignar un color a cada nodo de forma tal que ningún par de nodos adyacentes comparten el mismo color. Sea el grafo G=(V,E) se desea obtener una coloración de no más de k colores. Resuelva utilizando Backtracking.
'''

def coloreo():
    

    visitados = set()
    def bt_colores(grafo, nodo, colores):
        if len(visitados) == len(grafo.vertices()):
            return grafo
        
        for color in colores:
            nodo.pintar(color)
            visitados.add(nodo)
            if es_valido_color(grafo): #La funcion es valido chequea si alguno de los adyacentes tiene el mismo color
                for adyacente in nodo.ady():
                    if adyacente not in visitados:
                        bt_colores(grafo, adyacente, colores)
                    if not bt_colores(grafo, adyacente, colores):
                        break
            nodo.despintar()
            visitados.remove(nodo)

    for v in grafo:
        if v not in visitados:
            es_valido = bt_colores(G, v, colores)
            if not es_valido:
                return False
    return grafo

'''
Greedy: La costa de un país cuenta con “n” faros. Cada faro “i” cubre una cantidad de kilómetros de costa lineal no interrumpida a su alrededor comenzando por el kilómetro si y finalizando en el kilómetro ei. Muchos de esos faros se solapan en su cobertura, incluso algunos están totalmente cubiertos entre sí. Para minimizar la asignación de personal que requieren nos solicitan que seleccionemos el menor subconjunto de faros que cubran totalmente la línea costera o afirmar que no es posible. Proponga un algoritmo greedy que lo resuelva.
'''
def ubicar_faros(faros): # Faro = (si, ei)
    faros.sort() #Ordenar por fecha de inicio en caso de empate, ordenar por orden descente segun ei.
    inicio = 0
    pos_actual = 0
    sol = set()
    candidato = 0
    
    for faro in faros:
        
        if inicio < faro.si:
            pos_actual=max(pos_actual, faro.ei)
        else:
            sol.add(candidato)
            inicio = faro.anterior().ei
            candidato = faro
            pos_actual = faro.ei

'''
Programación dinámica: El dueño de un salón de convenciones debe decidir a qué exposiciones y congresos alquilará en los próximos meses. Ha reunido “n” propuestas cada una de ellas con una ganancia diferente según los servicios solicitados. Algunos de ellos se superponen entre sí. Para cada propuesta conoce: fecha de inicio, fecha de finalización, monto a ganar por realizarlo. Planea elegir las que duren menos. Mostrar que esta solución no es óptima. Proponer una solución utilizando programación dinámica que responda propuestas elegir y cuánto se puede ganar.
'''

 # OPT [0] = 0
 # OPT [i] = max(OPT[i - 1], OPT [pi] + gi) Siendo pi el ultimo compatible con i

def congreso(propuestas):
    n = len(propuestas)
    propuestas.sort()# ordeno las charlas por fin
    dp = [0] * n + 1
    for i in range(1, n + 1):
        enOptimo = propuestas[i].ganancia + dp[propuestas[i].ultimo_compatible()]
        noEnOptimo = dp[i-1].ganancia()
        if enOptimo > noEnOptimo:
            dp[i] = enOptimo
        else:
            dp[i] = dp[i-1] 
    
    dp[n]
    sol = []
    i = n
    while i > 0:
        if dp[i] == dp[i-1]:
            i-=1
        else:
            sol.append[propuestas[i]]
            i = ultimo_compatible(i)
    
    return sol.reverse(), dp[n]

'''
Clases de Complejidad: Para elaborar un juego de aventura gráfica se juntaron “m” equipos de diseñadores para proponer diferentes escenarios. No todos los escenarios son compatibles entre sí. Por cada una de las “n” escenarios han anotado que equipo lo propuso y con cuales otros no es compatible. Desean poder seleccionar “k” escenarios compatibles para construir el juego. Se requiere que todos los escenarios pertenezcan al mismo equipo de diseñadores. Se pide: Demostrar que el problema es NP-Completo. (HINT!: Tal vez le resulte útil clique)
'''

def certificador(k, solucion, equipos, escenarios):

    if len(solucion) != k:
        return False
    equipo = solucion[0].equipo()
    if equipo not in equipos:
        return False
    for escenario in solucion:
        if not escenario.es_compatible(solucion - [escenario]):
            return False
        if escenario not in escenarios:
            return False
        if escenario.equipo != equipo:
            return False

    return True


#transformacion
# Cada nodo es un escenario
# Los nodos unidos son los compatibles entre si
# Todos los escenarios pertenecen a un mismo equipo
# K es el mismo
# Juego_aventura(escenarios, k, compatibles, equipo)

#PARCIAL 16 DE DICIEMBRE 2024
'''
Fuerza Bruta: Se cuenta con 'n' fábricas por construir y la misma cantidad de ciudades donde ubicarlas. En cualquier ciudad se puede establecer 1 y solo 1 fábrica. Tenemos un estimado de la ganancia a obtener por asignar cada fábrica a cada ciudad. Queremos asignarlas de forma tal de maximizar la ganancia total. Proponer un algoritmo por branch and bound que resuelva este problema de asignación.
'''
#Arbol de estados: Inicialmente todas las ciudades vacías. En cada nivel se evalúa poner una fabrica en la ciudad i. Cada hijo es poner una fabrica en las ciudades restantes.

def funcion_costo(fabricas, ciudades, ganancia_parcial):
    cota = 0
    for ciudad in ciudades:
        if not ciudad.esta_usada():
            cota += max(ciudad.fabricas_disponibles())
    return cota + ganancia_parcial
mejor_solucion = set()
maxima_ganancia = 0
usados = set()
def bb_fabricas(fabricas, ciudades, ganancia_parcial, solucion_parcial,ciudad_actual):
    if len(solucion_parcial) == len(ciudades):
        if mejor_ganancia < ganancia_parcial:
            mejor_ganancia = ganancia_parcial
            mejor_solucion = solucion_parcial
        return 
    cota = funcion_costo(fabricas, ciudades, ganancia_parcial)
    if cota < mejor_ganancia:
        return
    for fabrica in fabricas:
        if fabrica not in usados:
            usados.add(fabrica)
            ciudades[ciudad_actual] = fabrica
            nueva_ganancia = ganancia_parcial+fabrica.ganancia()
            bb_fabricas(fabricas, ciudades, nueva_ganancia, ciudad_actual + 1)
            usados.remove(fabrica)
            ciudades[ciudad_actual] = None
    

'''
Greedy: Contamos con cartas numeradas del 1 al 'n' mezcladas en un orden desconocido. Debemos seleccionar de a una, mirarla y acomodarla en pilas. Una carta puede formar una pila nueva o ubicarse en una existente siempre que la carta superior en esta sea un número mayor. Queremos ubicar todas las cartas en la menor cantidad de pilas posible. Resolver el problema con la menor complejidad posible y demostrar optimalidad.
'''
def solitario(pilas, cartas):
    for carta in cartas:
        if pilas.esta_vacia():
            pilas.append(Pila(carta)) #Creo una pila con la carta en el tope
            continue
        idx = buscar_idx_pila(pilas, carta, 0, len(pilas), -1)
        if idx == -1:
            pilas.append(Pila(carta))
            continue
        pilas[idx].apilar(carta)
    return pilas

def buscar_idx_pila(pilas, carta, inicio, fin, candidato):
    if inicio > fin:
        return candidato
    medio = (inicio + fin) / 2
    if pilas[medio].tope() < carta:
        return buscar_idx_pila(pilas, carta, medio + 1, fin, candidato)
    if pilas[medio].tope() > carta:
        candidato = medio
        return buscar_idx_pila(pilas, carta, inicio, medio, candidato)
    
'''
Programación dinámica: Sea G=(V,E) un grafo dirigido. No se conoce un algoritmo polinomial para encontrar el camino más largo simple (El largo del camino corresponde a la cantidad de nodos por los que pasa). Sin embargo, para ciertos casos se puede resolver en forma eficiente. Consideremos que G corresponde a un grafo ordenado. En este caso se pueden disponer ordenados los nodos de forma que:

i) Desde cada nodo pueden existir ejes salientes a nodos con mayor "índice" (posteriores en su ordenamiento) pero no a nodos de menor índice.
ii) Cada nodo excepto el último tiene ejes salientes.

Proponer un algoritmo eficiente que resuelva este problema.
'''
# dp[i] : El camino mas largo que arranca en i y termina en n

def camino_simple_mas_largo(grafo):
    n = len(grafo)
    dp = [1] * (n + 1)
    dp[n] = 1
    next = [-1] * (n + 1)
    for i in range(1, n, -1):
        max_path = 0
        idx = -1
        for j in range(i + 1, n + 1):
            if grafo.hay_arista(i, j):
                if dp[j] > max_path:
                    max_path = dp[j]
                    idx = j
        dp[i] = max_path + 1
        next[i] = idx
    
    max_path = 0
    idx_start = -1

    for i in range(1, n+1):
        if dp[i] > max_path:
            max_path = dp[i]
            idx_start = i
    
    camino = []
    indice = idx_start
    while indice != -1:
        camino.append(indice)
        indice = next[indice]
    
    return max_path, camino



'''
Clases de Complejidad: Definimos el problema Subgrafo denso de la siguiente manera: Dado un grafo G=(V,E) y dos parámetros a y b. ¿Existe en G un subconjunto S de al menos “a” vértices con al menos “b” ejes entre ellos? Demostrar que este problema es NP-Completo. Sugerencia: Utilizar el problema del Clique.
'''

def certificador_subgrafo_denso(sol, grafo, a, b):
    if len(sol) < a:
        return False
    for v in sol:
        if v not in grafo:
            return False
    aristas_sol = set()
    for v in grafo:
        for w in grafo.adacentes(v):
            if grafo.arista(v, w) not in aristas_sol:
                aristas_sol.add(grafo.arista(v, w))
    
    if len(aristas_sol) < b:
        return False
    return True


# Instancia clique:
# Grafo, k
# Buscas un subgrafo completo de al menos k vertices

# Transformacion:
    # El grafo es el mismo
    # a = k
    # b = k*(k-1)/2 <-Buena de eze esta
    # subgr


#ULTIMO PARCIAL WHATSAPP

'''
División y conquista: Dado un vector A de 'n' números enteros (tanto positivos como negativos) queremos obtener el subvector cuya suma de elementos sea mayor a la suma de cualquier otro subvector en A.
Ejemplo: Array: [-2, -5, 6, -2, -3, 1, 5, -6]
Solución: [6, -2, -3, 1, 5]
Resolver el problema de subarreglo de suma máxima por división y conquista.
'''

def max_sub_arr(arreglo, inicio, final):
    if inicio == final:
        return arreglo[inicio]
    medio = (inicio + final) // 2
    max_izq = max_sub_arr(arreglo, inicio ,medio)
    max_der = max_sub_arr(arreglo, medio + 1, final)
    max_cruzado = arreglo.maximo_subarreglo_cruzado()
    return max(max_izq, max_der, max_cruzado)

'''
Programación dinámica: El problema de maximización del set independiente con pesos es NP-Hard. Sin embargo, para algunos casos especiales de grafos se puede resolver de forma eficiente. Considerar el siguiente caso: Un grafo es un camino si se pueden escribir sus nodos como una sucesión V1, V2, ..., Vn donde cada nodo Vi tiene un eje únicamente con Vi-1 y Vi+1. (Excepto en los extremos donde solo tienen un eje con el siguiente o el anterior). Considerar que cada nodo tiene un peso entero positivo. Construir un algoritmo utilizando programación dinámica que encuentre el set independiente que sume el mayor peso.
'''
#dp[0] = 0
#dp [1] = 1.ganancia()
#dp[2] = max(dp[1], dp[2])
#dp[i] = max(dp[i-1], dp[i-2] + i.peso())
def dp_max_set_ind(grafo):
    n = len(grafo)
    dp = [0] * (n+1)
    dp[1] = grafo[1].ganancia()
    for i in range (2, n+1):
        enOptimo = dp[i-2] + grafo[i].ganancia()
        noEnOptimo = dp[i-1]
        if enOptimo > noEnOptimo:
            dp[i] = enOptimo
        else:
            dp[i] = noEnOptimo
    i = n
    sol = set()
    while i > 0:
        if dp[i] == dp[i-1]:
            i -= 1
        else:
            sol.add(grafo[i])
            i-=2
    return dp[n], sol

'''
Redes de Flujo: Dentro de una cuadrícula de n*n celdas hay posiciones de paso y prohibidas. Inicialmente en “p” posiciones al azar se colocan mangueras. También al azar se ubican “p” incendios. El objetivo es lograr estirar las mangueras llevándolas a los incendios. Los movimientos permitidos por las celdas son verticales y horizontales. Por donde pasa una manguera no puede pasar otra. Nos solicitan que determinemos cómo lograr el objetivo o indicar que no es posible.
'''

# Para la reconstruccion simplemente agarro el grafo original y me fijo desde cada nodo que representa una celda donde arranca una manguera cuales de sus aristas contienen flujo 1, o sea que pasaron por ahi. Asi hasta llegar a un incendio y completar el camino de esa manguera.

'''
Clases de Complejidad: Un inspector debe recorrer “n” aeropuertos. Conoce el precio de cada vuelo directo disponible (no necesariamente todos los aeropuertos tienen vuelos directos que los unan). El valor de cada viaje lo paga su compañía y le piden que el precio por trayecto no supere un máximo de “p” pesos. No se puede visitar el mismo aeropuerto más de una vez y debe empezar y terminar en el mismo lugar. Demostrar que resolver este problema es NP-C (HINT: Tal vez le resulte útil ciclo hamiltoniano).
'''

# Transformacion
# Cada nodo representa un aeropuerto
# Cada arista entre u y v, representa que existen vuelos entre u y v
# El parametro p se setea en infinito ya que no es una restriccion en ciclo hamiltoniano
# Llamo a problema_aeropuertos(aeropuertos, p = inf)


'''
Clases de complejidad:
La organización de un workshop internacional debe coordinar las
fechas de paneles de exposición. En cada panel se presentan un
conjunto de oradores. Un orador puede estar en varios paneles. Se
cuenta con un total “j” jornadas diferentes donde se pueden
establecer paneles. Se desea generar un procedimiento eficiente
para decidir si es posible cumplir con cumplir con todos los
paneles con todos sus oradores. En caso afirmativo, dar una
posible asignación de paneles por jornada.
Se pide: Demostrar que el problema es NP-Completo.
HINT: Se puede utilizar K-coloreo de grafos.
'''

def certificador_workshop(sol, paneles, jornadas):
    # Para cada jornada en la solucion chequeo que tenga al menos un panel asociado
    # Chequeo que en una misma jornada no haya un orador miembro de mas de un panel de esa jornada
    # Chequeo que todos los oradores existan y que esten en su panel/paneles correspondientes 
    return 0

# Transformacion
    # Cada vertice se transforma en un panel
    # Cada arista u-v refleja que el panel u y el panel v comparten oradores
    # El numero de coloreo k pasa a ser el numero de jornadas j
    # workshop(paneles, j)


# 2 de agosto 2021

'''
Greedy:
El proceso de aprobación de trámites de la “central burocrática”
está dividido en 2 partes. La primera parte consiste en una
entrevista personalizada cuya duración se puede conocer según el
tipo de trámite. La segunda parte es la revisión de la
documentación cuya duración se calcula previamente mediante una
fórmula matemática en función de la persona solicitante. Cada día
se citan “n” personas. Cada una para realizar un trámite. Por cada
persona se cuenta, entonces, con su tiempo de la etapa 1 y su
tiempo de la etapa 2. La etapa 1 únicamente la realiza 1 empleado.
Para la etapa 2, hay una cantidad ilimitada de personal para
realizarla. Nuestra tarea es determinar el orden de atención para
cada una de las “n”. El objetivo es minimizar el tiempo total de
la jornada laboral.
Presentar una solución greedy que resuelva el problema. Explicar
la optimalidad del mismo.
'''

def minimo_tiempo_tramites(personas):
    personas.sort() # Ordeno personas por t2 decreciente

    t_global = 0
    t_tramite_1 = 0
    for persona in personas:
        t_tramite_1 += persona.t1
        t_final_persona = t_tramite_1 + persona.t2
        if t_final_persona > t_global:
            t_global = t_final_persona
    
    return t_global

'''
Programación dinámica:
Recordemos al problema 2-Partition: Se cuenta con un conjunto de
“n” elementos. Cada uno de ellos tiene un valor asociado. Se desea
separar los elementos en 2 conjuntos que cumplan con: La suma de
los valores de cada conjunto sea igual entre ellos. Se puede ver
que este corresponde a un problema NP-C. Sin embargo - al igual
que otros problemas en esta clase como el problema de la mochila -
puede ser resuelto utilizando programación dinámica.
Proponga un algoritmo utilizando programación dinámica que
resuelva cualquier instancia de 2-Partition. Analice su
complejidad temporal y espacial.
'''

def two_partition(arr):
    total = sum(arr)
    if total % 2 !=0: return None

    n = len(arr)
    target = total / 2
    dp = [False] * (target+1)
    dp[0] = True
    padre = [-1] * (target+1)
    for i in range(0, n+1):
        num = arr[i]
        if num > target:
            continue
        
    return

'''
Redes de Flujo:
Para satisfacer la producción de un producto electrónico una
empresa debe comprar un componente a sus diferentes proveedores.
Cada proveedor tiene una cantidad máxima que puede ofrecer
mensualmente. Además las diferentes plantas de producción demandan
una cantidad mensual del mismo. Por cuestiones logísticas algunos
proveedores no pueden enviar a ciertas plantas de producción. El
mes próximo por una promoción se va a tener que producir al 100%
de la capacidad. Determinar en forma eficiente si es posible
satisfacer esta demanda.
Explicar detalladamente y paso a paso la solución propuesta.
Analizar complejidad
'''

'''
Clases de Complejidad / Reducciones:
Un instituto de enseñanza debe coordinar las fechas de exámenes
finales de sus respectivos cursos. En cada curso se anotaron
varios alumnos. Y un alumno puede estar en varios cursos. En total
se cuenta con “k” fechas posibles de examen. Se desea generar un
procedimiento eficiente para decidir si es posible cumplir con ese
requerimiento. En caso afirmativo, dar una posible asignación de
exámenes por fecha.
Se pide: Demostrar que el problema es NP-Completo.
HINT: Se puede utilizar K-coloreo de grafos.
'''

# Igual que los paneles y oradores

# 5 de abril de 2021

'''
1) Luego de aprender programación dinámica un estudiante en una
charla de café le explica a un amigo que atiende un negocio el
algoritmo de cambio mínimo de monedas. Con eso, afirma, podrá
optimizar el despacho de mercadería. El comerciante despacha
pedidos de cierto producto que viene en empaques prearmados de
distintas cantidades o en unidades sueltas. Sin embargo, el amigo
le replica que su algoritmo es poco realista. Supone que uno tiene
una cantidad ilimitada de empaques de cada presentación. Luego de
pensar unos momentos, el estudiante llega a una variante de este
problema teniendo en cuenta esta restricción. ¿Podría usted
detallar cuál es esta solución? Describa paso a paso y explique
con un ejemplo cómo funciona.
'''


'''
Greedy:
Un centro de distribución de repuestos ferroviarios se
encuentra en un punto de la red de este transporte. Es la
encargada de distribuir a demanda los materiales y recursos para
las reparaciones que solicitan las diferentes estaciones. Como la
red es antigua y está mal mantenida la cantidad de kilos que se
puede transferir sobre cada trayecto es variable. Esto para ellos
es un problema porque quieren enviar la mayor cantidad posible de
material por viaje. Tanto es así que no les importa realizar un
camino más largo siempre que eso implique transportar más
materiales.
Se pueden armar diferentes caminos que unan el centro de
distribución con cada estación. Estos estarán conformados por una
secuencia de trayectos, cada uno con su propia limitación de kilos
que soporta. Llamamos cuello de botella al valor mínimo entre
ellos.
Construir un algoritmo greedy que permita calcular el camino con
el máximo cuello de botella entre el punto de partida y el resto
de los puntos. ¿Qué complejidad tiene? Demuestre que es óptima su
solución.
'''

# Resuelto en guia

'''
Para el desarrollo de un circuito digital se requiere construir
“n” caminos por donde pasará corriente eléctrica. Por diseño cada
uno de esos caminos debe empezar en un determinado punto y
finalizar en otro. Por supuesto, estos caminos no deben cruzarse.
Para la construcción de este circuito se cuenta diferentes capas
conductoras en los que se pueden imprimir diferentes caminos. Pero
esto se puede abstraer como una grafo donde cada vértice
corresponde a una región por la puede pasar un camino y los ejes
las regiones circundantes con las que puede conectarse.
Se pide: Demostrar que el problema es NP-Completo.
HINT: El problema se puede ver como “Node-disjoint directed path
problem”. Pruebe con “3-SAT”
'''

# Preguntar

# 14 de Abril 2021

'''
Para un evento a realizar se requiere conformar una selección
musical entre el conjunto A de “n” canciones. Podemos enumerar a
los elementos de A como a1,a2,...,an. Por otra parte, contamos con
un conjunto “B” de “m” personas. Cada una de ellas con un subsets
de esas canciones que le gustan. Deseamos saber si podemos
seleccionar un subconjunto de no más de “k” canciones, de tal
forma que existe al menos 1 canción que le gusta a cada uno.
Se pide: Demostrar que el problema es NP-Completo.
HINT: Se puede utilizar Vertex Cover.
'''

# Cada vertice es una cancion
# cada arista u-v es una persona que le gustan las canciones u y v

# 23 de Agosto 2021

'''
Redes de Flujo:
Una ciudad tiene una red inalámbrica interna para interconectar
diferentes servidores de varias instituciones públicas. Existen un
conjunto "A" de antenas de interconexión que están dispersas por
la ciudad. Cada una de ellas tiene una localización "x,y", un
alcance de recepción limitado (un radio "R_a") y una cantidad
máxima de conexiones que puede tener en forma simultánea. Se
recopiló una lista "S" de servidores, cada uno de ellos con su
ubicación "x,y"
Determinar si es posible que todos los servidores pueden estar
conectados a una antena respetando las restricciones impuestas.
Explique paso a paso la solución propuesta y analice su
complejidad temporal.
'''

'''
Clases de Complejidad / Reducciones:
Se requiere realizar un viaje a través de un territorio de difícil
acceso. El mismo se encuentra dividido en zonas por las que se
debe pasar. Existen m facciones que controlan algunas de esas
zonas. Una facción puede controlar más de 1 zona y una zona puede
ser controlada por más de una. Para poder realizar el viaje se
debe pactar con alguna de estas. Cada pacto con una facción nos
asegura el paso seguro por todas las zonas que controlan
independientemente de si alguna de sus zonas son también
controladas por otras facciones. Deseamos saber si es posible
pactar con no más de k facciones para poder concretar el viaje de
forma segura.
Se pide: Demostrar que el problema es NP-Completo.
HINT: Se puede utilizar Vertex Cover.
'''

# Cada nodo es una faccion
# Cada arista u-v es una zona controlada por las facciones u y v


'''
Redes de Flujo:
Una empresa de autobuses se conformó luego de la fusión de varias
compañías menores. Actualmente tienen diferentes rutas que cubrir.
Cada una con horario de inicio en una ciudad y finalización en
otra. Existe la posibilidad de cubrir con un mismo micro
diferentes rutas.
Siempre la ruta comienza desde donde parte el micro, pero también
puede pasar que el micro tenga tiempo suficiente para trasladarse
hasta otro punto y cubrir otra ruta. Cuentan con una flota activa
de N micros. Necesitan saber si les es posible cubrir con ella los
requerimientos o si requieren contar con micros extra.
Resolver el problema utilizando como parte del mismo redes de
flujo. Analice su complejidad temporal y espacial.
'''

# Aristas con limite inferior cero

'''
Clases de Complejidad / Reducciones:
El proyecto de colonización de Marte lleva años desarrollándose en
secreto. En una nueva etapa se requieren N granjeros-espaciales
para terraformar una hectárea del suelo marciano. Se realizó una
amplia búsqueda de candidatos “r” (r>>n), siendo todos ellos
capaces. Dadas las duras condiciones que enfrentarán, es
primordial que sean compatibles entre ellos. Se realizaron
complejos estudios psicológicos y se construyó una tabla donde
para cada granjero se indica con cuáles otros puede trabajar sin
conflictos. En este momento quieren saber si los candidatos
disponibles pueden armar la tripulación necesaria.
Demuestre que lo solicitado es NP-COMPLETO
HINT!: Tal vez le resulte útil clique
'''

# Cada nodo es un granjero
# Cada arista u-v es una compatibilidad del granjero u con v

# Puntos mas cercanos en un plano

def closest_pairs_rec(px, py):
    # if len(px) <= 3: return el mínimo de comparar cada punto
    
    # Construir Qx, Qy, Rx, Ry (O(n))
    
    # q0, q1 = closest_pairs_rec(Qx, Qy)
    # r0, r1 = closest_pairs_rec(Rx, Ry)
    
    # d = min(d(q0, q1), d(r0, r1))
    # x* = máxima coordenada x de Qx
    
    # S = puntos de P que están a distancia <= d de la recta x = x*
    
    # Construir Sy (O(n))
    
    # por cada punto s de Sy computar distancia contra los siguientes 15 puntos
    #     quedarse con s y s' que minimizan esa distancia
        
    # if d(s, s') < d: return s, s'
    # elif d(q0, q1) < d(r0, r1): return q0, q1
    # else: return r0, r1
    return 0

# Cambio minimo dinamica
# opt[i]: cantidad minima de monedas para devolver i pesos
# opt[i]: 1 + min{opt[i-j]} donde j <= i

def cambio_minimo(sist_monetario, dinero):
    cant = [float("inf")] * (dinero + 1)
    cant[0] = 0

    monedas_usadas = [[] for valor in sist_monetario]
    monedas_usadas[0] = []
    for i in range(1, dinero + 1):
        for moneda in sist_monetario:
            if moneda <= i:
                if cant[i-moneda] < cant[i]:
                    cant[i] = 1 + cant[i - moneda]
                    monedas_usadas[i] = monedas_usadas[i-moneda] + [moneda]

    return cant[dinero], monedas_usadas[dinero]


'''
Una empresa que realiza ciencia de datos debe realizar en las próximas “n” semanas procesos y cálculos intensivos. Para eso debe contratar tiempo de cómputo en un data center. Realizando una estimación conocen cuantas horas de cómputo necesitarán para cada una de las semanas. Por otro lado luego de negociar con los principales proveedores tienen 2 opciones que pueden combinar a gusto: ● Opción 1: Contratar a la empresa “Arganzón” por semana. En
esa semana se cobra proporcional al tiempo de cómputo según un parámetro “r” (horas computo x r). ● Opción 2: Contratar a la empresa “Fuddle” por un lapso de 3 semanas contiguas. Durante el lapso contratado se paga una
tarifa fija de “c”. Proponer una solución utilizando programación dinámica que nos indique la secuencia de elecciones a realizar para minimizar el costo total de cómputo. Analizar su complejidad temporal y espacial.'''

def plan_minimo(H, r, c):
    n = len(H)
    dp = [0] * (n + 3) 
    decision = [""] * n

    for i in range(n - 1, -1, -1):
        cost_arganzon = H[i] * r + dp[i + 1]
        cost_fuddle = c + dp[i + 3]
        if cost_arganzon <= cost_fuddle:
            dp[i] = cost_arganzon
            decision[i] = "A"
        else:
            dp[i] = cost_fuddle
            decision[i] = "F"

    elecciones = []
    i = 0
    while i < n:
        if decision[i] == "A":
            elecciones.append(("A", i))
            i += 1
        else:
            elecciones.append(("F", i))
            i += 3
    return dp[0], elecciones