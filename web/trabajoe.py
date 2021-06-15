# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 12:18:22 2018

@author: LUISFERNANDO
"""
from flask import Flask, jsonify, request
from sklearn.externals import joblib
import numpy as np
import pandas
import json
import sklearn


url = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv'
df=pandas.read_csv(url)

for index, row in df.iterrows():
    #print(row)
    sl = row['sepal_length']
    sw = row['sepal_length']
    print( sl, sw)
    