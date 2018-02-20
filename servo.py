import pigpio
from time import sleep

PIN=18
STEP=10
LEFT=550
RIGHT=2150
CENTER=(LEFT+RIGHT)/2.0
#note: pulsewidth from about 1220 to 1250 motor produces jitter

pi=pigpio.pi()
pi.set_PWM_frequency(PIN, 50)

#from SG90 datasheet:
#1500us pulse is middle, 
#2000us is all the way right, 
#1000us is all the way left

for i in range(0,4):
	print "i="+str(i)
	print str(i%2)
	if i%2 == 0:
		ra=range(LEFT,RIGHT, STEP)
	else:
		ra=range(RIGHT,LEFT, -1*STEP)

	for p in ra:
		print "pulsewidth="+str(p)
		pi.set_servo_pulsewidth(PIN, p)
		sleep(.1)

pi.set_servo_pulsewidth(PIN, CENTER)
pi.stop()
