from flask import Flask
from pydispatch import dispatcher
import requests, time
from werkzeug.serving import run_simple

app1 = Flask(__name__)
app1.debug = True

first_sender = {'name': 'Steve'}
second_sender = {'name': 'Nate'}
SIGNAL = 'my-first-signal'
SIGNALFAIL = 'FAIL'
SIGNALPASS = 'PASS'

@app1.route("/")
def hello():
	return "Hello World!"

def buildFaild():
	print("FAILD")

def buildPassed():
	print("PASSED")

if __name__ == "__main__":
	dispatcher.connect( buildFaild, signal=SIGNALFAIL, sender=dispatcher.Any )
	dispatcher.connect( buildPassed, signal=SIGNALPASS, sender=dispatcher.Any )
	run_simple('localhost', 6000, app1, use_reloader=True, use_debugger=True,)


