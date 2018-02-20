#!/usr/bin/env python

from time import sleep
import random
import RPi.GPIO as GPIO
import StepperMotor

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

m = StepperMotor.Motor([6, 13, 19, 26], 3)
#if rpm is too high or low motor will just vibrate
m.rpm = 15.0
i=0
while i<10:
	r = random.randint(0,180)
	m.move_to(r)
	sleep(0.5)
	i=i+1

GPIO.cleanup()
