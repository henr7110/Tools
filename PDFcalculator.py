#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:16:22 2017

@author: Henrik
"""
import math as m
import matplotlib.pyplot as plt

def tableloader():
    #load pereodic table in dictonary table
    f = open("ptable.txt")
    table = {}
    for line in f:
        element = line.split(",")
        element[1] = element[1].replace("\n","")
        table[element[0]] = float(element[1])
    return table 
    
def coordinatereader(fil):
    """function that reads a file for coordinates of a unit cell, 
    and returns a list containing the central atom first following tuples of the coordinating 
    atoms and their coordinates""" 
    f = open(fil)
    kompleks = []
    
    for line in f:
        l = line.split(",")
        coordinates =[]
        for i in range(len(l)):
            if i == 0:
                name = l[i]
            else:
                coordinates.append(l[i].replace("\n",""))
        kompleks.append((name,coordinates))
    return kompleks

def distances(coordinates):
    r = []
    checked = []
    for i in coordinates:
        x1 = float(i[1][0])
        y1 = float(i[1][1])
        z1 = float(i[1][2])
        checked.append(i[1])
        name1 = i[0]
        for u in [x for x in coordinates if x[1] not in checked]:
            name2 = u[0]
            x2 = float(u[1][0])
            y2 = float(u[1][1])
            z2 = float(u[1][2])
            r.append((name1,name2,m.sqrt((x2-x1)**2.0+((y2-y1)**2.0)+(z2-z1)**2.0)))
    return r
    
def avgscat(coordinates,table):
    
    sumb = 0.0
    for i in coordinates:
        sumb += table[i[0]]
    avgb = sumb / float(len(coordinates))
    
    return avgb
    
def pdf(coordinatefile,p_0):
    """function that calculates the pdf of a function 
    from coordinates and their position in the periodic table"""
    #load coordinates
    coordinates = coordinatereader(coordinatefile)
    #load table
    table = tableloader()
    #calculate distances
    r = distances(coordinates)
    #calculate avgb
    avgb = avgscat(coordinates,table)
    
    G = []
    rx = []
    for i in r:
        G.append(1/i[2]*((table[i[0]]*table[i[1]])/(avgb**2))-4*m.pi*p_0*i[2])
        rx.append(i[2])

    plt.plot(rx,G,"ro")
    plt.show()
    
def rrpdf(coordinatefile,p_0):
    """function that calculates the pdf of a function 
    from coordinates and their position in the periodic table"""
    #load coordinates
    coordinates = coordinatereader(coordinatefile)
    #load table
    table = tableloader()
    #calculate distances
    r = distances(coordinates)
    #calculate avgb
    avgb = avgscat(coordinates,table)
    
    G = []
    rx = []
    for i in r:
        G.append(((table[i[0]]*table[i[1]])/(avgb**2)))
        rx.append(i[2])

    plt.plot(rx,G,"ro")
    plt.show()
        
    