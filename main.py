import numpy as np
import matplotlib.pyplot as plt
import math as mt
import managers.functions as fn
import managers.integrate_by_runge_kutt as rk

x = np.linspace(2, 6, 1)
y = np.linspace(-2, -6, 1)
t = np.linspace(0, 10, 1)
#vy = fn.yfunction(x,t)
vx = fn.xfunction(x,t)
plt.plot(vx)
#X=rk.runge_kutt_4(t, x0, n, vx)
#Y=rk.runge_kutt_4(t, x0, n, vy)