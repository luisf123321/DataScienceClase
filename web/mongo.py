# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:00:57 2018

@author: LUISFERNANDO
"""

import pandas
import psycopg2

url="https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv"
df = pandas.read_csv(url)

import pymongo

from pymongo import MongoClient
from pprint import pprint

mongourl='mongodb://iris:LU0987654321i.S@ds263380.mlab.com:63380/iris'

client = MongoClient()

#client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://192.168.209.165:27017/')



db = client['iris']

collection = db['especies']



for index, row in df.iterrows():
    sl=row['sepal_length']
    sw=row['sepal_width']
    pl=row['petal_length']
    pw=row['petal_width']
    sp=row['species']
    
    post = {"sl": sl,"sw": sw, "pl":pl, "pw": pw }
    
    post_id = collection.insert_one(post).inserted_id
    print(post)

