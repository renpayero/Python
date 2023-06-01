from dataclasses import dataclass
class AVL():
    @dataclass
    class _Node:
        clave:None
        Value:None
        altura:int
        parent:None
        left=None
        right=None

    class _Root:
        left=None
        right=None
        parent=None

    __slots__=["_root","_len"]


    def __init__(self,iterable=None):
        self._root=AVL._Root()
        self._len=0

    def empty(self):
        return self._root._left is None
    def clear(self):
        self._root.left=None
        self._len=0
    def __len__(self):
        return self._len
    def begin(self):
        return self._root.left
    def end(self):
        return self._root
    def insert(self,key,value):
        def do_insert(node,parent):
            if node is None:
                node=AVL._Node(key,value,1,parent)
                self._len+=1
            elif key==node.clave:
                node.value=value
            else:
                if key<node.clave:
                    node.left=do_insert(node.left,node)
                else:
                    node.right=do_insert(node.right,node)
                node=self.balance(node)#Como se trata de recursion, esta operacion la realiza con todos los nodos por los que paso antes de crear el nodo nuevo
            return node

        self._root.left=do_insert(self._root.left,self._root)

    def balance(self,nodo):
        def factor_Equilibrio(node):#Verifica en cualquier nodo su factor de equilibrio
            factor=0
            if node.left is not None: #Si tiene hijo izquierdo, suma su altura a factor
                factor+=node.left.altura
            if node.right is not None: #Si tiene hijo derecho, resta su altura a factor
                factor-=node.right.altura
            return factor


        factor=factor_Equilibrio(nodo)
        if factor==2: #Si el factor de equilibrio me dio 2 o -2 esta desequilibrado, por lo que tiene q balancearse
            if factor_Equilibrio(nodo.left)==-1:
                nodo.left=rotacion_izquierda(nodo.left)
            nodo=rotacion_derecha(nodo)
        elif factor== -2:
            if factor_Equilibrio(nodo.right)==1:
                nodo.right=rotacion_derecha(nodo.right)
            nodo=rotacion_izquierda(nodo)





        def rotar_derecha(nodo):
            hijo_Izquierdo=nodo.left
            nodo.left=hijo_Izquierdo.right #Si no tiene hijo derecho es None, sino es el hijo derecho, Si tiene hijo, lo acomodo para que el nodo enganche al hijo
            if nodo.left is not None: #Esto depende de si tenia hijos o no la operacion anterior
                hijo_Izquierdo.parent=nodo.parent
            hijo_Izquierdo.right=nodo #Ahora el hijo izquierdo va a tener como hijo al nodo padre
            hijo_Izquierdo.parent=nodo.parent #El padre del hizo izquierdo va a ser el padre del nodo desbalanceado
            nodo.parent=hijo_Izquierdo #Ahora el padre del nodo desbalanceado es el hijo izquierdo,
            nodo=hijo_Izquierdo #Por lo que ahora el nuevo nuevo balanceado sera su hijo izquierdo
            #FALTA ACTUALIZAR LAS ALTURAS
            self.actualizar_altura(nodo.right)
            self.actualizar_altura(nodo)
            return nodo



        def rotar_izquierda(nodo):
            #Se le puede pasar el hijo izquierdo del nodo, o el nodo desbalanceado, segun la situacion
            hijo_Derecho=nodo.right
            nodo.right=hijo_Derecho.left #Si no tiene hijo izquierdo es None, sino es el el hijo izquierdo, Si tiene hijo, lo acomodo para que el nodo enganche al hijo
            if nodo.right is not None: #Si se le pasa por parametro el hijo izquierdo del nodo desbalanceado, esto va a ser None por lo cual se lo saltea
                nodo.right.parent=nodo
            hijo_Derecho.left=nodo
            hijo_Derecho.parent=nodo.parent #Se le asigna al hijo derecho el padre del nodo que se le paso por parametro
            nodo.parent=hijo_Derecho
            nodo=hijo_Derecho
            #FALTA ACTUALIZAR LAS ALTURAS
            self.actualizar_altura(nodo.left)
            self.actualizar_altura(nodo)
            return nodo


    def actualizar_altura(nodo):
        altura_izquierda=0
        if nodo.left is not None:
            altura_izquierda=nodo.left.altura
        altura_derecha=0
        if nodo.right is not None:
            altura_derecha=nodo.right.altura
        nodo.altura=1+ max(altura_izquierda,altura_derecha)
                
            
            
            
            





































        
    
