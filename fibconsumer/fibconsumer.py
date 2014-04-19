import urllib2
import os
import sys
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index():
    fibip = os.popen("/usr/bin/serf members -tag role=fibservice | awk {'print $2'} | cut -d':' -f1")
    fibipstr = fibip.read()
    url = 'http://%s:5001/fib' % fibipstr
    response = urllib2.urlopen(url)
    html = response.read()
    return "Hello from fibConsumer! fibService says %s" % html

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)