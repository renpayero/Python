from Pila import *
from cola import *
import Pila
import cola
A=Stack()
P=Head()
x=input("ponga algo ")
for i in x:
    A.push(i)
    P.push(i)

for f in range(len(x)):
    if A.top()==P.first():
        rta=True
        P.pop()
        A.pop()
    else:
        rta=False
        break
if rta==True:
    print("Es Palindromo")
else:
    print("No Es Palindromo")
     


        
        

    
    
        
        

        





