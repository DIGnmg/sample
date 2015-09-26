from flask import Flask
from pydispatch import dispatcher
import requests, time
from werkzeug.serving import run_simple

app2 = Flask(__name__)
app2.debug = True

first_sender = {'name': 'Steve'}
second_sender = {'name': 'Nate'}
SIGNAL = 'my-first-signal'
SIGNALFAIL = 'FAIL'
SIGNALPASS = 'PASS'

@app2.route("/")
def hello():
	print('APP2')
	return "APP2"

def buildFaild():
	print("FAILD")

def buildPassed():
	print("PASSED")

if __name__ == "__main__":
	dispatcher.connect( buildFaild, signal=SIGNALFAIL, sender=dispatcher.Any )
	dispatcher.connect( buildPassed, signal=SIGNALPASS, sender=dispatcher.Any )
	# app2.run(port=5555)
	run_simple('localhost', 7000, app2, use_reloader=True, use_debugger=True,)


