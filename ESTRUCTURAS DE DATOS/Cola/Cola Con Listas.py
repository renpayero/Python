from dataclasses import dataclass

class Head():

    __slots__=["_values","length"]
    def __init__(self,iterator=None):#Generador
        _values=any
        self.length=0
        self._values=[]
        if iterator is not None:
            for values in iterator:
                self.push(values)
               

    def __len__(self):#Tamaño, O(1)
        return self.length

    def empty(self):#Es_Vacia, O(1)
        return len(self._values)==0

    def top(self):#Ver_Tope, O(1)
        assert not self.empty(),'sin elementos'
        return self._values[-1]

    def first(self):#Ver_Primero, O(1)
        assert not self.empty(),'sin elementos'
        return self._values[0]
    

    def pop(self):#Desencolar, O(1)
        self.length-=1
        self._values.pop(0)
    
    def push(self,values):#Encolar, O(1)
        self._values.append(values)
        self.length+=1

    def clear(self):#Vaciar, O(1)
        self._values=[]

    def __eq__(self,other):
        return self._values==other._values



            
        
            
        
    

    
    
