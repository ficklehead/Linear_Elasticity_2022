import numpy as np
import managers.functions as fun
def runge_kutt_4 (t, x0, n, bi):
    h=t/n
    if bi == 1:
        function = fun.xfunction
    else:
        function = fun.yfunction
    T=np.arange(0,n-1)
    T[0]=0
    for j in range(1, n-1):
        T[j]=T[j-1]+h

    X=np.arange(0,n-1, dtype=float)
    X[0]=x0
    for i in range(n-2):

        f1 = function(T[i], X[i])
        c1 = function(T[i]+h/2, X[i]+h*(f1/2))
        c2 = function(T[i]+h/2, X[i]+h*(c1/2))
        c3 = function(T[i]+h, X[i]+h*c2)
        X[i+1]=X[i]+(h/6)*(f1+2*c1+2*c2+c3)

    return(X)
