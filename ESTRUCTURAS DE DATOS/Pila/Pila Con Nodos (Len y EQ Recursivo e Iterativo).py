from dataclasses import dataclass

class Stack():
    @dataclass
    class _node():
        _value=any
        _next:"_node"=None

    __slots__=["_top","_inicio","_length"]

    def __init__(self,iterable=None):
        self._length=0
        self._top=None
        if iterable is not None:
            for values in iterable:
                self.push(values)

    def apilar(self,values):
        if self._top==None:
            nuevo=Stack._node()
            nuevo._value=values
            nuevo._next=None
            self._inicio=nuevo
            self._top=nuevo
            self._length+=1
        else:
            nuevo2=Stack._node()
            nuevo2._value=values
            nuevo2._next=None
            self._top._next=nuevo2
            self._top=nuevo2
            self._length+=1

    def __len__(self):
        return self._length

    def clear(self):
        self._top=None
        self._length=0

    def is_empty(self):
        return self._top is None

    def desapilar(self):
        assert not self.is_empty(),'sin elementos'
        value= self._top._value
        self._top=self._top._next
        self._length-=1
        return value


    def recorrer(self):
        current=self._inicio
        while(current!=None):
            print(current._value)
            current=current._next

    def top(self):
        assert not self.is_empty(),'Sin elementos'
        return self._top._value

    def copy(self):
        n=Stack()
        if not self.is_empty():
            node=self._top
            new_node=Stack._node(node._value,None)
            n._top=new_node
            while node._next is not None:
                node=node._next
                new_node._next=Stack._node(node._value,None)
                new_node=new_node._next
        return n

    def lenRecursivo(self):
        def lenR(nodo):
            if nodo._next==None:
                return 0
            else:
                return 1+ lenR(nodo._next)
        return lenR(self._inicio)
    def lenIterativo(sef):
        n=0
        node=self._top
        while node is not None:
            node=node._next
            n+=1
        return n


    def __eq__(self,other):
        x=self._top
        y=other._top
        while x is not None and y is not None:
            if x._value != y._value:
                return False
            x=x._next
            y=y._next
        return x is None and y is None

    def equal_recursivo(self,other):
        def do_equal(x,y):
            if x is None and y is None:
                return x is None and y is None
            elif x is None or y is None:
                return False

            elif x._value !=y._value:
                return False
            elif x._value==y._value:
                return do_equal(x._next,y._next)
            else:
                return False
        
        return do_equal(self._top,other._top)



    def __repr__(self):
        values=[]
        node=self._top
        while node is not None:
            values.insert(0,node._value)
            node=node._next

        return 'Stack([' + ', '.join(repr(x) for x in values) + '] )'
                    
    
            
        
        
    
            
            
        
        
