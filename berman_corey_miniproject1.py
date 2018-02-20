#!/usr/bin/env python

#Mini-Project #1 LED Morse Code
#Author: Corey Berman
#SIUE, ME 592, Summer 2016, Prof Ryan Krauss

import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BOARD)
ledpin=37
GPIO.setup(ledpin, GPIO.OUT)

def blinkmorse(msg, ledpin):
	morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..'}

	#length of a dot, in seconds
	tdot=0.200
	#length of a dash is 3 times length of a dot
	tdash=3*tdot
	#length between dots and dashes within one character is one time unit
	tinter=tdot
	#length between letters is 3 time units
	tletter=3*tdot
	tword=7*tdot

	for i in range(len(msg)):

		morsel=morse[msg[i]]
		print msg[i] + " " + morsel

		GPIO.output(ledpin, GPIO.LOW)
		for j in range(len(morsel)):
			GPIO.output(ledpin, GPIO.HIGH)
			if morsel[j] == '.':
				time.sleep(tdot)
			elif morsel[j] == '-':
				time.sleep(tdash)
			else:
				break
			GPIO.output(ledpin, GPIO.LOW)
			time.sleep(tinter)
		GPIO.output(ledpin, GPIO.LOW)
		time.sleep(tletter)	

name='corey'

blinkmorse(name, ledpin)

GPIO.cleanup()
print "Done"
