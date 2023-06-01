from Pila import Stack


def reverseIterativo(palabra):
    p=Stack(palabra)
    tamaño=len(p)
    for x in range(tamaño):
        print(p.pop())

def reverseRecursion(palabra):
    p=Stack(palabra)
    r=Stack()
    

    def recursion(p,r): 
        if len(p)<=0:
            return r
        else:
            r.push(p.pop())
            return recursion(p,r)
  


            
        
    return recursion(p,r)


# 3) En la forma recursiva e iterativa la desventaja es que en Orden N, pero
#   la ventaja es que tiene menos lineas de codigo y mas simple por usarlo con pila
