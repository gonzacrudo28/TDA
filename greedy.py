import heapq
'''
⭐Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo) contiene el número de kilómetros donde está ubicada cada una. Se desea ubicar la menor cantidad de patrullas policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km. Proponer un algoritmo que lo resuelva. 

Ejemplo (ciudad,Bifurcación): (Castelli, 185), (Gral Guido, 249), (Lezama 156), (Maipu, 270), (Sevigne, 194).	Si incluimos un patrullero en la bifurcación de Lezama, cubre además de esta a Castelli y Sevigne. Pero no Gral Guido y Maipú. Se necesitaría en ese caso, ubicar otro. Al agregar otro patrullero en Gral Guido, se cubren todas las ciudades restantes. Con 2 móviles policiales en bifurcaciones se cubren todas los accesos a todas las ciudades con distancia menor a 50km.
'''

def colocar_patrulla(pueblos):
    pueblos.sort() #ordeno por ubicacion (creciente)
    patrullas = set()
    i = 0
    n = len(pueblos)
    inicio = pueblos[0].ubicacion
    for i in range(0, len(pueblos)):
        if pueblos[i].ubicacion - inicio > 50:
            patrullas.add(pueblos[i-1])
            inicio = pueblos[i-1].ubicacion
    if  pueblos[-1].ubicacion - inicio > 50:
        patrullas.add(pueblos[-1])
    return patrullas
        
#Complejidad Temporal: O(n log n) por ordenar 

'''
⭐⭐Para la realización del próximo congreso de “charlas motivacionales para el joven de hoy” se contrató un hotel que cuenta con “m” salas de exposición. Existirán “n” oradores. Cada uno solicitó un tiempo de exposición definido por un horario de ingreso y una duración. Los organizadores quieren asignar las salas con un intervalo entre charla y charla de 15 minutos y desean utilizar la menor cantidad de salas posibles. Presentar un algoritmo greedy que resuelve el problema indicando la cantidad de salas a utilizar y la asignación de las charlas. En caso de sobrepasar el máximo de salas disponibles informar. Analice complejidad y optimalidad 
'''

# m salas de exposicion
# n oradores
# hora de ingreso + duracion + 15 minutos

def asignar_salas(charlas, m):
    #a todos los horarios de finalizacion de las charlas le añado 15 minutos 
    charlas.sort() #las ordeno por fecha de inicio
    heap_salas = heapq()
    n = 1
    heap_salas.push(charlas[0].finalizacion)
    dicc={}
    numero_sala = 0
    dicc[charlas[0]] = numero_sala
    for charla in charlas:
        if heap_salas.peek() > charla.inicio:
            n += 1
            heap_salas.push(charla.finalizacion)
            numero_sala += 1
            dicc[charla] = numero_sala
        else:
            charla_saliente = heap_salas.pop()
            dicc[charla] = dicc[charla_saliente]
            heap_salas.push(charla.finalizacion)
    if n > m:
        print("Se necesitan mas salas")
    return dicc

#Complejidad Temporal: O(n log n)
#Complejidad Espacial: O(n) en el hash siempre van a estar todas las charlas

'''
⭐⭐Una carrera tipo “Ironman” es un triatlón compuesto por 3 instancias: natación (3,86 km de natación), ciclismo (180 km) y carrera a pie (42,2km). Para conocer al ganador se suman los tiempos realizados en cada una de las etapas. Tanto el ciclismo como la carrera a pie se puede realizar en simultáneo con todos los inscriptos. Pero, por una regulación se prohibió que más de 1 persona realice la etapa de nado en el lago en simultáneo. Se conoce el tiempo estimado de cada participante para cada evento. Proponga un orden de salida de tal forma de minimizar el tiempo total de toda la competencia.
'''
def ironman(participantes):
    #ordeno participantes por tiempo de natacion creciente y en caso de empate, defino por el que tarde más en el resto de las disciplinas
    return


'''
⭐El club de amigos de la república Antillense prepara un ágape en sus instalaciones en la que desea invitar a la máxima cantidad de sus “n” socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Sólo puede asistir si conoce a al menos otras 4 personas invitadas. Nos solicita seleccionar el mayor número posible de invitados. Proponga una estrategia greedy óptima para resolver el problema
'''
def invitar_gente(personas):
    cola = cola()
    for persona in personas:
        if persona.conocidos < 4:
            cola.encolar(persona)
    while not cola.esta_vacia():
        persona = cola.desencolar()
        for conocido in persona.conocidos_p:
            conocido.conocidos -=1
            if conocido.conocidos < 4:
                cola.encolar(persona)
    invitados = []
    for persona in personas:
        if persona.conocidos >= 4:
            invitados.append(persona)
    return invitados

#Complejidad Temporal: O(n+k) k es la cantidad de relaciones totales entre las personas.
 

'''
El ajedrez se juega con un tablero cuadriculado. La pieza llamada “Rey” puede moverse en cualquiera de los 8 cuadrados aledañas a su posición actual comiendo cualquier otra pieza que esté en ellos. Contamos con un tablero especial de nxm cuadrados y una cantidad ilimitada de piezas “Rey”. Queremos ubicar la mayor cantidad de reyes sin que estos se puedan comer entre si. Proponer un algoritmo greedy para resolverlo. Brindar complejidad. Justificar la optimalidad de su propuesta.
'''
# Recorrer de 2 en 2 cada fila salteando la siguiente.

'''
⭐⭐Un centro de distribución de repuestos ferroviarios se encuentra en un punto de la red de este transporte. Es la encargada de distribuir a demanda los materiales y recursos para las reparaciones que solicitan las diferentes estaciones. Como la red es antigua y está mal mantenida la cantidad de kilos que se puede transferir sobre cada trayecto es variable. Esto para ellos es un problema porque quieren enviar la mayor cantidad posible de material por viaje. Tanto es así que no les importa realizar un camino más largo siempre que eso implique transportar más materiales. Se pueden armar diferentes caminos que unan el centro de distribución con cada estación. Estos estarán conformados por una secuencia de trayectos, cada uno con su propia limitación de kilos que soporta. Llamamos cuello de botella al valor mínimo entre ellos. Construir un algoritmo greedy que permita calcular el camino con el máximo cuello de botella entre el punto de partida y el resto de los puntos.
'''

def camino_maximo(grafo, origen):
    cuello_de_botella = {}
    padre = {}
    for v in grafo:
        cuello_de_botella[v] = 0
    cuello_de_botella[origen] = float("inf")
    padre[origen] = None
    q = heapq
    q.encolar(origen, cuello_de_botella[origen])
    while not q.esta_vacia():
        v, cb = q.pop()
        for w in grafo.adyacentes(v):
            nuevo_cb = min(cb, grafo.peso_Arista(v, w))
            if nuevo_cb > cuello_de_botella[w]:
                cuello_de_botella[w] = nuevo_cb
                padre[w] = v
                q.encolar(w, nuevo_cb)
    return padre  

#Complejidad Temporal O((V+E) log V)
#Complejidad Espacial O(V)                

'''
⭐⭐Una jefa de trabajos prácticos (jtp) está a cargo de un grupo de N ayudantes, cada uno de los cuales tiene que trabajar un turno completo durante la semana. Hay muchas actividades asociadas con cada turno (atender el laboratorio, dar clase de consultas, etc.) pero podemos pensar en un turno como un intervalo de tiempo contiguo. Puede haber más de un turno simultáneamente. La  Jtp está tratando de construir un subconjunto de esos N ayudantes para formar un comité de supervisión, que esté en contacto con todos los ayudantes. Un comité de supervisión está en contacto con todos los ayudantes si, cualquiera sea el turno de un ayudante, hay alguien en el comité de supervisión cuyo turno se superpone, aunque sea parcialmente, con el turno de ese ayudante. Ejemplo: N=3, ayudante 1 = Lunes de 16 a 20, ayudante 2 = Lunes de 18 a 22, ayudante 3 = Lunes de 21 a 23. En este caso, la solución es {ayudante 2}. Dado un conjunto de ayudantes, diseñar un comité de supervisión lo más pequeño posible, usando una estrategia greedy.
'''

def comite_supervision(turnos):
    n = len(turnos)
    if n == 0:
        return set()
    
    # ORDENAR POR INICIO CRECIENTE
    intervalos_ordenados = [(inicio, fin, idx) for idx, (inicio, fin) in enumerate(turnos)]
    intervalos_ordenados.sort(key=lambda x: x[0])
    
    comite = set()
    i = 0
    while i < n:
        inicio_actual, fin_actual, idx_original = intervalos_ordenados[i]
        mejor_indice = i
        max_fin = fin_actual
        
        # Buscar el mejor candidato que se superponga con el intervalo actual
        j = i + 1
        while j < n:
            inicio_j, fin_j, idx_j = intervalos_ordenados[j]
            if inicio_j > fin_actual:
                break
            if fin_j > max_fin:
                max_fin = fin_j
                mejor_indice = j
            j += 1
        
        # Añadir el mejor candidato al comité
        candidato = intervalos_ordenados[mejor_indice][2]
        comite.add(candidato)
        
        # Avanzar hasta el primer intervalo no cubierto por el candidato
        fin_candidato = intervalos_ordenados[mejor_indice][1]
        while i < n and intervalos_ordenados[i][0] <= fin_candidato: #Mientras intervalos_ordenados[i].inicio <= fin_candidato -> avanzo
            i += 1
    
    return comite

'''
⭐⭐Una familia planea un viaje. Tienen pensado salir desde su ciudad a una determinada hora y llegar lo antes que puedan a la ciudad de destino. Para hacer el viaje cuentan con diferentes opciones de recorridos. Diferentes rutas pasan por diferentes pueblos y se ramifican en otras rutas diferentes. Cada trayecto cuenta con una longitud que - teniendo en cuenta el límite de velocidad - les permite establecer el tiempo que les llevará recorrerlo. Por otro lado, conocen el tráfico por hora de cada trayecto. Esto es, el tiempo extra que le insume realizar un trayecto si inician el recorrido en una determinada hora. Construir un algoritmo greedy que determine el mejor camino a realizar en el menor tiempo posible.
'''

'''
⭐⭐Para habilitar la realización de un importante evento multideportivo se solicitó como precondición que durante el lapso que dura cada actividad exista junto a la misma personal médico. Conocemos para cada una de las “n” actividades a realizar, el momento de inicio y final. Como encargados de la inspección nos solicitan que programemos la menor cantidad de inspecciones posibles en las que constatamos que (al menos al momento de la inspección) se cumple la precondición. Una inspección verifica únicamente aquellos eventos que se están llevando a cabo en el momento. Ninguna actividad debe quedar sin inspeccionar. Presentar una solución greedy óptima al problema.
'''

'''
⭐Nos proponen el siguiente juego de cartas en el que tenemos que adivinar la carta que tiene un rival. El mazo tiene 1 carta de “1 de Oro”, 2 cartas de “2 de Oro” y así hasta 9 cartas de “9 de Oro”. El rival mezcla y selecciona una carta. Mediante preguntas que solo se pueden responder por sí o por no tenemos que averiguar en la menor cantidad de consultas cual es la carta. (ejemplos: “La carta es mayor a 4?, “La carta es un “1” o un “3”, etc). Proponer un algoritmo greedy que resuelva el problema minimizando la cantidad probable de preguntas a realizar.
'''

'''
⭐⭐Un servidor de videojuegos se alquila por horas. El contrato dura un tiempo fijo y permite utilizar en forma exclusiva el mismo por una cantidad continua de horas una vez por semana. Por cada contrato que el dueño del servidor establece, se lleva un monto fijo de dinero. Al dueño del servidor le interesa tener la mayor cantidad de contratos posibles (sin importar la duración en horas de los mismos). El servidor funciona las 24hs. Recibe un conjunto de ofertas de contrato y debe seleccionar cuales aceptar. Cada contrato tiene un día y hora de inicio y un día y hora de fin. Durante ese lapso tendrán la exclusividad del servidor. Ese tiempo contiguo no puede durar más de 1 semana (un contrato podría pedir por ejemplo 3 días completos pero nunca superar la semana).. Y esa fecha se repite todas las semanas. Los contratos aceptados no deben superponerse. Proponer una solución greedy que solucione el problema de forma óptima. Tenga en cuenta que es posible contratos que empiecen al finalizar la semana y terminen horas después del inicio de la misma.
'''

'''
⭐Una fotocopiadora cada mañana recibe un conjunto de pedidos de clientes. El pedido del cliente i demora ti en ejecutarse. Para una planificación dada (es decir un cierto orden de las tareas) Ci es la hora en la cual el pedido i termina de ejecutarse (por ejemplo, si el pedido j es el primero que se ejecuta, Cj = tj; si el pedido j se ejecuta a continuación del pedido i, Cj=Ci+tj). Cada cliente tiene un peso wi que representa su importancia. Se supone que la felicidad de un cliente depende de cuán rápido le entregan el trabajo, por lo que la empresa decide minimizar el tiempo de demora ponderado = Suma (wi * Ci). Diseñar un algoritmo greedy eficiente para resolver este problema. 
'''

'''
⭐Contamos con una impresora central en un centro de cómputos del campus universitario. Entre varios departamentos y laboratorios nos solicitan al inicio de cada mes, la impresión de “n” documentos. Cada uno de ellos tiene una duración determinada y cuenta con una fecha de entrega. Si nos pasamos de esta recibimos un apercibimiento proporcional al retraso más largo del mes. Como a la impresora le falta mantenimiento queremos lograr - siempre que sea posible - tiempo entre los trabajos de impresión. Presentar un algoritmo greedy que dada la lista de tareas proponga la fechas de inicio de publicación minimizando el apercibimiento y dando tiempo entre las tareas siempre que sea posible. 
'''


