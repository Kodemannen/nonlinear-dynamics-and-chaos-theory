import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(nrows=2, ncols=1, sharex=False,  sharey=False)

T = 4
N = 10000
dt = T/(N-1)
t = np.linspace(0, T, N)

x0 = [-2.5, -2, -1, 1, 1.99, 2]        # different initial conditions
                                    # that we iterate over


for x0_ in x0:

    #------------------------------
    # numerical integration:
    #------------------------------

    x     = np.zeros_like(t)
    x_dot = np.zeros_like(t)

    x[0] = x0_                      # setting initial conditions

    for i in range(N-1):

        #--------------------------
        # this part could be 
        # generalized with a 
        # function x_dot[i] = g(x)
        #--------------------------
        x_dot[i] = 4*x[i]**2 - 16
        x[i+1]   = x[i] + x_dot[i]*dt 

    
    ax[0].plot(x, x_dot)
    ax[1].plot(t, x, label=f'x(0)={x0_}')


plt.savefig('testfig.pdf')
