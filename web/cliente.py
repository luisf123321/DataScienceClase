# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:49:26 2018

@author: LUISFERNANDO
"""
import socket


mysocket = socket.socket()
mysocket.connect(('localhost',8000))

mysocket.send("hola cliente")
respuesta = mysocket.recv(1024)

mysocket.close()