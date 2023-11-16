import json

from flask import request
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.js')

@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output)
    result = json.loads(output)

if __name__ == "__main__":
    app.run(debug=True)
