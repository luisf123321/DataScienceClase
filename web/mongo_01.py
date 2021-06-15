# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 08:18:59 2018

@author: LUISFERNANDO
"""

import pymongo


from pymongo import MongoClient
from pprint import pprint



client = MongoClient()
#client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://192.168.209.165:27017/')

db = client['iris']

collection = db['especies']
"""
import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}


post_id = collection.insert_one(post).inserted_id
print(post_id)
"""
data = collection.find_one({})

for doc in collection.find({}):
    print(type(doc))
    pprint(doc)

print(type(data))
print(data)
"""
author = data["author"]
text = data["text"]
print(author, text)
"""
