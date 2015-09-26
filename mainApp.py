from flask import Flask
from pydispatch import dispatcher
import requests, time
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from app1 import app1 as app1
from app2 import app2 as app2

mainApp = Flask(__name__)
mainApp.debug = True

app = DispatcherMiddleware(mainApp, {
    '/app1':     app1,
    '/app2':     app2
})

@mainApp.route("/")
def hello():
	print('mainApp')
	return "mainApp"

if __name__ == "__main__":
	run_simple('localhost', 5000, app, use_reloader=True, use_debugger=True,)


