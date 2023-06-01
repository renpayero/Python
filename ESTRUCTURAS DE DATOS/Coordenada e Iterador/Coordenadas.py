

class _Coordenada():

    __slots__=["_nodo"]
    def __init__(self,coordenada_o_nodo):
        if isinstance(coordenada_o_nodo,ListaDoble._Coordenada):
            self._nodo=coordenada_o_nodo._node
        else:
            self._node=coordenada_o_nodo


    @property
    def value(self):
        return self._nodo.value
    @value.setter
    def value(self,value):
        self._nodo._value=value

    def advance(self):
        self._nodo=self._nodo._next
        return self

    def next(self):
        return ListaDoble._Coordenada(self._nodo).advance()

    def retroceder(self):
        self._nodo=self._nodo._prev
        return self

    def previo(self):
        return ListaDoble._Coordenada(self._nodo).retroceder()

    def __eq__(self,other):
        return self._nodo is other._nodo

    def find(primero,ultimo,value):
        while primero != ultimo:
            if primero._value==value:
                return primero
            primero=primero.next()
        return ultimo

    
