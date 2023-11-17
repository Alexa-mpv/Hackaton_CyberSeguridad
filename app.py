import json
import openai

from flask import request
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.js')

@app.route('/test', methods=['GET', 'POST'])
def test():
    
    if request.method == 'POST':
    
        output = request.get_json()
        print(output)
        print("si entro")
        conexion(output)
        
        result = json.loads(output)
        return 'OK', 200
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)



def conexion(prompt):
    openai.api_key = ''

    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    print(completion)
    print("finish")

if __name__ == "__main__":
    app.run(debug=True)
    
