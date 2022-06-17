import requests
host="http://localhost:8000"
res=requests.get(host)
res.encoding="utf-8"
print(res.text)
