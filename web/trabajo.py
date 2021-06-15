# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:44:49 2018

@author: LUISFERNANDO
"""
import ast

import pymongo

from pymongo import MongoClient
from pprint import pprint

import urllib.parse

#client = MongoClient()


import serial, time
arduino = serial.Serial('COM5', 9600)
id = 1
while True:
    time.sleep(2)
    rawString = arduino.readline()
    d = rawString.decode('ASCII')
    a = "{" + d +","+ "'"+"id" +"'"+ ":" + str(id) + "}"
    #print(a)
    b = ast.literal_eval(a)
    print(b)
    #print(type(rawString))
    id = id + 1 
    #post_id = set(mongourl , b)
    #campos = urllib.parse.urlencode({"sl": 3.2})
    import json
    import urllib.request
    conditionsSetURL = 'https://frozen-temple-13834.herokuapp.com/pets/guardar'
    newConditions = b 
    print(type(newConditions))
    params = json.dumps(newConditions).encode('utf8')
    req = urllib.request.Request(conditionsSetURL, data=params,headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf8'))
    #sitio = urllib.request.urlopen("http://localhost:8080/pets/clasificar", rawString)
    #print (sitio.read())
    
arduino.close()
