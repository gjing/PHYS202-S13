import numpy as np

def pointPotential(x,y,q,Xc,Yc):
	"""return the electrostatic potential"""
	k = 8.9875518e9
	v = (k*q)/(((x-Xc)**2.)+(y-Yc)**2.)**(1/2.) - ((k*q)/(((x-Xc)**2.)+(y+Yc)**2.)**(1/2.))
	return v

def dipolePotential(x,y,q,d):
	return pointPotential(x,y,q,d,0)

