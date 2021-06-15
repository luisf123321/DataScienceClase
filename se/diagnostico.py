# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:01:19 2018

@author: LUISFERNANDO
"""
from flask import Flask, jsonify, request
from random import choice
from pyknow import *

"""
100 Diabetes
101 Orina constante
102 sed 
103
"""
app = Flask(__name__)

class Sintoma(Fact):
    """Info about the traffic light."""
    pass

class Enfermedad(Fact):
    """Info about the traffic light."""
    pass

watch('RULES', 'FACTS')
class DiagnosticoEnfermedad(KnowledgeEngine):
    
    

    @Rule(AND(Sintoma(codigo=101),
          Sintoma(codigo=102),
          Sintoma(codigo=103)
    ))
    def regla1(self):
        self.declare(Enfermedad(codigo=100, nombre='Diabetes'))
        
    @Rule(AND(Sintoma(codigo=201),
          Sintoma(codigo=202),
          Sintoma(codigo=203)
    ))
    def regla2(self):
        self.declare(Enfermedad(codigo=200, nombre='colesterol'))
        
    @Rule(AND(Sintoma(codigo=301),
          Sintoma(codigo=302),
          Sintoma(codigo=303)
    ))
    def regla3(self):
        self.declare(Enfermedad(codigo=300, nombre='gastritis'))
        
@app.route('/diagnosticar', methods=['POST'])
def diagnosticar():
    
    data_json = request.json
    sintomas = data_json['sintomas']
    
    print(sintomas)
    watch('RULES', 'FACTS')

    engine = DiagnosticoEnfermedad()
    engine.reset()
    
    for code in sintomas:
        engine.declare(Sintoma(codigo=code))
    
    
    engine.run()
    
    
    
    diagnostico = engine.facts
    
  
    
    for d in diagnostico:
        if(type(diagnostico[d]) == Enfermedad):
            print(diagnostico[d]['codigo'])
            print(diagnostico[d]['nombre'])
            
            codigo = diagnostico[d]['codigo']
            nombre = diagnostico[d]['nombre']
            
    respuesta = {'codigo':codigo,'nombre':nombre}
    print(respuesta)
    
    return jsonify(respuesta)
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

