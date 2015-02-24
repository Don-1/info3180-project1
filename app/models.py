from . import db

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