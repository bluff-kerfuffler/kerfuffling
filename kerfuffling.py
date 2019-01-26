from flask import Flask
from flask import jsonify
import json
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/verify', methods=['GET'])
def face_auth(data):
  d = json.loads(data)
  session = create_session(d['userId'])
  response = requests.request(
    'POST', 
	'https://api.aimbrain.com:443/v1/face/auth',
	headers={
	  'Content-Type': 'application/json', 
	  'X-aimbrain-apikey': 'test',
	  'X-aimbrain-signature': 'dBxk9M++dNhI7pk+tXvAVaUwlWuOPl8S4wlmrhKhSqs='
	},
	json=json.dump({
	  'session': session,
	  'faces': d['images']
	})
  )
  return response
 
@app.route('/enroll', methods=['GET'])
def face_enroll(data):
  response = requests.request(
    'POST', 
	'https://api.aimbrain.com:443/v1/face/enroll',
	headers={
	  'Content-Type': 'application/json', 
	  'X-aimbrain-apikey': 'test',
	  'X-aimbrain-signature': 'VXNfJLbOntEVUlOp6UUwo8D4YyKjNtzspeBCOqZYM9A='
	},
	json=data
  )
  return response
  
def create_session(id):
  return requests.request(
    'POST', 
	'https://api.aimbrain.com:443/v1/face/sessions',
	headers={
	  'Content-Type': 'application/json', 
	  'X-aimbrain-apikey': 'test',
	  'X-aimbrain-signature': 'E7vPXCNHsJQhadkTruAbCE+q9fCmRK9Gf+wtl2/3yrA='
	},
	json=Flask.jsonify({
	  "device": "test", 
	  "screenHeight": 0, 
	  "screenWidth": 0, 
	  "userId": id, 
	  "system": "test"
	})
  )


@app.route('/')
def index():
  return "hi"
  
if __name__ == '__main__':
    app.run(debug=True)