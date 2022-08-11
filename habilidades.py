from flask_restful import Resource
from flask import request
import json

lista_habilidades=['Python', 'Java', 'JavaScript', 'PHP', 'Fask']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados)
        return lista_habilidades 

class Habilidade(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id]=dados
        return lista_habilidades

    def delete(self, id):
        lista_habilidades.pop(id)
        mensagem ='habilidade deletada'
        return  {'status': 'Sucesso', 'mensagem':mensagem, 'dados': lista_habilidades}    
