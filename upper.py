"""Cloud Foundry test"""
from flask import Flask, render_template, request
import os

app = Flask(__name__)

if os.getenv("VCAP_APP_PORT"):
	port = int(os.getenv("VCAP_APP_PORT"))
else:
	port = 8080

@app.route('/', methods=['GET'])
def display_template():
	if "lower" in request.args:
		return request.args["lower"].lower()	
	elif "upper" in request.args:
		return request.args["upper"].upper()
	else: 			
		return render_template('index.html')	

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port, debug=True)
