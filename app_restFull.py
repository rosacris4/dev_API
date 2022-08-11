from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, Habilidade
import json

app= Flask(__name__)
api= Api(app)

desenvolvedores=[
    {   
        'id': 0,
        'nome': 'Rosa',
        'habilidades':['javascript', 'python']
    },
     {  
        'id': 1,
        'nome': 'Cristina',
        'habilidades':['java', 'PHP']
    }
]
class Desenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
         dados = json.loads(request.data)
         posicao= len(desenvolvedores)
         dados['id']= posicao
         desenvolvedores.append(dados)
         return desenvolvedores[posicao]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem= 'Desenvolvedor de ID {} não existe'.format(id)
            response ={'status':'erro', 'mensagem':mensagem} 
        return response

    def put(self, id):
        dados= json.loads(request.data)
        desenvolvedores[id]=dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'menssagem': 'registro excluido'}    
    
api.add_resource(Desenvolvedores, '/dev/')
api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(Habilidades, '/habilidades')
api.add_resource(Habilidade, '/habilidades/<int:id>')
if __name__ == '__main__':
    app.run(debug=True)