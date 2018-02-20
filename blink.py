#!/usr/bin/python

#import GPIO to access the pins
import RPi.GPIO as GPIO
#import time to use time.sleep
import time

#pins will be accessed from physical location on board
GPIO.setmode(GPIO.BOARD)
#we are wired to GPIO 26, which is physically pin 37
ledpin=37
#set our LED pin as an output to send current to it
GPIO.setup(ledpin, GPIO.OUT)

#we will loop to blink the led a few times
for i in range(0,10):
	#when i is even the led will turn off
	if i%2==0:
		GPIO.output(ledpin, GPIO.LOW)
		print "gpio low"
	#else, i is odd, and the led will turn on
	else:
		GPIO.output(ledpin, GPIO.HIGH)
		
		print "gpio high"
	#leave the led on/off for 1 second
	time.sleep(1)

#releases the pin setmode back to default
GPIO.cleanup()
print "Done blinking"
