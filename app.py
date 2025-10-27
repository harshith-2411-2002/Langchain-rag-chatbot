from flask import Flask, render_template, request, jsonify
from model import final_result

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        user_input = request.form['user_input']
        response = final_result(user_input)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': f"An error occurred from send message: {e}"})
if __name__ == '__main__':
    app.run(debug=True)
