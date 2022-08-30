from datetime import datetime
from blog import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  title = db.Column(db.Text, nullable=False)
  content_summary = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text, nullable=False)
  image_file = db.Column(db.String(40), nullable=False, default='default.jpg')
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"Post('{self.date}', '{self.title}', '{self.content_summary}', '{self.content}')"

class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(20), unique=False, nullable=False)
  last_name = db.Column(db.String(20), unique=False, nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  hashed_password=db.Column(db.String(128))
  post = db.relationship('Post', backref='user', lazy=True)
  comment = db.relationship('Comments', backref='user', lazy=True)

  def __repr__(self):
    return f"User('{self.username}', '{self.password}')"


#adapted from Grinberg(2014, 2018)
  @property
  def password(self):
    raise AttributeError('Password is not readable.')

  @password.setter
  def password(self,password):
    self.hashed_password=generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.hashed_password,password)


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class Comments(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  body = db.Column(db.Text, nullable=False)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
  post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=True)

  def __repr__(self):
    return f"Comments('{self.date}', '{self.body}', '{self.author_id}')"