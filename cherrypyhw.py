from __future__ import division
import cherrypy
import RPi.GPIO as GPIO
import time

class Website(object):
	@cherrypy.expose
	def index(self):
		#get the user input
		return """<html>
			<head></head>
			<body>
				<form method="get" action="submit">
					<table>
					<tr>
					<td>Time [seconds]</td>
					<td>
						<input type="text" value="5" name="time" />
					</td>
					</tr>
					<tr>
					<td>Number of Blinks</td>
					<td>
						<input type="text" value="3" name="num" />
					</td>
					</tr>
					<tr>
					<td colspan="2">
						<button type="submit">Blink!</button>
					</td>
					</tr>
					</table>
				</form>
			</body>
		</html>"""
		
	@cherrypy.expose
	def submit(self, time, num):
		time = float(time)
		num = int(num)
		
		GPIO.setmode(GPIO.BOARD)
		light = LED(40)
		
		#save us from blinking for a long time
		if time > 30 :
			time = 30
		
		#standard off time of 200 msec
		offtime = .2
		#time = num*(ontime + offtime)
		ontime = time/num - offtime
		
		#prevent error from negative ontime
		if ontime < 0:
			ontime = time/(2*num)
			offtime = ontime
		
		#do the blinking
		for i in range(0, num):
			light.blink(ontime, offtime)
		
		#tell user what we did
		html = 'blinking '+str(num)+' times, over '+str(time)+' seconds'
		html = html + "<br><a href=\"/\">Return</a>"
		return html
	
class LED(object):
	"Handy LED class for blinking"
	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)
		
	def blink(self, ontime, offtime):
		#this is blocking with time.sleep, could be improved with threading
		GPIO.output(self.pin, GPIO.HIGH)
		time.sleep(ontime)
		GPIO.output(self.pin, GPIO.LOW)
		time.sleep(offtime)
		
		
if __name__ == '__main__':
	cherrypy.quickstart(Website())

