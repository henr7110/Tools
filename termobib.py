import math as m
import numpy as np
from scipy import stats
import sympy as s

k = 1.3806526 * 10**(-23) #J/K
R_JK = 8.314 #J/molK
R_m3atm = 8.20575 * 10**(-5) #m^3atm/Kmol
h = 6.626176*10**(-34) #Js


# ------------Gibbs free energy----------------------

def Hoff(K,T):
    """returns delH°,delS° from Van't Hoff plot of numpy arrays: K and T (in Kelvin)"""

    lnK = m.log(np.array(K))
    Tinv = np.array(T)**(-1)
    slope, intercept, r_value, p_value, std_err = stats.linregress(Tinv,lnK)
    return -1 * slope * 8.314, intercept * 8.314


# ------------------Partiotion Sums------------------
def qvib(v):
    T = s.Symbol("T")
    return 1.0 / (1.0 - s.exp(-1.0 * (h * v) / (k * T)))

def qtrans(m,V):
    T = s.Symbol("T")
    return (((2 * s.pi * m * k * T) / (h**2))**(3/2)) * V

def qrot(I,sym):
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
