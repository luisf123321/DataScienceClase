# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:32:19 2018

@author: LUISFERNANDO
"""


"""
from gtts import gTTS
tts = gTTS('hello usco 2018', lang="es")
tts.save('hello.mp3')
"""

"""
italiano = it
frances = fr
ingles = en
aleman = de 
español = es


db.
{"language":"en","GM":"Good morning","GA":"Good afternoon","GE":"Good evening"}
{"language":"it","GM":"Buongiorno","GA":"buon pomeriggio","GE":"buona notte"}
{"language":"fr","GM":"Bonjour","GA":bonsior"","GE":"bonne nuit"}
{"language":"de","GM":"Guten Morgen","GA":"Guten Tag","GE":"gute Nacht"}
{"language":"es","GM":"Buenos dias","GA": "buenas tardes","GE":"buenas tardes"}


listar base dato

-show dbs

crear o utilizar una db

-use saludo

-
-show collections


"""


"""

from pymongo import MongoClient
from pprint import pprint


client = MongoClient()


db = client['greeting']
 
collection = db['saludos']
 
data = collection.find_one({"language":"fr"})

print(type(data))
print(data)


GM = data['GM']
GA = data["GA"]
GE = data["GE"]

print(GM)
print(GA)
print(GE)



"""
from pyknow import *

class Greeting(Fact):
    pass

class Hora(Fact):
    pass

class Saludar(KnowledgeEngine):
    greeting = ""
    salution = ""
    
    def setGreeting(self, g):
        self.greeting = g
    
    def getGreeting(self):
        return self.greeting
        
    def getMessage(self):
        return self.getGreeting()
    

    @Rule(Greeting(hora = P(lambda hora: hora >= 0) & P(lambda hora: hora <= 11)))
    def morning(self):
        self.setGreeting("GM")

    @Rule(Greeting(hora = P(lambda hora: hora >= 12) & P(lambda hora: hora <= 17)))
    def afternoon(self):
        self.setGreeting("GA")
        
    @Rule(Greeting(hora = P(lambda hora: hora >= 18) & P(lambda hora: hora <= 23)))
    def evening(self):
        self.setGreeting("GE")
        
        
def get_audio(language, hora):
    watch('RULES', 'FACTS')
    nxm = Saludar()  
    nxm.reset()
    
    """
    language= "es"
    hora=2
    """
    nxm.declare(Greeting(hora=hora))
    nxm.run()
    nxm.facts
    greeting = nxm.getMessage()
    print(greeting)
    from pymongo import MongoClient
    client = MongoClient()
    db = client['greeting']
    collection = db['saludos']
    data = collection.find_one({"language": language})
    saludo = data[greeting]
    print(saludo)
    from gtts import gTTS
    tts = gTTS('hello usco 2018', lang="es")
    tts.save('hello.mp3')
    
    



from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World usco!'


@app.route("/mp3")
def streammp3():
    def generate():
        import datetime
        now = datetime.datatime.now()
        hora = now.hour
        print(hora)
        get_audio("fr",hora)
        with open("hello.mp3", "rb") as fogg:
            data = fogg.read(1024)
            while data:
                yield data
                data = fogg.read(1024)
                
    return Response(generate(), mimetype="audio/mp3")

if __name__ == "__main__":
    app.run(debug=True)
