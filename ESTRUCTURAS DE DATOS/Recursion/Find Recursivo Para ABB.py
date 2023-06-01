def find(self,key):
    def do_find(node):
        if node is None:
            return False #o return self.end()
        elif key<node.clave:
            return do_find(nodo.left)
        elif key > nodo.clave:
            return do_find(nodo.right)
        else:#key==nodo.clave
            return nodo.Value #o return Tree_Dict._Coordenada(nodo)

    return do_find(self._root.left)
