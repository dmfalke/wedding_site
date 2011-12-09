#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util, template


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render('templates/index.html', {}))


class AboutHandler(webapp.RequestHandler):
    """Info about Kathleen and Dave. Include images."""
    def get(self):
        self.response.out.write(template.render('templates/about.html', {}))


class ChapelHandler(webapp.RequestHandler):
    """About the Day Chapel. With images and map/directions."""
    def get(self):
        self.response.out.write(template.render('templates/chapel.html', {}))

class EngagementPhotosHandler(webapp.RequestHandler):
    """Our Engagement photos!!"""
    def get(self):
        self.response.out.write(template.render('templates/engagement_photos.html', {}))

class WeddingPhotosHandler(webapp.RequestHandler):
    """Our wedding photos!!"""
    def get(self):
        self.response.out.write(template.render('templates/wedding_photos.html', {}))

class HoneymoonPhotosHandler(webapp.RequestHandler):
    """Our Honeymoon photos!!"""
    def get(self):
        self.response.out.write(template.render('templates/honeymoon_photos.html', {}))


class CeremonyHandler(webapp.RequestHandler):
    """About the Classic City. Things to do, places to eat."""
    def get(self):
        self.response.out.write(template.render('templates/ceremony.html', {}))

class AthensHandler(webapp.RequestHandler):
    """About the Classic City. Things to do, places to eat."""
    def get(self):
        self.response.out.write(template.render('templates/athens.html', {}))


class HotelsHandler(webapp.RequestHandler):
    """About the Classic City. Things to do, places to eat."""
    def get(self):
        self.response.out.write(template.render('templates/hotels.html', {}))


class RegistryHandler(webapp.RequestHandler):
    """About the Classic City. Things to do, places to eat."""
    def get(self):
        self.response.out.write(template.render('templates/registry.html', {}))


class MiscHandler(webapp.RequestHandler):
    """About the Classic City. Things to do, places to eat."""
    def get(self):
        self.response.out.write(template.render('templates/misc.html', {}))


class HTTP404Handler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render('templates/404.html', {}))


def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/about/?', AboutHandler),
                                          ('/chapel/?', ChapelHandler),
                                          ('/engagement_photos/?', EngagementPhotosHandler),
                                          ('/wedding_photos/?', WeddingPhotosHandler),
                                          ('/honeymoon_photos/?', HoneymoonPhotosHandler),
                                          ('/ceremony/?', CeremonyHandler),
                                          ('/athens/?', AthensHandler),
                                          ('/hotels/?', HotelsHandler),
                                          ('/registry/?', RegistryHandler),
                                          ('/misc/?', MiscHandler),
                                          ('.*', HTTP404Handler),
                                         ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
