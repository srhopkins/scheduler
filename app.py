#!/usr/bin/env python

import os.path
import cherrypy
import json
 
class Root(object):
    @cherrypy.expose
    #@cherrypy.tools.CORS
    @cherrypy.tools.json_out()
    def api(self):
	data = json.load(open('my.json'))
        return data

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"

current_dir = os.path.dirname(os.path.abspath(__file__))

cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)

conf = {'/': {'tools.CORS.on': True,
              'tools.staticdir.on': True,
              'tools.staticdir.dir': os.path.join(current_dir, 'static'),
              'tools.staticdir.content_types': {'html': 'text/html'},
              'tools.staticdir.index' : 'index.html' }
       }

#cherrypy.config.update("server.conf")
cherrypy.server.socket_host = '0.0.0.0'
#cherrypy.server.socket_port = 80

cherrypy.quickstart(Root(), '/', config=conf)
