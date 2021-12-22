import json
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def log():
    data = json.loads(request.data)
    print(data)
    return ''

if __name__ == "__main__":
    app.run()
