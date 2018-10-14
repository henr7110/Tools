#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:16:22 2017
@author: Henrik
Calculate a pdf given a coordinate file and periodic table file.
Approximates charges as points only
"""
import math as m
import matplotlib.pyplot as plt

def tableloader():
    """load pereodic table in dictonary table"""
    f = open("ptable.txt")
    table = {}
    for line in f:
        element = line.split(",")
        element[1] = element[1].replace("\n","")
        table[element[0]] = float(element[1])
    return table

def coordinatereader(fil):
    """function that reads a unit cell coordinate file
    ----------Parameters---------
    fil: str, pahtname
        path to coord file. Each line should be in the format "name,x,y,z"
    ----------Returns------------
    List starting with name of first atom (central atom) followed by coordinates
    [x1,y1,z1],[x2,y2,z2]
    """
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
    """Calculate distances between all atoms
    ----------Parameters---------
    coordinates: list of lists
        coordinates in format [[[x1,y1,z1],[x2,y2,z2]...]]
    ----------Returns------------
    list of distances in sample [[atom1,atom2,r],...]
    """
    r = []
    checked = [] # Keep list to ensure no doublecounting
    for i in coordinates:
        x1,y1,z1 = float(i[1][0]),float(i[1][1]),float(i[1][2])
        checked.append(i[1])
        name1 = i[0]
        for u in [x for x in coordinates if x[1] not in checked]:
            name2 = u[0]
            x2,y2,z2 = float(u[1][0]),float(u[1][1]),float(u[1][2])
            r.append((name1,name2,m.sqrt((x2-x1)**2.0+((y2-y1)**2.0)+(z2-z1)**2.0)))
    return r

def avgscat(coordinates,table):
    """calculate average scattering assuming scattering=nuclear number
    ----------Parameters---------
    coordinates: list of lists
        coordinates in format [[[x1,y1,z1],[x2,y2,z2]...]]
    table: dictionary
        map from atom to nuclear number
    ----------Returns------------
    float: Average scattering
    """
    sumb = 0.0
    for i in coordinates:
        sumb += table[i[0]]
    avgb = sumb / float(len(coordinates))
    return avgb

def pdf(coordinatefile,p_0):
    """calculate pdf and plot
    ----------Parameters---------
    coordinatefile: st
        path to coord file. Each line should be in the format "name,x,y,z"
    p_0: float
        multiplicative factor as found in
    """
    #load coordinates
    coordinates = coordinatereader(coordinatefile)
    table = tableloader()
    r = distances(coordinates)
    avgb = avgscat(coordinates,table)
    G = []
    rx = []
    for i in r:
        G.append(1/i[2]*((table[i[0]]*table[i[1]])/(avgb**2))-4*m.pi*p_0*i[2])
        rx.append(i[2])
    plt.plot(rx,G,".",markersize=0.5)
    plt.xlabel("Distance")
    plt.ylabel("G")
    plt.show()
