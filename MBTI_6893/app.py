from flask import Flask, request, render_template
import warnings
from flask_sqlalchemy import SQLAlchemy
import time

warnings.filterwarnings('ignore')

app = Flask(__name__)


def predict(username):
    time.sleep(5)
    return 'intj'


@app.route('/index')
@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/username', methods=['GET', 'POST'])
def get_username():
    username = request.form.get('username')
    print(username)
    # calculating
    if predict(username) == 'intj':
        return render_template("intj.html")
    if predict(username) == 'intp':
        return render_template("intp.html")
    if predict(username) == 'esfp':
        return render_template("esfp.html")
    else:
        return render_template("index.html")


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/intj', methods=['GET', 'POST'])
def intj():
    return render_template('intj.html')


@app.route('/intp', methods=['GET', 'POST'])
def intp():
    return render_template('intp.html')


@app.route('/esfp', methods=['GET', 'POST'])
def esfp():
    return render_template('esfp.html')


if __name__ == '__main__':
    app.run()
