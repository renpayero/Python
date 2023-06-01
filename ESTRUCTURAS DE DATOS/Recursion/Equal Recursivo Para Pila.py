def __eq__(self,other): #Equal recursivo para Pila
    def are_equal(x,y):
        if x is None and y is None:
            return x is None and y is None
        if x._value!=y._value:
            return False

        return are_equal(x._next,y._next)
    return are_equal(self._top,other._top)
