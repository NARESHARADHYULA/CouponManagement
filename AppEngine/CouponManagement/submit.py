import os
import cgi
import traceback
import json
import jinja2
import webapp2
import logging
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext.webapp.util import run_wsgi_app
from pprint import pprint

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
class homepage(webapp2.RequestHandler):
    """  handles rendering of index page """
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

application = webapp2.WSGIApplication([
    ('/', homepage)
], debug=True)
