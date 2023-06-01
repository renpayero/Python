from dataclasses import dataclass
class ListaDoble():

    @dataclass
    class _node:
        _value:any
        _prev:'_node'=None
        _next:'_node'=None

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

    class _iterador():
        __slots__=["node","_end"]

        def __init__(self,head,end):
            self.node=head
            self.end=end

        def __iter__(self):
            return self
        def __next__(self):
            if self.node is self.end:
                raise StopIteration
            value=self.node._value
            self.node=self.node._next
            return value


        
    @dataclass
    class _Head:
        _prev:'_node'=None
        _next:'_node'=None



    __slots__=["_head","_length"]

    def __init__(self,iterable=None):
        self._head=ListaDoble._Head()
        self._length=0
        self._head._prev=self._head._next=self._head
        if iterable is not None:
            for value in iterable:
                self.append_back(value)

    
    def __len__(self):
        return self._length

    @property
    def front(self):
        assert not self.is_empty(),'sin elementos'
        return self._head._next._value

    @property
    def back(self):
        assert not self.is_empty(),'sin elementos'
        return self._head._prev._value

    def append_front(self,value):
        self.insert(self.begin(),value)

    def append_back(self,value):
        self.insert(self.end(),value)

    def copy(self):
        newList=ListaDoble()
        actual=newList._head
        for value in self:
            nodo=ListDoble._node(value)
            nodo._prev=actual
            actual._next=nodo
            actual=nodo
        newList._head._prev=actual
        actual._next=newList._head
        return newList

    def clear(self):
        self._length=0
        self._head._prev=self._head._next=self._head

    def begin(self):
        return ListaDoble._Coordenada(self._head._next)

    def end(self):
        return ListaDoble._Coordenada(self._head)

    def __eq__(self,other): #Con Coordenadas
        p=self.begin()
        v=other.begin()
        while p !=self.end()and v != other.end():
            if p._value != v._value:
                return False
            p.advance()
            v.advance()
        return p==self.end() and v==other.end()

    def __repr__(self):
        return 'Lista Doble ([' + ', '.join(repr(v)for v in self) + '])'

    def insert(self,coord,value): #Con coordenadas
        actual=coord._nodo
        nodo=ListaDoble._node(value)
        nodo._prev=actual._prev
        nodo._next=actual
        nodo._prev._next=nodo
        nodo._next._prev=nodo
        return ListaDoble._Coordenada(actual)

    def erase(self,coord):#Con Coordenadas
        actual=coord._nodo
        actual._prev._next=actual._next
        actual._next._prev=actual._prev
        return coord.next()

    def __iter__(self):#Con Iteradores
        return ListaDoble._iterador(self._head._next,self._head)
    

    

    

