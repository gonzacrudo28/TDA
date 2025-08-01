import random

class Graph:
    def __init__(self, directed = False):
        self.dict_graph = {}
        self.directed = directed
        self.weight = {}

    def add_vertex(self, v):
        if v in self.dict_graph:
            return
        self.dict_graph[v] = []


    def delete_vertex(self, v):
        if not v in self.dict_graph:
            return
        for w in self.dict_graph[v]:
            self.delete_edge(v, w)
            if self.directed:
                self.delete_edge(w, v)
        del self.dict_graph[v]

    def add_edge(self, v, w, peso = 1):
        if not v in self.dict_graph or not w in self.dict_graph:
            return
        self.dict_graph[v].append(w)
        self.weight[(v, w)] = peso
        if not self.directed:
            self.weight[(w, v)] = peso
            self.dict_graph[w].append(v)
        
    def delete_edge(self, v, w):
        if not v in self.dict_graph or not w in self.dict_graph:
            return
        if w in self.dict_graph[v]:
            self.dict_graph[v].remove(w)
            del self.weight[(v, w)]
            if not self.directed:
                self.dict_graph[w].remove(v)
                del self.weight[(w, v)]

    def are_united(self, v, w):
        if v in self.dict_graph and w in self.dict_graph:
            if w in self.dict_graph[v]:
                return True
        return False
    
    def edge_weight(self, v, w):
        if (v, w) in self.weight:
            return self.weight[(v, w)]
        return 0
    
    def get_vertex(self):  
        return list(self.dict_graph.keys())
    
    def random_vertex(self):
        return random.choice(self.get_vertex())
    
    def adjacent(self, v):
        return self.dict_graph[v] if v in self.dict_graph else []
    
    def change_weight(self, v, u, valor):
        if (v, u) in self.weight:
            self.weight[(v, u)] = valor
    
    def vertex_belongs(self,v):
        return v in self.dict_graph