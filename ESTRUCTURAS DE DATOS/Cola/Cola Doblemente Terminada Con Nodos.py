from dataclasses import dataclass

class ColaD():
    @dataclass
    class _node:#Nodo
        _value:any
        prev:"_Node"=None
        sig:"_Node"=None
    __slots__=["_end","length","_value","_start"]

    def __init__(self,iterable=None):#Generador
        self._end=self._start=ColaD._node(None,None,None)
        self.length=0
        if iterable is not None:
            for values in iterable:
                self.push_end(values)

    def push_end(self,values):#Agregar Al Final, O(1)
        aux=ColaD._node(values,None,None)
        self._end.sig=aux
        aux.prev=self._end
        self._end=aux
        self.length+=1
        if self._start._value==None:
            self._start=aux

    def push_start(self,values):#Agregar Al Principio, O(1)
        aux=ColaD._node(values,None,None)
        self._start.prev=aux
        aux.sig=self._start
        self._start=aux
        self.length+=1
        if self._end._value==None:
            self._end=aux

    def __len__(self):#Tamaño
        return self.length

    def empty(self):#Es_Vacia
        return self.length==0

    def first(self):#Primer Elemento
        return self._start._value

    def end(self):#Ultimo Elemento
        return self._end._value

    def popS(self):#Sacar Por El Principio
        aux=self._start
        self._start=aux.sig
        self.length-=1
        return aux._value

    def popE(self):#Sacar Por El Final
        aux=self._end
        self._end=aux.prev
        self.length-=1
        return aux._value

    def clear(self):#Vaciar
        self._end=self._start=None
        self.length=0

    
        
        
    
        
