import subprocess
import re
from flask import Flask, Response

app = Flask(__name__)


def telega():
    result = subprocess.run('python telega.py', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return result.stdout.decode('utf-8')


def get_code(text):
    m = re.search(r"'code': '(\d+)'", text)
    if m:
        return m[1]

    return None


@app.route('/')
def index():
    return Response("Hello!", mimetype="text/html")


@app.route('/code')
def code():
    code = get_code(telega())
    return Response(code, mimetype="text/html")


@app.route('/detail')
def detail():
    message = telega()
    return Response(message, mimetype="text/html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
