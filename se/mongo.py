# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:44:14 2018

@author: LUISFERNANDO
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
        
        
watch('RULES', 'FACTS')
nxm = Saludar()  
nxm.reset()


for i in range(0,24):
    print(i)
    nxm.declare(Greeting(hora=i))
    nxm.run()
    #nxm.facts      
    message = nxm.getMessage()
    print(message)
    




def getGreetingLanguage(self, language, greeting):
    from pyknow import MongoClient
    client = MongoClient()
    db = client['saludo']
    collection = db['saludos']
    data = collection.find_one({"language": language})
    greeting_text = data[greeting]
    return greeting_text
    watch('RULES', 'FACTS')
    nxm = Saludar()  
    nxm.reset()
        
    language = "it"
    hora=10
    nxm.declare(Greeting(hora=hora))
    nxm.run()
    nxm.facts
    greeting = nxm.getMessage()
    print(greeting)
    greeting_text = nxm.getGreetingLanguage(language, greeting)
    print(greeting_text)
    from gtts import gTTS
    tts= gTTS(greeting_text, lang=language)
    tts.save('hello.mp3')

from flask import Flask, Response
app = Flask(__name__)
@app.route("/mp3")
def streammp3():
        def generate():
            with open("hello.mp3","rb") as fogg:
                data=fogg.read(1024)
                while data:
                    yield data 
                    data = fogg.read(1024)
        return Response(generate(), mimetype="audio/mp3")
if __name__=="__main__":
    app.run(debug=True)

