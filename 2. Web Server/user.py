# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:10:58 2020
@author: psds0
"""

#import pymongo
import mongoengine as me
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, AnonymousUserMixin
import datetime
import locale
locale.setlocale(locale.LC_TIME,'ko_KR.UTF-8')


# Customer DB
# Define
class CustomerList(me.DynamicDocument):
    ProductName = me.StringField()
    Option = me.StringField()
    Quantity = me.DecimalField()
    BuyerId = me.StringField()
    BuyerName = me.StringField()
    RecentContact = me.StringField()
    Location = me.StringField()
    AS_Status = me.StringField()
    CustomerType = me.StringField()
    CustomerName = me.StringField()
    CustomerPhone = me.StringField()
    CustomerEmail = me.StringField()
    CustomerSpecial = me.StringField()
    CustomerRecord = me.StringField()
    CustomerETC = me.StringField()
    CustomerResult = me.StringField()
    DateModified = me.DateTimeField(default=datetime.datetime.utcnow)

# Create
today = datetime.date.today()
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')

ProductName = '보험증권분석'
Option = 'Option 1'
Quantity = 1
BuyerId = 'psds075@gmail.com'
BuyerName = '김동현'
RecentContact = '6월 28일 오후 3시'
Location = '대전'
AS_Status = '해당없음'
CustomerType = 'Single'
CustomerName = '권숙자'
CustomerPhone = '010-1234-1234'
CustomerEmail = 'sukja@gmail.com'
CustomerSpecial = '기혼, 3인(자녀1), 보험료 20만원대, 본인관리(특별히 관리자는 없음), 암X 뇌혈관X 심혈관X'
CustomerRecord = '[]'
CustomerETC = ''
CustomerResult = '상담중'
item = CustomerList(ProductName=ProductName, Option=Option, Quantity=Quantity, BuyerId=BuyerId, BuyerName=BuyerName, RecentContact=RecentContact, Location=Location, AS_Status=AS_Status, CustomerType=CustomerType, CustomerName=CustomerName, CustomerPhone=CustomerPhone, CustomerEmail=CustomerEmail, CustomerSpecial=CustomerSpecial, CustomerRecord=CustomerRecord, CustomerETC=CustomerETC, CustomerResult=CustomerResult)
item.save()

me.disconnect()

# Read
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
for item in CustomerList.objects(BuyerId='psds075@gmail.com'):
    print(item.ProductName)
    print(item.pk)
me.disconnect()

# Delete All
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
item = CustomerList.objects()
item.delete()
me.disconnect()




'''
# User Account DB
# Define
class UserList(UserMixin, me.Document):
    Name = me.StringField()
    Email = me.StringField()
    Password = me.StringField()
    DateModified = me.DateTimeField(default=datetime.datetime.utcnow)

# Create
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
Name = '김동현'
Email = 'psds075@gmail.com'
Password = '1111'
if UserList.objects(Email=Email):
    print("중복입니다.")
else:
    user = UserList(Name=Name, Email=Email, Password=Password)
    user.save()
me.disconnect()

# Read
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
for item in UserList.objects():
    print(item.Email)
me.disconnect()

# Delete All
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
item = UserList.objects()
item.delete()
me.disconnect()
'''

'''
# Product DB
# Define
class ProductList(me.DynamicDocument):
    Name = me.StringField()
    ShortDesc = me.StringField()
    LongDesc = me.StringField()
    Option = me.ListField()
    Price = me.ListField()
    DateModified = me.DateTimeField(default=datetime.datetime.utcnow)

# Create
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
Name = '보험증권분석'
ShortDesc = '생명보험 관련 DB를 구매할 수 있습니다.'
LongDesc = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vitae condimentum erat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed posuere, purus at efficitur hendrerit, augue elit lacinia arcu, a eleifend sem elit et nunc. Sed rutrum vestibulum est, sit amet cursus dolor fermentum vel. Suspendisse mi nibh, congue et ante et, commodo mattis lacus. Duis varius finibus purus sed venenatis. Vivamus varius metus quam, id dapibus velit mattis eu. Praesent et semper risus. Vestibulum erat erat, condimentum at elit at, bibendum placerat orci. Nullam gravida velit mauris, in pellentesque urna pellentesque viverra. Nullam non pellentesque justo, et ultricies neque. Praesent vel metus rutrum, tempus erat a, rutrum ante. Quisque interdum efficitur nunc vitae consectetur. Suspendisse venenatis, tortor non convallis interdum, urna mi molestie eros, vel tempor justo lacus ac justo. Fusce id enim a erat fringilla sollicitudin ultrices vel metus.'
Option = ['Option 1','Option 2']
Price = [60000,120000]
Product = ProductList(Name=Name, ShortDesc=ShortDesc,LongDesc=LongDesc,Option=Option,Price=Price)
Product.save()
me.disconnect()

# Read
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
for Product in ProductList.objects():
    print(Product.Name)
me.disconnect()

# Delete All
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
Product = ProductList.objects()
Product.delete()
me.disconnect()
'''

'''
# Order DB
# Define
class OrderList(me.DynamicDocument):
    ProductName = me.StringField(required=True)
    Quantity = me.DecimalField()
    Price = me.DecimalField()
    BuyerId = me.StringField()
    BuyerName = me.StringField()
    OrderDate = me.StringField()
    Location = me.StringField()
    Status = me.StringField()
    DateModified = me.DateTimeField(default=datetime.datetime.utcnow)

# Create
today = datetime.date.today()
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
ProductName = '보험증권분석'
Quantity = 1
Price = 60000
BuyerId = 'psds075@gmail.com'
BuyerName = '김동현'
OrderDate = f'{today.year}년 {today.month}월 {today.day}일'
Location = '대전'
Status = '신청'
item = OrderList(ProductName=ProductName, Quantity=Quantity,Price=Price,BuyerId=BuyerId,BuyerName=BuyerName,OrderDate=OrderDate,Location=Location,Status=Status)
item.save()
me.disconnect()


# Read
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
for item in OrderList.objects(BuyerId='psds075@gmail.com'):
    print(item.ProductName)
    print(item.pk)
me.disconnect()

# Delete All
me.connect('HANBOGUM', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
item = OrderList.objects()
item.delete()
me.disconnect()
'''

'''
# Test DB
# Define
class Page(me.DynamicDocument):
    title = me.StringField(max_length=200, required=True)
    date_modified = me.DateTimeField(default=datetime.datetime.utcnow)


# Create
me.connect('project1', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
page = Page(title='Using MongoEngine3')
page.tags = ['mongodb', 'mongoengine']
page.save()
me.disconnect()

# Read
me.connect('project1', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
for page in Page.objects:
    print(page.title)
    if('tags' in page):
        print(page.tags)
me.disconnect()

# Update
me.connect('project1', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
page = Page.objects(title='Using MongoEngine2')
page.update(title='Example Post')
me.disconnect()

# 중복 체크
me.connect('project1', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
if(Page.objects(title='Example Post')):
    print('중복입니다.')
else:
    print('괜찮습니다.')
me.disconnect()

# Delete
me.connect('project1', host='mongodb://ai:1111@dentiqub.iptime.org:27017/?authSource=admin')
page = Page.objects(title='Using MongoEngine3')
page.delete()
me.disconnect()

# Count
print(Page.objects(title='Using MongoEngine').count())
'''