import http.client
import urllib
import os

def send_message(to, body):

    conn = http.client.HTTPSConnection("api.msg91.com")
    AUTH_KEY = os.environ.get('AUTH_KEY', '')
    SENDER = os.environ.get('SENDER', '')

    conn.request("GET", "/api/sendhttp.php?route=1&sender="+ SENDER +"&message=" + urllib.parse.quote_plus(body) +
                "&country=91&"+
                "mobiles="+ to +"&authkey="+ AUTH_KEY)

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8") )