from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    'Show the homepage'
    return render_template('home.html'), 200


@app.route('/endpoint', methods=['GET'])
def endpoint():
    'Any custom endpoint - useful when creating APIs'

    return jsonify({"result": "This just works!"}), 200


app.run(debug=True)
