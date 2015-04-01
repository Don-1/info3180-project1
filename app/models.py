from . import db
<<<<<<< HEAD

class Profile(db.Model):
  userid = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  fname = db.Column(db.String(80),nullable=False, index=True)
  lname = db.Column(db.String(80), nullable=False, index=True)
  username = db.Column(db.String(80), index=True, nullable=False, unique=True)
  sex = db.Column(db.String(10), nullable=False, index=True)
  age = db.Column(db.String(25), nullable=False, index=True)
  highscore = db.Column(db.Integer)
  tdollar = db.Column(db.Integer)
  profile_add_on = db.Column(db.String(80), nullable=False)
  image = db.Column(db.String(80), nullable=False) 
  '''
  def __init__(self, fname, lname, username, sex, age, highscore, tdollar):
    self.fname = fname
    self.lname = lname
    self.username = username
    self.sex = sex
    self.age = age
    self.highscore = highscore
    self.tdollar = tdollar
  '''
  def __repr__(self):
    return "<User %r>" % (self.username)
=======
from marshmallow import schema 

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fisrt_name = db.Column(db.String(80))
  last_name = db.Column(db.String(80))
  age = db.Column(db.Integer)
  sex = db.Column(db.String(10))
  image = db.Column(db.String(120))
  
  def __init__(self, fisrt_name, last_name, age, sex, image):
    self.fisrt_name = fisrt_name
    self.last_name = last_name
    self.age = age
    self.sex = sex
    self.image = image
    
  def __repr__(self):
    return '<User %r>' % self.fisrt_name
class UserSchema(schema):
  formatted_name = fields.Method("format_name")
  
class Meta:
  fields = ('fisrt_name','last_name','age','sex','image')
>>>>>>> 220afe0f976d85dc7a46f7cc89eb3ca0a859900f
