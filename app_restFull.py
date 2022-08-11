from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, Habilidade, lista_habilidades
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
         lista_dados= dados.get('habilidades')
         cont=0
         for i in range(0 ,len(lista_habilidades)):
            for j in range(0, len(lista_dados)):
                if lista_habilidades[i] == lista_dados[j]:
                    cont+=1
         if(cont == 2):
            posicao= len(desenvolvedores)
            dados['id']= posicao
            desenvolvedores.append(dados)
            return desenvolvedores[posicao] 
                   
         elif(cont == 1):
            return {'status': 'erro', 'mensagem': 'só uma das habilidades existe na lista de habilidade'}
             
        
         elif(cont == 0):
            return {'status': 'erro', 'mensagem': 'nenhuma das habilidades existe na lista de habilidade'}
             
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