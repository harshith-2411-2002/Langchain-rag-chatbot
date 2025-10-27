from flask import Flask, request, jsonify , render_template
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from user import add_user_input_to_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/add_user_input', methods=['POST'])
def add_user_input():
    try:
        user_input = request.form['user_input']
        success = add_user_input_to_db(user_input)
        if success == 1 :
            return jsonify({'response': 'User input added to the database.'})
        else:
            return jsonify({'response': 'Failed to add user input to the database.'})
    except Exception as e:
        return jsonify({'response': f"An error occurred from add_user_input: {e}"})

if __name__ == '__main__':
    app.run(port=5001)
app.run(debug=True)
