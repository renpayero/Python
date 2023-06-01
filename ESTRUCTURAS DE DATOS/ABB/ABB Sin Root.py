from dataclasses import dataclass
from typing import Any
class Tree():
    
    @dataclass
    class _Node():
        clave: None
        Value: None
        parent:None
        left=None
        right=None

    __slots__=["_root","_Len"]

    def __init__(self,iterable=None):
        self._root=None
        self._Len=0

    def empty(self):
        return self._root is None
    
    def __len__(self):
        return self._Len

    def insert(self,key,value):
        if self.empty()==True:
            self._root=Tree._Node(clave=key,Value=value,parent=None)
            self._Len+=1
        else:
            def do(nodo,parent):
                if nodo is None:
                    nodo=Tree._Node(clave=key,Value=value,parent=parent)
                    self._Len+=1
                elif key<nodo.clave:
                    print("llega aca el mas chico")
                    nodo.left=do(nodo.left,nodo)
                elif key>nodo.clave:
                    print("llega aca el mas grande")
                    nodo.right=do(nodo.right,nodo)
                else:#Si son iguales:
                    nodo.Value=value
                return nodo
            return do(self._root,None)
    def maximo(self):
        aux=self._root
        while aux.right is not None:
            aux=aux.right
        return aux
    
    def minimo(self):
        aux=self._root
        while aux.left is not None:
            aux=aux.left
        return aux
    
    def find(self,key):
        aux=self._root
        while aux is not None:
            if key<aux.clave:
                aux=aux.left
                print("paso al mas chico")
            elif key>aux.clave:
                aux=aux.right
                print("paso al mas grande")
            else:
                return aux
        return False

        return False
    def clear(self):
        self._root=None
        self._Len=0

    def erase(self,key):
        def reemplazar(nodo,hijo):
            hijo.parent=nodo.parent #Si no tiene hijos va directo al if, hijo=None
            if nodo.parent.right==nodo:
                nodo.parent.right=hijo
            else:
                nodo.parent.left=hijo
            hijo.parent=nodo.parent


        if self._root is None:
            return "Esta vacio"
        else:
            nodo=self.find(key)
            if nodo==False:
                return "Clave invalida"
            else:
                if nodo.left is None and nodo.right is None: #Si el nodo a borrar no tiene hijos:
                    reemplazar(nodo,None)
                elif nodo.left is not None and nodo.right is None:#Si el nodo a borrar solo tiene un hijo izquierdo:
                    reemplazar(nodo,nodo.left) 
                elif nodo.left is None and nodo.right is not None:
                    reemplazar(nodo,nodo.right)
                else:
                    maximo=extraer_Maximo(nodo.left)
                    if maximo.left is not None:
                        reemplazar(maximo,maximo.left)

                    reemplazar(nodo,maximo)
                    if nodo.left != maximo:
                        maximo.left=nodo.left
                        maximo.left.parent=maximo
                    maximo.right=nodo.right
                    nodo.right.parent=maximo

        def extraer_Maximo(nodo):
            maximo=nodo
            prev=None
            while maximo.right is not None:
               maximo=maximo.right
            return maximo

    def begin(self):
        return self.minimo()
    def end(self):
        return self.maximo()


    def __str__(self):
        def calculate_placement(node, level):
            if node is None:
                return 0
                
            nonlocal count
            m1 = calculate_placement(node.left, level + 1)
            placements.append((level, count, node))
            count += 1
            m3 = calculate_placement(node.right, level + 1)
            return max(m1, len(str(node.clave)), m3)

        count = 0
        placements = []
        key_len = calculate_placement(self._root, 0) + 2

        lines = []
        prev_level = -1
        for level, pos, node in placements:
            i = 2 * level
            while len(lines) <= i:
                lines.append('')

            skip = ' ' * (pos * key_len - len(lines[i]))
            lines[i] += skip + '[{:^{}}]'.format(node.clave, key_len - 2)

            if prev_level != -1:
                if prev_level < level:
                    i = 2 * prev_level + 1
                    skip = ' ' * (pos * key_len - len(lines[i]))
                    c = '\\'
                else:
                    i = 2 * level + 1
                    skip = ' ' * (pos * key_len - len(lines[i]) - 1)
                    c = '/'

                lines[i] += skip + '{:>{}}'.format(c,  key_len // 2)

            prev_level = level

        return '\n'.join(lines)

