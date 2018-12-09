#!flask/bin/python
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    f = open("/var/data/visitor.txt", "a")
    if request.environ.get('HTTP_X_REAL_IP') is None:
        f.write(request.environ['REMOTE_ADDR'] + "\n")
        f.close()
        return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    else:
        f.write(request.environ['HTTP_X_REAL_IP'] + "\n")
        f.close()
        return jsonify({'ip': request.environ['HTTP_X_REAL_IP']}), 200

@app.route('/visitors', methods=['GET'])
def get_visitors():
    location_data = []
    f = open("/var/data/visitor.txt", "r")
    for line in f:
        line = line.split()
        location_data.append({"ip": line[0]})

    location_data = {"location_data": location_data}
    f.close()
    return json.dumps(location_data), 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)