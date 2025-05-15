from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.fields import TextAreaField,SubmitField, StringField
from wtforms.validators import InputRequired, EqualTo, Email

class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired()])
    # adding two validators, one to ensure input is entered and other to check if the 
    # description meets the length requirements
    description = TextAreaField('Description', validators = [InputRequired()])
    image = StringField('Cover Image', validators=[InputRequired()])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField("Create")
    
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email("Please enter a valid email.")])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message="Passwords must match.")])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("Register")

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField("Post Comment")