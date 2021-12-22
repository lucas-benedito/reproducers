# reproducers

- Configuring a simple Flask API for GET/POST requests

Create a venv with the Flask packages
```
# /usr/libexec/platform-python -m venv piprepo
# source piprepo/bin/activate
# pip install flask
```

Create the flask app.py with contents similar to this:
```
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
        data = str(request.json)
        with open('/tmp/test.txt', 'w') as final:
            final.write(data)
        return "Ok"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```

Run the Flask APP and make GET/POST Requests
```
FLASK_APP=app flask run -p 8080
```
To define the ip for the app, run as follows:
```
FLASK_APP=app flask run -h 192.168.1.x -p 8080
```