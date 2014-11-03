import webapp2
import string
import cgi

form = """
  <form method="post">
    What is your Birthday?
    <br>
    <label> Month
      <input type="text" name="month">
    </label>
    <label> Day
    <input type="text" name="day">
    </label>
    <label> Year
    <input type="text" name="year">
    </label>
    <br>
    <input type="submit">
  </form>
"""

rot13 = """
  <h1>Enter some text to ROT13:</h1>
  <form method="post">
    <textarea name="text" style="height: 100px; width: 400px">%(text)s</textarea>
    <br>
    <br>
    <input type="submit">
  </form>
"""

def escape_html(s):
  return cgi.escape(s, quote=True)

def rot_13(string):
  return string.encode("rot13")


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
      self.response.out.write("Thanks!")

class Rot13(webapp2.RequestHandler):
  def write_form(self, s=""):
    self.response.out.write(rot13 % {"text" :escape_html(s)})

  def get(self):
    self.write_form()

  def post(self):
    user_input = self.request.get('text')
    crypto = rot_13(user_input)
    self.write_form(crypto)

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/rot13', Rot13)
], debug=True)
