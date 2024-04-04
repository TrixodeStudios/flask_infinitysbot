from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return "Homepage"


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello"

@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.json
    print("Received data:", data)
    return jsonify({"success": True, "msg": "Data received"}), 200

if __name__ == '__main__':
  app.run(port=5000)



