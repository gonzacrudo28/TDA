'''
⭐⭐La red ARPANET, antecesora de internet, se creó para seguir funcionando incluso ante fallas en parte de su red. El país “Atrasoñia” - que se mantuvo cerrado a los avances tecnológicos de las últimas décadas - ha decidido construir su propia red de redes. Han leído la documentación desclasificada de ARPANET y se han instruido en conectividad de redes. Proponen una red informática para unir sus principales organismos estatales. Nos convocan para que validemos su diseño. Debemos responder: ¿Cuántos cables de datos de la red se tienen que romper antes que la conectividad del grafo se rompa? (tener en cuenta que los cables de datos son bidireccionales) ¿Cuántos nodos se tienen que romper antes que el grafo restante deje de ser conexo? (Sugerencia: piense en transformar de alguna forma los nodos para resolverlo mediante lo creado en el punto a)
'''

# def ff_ek(grafo, s, t):
#     flujo = 0
#     inicializo el grafo residual gr
#     mientras haya un camino de aumento:
#         Encuentro el camino minimo con BFS
#         sea p el camino minimo
#         sea w el cuello de botella de p
#         flujo += w
#         actualizo el grafo residual con w
#     retornar flujo gr

#codigo del ejercicio:
#flujo, gr = ff_ek(arpanet, s, t)
#corte_minimo = flujo
#La minima cantidad de cables de datos de la red que se tienen que romper para que el grafo se rompa es corte_minimo
# # alcanzables = set()
# no_alcanzables = set()
# alcanzables.add(adyacentes(s))
# no_alcanzables = complemento alcanzables
# c_m = set()
# por cada nodo en alcanzables:
#     obtener adyacentes del nodo
#     por cada ady en adyacentes:
#         si adyacentes esta en no_alcanzables:
#             agrego arista (nodo, adyacente) a c_m

#Si quiero reducir el flujo un x %. Obtengo el flujo, el corte minimo y, de este ultimo, elimino ese porcentaje de aristas del corte

#Si quiero saber asignaciones, utilizo el grafo residual,para cada arista que una dos conjuntos (vehiculos, estacionamientos), si estan saturadas, la asignacion es esa.
