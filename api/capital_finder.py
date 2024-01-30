from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
  
  def do_GET(self):
    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components)
    country_dictionary = dict(query_string_list)

    if "country" in country_dictionary:
      response = requests.get(f"https://restcountries.com/v3.1/name/{country_dictionary['country']}?fullText=true")
      # response = requests.get(f"https://restcountries.com/v3.1/name/Germany?fullText=true")
      response_json = response.json()
      capitals = []
      capital = response_json[0]["capital"][0]
      capitals.append(capital)
      message = f"The capital of {country_dictionary['country']} is {capital}"
    elif "capital" in country_dictionary:
      response = requests.get(f"https://restcountries.com/v3.1/capital/{country_dictionary['capital']}")
      response_json = response.json()
      country = response_json[0]["name"]["common"]
      message = f"{country_dictionary['capital']} is the capital of {country}"
    else:
      message = "Please enter a valid capital or country"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode('utf-8'))
    return