from flask import Flask, render_template

#create a Flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

#def index():
#    return "<h1>Hello World!</h1>"

def index():
    first_name = "sai"
    stuff = "This is <strong>bold</strong> text"
    favourite_pizza = ['Pepperoni',"cheese","Mashroom",41]
    return render_template("index.html",
    first_name = first_name,
    stuff = stuff,
    favourite_pizza = favourite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name = name)

# Create custom error pages

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500