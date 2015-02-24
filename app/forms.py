from flask.ext.wtf import Form
from wtforms.fields import TextField
# other fields include PasswordField
from wtforms.validators import required

class UserForm(Form):
  fisrt_name = TextField('first_name', validators=[required()])
  last_name = TextField('last_name', validators=[required()])
  age = TextField('age', validators=[required()])
  sex = TextField('sex', validators=[required()])
  image = TextField('image', validators=[required()])
  
  