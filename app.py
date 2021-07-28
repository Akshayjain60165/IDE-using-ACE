from flask import Flask,render_template, request, flash,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import  SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from wtforms.fields.html5 import DateField
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'MLXH243GssUWwKdTWS7FDhdwYF56wPj8'

@app.route('/',methods = ['GET','POST'])
def funcalling():
   return render_template('test.html')
