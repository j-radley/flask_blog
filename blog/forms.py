import email
from email.message import EmailMessage
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp, Length, Email
from blog.models import User, Comments

class RegistrationForm(FlaskForm):
  first_name = StringField('First Name', validators=[DataRequired(),Regexp('^[a-z]{3,20}$', message='Your first name should be between 3 and 20 characters long, and can only contain lowercase letters.')])
  last_name = StringField('Last Name', validators=[DataRequired(),Regexp('^[a-z]{3,20}$', message='Your last name should be between 3 and 20 characters long, and can only contain lowercase letters.')])
  email = StringField('Email', validators=[DataRequired(), Regexp('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', message='Your email must be formatted correctly and be under 100 characters. e.g. johndoe@flaskblog.com')])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Register')
  def validate_email(self, field):
   email = User.query.filter_by(email=field.data).first()
   if email is not None:
     raise ValidationError('This email already exists. Please sign up with another email!')


class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')

class CommentForm(FlaskForm):
  body = StringField('Comment',validators=[DataRequired()])

