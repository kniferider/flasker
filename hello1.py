from flask import Flask, render_template
from flask_wtf import FlaskForm
#from wtforms import Stringfield, SubmitField
#from wtforms.validators import DataRequired

#Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "FFSSOORRTN555"

# Create a Form Class
class NamerForm(FlaskForm):
	name = Stringfield("What´s Your Name", validators=[DataRequired()])
	submit= SubmitField("Submit")

# Create a route decorator
@app.route('/')

#def index():
#	return "<h1>Hello World!</h1>"

#def index():
#	return render_template("index.html")

def index():
	return render_template("index.html")

# localhost:5000/user/Vali
@app.route('/user/<name>')

def user(name):
	return "<h1>Hello {}</h1>".format(name)


