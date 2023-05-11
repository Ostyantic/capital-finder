from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        url = self.path
        # print(f'url is: {url}')
        url_list = parse.urlsplit(url)
        # print(f'url_list is: {url_list}')
        query_list = parse.parse_qsl(url_list.query)
        # print(f'query list is: {query_list}')
        query_dict = dict(query_list)
        # print(f'query dict is: {query_dict}')

        message = ''

        country = query_dict.get('country')
        country_url = f'https://restcountries.com/v3.1/name/{country}'

        capital = query_dict.get('capital')
        capital_url = f'https://restcountries.com/v3.1/capital/{capital}'

        if country:
            r = requests.get(country_url)
            data = r.json()
            capital_name = data[0]['capital'][0]
            message = f"The capital of {country} is {capital_name}"
        elif capital:
            r = requests.get(capital_url)
            data = r.json()
            country_name = data[0]['name']['common']
            message = f"{capital} is the capital of {country_name}"
        else:
            message = 'Please enter a valid country or capital'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, handler)
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
