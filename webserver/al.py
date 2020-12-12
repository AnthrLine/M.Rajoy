from flask import Flask
app=Flask(__name__)

@app.route('/')
def sayhello():
	return 'Hello'
def keepalive():
	app.debug=True
	app.run()