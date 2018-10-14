"""Author: Henrik Pinholt
Created: 4. november 2017 kl. 23.30
Small library of functions for thermodynamic computations and to check out
sympy features
"""


#Initialize
import math as m
import numpy as np
from scipy import stats
import sympy as s
k = 1.3806526 * 10**(-23) #J/K Boltzmans constant
R_JK = 8.314 #J/molK The gas constant
R_m3atm = 8.20575 * 10**(-5) #m^3atm/Kmol Gas constant in different units
h = 6.626176*10**(-34) #Js Plancks constant


# ------------Gibbs free energy----------------------
def Hoff(K,T):
    """returns delH°,delS° from Van't Hoff plot of numpy arrays: K and T (in Kelvin)
    ----------Parameters---------
    K: float, len(T)
        array of measured heat capacities
    T:
        array of temperatures at which the heat capacities were measured
    ----------Returns------------
    delH°: float
        Standard enthalpy for the process
    delS°: float
        Standard entropy for the process
    """
    lnK = m.log(np.array(K))
    Tinv = np.array(T)**(-1)
    slope, intercept, r_value, p_value, std_err = stats.linregress(Tinv,lnK)
    return -1 * slope * 8.314, intercept * 8.314

# ------------------Partition Sums------------------
def qvib(v):
    """Calculates the vibrational partition function, assuming harmonic motion
    around the vibrational angular frequency omega.
    ----------Parameters---------
    v: float
        vibrational frequency in m^-1
    ----------Returns------------
    float
        vibrational part of the partition function
    """
    T = s.Symbol("T")
    return 1.0 / (1.0 - s.exp(-1.0 * (h * v) / (k * T)))

def qtrans(m,V):
    """Calculates the translational partition function, assuming free movement
    ie. no spatial potential.
    ----------Parameters---------
    m: float
        mass of the molecule in kg
    V: float
        m^3 volume of the container
    ----------Returns------------
    float
        translational part of the partition function
    """
    T = s.Symbol("T")
    return (((2 * s.pi * m * k * T) / (h**2))**(3/2)) * V

def qrot(I,sym):
    """Calculates the rotational partition function, assuming rigid rotor
    ----------Parameters---------
    I: array [I_x,I_y,I_z] or float I
        [kgm^2] moment of inertia, either around the three principal axis of rotation in space
        or for linear molecules just the float specifying the one compoment of rotation
    sym: int
        symmetry number, the number of ways in which the molecule can be
        brought into itself through symmetry operations/number of similar rotation axis
    ----------Returns------------
    float
        rotational part of the partition function
    """
    T = s.Symbol("T")
    if type(I) == list:
        return (((s.pi * I[0] * I[1] * I[2])**(1/2))/sym) * ((8 * s.pi**2 * k * T) / (h**2))**(3/2)
    else:
        return (((s.pi * I)**(1/2))/sym) * ((8 * s.pi**2 * k * T) / (h**2))**(3/2)

def partition(v,m,I,V,sym):
    """returns partition sum without electronic contribution,
    v = vibrational frequency in m^-1,  m = mass in kg, I=moment of inertia either
    number or list of three [kgm^2], V= Volume in m^3, sym=number of similar rotation axis """
    T = s.Symbol("T")
    return qvib(v) + qtrans(m,V) + qrot(I,sym)

# ---------------------interface-----------------------

Hoff(K,T)
partition(v,m,I,V,sym)
