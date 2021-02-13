from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {"hotel_id": "copacabana", "nome": "Copacabana Palace", 
    "qtd_estrelas": 5, "Diária": 1000.00, "cidade": "Rio de Janeiro"},
    {"hotel_id": "gravata", "nome": "Hotel Gravatá", 
    "qtd_estrelas": 3, "Diária": 400.00, "cidade": "Gravatá"},
    {"hotel_id": "noronha", "nome": "Hotel de Noronha", 
    "qtd_estrelas": 4, "Diária": 300.25, "cidade": "Fernando de Noronha"}
]

#Endpoint de listagem de todos os hoteis
class Hoteis(Resource):  
    def get(self):
        return {"hoteis": hoteis}

#Endpoint de criação, edição, remoção e pesquisa de hoteis
class Hotel(Resource): 
#So consigo receber dados como Json
#SO consigo usar com dicionario
#so consigo mandar como Json
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument("estrelas")
    argumentos.add_argument("diaria")
    argumentos.add_argument("cidade")
    #find by id
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
            return ("message: Hotel não encontrado!"), 404

    #create hotel
    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_object = HotelModel(hotel_id,**dados) #** dados acessa os dados acima (argumentos.add_argument")
        novo_hotel = hotel_object.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 200
        #status que representa "sucesso"
    
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        novo_hotel = {'hotel_id' : hotel_id, **dados}

        hotel = Hotel.find_hotel(hotel_id)

        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        
        hoteis.append(novo_hotel)
        return novo_hotel, 201
        #Status representa "criado"

    def delete(self, hotel_id):
        exist_hotel = hotel.find_hotel(hotel_id)
        if exist_hotel:
            hoteis.remove(exist_hotel)
            return ("message: Deleted successfully."), 200
        return ("message: ID not found."), 404


'''MODEL   ------->          CONTROLER     ------->        VIEW
             (PADRAO DE DESENVOLVIMENTO DE PROJETO)
camada de            camada de controle        camada de visualização
conexão com o        de acesso(validações,     do usuario (front-end)
banco de dados       requisições)                                     '''
#Model nao comunica com o VIEW