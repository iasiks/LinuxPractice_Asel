from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, World from ismukhanova_server!<!p><p>This is Linux A.<!p>"

@app.route('/get', methods=['GET'])
def handle_get():
    return "This is a GET request response from Linux A (ismukhanova_server)."

@app.route('/post', methods=['POST'])
def handle_post():
    return "This is a POST request response from Linux A (ismukhanova_server). Received data: {data}"

@app.route('/put', methods=['PUT'])
def handle_put():
    data = request.data.decode() if request.data else "No data sent in PUT body"
    return "This is a PUT request response from Linux A (ismukhanova_server). Received data: {data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)