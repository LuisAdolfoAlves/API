# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from resources.Library.hotel import Hoteis, Hotel

app = Flask(__name__) # Lugar onde coloca-se a rot(__name__)
api = Api(app)        #Cria o ambiente virtual

#Cruds = aplicações básicas no mercado
"""
C - Create (Post)
R - Read   (Get)
U - Update (Put)
D - Delete (Delete)
S - Search (Get)
"""

#Resource = conceito de comunicação com o flask 

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    app.run(debug=True)
