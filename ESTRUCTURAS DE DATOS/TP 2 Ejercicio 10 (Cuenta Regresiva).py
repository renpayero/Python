class cuentaRegresiva():
    class iterator():
        __slots__=["_node","_end"]
        def __init__(self,head,end):
            self._node=head
            self._end=end

        def __iter__(self):
            return self

        def __next__(self):
            if self._node==self._end:
                raise StopIteration
            else:
                self._node-=1
                return self._node

    __slots__=["_inicio","_ultimo"]

    def __init__(self,inicio=None,ultimo=None):
        if inicio !=None:
            self._inicio=inicio
        else:
            self._inicio=None
        self._ultimo=ultimo
        


    def __iter__(self): #PUNTO 11
        return cuentaRegresiva.iterator(self._inicio,self._ultimo)

    
        
