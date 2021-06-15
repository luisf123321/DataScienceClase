# -*- coding: utf-8 -*-

"""
Created on Tue Aug 28 17:37:47 2018

@author: LUISFERNANDO
"""
from flask import Flask, jsonify, request
from flask import json, Response


import re 
from pyknow import *

app = Flask(__name__)

class Producto(Fact):
    """
    Producto que ha comprado un cliente.

    >>> Producto(nombre="pepsi", tipo="refresco de cola", cantidad=1)

    """
    pass

class Cupon(Fact):
    """
    Cupón a generar para la próxima compra del cliente.

    >>> Cupon(tipo="2x1", producto="pepsi")
    
    """
    pass

class Promo(Fact):
    """
    Promoción vigente en el comercio.

    >>> Promo(tipo="2x1", **depende_de_la_promo)

    """
    pass

class Beneficio(Fact):
    """
    Define los beneficios que obtiene el comercio por cada producto.

    >>> Beneficio(nombre="pepsi", tipo="refresco de cola", ganancias=0.2)

    """
    pass

class OfertasNxM(KnowledgeEngine):
    @DefFacts()
    def carga_promociones_nxm(self):
        """
        Hechos iniciales.
        
        Genera las promociones vigentes
        """
        
        
        yield Promo(tipo="2x1", producto="Dodot")
        yield Promo(tipo="2x1", producto="Leche Pascual")
        yield Promo(tipo="3x2", producto="Pilas AAA")
    
        """""
        import json
        with open("promociones.json", "r") as read_file:
            data = json.load(read_file)
        promociones = data['promo']

        for p in promociones: 
            yield Promo(tipo=p['tipo'], producto=p['producto'])
    """
    
    @Rule(Promo(tipo=MATCH.t & P(lambda t: re.match(r"\d+x\d+", t)),
                producto=MATCH.p),
          Producto(nombre=MATCH.p))
    def oferta_nxm(self, t, p):
        """
        Sabemos que el cliente volverá para aprovechar
        la promoción, ya que hoy ha comprado el producto.
        """
        self.declare(Cupon(tipo=t, producto=p))
        

@app.route('/facturar')
def facturar():
    
    #return 'Hello, World!'
    
    watch('RULES', 'FACTS')
    nxm = OfertasNxM()

    nxm.reset()

    nxm.declare(Producto(nombre="Dodot"))
    nxm.declare(Producto(nombre="Agua Mineral"))
    nxm.declare(Producto(nombre="Pilas AAA"))

    nxm.run()
    cupones = nxm.facts
    print(type(cupones))
    
    for i in cupones:
        print(type(i),i)

    return jsonify(exito='true', mensaje="cupones")




        
@app.route('/hello')
def hello_world():
    #return 'Hello, World!'
    return jsonify(id=1, nombre="pepsi")

@app.route('/listar')
def listar():
    lista = []
    lista.append({"id":1,"nombre":"pepsi"})
    lista.append({"id":2,"nombre":"ñññññ"})
    lista.append({"id":3,"nombre":"trapeador"})
    r = Response(response=json.drumps(lista), status=200, minetype="application/json")
    r.headers["Content-Type"] = "text/json; charset:utf-8"
    #return 'Hello, World!'
    return r

@app.route('/procesar', methods=['GET', 'POST'])
def procesar():
    
    content = request.json
    print(content['id'])
    print(content['nombre'])
    print(content['precio'])
    #return 'Hello, World!'
    return jsonify({"datos":content})

@app.route('/generar', methods=['POST'])
def generar():
    
    content = request.json
    print(type(content))
    promociones = content['promo']
    
    for row in promociones:
        tipo = row['tipo']
        producto = row['producto']
        print(tipo,producto)
    #return 'Hello, World!'
    return jsonify({"datos":content})




if __name__ == '__main__':
    app.run()
