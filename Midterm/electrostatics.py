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

def pointField(x,y,q,Xq,Yq):
    k = 8.975518*10**9
    Ex = k*q*(x-Xq)/((x-Xq)**2 + (y-Yq)**2)**.5
    Ey = k*q*(y-Yq)/((x-Xq)**2 + (x-Xq)**2)**.5
    return Ex,Ey
