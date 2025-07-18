'''
⭐Problema del camino más largo en un grafo general con aristas sin peso: Dados G = (V, E) un grafo no dirigido y un natural k, determinar si existe un camino simple en G de longitud >=k. Probar que es un problema NP-completo (Usar el problema del camino hamiltoniano para probarlo).
'''
#Se puede construir polinomialmente un certificador

def cert_camino_mas_largo(grafo, k, camino):
    if len(camino) < k:
        return False
    visitados = set()
    contador = 0
    for nodo in camino:
        if not nodo in grafo:
            return False
        if nodo in visitados:
            return False
        visitados.add(nodo)
        if contador + 1 < camino.len():
            if not camino[contador + 1] in grafo.adyacentes(nodo):
                return False
        contador += 1
    return True
#O(n) donde n es la cantidad de elementos y es mayor o igual a k
# Camino Hamiltoniano (grafo)
#     k = len(grafo)
#     Camino_simple(grafo, k)

'''
⭐La siguiente es una versión de Conjunto Independiente. Dado un grafo G= (V, E) y un entero k, decimos que I ⊆ V es fuertemente independiente si dados dos vértices u y v en I, la arista (v, u) no pertenece a E y además no hay ningún camino de tamaño 2 (con dos aristas) de u a v. El problema de Conjuntos Fuertemente Independientes consiste en decidir si G tiene un conjunto fuertemente independiente de tamaño al menos k. Probar que el problema de Conjuntos Fuertemente Independientes es NP completo. Utilizar para ello que Conjuntos Independientes es NP completo.
'''
#Agregar un nodo intermedio entre cada par de nodos adyacentes.


'''
⭐Una agencia de marketing coloca publicidad en la Web. Se han ilusionado con vender publicidad con la siguiente idea, que llamaremos el problema de la Publicidad Estratégica: Un sitio Web se puede modelar como un grafo G = (V, E). Las acciones habituales de los usuarios que visitan un sitio se pueden modelar mediante “t” recorridos posibles P1, P2, ... , Pt (donde cada Pi es un camino dirigido en G). Dado un número k, se quieren elegir a lo sumo k vértices en G para poner publicidad, de modo tal que todos los “t” recorridos habituales pasen por al menos uno de esos vértices. Tenemos que mostrarle a esta empresa que  su idea no es realizable por el momento ya que el problema de la Publicidad Estratégica es NP-completo. Sugerencia: relacionarlo con cubrimiento de vértices.
'''
#Tengo vertices donde cada uno es una acción y las acciones "correlativas" se conectan mediante una arista.
#Para cada nodo, veo sus ady y pongo las aristas en un set, tambien como parametro recibo todas las aristas del grafo. Me fijo que los conjunttos sean iguales y de tamaño k y que cada vertice pertenezca al grafo
def certificador_pub_estrategica(grafo, aristas, conjunto, k):
    if len(conjunto) > k:
        return False
    aristas_conjunto = set()
    for nodo in conjunto:
        if not nodo in grafo.nodos():
            return False
        for ady in nodo.ady():
            if not ady in grafo.nodos():
                return False
            if (nodo,ady) in aristas_conjunto:
                return False
            if (nodo, ady) not in aristas:
                return False
            aristas_conjunto.add((nodo, ady))
    return len(aristas_conjunto) == len(aristas)

#Vertex Cover(grafo, k):
# Lo transformo en dirigido agregando aristas opuestas a-b, a->b y b->a
# Publicidad Estratégica (grafo, k)


'''
⭐Nos piden que organicemos una jornada de apoyo de estudio para exámenes. Tenemos que poder dar apoyo a “n” materias y hemos recibido currículos de “m” postulantes para ser potenciales ayudantes. Cada ayudante puede ayudar en un determinado subconjunto de materias. Para cada una de las materias hay un subconjunto de postulantes que pueden dar apoyo en ella. La pregunta es: dado un número k < m, ¿es posible seleccionar a lo sumo “k” ayudantes de modo tal que siempre haya un ayudante que pueda dar consultas en alguna de las n materias? Este problema se llama Contratación Eficiente. Probar que “Contratación Eficiente” es NP-completo. Sugerencia: se puede tratar de usar Cubrimiento de Vértices.
'''

def cert_ayudantes(postulantes, materias, k, solucion):
    if len(solucion) > k: return False
    utilizados = set()
    materias_cubiertas = set()
    for materia, ayudante in solucion.items():
        if not ayudante in postulantes or ayudante in utilizados:
            return False
        if materia not in materias or materia not in ayudante.materias_posibles():
            return False
        utilizados.add(ayudante)
        materias_cubiertas.add(materia)
    return materias_cubiertas == materias

#Vertex Cover es cubrir todas las aristas usando la menor cantidad de vertices posibles. 
#Pensar a la materia como una arista, y los vertices los ayudantes.

'''
⭐Se conoce Bin-Packing al problema de decisión donde se cuenta con “N” elementos de diferentes pesos y con “M” contenedores de cierta capacidad. Queremos saber si es posible acomodar todos los elementos en no más de k contenedores. Se pide demostrar que el problema es NP-Completo. Sugerencia utilizar 2-partition.
'''
# 2-Partition(conjunto)
#     M = 2
#     Capacidad M = conjunto.peso()/2
#     Bin-Packing(conjunto, M, 2)

'''
⭐Un grupo de amigos que conviven están mudándose a un departamento nuevo. Han juntado sus pertenencias en cajas de diferentes volúmenes que recolectaron en supermercados y tiendas. Al llegar la compañía de mudanza les informan que por normativa únicamente transportarán utilizando como contenedores sus recipientes de volumen V. Por lo tanto, los amigos deben ingresar sus cajas en los contenedores autorizados. En el camión entran como máximo “r” recipientes. Al llenarse realiza el trayecto para descargar y regresar a cargar otros contenedores. Antes de proceder quieren saber si podrán acomodar todas sus cajas de tal forma que puedan realizar menos de k viajes. Demostrar que es un problema NP-Completo. Sugerencia: Este problema es fácilmente relacionable con Bin Packing.
'''
# bin-packing(K, M):
#     viajes_neces


'''
⭐⭐Definimos el problema Subgrafo denso de la siguiente manera: Dado un grafo G=(V,E) y dos parámetros a y b. Existe en G un subconjunto S de al menos “a” vértices con al menos “b” ejes entre ellos. Demostrar que este problema es NP-Completo. Sugerencia: Utilizar el problema del Clique.
'''
# Clique(Grafo, k):
#   a = k
#   b = a*(a-1)/2
#   Subgrafo denso(G, a, b)

'''
⭐Definimos al problema de Set Packing como: Dado “n” conjuntos S1,S2,...,Sn y un parámetro k. Queremos saber si existe una colección de tamaño k de los subconjuntos tales que ningún elemento contenido en ellos está repetido en estos “k” conjuntos? Demostrar que este problema es NP-Completo. Sugerencia: Utilizar Conjunto independiente.
'''
# Independent_set(grafo, k):
    # el Universo de elementos es el conjunto E de aristas
    # Por cada vertice del grafo creo un subconjunto
    # por cada arista del grafo la tomo como un elemento y lo añado a cada subconjunto de sus extremos
    # set_packing (subconjuntos, k)
'''
⭐Dado un grafo G=(V,E) no dirigido se denomina como Feedback set a un subconjunto X⊆V de vértices tal que el grafo resultante de eliminar los vértices de X y los ejes adyacentes a estos no tiene ciclos. El problema de decisión de Undirected Feedback Set quiere responder si dado un grafo G no dirigido existe un feedback set de tamaño k o menor. Demostrar que este problema es NP-Completo. Sugerencia: Utilizar Vertex Cover.
'''
# Vertex-cover(grafo, k):
    # Sea G' = G 
    #Por cada arista entre u y v, agrego a G' un vertice w y lo uno tanto con u como con v, formando ciclo de 3 vertices
    #Undirected-Feedback-Set(G', k)
    # El conjunto de vertices eliminados coincide con el conjunto de vertices cubridores
'''

⭐⭐Definimos el problema DOBLE-SAT como: dado una fórmula booleana determinar si existen dos asignaciones de variables que satisfacen a la misma. Probar que DOBLE-SAT pertenece a NP-C. Sugerencia: Utilizar 3SAT
'''

'''
⭐ Una compañía multinacional desea contratar cobertura satelital para sus “n” sedes repartidas por el mundo. Han averiguado entre varias empresas que proveen el servicio pero ninguna de ellas tiene cobertura total. Les gustaría poder contratar a “k” o menos empresas. Pero tienen una condición adicional: al menos una de sus sedes debe tener cobertura de todas las empresas que la ofrecen. Con eso pueden iniciar una certificación de calidad que necesitan. Se pide: Demostrar que el problema es NP-Completo. Sugerencia: Utilizar Set Cover
'''
# U = {1, 2, 3, 4}
# S1 = {1, 2}
# s2 = {3}
# S3 = {4}

# U' = U + {X}
# S1' = S1 + X

'''
⭐⭐ El problema del Ciclo Hamiltoniano dirigido corresponde a una variante del problema de Ciclo Hamiltoniano con la diferencia que la instancia corresponde a un grafo dirigido. Demostrar que este problema pertenece a NP-C. Sugerencia: Puede utilizar Ciclo Hamiltoniano.
'''
# Changuita, haces el grafo bidireccional
'''
⭐ La elaboración de una flota de “n” minisatélites requiere la integración de 4 componentes cuyos códigos de identificación son pA, pB, pC y pD. Contamos con “n” piezas de cada uno de ellos. Un estudio de compatibilidad informa que no cualquier cuadrupla de piezas es viable para ensamblar el satélite. Nos proveen un listado de las cuadruplas que si pueden conformarlos. Queremos saber si es posible seleccionar de forma adecuada las piezas para armar los “n“ satélites. Se pide: Demostrar que el problema es NP-Completo. Sugerencia: Se puede utilizar 3 Dimensional Matching
'''

'''
⭐⭐ Un artesano puede contratar x máquinas de impresión 3D. Se ha comprometido en realizar un conjunto de “N” pedidos. Cada pedido “i” cuenta con un tiempo “ti” en horas de realización. Dentro de D días debe entregarlas. Nos solicita que encontremos un procedimiento que le indique si es posible realizarlo en el tiempo disponible y programar que pedido realizar en cada máquina. Demostrar que el problema es NP-C. Sugerencia: Puede utilizar 2-partition
'''
#Cada elemento del conjunto total representa la duracion de una tarea. El numero total de elementos es el numero total de pedidos. El x (cantidad) de maquinas es 2
#La duracion total de cada maquina es la suma de todas las tareas / 2
'''
⭐ Un departamento dentro de una universidad adquirió “n” proyectores para dar clases durante el cuatrimestre. Envió un formulario a los docentes de las distintas materias para conocer si los necesitaban como complemento para sus clases. Un subconjunto de docentes respondió afirmativamente. Sabiendo que cada materia tiene clases 1 o más veces por semana en un horario establecido. Y sabiendo que los horarios de varias de esas materias se superponen. Nos solicitan determinar si la cantidad comprada alcanza o si se tiene que dejar a docentes sin acceso a esas cuentas. Demostrar que lo solicitado es NP-COMPLETO. Sugerencia: Tal vez le resulte útil “k” coloreo de grafos.
'''
#Cada nodo es una clase, las conecto entre las que se superponen A->B (A y B se superponen)
#K va a ser la cantidad de proyectores comprados
#Si puedo pintar el grafo, significa que me alcanzan

'''
⭐ Para elaborar una película de detectives un grupo de escritores se ha juntado para elaborar una trama atrapante y que tenga coherencia. En largas jornadas han propuesto un gran conjunto de premisas, giros argumentales y eventos claves. Lamentablemente algunas de ellas no son compatibles entre sí. Por cada situación han anotado con cual no es compatible. Desean poder seleccionar un conjunto de N premisas compatibles para presentar a los productores como idea inicial. Se pide: Demostrar que el problema es NP-Completo. Sugerencia:  Tal vez le resulte útil clique
'''
#Cada nodo es una pelicula, las conecto entre las compatibles. 

'''
⭐⭐ El plan de evacuación ante ataques zombies/alienígenas de la ciudad implica poder trasladar a los más importantes científicos, militares y políticos designados a refugios. Diferentes ramas y organizaciones gubernamentales presentaron diferentes rutas de evacuación. Cada una corresponde un punto de encuentro, un recorrido y un refugio. En total existen N rutas presentadas. Es importante que ninguna ruta comparta o se cruce en su recorrido con otra para maximizar la posibilidad de supervivencia. Debemos responder si con las propuestas se pueden seleccionar al menos K caminos de tal forma que cumpla estas restricciones. Demuestre que lo solicitado es NP-COMPLETO. Sugerencia: Se puede realizar con 3 Dimensional Matching o INDEPENDENT-SET

'''

'''
⭐⭐ Para un evento a realizar se requiere conformar una selección musical entre el conjunto A de “n” canciones. Podemos enumerar a los elementos de A como a1,a2,...,an. Por otra parte, contamos con un conjunto “B” de “m” personas. Cada una de ellas con un subsets de esas canciones que le gustan. Deseamos saber si podemos seleccionar un subconjunto de no más de “k” canciones, de tal forma que existe al menos 1 canción que le guste a cada uno. Se pide: Demostrar que el problema es NP-Completo. Sugerencia: Se puede utilizar Vertex Cover.
'''

# Cada vertice es una cancion, cada arista u-v es una persona la cual su subset de canciones que le gustan es {u, v}

