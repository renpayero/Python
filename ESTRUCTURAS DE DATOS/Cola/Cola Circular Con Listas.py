class Cola():
    __slots__=["_values","_front","_length"]
    def __init__(self,iterable=None):
        self._front=0
        if iterable is not None:
            self._values=list(iterable)
        else:
            self._values=[]
        self._length=len(self._values)

    def __len__(self):
        return self._length
    def empty(self):
        return self._length==0
    def __eq__(self,other):
        return self._values==other._values
    def first(self):
        return self._values[self._front]
    def top(self):
        return self._values[-1]
    def push(self,value):
        if self._length>10:
            self._values[(self._front%11)]=value
            self._front+=1
            
        else:
            self._values.append(value)
            self._length+=1

    def __repr__(self):
        return("<-["+"][".join(repr(x)for x in self._values)+"]<-")

    def pop(self):
        self._length-=1
        self._values.pop(0)
        
            
        
    

    

    
