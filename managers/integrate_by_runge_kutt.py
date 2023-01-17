import numpy

def runge_kutt_4 (t, x0, n, function):
    h=t/n

    T=[]
    T[0]=0
    for j in range(1, n-1):
        T[j]=T[j-1]+h

    X=[]
    X[0]=x0
    for i in range(0, n-1):
        с0 = function(T[i], X[i])
        c1 = function(T[i]+h/2, X[i]+h*(c0/2))
        c2 = function(T[i]+h/2, X[i]+h*(c1/2))
        c3 = function(T[i]+h, X[i]+h*c2)
        X[i+1]=X[i]+(h/6)*(c0+2*c1+2*c2+c3)

    return(X)
