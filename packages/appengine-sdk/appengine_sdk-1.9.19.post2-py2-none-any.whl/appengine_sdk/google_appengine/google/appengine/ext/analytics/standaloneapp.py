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




"""Script which allows analytics to run as stand alone app."""



from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
  """Handler for standalone app."""

  def get(self):
    self.redirect('/stats')


URLMAP = [
    ('/.*', MainPage),
    ]

app = webapp.WSGIApplication(URLMAP, debug=True)


def main():
  run_wsgi_app(app)


if __name__ == '__main__':
  main()
