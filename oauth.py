#!/usr/bin/env python
from google.appengine.ext import ndb
import logging
import webapp2
import json
import os
import httplib
import random
import string
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from google.appengine.api import users


class OauthHandler(webapp2.RequestHandler):
    def get(self):
        state = self.request.get('state')
        checkstate = memcache.get(key="state")
        if state == checkstate:
            code = self.request.get('code')
            payload = {
                'code' : code,
                'client_id' : "506935405436-bpi49m874cgaoovcl2grrlgt0tgeg0hg.apps.googleusercontent.com",
                'client_secret' : "R3h0caG2Vuf6a0KCwHx2y7rK",
                'redirect_uri' : "https://key-shine-172121.appspot.com/oauth",
                'grant_type' : "authorization_code",
            }
            header = {"content-type": "application/json"}
            connect = httplib.HTTPSConnection("www.googleapis.com/")
            connect.request('POST', '/oauth2/v4/token', json.dumps(payload), header)
            response = connect.getresponse()
            data = json.loads(response.read().decode('utf8'))
            self.response.out.write(json.dumps(data))
        else:
            self.response.write("Error confirming secret state")

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        code = ''.join(random.choice(string.lowercase) for i in range(9))
        memcache.set(key="state", value=code, time=600)
        gplusurl = "https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id="
        clientid = "506935405436-bpi49m874cgaoovcl2grrlgt0tgeg0hg.apps.googleusercontent.com"
        redirect =  "&redirect_uri=https://key-shine-172121.appspot.com/oauth&scope=email&state="
        url = gplusurl + clientid + redirect + code
        template_values = {
            'url' : url,
        }
        self.response.out.write(template.render(path, template_values))

allowed_methods = webapp2.WSGIApplication.allowed_methods
new_allowed_methods = allowed_methods.union(('PATCH',))
webapp2.WSGIApplication.allowed_methods = new_allowed_methods

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/oauth', OauthHandler),
], debug=True)
