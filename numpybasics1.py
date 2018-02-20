#!/usr/bin/env python

#Author: Corey Berman
#SIUE, ME 592, Summer 2016, Prof Ryan Krauss

#import only what we need
from numpy import arange, sin, pi
from matplotlib.pyplot import figure, clf, xlabel, ylabel, plot, legend, savefig, show

#wrap commonly used plotting functions into a small function
def quickplot(x, y, xlab, ylab):
	"Quick Plot of X, Y with labels"
	clf()
	xlabel(xlab)
	ylabel(ylab)
	plot(x, y, label=ylab)
	legend()
	return		

#constants
SAMPLESTART=0
SAMPLELENGTH=1
dt=0.01
FREQ=2

#plotting variables
t=arange(SAMPLESTART,SAMPLELENGTH,dt)
y1=sin(2*pi*FREQ*t)

#make the plot
figure(1)
quickplot(t, y1, "time (s)", "$y(t)$")

#save as an image
savefig("numpybasicsplotting.png", dpi=300)
