import requests as rq

req_version = rq.__version__

URL = "http://www.google.com"
r = rq.get(url = URL)

RAW_URL = "https://raw.githubusercontent.com/nasif92/CMPUT404_Lab_1/master/Lab%201/lab1.py"
git_req = rq.get(url=RAW_URL)

print("The request version is", req_version)
print("The google homepage is\n" + r.text,"\n")
print("The python script is\n" + git_req.text,"\n")