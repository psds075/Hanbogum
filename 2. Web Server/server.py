# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, escape, redirect, url_for, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, AnonymousUserMixin
import mongoengine as me
import datetime
import json
import locale
locale.setlocale(locale.LC_TIME,'ko_KR.UTF-8')

#from werkzeug.security import generate_password_hash, check_password_hash
#from datetime import datetime

me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')

app = Flask(__name__)
app.secret_key = b'123'
DEBUG_MODE = True

app.config['SECRET_KEY'] = '123'

# 로그인 매니저
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class UserList(UserMixin, me.Document):
    Name = me.StringField()
    Email = me.StringField()
    Password = me.StringField()
    DateModified = me.DateTimeField(default=datetime.datetime.utcnow)
    def get_id(self):
        return self.Email

class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.Name = 'GUEST'
        self.Email = 'GUEST'

login_manager.anonymous_user = Anonymous

@login_manager.user_loader
def load_user(id):
    return UserList.objects(Email=id).first()

class OrderList(me.DynamicDocument):
    ProductName = me.StringField()
    Quantity = me.IntField()
    Price = me.IntField()
    BuyerId = me.StringField()
    BuyerName = me.StringField()
    OrderDate = me.StringField()
    Location = me.StringField()
    Status = me.StringField()
    DateModified = me.DateTimeField(default=datetime.datetime.utcnow)

class ProductList(me.DynamicDocument):
    Name = me.StringField()
    ShortDesc = me.StringField()
    LongDesc = me.StringField()
    Option = me.ListField()
    Price = me.ListField()
    DateModified = me.DateTimeField(default=datetime.datetime.utcnow)

# 로그인 및 회원가입
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        check_user = UserList.objects(Email=email)
        if check_user:
            print("Exist")
        else :
            new_user = UserList(name = name, email = email, password = password).save()
            login_user(new_user)
            return redirect(url_for('shop'))
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == True:
        return redirect(url_for('shop'))
    if request.method == 'POST':
        check_user = UserList.objects(Email=request.form['email']).first()
        if(check_user):
            login_user(check_user)
            return redirect(url_for('shop'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('shop'))

# 고객 페이지 관련
@app.route("/", methods=['GET', 'POST'])
def shop():
    return render_template('client_shop.html', user=current_user.Email, ProductList = ProductList.objects())

@app.route("/history", methods=['GET', 'POST'])
@login_required
def shop_history():
    return render_template('client_history.html', user=current_user.Email, OrderList = OrderList.objects(BuyerId=current_user.Email))

@app.route("/mydb", methods=['GET', 'POST'])
def mydb():
    return render_template('client_mydb.html', user=current_user.Email)

# 어드민 페이지 관련
@app.route("/admin", methods=['GET', 'POST'])
@login_required
def admin():
    return render_template('admin_ordermanager.html', user = current_user.Email, OrderList = OrderList.objects())


@app.route("/admin/history", methods=['GET', 'POST'])
def admin_history():
    return render_template('admin_dbmanager.html')

'''
@app.route("/admin/shopmanager", methods=['GET', 'POST'])
def admin_shopmanager():
    return render_template('admin_productmanager.html')
'''

@app.route("/restAPI/<command>", methods=['GET', 'POST'])
def restAPI(command):
    if(command == 'insertOrder'):
        order = request.get_json()
        for i in range(0,len(order['Amounts'])):
            ProductName = order['Name']
            Quantity = int(order['Amounts'][i])
            if(Quantity > 0):
                Price = int(order['Prices'][i].replace(',',''))
                BuyerId = current_user.Email
                BuyerName = current_user.Name
                today = datetime.date.today()
                OrderDate = f'{today.year}년 {today.month}월 {today.day}일'
                Location = '대전'
                Status = '신청'
                item = OrderList(ProductName=ProductName, Quantity=Quantity,Price=Price,BuyerId=BuyerId,BuyerName=BuyerName,OrderDate=OrderDate,Location=Location,Status=Status)
                item.save()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    elif(command == 'deleteOrder'):
        order = request.get_json()
        pk = order['pk']
        item = OrderList.objects(pk=pk)
        item.delete()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    elif(command == 'changeStatus'):
        order = request.get_json()
        pk = order['pk']
        item = OrderList.objects(pk=pk)
        item.update(Status=order['status'])
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    else:
        return json.dumps({'success':False})

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host = '0.0.0.0', port = 80)
    




