from dataclasses import dataclass

class Stack():
    __slots__=["_values","length"]
    def __init__(self,iterable=None):
        _values=any
        self.length=0
        self._values=[]
        if iterable is not None:
            for value in iterable:
                self.push(value)#Hay q hacer el metodo push

    def push(self,value):#Apilar, O(1)
        self._values.append(value)
        self.length+=1

    def top(self):#Tope, O(1)
        assert not self.empty(),'sin elementos'
        return self._values[-1]


    def empty(self):#Es_Vacia, O(1)
        return len(self._values)==0

    def __len__(self):#Tamaño,O(1)
        return self.length

    def pop(self):#Desapilar, O(1)
        assert not self.empty(),'sin elementos'
        self.length-=1
        return self._values.pop()

    def __eq__(self,other):
        return self._values==other._values

    def __repr__(self):
        return ('Stack([' + ', '.join(repr(x) for x in self._values) + '])' )

    def clear(self):
        self._values.clear()
        self.length=0

    def copy(self):
        n=Stack()
        n._values=self._values.copy()
        return n


    #Opcional:
    def print_inverso(self):
        while self.length != 0:
            print(self._values[-1])
            self.pop()

    def copyRecursivo(pila):
        r=Stack()
        def copR(pila,r):
            copia=Stack(pila._values)
            if len(copia)==0:
                return r
            else:
                top=copia.pop()
                sol=copR(copia,r)
                r.push(top)
                return r
        return copR(pila,r)
            


                


    

            





        
 
    

    

    
            
