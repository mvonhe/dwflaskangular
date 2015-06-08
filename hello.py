"""Cloud Foundry test"""
from flask import Flask
import os

app = Flask(__name__)

if os.getenv("VCAP_APP_PORT"):
	port = int(os.getenv("VCAP_APP_PORT"))
else:
	port = 8080

@app.route('/upper/<input>', methods=['GET'])
def upper(input):
	return input.upper()

@app.route('/lower/<input>', methods=['GET'])
def lower(input):
	return input.lower()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)
