import numpy as np

def pointPotential(x,y,q,posx,posy):
    """returns the potential at x,y"""
    k = 8.9875518*10**9
    q = 1*10**-9
    d=1
    Vyx = (k*q)/((x-posx)**2 + (y-posy)**2)**(1./2.)
    return Vyx

def dipolePotential(x,y,q,d):
    k = 8.9875518*10**9
    q = 1*10**-9
    d=1
    Vxy = (k*q/((x)**2 + (y - d)**2)**(1/2.) - (k*q/(x**2 + (y + d)**2)**(1/2.))) #insert Vxy function
    return Vxy
