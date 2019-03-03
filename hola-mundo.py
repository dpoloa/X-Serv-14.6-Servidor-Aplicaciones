#!/usr/bin/python3

# Created by:
# Daniel Polo Álvarez
# d.poloa@alumnos.urjc.es

import webapp

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Programa hola mundo con clases</h1>
    <p> Hola mundo!</p>
  </body>
</html>
"""


class HolaApp(webapp.WebApp):

    def parse(self, request):

        return request.split(' ', 2)[1][1:]

    def process(self, parsedRequest):

        return "200 OK", PAGE


if __name__ == "__main__":
    testWebApp = HolaApp("localhost", 1234)
