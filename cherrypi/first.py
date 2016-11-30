#!/usr/bin/python
import cherrypy

class demoExample:
   def index(self):
    return "Hello Pak Iwannn"
   index.exposed = True
cherrypy.quickstart(demoExample())
