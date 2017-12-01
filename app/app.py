from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/')
def index():
    return send_file("templates/index.html")

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello Stranger'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
