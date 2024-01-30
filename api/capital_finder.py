from http.server import BaseHTTPRequestHandler
import requests
from urllib import parse

class handler(BaseHTTPRequestHandler):
  
  def do_GET(self):
    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components)
    country_dictionary = dict(query_string_list)

    if "country" in country_dictionary:
      # response = requests.get(f"https://restcountries.com/v3.1/name/{country_dictionary["country"]}?fullText=true")
      response = requests.get(f"https://restcountries.com/v3.1/name/Germany?fullText=true")

      response_json = response.json()
      capitals = []
      for country_data in response_json:
        capital = country_data["capital"]
        capitals.append(capital)
        print("capital")
      message = str(capitals)

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(f'{message}'.encode('utf-8'))
    return