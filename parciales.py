
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

    if producto.peso <= capacidad_restante and es_compatible(producto, seleccionados):
        seleccionados.append(producto)
        max_ganancia_contenedor(productos, indice+1, seleccionados, capacidad_restante - producto.pesp, ganancia_parcial + producto.ganancia)
        seleccionados.remove(producto)
    
    max_ganancia_contenedor(productos, indice+1, seleccionados, capacidad_restante, ganancia_parcial)




