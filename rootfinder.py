#det?#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:27:13 2016
@author: Henrik Pinholt
Function for finding roots of a function
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative as d

def rootfinder(func,xmin,xmax):
    '''finds the roots of the function in the interval
    xmin and xmax and returns a tuple of all the roots
    -------Parameters------
    func: Function
        function that takes x in and returns the y value
    xmin: float
        minimal x-value to find roots
    xmax: float
        max x-value to find roots
    '''
    #massage the inputs and convert to numpy array
    x = np.linspace(xmin,xmax,num=10*(abs(xmax/xmin)))
    vfunc = np.vectorize(func)
    y = vfunc(x)

    #find guess by finding where graph passes x-axis
    guess = []
    for i in range(len(x)):
        if i == 0:
            pass
        else:
            if (y[i] * y[i-1]) < 0:
                guess.append(y[i])
    print ("found %d possible roots, evaluating them now" % (len(guess)))

    #guess and approx using Newtons method while keeping track of
    #convergence of x1 for debugging purposes :D
    overprog = []
    roots = []
    for i in guess:
        x1 = i
        progress = []
        progress.append(x1)
        for i in range(1000):
            x2 = x1 - (func(x1)/d(func,x1,))
            if x2 == x1:
                break
                print ("solution found")
            else:
                x1 = x2
                progress.append(x2)
        overprog.append(progress)
        roots.append(x1)
    for i in range(len(roots)):
        print ("root " + str(i) + " = " + str(roots[i]))
    return roots
    #plt.plot(range(len(overprog[0])),overprog[0])
