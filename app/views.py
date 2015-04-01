from app import app
<<<<<<< HEAD
from flask import render_template, request, redirect, url_for, flash, jsonify, session, send_file
import os
from os import path
from werkzeug import secure_filename
from flask_wtf.file import FileField
import json
from .forms import Profile
from db_insert import *
from . import db, models
import time

=======
from flask import render_template, request, redirect, url_for
from app import db
from app.models import User
from .forms import UserForm
###
# Routing for your application.
###
>>>>>>> 220afe0f976d85dc7a46f7cc89eb3ca0a859900f

@app.route('/profile/', methods=["GET", "POST"])
def profile():
  form = UserForm(csrf_enabled=False)
  if request.method == 'POST' and form.validate():
    user = User(form.fisrt_name.data, form.last_name.data, form.age.data, form.sex.data,
                    form.image.data)
    db_session.add(user)
    db.session.commit()
  return render_template('profile.html', form=form)

@app.route('/profiles/', method=["GET"])
def profiles():
  

@app.route('/')
<<<<<<< HEAD
@app.route('/index')
def index():
  return render_template('index.html', title="Home")

@app.route('/viewprofile', methods=['GET', 'POST'])
def viewprofile():
  u = models.Profile.query.all()
  return render_template("profile 2.html", title="View User GUI", u=u)
  

@app.route('/games', methods=['GET', 'POST'])
def games():
  return render_template("/proj-1/index.html", title="game")
  
  
@app.route('/gui_profile/<idNo>', methods=['GET', 'POST'])
def gui_profile(idNo):
  a = models.Profile.query.get(idNo)
  return render_template('profile 3.html', userid= str(a.userid), fname=str(a.fname), lname=str(a.lname), username=str(a.username), sex=str(a.sex), age=str(a.age), highscore=str(a.highscore), tdollar=str(a.tdollar), profile_add_on=str(a.profile_add_on), files=[f for f in os.listdir('app/static') if f==str(a.image)][0])


#create new profile
@app.route('/profile', methods=['POST', 'GET'])
def profile():
  form = Profile()
  if form.validate()==True and request.method == 'POST':
    filename = secure_filename(form.image.data.filename)
    form.image.data.save(os.path.join('app/static', filename))
    insert(form.fname.data, form.lname.data, form.username.data, form.sex.data, form.age.data, filename, 0, 0)
    
    flash('%s\'s was successfully login' % form.username.data)
    return redirect(url_for('index'))
    
  return render_template('profile 1.html', title='Sign Up', form=form)


#list of profiles
@app.route('/profiles', methods=['POST', 'GET'])
def profiles():
  u = models.Profile.query.all()
  lst=[]
  
  for i in u: 
    dic = {'username':i.username, 'userid':i.userid}
    lst += [dic]
    
  usr = {'users':lst}
  return jsonify(usr)
   

#view a profile
@app.route('/profile/<userid>', methods=['GET', 'POST'])
def profileView(userid):
  u = models.Profile.query.filter_by(userid=userid).first_or_404()
  
  return jsonify({
                  'userid':u.userid, 
                  'username':u.username, 
                  'sex':u.sex, 
                  'age':u.age, 
                  'highscore':u.highscore, 
                  'tdollar':u.tdollar,
                  'profile_add_on':u.profile_add_on,
                  'image':u.image
                 })
=======
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/person')
def person():
  first_user = db.session.query(User).first()
  return "fisrt_name: {}, last_name: {}, age: {}, sex: {}, image: {}".format(first_user.fisrt_name, first_user.last_name, first_user.age, first_user.sex, first_user.image)
  

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

>>>>>>> 220afe0f976d85dc7a46f7cc89eb3ca0a859900f

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html', title='404'), 404

if __name__ == '__main__':
<<<<<<< HEAD
  app.run(debug=True, host='0.0.0.0', port=8080)
=======
    app.run(debug=True,host="0.0.0.0",port="8080")
>>>>>>> 220afe0f976d85dc7a46f7cc89eb3ca0a859900f
