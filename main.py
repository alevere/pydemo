# Copyright 2016 Google Inc.
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

import webapp2
import random

class MainPage(webapp2.RequestHandler):
    def get(self):
        movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html><head><title>Test</title></head><body>')
        self.response.write(random.choice(movie_list))
        self.response.write('</body></html>')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
