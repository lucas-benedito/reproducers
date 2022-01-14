import re
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route("/api/logfile", methods=['GET', 'POST'])
def post_logfile():
    if request.method == 'GET':
        with open('/tmp/test.txt', 'rb') as data:
            final = str(data.readlines())
        return "OK"
    elif request.method == 'POST':
        if request.json:
            data = str(request.json)
        if request.values:
            data = str(request.values)
        with open('/tmp/test.txt', 'w') as final:
            final.write(data)
        return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090)
