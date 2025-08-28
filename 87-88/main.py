from flask import Flask, render_template

app = Flask('my_app')

my_books = [
    {'name': 'Идиот', 'author': 'Достоевкий'},
    {'name': 'Мертвые души', 'author': 'Гоголь'},
]
@app.route("/")
def hello():
    return '<h1>Hello world!</h1>'

@app.route("/books")
def books():


    return render_template('books.html', my_books=my_books)

app.run(debug=True)