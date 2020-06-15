# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, escape, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import mongoengine as me

#from werkzeug.security import generate_password_hash, check_password_hash
#from datetime import datetime

me.connect('HANBOGUM', host='mongodb://ai:1111@psds075.iptime.org:27017/?authSource=admin')

app = Flask(__name__)
app.secret_key = b'123'
DEBUG_MODE = True

app.config['SECRET_KEY'] = '123'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, me.Document):
    name = me.StringField()
    email = me.StringField()
    password = me.StringField()
    def get_id(self):
        return self.email

from flask_login import AnonymousUserMixin
class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.name = 'GUEST'
        self.email = 'GUEST'

login_manager.anonymous_user = Anonymous

@login_manager.user_loader
def load_user(id):
    return User.objects(email=id).first()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        check_user = User.objects(email=email)
        if check_user :
            print("Exist")
        else :
            new_user = User(name = name,email = email,password = password).save()
            login_user(new_user)
            return redirect(url_for('shop'))
    return render_template('register.html')

# 일반 로그인 관련 
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == True:
        return redirect(url_for('shop'))
    if request.method == 'POST':
        check_user = User.objects(email=request.form['email']).first()
        if(check_user):
            login_user(check_user)
            return redirect(url_for('shop'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('shop'))

'''

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')


# 어드민 페이지 관련
@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return render_template('admin_status.html', user = escape(session['username']))
    else:
        return render_template('admin_status.html', user = 'GUEST')

@app.route("/admin/history", methods=['GET', 'POST'])
def admin_history():
    return render_template('admin_history.html')

@app.route("/admin/shopmanager", methods=['GET', 'POST'])
def admin_shopmanager():
    return render_template('admin_shopmanager.html')
'''
# 고객 페이지 관련
@app.route("/", methods=['GET', 'POST'])
def shop():
    print(current_user.email)
    return render_template('client_shop.html', user=current_user.email)

@app.route("/history", methods=['GET', 'POST'])
def shop_history():
    return render_template('client_history.html', user=current_user.email)

@app.route("/mydb", methods=['GET', 'POST'])
def mydb():
    return render_template('client_mydb.html', user=current_user.email)

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host = '0.0.0.0', port = 80)
    




