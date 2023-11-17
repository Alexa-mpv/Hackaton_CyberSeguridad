import json
import openai

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
    print("si entro")
    conexion(output)
    
    result = json.loads(output)



def conexion(prompt):
    openai.api_key = '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'

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
    
