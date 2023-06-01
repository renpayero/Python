import Pila
from Pila import *

def balanceado(cadenaDeSimbolos):
    p=Stack()
    indice=0
    if len(cadenaDeSimbolos)<=1:
        balance=False
    else:
        
        while indice<len(cadenaDeSimbolos):
            
            simbolos=cadenaDeSimbolos[indice]
            
            if simbolos in "({[":
                p.push(simbolos)
                indice+=1
                balance=True
            else:
                try:
                    tope=p.pop()
                except:
                    balanceado=False
                    break
                if not parejas(tope,simbolos):
                    balance=False
                else:
                    indice+=1
                    balance=True
    if balance:
        print("Esta balanceado")
    else:
        print("No Esta balanceeado")
        

def parejas(simboloApertura,simboloCierre):
    apertura="({["
    cierre=")}]"
    return apertura.index(simboloApertura)==cierre.index(simboloCierre)

                
    
