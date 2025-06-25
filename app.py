from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)
names = ["Swastik", "Tania", "Rohit", "Dia", "Naman", "Ashok"]

@app.route('/')
def index():
    return render_template('random.html')

@app.route('/random')
def random_name():
    return jsonify({"name": random.choice(names)})

if __name__ == '__main__':
    app.run()
