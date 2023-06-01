from dataclasses import dataclass
from typing import Any
class ListaSimple():
    @dataclass
    class Nodo:
        dato: Any
        sig: '_Nodo'
    __slots__ = ['_pri', '_tamaño']


    def __init__(self,iterable=None):
        self._pri=None#Esta cambiado, actualizado, antes era self._pri=ListaSimple.Nodo(None,None)
        self._tamaño=0
        if iterable is not None:
            for value in iterable:
                self.agregar_al_frente(value)

    def agregar_al_frente(self,value):
        aux=ListaSimple.Nodo(value,self._pri)
        aux.sig=self._pri
        self._pri=aux
        self._tamaño+=1

    def __repr__(self):
        aux=self._pri
        lista=[]
        while aux is not None:
            lista.append(aux.dato)
            aux=aux.sig
        return ("["+"][".join(repr(x) for x in lista)+"]")


    def cortar(self,indice): #ESTA ES LA ORIGINAL DEL PARCIAL
        nueva=ListaSimple()
        first=self._pri
        if indice<=self._tamaño:
            for e in range(0,self._tamaño-1):
                if e==indice:#ESTE IF ES NUEVO, NO ESTABA EN LA ENTREGA DEL PARCIAL
                    aux=first
                first=first.sig
                if e<indice:
                    continue
                else:
                    nueva.agregar_al_frente(first.dato)
                    #EN EL PARCIAL FALTABA EL ERASE
            aux.sig=None#Esto no estaba en el parcial, porque no sabia como borrar.
            return nueva
        return "Indice invalido"
    #Cortar recursivo
    def cortarR(self,indice): #Lo hice ahora, despues del parciall, por lo tanto es nuevo
        nueva=ListaSimple() #Creo una lista y guardo el primer elemento de la lista original
        first=self._pri
        def rec(nodo):
            for e in range(0,self._tamaño-1): #itero hasta la longitud total de la lista original, pregunto si esta vaciao si el nodo es none y si se cumple, corta
                if nodo==None:
                    break
                elif e<=indice: #si es menor al indice, retorna la funcion para que lo haga con el proximo elemento
                    return rec(nodo.sig)
                else:# si es indice es igual o es mayor a E
                    if e==indice:#Si es igual, lo guardo en un auxiliar para luego borrar
                        aux=nodo
                    nueva.agregar_al_frente(nodo)
                    return rec(nodo.sig)#sigo con el proximo elemento
            aux.sig=None  #Borro un elemento por lo tanto los que le siguen tambien se borran         
            return nueva
                
        return rec(first)
            
            
            
        return "Indice invalido"
    #2da ALTERNATIVA DEL CORTAR:
    def cortar2(self,indice):
        nueva=ListaSimple()
        first=self._pri
        if indice<=self.tamaño:
            for e in range(0,indice):
                actual=actual.sig
            aux=actual
            while actual is not None:
                nueva.agregar_al_frente(actual.dato)
                actual=None

                actual=actual.sig
                
            
            return nueva
        return "indice invalido"


    def __eq__(self,other):
        if self._tamaño==other._tamaño:
            first=self._pri
            other_first=other._pri
            while first is not None:
                if first==other_first:
                    first=first.sig
                    other_first=other_first.sig
                else:
                    return False
            return True
        return False
        #Si quiero hacerlo recursivo, tengo q guardar el primero de cada lista
        #en una variable , ir comparando las dos y llamar de vuelta a la funcion con el next de cada uno
    
        
    

            
