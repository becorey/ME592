import cherrypy

class StringGenerator(object):
	@cherrypy.expose
	def index(self):
		return "Hello world!"
		
	@cherrypy.expose
	def myfunc(self, a=1, b=2):
		a = float(a)
		b = float(b)
		c = a+b
		line1 = 'a = %s' % a
		line2 = 'b = %s' % b
		line3 = 'c = %s' % c
		mylist = [line1, line2, line3]
		outstr = ' <br> '.join(mylist)
		return outstr
		
	def myfunc2(self, a=7):
		c = a*3
		msg = 'c = %i' % c
		return msg
		
if __name__ == '__main__':
	conf = {'server.socket_host': '0.0.0.0'}
	cherrypy.config.update(conf)
	cherrypy.quickstart(StringGenerator())
