class Grafos():
    __slots__=["_vertices","_aristas"]

    def __init__(self,iterable=None):
        self._vertices=[]
        self._aristas=[]


    def empty(self):
        return len(self._vertices)==0
    
    def clear(self):
        self._vertices=[]
        self._aristas=[]

    def __len__(self):
        return len(self._vertices)

    def vertices(self):
        return list(range(len(self._vertices)))

    def get_vertice(self,indice):
        return self._vertices[indice]

    def set_vertices(self,indice,valor):
        self._vertices[indice]=valor

    def erase_item(self,key):
        if isinstance(key,tuple):
            self.erase_arista(key[0],key[1])
        else:
            self.erase_vertice(key)

    def get_edge(self,from_,to):
        return self._aristas[from_][to]

    def erase_vertice(self,indice):
        if 0<=indice<len(self._vertices):
            del self._vertices[indice]
            del self._aristas[indice]
            for edge in self._aristas:
                del edge[indie]

    def erase_arista(self,_from,to):
        if self._aristas[_from][to] is not None or self._aristas[_from][to]==True:
            self._aristas[_from][to]=None
            return True
        return False
    
    def add_vertice(self,value):
        indice=len(self._vertices)
        self._vertices.append(value)
        for edges in self._aristas:
            edges.append(None)
        self._aristas.append([None]*(indice+1))
        return indice #Retorna donde guardo el elemento

    def add_arista(self,_from,to,peso=None):
        self._aristas[_from][to]=peso

    def __eq__(self,other):
        return self._vertices==other._vertices and self._aristas==other._aristas
    
    def es_adyacente(self,_from,to):
        return self._aristas[_from][to] is not None

    def adyacentes(self,_from):
        resultados=[]
        for i in range(len(self._vertices)):
            if self._aristas[_from][i] is not None:#Se fija si el camino desde donde le indique hasta cada uno de los vertices es != de None
                resultados.append(i)
        return resultados

    def copy(self):
        result=Grafos()
        result._vertices=self._vertices.copy()
        result._aristas=[]
        for aristas in self._aristas:
            result._aristas.append(aristas.copy())
        return result

    def __repr__(self):
        result='( '
        for v in self.vertices():
            for w in self.adyacentes(v):
                result+='{0}-({2})->{1}, '.format(v, w,self.get_edge(v,w))
        return result + ') :Grafos '
    
    
                             
            















