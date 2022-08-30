from datetime import datetime
from xml.etree.ElementTree import Comment
from flask import render_template, url_for, request, redirect, flash
from blog import app, db
from blog.models import User, Post, Comments
from blog.forms import RegistrationForm, LoginForm, CommentForm
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")

@app.route("/home", methods=['GET','POST'])
def home():
  posts=Post.query.all()
  return render_template('home.html',posts=posts)

@app.route("/about", methods=['GET','POST'])
def about():
  return render_template('about.html', title='About')

@app.route("/post/<int:post_id>", methods=['GET','POST'])
def post(post_id):
  post=Post.query.get_or_404(post_id)
  comments_post = Comments.query.filter_by(post_id=post_id).all()
  return render_template('post.html',title=post.title,post=post, comments_post=comments_post)


@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(email=form.email.data, password=form.password.data, first_name=form.first_name.data, last_name=form.last_name.data)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    flash('Registration successful!')
    return redirect(url_for('home'))
  return render_template('register.html',title='Register',form=form)


@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('You\'ve successfully logged in,'+' '+ current_user.first_name +'!')
      return redirect(url_for('home'))
    flash('Invalid username or password.')
  return render_template('login.html',title='Login', form=form)

@app.route("/logout")
def logout():
  logout_user()
  flash('You\'re now logged out. Thanks for your visit!')
  return redirect(url_for('home'))

@app.route("/staticsecurity")
def staticposts():
  return render_template('staticsecurity.html', title='Static Version of Security')

@app.route("/quality_usability")
def quality_usability():
  return render_template('quality_usability.html', title='Static Version of Quality and Usability')



@app.route("/addcomment", methods=['GET','POST'])
def addcomment():
  post_id = request.args.get('post_id')
  form = CommentForm()
  if form.validate_on_submit():
    comment = Comments(body=form.body.data, author_id=current_user.id, post_id=post_id)
    db.session.add(comment)
    db.session.commit()
    flash('Your Comment has been Posted!')
    return redirect(url_for('home'))
  return render_template('addcomment.html', title='Add a Comment', form=form, post_id=post_id)

