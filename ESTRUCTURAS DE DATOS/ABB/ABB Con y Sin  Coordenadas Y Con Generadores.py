from dataclasses import dataclass

class Tree_Dict():
    @dataclass
    class _Node: #Definimos los Nodos
        clave:None
        Value:None
        parent:None
        left=None
        right=None

    @dataclass
    class _Root: #Definimos la raiz escondida
        left=None
        right=None #Este basicamente no se usa
        parent=None #Este tampoco
    __slots__=["_root","_len"]

    def __init__(self,iterable=None):#Solo lo creamos sin elementos
        self._root=Tree_Dict._Root()
        self._len=0

    def empty(self): #O(1)
        return self._root.left is None

    def __len__(self): #O(1)
        return self._len

    def clear(self):
        self._root.left=None
        self._len=0

    def insert(self,key,value=None):#Recursivo
        def do_insert(nodo,parents):
            if nodo is None:
                nodo=Tree_Dict._Node(key,value,parent=parents)
                self._len+=1
                return nodo
            elif key<nodo.clave:
                nodo.left=do_insert(nodo.left,nodo)
            elif key>nodo.clave:
                nodo.right=do_insert(nodo.right,nodo)
            else: #Si son iguales:
                nodo.Value=value
            return nodo
        self._root.left=do_insert(self._root.left,self._root)


    def find(self,key): #O(N)
        aux=self._root.left
        while aux is not None:
            if key<aux.clave:
                aux=aux.left#Si la clave es menor que AUX, va para la izquierda
            elif key>aux.clave:
                aux=aux.right #Si la calve es mayor que AUX, va para la derecha
            else:#key==aux.clave
                return aux #o return Tree_Dict._Coordenada(aux)
        return False #o return self.end()


    def minimo(self): #Retorna el minimo nodo en el arbol
        aux=self._root.left
        while aux.left is not None:
            aux=aux.left
        return aux
        #Todo esto se puede reemplazar por:
        #return Tree_Dict._Coordenada(minimoNodo(self._root))

    def minimoNodo(node): #Tambien retorna el minimo nodo en el arbol, pero hay que pasarle un nodo por parametro
        if node is not None:
            while node.left is not None:
                node=node.left
        return node
    
    def maximoNodo(node): #Retorna el maximo nodo en el arbol a partir de un nodo especifico que se le pasa por parametro
        if node is not None:
            while node.right is not None:
                node=node.right
        return node
    
    def maximo(self): #Retorna el maximo nodo en el arol
        aux=self._root.left
        while aux.right is not None:
            aux=aux.right
        return aux
        #Todo esto se puede remplazar por:
        #return Tree_Dict._Coordenada(maximoNodo(self._root.left))


    def erase(self,key):
        def reemplazar(node,hijo): #Esta funcion le asigna el padre del nodo al hijo para que se pueda borrar el nodo
            if hijo is not None: #Si no tiene hijos, esta se omite
                hijo.parent = node.parent #El padre del hijo, va a ser el padre del nodo a borrar
            if node.parent.right==node: #Si el padre, tiene como hijo derecho al nodo a borrar:
                node.parent.right = hijo
            else: #Si el padre, tiene como hijo izquierdo al nodo a borrar:
                node.parent.left = hijo

            
        def extraer_Maximo(nodo): #Misma funcion que "maximoNodo". Tienen la misma funcionalidad.
            maximo=nodo
            while maximo.right is not None: #Si no tiene hijo derecho, el nodo que se le pasa como parametro, sera el maximo
                maximo=maximo.right
            return maximo
        
        #!!!!!!ACA ARRANCA EL ERASE!!!!!
        
        if self._root.left is None: #Si el arbol esta vacio, no retorna nada
            return "esta vacio"

        else:
            nodo=self.find(key) #Busca la clave que se quiere borrar
            if nodo==False:
                return "CLAVE INVALIDA" #No Se Encontro La Clave Especificada
            else:
                if nodo.left is None and nodo.right is None: #Si el nodo a borrar no tiene hijos
                    reemplazar(nodo,None)
                    
                elif nodo.left is not None and nodo.right is None: #Si solo tiene hijo izquierdo:
                    reemplazar(nodo,nodo.left)
                    
                elif nodo.left is None and nodo.right is not None: #Si solo tiene hijo derecho
                    reemplazar(nodo,nodo.right)
                    
                else: #Si tiene hijo izquierdo e hijo derecho:
                    maximo=extraer_Maximo(nodo.left) #Extraigo el maximo del subarbol izquierdo (hijo izquierdo)
                    
                    if maximo.left is not None: #Si el maximo tiene hijo izquierdos
                        reemplazar(maximo,maximo.left) #Se reemplaza el maximo ya que este sera el reemplazante del nodo a borrar
                        
                    reemplazar(nodo,maximo) #Esto se ejecuta siempre
                    
                    if nodo.left!=maximo: #Si el maximo no es el hijo izquierdo del nodo a borrar:
                        maximo.left=nodo.left #ACA SE HACE EL ENGANCHE DEL HIJO IZQUIERDO DEL NODO A BORRAR CON EL NODO REEMPLAZANTE
                        maximo.left.parent=maximo
                        
                    maximo.right=nodo.right #Se hace el otro enganche del hijo derecho del nodo a borrar
                    nodo.right.parent=maximo


    def copy(self): #Recursivo
        def do_copy(nodo,parent):
            if nodo is None:
                new=nodo
            else:
                new=Tree_Dict._Node(nodo.clave,nodo.Value,parent)
                new.left=do_copy(nodo.left,new)
                new.right=do_copy(nodo.right,new)
            return new

        nuevoArbol=Tree_Dict()
        nuevoArbol._root.left=do_copy(self._root.left,nuevoArbol._root)
        nuevoArbol._len=self._len
        return nuevoArbol

    def begin(self):#Esto Es Con Coordenadas
        return Tree_Dict._Coordenada(minimoNodo(self._root))

    def end(self):#Esto Es Con Coordenadas
        return Tree_Dict._Coordenada(self._root)

    def __eq__(self,other):#Con Coordenadas
        p=self.begin()
        q=other.begin()
        whiñe p!=self.end() and q!= other.end():
            if p.clave!=q.clave or p.Value!=q.Value:
                return False
            p.advance()
            q.advance()
        return p==self.end() and q==other.end()

    def items(self):#Con Coordenadas y generadores
        pos= self.begin()
        end=self.end()
        while pos != end:
            yield pos.clave,pos.Value
            pos.advance()
    def values(self):#Con Coordenadas y generadores
        for _,value in self.items():
            yield value



    def __str__(self):
        #Es para imprimir el árbol de una manera bonita :-)
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
        key_len = calculate_placement(self._root.left, 0) + 2

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
                
        
