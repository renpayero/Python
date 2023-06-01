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



            def __iter__(self):#Con Iteradores ---- Este va en el contenedor
        return ListaDoble._iterador(self._head._next,self._head)
               #Cambiar el nombre del contenedor
