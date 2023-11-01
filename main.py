

# Installing some useful libraries:
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is a stupid docker app....'

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)