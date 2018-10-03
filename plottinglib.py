#det?#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:27:13 2016

@author: Henrik
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def logplotter(c,label1=""):
    x = (np.linspace(-5,5,num=200))
    y = np.log(x*x-c)
    plt.plot(x,y,label=label1)
    
def cp1rew31():
    for i in range(4):
        logplotter(i,label1="log(x^2-%d)"%i)
        print "log(x^2-%d)"%i
        logplotter(-i,label1="log(x^2-%d)"%-i) 
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    plt.show()

def rootfinder(func,xmin,xmax):
    '''finds the roots of the function in the interval xmin and xmax and returns a tuple of all the roots'''
    #massage the inputs and convert to numpy array world
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
    print "found %d possible roots, evaluating them now" % (len(guess))
    
    #guess and approx using Newtons method while keeping track of 
    #convergence of x1 for debugging purposes :D 
    overprog = []
    roots = []
    for i in guess:
        x1 = i
        progress = []
        progress.append(x1)
        for i in range(1000):
            x2 = x1 - (func(x1)/sp.misc.derivative(func,x1,))
            if x2 == x1:
                break
                print "solution found"
            else: 
                x1 = x2
                progress.append(x2)
        overprog.append(progress)
        roots.append(x1)
    for i in range(len(roots)):
        print "root " + str(i) + " = " + str(roots[i])
    return roots
    #plt.plot(range(len(overprog[0])),overprog[0])
            
        
        
        
    