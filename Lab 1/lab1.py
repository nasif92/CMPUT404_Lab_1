import requests as rq

print(rq.__version__)

URL = "http://www.google.com"
r = rq.get(url = URL)
print(r)