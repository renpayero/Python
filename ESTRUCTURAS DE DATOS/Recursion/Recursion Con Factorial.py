def factorial(n): #Con recursion
    if n<=1:
        return n
    else:
        return n*factorial(n-1)


def Factorial2(n): #Sin recursion
    fact = 1
    for x in range(1,n+1):
        fact=fact*x
    return fact
