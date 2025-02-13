from flask import Flask, render_template

app = Flask(__name__)

user = {'name': 'Илья', 'last_name': 'Евдокимов'}

@app.route('/')
def hello_world():
    return render_template('main.html', user=user)


@app.route('/home')
def home():
    return 'Home page'


app.run()