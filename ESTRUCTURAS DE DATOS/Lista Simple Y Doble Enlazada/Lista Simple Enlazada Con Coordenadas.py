from dataclasses import dataclass
from typing import Any

class listaSimple():
        class _coordinate():
                __slots__=["_coord"]
                def __init__(self,coord_or_node):
                        if isinstance(coord_or_node,listaSimple._coordinate):
                                self._coord=coord_or_node._node
                        else:
                                self._coord=coord_or_node
                @property
                def value(self):
                        return self._coord.value
                @value.setter
                def value(self,value):
                        self._coord.value=value #El .value es la funcion de arriba
                def next(self):
                        return _coordinate(self._coord).advance()
                def advance(self):
                        self._coord=self._node.next
                        return self
                def __eq__(self,other):
                        return self._coord==other._coord

                
        
        @dataclass
        class _Head():
                _next:"_node"=None
        @dataclass
        class _node():
                value:any
                _next:"_node"=None
        __slots__=["_head"]

        def __init__(self,iterable=None):
                self._head=listaSimple._Head(None)
                if iterable is not None:
                        actual=self._head
                        for value in iterable:
                                node=listaSimple._node(value,None)
                                actual._next=node
                                actual=node
        def begin(self):
                return listaSimple._coordinate(self._head._next)
        def end(self):
                return listaSimple._coordinate(self._head)

        def insert(self,coord,value):
                cabeza=self._head
                if self._head._next is None:
                        nodo=listaSimple._node(value,None)
                        cabeza._next=nodo
                        cabeza=nodo
                        coord._coord=cabeza
                        coord._coord._next=cabeza._next
                else:
                        nuevo=listaSimple._node(value)
                        nuevo._next=coord._coord._next
                        #Se usa el _next de la clase nodo y head
                        coord._coord._next=nuevo

        def find(self,value):
                if self._head._next==None:
                        return False
                else:
                        aux=self._head._next
                        while aux !=None:
                                if aux.value==value:
                                        coordenada=listaSimple._coordinate(aux)
                                        return coordenada
                                else:
                                        aux=aux._next
                        return False
        def remove(self,coord):
                coord._coord._next=coord._coord._next._next

        def recorrer(self):
                current=self._head
                while(current._next!=None):
                        print(current._next.value)
                        current=current._next
                        

                        


        
                        
                        
                        
                


                        
                        
                        

                
                        
                
                

    
            
    
