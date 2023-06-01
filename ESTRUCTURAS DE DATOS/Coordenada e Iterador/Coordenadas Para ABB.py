class _Coordenada():
    __slots__=['_node']

    def __init__(self,coor_o_nodo):
        if isinstance(cood_o_nodo,Tree_Dict._Coordenada):
            self._node=coord_o_nodo
        else:
            self._node=coord_o_nodo

    @property
    def key(self):
        return self._node.clave
    
    @property
    def value(self):
        return self._node.Value

    @value.setter
    def value(self,value):
        self._node.Value=value

    def advance(self):
        node=self._node
        if node.right is not None:
            node=minimoNodo(node.right)
        else:
            while node.parent is not None:
                prev=node
                node=node.parent
                if node.right is not prev:
                    break
            self._node=node
            return self

    def retroceder(self):
        node=self._node
        if node.left is not None:
            node=maximoNodo(node.left)
        else:
            while node.parent is not None:
                prev=node
                node=node.parent
                if node.left is not prev:
                    break
        self._node=node
        return self
    def next(self):
        return Tree_Dict._Coordenada(self._node).advance()
    def previo(self):
        return Tree_Dict._Coordenada(self._node).retroceder()

    def __eq__(self,other):
        return self._node is other._node
