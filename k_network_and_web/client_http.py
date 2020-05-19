from urllib import request, parse
import requests


# Base URL being accessed
url_get = 'http://httpbin.org/get'
url_post = 'http://httpbin.org/post'

# Dictionary of query parameters
params = {
    'name1': 'value1',
    'name2': 'value2'
}

# Encode the query string
query_string = parse.urlencode(params)

# Make a GET request and read the response
u = request.urlopen(url_get + '?' + query_string)
resp = u.read()
print(resp)

# Make a POST request and read the response
u = request.urlopen(url_post, query_string.encode('ascii'))
resp = u.read()
print(resp)

# extra headers
headers = {
    'User-agent': 'none/ofyoubusiness',
    'Spam': 'Eggs'
}

req = request.Request(url_post, query_string.encode('ascii'), headers=headers)
u = request.urlopen(req)
resp = u.read()
print(resp)
# same as
resp = requests.post(url_post, data=params, headers=headers)
text = resp.text
print(text)

# head request
resp = requests.head('http://www.python.org/index.html')
status = resp.status_code
print(type(resp.headers))
# last_modified = resp.headers['last-modified']
# print(last_modified)
# content_type = header['Content-Type']
# print(content_type)
# content_length = header['Content-Length']
# print(content_length)

# sing in
resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('user', 'password'))

# pass cookies to next get
resp1 = requests.get(url_get)
resp2 = requests.get(url_get, cookies=resp1.cookies)

# upload files
files = {'file': ('data.csv', open('./utils/data.csv', 'rb'))}
r = requests.post(url_post, files=files)
