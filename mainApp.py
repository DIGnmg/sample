from flask import Flask
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware


mainApp = Flask(__name__)
mainApp.debug = True

@mainApp.route("/")
def hello():
	return "mainApp"

if __name__ == "__main__":
	run_simple('localhost', 5000, mainApp, use_reloader=True, use_debugger=True,)


