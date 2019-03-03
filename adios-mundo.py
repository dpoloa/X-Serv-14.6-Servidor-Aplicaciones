#!/usr/bin/python3

# Created by:
# Daniel Polo Álvarez
# d.poloa@alumnos.urjc.es

import webapp

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Programa adios mundo con clases</h1>
    <p> Adios mundo cruel...</p>
  </body>
</html>
"""


class AdiosApp(webapp.WebApp):

    def parse(self, request):

        return request.split(' ', 2)[1][1:]

    def process(self, parsedRequest):

        return "200 OK", PAGE


if __name__ == "__main__":
    testWebApp = AdiosApp("localhost", 1234)
