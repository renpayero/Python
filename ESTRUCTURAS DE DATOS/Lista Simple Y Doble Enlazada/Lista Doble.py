from dataclasses import dataclass
class ListaDoble():

    @dataclass
    class _node:
        _value:any
        _prev:'_node'=None
        _next:'_node'=None

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

    def is_empty(self):
        return self._head._next is self._head

    @property
    def front(self):
        assert not self.is_empty(),'sin elementos'
        return self._head._next._value

    @property
    def back(self):
        assert not self.is_empty(),'sin elementos'
        return self._head._prev._value

    def append_back(self,value):
        new=ListaDoble._node(value)
        self._head._prev._next=new
        new._prev=self._head._prev
        self._head._prev=new
        self._length+=1
        if self._head._next._value == None:
            self._head._next=new

    def append_front(self,value):
        new=ListaDoble._node(value)
        self._head._next._prev=new
        new._next=self._head._next
        self._head._next=new
        self._length+=1
        if self._head._prev==None:
            self._head._prev=new

    def clear(self):
        self._length=0
        self._head._prev=self._head._next=self._head


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

    def __eq__(self,other):
        p=self._head._next
        v=other._head._next
        while p !=self._head._prev and v != other._head._prev:
            if p._value != v._value:
                return False
            p=p._next
            v=v._next
        return p==self._head._prev and v==other._head._prev



    


                
