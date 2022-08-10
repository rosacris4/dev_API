import json
from urllib import response
from flask import Flask, jsonify, request

app = Flask(__name__)


tarefas=[
    {
        'id':0,
        'responsavel': 'Rosa',
        'tarefa': 'construir um API',
        'status': 'concluido'

    },
    {
        'id':1,
        'responsavel': 'Cristina',
        'tarefa': 'fazer conexão com a BD',
        'status': 'Pendente',

    }
]

@app.route('/admin', methods=['GET', 'POST'])

def gestaoTarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao= len(tarefas)
        dados['id']= posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])

    elif request.method == 'GET':
        return jsonify(tarefas)

@app.route('/admin/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def gastaoTarefas(id):
    if request.method == 'GET':
        try:
            response= tarefas[id]
        except IndexError:
            mensagem = 'tarefa não existe'
            response= {'status': 'error', 'mensagem ': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados= json.loads(request.data)
        tarefas[id]['status']= dados.get('status')
        
        return jsonify(dados)
    elif request.method == 'DELETE':
        tarefas.pop(id) 
        return jsonify({'status': 'sucesso', 'mensagem': 'tarefa deletada'})   

if __name__ == '__main__':
    app.run(debug=True)

