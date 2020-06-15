# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:10:58 2020

@author: psds0
"""

#import pymongo
import mongoengine as me
import datetime

#myclient = pymongo.MongoClient("mongodb://ai:1111@psds075.iptime.org:27017/")

#print(myclient.list_database_names())

me.connect('project1', host='mongodb://ai:1111@psds075.iptime.org:27017/?authSource=admin')

class Page(me.Document):
    title = me.StringField(max_length=200, required=True)
    date_modified = me.DateTimeField(default=datetime.datetime.utcnow)

'''
page = Page(title='Using MongoEngine2')
page.tags = ['mongodb', 'mongoengine']
page.save()
'''

for page in Page.objects:
    print(page.title)

#print(Page.objects(title='Using MongoEngine').count())

me.disconnect()
