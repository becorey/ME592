import pigpio
from time import sleep
from numpy import arange
import math

PIN=18

pi=pigpio.pi()
pi.set_PWM_frequency(PIN, 200)

dt = 0.01
tl = 15.
n = 3
for t in arange(0., tl, dt):
	brightness = 255*0.5*(1.+math.sin(2*math.pi/(tl/n)*t))
	pi.set_PWM_dutycycle(PIN, brightness)
	print "brightness ="+str(brightness)
	sleep(dt)


pi.stop()
